"""质量评审 —— 抓 gate 抓不到的问题。

分工很清楚：
  gate  抓**可量化**的 —— 字数、标点、句长分布、比喻密度
  judge 抓**要读懂才知道**的 —— 这段对话有没有潜台词、人物有没有做出
        自己绝不会做的事、情绪推进是不是真的落在了具体事件上

judge 的产出必须**定位到具体场景**。笼统的「再细腻些」没法执行，
修订环拿到这种意见只能整章重写，那就失去了分场景生成的全部意义。
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import Field

from ..llm import LLMClient, Prompt
from ..skills import SkillLibrary
from ..state import render as render_bible
from ..state.schema import Base, StoryState
from .schemas import ChapterOutline

Dimension = Literal[
    "emotional_progress",   # 情绪推进：关系真的被推动了吗
    "character_consistency",# 人物一致性：口吻与行为符合人物卡吗
    "dialogue_quality",     # 对话质量：有潜台词吗，还是在互相交代背景
    "sensory_detail",       # 感官与细节：具体可感，还是概念化叙述
    "logic_consistency",    # 逻辑与设定：时间线、地点、已知事实无冲突
    "cliche_avoidance",     # 陈词滥调：有没有落进俗套
    "chapter_hook",         # 章末钩子：有让人看下一章的动力吗
]

LABELS: dict[str, str] = {
    "emotional_progress": "情绪推进",
    "character_consistency": "人物一致性",
    "dialogue_quality": "对话质量",
    "sensory_detail": "感官与细节",
    "logic_consistency": "逻辑与设定",
    "cliche_avoidance": "陈词滥调规避",
    "chapter_hook": "章末钩子",
}


class DimensionScore(Base):
    dimension: Dimension
    score: int = Field(ge=1, le=5)
    reason: str  # 为什么是这个分，要具体


class RevisionNote(Base):
    """一条可执行的修改意见。"""

    scene_id: str
    problem: str  # 哪里不对
    fix: str      # 具体怎么改 —— 不是"再细腻些"，是"把X换成Y"


class JudgeVerdict(Base):
    scores: list[DimensionScore] = Field(min_length=7, max_length=7)
    notes: list[RevisionNote] = Field(default_factory=list)
    overall: str

    @property
    def total(self) -> int:
        return sum(s.score for s in self.scores)

    def by_dimension(self) -> dict[str, DimensionScore]:
        return {s.dimension: s for s in self.scores}

    def failing(self, floor: int) -> list[DimensionScore]:
        return sorted((s for s in self.scores if s.score < floor),
                      key=lambda s: s.score)

    def passed(self, *, min_per_dimension: int, min_total: int) -> bool:
        return self.total >= min_total and not self.failing(min_per_dimension)

    def render(self, *, min_per_dimension: int = 3, min_total: int = 24) -> str:
        ok = self.passed(min_per_dimension=min_per_dimension, min_total=min_total)
        lines = [f"judge: {'通过' if ok else '未通过'}  总分 {self.total}/35"]
        for s in sorted(self.scores, key=lambda x: x.score):
            mark = "✓" if s.score >= min_per_dimension else "✗"
            lines.append(f"  {mark} {LABELS.get(s.dimension, s.dimension):8} "
                         f"{s.score}/5  {s.reason}")
        if self.notes:
            lines.append("  修改意见：")
            lines += [f"    [{n.scene_id}] {n.problem} → {n.fix}" for n in self.notes]
        return "\n".join(lines)


JUDGE_ROLE = """\
你是一位小说编辑，负责审稿。你不改稿，只指出问题并给出可执行的改法。

## 你要抓的和不用管的

程序已经检查过字数、标点、句长分布、比喻密度这些**能数出来**的东西，
不用你操心。你要抓的是**必须读懂才能发现**的问题：

- 这段对话是在推进关系，还是在互相交代读者已经知道的信息？
- 人物有没有做出以他的性格绝不会做的事？说话口吻是不是他的？
- 「关系推进了」是落在一个具体事件上，还是只是叙述者宣布了一下？
- 有没有落进俗套？（不是"用了雨天"就叫俗套，是"用雨天的方式和一万本书一样"）

## 打分

七个维度各 1-5 分。**3 分是及格线，意思是"能用但不出彩"**。
不要滥用 4-5 分 —— 如果一章七项全是 4 分以上，通常说明你没读仔细。

给分必须说出**具体依据**，指向文本里的某个位置。
"这一章情绪推进不足" 是废话；
"第二场她从戒备到动摇，但转变发生在她自己的一段心理活动里，
 没有任何外部事件触发" 才是评审。

## 修改意见

每条意见必须绑定到一个**场景 id**，并且给出**具体改法**。

不合格：「对话可以更有层次」
合格：「ch012_s2 里两人在解释各自的时间安排，信息读者已经知道。
       删掉这段，改成她问一个明知答案的问题，让他被迫回答第二遍」

如果某一场没有问题，就不要为它编一条意见。宁可少写。
"""


class Judge:
    def __init__(self, client: LLMClient, skills_dir: str | Path,
                 *, min_per_dimension: int = 3, min_total: int = 24) -> None:
        self.client = client
        self.skills = SkillLibrary(skills_dir)
        self.min_per_dimension = min_per_dimension
        self.min_total = min_total

    def system_core(self) -> str:
        # 评审要按同一套标准，所以共享 writer 关心的那几份 skill
        extra = self.skills.compose(
            ["cliche_blacklist", "dialogue", "intimacy_levels"], strict=False
        )
        return f"{JUDGE_ROLE}\n\n---\n\n{extra}" if extra else JUDGE_ROLE

    def review(self, state: StoryState, outline: ChapterOutline, text: str) -> JudgeVerdict:
        specs = "\n".join(
            f"- {s.id}｜{s.where}｜目标：{s.goal}｜"
            f"情绪 {s.entry_emotion} → {s.exit_emotion}｜{s.beat_type}"
            for s in outline.scenes
        )
        instruction = (
            f"审第 {outline.ch} 章《{outline.title}》。\n\n"
            f"本章意图：{outline.intent}\n"
            f"章末钩子应当是：{outline.hook}\n\n"
            f"场景规格（对照检查每一场是否达成）：\n{specs}\n\n"
            f"<正文>\n{text}\n</正文>"
        )
        result = self.client.parse(
            "judge",
            Prompt(
                system_core=self.system_core(),
                bible=f"<设定集>\n{render_bible(state)}\n</设定集>" if state.characters else "",
                instruction=instruction,
            ),
            JudgeVerdict,
        )
        return result.parsed  # type: ignore[return-value]
