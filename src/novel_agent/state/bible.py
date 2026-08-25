# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/state/bible.py
# 来源   : bible.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = 'StoryState → story_bible.md 渲染。\n\n人读 markdown，机器读 json，事实源只有一个（json）。\nbible.md 是**产物**，手改它没有意义，下次渲染就覆盖了。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'StoryState → story_bible.md 渲染。\n\n人读 markdown，机器读 json，事实源只有一个（json）。\nbible.md 是**产物**，手改它没有意义，下次渲染就覆盖了。\n',
    3: '大学',
    4: '毕业过渡',
    5: '职场',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('render', 0): '# ',
    ('render', 1): ' — 设定集',
    ('render', 3): '> 本文件由 `story_state.json` 自动渲染，**手改无效**。当前进度：第 ',
    ('render', 4): ' 章。',
    ('render', 5): '## ⚠ 逾期未回收的情感债',
    ('render', 6): '- **',
    ('render', 7): '**（',
    ('render', 8): '）—— 第 ',
    ('render', 9): ' 章埋下，应在第 ',
    ('render', 10): ' 章前回收',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[str]',
    ('_characters', 0): '## 人物',
    ('_characters', 2): '（',
    ('_characters', 3): '、',
    ('_characters', 4): '）',
    ('_characters', 5): '### ',
    ('_characters', 6): '- **性格内核**：',
    ('_characters', 7): '- **说话习惯**：',
    ('_characters', 8): '- **核心创伤**：',
    ('_characters', 9): '- **价值观底线**：',
    ('_characters', 10): '- **代表台词**：',
    ('_characters', 11): '  - 「',
    ('_characters', 12): '」',
    ('_characters', 15): '| ',
    ('_characters', 16): ' | ',
    ('_characters', 17): ' |',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[str]',
    ('_relationships', 0): '## 关系',
    ('_relationships', 2): '、',
    ('_relationships', 4): '—',
    ('_relationships', 5): '| ',
    ('_relationships', 6): ' | ',
    ('_relationships', 7): ' | 第 ',
    ('_relationships', 8): ' 章 |',
    ('_relationships', 9): '- **',
    ('_relationships', 10): ' 未解决**：',
    ('_relationships', 11): '；',
    ('<genexpr>', 0): '→',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('_names', 0): ' ↔ ',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[str]',
    ('_debts', 0): '## 未回收的情感债',
    ('_debts', 4): '| ',
    ('_debts', 5): ' | ',
    ('_debts', 6): ' | 第 ',
    ('_debts', 7): ' 章 | 第 ',
    ('_debts', 8): ' 章 |',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[str]',
    ('_beats', 0): '## 已用桥段（禁止重复）',
    ('_beats', 2): '- `',
    ('_beats', 3): '` 第 ',
    ('_beats', 4): ' 章 —— ',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[str]',
    ('_summaries', 0): '## 卷级摘要',
    ('_summaries', 4): '**第 ',
    ('_summaries', 5): ' 卷**（第 ',
    ('_summaries', 6): '-',
    ('_summaries', 7): ' 章）：',
    ('_summaries', 8): '## 章节摘要',
    ('_summaries', 10): '- **第 ',
    ('_summaries', 11): ' 章 ',
    ('_summaries', 12): '**（',
    ('_summaries', 13): ' 字，',
    ('_summaries', 14): '）：',
}

# ───────────── 还原后的源码 ─────────────
from novel_agent.state.schema import StoryState

# TODO(重建): _STAGE_ORDER 是模块级字典，值由 _characters 的排序 lambda
# （_STAGE_ORDER.get(x.stage, 9)）引用。三个阶段字符串来自模块级常量表
# （下标 3/4/5：大学、毕业过渡、职场），按出现顺序赋 0/1/2 为合理还原；
# 具体数值无法从 .pyc 精确确认。
_STAGE_ORDER = {"大学": 0, "毕业过渡": 1, "职场": 2}


