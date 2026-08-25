# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/llm/prompt_builder.py
# 来源   : prompt_builder.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = 'Prompt 组装 —— 全项目唯一入口，任何 agent 不得自行拼 prompt。\n\n理由：prompt 缓存是**前缀匹配**。前缀里任何一个字节变了，它之后的所有缓存全部失效。\n本项目的 bible + skills 有几万 token，如果被 RAG 片段（每章都变）挤在前面，\n每章都要全价重算，成本差 5-10 倍。\n\n这条规则对**所有供应商**都成立 —— 无论是 Anthropic 的显式断点，还是\nOpenAI / DeepSeek / Kimi 的自动前缀缓存，缓存都是前缀匹配。因此本模块\n只描述"分层"，把"翻译成某家的请求形状"交给 backends。\n\n本模块用分层结构从类型上强制正确的顺序：\n\n    system_core   全书不变      [断点1]\n    bible         每卷变一次    [断点2]\n    volume        每卷变一次    [断点3]\n    ---- 以上是缓存前缀，卷内所有章节共享 ----\n    rag / prev_tail / instruction   每次都变，不加断点\n'

import hashlib
import json
import re
from dataclasses import dataclass, field
from typing import Any

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'Prompt 组装 —— 全项目唯一入口，任何 agent 不得自行拼 prompt。\n\n理由：prompt 缓存是**前缀匹配**。前缀里任何一个字节变了，它之后的所有缓存全部失效。\n本项目的 bible + skills 有几万 token，如果被 RAG 片段（每章都变）挤在前面，\n每章都要全价重算，成本差 5-10 倍。\n\n这条规则对**所有供应商**都成立 —— 无论是 Anthropic 的显式断点，还是\nOpenAI / DeepSeek / Kimi 的自动前缀缓存，缓存都是前缀匹配。因此本模块\n只描述"分层"，把"翻译成某家的请求形状"交给 backends。\n\n本模块用分层结构从类型上强制正确的顺序：\n\n    system_core   全书不变      [断点1]\n    bible         每卷变一次    [断点2]\n    volume        每卷变一次    [断点3]\n    ---- 以上是缓存前缀，卷内所有章节共享 ----\n    rag / prev_tail / instruction   每次都变，不加断点\n',
    5: 'type',
    6: 'ephemeral',
    7: 'dict[str, str]',
    8: 'CACHE',
    9: '\\d{4}-\\d{2}-\\d{2}[T ]\\d{2}:\\d{2}',
    10: 'ISO 时间戳',
    11: '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
    12: 'UUID',
    13: 'list[tuple[re.Pattern[str], str]]',
    14: '_INVALIDATORS',
    15: '<风格参照>\n以下片段来自参考语料，**仅供体会**叙述节奏、情绪推进方式与对话质感。\n严禁复用其中任何原句、原比喻、原台词、原意象组合。\n如果你发现自己正在改写其中某一句，立刻停下，换一个完全不同的写法。\n',
    17: 'PromptLayerError',
    21: 'Prompt',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('PromptLayerError', 0): 'PromptLayerError',
    ('PromptLayerError', 1): '分层约束被违反 —— 通常意味着缓存会失效。',
    ('__annotate__', 1): 'obj',
    ('__annotate__', 2): 'Any',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('stable_json', 0): '确定性序列化。\n\n`sort_keys=True` 不是洁癖：Python dict 的插入顺序会随构造路径变化，\n序列化出的字节不同 → 前缀不同 → 缓存永远 miss，且没有任何报错。\n',
    ('Prompt', 0): 'Prompt',
    ('Prompt', 1): '一次调用的分层内容。字段顺序即 prompt 中的物理顺序。',
    ('Prompt', 2): 'str',
    ('Prompt', 3): 'system_core',
    ('Prompt', 5): 'bible',
    ('Prompt', 6): 'volume',
    ('Prompt', 8): 'list[str]',
    ('Prompt', 9): 'rag_snippets',
    ('Prompt', 10): 'prev_tail',
    ('Prompt', 11): 'instruction',
    ('Prompt', 16): 'strict',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[str]',
    ('audit', 0): '扫描稳定层里的隐形缓存失效源。返回问题描述列表。',
    ('audit', 1): 'system_core',
    ('audit', 2): 'bible',
    ('audit', 3): 'volume',
    ('audit', 4): '稳定层 ',
    ('audit', 5): ' 含 ',
    ('audit', 6): '（',
    ('audit', 7): '）—— 每次请求前缀都会变，缓存必然 miss',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('prefix_fingerprint', 0): '稳定前缀的指纹。\n\n同一卷内逐章调用时，这个值必须不变。变了就说明有东西污染了前缀——\n这是缓存命中率掉下去时的第一排查手段。\n',
    ('prefix_fingerprint', 1): '\x00',
    ('prefix_fingerprint', 2): 'utf-8',
    ('__annotate__', 1): 'strict',
    ('__annotate__', 2): 'bool',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('validate', 0): '出手前的护栏。backends 在 render() 里调用。',
    ('validate', 1): 'system_core 不可为空',
    ('validate', 2): 'instruction 不可为空 —— 模型不知道要做什么',
    ('validate', 3): '检测到缓存失效源：\n  - ',
    ('validate', 4): '\n  - ',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[str]',
    ('stable_layers', 0): '缓存前缀的各层，按物理顺序。空层已剔除。',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('render_rag', 1): '\n【参照 ',
    ('render_rag', 2): '】\n',
    ('render_rag', 4): '</风格参照>',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('describe', 0): '人类可读的分层报告，调试用。',
    ('describe', 1): '缓存前缀指纹: ',
    ('describe', 2): '  system_core : ',
    ('describe', 3): '>7,',
    ('describe', 4): ' 字符  [稳定]',
    ('describe', 5): '  bible       : ',
    ('describe', 6): ' 字符  ',
    ('describe', 7): '[稳定]',
    ('describe', 8): '(空)',
    ('describe', 9): '  volume      : ',
    ('describe', 10): '  rag         : ',
    ('describe', 11): ' 字符  (易变)',
    ('describe', 12): '  prev_tail   : ',
    ('describe', 13): '  instruction : ',
    ('describe', 14): '⚠ 缓存失效源:',
    ('<genexpr>', 0): '    - ',
}

