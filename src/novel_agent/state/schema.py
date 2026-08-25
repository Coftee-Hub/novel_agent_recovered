# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/state/schema.py
# 来源   : schema.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '故事状态的类型定义 —— 全书唯一事实源。\n\n设计要点：**跨阶段不变的属性挂在 Character 上，只有 arcs 随阶段变**。\n这不是风格偏好，而是一道结构性约束：archivist 提交的 patch 在类型上\n就够不到 core_wound / speech_habits / value_line，因此"时间一跳、\n人物像换了个人"这个跨阶段言情最常见的崩法，被类型系统挡住了。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '故事状态的类型定义 —— 全书唯一事实源。\n\n设计要点：**跨阶段不变的属性挂在 Character 上，只有 arcs 随阶段变**。\n这不是风格偏好，而是一道结构性约束：archivist 提交的 patch 在类型上\n就够不到 core_wound / speech_habits / value_line，因此"时间一跳、\n人物像换了个人"这个跨阶段言情最常见的崩法，被类型系统挡住了。\n',
    6: 'Base',
    8: 'CharacterArc',
    10: 'Character',
    12: 'Relationship',
    14: 'EmotionalDebt',
    16: 'TimelinePoint',
    18: 'UsedBeat',
    20: 'ChapterSummary',
    22: 'VolumeSummary',
    24: 'StoryState',
    26: 'CharacterArcUpdate',
    28: 'StatePatch',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Base', 0): 'Base',
    ('Base', 1): 'forbid',
    ('Base', 3): 'after',
    ('_normalize_punctuation', 0): '把所有中文字符串字段的标点规范化。\n\n为什么放在 schema 层而不是只查正文：卷大纲、人物卡、章节摘要都会\n进入 writer 的上下文。实测一份卷大纲里有 44 处半角逗号 —— writer\n每写一个场景都会看到 44 个错误示范，而 format_spec 同时在要求全角。\n与其事后检查，不如在数据进入系统时就统一口径。\n\n只在紧邻汉字时转换，所以 id、英文、数字不受影响。\n',
    ('CharacterArc', 0): 'CharacterArc',
    ('CharacterArc', 1): '人物在某个人生阶段的切片。只有这一层能随阶段变。',
    ('CharacterArc', 2): 'Stage',
    ('CharacterArc', 3): 'stage',
    ('CharacterArc', 5): 'int',
    ('CharacterArc', 6): 'age',
    ('CharacterArc', 7): 'str',
    ('CharacterArc', 8): 'identity',
    ('CharacterArc', 9): 'outer_goal',
    ('CharacterArc', 10): 'inner_want',
    ('CharacterArc', 11): 'status',
    ('Character', 0): 'Character',
    ('Character', 1): 'str',
    ('Character', 2): 'id',
    ('Character', 3): 'name',
    ('Character', 5): 'list[str]',
    ('Character', 6): 'aliases',
    ('Character', 8): 'core_traits',
    ('Character', 9): 'speech_habits',
    ('Character', 10): 'core_wound',
    ('Character', 11): 'value_line',
    ('Character', 12): 'list[CharacterArc]',
    ('Character', 13): 'arcs',
    ('Character', 15): 'voice_samples',
    ('__annotate__', 1): 'stage',
    ('__annotate__', 2): 'Stage',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'CharacterArc | None',
    ('Relationship', 0): 'Relationship',
    ('Relationship', 1): 'str',
    ('Relationship', 2): 'a_id',
    ('Relationship', 3): 'b_id',
    ('Relationship', 4): 'RelationStage',
    ('Relationship', 5): 'stage',
    ('Relationship', 6): 'tension_source',
    ('Relationship', 8): 'dict[str, int]',
    ('Relationship', 9): 'affection',
    ('Relationship', 10): 'int',
    ('Relationship', 11): 'last_advanced_ch',
    ('Relationship', 12): 'list[str]',
    ('Relationship', 13): 'unresolved',
    ('__annotate__', 1): 'v',
    ('__annotate__', 2): 'dict[str, int]',
    ('__annotate__', 3): 'return',
    ('_bounded', 1): '好感度 ',
    ('_bounded', 2): '=',
    ('_bounded', 3): ' 越界，应在 0-100',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'tuple[str, str]',
    ('key', 0): '无向对的规范化键，避免 (A,B) 与 (B,A) 变成两条记录。',
    ('EmotionalDebt', 0): 'EmotionalDebt',
    ('EmotionalDebt', 1): 'str',
    ('EmotionalDebt', 2): 'id',
    ('EmotionalDebt', 3): 'DebtKind',
    ('EmotionalDebt', 4): 'kind',
    ('EmotionalDebt', 5): 'desc',
    ('EmotionalDebt', 6): 'int',
    ('EmotionalDebt', 7): 'planted_ch',
    ('EmotionalDebt', 8): 'due_by_ch',
    ('EmotionalDebt', 9): 'open',
    ('EmotionalDebt', 10): "Literal['open', 'paid', 'abandoned']",
    ('EmotionalDebt', 11): 'status',
    ('EmotionalDebt', 12): 'after',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'EmotionalDebt',
    ('_due_after_planted', 0): '情感债 ',
    ('_due_after_planted', 1): ' 的到期章 ',
    ('_due_after_planted', 2): ' 不晚于埋设章 ',
    ('__annotate__', 1): 'current_ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'bool',
    ('is_overdue', 0): 'open',
    ('TimelinePoint', 0): 'TimelinePoint',
    ('TimelinePoint', 1): 'int',
    ('TimelinePoint', 2): 'ch',
    ('TimelinePoint', 3): 'str',
    ('TimelinePoint', 4): 'when',
    ('TimelinePoint', 5): 'where',
    ('TimelinePoint', 7): 'list[str]',
    ('TimelinePoint', 8): 'present',
    ('UsedBeat', 0): 'UsedBeat',
    ('UsedBeat', 1): '已用桥段。写作前塞给 writer 当"禁止重复"清单。',
    ('UsedBeat', 2): 'str',
    ('UsedBeat', 3): 'beat_type',
    ('UsedBeat', 4): 'int',
    ('UsedBeat', 5): 'ch',
    ('UsedBeat', 6): 'one_line',
    ('ChapterSummary', 0): 'ChapterSummary',
    ('ChapterSummary', 1): 'int',
    ('ChapterSummary', 2): 'ch',
    ('ChapterSummary', 3): 'str',
    ('ChapterSummary', 4): 'title',
    ('ChapterSummary', 5): 'summary',
    ('ChapterSummary', 6): 'Stage',
    ('ChapterSummary', 7): 'stage',
    ('ChapterSummary', 8): 'word_count',
    ('VolumeSummary', 0): 'VolumeSummary',
    ('VolumeSummary', 1): 'int',
    ('VolumeSummary', 2): 'volume',
    ('VolumeSummary', 3): 'ch_start',
    ('VolumeSummary', 4): 'ch_end',
    ('VolumeSummary', 5): 'str',
    ('VolumeSummary', 6): 'summary',
    ('StoryState', 0): 'StoryState',
    ('StoryState', 1): '未命名',
    ('StoryState', 2): 'str',
    ('StoryState', 3): 'title',
    ('StoryState', 4): 'int',
    ('StoryState', 5): 'current_chapter',
    ('StoryState', 7): 'list[Character]',
    ('StoryState', 8): 'characters',
    ('StoryState', 9): 'list[Relationship]',
    ('StoryState', 10): 'relationships',
    ('StoryState', 11): 'list[EmotionalDebt]',
    ('StoryState', 12): 'debts',
    ('StoryState', 13): 'list[TimelinePoint]',
    ('StoryState', 14): 'timeline',
    ('StoryState', 15): 'list[UsedBeat]',
    ('StoryState', 16): 'used_beats',
    ('StoryState', 17): 'list[ChapterSummary]',
    ('StoryState', 18): 'chapter_summaries',
    ('StoryState', 19): 'list[VolumeSummary]',
    ('StoryState', 20): 'volume_summaries',
    ('__annotate__', 1): 'cid',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'Character | None',
    ('__annotate__', 1): 'a',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'b',
    ('__annotate__', 4): 'return',
    ('__annotate__', 5): 'Relationship | None',
    ('__annotate__', 1): 'current_ch',
    ('__annotate__', 2): 'int | None',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[EmotionalDebt]',
    ('overdue_debts', 0): '已过期但仍未回收的情感债 —— 防烂尾的核心检查，不需要 LLM。',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[EmotionalDebt]',
    ('open_debts', 0): 'open',
    ('__annotate__', 1): 'n',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[ChapterSummary]',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('compressed_through', 0): '已经被卷梗概覆盖到第几章。没有卷梗概时返回 0。',
    ('__annotate__', 1): 'cap',
    ('__annotate__', 2): 'int | None',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[ChapterSummary]',
    ('live_summaries', 0): '还需要逐章记住的那些摘要 —— 即尚未被卷梗概覆盖的部分。\n\n两层摘要的分界线就在这里：往卷读梗概（一段话），本卷读章摘要（逐章）。\n用"有没有被卷梗概覆盖"而不是"最近 N 章"来划界，是因为 N 是个与故事\n结构无关的数字：N=10 时，第 11 章一开始就再也看不到第 1 章，而那时\n本卷还没结束、卷梗概还没产生 —— 中间那段谁都不管。\n\n`cap` 是安全阀，不是设计的一部分：它一旦生效就说明某一卷末尾的压缩\n没做成，窗口在无限长大。调用方应当据此告警。\n',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[str]',
    ('CharacterArcUpdate', 0): 'CharacterArcUpdate',
    ('CharacterArcUpdate', 1): '只能新增/替换某人物的一个阶段切片。\n\n刻意不提供改 core_wound / speech_habits / value_line 的路径 ——\n人物内核跨阶段恒定，这是类型层面的保证，不靠提示词自觉。\n',
    ('CharacterArcUpdate', 2): 'str',
    ('CharacterArcUpdate', 3): 'character_id',
    ('CharacterArcUpdate', 4): 'CharacterArc',
    ('CharacterArcUpdate', 5): 'arc',
    ('StatePatch', 0): 'StatePatch',
    ('StatePatch', 1): 'archivist 读完一章后提交的增量。绝不整体重写 state。',
    ('StatePatch', 2): 'ChapterSummary',
    ('StatePatch', 3): 'chapter_summary',
    ('StatePatch', 5): 'list[Character]',
    ('StatePatch', 6): 'new_characters',
    ('StatePatch', 7): 'list[CharacterArcUpdate]',
    ('StatePatch', 8): 'arc_updates',
    ('StatePatch', 9): 'list[Relationship]',
    ('StatePatch', 10): 'relationship_updates',
    ('StatePatch', 11): 'list[EmotionalDebt]',
    ('StatePatch', 12): 'new_debts',
    ('StatePatch', 13): 'list[str]',
    ('StatePatch', 14): 'resolved_debt_ids',
    ('StatePatch', 15): 'list[TimelinePoint]',
    ('StatePatch', 16): 'timeline_points',
    ('StatePatch', 17): 'list[UsedBeat]',
    ('StatePatch', 18): 'used_beats',
    ('StatePatch', 20): 'VolumeSummary | None',
    ('StatePatch', 21): 'volume_summary',
}

