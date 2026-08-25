# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/agents/architect.py
# 来源   : architect.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = 'agent_creat —— 卷大纲 → 章细纲 → 场景规格。\n\n唯一带人工确认断点的节点：卷大纲要作者点头才往下走。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'agent_creat —— 卷大纲 → 章细纲 → 场景规格。\n\n唯一带人工确认断点的节点：卷大纲要作者点头才往下走。\n',
    10: 'Architect',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Architect', 0): 'Architect',
    ('Architect', 1): 'summary_cap',
    ('Architect', 13): 'note',
    ('__annotate__', 1): 'client',
    ('__annotate__', 2): 'LLMClient',
    ('__annotate__', 3): 'skills_dir',
    ('__annotate__', 4): 'str | Path',
    ('__annotate__', 5): 'summary_cap',
    ('__annotate__', 6): 'int',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'None',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('system_core', 0): '全书不变。strict=False：语料未到位时部分 skill 尚未萃取，先跑起来。',
    ('system_core', 3): '\n\n---\n\n',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('bible_layer', 0): '设定集 + **人物 id 表**。\n\nid 表不能省：bible 渲染的是姓名，模型看不到 id 就会自己造一个\n（实测它会把 `shen` 写成 `shen_zhiwei`），随后 apply_patch 的引用\n完整性校验会拒绝整个 patch。\n',
    ('bible_layer', 4): '<人物 id 表·引用时必须逐字使用左边的 id>\n',
    ('bible_layer', 5): '\n</人物 id 表>\n\n<设定集>\n',
    ('bible_layer', 6): '\n</设定集>',
    ('<genexpr>', 0): '- `',
    ('<genexpr>', 1): '` = ',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'referenced',
    ('__annotate__', 4): 'set[str]',
    ('__annotate__', 5): 'where',
    ('__annotate__', 6): 'str',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'None',
    ('_check_ids', 0): '校验输出引用的人物 id 都真实存在。\n\n模型编造 id 时立刻报错，而不是等到 apply_patch 阶段才发现 ——\n那时已经白写了一整章。\n',
    ('_check_ids', 1): ' 引用了不存在的人物 id：',
    ('_check_ids', 2): '。已知的 id 是 ',
    ('_check_ids', 3): ' —— 必须逐字使用，不要自行改写。',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'VolumeOutline | None',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'str',
    ('history_layer', 0): '卷内不变的部分：前情摘要、已用桥段、未收的债、已确认的卷大纲。',
    ('history_layer', 5): '<往卷梗概>\n',
    ('history_layer', 6): '\n</往卷梗概>',
    ('history_layer', 9): '<本卷已写章节>\n',
    ('history_layer', 10): '\n</本卷已写章节>',
    ('history_layer', 11): '<已用桥段·禁止重复>\n',
    ('history_layer', 13): '\n</已用桥段·禁止重复>',
    ('history_layer', 16): '<未回收的情感债>\n',
    ('history_layer', 17): '\n</未回收的情感债>',
    ('history_layer', 18): '<本卷大纲·已确认>\n',
    ('history_layer', 19): '\n</本卷大纲·已确认>',
    ('<genexpr>', 0): '- 第 ',
    ('<genexpr>', 1): ' 卷（第 ',
    ('<genexpr>', 2): '-',
    ('<genexpr>', 3): ' 章）：',
    ('<genexpr>', 0): '- 第 ',
    ('<genexpr>', 1): ' 章 ',
    ('<genexpr>', 2): '：',
    ('<genexpr>', 0): '- ',
    ('<genexpr>', 0): '- [',
    ('<genexpr>', 1): '] ',
    ('<genexpr>', 2): '：',
    ('<genexpr>', 3): '（第 ',
    ('<genexpr>', 4): ' 章埋下，应在第 ',
    ('<genexpr>', 5): ' 章前回收）',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'ch_start',
    ('__annotate__', 6): 'ch_end',
    ('__annotate__', 7): 'stage',
    ('__annotate__', 8): 'str',
    ('__annotate__', 9): 'note',
    ('__annotate__', 10): 'return',
    ('__annotate__', 11): 'VolumeOutline',
    ('plan_volume', 0): '出卷大纲。这一步之后会停下来等作者确认。',
    ('plan_volume', 1): '设计第 ',
    ('plan_volume', 2): ' 卷的大纲，覆盖第 ',
    ('plan_volume', 3): ' 到第 ',
    ('plan_volume', 4): ' 章（共 ',
    ('plan_volume', 5): ' 章），人生阶段为「',
    ('plan_volume', 6): '」。',
    ('plan_volume', 8): '要求：',
    ('plan_volume', 9): '- 关系推进要匀速，一卷之内不要跨越太多阶段',
    ('plan_volume', 10): '- 转折点的章号必须落在本卷区间内',
    ('plan_volume', 11): '- 每条关系推进都要说明「靠什么推进的」，必须是具体事件而非抽象描述',
    ('plan_volume', 12): '- 上下文里未回收的情感债，挑到期的在本卷收掉',
    ('plan_volume', 13): '作者补充要求：',
    ('plan_volume', 14): 'architect',
    ('plan_volume', 17): '第 ',
    ('plan_volume', 18): ' 卷大纲',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'VolumeOutline',
    ('__annotate__', 5): 'ch',
    ('__annotate__', 6): 'int',
    ('__annotate__', 7): 'note',
    ('__annotate__', 8): 'str',
    ('__annotate__', 9): 'return',
    ('__annotate__', 10): 'ChapterOutline',
    ('plan_chapter', 0): '出章细纲 + 场景规格。卷内逐章调用，共享同一个缓存前缀。',
    ('plan_chapter', 3): '设计第 ',
    ('plan_chapter', 4): ' 章的细纲，拆成 2-4 个场景。',
    ('plan_chapter', 6): '要求：',
    ('plan_chapter', 7): '- 每个场景的起止情绪必须不同，且要写清楚靠什么完成这个位移',
    ('plan_chapter', 8): '- 场景 id 用 `ch{:03d}_s{{n}}` 格式',
    ('plan_chapter', 9): '- 全章目标字数 2800-3600，分配到各场景',
    ('plan_chapter', 10): '- 章末要留钩子',
    ('plan_chapter', 11): '- **本章是本卷的转折点**：',
    ('plan_chapter', 12): '作者补充要求：',
    ('plan_chapter', 13): 'architect',
    ('plan_chapter', 16): '第 ',
    ('plan_chapter', 17): ' 章细纲',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────

