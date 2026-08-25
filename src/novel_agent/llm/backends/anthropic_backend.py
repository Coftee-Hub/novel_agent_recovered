# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/llm/backends/anthropic_backend.py
# 来源   : anthropic_backend.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = 'Anthropic 后端 —— 显式 cache_control 断点。'

import os
from typing import Any

from pydantic import BaseModel

from ..prompt_builder import Prompt
from .base import Backend, ProviderConfig, RawResult

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'Anthropic 后端 —— 显式 cache_control 断点。',
    7: 'type',
    8: 'ephemeral',
    9: 'dict[str, str]',
    10: 'CACHE',
    12: 'AnthropicBackend',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('AnthropicBackend', 0): 'AnthropicBackend',
    ('AnthropicBackend', 1): 'anthropic',
    ('__annotate__', 1): 'config',
    ('__annotate__', 2): 'ProviderConfig',
    ('__annotate__', 3): 'client',
    ('__annotate__', 4): 'Any',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('__init__', 1): 'bearer',
    ('__init__', 2): 'auth_token',
    ('__init__', 3): 'api_key',
    ('__init__', 4): 'base_url',
    ('__annotate__', 1): 'prompt',
    ('__annotate__', 2): 'Prompt',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict[str, Any]',
    ('render', 0): 'type',
    ('render', 1): 'text',
    ('render', 2): 'cache_control',
    ('render', 3): 'role',
    ('render', 4): 'user',
    ('render', 5): 'content',
    ('render', 6): 'system',
    ('render', 7): 'messages',
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
    ('call', 0): 'model',
    ('call', 1): 'max_tokens',
    ('call', 2): 'effort',
    ('call', 3): 'output_config',
    ('call', 6): 'input_tokens',
    ('call', 7): 'output_tokens',
    ('call', 8): 'cache_read_input_tokens',
    ('call', 9): 'cache_creation_input_tokens',
    ('call', 10): 'parsed_output',
    ('call', 12): 'stop_reason',
    ('call', 13): '_request_id',
    ('<genexpr>', 0): 'text',
    ('__annotate__', 1): 'kwargs',
    ('__annotate__', 2): 'dict[str, Any]',
    ('__annotate__', 3): 'output_format',
    ('__annotate__', 4): 'type[BaseModel] | None',
    ('__annotate__', 5): 'model',
    ('__annotate__', 6): 'str',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'Any',
    ('_invoke', 5): 'output_config',
    ('__annotate__', 1): 'kw',
    ('__annotate__', 2): 'dict[str, Any]',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'Any',
    ('send', 1): 'output_format',
}

# cache_control 断点标记 —— Anthropic 专用。
CACHE: dict[str, str] = {'type': 'ephemeral'}


class AnthropicBackend(Backend):
    kind = 'anthropic'

    def __init__(self, config: ProviderConfig, client: Any = None) -> None:
        'bearer'
        super().__init__(config)
        if client is not None:
            self._client = client
            return None
        import anthropic
        secret = os.environ.get(config.api_key_env)
        kw = {}
        if secret:
            if config.auth_style == 'bearer':
                kw['auth_token'] = secret
            else:
                kw['api_key'] = secret
        if config.base_url:
            kw['base_url'] = config.base_url
        self._client = anthropic.Anthropic(**kw)
        return None

    def render(self, prompt: Prompt) -> dict[str, Any]:
        'type'
        prompt.validate()
        system = [{'type': 'text', 'text': prompt.system_core, 'cache_control': dict(CACHE)}]
        messages = [
            {'role': 'user', 'content': [{'type': 'text', 'text': layer, 'cache_control': dict(CACHE)}]}
            for layer in prompt.stable_layers()
        ]
        messages.append({
            'role': 'user',
            'content': [{'type': 'text', 'text': self._tail_text(prompt)}],
        })
        return {'system': system, 'messages': messages}

    def call(
        self,
        prompt: Prompt,
        model: str,
        max_tokens: int,
        effort: str | None = None,
        output_format: type[BaseModel] | None = None,
        **overrides: Any,
    ) -> RawResult:
        'model'
        kwargs = {
            'model': model,
            'max_tokens': max_tokens,
            **self.render(prompt),
            **overrides,
        }
        if effort and self.config.supports_effort and model not in self._unsupported:
            kwargs['output_config'] = {'effort': effort}
        response = self._invoke(kwargs, output_format, model)
        usage = response.usage
        return RawResult(
            text=''.join(b.text for b in response.content if b.type == 'text'),
            model=getattr(response, 'model', model),
            input_tokens=getattr(usage, 'input_tokens', 0) or 0,
            output_tokens=getattr(usage, 'output_tokens', 0) or 0,
            cache_read=getattr(usage, 'cache_read_input_tokens', 0) or 0,
            cache_created=getattr(usage, 'cache_creation_input_tokens', 0) or 0,
            parsed=getattr(response, 'parsed_output', None) if output_format else None,
            stop_reason=getattr(response, 'stop_reason', None),
            request_id=getattr(response, '_request_id', None),
        )

    def _invoke(self, kwargs: dict[str, Any], output_format: type[BaseModel] | None, model: str) -> Any:
        'output_config'
        import anthropic

        def send(kw: dict[str, Any]) -> Any:
            'output_format'
            if output_format is not None:
                return self._client.messages.parse(*(), output_format=output_format, **kw)
            if self.config.stream:
                with self._client.messages.stream(*(), **kw) as stream:
                    return stream.get_final_message()
            return self._client.messages.create(*(), **kw)

        try:
            return self._retry(lambda: send(kwargs))
        except (anthropic.BadRequestError, TypeError) as exc:
            if 'output_config' not in kwargs or 'output_config' not in str(exc):
                raise
            self._unsupported.add(model)
            stripped = {k: v for k, v in kwargs.items() if k != 'output_config'}
            return self._retry(lambda: send(stripped))