# ───────────── 还原后的源码 ─────────────
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from novel_agent.corpus.ingest import normalize_punctuation

# TODO(重建): Stage / RelationStage / DebtKind 三个枚举类型在原源码中由
# 外部模块提供，加密前的 .pyc 只保存了它们的名字（字符串注解），定义本身
# 不在本仓库可还原的范围内。恢复编译不受影响；运行时导入需要补上定义。
# 可参照 test_state.py 的用法推断取值：Stage∈{大学,毕业过渡,职场}、
# RelationStage∈{好感,暧昧,确认,...}、DebtKind∈{误会,物件,...}。


class Base(BaseModel):
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def _normalize_punctuation(self):
        """把所有中文字符串字段的标点规范化。

        为什么放在 schema 层而不是只查正文：卷大纲、人物卡、章节摘要都会
        进入 writer 的上下文。实测一份卷大纲里有 44 处半角逗号 —— writer
        每写一个场景都会看到 44 个错误示范，而 format_spec 同时在要求全角。
        与其事后检查，不如在数据进入系统时就统一口径。

        只在紧邻汉字时转换，所以 id、英文、数字不受影响。
        """
        for name, value in self.__dict__.items():
            if isinstance(value, str) and value:
                fixed = normalize_punctuation(value)
                if fixed != value:
                    object.__setattr__(self, name, fixed)
            elif isinstance(value, list) and value and isinstance(value[0], str):
                object.__setattr__(self, name, [normalize_punctuation(x) for x in value])
        return self