def render(state: StoryState) -> str:
    out = [
        f"# {state.title} — 设定集",
        "",
        f"> 本文件由 `story_state.json` 自动渲染，**手改无效**。当前进度：第 {state.current_chapter} 章。",
        "",
    ]
    overdue = state.overdue_debts()
    if overdue:
        out += ["## ⚠ 逾期未回收的情感债", ""]
        for d in overdue:
            out.append(f"- **{d.desc}**（{d.kind}）—— 第 {d.planted_ch} 章埋下，应在第 {d.due_by_ch} 章前回收")
        out.append("")
    out += _characters(state) + _relationships(state) + _debts(state)
    out += _beats(state) + _summaries(state)
    return "\n".join(out).rstrip() + "\n"


def _characters(state: StoryState) -> list[str]:
    if not state.characters:
        return []
    out = ["## 人物", ""]
    for c in state.characters:
        alias = f"（{'、'.join(c.aliases)}）" if c.aliases else ""
        out += [
            f"### {c.name}{alias}",
            "",
            f"- **性格内核**：{'、'.join(c.core_traits)}",
            f"- **说话习惯**：{c.speech_habits}",
            f"- **核心创伤**：{c.core_wound}",
            f"- **价值观底线**：{c.value_line}",
        ]
        if c.voice_samples:
            out.append("- **代表台词**：")
            out += [f"  - 「{v}」" for v in c.voice_samples]
        if c.arcs:
            out += ["", "| 阶段 | 年龄 | 身份 | 外在目标 | 内在渴望 | 处境 |", "|---|---|---|---|---|---|"]
            for a in sorted(c.arcs, key=lambda x: _STAGE_ORDER.get(x.stage, 9)):
                out.append(f"| {a.stage} | {a.age} | {a.identity} | {a.outer_goal} | {a.inner_want} | {a.status} |")
        out.append("")
    return out


def _relationships(state: StoryState) -> list[str]:
    if not state.relationships:
        return []
    out = ["## 关系", "", "| 双方 | 阶段 | 张力来源 | 好感度 | 上次推进 |", "|---|---|---|---|---|"]
    for r in state.relationships:
        names = _names(state, r)
        aff = "、".join(f"{k}→{v}" for k, v in sorted(r.affection.items())) or "—"
        out.append(f"| {names} | {r.stage} | {r.tension_source} | {aff} | 第 {r.last_advanced_ch} 章 |")
    out.append("")
    for r in state.relationships:
        if not r.unresolved:
            continue
        out.append(f"- **{_names(state, r)} 未解决**：{'；'.join(r.unresolved)}")
    return out + [""]


def _names(state: StoryState, r) -> str:
    return " ↔ ".join(
        state.character(cid).name if state.character(cid) else cid
        for cid in (r.a_id, r.b_id)
    )


def _debts(state: StoryState) -> list[str]:
    open_debts = state.open_debts()
    if not open_debts:
        return []
    out = ["## 未回收的情感债", "", "| 类型 | 内容 | 埋设 | 应回收 |", "|---|---|---|---|"]
    for d in sorted(open_debts, key=lambda x: x.due_by_ch):
        out.append(f"| {d.kind} | {d.desc} | 第 {d.planted_ch} 章 | 第 {d.due_by_ch} 章 |")
    return out + [""]


def _beats(state: StoryState) -> list[str]:
    if not state.used_beats:
        return []
    out = ["## 已用桥段（禁止重复）", ""]
    for beat in state.used_beats:
        out.append(f"- `{beat.beat_type}` 第 {beat.ch} 章 —— {beat.one_line}")
    return out + [""]


def _summaries(state: StoryState) -> list[str]:
    out: list[str] = []
    if state.volume_summaries:
        out += ["## 卷级摘要", ""]
        for v in sorted(state.volume_summaries, key=lambda x: x.volume):
            out.append(f"**第 {v.volume} 卷**（第 {v.ch_start}-{v.ch_end} 章）：{v.summary}")
            out.append("")
    if state.chapter_summaries:
        out += ["## 章节摘要", ""]
        for s in sorted(state.chapter_summaries, key=lambda x: x.ch):
            out.append(f"- **第 {s.ch} 章 {s.title}**（{s.word_count} 字，{s.stage}）：{s.summary}")
        out.append("")
    return out