# ================= 重建源码（从字节码恢复） =================
from pathlib import Path

from ..llm import LLMClient, Prompt
from ..skills import SkillLibrary
from ..state import render as render_bible
from ..state.schema import StoryState
from .prompts import ARCHITECT_ROLE, ARCHITECT_SKILLS  # TODO(重建): prompts.py 尚为骨架，需在其恢复文件中定义 ARCHITECT_ROLE / ARCHITECT_SKILLS
from .schemas import ChapterOutline, VolumeOutline


class Architect:
    'Architect'

    # 注(重建)：字节码显示 `summary_cap` 的 kwdefault 为 24（骨架签名省略了默认值）。
    def __init__(self, client, skills_dir, *, summary_cap=24):
        self.client = client
        self.skills = SkillLibrary(skills_dir)
        self.summary_cap = summary_cap

    def system_core(self):
        '全书不变。strict=False：语料未到位时部分 skill 尚未萃取，先跑起来。'
        extra = self.skills.compose(ARCHITECT_SKILLS, strict=False)
        return f'{ARCHITECT_ROLE}\n\n---\n\n{extra}' if extra else ARCHITECT_ROLE

    def bible_layer(self, state):
        '设定集 + **人物 id 表**。\n\nid 表不能省：bible 渲染的是姓名，模型看不到 id 就会自己造一个\n（实测它会把 `shen` 写成 `shen_zhiwei`），随后 apply_patch 的引用\n完整性校验会拒绝整个 patch。\n'
        if not state.characters:
            return ''
        roster = '\n'.join(f'- `{c.id}` = {c.name}' for c in state.characters)
        return (
            '<人物 id 表·引用时必须逐字使用左边的 id>\n'
            f'{roster}'
            '\n</人物 id 表>\n\n<设定集>\n'
            f'{render_bible(state)}'
            '\n</设定集>'
        )

    @staticmethod
    def _check_ids(state, referenced, where):
        '校验输出引用的人物 id 都真实存在。\n\n模型编造 id 时立刻报错，而不是等到 apply_patch 阶段才发现 ——\n那时已经白写了一整章。\n'
        known = {c.id for c in state.characters}
        unknown = referenced - known
        if unknown:
            raise ValueError(
                f'{where} 引用了不存在的人物 id：{sorted(unknown)}。已知的 id 是 {sorted(known)} —— 必须逐字使用，不要自行改写。'
            )

    # 注(重建)：字节码显示 `volume` 的默认值为 None（骨架签名省略了默认值）。
    def history_layer(self, state, volume=None):
        '卷内不变的部分：前情摘要、已用桥段、未收的债、已确认的卷大纲。'
        parts = []
        if state.volume_summaries:
            rows = '\n'.join(
                f'- 第 {v.volume} 卷（第 {v.ch_start}-{v.ch_end} 章）：{v.summary}'
                for v in sorted(state.volume_summaries, key=lambda x: x.volume)
            )
            parts.append(f'<往卷梗概>\n{rows}\n</往卷梗概>')
        live = state.live_summaries(cap=self.summary_cap)
        if live:
            rows = '\n'.join(
                f'- 第 {s.ch} 章 {s.title}：{s.summary}'
                for s in live
            )
            parts.append(f'<本卷已写章节>\n{rows}\n</本卷已写章节>')
        beats = state.used_beat_types()
        if beats:
            parts.append(
                '<已用桥段·禁止重复>\n'
                + '\n'.join(f'- {b}' for b in beats)
                + '\n</已用桥段·禁止重复>'
            )
        open_debts = state.open_debts()
        if open_debts:
            rows = '\n'.join(
                f'- [{d.id}] {d.kind}：{d.desc}（第 {d.planted_ch} 章埋下，应在第 {d.due_by_ch} 章前回收）'
                for d in sorted(open_debts, key=lambda x: x.due_by_ch)
            )
            parts.append(f'<未回收的情感债>\n{rows}\n</未回收的情感债>')
        if volume is not None:
            parts.append(
                f'<本卷大纲·已确认>\n{volume.to_markdown()}\n</本卷大纲·已确认>'
            )
        return '\n\n'.join(parts)

    # 注(重建)：字节码显示 `note` 的 kwdefault 为 ''（骨架签名省略了默认值）。
    def plan_volume(self, state, *, volume, ch_start, ch_end, stage, note=''):
        '出卷大纲。这一步之后会停下来等作者确认。'
        ask = [
            f'设计第 {volume} 卷的大纲，覆盖第 {ch_start} 到第 {ch_end} 章（共 {ch_end - ch_start + 1} 章），人生阶段为「{stage}」。',
            '',
            '要求：',
            '- 关系推进要匀速，一卷之内不要跨越太多阶段',
            '- 转折点的章号必须落在本卷区间内',
            '- 每条关系推进都要说明「靠什么推进的」，必须是具体事件而非抽象描述',
        ]
        if state.open_debts():
            ask.append('- 上下文里未回收的情感债，挑到期的在本卷收掉')
        if note:
            ask += ['', f'作者补充要求：{note}']
        result = self.client.parse(
            'architect',
            Prompt(
                system_core=self.system_core(),
                bible=self.bible_layer(state),
                volume=self.history_layer(state),
                instruction='\n'.join(ask),
            ),
            VolumeOutline,
        )
        outline = result.parsed
        refs = {cid for r in outline.relation_targets for cid in (r.a_id, r.b_id)}
        self._check_ids(state, refs, f'第 {volume} 卷大纲')
        return outline

    # 注(重建)：字节码显示 `note` 的 kwdefault 为 ''（骨架签名省略了默认值）。
    def plan_chapter(self, state, volume, *, ch, note=''):
        '出章细纲 + 场景规格。卷内逐章调用，共享同一个缓存前缀。'
        turning = next(
            (t for t in volume.turning_points if t.ch == ch), None
        )
        ask = [
            f'设计第 {ch} 章的细纲，拆成 2-4 个场景。',
            '',
            '要求：',
            '- 每个场景的起止情绪必须不同，且要写清楚靠什么完成这个位移',
            '- 场景 id 用 `ch{:03d}_s{{n}}` 格式'.format(ch),
            '- 全章目标字数 2800-3600，分配到各场景',
            '- 章末要留钩子',
        ]
        if turning:
            ask.append(f'- **本章是本卷的转折点**：{turning.what}')
        if note:
            ask += ['', f'作者补充要求：{note}']
        result = self.client.parse(
            'architect',
            Prompt(
                system_core=self.system_core(),
                bible=self.bible_layer(state),
                volume=self.history_layer(state, volume),
                instruction='\n'.join(ask),
            ),
            ChapterOutline,
        )
        chapter = result.parsed
        refs = {cid for sc in chapter.scenes for cid in sc.present}
        self._check_ids(state, refs, f'第 {ch} 章细纲')
        return chapter
