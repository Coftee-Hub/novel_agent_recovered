# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/agents/schemas.py
# 来源   : schemas.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = 'architect 的输出契约。\n\n三层：卷大纲（人工确认）→ 章细纲 → 场景规格。\nSceneSpec 是 architect 与 writer 之间的接口，字段设计直接决定正文质量：\n写作时 writer 只看到本 scene 的 spec + 上一 scene 结尾，看不到全章，\n所以凡是 writer 需要知道的，都必须在 spec 里说清楚。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'architect 的输出契约。\n\n三层：卷大纲（人工确认）→ 章细纲 → 场景规格。\nSceneSpec 是 architect 与 writer 之间的接口，字段设计直接决定正文质量：\n写作时 writer 只看到本 scene 的 spec + 上一 scene 结尾，看不到全章，\n所以凡是 writer 需要知道的，都必须在 spec 里说清楚。\n',
    6: 'SceneSpec',
    8: 'DebtPlan',
    10: 'ChapterOutline',
    12: 'RelationTarget',
    14: 'TurningPoint',
    16: 'VolumeOutline',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('SceneSpec', 0): 'SceneSpec',
    ('SceneSpec', 1): '一个场景的完整规格。writer 按这个写，gate 与 judge 按这个验。',
    ('SceneSpec', 2): 'str',
    ('SceneSpec', 3): 'id',
    ('SceneSpec', 4): 'where',
    ('SceneSpec', 5): 'when',
    ('SceneSpec', 7): 'list[str]',
    ('SceneSpec', 8): 'present',
    ('SceneSpec', 9): 'goal',
    ('SceneSpec', 10): 'entry_emotion',
    ('SceneSpec', 11): 'exit_emotion',
    ('SceneSpec', 12): 'beat_type',
    ('SceneSpec', 13): 'L0',
    ('SceneSpec', 14): 'IntimacyLevel',
    ('SceneSpec', 15): 'intimacy_level',
    ('SceneSpec', 19): 'int',
    ('SceneSpec', 20): 'target_words',
    ('SceneSpec', 22): 'must_include',
    ('SceneSpec', 23): 'must_not',
    ('SceneSpec', 24): 'after',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'SceneSpec',
    ('_emotion_must_shift', 0): '情绪没有变化的场景，在言情里就是废戏。\n\n这条在 architect 出图时就拦住，比等 judge 打回便宜得多。\n',
    ('_emotion_must_shift', 1): '场景 ',
    ('_emotion_must_shift', 2): ' 的起止情绪相同（',
    ('_emotion_must_shift', 3): '）—— 没有情绪推进的场景应当合并或删除',
    ('DebtPlan', 0): 'DebtPlan',
    ('DebtPlan', 1): '本章要埋或要回收的情感债。',
    ('DebtPlan', 2): 'str',
    ('DebtPlan', 3): 'debt_id',
    ('DebtPlan', 4): "Literal['plant', 'pay']",
    ('DebtPlan', 5): 'action',
    ('DebtPlan', 7): 'DebtKind | None',
    ('DebtPlan', 8): 'kind',
    ('DebtPlan', 9): 'desc',
    ('DebtPlan', 10): 'int | None',
    ('DebtPlan', 11): 'due_by_ch',
    ('DebtPlan', 12): 'after',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'DebtPlan',
    ('_plant_needs_deadline', 0): 'plant',
    ('_plant_needs_deadline', 1): '情感债 ',
    ('_plant_needs_deadline', 2): ' 是埋设（plant），必须给出 kind 与 due_by_ch —— 没有到期章就无法机械检查是否忘了回收',
    ('ChapterOutline', 0): 'ChapterOutline',
    ('ChapterOutline', 1): 'int',
    ('ChapterOutline', 2): 'ch',
    ('ChapterOutline', 3): 'str',
    ('ChapterOutline', 4): 'title',
    ('ChapterOutline', 5): 'Stage',
    ('ChapterOutline', 6): 'stage',
    ('ChapterOutline', 7): 'intent',
    ('ChapterOutline', 9): 'list[SceneSpec]',
    ('ChapterOutline', 10): 'scenes',
    ('ChapterOutline', 11): 'hook',
    ('ChapterOutline', 13): 'list[DebtPlan]',
    ('ChapterOutline', 14): 'debts',
    ('ChapterOutline', 17): 'after',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'ChapterOutline',
    ('_scene_ids_unique', 0): '第 ',
    ('_scene_ids_unique', 1): ' 章存在重复的场景 id：',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('to_markdown', 0): '给人看的渲染。\n\n细纲此前只活在内存里，跑完就没了 —— 而第 2 章连续三次卡在对话占比\n下限时，真正要查的恰恰是它（三个场景全是独处，再怎么要求 writer\n也变不出对话）。落盘之后才谈得上"写之前先看一眼细纲"。\n',
    ('to_markdown', 1): '## 第 ',
    ('to_markdown', 2): ' 章 ',
    ('to_markdown', 3): '（',
    ('to_markdown', 4): ' · ',
    ('to_markdown', 5): ' 场 · 目标 ',
    ('to_markdown', 6): ' 字）',
    ('to_markdown', 8): '**本章意图**：',
    ('to_markdown', 9): '### ',
    ('to_markdown', 10): '. `',
    ('to_markdown', 11): '` ',
    ('to_markdown', 12): '- 在场：',
    ('to_markdown', 13): '、',
    ('to_markdown', 14): '　← 独处场，写不出对话',
    ('to_markdown', 15): '- 目标：',
    ('to_markdown', 16): '- 情绪：',
    ('to_markdown', 17): ' → **',
    ('to_markdown', 18): '**',
    ('to_markdown', 19): '- 节拍：',
    ('to_markdown', 20): '　亲密度 ',
    ('to_markdown', 21): '　目标 ',
    ('to_markdown', 22): ' 字',
    ('to_markdown', 23): '- 必须出现：',
    ('to_markdown', 24): '；',
    ('to_markdown', 25): '- 不许出现：',
    ('to_markdown', 26): '**章末钩子**：',
    ('to_markdown', 27): '**情感债**：',
    ('to_markdown', 28): '（第 ',
    ('to_markdown', 29): ' 章前回收）',
    ('to_markdown', 30): '- ',
    ('to_markdown', 31): 'plant',
    ('to_markdown', 32): '埋',
    ('to_markdown', 33): '收',
    ('to_markdown', 34): ' [',
    ('to_markdown', 35): '] ',
    ('RelationTarget', 0): 'RelationTarget',
    ('RelationTarget', 1): '本卷要把某段关系推到哪一步。',
    ('RelationTarget', 2): 'str',
    ('RelationTarget', 3): 'a_id',
    ('RelationTarget', 4): 'b_id',
    ('RelationTarget', 5): 'RelationStage',
    ('RelationTarget', 6): 'from_stage',
    ('RelationTarget', 7): 'to_stage',
    ('RelationTarget', 8): 'via',
    ('TurningPoint', 0): 'TurningPoint',
    ('TurningPoint', 1): 'int',
    ('TurningPoint', 2): 'ch',
    ('TurningPoint', 3): 'str',
    ('TurningPoint', 4): 'what',
    ('VolumeOutline', 0): 'VolumeOutline',
    ('VolumeOutline', 1): '卷大纲 —— **唯一需要你点头的东西**。\n\n刻意做得短：你要能在两分钟内判断"这个方向我接受不接受"。\n细到场景的东西放 ChapterOutline，不占用你的注意力。\n',
    ('VolumeOutline', 2): 'int',
    ('VolumeOutline', 3): 'volume',
    ('VolumeOutline', 4): 'Stage',
    ('VolumeOutline', 5): 'stage',
    ('VolumeOutline', 6): 'ch_start',
    ('VolumeOutline', 7): 'ch_end',
    ('VolumeOutline', 8): 'str',
    ('VolumeOutline', 9): 'premise',
    ('VolumeOutline', 11): 'list[RelationTarget]',
    ('VolumeOutline', 12): 'relation_targets',
    ('VolumeOutline', 13): 'list[TurningPoint]',
    ('VolumeOutline', 14): 'turning_points',
    ('VolumeOutline', 16): 'list[str]',
    ('VolumeOutline', 17): 'debts_to_plant',
    ('VolumeOutline', 18): 'debts_to_pay',
    ('VolumeOutline', 19): 'new_characters',
    ('VolumeOutline', 20): 'ends_on',
    ('VolumeOutline', 23): 'after',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'VolumeOutline',
    ('_range_sane', 0): '第 ',
    ('_range_sane', 1): ' 卷章节区间颠倒：',
    ('_range_sane', 2): '-',
    ('_range_sane', 3): '转折点在第 ',
    ('_range_sane', 4): ' 章，超出本卷区间 ',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('to_markdown', 0): '给人看的渲染 —— 这是你在确认断点上实际读到的东西。',
    ('to_markdown', 1): '## 第 ',
    ('to_markdown', 2): ' 卷（第 ',
    ('to_markdown', 3): '-',
    ('to_markdown', 4): ' 章，共 ',
    ('to_markdown', 5): ' 章 · ',
    ('to_markdown', 6): '）',
    ('to_markdown', 8): '**主线**：',
    ('to_markdown', 9): '**关系推进**：',
    ('to_markdown', 10): '- ',
    ('to_markdown', 11): ' ↔ ',
    ('to_markdown', 12): '：',
    ('to_markdown', 13): ' → **',
    ('to_markdown', 14): '**（',
    ('to_markdown', 15): '**转折点**：',
    ('to_markdown', 18): '- 第 ',
    ('to_markdown', 19): ' 章：',
    ('to_markdown', 20): '**埋**：',
    ('to_markdown', 21): '；',
    ('to_markdown', 22): '**收**：',
    ('to_markdown', 23): '**新人物**：',
    ('to_markdown', 24): '、',
    ('to_markdown', 25): '**卷末停在**：',
}

