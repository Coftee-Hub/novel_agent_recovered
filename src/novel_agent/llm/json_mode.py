# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/llm/json_mode.py
# 来源   : json_mode.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '结构化输出的兜底路径 —— 把 schema 写进 prompt，再宽松解析回来。\n\n为什么需要：不是每个端点都支持 `output_config.format`。中转站尤其常见\n把它整个剥掉（实测 PackyAPI 会），此时模型会照自己的习惯输出散文或\nmarkdown，`messages.parse()` 直接 JSON 解析失败。\n\n这条路径在任何模型上都能用，代价是多占一点 token、且需要宽松解析。\n'

import json
from typing import Any

from pydantic import BaseModel

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '结构化输出的兜底路径 —— 把 schema 写进 prompt，再宽松解析回来。\n\n为什么需要：不是每个端点都支持 `output_config.format`。中转站尤其常见\n把它整个剥掉（实测 PackyAPI 会），此时模型会照自己的习惯输出散文或\nmarkdown，`messages.parse()` 直接 JSON 解析失败。\n\n这条路径在任何模型上都能用，代价是多占一点 token、且需要宽松解析。\n',
    5: '\n## 输出格式（必须严格遵守）\n\n只输出**一个 JSON 对象**。不要有任何解释、前言、结语，不要用 ``` 包裹。\n第一个字符必须是 `{`，最后一个字符必须是 `}`。\n\nJSON 必须符合下面的 schema：\n\n{schema}\n',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'instruction',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'model',
    ('__annotate__', 4): 'type[BaseModel]',
    ('__annotate__', 5): 'return',
    ('augment', 0): '把 schema 追加到指令末尾。\n\n放末尾而非开头：指令区是易变层，不影响缓存前缀；且模型对结尾的\n格式要求服从度更高。\n',
    ('augment', 3): '{schema}',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('extract', 0): '从可能带杂质的回复里抠出 JSON 主体。\n\n实际会遇到的杂质：```json 围栏、"好的，这是大纲："之类的前言、\n末尾补充说明。策略是取第一个 { 到最后一个 } —— 对本项目的单对象\n输出足够，且比正则健壮。\n',
    ('extract', 1): '```',
    ('extract', 3): '{',
    ('extract', 4): '}',
    ('extract', 5): '回复里找不到 JSON 对象（前 80 字符：',
    ('extract', 7): '）',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'model',
    ('__annotate__', 4): 'type[BaseModel]',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'BaseModel',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'bool',
    ('looks_like_json', 0): '判断端点是否真的受理了结构化输出请求。\n\n用于自动探测：请求了结构化输出却回来散文，说明该端点把参数吞了。\n',
    ('looks_like_json', 1): '{',
    ('__annotate__', 1): 'model',
    ('__annotate__', 2): 'type[BaseModel]',
    ('__annotate__', 3): 'error',
    ('__annotate__', 4): 'Exception',
    ('__annotate__', 5): 'bad',
    ('__annotate__', 6): 'str',
    ('__annotate__', 7): 'return',
    ('repair_instruction', 0): '一次修复请求。比整轮重跑便宜得多。',
    ('repair_instruction', 1): '你上一次的输出无法解析成要求的 JSON。\n\n错误：',
    ('repair_instruction', 2): '\n\n你输出的内容（前 500 字符）：\n',
    ('repair_instruction', 4): '\n\n请重新输出，只输出一个符合 schema 的 JSON 对象，第一个字符是 `{`，最后一个字符是 `}`，不要任何其他文字。\n\nschema：\n',
    ('__annotate__', 1): 'obj',
    ('__annotate__', 2): 'Any',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
}

# 输出格式模板（100% 原样）。{schema} 占位符在运行时被替换。
_INSTRUCTION = '\n## 输出格式（必须严格遵守）\n\n只输出**一个 JSON 对象**。不要有任何解释、前言、结语，不要用 ``` 包裹。\n第一个字符必须是 `{`，最后一个字符必须是 `}`。\n\nJSON 必须符合下面的 schema：\n\n{schema}\n'


def augment(instruction: str, model: type[BaseModel]) -> str:
    '把 schema 追加到指令末尾。\n\n放末尾而非开头：指令区是易变层，不影响缓存前缀；且模型对结尾的\n格式要求服从度更高。\n'
    schema = json.dumps(model.model_json_schema(), ensure_ascii=False, indent=2)
    return instruction + _INSTRUCTION.replace('{schema}', schema)


def extract(text: str) -> str:
    '从可能带杂质的回复里抠出 JSON 主体。\n\n实际会遇到的杂质：```json 围栏、"好的，这是大纲："之类的前言、\n末尾补充说明。策略是取第一个 { 到最后一个 } —— 对本项目的单对象\n输出足够，且比正则健壮。\n'
    cleaned = text.strip()
    if cleaned.startswith('```'):
        cleaned = cleaned.split('\n', 1)[-1]
        if '```' in cleaned:
            cleaned = cleaned.rsplit('```', 1)[0]
        cleaned = cleaned.strip()
    start = cleaned.find('{')
    end = cleaned.rfind('}')
    if start == -1 or end <= start:
        raise ValueError('回复里找不到 JSON 对象（前 80 字符：' + repr(text[:80]) + '）')
    return cleaned[start:end + 1]


def parse_into(text: str, model: type[BaseModel]) -> BaseModel:
    return model.model_validate_json(extract(text))


def looks_like_json(text: str) -> bool:
    '判断端点是否真的受理了结构化输出请求。\n\n用于自动探测：请求了结构化输出却回来散文，说明该端点把参数吞了。\n'
    stripped = text.strip()
    if not stripped.startswith('{'):
        return False
    try:
        json.loads(stripped)
    except json.JSONDecodeError:
        return False
    return True


def repair_instruction(model: type[BaseModel], error: Exception, bad: str) -> str:
    '一次修复请求。比整轮重跑便宜得多。'
    return (
        '你上一次的输出无法解析成要求的 JSON。\n\n错误：'
        + str(error)
        + '\n\n你输出的内容（前 500 字符）：\n'
        + str(bad[:500])
        + '\n\n请重新输出，只输出一个符合 schema 的 JSON 对象，第一个字符是 `{`，最后一个字符是 `}`，不要任何其他文字。\n\nschema：\n'
        + str(json.dumps(model.model_json_schema(), ensure_ascii=False, indent=2))
    )


def as_dict(obj: Any) -> dict:
    if isinstance(obj, dict):
        return obj
    return json.loads(obj)
