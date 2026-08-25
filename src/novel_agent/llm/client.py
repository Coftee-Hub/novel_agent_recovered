# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/llm/client.py
# 来源   : client.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '统一调用入口 —— 路由到后端、归一化结果、记账。\n\n刻意不引入 LangChain：本项目需要在指定内容块上精确放 cache_control，\nLangChain 对此是间接支持，静默失效的代价（成本翻数倍且无报错）太高。\nLangGraph 只负责编排，节点调用这里。\n'

import json
import time
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, TypeVar

from pydantic import BaseModel, ValidationError

from . import json_mode
from .backends import build_backend
from .backends.base import Backend
from .prompt_builder import Prompt
from .router import Router

T = TypeVar('T')

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '统一调用入口 —— 路由到后端、归一化结果、记账。\n\n刻意不引入 LangChain：本项目需要在指定内容块上精确放 cache_control，\nLangChain 对此是间接支持，静默失效的代价（成本翻数倍且无报错）太高。\nLangGraph 只负责编排，节点调用这里。\n',
    11: 'T',
    14: 'CallResult',
    16: 'LLMClient',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('CallResult', 0): 'CallResult',
    ('CallResult', 1): 'str',
    ('CallResult', 2): 'text',
    ('CallResult', 3): 'model',
    ('CallResult', 4): 'provider',
    ('CallResult', 5): 'role',
    ('CallResult', 6): 'float',
    ('CallResult', 7): 'cost_usd',
    ('CallResult', 8): 'int',
    ('CallResult', 9): 'input_tokens',
    ('CallResult', 10): 'output_tokens',
    ('CallResult', 11): 'cache_read',
    ('CallResult', 12): 'cache_created',
    ('CallResult', 13): 'elapsed_s',
    ('CallResult', 14): 'str | None',
    ('CallResult', 15): 'stop_reason',
    ('CallResult', 16): 'prefix_fingerprint',
    ('CallResult', 18): 'BaseModel | None',
    ('CallResult', 19): 'parsed',
    ('CallResult', 20): 'request_id',
    ('CallResult', 22): 'bool',
    ('CallResult', 23): 'degraded',
    ('CallResult', 24): 'attempts',
    ('CallResult', 26): 'retry_wait_s',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'bool',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('total_input', 0): '真实的 prompt 总量。input_tokens 只是未缓存余量，单看它会严重低估。',
    ('LLMClient', 0): 'LLMClient',
    ('__annotate__', 1): 'router',
    ('__annotate__', 2): 'Router',
    ('__annotate__', 3): 'log_path',
    ('__annotate__', 4): 'str | Path | None',
    ('__annotate__', 5): 'backends',
    ('__annotate__', 6): 'dict[str, Backend] | None',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'None',
    ('__annotate__', 1): 'provider',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'Backend',
    ('backend_for', 0): '按需构造后端 —— 没用到的供应商不会去碰它的 SDK 或环境变量。',
    ('__annotate__', 1): 'role',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'prompt',
    ('__annotate__', 4): 'Prompt',
    ('__annotate__', 5): 'overrides',
    ('__annotate__', 6): 'Any',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'CallResult',
    ('complete', 0): '自由文本生成（writer / stitcher / architect 的散文部分）。',
    ('__annotate__', 1): 'role',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'prompt',
    ('__annotate__', 4): 'Prompt',
    ('__annotate__', 5): 'output_format',
    ('__annotate__', 6): 'type[T]',
    ('__annotate__', 7): 'overrides',
    ('__annotate__', 8): 'Any',
    ('__annotate__', 9): 'return',
    ('__annotate__', 10): 'CallResult',
    ('parse', 0): '结构化输出（architect 大纲 / judge 评分 / archivist 的 state patch）。\n\n两条路径：\n1. 原生 `output_config.format` —— 端点支持时最可靠\n2. 把 schema 写进 prompt + 宽松解析 —— 端点不支持时的兜底\n\n走哪条由供应商配置决定；配成 None（未知）时第一次调用自动探测，\n探到端点吞参数就记住，之后不再浪费调用。\n',
    ('__annotate__', 1): 'role',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'prompt',
    ('__annotate__', 4): 'Prompt',
    ('__annotate__', 5): 'output_format',
    ('__annotate__', 6): 'type[T]',
    ('__annotate__', 7): 'overrides',
    ('__annotate__', 8): 'Any',
    ('__annotate__', 9): 'return',
    ('__annotate__', 10): 'CallResult',
    ('_parse_via_prompt', 0): '兜底路径。schema 追加在 instruction（易变层），不动缓存前缀。',
    ('_parse_via_prompt', 3): '\n\n注意：上一次你没有输出任何内容。请直接输出 JSON，不要在推理上花太多篇幅。',
    ('__annotate__', 1): 'role',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'prompt',
    ('__annotate__', 4): 'Prompt',
    ('__annotate__', 5): 'output_format',
    ('__annotate__', 6): 'type[T] | None',
    ('__annotate__', 7): 'overrides',
    ('__annotate__', 8): 'Any',
    ('__annotate__', 9): 'return',
    ('__annotate__', 10): 'CallResult',
    ('_call', 1): 'model',
    ('_call', 2): 'max_tokens',
    ('_call', 3): 'effort',
    ('_call', 4): 'output_format',
    ('_call', 5): '    ⚠ ',
    ('_call', 6): '/',
    ('_call', 7): ' 重试耗尽（',
    ('_call', 8): '），降级到 ',
    ('__annotate__', 1): 'r',
    ('__annotate__', 2): 'CallResult',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('_log', 0): '逐行追加到 run_log.jsonl。\n\nprefix_fingerprint 是关键字段：同一卷内它必须恒定。一旦发现它在\n逐章调用间跳变，就是有东西污染了缓存前缀。\n',
    ('_log', 4): 'ts',
    ('_log', 5): '%Y-%m-%dT%H:%M:%S',
    ('_log', 6): 'role',
    ('_log', 7): 'provider',
    ('_log', 8): 'model',
    ('_log', 9): 'prefix_fingerprint',
    ('_log', 10): 'input_tokens',
    ('_log', 11): 'cache_read',
    ('_log', 12): 'cache_created',
    ('_log', 13): 'total_input',
    ('_log', 14): 'output_tokens',
    ('_log', 15): 'cost_usd',
    ('_log', 16): 'elapsed_s',
    ('_log', 17): 'attempts',
    ('_log', 18): 'retry_wait_s',
    ('_log', 19): 'stop_reason',
    ('_log', 20): 'request_id',
    ('_log', 21): 'degraded',
    ('_log', 22): 'a',
    ('_log', 23): 'utf-8',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