# ───────────── 还原后的源码 ─────────────
from typing import Literal

from pydantic import BaseModel, Field, model_validator

# TODO(重建): Stage / RelationStage / DebtKind / IntimacyLevel 枚举类型在原源码中
# 由外部模块提供，加密前的 .pyc 只保存了名字（字符串注解）。恢复编译不受影响；
# 运行时导入需要补上定义。IntimacyLevel 的取值在 SceneSpec 默认值中可见为 "L0"
# （prompts.py 提到 L0/L1/L2 三档）。


class SceneSpec(BaseModel):
    """一个场景的完整规格。writer 按这个写，gate 与 judge 按这个验。"""

    id: str
    where: str
    when: str
    present: list[str] = Field(min_length=1)
    goal: str
    entry_emotion: str
    exit_emotion: str
    beat_type: str
    intimacy_level: IntimacyLevel = "L0"
    target_words: int = Field(ge=400, le=2000)
    must_include: list[str] = Field(default_factory=list)
    must_not: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _emotion_must_shift(self) -> SceneSpec:
        """情绪没有变化的场景，在言情里就是废戏。

        这条在 architect 出图时就拦住，比等 judge 打回便宜得多。
        """
        if self.entry_emotion.strip() == self.exit_emotion.strip():
            raise ValueError(
                f"场景 {self.id} 的起止情绪相同（{self.entry_emotion!r}）—— 没有情绪推进的场景应当合并或删除"
            )
        return self


