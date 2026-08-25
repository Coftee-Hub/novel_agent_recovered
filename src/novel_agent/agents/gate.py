# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/agents/gate.py
# 来源   : gate.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '确定性闸门 —— 零 LLM 调用。\n\n排在 judge 之前：格式不合规的稿子不该浪费一次 LLM 评审。\n这里的每一条规则都是可单元测试的，不存在"这次判得松一点"的可能。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '确定性闸门 —— 零 LLM 调用。\n\n排在 judge 之前：格式不合规的稿子不该浪费一次 LLM 评审。\n这里的每一条规则都是可单元测试的，不存在"这次判得松一点"的可能。\n',
    10: '一-鿿',
    11: '[',
    12: ']',
    13: '[“][^”]*[”]|「[^」]*」',
    14: '[“][^”]*[”]|「[^」]*」|\\"[^\\"\\n]{2,}\\"|\'[^\'\\n]{2,}\'',
    15: '[。！？…]+',
    16: 'metaphor',
    17: 'psychology',
    18: 'sensory_touch',
    19: 'modal_particle',
    20: 'dict[str, tuple[str, ...]]',
    21: 'STYLE_MARKERS',
    25: 'Finding',
    27: 'GateReport',
    29: 'Gate',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'value',
    ('__annotate__', 2): 'float',
    ('__annotate__', 3): 'lo',
    ('__annotate__', 4): 'float | None',
    ('__annotate__', 5): 'hi',
    ('__annotate__', 6): 'tolerance',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'tuple[str, float | None]',
    ('bound_check', 0): '区间判定，三态。\n\n返回 ("ok"|"soft"|"hard", 越界的那个边界值)。\n\n"soft" 是刻意留的浮动：统计特征擦边不该当作错误。硬性打回会让\n修订环去修一个本不该由它修的问题 —— 实测第 2 章连续三次对话占比\n落在 13.3%~13.6%（下限 15%），因为那一章的场景本身就偏独处。\n',
    ('bound_check', 1): 'soft',
    ('bound_check', 2): 'hard',
    ('Finding', 0): 'Finding',
    ('Finding', 1): 'str',
    ('Finding', 2): 'rule',
    ('Finding', 3): 'Severity',
    ('Finding', 4): 'severity',
    ('Finding', 5): 'message',
    ('Finding', 7): 'int | None',
    ('Finding', 8): 'line',
    ('Finding', 9): 'str | None',
    ('Finding', 10): 'excerpt',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('__str__', 0): 'error',
    ('__str__', 1): '✗',
    ('__str__', 2): '!',
    ('__str__', 3): ' 第',
    ('__str__', 4): '行',
    ('__str__', 6): '  →「',
    ('__str__', 7): '」',
    ('__str__', 8): ' [',
    ('__str__', 9): ']',
    ('GateReport', 0): 'GateReport',
    ('GateReport', 2): 'list[Finding]',
    ('GateReport', 3): 'findings',
    ('GateReport', 4): 'dict[str, Any]',
    ('GateReport', 5): 'stats',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[Finding]',
    ('errors', 0): 'error',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[Finding]',
    ('warnings', 0): 'warn',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'bool',
    ('__annotate__', 1): 'style',
    ('__annotate__', 2): 'dict',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('style_profile', 0): '整章的文风剖面对照表。\n\n修订时必须给这个，而不是只给失败的那一项。实测教训：只说\n「长句率不足」，模型改完长句就把比喻写超标了；再说「比喻超标」，\n它又把对话砍没了 —— 一轮修一项、一轮坏一项，永远收敛不了。\n',
    ('style_profile', 1): '整章文风剖面（实测 → 目标区间）：',
    ('style_profile', 2): 'style_',
    ('style_profile', 4): '_min',
    ('style_profile', 5): '_max',
    ('style_profile', 6): '不限',
    ('style_profile', 7): '—',
    ('style_profile', 8): ' ~ ',
    ('style_profile', 10): '✗',
    ('style_profile', 11): '✓',
    ('style_profile', 13): '：',
    ('style_profile', 14): '（目标 ',
    ('style_profile', 15): '）',
    ('style_profile', 16): 'dialogue_ratio',
    ('style_profile', 17): '  · 对话占比：',
    ('style_profile', 18): '.1%',
    ('style_profile', 19): '**这些是整章的统计特征，要一起满足，不要为了修某一项把别的写坏。**',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('render', 0): '通过',
    ('render', 1): '未通过（',
    ('render', 2): ' 项错误）',
    ('render', 3): 'gate: ',
    ('render', 4): '  字数 ',
    ('render', 5): 'word_count',
    ('render', 6): ',',
    ('render', 7): ' | 段落 ',
    ('render', 8): 'paragraphs',
    ('render', 9): ' | 对话占比 ',
    ('render', 10): 'dialogue_ratio',
    ('render', 11): '.0%',
    ('Gate', 0): 'Gate',
    ('Gate', 6): 'state',
    ('Gate', 7): 'expected_ch',
    ('__annotate__', 1): 'config',
    ('__annotate__', 2): 'dict[str, Any]',
    ('__annotate__', 3): 'corpus_index',
    ('__annotate__', 4): 'NGramIndex | None',
    ('__annotate__', 5): 'self_index',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'None',
    ('__init__', 0): 'length',
    ('__init__', 1): 'format',
    ('__init__', 2): 'similarity',
    ('__init__', 3): 'style',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'kw',
    ('__annotate__', 4): 'Any',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'Gate',
    ('from_config', 0): 'utf-8',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'state',
    ('__annotate__', 4): 'StoryState | None',
    ('__annotate__', 5): 'expected_ch',
    ('__annotate__', 6): 'int | None',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'GateReport',
    ('__annotate__', 1): 'lines',
    ('__annotate__', 2): 'list[str]',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'tuple[tuple[int, str] | None, list[tuple[int, str]]]',
    ('_split_title', 0): '#',
    ('__annotate__', 1): 'body',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'paragraphs',
    ('__annotate__', 4): 'list[tuple[int, str]]',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'dict[str, Any]',
    ('_stats', 0): '\\s',
    ('_stats', 3): 'word_count',
    ('_stats', 4): 'paragraphs',
    ('_stats', 5): 'dialogue_ratio',
    ('__annotate__', 1): 'title',
    ('__annotate__', 2): 'tuple[int, str] | None',
    ('__annotate__', 3): 'expected_ch',
    ('__annotate__', 4): 'int | None',
    ('__annotate__', 5): 'r',
    ('__annotate__', 6): 'GateReport',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'None',
    ('_check_title', 1): 'title',
    ('_check_title', 2): 'error',
    ('_check_title', 3): '缺少章节标题（应为 `## 第N章 标题`）',
    ('_check_title', 4): 'chapter_title_pattern',
    ('_check_title', 5): '章节标题格式不符',
    ('_check_title', 6): '第(\\d+)章',
    ('_check_title', 7): '章节号应为 ',
    ('_check_title', 8): '，实际 ',
    ('__annotate__', 1): 'r',
    ('__annotate__', 2): 'GateReport',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('_check_length', 0): '字数与对话占比。两者都走三态判定 —— 擦边降级为警告。',
    ('_check_length', 1): 'tolerance',
    ('_check_length', 3): 'word_count',
    ('_check_length', 4): 'chapter_min',
    ('_check_length', 5): 'chapter_max',
    ('_check_length', 6): 'ok',
    ('_check_length', 7): 'length',
    ('_check_length', 8): 'hard',
    ('_check_length', 9): 'error',
    ('_check_length', 10): 'warn',
    ('_check_length', 11): '字数 ',
    ('_check_length', 12): ',',
    ('_check_length', 14): '超出上限',
    ('_check_length', 15): '少于下限',
    ('_check_length', 16): ',.0f',
    ('_check_length', 17): 'soft',
    ('_check_length', 18): '，在容差内',
    ('_check_length', 20): 'dialogue_ratio',
    ('_check_length', 21): 'dialogue_ratio_min',
    ('_check_length', 22): 'dialogue_ratio_max',
    ('_check_length', 23): ' —— 缺少叙述支撑',
    ('_check_length', 24): ' —— 叙述压过了场景',
    ('_check_length', 25): '对话占比 ',
    ('_check_length', 26): '.1%',
    ('_check_length', 27): '高于上限',
    ('_check_length', 28): '低于下限',
    ('__annotate__', 1): 'paragraphs',
    ('__annotate__', 2): 'list[tuple[int, str]]',
    ('__annotate__', 3): 'r',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('_check_punctuation', 0): '[,!?;:]',
    ('_check_punctuation', 1): 'punctuation',
    ('_check_punctuation', 2): 'error',
    ('_check_punctuation', 3): '半角标点 ',
    ('_check_punctuation', 4): ' 出现在中文里',
    ('_check_punctuation', 5): 'forbid_ascii_quotes',
    ('_check_punctuation', 6): '["\\\']',
    ('_check_punctuation', 7): '使用了 ASCII 引号，应为“”或「」',
    ('_check_punctuation', 8): 'forbid_repeated_marks',
    ('_check_punctuation', 9): '连续标点 ',
    ('_check_punctuation', 10): '\\.{2,}|。{3,}',
    ('_check_punctuation', 11): '省略号应为 …… ',
    ('_check_punctuation', 12): '(?<!…)…(?!…)',
    ('_check_punctuation', 13): '省略号应为两个 … 连用（……）',
    ('_check_punctuation', 14): '--|－－',
    ('_check_punctuation', 15): '(?<!—)—(?!—)',
    ('_check_punctuation', 16): '破折号应为 —— ',
    ('__annotate__', 1): 'paragraphs',
    ('__annotate__', 2): 'list[tuple[int, str]]',
    ('__annotate__', 3): 'r',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('_check_paragraphs', 0): 'paragraph_max_chars',
    ('_check_paragraphs', 1): 'paragraph_max_sentences',
    ('_check_paragraphs', 2): 'paragraph_median_max',
    ('_check_paragraphs', 4): 'paragraph_rhythm',
    ('_check_paragraphs', 5): 'error',
    ('_check_paragraphs', 6): '段落中位数 ',
    ('_check_paragraphs', 7): ' 字超出 ',
    ('_check_paragraphs', 8): ' —— 整章段落普遍偏长，本题材应当短句密排',
    ('_check_paragraphs', 9): 'paragraph',
    ('_check_paragraphs', 10): '单段 ',
    ('_check_paragraphs', 11): ' 字超出上限 ',
    ('_check_paragraphs', 12): ' —— 言情忌大段密排',
    ('_check_paragraphs', 14): '…',
    ('_check_paragraphs', 15): 'warn',
    ('_check_paragraphs', 16): ' 句，超过 ',
    ('__annotate__', 1): 'paragraphs',
    ('__annotate__', 2): 'list[tuple[int, str]]',
    ('__annotate__', 3): 'r',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('_check_dialogue', 0): '同段内出现两个**不同说话人**才算错。\n\n只数引号对数会大量误判：`“社刊旧刊。”他说，“九本。”` 是同一个人\n说话、中间插提示语，属于标准写法。判据是两段引号**之间**那截文字\n怎么收尾 —— 逗号收尾是提示语插入（同一人），句号收尾才是换了人：\n\n    “九本。”他说，“不到六点。”      → 同一人，合法\n    “九本。”他摇头。“不到六点。”她说。→ 两个人，必须分段\n',
    ('_check_dialogue', 1): 'dialogue_own_paragraph',
    ('_check_dialogue', 4): '。！？…',
    ('_check_dialogue', 5): 'dialogue',
    ('_check_dialogue', 6): 'error',
    ('_check_dialogue', 7): '同一段里出现两个说话人 —— 必须分段',
    ('_check_dialogue', 9): '…',
    ('__annotate__', 1): 'body',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'r',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('_check_style', 0): '文风统计特征是否落在源书的区间内。\n\n这是"挡平庸"的检查：一章可以标点全对、字数达标，却句句短促、\n没有一个比喻、没有一个语气词 —— 读起来就是不像人写的。单看任何\n一句都挑不出错，只有整章的统计特征能抓到。\n\n第 13 章的实测偏离：比喻 −87%、触温 −85%、语气词 −77%、短句率 +77%。\n',
    ('_check_style', 4): 'sentence_median',
    ('_check_style', 5): 'short_sentence_ratio',
    ('_check_style', 7): 'long_sentence_ratio',
    ('_check_style', 10): 'style_',
    ('_check_style', 11): '叙述句长中位',
    ('_check_style', 12): '短句率',
    ('_check_style', 13): '长句率',
    ('_check_style', 14): 'metaphor',
    ('_check_style', 15): '比喻密度',
    ('_check_style', 16): 'psychology',
    ('_check_style', 17): '心理描写密度',
    ('_check_style', 18): 'sensory_touch',
    ('_check_style', 19): '触觉/温度密度',
    ('_check_style', 20): 'modal_particle',
    ('_check_style', 21): '语气词密度',
    ('_check_style', 22): 'short_sentence_ratio_max',
    ('_check_style', 23): '句子过碎，读起来断断续续',
    ('_check_style', 24): 'long_sentence_ratio_min',
    ('_check_style', 25): '缺少绵延的长句，节奏没有起伏',
    ('_check_style', 26): 'metaphor_min',
    ('_check_style', 27): '几乎没有比喻 —— 言情最吃亏的就是这条',
    ('_check_style', 28): 'sensory_touch_min',
    ('_check_style', 29): '缺少触觉与温度，情绪没有身体落点',
    ('_check_style', 30): 'modal_particle_min',
    ('_check_style', 31): '语气词太少，对话像公文不像人说话',
    ('_check_style', 32): 'modal_particle_max',
    ('_check_style', 33): '语气词过密，读着聒噪',
    ('_check_style', 34): 'psychology_min',
    ('_check_style', 35): '心理描写太少，人物只剩动作，读者看不见挣扎',
    ('_check_style', 36): 'metaphor_max',
    ('_check_style', 37): '比喻过密，用力过猛',
    ('_check_style', 38): 'tolerance',
    ('_check_style', 40): '_min',
    ('_check_style', 41): '_max',
    ('_check_style', 42): 'ok',
    ('_check_style', 43): 'min',
    ('_check_style', 44): 'max',
    ('_check_style', 45): 'ratio',
    ('_check_style', 46): '.1%',
    ('_check_style', 47): '／',
    ('_check_style', 48): '.1f',
    ('_check_style', 49): '_',
    ('_check_style', 50): 'style',
    ('_check_style', 51): 'hard',
    ('_check_style', 52): 'error',
    ('_check_style', 53): 'warn',
    ('_check_style', 55): '（实测／',
    ('_check_style', 56): '下限',
    ('_check_style', 57): '上限',
    ('_check_style', 58): 'soft',
    ('_check_style', 59): '，在容差内',
    ('_check_style', 60): '）',
    ('_check_style', 61): ' —— ',
    ('__annotate__', 1): 'paragraphs',
    ('__annotate__', 2): 'list[tuple[int, str]]',
    ('__annotate__', 3): 'r',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('_check_stray_notes', 0): '正文里不该有分隔线。\n\n实测 stitcher 会在正文末尾用 `---` 起一段"缝合说明"（列它改了哪几处、\n统一了哪个设定），而输出是原样存盘的，说明就成了小说的一部分。\nwriter 那边已经机械剥掉，这里是第二道防线。\n\n这类缺陷修订环**修不掉**：重写场景改变不了 stitcher 的习惯，\n每重缝一次就再加一遍 —— 第 3 章两轮修订就是这么白烧的。\n',
    ('_check_stray_notes', 1): '(?:-{3,}|\\*{3,}|_{3,}|={3,})',
    ('_check_stray_notes', 2): 'stray_notes',
    ('_check_stray_notes', 3): 'error',
    ('_check_stray_notes', 4): '正文里出现分隔线 —— 多半后面跟着模型写给人看的说明，那不是小说的一部分',
    ('__annotate__', 1): 'body',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'r',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('_check_plagiarism', 1): 'max_matches',
    ('_check_plagiarism', 2): 'plagiarism',
    ('_check_plagiarism', 3): 'error',
    ('_check_plagiarism', 4): '与参考语料出现连续 ',
    ('_check_plagiarism', 5): ' 字雷同',
    ('__annotate__', 1): 'body',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'r',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('_check_self_repetition', 2): 'self_repetition',
    ('_check_self_repetition', 3): 'warn',
    ('_check_self_repetition', 4): '与本书前文用词重复',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState | None',
    ('__annotate__', 3): 'r',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('_check_debts', 0): '情感债到期未回收 —— 防烂尾，完全不需要 LLM。',
    ('_check_debts', 2): 'emotional_debt',
    ('_check_debts', 3): 'warn',
    ('_check_debts', 4): '第 ',
    ('_check_debts', 5): ' 章埋下的「',
    ('_check_debts', 6): '」应在第 ',
    ('_check_debts', 7): ' 章前回收，已逾期',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────