class CharacterArc(BaseModel):
    """人物在某个人生阶段的切片。只有这一层能随阶段变。"""

    stage: Stage
    age: int = Field(ge=15, le=60)
    identity: str
    outer_goal: str
    inner_want: str
    status: str


class Character(BaseModel):
    id: str
    name: str
    aliases: list[str] = Field(default_factory=list)
    core_traits: list[str] = Field(min_length=3, max_length=5)
    speech_habits: str
    core_wound: str
    value_line: str
    arcs: list[CharacterArc] = Field(default_factory=list)
    voice_samples: list[str] = Field(default_factory=list, max_length=5)

    def arc_at(self, stage: Stage) -> CharacterArc | None:
        return next((a for a in self.arcs if a.stage == stage), None)


class Relationship(BaseModel):
    a_id: str
    b_id: str
    stage: RelationStage
    tension_source: str
    affection: dict[str, int] = Field(default_factory=dict)
    last_advanced_ch: int = 0
    unresolved: list[str] = Field(default_factory=list)

    @field_validator("affection")
    @classmethod
    def _bounded(cls, v: dict[str, int]) -> dict[str, int]:
        for who, score in v.items():
            if not (0 <= score <= 100):
                raise ValueError(f"好感度 {who}={score} 越界，应在 0-100")
        return v

    @property
    def key(self) -> tuple[str, str]:
        """无向对的规范化键，避免 (A,B) 与 (B,A) 变成两条记录。"""
        return tuple(sorted((self.a_id, self.b_id)))