class DebtPlan(BaseModel):
    """本章要埋或要回收的情感债。"""

    debt_id: str
    action: Literal["plant", "pay"]
    kind: DebtKind | None = None
    desc: str
    due_by_ch: int | None = None

    @model_validator(mode="after")
    def _plant_needs_deadline(self) -> DebtPlan:
        if self.action == "plant" and (self.due_by_ch is None or self.kind is None):
            raise ValueError(
                f"情感债 {self.debt_id} 是埋设（plant），必须给出 kind 与 due_by_ch —— 没有到期章就无法机械检查是否忘了回收"
            )
        return self


class ChapterOutline(BaseModel):
    ch: int
    title: str
    stage: Stage
    intent: str
    scenes: list[SceneSpec] = Field(min_length=2, max_length=4)
    hook: str
    debts: list[DebtPlan] = Field(default_factory=list)

    @property
    def target_words(self) -> int:
        return sum(s.target_words for s in self.scenes)

    @model_validator(mode="after")
    def _scene_ids_unique(self) -> ChapterOutline:
        ids = [s.id for s in self.scenes]
        if len(set(ids)) != len(ids):
            raise ValueError(f"第 {self.ch} 章存在重复的场景 id：{ids}")
        return self

    def to_markdown(self) -> str:
        """给人看的渲染。

        细纲此前只活在内存里，跑完就没了 —— 而第 2 章连续三次卡在对话占比
        下限时，真正要查的恰恰是它（三个场景全是独处，再怎么要求 writer
        也变不出对话）。落盘之后才谈得上"写之前先看一眼细纲"。
        """
        lines = [
            f"## 第 {self.ch} 章 {self.title}（{self.stage} · {len(self.scenes)} 场 · 目标 {self.target_words} 字）",
            "",
            f"**本章意图**：{self.intent}",
            "",
        ]
        for n, s in enumerate(self.scenes, 1):
            lines += [
                f"### {n}. `{s.id}` {s.where} · {s.when}",
                "",
                f"- 在场：{'、'.join(s.present)}"
                + ("　← 独处场，写不出对话" if len(s.present) == 1 else ""),
                f"- 目标：{s.goal}",
                f"- 情绪：{s.entry_emotion} → **{s.exit_emotion}**",
                f"- 节拍：{s.beat_type}　亲密度 {s.intimacy_level}　目标 {s.target_words} 字",
            ]
            if s.must_include:
                lines.append(f"- 必须出现：{'；'.join(s.must_include)}")
            if s.must_not:
                lines.append(f"- 不许出现：{'；'.join(s.must_not)}")
            lines.append("")
        lines.append(f"**章末钩子**：{self.hook}")
        if self.debts:
            lines += ["", "**情感债**："]
            for d in self.debts:
                due = f"（第 {d.due_by_ch} 章前回收）" if d.due_by_ch else ""
                lines.append(f"- {'埋' if d.action == 'plant' else '收'} [{d.debt_id}] {d.desc}{due}")
        return "\n".join(lines)


