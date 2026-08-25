# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/llm/backends/base.py
# 来源   : base.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '后端抽象 —— 让模型供应商可替换。\n\n分层 Prompt 是**跨供应商**的资产：无论显式断点（Anthropic）还是自动前缀\n缓存（OpenAI / DeepSeek / Kimi ...），缓存都是前缀匹配，"稳定层在前、\n易变层在后"这条规则对所有家都成立。差异只在如何把分层翻译成各家的请求形状。\n'

import random
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from pydantic import BaseModel

from ..prompt_builder import Prompt

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '后端抽象 —— 让模型供应商可替换。\n\n分层 Prompt 是**跨供应商**的资产：无论显式断点（Anthropic）还是自动前缀\n缓存（OpenAI / DeepSeek / Kimi ...），缓存都是前缀匹配，"稳定层在前、\n易变层在后"这条规则对所有家都成立。差异只在如何把分层翻译成各家的请求形状。\n',
    9: 'RawResult',
    11: 'ProviderConfig',
    13: 'Backend',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('RawResult', 0): 'RawResult',
    ('RawResult', 1): '各家响应归一化后的形状。',
    ('RawResult', 2): 'str',
    ('RawResult', 3): 'text',
    ('RawResult', 4): 'model',
    ('RawResult', 5): 'int',
    ('RawResult', 6): 'input_tokens',
    ('RawResult', 7): 'output_tokens',
    ('RawResult', 8): 'cache_read',
    ('RawResult', 9): 'cache_created',
    ('RawResult', 11): 'BaseModel | None',
    ('RawResult', 12): 'parsed',
    ('RawResult', 13): 'str | None',
    ('RawResult', 14): 'stop_reason',
    ('RawResult', 15): 'request_id',
    ('ProviderConfig', 0): 'ProviderConfig',
    ('ProviderConfig', 1): 'str',
    ('ProviderConfig', 2): 'name',
    ('ProviderConfig', 3): 'kind',
    ('ProviderConfig', 4): 'api_key_env',
    ('ProviderConfig', 6): 'str | None',
    ('ProviderConfig', 7): 'base_url',
    ('ProviderConfig', 9): 'bool',
    ('ProviderConfig', 10): 'supports_effort',
    ('ProviderConfig', 11): 'api_key',
    ('ProviderConfig', 12): 'auth_style',
    ('ProviderConfig', 13): 'int',
    ('ProviderConfig', 14): 'max_retries',
    ('ProviderConfig', 16): 'list[int]',
    ('ProviderConfig', 17): 'retry_on_status',
    ('ProviderConfig', 18): 'retry_on_connection_error',
    ('ProviderConfig', 20): 'float',
    ('ProviderConfig', 21): 'retry_max_wait',
    ('ProviderConfig', 22): 'stream',
    ('ProviderConfig', 23): 'bool | None',
    ('ProviderConfig', 24): 'supports_structured_output',
    ('ProviderConfig', 25): 'merge_consecutive_user',
    ('Backend', 0): 'Backend',
    ('Backend', 1): 'str',
    ('Backend', 2): 'kind',
    ('__annotate__', 1): 'config',
    ('__annotate__', 2): 'ProviderConfig',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('__annotate__', 1): 'prompt',
    ('__annotate__', 2): 'Prompt',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict[str, Any]',
    ('render', 0): '把分层 Prompt 翻译成本家的请求参数。',
    ('__annotate__', 1): 'prompt',
    ('__annotate__', 2): 'Prompt',
    ('__annotate__', 3): 'model',
    ('__annotate__', 4): 'str',
    ('__annotate__', 5): 'max_tokens',
    ('__annotate__', 6): 'int',
    ('__annotate__', 7): 'effort',
    ('__annotate__', 8): 'str | None',
    ('__annotate__', 9): 'output_format',
    ('__annotate__', 10): 'type[BaseModel] | None',
    ('__annotate__', 11): 'overrides',
    ('__annotate__', 12): 'Any',
    ('__annotate__', 13): 'return',
    ('__annotate__', 14): 'RawResult',
    ('call', 0): '发一次请求并归一化结果。',
    ('_retry', 0): '重试 SDK 自己不重试的失败。\n\n两类：\n1. 状态码 —— aws-q 这类逆向渠道会间歇性返回 422、cc-sale 号池会返回\n   403，而 SDK 按语义把它们当永久拒绝，不重试。\n2. 连接层 —— 断网、超时、连接重置。SDK 自带重试次数很少（通常 2 次），\n   实测一段几分钟的网络中断就能让整批任务全灭（萃取时 20 章连续失败）。\n',
    ('__annotate__', 1): 'exc',
    ('__annotate__', 2): 'Exception',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'bool',
    ('_retryable', 0): 'status_code',
    ('__annotate__', 1): 'prompt',
    ('__annotate__', 2): 'Prompt',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('_tail_text', 0): '把易变尾部拼成一段文本：RAG 片段 → 上文结尾 → 指令。\n\n指令必须在最后 —— 模型对结尾指令最敏感。\n',
    ('_tail_text', 1): '<上文结尾>\n',
    ('_tail_text', 2): '\n</上文结尾>',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