@dataclass
class CallResult:
    text: str
    model: str
    provider: str
    role: str
    cost_usd: float
    input_tokens: int
    output_tokens: int
    cache_read: int
    cache_created: int
    elapsed_s: float
    stop_reason: str | None
    prefix_fingerprint: str
    parsed: BaseModel | None = None
    request_id: str | None = None
    degraded: bool = False
    attempts: int = 1
    retry_wait_s: float = 0.0

    @property
    def cache_hit(self) -> bool:
        return self.cache_read > 0

    @property
    def total_input(self) -> int:
        '真实的 prompt 总量。input_tokens 只是未缓存余量，单看它会严重低估。'
        return self.input_tokens + self.cache_read + self.cache_created


class LLMClient:
    def __init__(
        self,
        router: Router,
        log_path: str | Path | None = None,
        backends: dict[str, Backend] | None = None,
    ) -> None:
        self.router = router
        self.log_path = Path(log_path) if log_path else None
        self._backends = backends or {}
        self._no_structured = set()

    def backend_for(self, provider: str) -> Backend:
        '按需构造后端 —— 没用到的供应商不会去碰它的 SDK 或环境变量。'
        if provider not in self._backends:
            self._backends[provider] = build_backend(self.router.provider(provider))
        return self._backends[provider]

    def complete(self, role: str, prompt: Prompt, **overrides: Any) -> CallResult:
        '自由文本生成（writer / stitcher / architect 的散文部分）。'
        return self._call(role, prompt, None, **overrides)

    def parse(self, role: str, prompt: Prompt, output_format: type[T], **overrides: Any) -> CallResult:
        '结构化输出（architect 大纲 / judge 评分 / archivist 的 state patch）。\n\n两条路径：\n1. 原生 `output_config.format` —— 端点支持时最可靠\n2. 把 schema 写进 prompt + 宽松解析 —— 端点不支持时的兜底\n\n走哪条由供应商配置决定；配成 None（未知）时第一次调用自动探测，\n探到端点吞参数就记住，之后不再浪费调用。\n'
        cfg = self.router.for_role(role)
        native = self.router.provider(cfg.provider).supports_structured_output
        if native is not False and cfg.provider not in self._no_structured:
            try:
                result = self._call(role, prompt, output_format, **overrides)
                if result.parsed is not None:
                    return result
                if result.text and json_mode.looks_like_json(result.text):
                    result.parsed = output_format.model_validate_json(result.text)
                    return result
                self._no_structured.add(cfg.provider)
            except (ValidationError, json.JSONDecodeError):
                self._no_structured.add(cfg.provider)
        return self._parse_via_prompt(role, prompt, output_format, **overrides)

    def _parse_via_prompt(self, role: str, prompt: Prompt, output_format: type[T] | None, **overrides: Any) -> CallResult:
        '兜底路径。schema 追加在 instruction（易变层），不动缓存前缀。'
        asked = replace(prompt, instruction=json_mode.augment(prompt.instruction, output_format))
        result = self._call(role, asked, None, **overrides)
        if not result.text.strip():
            result = self._call(role, replace(asked, instruction=asked.instruction + '\n\n注意：上一次你没有输出任何内容。请直接输出 JSON，不要在推理上花太多篇幅。'), None, **overrides)
        try:
            result.parsed = json_mode.parse_into(result.text, output_format)
            return result
        except (ValueError, ValidationError) as exc:
            repair = replace(prompt, instruction=json_mode.repair_instruction(output_format, exc, result.text))
            fixed = self._call(role, repair, None, **overrides)
            fixed.parsed = json_mode.parse_into(fixed.text, output_format)
            return fixed

    def _call(self, role: str, prompt: Prompt, output_format: type[T] | None, **overrides: Any) -> CallResult:
        'model'
        cfg = self.router.for_role(role)
        chain = [(cfg.provider, cfg.model)] + list(cfg.fallbacks)
        last = None
        for attempt, (provider_name, model) in enumerate(chain):
            backend = self.backend_for(provider_name)
            started = time.monotonic()
            try:
                raw = backend.call(
                    prompt,
                    model=model,
                    max_tokens=overrides.get('max_tokens', cfg.max_tokens),
                    effort=cfg.effort,
                    output_format=output_format,
                    **{k: v for k, v in overrides.items() if k != 'max_tokens'},
                )
                elapsed = time.monotonic() - started
                result = CallResult(
                    text=raw.text,
                    model=raw.model,
                    provider=provider_name,
                    role=role,
                    cost_usd=self.router.cost_usd(model, raw),
                    input_tokens=raw.input_tokens,
                    output_tokens=raw.output_tokens,
                    cache_read=raw.cache_read,
                    cache_created=raw.cache_created,
                    elapsed_s=elapsed,
                    stop_reason=raw.stop_reason,
                    prefix_fingerprint=prompt.prefix_fingerprint(),
                    parsed=raw.parsed,
                    request_id=raw.request_id,
                    degraded=attempt > 0,
                )
                self._log(result)
                return result
            except Exception as exc:
                last = exc
                remaining = len(chain) - attempt - 1
                if not remaining:
                    raise
                nxt = chain[attempt + 1]
                print(f'    ⚠ {provider_name}/{model} 重试耗尽（{type(exc).__name__}），降级到 {nxt[0]}/{nxt[1]}', flush=True)
        assert last is not None
        raise last

    def _log(self, r: CallResult) -> None:
        '逐行追加到 run_log.jsonl。\n\nprefix_fingerprint 是关键字段：同一卷内它必须恒定。一旦发现它在\n逐章调用间跳变，就是有东西污染了缓存前缀。\n'
        if self.log_path is None:
            return None
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        record = {
            'ts': time.strftime('%Y-%m-%dT%H:%M:%S'),
            'role': r.role,
            'provider': r.provider,
            'model': r.model,
            'prefix_fingerprint': r.prefix_fingerprint,
            'input_tokens': r.input_tokens,
            'cache_read': r.cache_read,
            'cache_created': r.cache_created,
            'total_input': r.total_input,
            'output_tokens': r.output_tokens,
            'cost_usd': round(r.cost_usd, 6),
            'elapsed_s': round(r.elapsed_s, 2),
            'attempts': r.attempts,
            'retry_wait_s': r.retry_wait_s,
            'stop_reason': r.stop_reason,
            'request_id': r.request_id,
            'degraded': r.degraded,
        }
        with self.log_path.open('a', encoding='utf-8') as fh:
            fh.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')