# 稳定层里的隐形缓存失效源：日期时间戳 / UUID。一旦出现在稳定层，
# 前缀就会逐次变化，缓存必然 miss。
_INVALIDATORS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r'\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}'), 'ISO 时间戳'),
    (re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'), 'UUID'),
]

# RAG 片段的防抄袭提示头。检索语料只是"参考"，不是"复制素材"。
_RAG_HEADER = '<风格参照>\n以下片段来自参考语料，**仅供体会**叙述节奏、情绪推进方式与对话质感。\n严禁复用其中任何原句、原比喻、原台词、原意象组合。\n如果你发现自己正在改写其中某一句，立刻停下，换一个完全不同的写法。\n'


class PromptLayerError(Exception):
    '分层约束被违反 —— 通常意味着缓存会失效。'
    # TODO(重建): 基类未在反汇编中直接体现，假定为 Exception。


def stable_json(obj: Any) -> str:
    '确定性序列化。\n\n`sort_keys=True` 不是洁癖：Python dict 的插入顺序会随构造路径变化，\n序列化出的字节不同 → 前缀不同 → 缓存永远 miss，且没有任何报错。\n'
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2)


@dataclass
class Prompt:
    '一次调用的分层内容。字段顺序即 prompt 中的物理顺序。'
    system_core: str
    bible: str = ''
    volume: str = ''
    rag_snippets: list[str] = field(default_factory=list)
    prev_tail: str = ''
    instruction: str = ''

    def audit(self) -> list[str]:
        '扫描稳定层里的隐形缓存失效源。返回问题描述列表。'
        problems = []
        for layer_name, text in [
            ('system_core', self.system_core),
            ('bible', self.bible),
            ('volume', self.volume),
        ]:
            for pattern, label in _INVALIDATORS:
                match = pattern.search(text)
                if match:
                    problems.append('稳定层 ' + layer_name + ' 含 ' + label + '（' + repr(match.group()) + '）—— 每次请求前缀都会变，缓存必然 miss')
        return problems

    def prefix_fingerprint(self) -> str:
        '稳定前缀的指纹。\n\n同一卷内逐章调用时，这个值必须不变。变了就说明有东西污染了前缀——\n这是缓存命中率掉下去时的第一排查手段。\n'
        blob = '\x00'.join((self.system_core, self.bible, self.volume))
        return hashlib.sha256(blob.encode('utf-8')).hexdigest()[:16]

    def validate(self, *, strict: bool = True) -> None:
        '出手前的护栏。backends 在 render() 里调用。'
        if not self.system_core.strip():
            raise PromptLayerError('system_core 不可为空')
        if not self.instruction.strip():
            raise PromptLayerError('instruction 不可为空 —— 模型不知道要做什么')
        problems = self.audit()
        if problems:
            if strict:
                raise PromptLayerError('检测到缓存失效源：\n  - ' + '\n  - '.join(problems))
            return None
        return None

    def stable_layers(self) -> list[str]:
        '缓存前缀的各层，按物理顺序。空层已剔除。'
        return [t for t in (self.bible, self.volume) if t.strip()]

    def render_rag(self) -> str:
        '\n【参照 '
        parts = [_RAG_HEADER]
        for i, snippet in enumerate(self.rag_snippets, 1):
            parts.append('\n【参照 ' + str(i) + '】\n' + str(snippet.strip()) + '\n')
        parts.append('</风格参照>')
        return ''.join(parts)

    def describe(self) -> str:
        '人类可读的分层报告，调试用。'
        lines = [
            f'缓存前缀指纹: {self.prefix_fingerprint()}',
            f'  system_core : {len(self.system_core):>7,} 字符  [稳定]',
            f'  bible       : {len(self.bible):>7,} 字符  ' + ('[稳定]' if self.bible.strip() else '(空)'),
            f'  volume      : {len(self.volume):>7,} 字符  ' + ('[稳定]' if self.volume.strip() else '(空)'),
            f'  rag         : {len(self.render_rag()) if self.rag_snippets else 0:>7,} 字符  (易变)',
            f'  prev_tail   : {len(self.prev_tail):>7,} 字符  (易变)',
            f'  instruction : {len(self.instruction):>7,} 字符  (易变)',
        ]
        problems = self.audit()
        if problems:
            lines.append('⚠ 缓存失效源:')
            lines.extend('    - ' + p for p in problems)
        return '\n'.join(lines)