# ================= 重建源码（从字节码恢复） =================
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

import yaml

from ..corpus.similarity import NGramIndex
from ..state.schema import StoryState

# TODO(重建): Severity 的准确定义无法从反汇编恢复；实测取值仅见 'error' / 'warn'。
Severity = Literal['error', 'warn']

# 模块级正则（模式串均来自 _RECOVERED_CONSTS 原文字符串）。
_CJK_RE = re.compile('[一-鿿]')
_DIALOGUE_RE = re.compile('[“][^”]*[”]|「[^」]*」')
_DIALOGUE_ANY_RE = re.compile('[“][^”]*[”]|「[^」]*」|\\"[^\\"\\n]{2,}\\"|\'[^\'\\n]{2,}\'')
_SENTENCE_END_RE = re.compile('[。！？…]+')

# TODO(重建): STYLE_MARKERS 的具体词表不在可恢复的常量表内，无法逐字还原；
# 这里保留四个 key，词表留空待补。
STYLE_MARKERS: dict[str, tuple[str, ...]] = {
    'metaphor': (),
    'psychology': (),
    'sensory_touch': (),
    'modal_particle': (),
}


def bound_check(value, lo, hi, tolerance):
    '区间判定，三态。\n\n返回 ("ok"|"soft"|"hard", 越界的那个边界值)。\n\n"soft" 是刻意留的浮动：统计特征擦边不该当作错误。硬性打回会让\n修订环去修一个本不该由它修的问题 —— 实测第 2 章连续三次对话占比\n落在 13.3%~13.6%（下限 15%），因为那一章的场景本身就偏独处。\n'
    if lo is not None and value < lo:
        if value >= lo * (1 - tolerance):
            return 'soft', lo
        return 'hard', lo
    if hi is not None and value > hi:
        if value <= hi * (1 + tolerance):
            return 'soft', hi
        return 'hard', hi
    return 'ok', None