@dataclass
class RawResult:
    '各家响应归一化后的形状。'
    text: str
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read: int = 0
    cache_created: int = 0
    parsed: BaseModel | None = None
    stop_reason: str | None = None
    request_id: str | None = None


@dataclass
class ProviderConfig:
    name: str
    kind: str
    api_key_env: str
    base_url: str | None = None
    supports_effort: bool = True
    auth_style: str = 'api_key'
    max_retries: int = 4
    retry_on_status: list[int] = field(default_factory=list)
    retry_on_connection_error: bool = True
    retry_max_wait: float = 8.0
    stream: bool = True
    supports_structured_output: bool | None = None
    merge_consecutive_user: bool = True


class Backend(ABC):
    kind: str

    def __init__(self, config: ProviderConfig) -> None:
        self.config = config
        self._unsupported = set()
        self.last_attempts = 1
        self.last_retry_wait = 0.0

    @abstractmethod
    def render(self, prompt: Prompt) -> dict[str, Any]:
        '把分层 Prompt 翻译成本家的请求参数。'
        return None

    @abstractmethod
    def call(
        self,
        prompt: Prompt,
        model: str,
        max_tokens: int,
        effort: str | None = None,
        output_format: type[BaseModel] | None = None,
        **overrides: Any,
    ) -> RawResult:
        '发一次请求并归一化结果。'
        return None

    def _retry(self, send):
        '重试 SDK 自己不重试的失败。\n\n两类：\n1. 状态码 —— aws-q 这类逆向渠道会间歇性返回 422、cc-sale 号池会返回\n   403，而 SDK 按语义把它们当永久拒绝，不重试。\n2. 连接层 —— 断网、超时、连接重置。SDK 自带重试次数很少（通常 2 次），\n   实测一段几分钟的网络中断就能让整批任务全灭（萃取时 20 章连续失败）。\n'
        self.last_attempts = 1
        self.last_retry_wait = 0.0
        if not self.config.retry_on_status and not self.config.retry_on_connection_error:
            return send()
        last = None
        for attempt in range(self.config.max_retries + 1):
            self.last_attempts = attempt + 1
            try:
                return send()
            except Exception as exc:
                if not self._retryable(exc):
                    raise
                last = exc
                if attempt == self.config.max_retries:
                    break
                wait = min(0.5 * 2 ** attempt + random.uniform(0, 0.3), self.config.retry_max_wait)
                self.last_retry_wait += wait
                time.sleep(wait)
        assert last is not None
        raise last

    def _retryable(self, exc: Exception) -> bool:
        'status_code'
        if getattr(exc, 'status_code', None) in self.config.retry_on_status:
            return True
        if not self.config.retry_on_connection_error:
            return False
        name = type(exc).__name__
        return any(name in k for k in ('Connection', 'Timeout', 'TimedOut'))

    def _tail_text(self, prompt: Prompt) -> str:
        '把易变尾部拼成一段文本：RAG 片段 → 上文结尾 → 指令。\n\n指令必须在最后 —— 模型对结尾指令最敏感。\n'
        parts = []
        if prompt.rag_snippets:
            parts.append(prompt.render_rag())
        if prompt.prev_tail.strip():
            parts.append('<上文结尾>\n' + str(prompt.prev_tail) + '\n</上文结尾>')
        parts.append(prompt.instruction)
        return '\n\n'.join(parts)