class EmotionalDebt(BaseModel):
    id: str
    kind: DebtKind
    desc: str
    planted_ch: int
    due_by_ch: int
    status: Literal["open", "paid", "abandoned"] = "open"

    @model_validator(mode="after")
    def _due_after_planted(self) -> EmotionalDebt:
        if self.due_by_ch <= self.planted_ch:
            raise ValueError(
                f"情感债 {self.id} 的到期章 {self.due_by_ch} 不晚于埋设章 {self.planted_ch}"
            )
        return self

    def is_overdue(self, current_ch: int) -> bool:
        return self.status == "open" and current_ch > self.due_by_ch


class TimelinePoint(BaseModel):
    ch: int
    when: str
    where: str
    present: list[str] = Field(default_factory=list)


class UsedBeat(BaseModel):
    """已用桥段。写作前塞给 writer 当"禁止重复"清单。"""

    beat_type: str
    ch: int
    one_line: str


class ChapterSummary(BaseModel):
    ch: int
    title: str
    summary: str
    stage: Stage
    word_count: int


class VolumeSummary(BaseModel):
    volume: int
    ch_start: int
    ch_end: int
    summary: str


class StoryState(BaseModel):
    title: str = "未命名"
    current_chapter: int = 0
    characters: list[Character] = Field(default_factory=list)
    relationships: list[Relationship] = Field(default_factory=list)
    debts: list[EmotionalDebt] = Field(default_factory=list)
    timeline: list[TimelinePoint] = Field(default_factory=list)
    used_beats: list[UsedBeat] = Field(default_factory=list)
    chapter_summaries: list[ChapterSummary] = Field(default_factory=list)
    volume_summaries: list[VolumeSummary] = Field(default_factory=list)

    def character(self, cid: str) -> Character | None:
        return next((c for c in self.characters if c.id == cid), None)

    def relationship(self, a: str, b: str) -> Relationship | None:
        want = tuple(sorted((a, b)))
        return next((r for r in self.relationships if r.key == want), None)

    def overdue_debts(self, current_ch: int | None = None) -> list[EmotionalDebt]:
        """已过期但仍未回收的情感债 —— 防烂尾的核心检查，不需要 LLM。"""
        ch = current_ch if current_ch is not None else self.current_chapter
        return [d for d in self.debts if d.is_overdue(ch)]

    def open_debts(self) -> list[EmotionalDebt]:
        return [d for d in self.debts if d.status == "open"]

    def recent_summaries(self, n: int) -> list[ChapterSummary]:
        return sorted(self.chapter_summaries, key=lambda s: s.ch)[-n:]

    def compressed_through(self) -> int:
        """已经被卷梗概覆盖到第几章。没有卷梗概时返回 0。"""
        return max((v.ch_end for v in self.volume_summaries), default=0)

    def live_summaries(self, cap: int | None = None) -> list[ChapterSummary]:
        """还需要逐章记住的那些摘要 —— 即尚未被卷梗概覆盖的部分。

        两层摘要的分界线就在这里：往卷读梗概（一段话），本卷读章摘要（逐章）。
        用"有没有被卷梗概覆盖"而不是"最近 N 章"来划界，是因为 N 是个与故事
        结构无关的数字：N=10 时，第 11 章一开始就再也看不到第 1 章，而那时
        本卷还没结束、卷梗概还没产生 —— 中间那段谁都不管。

        `cap` 是安全阀，不是设计的一部分：它一旦生效就说明某一卷末尾的压缩
        没做成，窗口在无限长大。调用方应当据此告警。
        """
        start = self.compressed_through() + 1
        live = [s for s in sorted(self.chapter_summaries, key=lambda s: s.ch) if s.ch >= start]
        if cap and len(live) > cap:
            return live[-cap:]
        return live

    def used_beat_types(self) -> list[str]:
        seen: dict[str, None] = {}
        for beat in self.used_beats:
            seen.setdefault(beat.beat_type, None)
        return list(seen)


class CharacterArcUpdate(BaseModel):
    """只能新增/替换某人物的一个阶段切片。

    刻意不提供改 core_wound / speech_habits / value_line 的路径 ——
    人物内核跨阶段恒定，这是类型层面的保证，不靠提示词自觉。
    """

    character_id: str
    arc: CharacterArc


class StatePatch(BaseModel):
    """archivist 读完一章后提交的增量。绝不整体重写 state。"""

    chapter_summary: ChapterSummary
    new_characters: list[Character] = Field(default_factory=list)
    arc_updates: list[CharacterArcUpdate] = Field(default_factory=list)
    relationship_updates: list[Relationship] = Field(default_factory=list)
    new_debts: list[EmotionalDebt] = Field(default_factory=list)
    resolved_debt_ids: list[str] = Field(default_factory=list)
    timeline_points: list[TimelinePoint] = Field(default_factory=list)
    used_beats: list[UsedBeat] = Field(default_factory=list)
    volume_summary: VolumeSummary | None = None