@dataclass
class Finding:
    'Finding'
    rule: str
    severity: Severity
    message: str
    line: int | None = None
    excerpt: str | None = None

    def __str__(self):
        'error'
        mark = '✗' if self.severity == 'error' else '!'
        where = f' 第{self.line}行' if self.line else ''
        tail = f'  →「{self.excerpt}」' if self.excerpt else ''
        return f'{mark} [{self.rule}]{where} {self.message}{tail}'


@dataclass
class GateReport:
    'GateReport'
    findings: list[Finding] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    @property
    def errors(self):
        'error'
        return [f for f in self.findings if f.severity == 'error']

    @property
    def warnings(self):
        'warn'
        return [f for f in self.findings if f.severity == 'warn']

    @property
    def passed(self):
        return not self.errors

    def style_profile(self, style):
        '整章的文风剖面对照表。\n\n修订时必须给这个，而不是只给失败的那一项。实测教训：只说\n「长句率不足」，模型改完长句就把比喻写超标了；再说「比喻超标」，\n它又把对话砍没了 —— 一轮修一项、一轮坏一项，永远收敛不了。\n'
        rows = [
            ('叙述句长中位', 'sentence_median', '{:.0f}'),
            ('短句率', 'short_sentence_ratio', '{:.1%}'),
            ('长句率', 'long_sentence_ratio', '{:.1%}'),
            ('比喻密度', 'metaphor', '{:.1f}'),
            ('心理描写密度', 'psychology', '{:.1f}'),
            ('触觉/温度密度', 'sensory_touch', '{:.1f}'),
            ('语气词密度', 'modal_particle', '{:.1f}'),
        ]
        out = ['整章文风剖面（实测 → 目标区间）：']
        for label, key, fmt in rows:
            value = self.stats.get(f'style_{key}')
            if value is None:
                continue
            lo = style.get(f'{key}_min')
            hi = style.get(f'{key}_max')
            if lo is None and hi is None:
                bound = '不限'
            else:
                bound = (
                    f'{fmt.format(lo) if lo is not None else "—"}'
                    f' ~ {fmt.format(hi) if hi is not None else "—"}'
                )
            bad = (lo is not None and value < lo) or (hi is not None and value > hi)
            out.append(
                f'  {"✗" if bad else "✓"} {label}：{fmt.format(value)}（目标 {bound}）'
            )
        ratio = self.stats.get('dialogue_ratio')
        if ratio is not None:
            out.append(f'  · 对话占比：{ratio:.1%}')
        out.append('**这些是整章的统计特征，要一起满足，不要为了修某一项把别的写坏。**')
        return '\n'.join(out)

    def render(self):
        '通过'
        head = '通过' if self.passed else f'未通过（{len(self.errors)} 项错误）'
        lines = [
            f'gate: {head}',
            f'  字数 {self.stats.get("word_count", 0):,}'
            f' | 段落 {self.stats.get("paragraphs", 0)}'
            f' | 对话占比 {self.stats.get("dialogue_ratio", 0):.0%}',
        ]
        lines += [f'  {f}' for f in self.findings]
        return '\n'.join(lines)


