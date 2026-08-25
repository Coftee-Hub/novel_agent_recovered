# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/state/store.py
# 来源   : store.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '状态读写与 patch 合并。\n\narchivist 只提交增量 patch，合并逻辑全在 Python 侧 —— 让 LLM 直接重写整个\nstate 是本项目最容易出的事故：几十章后字段会静默漂移、丢失。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '状态读写与 patch 合并。\n\narchivist 只提交增量 patch，合并逻辑全在 Python 侧 —— 让 LLM 直接重写整个\nstate 是本项目最容易出的事故：几十章后字段会静默漂移、丢失。\n',
    6: 'PatchError',
    8: 'StateStore',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('PatchError', 0): 'PatchError',
    ('PatchError', 1): 'patch 违反了引用完整性 —— 指向了不存在的人物或情感债。',
    ('StateStore', 0): 'StateStore',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'StoryState',
    ('load', 0): 'utf-8',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('save', 0): '原子写入。事实源写到一半崩溃会毁掉整本书的记忆。',
    ('save', 4): '.tmp',
    ('save', 6): 'w',
    ('save', 7): 'utf-8',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'patch',
    ('__annotate__', 4): 'StatePatch',
    ('__annotate__', 5): 'return',
    ('apply_patch', 0): '把一章的增量合并进 state，返回新对象（不原地修改）。\n\n引用完整性问题一律抛错而非静默跳过：archivist 编造了一个不存在的\n人物 id，是必须立刻发现的信号。\n',
    ('apply_patch', 3): 'new_characters 里的「',
    ('apply_patch', 4): '」(id=',
    ('apply_patch', 5): ') 与已有人物重名（已有 id=',
    ('apply_patch', 6): '）。同一个人不要用新 id 重新登记。',
    ('apply_patch', 8): 'arc_updates 指向未知人物 ',
    ('apply_patch', 10): 'relationship_updates 指向未知人物 ',
    ('apply_patch', 13): 'resolved_debt_ids 指向未知情感债 ',
    ('apply_patch', 14): 'paid',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'vs',
    ('__annotate__', 4): 'VolumeSummary',
    ('__annotate__', 5): 'return',
    ('apply_volume_summary', 0): '把一段卷梗概并进 state，按卷号覆盖，返回新对象。\n\n单独一个函数是因为它有两个调用点：逐章 patch 里带着它进来（重跑归档时），\n以及卷末压缩这个独立动作。两处必须用同一套校验，否则总有一处会漏。\n',
    ('apply_volume_summary', 1): '第 ',
    ('apply_volume_summary', 2): ' 卷梗概覆盖到第 ',
    ('apply_volume_summary', 3): ' 章，但故事只写到第 ',
    ('apply_volume_summary', 4): ' 章 —— 压缩了还没写出来的章节',
}

# ───────────── 还原后的源码 ─────────────
import os
import tempfile
from pathlib import Path

from novel_agent.state.schema import StatePatch, StoryState, VolumeSummary


class PatchError(Exception):
    """patch 违反了引用完整性 —— 指向了不存在的人物或情感债。"""


class StateStore:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> StoryState:
        if not self.path.exists():
            return StoryState()
        return StoryState.model_validate_json(self.path.read_text("utf-8"))

    def save(self, state: StoryState) -> None:
        """原子写入。事实源写到一半崩溃会毁掉整本书的记忆。"""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = state.model_dump_json(indent=2)
        fd, tmp = tempfile.mkstemp(dir=self.path.parent, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                fh.write(payload)
            os.replace(tmp, self.path)
        except BaseException:
            Path(tmp).unlink(missing_ok=True)
            raise


def apply_patch(state: StoryState, patch: StatePatch) -> StoryState:
    """把一章的增量合并进 state，返回新对象（不原地修改）。

    引用完整性问题一律抛错而非静默跳过：archivist 编造了一个不存在的
    人物 id，是必须立刻发现的信号。
    """
    new = state.model_copy(deep=True)

    known = {c.id for c in new.characters}
    by_name = {c.name: c.id for c in new.characters}

    for char in patch.new_characters:
        if char.id in known:
            continue
        if char.name in by_name:
            raise PatchError(
                f"new_characters 里的「{char.name}」(id={char.id!r}) 与已有人物重名（已有 id={by_name[char.name]!r}）。同一个人不要用新 id 重新登记。"
            )
        new.characters.append(char)
        known.add(char.id)

    for update in patch.arc_updates:
        target = new.character(update.character_id)
        if target is None:
            raise PatchError(f"arc_updates 指向未知人物 {update.character_id!r}")
        existing = next(
            (i for i, a in enumerate(target.arcs) if a.stage == update.arc.stage), None
        )
        if existing is None:
            target.arcs.append(update.arc)
        else:
            target.arcs[existing] = update.arc

    for rel in patch.relationship_updates:
        for cid in (rel.a_id, rel.b_id):
            if cid not in known:
                raise PatchError(f"relationship_updates 指向未知人物 {cid!r}")
        idx = next(
            (i for i, r in enumerate(new.relationships) if r.key == rel.key), None
        )
        if idx is None:
            new.relationships.append(rel)
        else:
            new.relationships[idx] = rel

    debt_ids = {d.id for d in new.debts}
    for debt in patch.new_debts:
        if debt.id not in debt_ids:
            new.debts.append(debt)
            debt_ids.add(debt.id)

    for did in patch.resolved_debt_ids:
        target_debt = next((d for d in new.debts if d.id == did), None)
        if target_debt is None:
            raise PatchError(f"resolved_debt_ids 指向未知情感债 {did!r}")
        target_debt.status = "paid"

    ch = patch.chapter_summary.ch
    new.timeline = [p for p in new.timeline if p.ch != ch] + patch.timeline_points
    new.used_beats = [b for b in new.used_beats if b.ch != ch] + patch.used_beats

    summary = patch.chapter_summary
    idx = next(
        (i for i, s in enumerate(new.chapter_summaries) if s.ch == summary.ch), None
    )
    if idx is None:
        new.chapter_summaries.append(summary)
    else:
        new.chapter_summaries[idx] = summary
    new.chapter_summaries.sort(key=lambda s: s.ch)
    new.current_chapter = max(new.current_chapter, summary.ch)

    if patch.volume_summary is not None:
        new = apply_volume_summary(new, patch.volume_summary)
    return new


def apply_volume_summary(state: StoryState, vs: VolumeSummary) -> StoryState:
    """把一段卷梗概并进 state，按卷号覆盖，返回新对象。

    单独一个函数是因为它有两个调用点：逐章 patch 里带着它进来（重跑归档时），
    以及卷末压缩这个独立动作。两处必须用同一套校验，否则总有一处会漏。
    """
    if vs.ch_end > state.current_chapter:
        raise PatchError(
            f"第 {vs.volume} 卷梗概覆盖到第 {vs.ch_end} 章，但故事只写到第 {state.current_chapter} 章 —— 压缩了还没写出来的章节"
        )
    new = state.model_copy(deep=True)
    idx = next(
        (i for i, v in enumerate(new.volume_summaries) if v.volume == vs.volume), None
    )
    if idx is None:
        new.volume_summaries.append(vs)
    else:
        new.volume_summaries[idx] = vs
    new.volume_summaries.sort(key=lambda v: v.volume)
    return new