class RelationTarget(BaseModel):
    """本卷要把某段关系推到哪一步。"""

    a_id: str
    b_id: str
    from_stage: RelationStage
    to_stage: RelationStage
    via: str


class TurningPoint(BaseModel):
    ch: int
    what: str


class VolumeOutline(BaseModel):
    """卷大纲 —— **唯一需要你点头的东西**。

    刻意做得短：你要能在两分钟内判断"这个方向我接受不接受"。
    细到场景的东西放 ChapterOutline，不占用你的注意力。
    """

    volume: int
    stage: Stage
    ch_start: int
    ch_end: int
    premise: str
    relation_targets: list[RelationTarget] = Field(min_length=1)
    turning_points: list[TurningPoint] = Field(min_length=1)
    debts_to_plant: list[str] = Field(default_factory=list)
    debts_to_pay: list[str] = Field(default_factory=list)
    new_characters: list[str] = Field(default_factory=list)
    ends_on: str

    @property
    def chapter_count(self) -> int:
        return self.ch_end - self.ch_start + 1

    @model_validator(mode="after")
    def _range_sane(self) -> VolumeOutline:
        if self.ch_end < self.ch_start:
            raise ValueError(f"第 {self.volume} 卷章节区间颠倒：{self.ch_start}-{self.ch_end}")
        for tp in self.turning_points:
            if not (self.ch_start <= tp.ch <= self.ch_end):
                raise ValueError(
                    f"转折点在第 {tp.ch} 章，超出本卷区间 {self.ch_start}-{self.ch_end}"
                )
        return self

    def to_markdown(self) -> str:
        """给人看的渲染 —— 这是你在确认断点上实际读到的东西。"""
        lines = [
            f"## 第 {self.volume} 卷（第 {self.ch_start}-{self.ch_end} 章，共 {self.chapter_count} 章 · {self.stage}）",
            "",
            f"**主线**：{self.premise}",
            "",
            "**关系推进**：",
        ]
        for r in self.relation_targets:
            lines.append(f"- {r.a_id} ↔ {r.b_id}：{r.from_stage} → **{r.to_stage}**（{r.via}）")
        lines += ["", "**转折点**："]
        for tp in sorted(self.turning_points, key=lambda x: x.ch):
            lines.append(f"- 第 {tp.ch} 章：{tp.what}")
        if self.debts_to_plant:
            lines += ["", f"**埋**：{'；'.join(self.debts_to_plant)}"]
        if self.debts_to_pay:
            lines += ["", f"**收**：{'；'.join(self.debts_to_pay)}"]
        if self.new_characters:
            lines += ["", f"**新人物**：{'、'.join(self.new_characters)}"]
        lines += ["", f"**卷末停在**：{self.ends_on}"]
        return "\n".join(lines)