class Gate:
    'Gate'

    def __init__(self, config, corpus_index, self_index):
        'length'
        self.length = config['length']
        self.fmt = config['format']
        self.sim = config.get('similarity', {})
        self.style = config.get('style', {})
        self.corpus_index = corpus_index
        self.self_index = self_index

    @classmethod
    def from_config(cls, path, **kw):
        'utf-8'
        return cls(yaml.safe_load(Path(path).read_text('utf-8')), **kw)

    # 注(重建)：字节码显示 `state` 与 `expected_ch` 的 kwdefault 均为 None（骨架签名省略了默认值）。
    def check(self, text, *, state=None, expected_ch=None):
        report = GateReport()
        lines = text.splitlines()
        title_line, body_lines = self._split_title(lines)
        paragraphs = [(i, ln.strip()) for i, ln in body_lines if ln.strip()]
        body = '\n'.join(p for _, p in paragraphs)
        report.stats = self._stats(body, paragraphs)
        self._check_title(title_line, expected_ch, report)
        self._check_length(report)
        self._check_punctuation(paragraphs, report)
        self._check_paragraphs(paragraphs, report)
        self._check_dialogue(paragraphs, report)
        self._check_style(body, report)
        self._check_stray_notes(paragraphs, report)
        self._check_plagiarism(body, report)
        self._check_self_repetition(body, report)
        self._check_debts(state, report)
        return report

    @staticmethod
    def _split_title(lines):
        '#'
        for i, ln in enumerate(lines):
            if ln.strip().startswith('#'):
                return (i + 1, ln.strip()), list(
                    enumerate(lines[i + 1:], start=i + 2)
                )
        return None, list(enumerate(lines, start=1))

    def _stats(self, body, paragraphs):
        '\\s'
        chars = len(re.sub(r'\s', '', body))
        dialogue_chars = sum(len(m) for m in _DIALOGUE_ANY_RE.findall(body))
        return {
            'word_count': chars,
            'paragraphs': len(paragraphs),
            'dialogue_ratio': dialogue_chars / chars if chars else 0.0,
        }

    def _check_title(self, title, expected_ch, r):
        'title'
        if title is None:
            r.findings.append(Finding(
                'title', 'error',
                '缺少章节标题（应为 `## 第N章 标题`）',
            ))
            return
        lineno, text = title
        if not re.match(self.fmt['chapter_title_pattern'], text):
            r.findings.append(Finding(
                'title', 'error', '章节标题格式不符', lineno, text,
            ))
            return
        if expected_ch is not None:
            found = re.search(r'第(\d+)章', text)
            if found and int(found.group(1)) != expected_ch:
                r.findings.append(Finding(
                    'title', 'error',
                    f'章节号应为 {expected_ch}，实际 {found.group(1)}',
                    lineno, text,
                ))
                return

    def _check_length(self, r):
        '字数与对话占比。两者都走三态判定 —— 擦边降级为警告。'
        tolerance = self.style.get('tolerance', 0.0)
        wc = r.stats['word_count']
        lo = self.length['chapter_min']
        hi = self.length['chapter_max']
        verdict, limit = bound_check(wc, lo, hi, tolerance)
        if verdict != 'ok':
            over = wc > hi
            r.findings.append(Finding(
                'length',
                'error' if verdict == 'hard' else 'warn',
                f'字数 {wc:,} {"超出上限" if over else "少于下限"} {limit:,.0f}'
                + ('，在容差内' if verdict == 'soft' else ''),
            ))
        ratio = r.stats['dialogue_ratio']
        rlo = self.length['dialogue_ratio_min']
        rhi = self.length['dialogue_ratio_max']
        verdict, limit = bound_check(ratio, rlo, rhi, tolerance)
        if verdict != 'ok':
            over = ratio > rhi
            tail = (
                '' if verdict == 'soft'
                else (' —— 缺少叙述支撑' if over else ' —— 叙述压过了场景')
            )
            r.findings.append(Finding(
                'dialogue_ratio',
                'error' if verdict == 'hard' else 'warn',
                f'对话占比 {ratio:.1%} {"高于上限" if over else "低于下限"} {limit:.1%}'
                + ('，在容差内' if verdict == 'soft' else '')
                + f'{tail}',
            ))

    def _check_punctuation(self, paragraphs, r):
        '[,!?;:]'
        for lineno, para in paragraphs:
            for m in re.finditer(r'[,!?;:]', para):
                i = m.start()
                near = (
                    (i > 0 and bool(_CJK_RE.match(para[i - 1])))
                    or (i + 1 < len(para) and bool(_CJK_RE.match(para[i + 1])))
                )
                if not near:
                    continue
                r.findings.append(Finding(
                    'punctuation', 'error',
                    f'半角标点 {m.group()!r} 出现在中文里',
                    lineno, para[max(0, i - 8):i + 8],
                ))
            if self.fmt.get('forbid_ascii_quotes') and re.search(r'["\']', para):
                r.findings.append(Finding(
                    'punctuation', 'error',
                    '使用了 ASCII 引号，应为“”或「」', lineno,
                ))
            for bad in self.fmt.get('forbid_repeated_marks', []):
                if bad in para:
                    r.findings.append(Finding(
                        'punctuation', 'error', f'连续标点 {bad!r}', lineno,
                    ))
                    break
            if re.search(r'\.{2,}|。{3,}', para):
                r.findings.append(Finding(
                    'punctuation', 'error', '省略号应为 …… ', lineno,
                ))
            if re.search(r'(?<!…)…(?!…)', para):
                r.findings.append(Finding(
                    'punctuation', 'error', '省略号应为两个 … 连用（……）', lineno,
                ))
            if re.search(r'--|－－', para) or re.search(r'(?<!—)—(?!—)', para):
                r.findings.append(Finding(
                    'punctuation', 'error', '破折号应为 —— ', lineno,
                ))

    def _check_paragraphs(self, paragraphs, r):
        'paragraph_max_chars'
        max_chars = self.length['paragraph_max_chars']
        max_sents = self.length['paragraph_max_sentences']
        median_cap = self.length.get('paragraph_median_max')
        if median_cap and paragraphs:
            lengths = sorted(len(p) for _, p in paragraphs)
            median = lengths[len(lengths) // 2]
            if median > median_cap:
                r.findings.append(Finding(
                    'paragraph_rhythm', 'error',
                    f'段落中位数 {median} 字超出 {median_cap} —— 整章段落普遍偏长，本题材应当短句密排',
                ))
        for lineno, para in paragraphs:
            if len(para) > max_chars:
                r.findings.append(Finding(
                    'paragraph', 'error',
                    f'单段 {len(para)} 字超出上限 {max_chars} —— 言情忌大段密排',
                    lineno, para[:20] + '…',
                ))
            n_sent = len(_SENTENCE_END_RE.findall(para))
            if n_sent > max_sents:
                r.findings.append(Finding(
                    'paragraph', 'warn',
                    f'单段 {n_sent} 句，超过 {max_sents}', lineno,
                ))

    def _check_dialogue(self, paragraphs, r):
        '同段内出现两个**不同说话人**才算错。\n\n只数引号对数会大量误判：`“社刊旧刊。”他说，“九本。”` 是同一个人\n说话、中间插提示语，属于标准写法。判据是两段引号**之间**那截文字\n怎么收尾 —— 逗号收尾是提示语插入（同一人），句号收尾才是换了人：\n\n    “九本。”他说，“不到六点。”      → 同一人，合法\n    “九本。”他摇头。“不到六点。”她说。→ 两个人，必须分段\n'
        if not self.fmt.get('dialogue_own_paragraph'):
            return
        for lineno, para in paragraphs:
            spans = list(_DIALOGUE_RE.finditer(para))
            for a, b in zip(spans, spans[1:]):
                between = para[a.end():b.start()].strip()
                if not between:
                    continue
                if between[-1] in '。！？…':
                    r.findings.append(Finding(
                        'dialogue', 'error',
                        '同一段里出现两个说话人 —— 必须分段',
                        lineno, para[:24] + '…',
                    ))
                    break

    def _check_style(self, body, r):
        '文风统计特征是否落在源书的区间内。\n\n这是"挡平庸"的检查：一章可以标点全对、字数达标，却句句短促、\n没有一个比喻、没有一个语气词 —— 读起来就是不像人写的。单看任何\n一句都挑不出错，只有整章的统计特征能抓到。\n\n第 13 章的实测偏离：比喻 −87%、触温 −85%、语气词 −77%、短句率 +77%。\n'
        if not self.style:
            return
        narration = _DIALOGUE_RE.sub('', body)
        sents = [
            s.strip()
            for s in _SENTENCE_END_RE.split(narration)
            if len(s.strip()) > 1
        ]
        lens = [len(_CJK_RE.findall(s)) for s in sents]
        if not lens:
            return
        chars = len(_CJK_RE.findall(body)) or 1
        per10k = 10000 / chars
        stats = {
            'sentence_median': sorted(lens)[len(lens) // 2],
            'short_sentence_ratio': sum(1 for x in lens if x <= 10) / len(lens),
            'long_sentence_ratio': sum(1 for x in lens if x >= 30) / len(lens),
        }
        style_stats = {
            k: sum(body.count(w) for w in ws) * per10k
            for k, ws in STYLE_MARKERS.items()
        }
        stats.update(style_stats)
        r.stats.update({f'style_{k}': v for k, v in stats.items()})
        labels = {
            'sentence_median': '叙述句长中位',
            'short_sentence_ratio': '短句率',
            'long_sentence_ratio': '长句率',
            'metaphor': '比喻密度',
            'psychology': '心理描写密度',
            'sensory_touch': '触觉/温度密度',
            'modal_particle': '语气词密度',
        }
        hints = {
            'short_sentence_ratio_max': '句子过碎，读起来断断续续',
            'long_sentence_ratio_min': '缺少绵延的长句，节奏没有起伏',
            'metaphor_min': '几乎没有比喻 —— 言情最吃亏的就是这条',
            'sensory_touch_min': '缺少触觉与温度，情绪没有身体落点',
            'modal_particle_min': '语气词太少，对话像公文不像人说话',
            'modal_particle_max': '语气词过密，读着聒噪',
            'psychology_min': '心理描写太少，人物只剩动作，读者看不见挣扎',
            'metaphor_max': '比喻过密，用力过猛',
        }
        tolerance = self.style.get('tolerance', 0.0)
        for key, value in stats.items():
            lo = self.style.get(f'{key}_min')
            hi = self.style.get(f'{key}_max')
            verdict, limit = bound_check(value, lo, hi, tolerance)
            if verdict == 'ok':
                continue
            bound = 'min' if (lo is not None and value < lo) else 'max'
            shown = (
                f'{value:.1%}／{limit:.1%}'
                if 'ratio' in key
                else f'{value:.1f}／{limit:.1f}'
            )
            tail = hints.get(f'{key}_{bound}', '')
            r.findings.append(Finding(
                'style',
                'error' if verdict == 'hard' else 'warn',
                f'{labels.get(key, key)} {shown}（实测／{"下限" if bound == "min" else "上限"}'
                + ('，在容差内' if verdict == 'soft' else '')
                + '）'
                + (f' —— {tail}' if tail else ''),
            ))

    def _check_stray_notes(self, paragraphs, r):
        '正文里不该有分隔线。\n\n实测 stitcher 会在正文末尾用 `---` 起一段"缝合说明"（列它改了哪几处、\n统一了哪个设定），而输出是原样存盘的，说明就成了小说的一部分。\nwriter 那边已经机械剥掉，这里是第二道防线。\n\n这类缺陷修订环**修不掉**：重写场景改变不了 stitcher 的习惯，\n每重缝一次就再加一遍 —— 第 3 章两轮修订就是这么白烧的。\n'
        for lineno, text in paragraphs:
            if re.fullmatch(r'(?:-{3,}|\*{3,}|_{3,}|={3,})', text.strip()):
                r.findings.append(Finding(
                    'stray_notes', 'error',
                    '正文里出现分隔线 —— 多半后面跟着模型写给人看的说明，那不是小说的一部分',
                    lineno, text,
                ))

    def _check_plagiarism(self, body, r):
        'max_matches'
        if self.corpus_index is None or self.corpus_index.is_empty:
            return
        hits = self.corpus_index.find_matches(body)
        allowed = self.sim.get('max_matches', 0)
        if len(hits) > allowed:
            for hit in hits:
                r.findings.append(Finding(
                    'plagiarism', 'error',
                    f'与参考语料出现连续 {self.corpus_index.n} 字雷同',
                    excerpt=hit,
                ))

    def _check_self_repetition(self, body, r):
        'self_repetition'
        if self.self_index is None or self.self_index.is_empty:
            return
        for hit in self.self_index.find_matches(body, limit=3):
            r.findings.append(Finding(
                'self_repetition', 'warn',
                '与本书前文用词重复',
                excerpt=hit,
            ))

    def _check_debts(self, state, r):
        '情感债到期未回收 —— 防烂尾，完全不需要 LLM。'
        if state is None:
            return
        for debt in state.overdue_debts():
            r.findings.append(Finding(
                'emotional_debt', 'warn',
                f'第 {debt.planted_ch} 章埋下的「{debt.desc}」应在第 {debt.due_by_ch} 章前回收，已逾期',
            ))
