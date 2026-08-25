"""OpenAI 兼容后端。

一个适配器覆盖绝大多数替代品：OpenAI、DeepSeek、通义千问、智谱 GLM、
Kimi、MiniMax、以及本地 Ollama / vLLM —— 它们都提供 OpenAI 兼容端点，
换 base_url 即可。

与 Anthropic 的两处实质差异：
1. 缓存是**自动**的前缀匹配，没有断点可放。分层顺序照样决定命中率。
2. usage 语义不同：OpenAI 的 prompt_tokens **含**已缓存部分，而
   Anthropic 的 input_tokens 是未缓存余量。这里做了归一化，否则成本会重复计算。
"""

from __future__ import annotations

import json
import os
from typing import Any

from pydantic import BaseModel

from ..prompt_builder import Prompt
from .base import Backend, ProviderConfig, RawResult


class OpenAIBackend(Backend):
    kind = "openai"

    def __init__(self, config: ProviderConfig, client: Any = None) -> None:
        super().__init__(config)
        if client is not None:
            self._client = client
        else:
            try:
                from openai import OpenAI
            except ImportError as exc:
                raise ImportError(
                    "需要 openai 包：uv pip install -e '.[openai]'"
                ) from exc
            self._client = OpenAI(
                api_key=os.environ.get(config.api_key_env, "unused"),
                base_url=config.base_url,
            )

    def render(self, prompt: Prompt) -> dict[str, Any]:
        prompt.validate()
        messages: list[dict[str, str]] = [
            {"role": "system", "content": prompt.system_core}
        ]
        stable = prompt.stable_layers()
        tail = self._tail_text(prompt)

        if self.config.merge_consecutive_user:
            # 合并成单条 user。缓存看 token 前缀而非消息边界，合并不影响命中；
            # 但能兼容要求 user/assistant 严格交替的服务。
            messages.append({"role": "user", "content": "\n\n".join([*stable, tail])})
        else:
            messages += [{"role": "user", "content": layer} for layer in stable]
            messages.append({"role": "user", "content": tail})
        return {"messages": messages}

    def call(
        self,
        prompt: Prompt,
        model: str,
        max_tokens: int,
        effort: str | None = None,
        output_format: type[BaseModel] | None = None,
        **overrides: Any,
    ) -> RawResult:
        kwargs: dict[str, Any] = {
            "model": model,
            "max_tokens": max_tokens,
            **self.render(prompt),
            **overrides,
        }
        if effort and self.config.supports_effort and model not in self._unsupported:
            kwargs["reasoning_effort"] = effort
        if output_format is not None:
            kwargs["response_format"] = _json_schema_format(output_format)

        response = self._invoke(kwargs, model)
        choice = response.choices[0]
        text = choice.message.content or ""

        parsed = None
        if output_format is not None:
            parsed = output_format.model_validate_json(text)

        return RawResult(
            text=text,
            model=getattr(response, "model", model),
            parsed=parsed,
            stop_reason=getattr(choice, "finish_reason", None),
            request_id=getattr(response, "id", None),
            **_normalize_usage(getattr(response, "usage", None)),
        )

    def _invoke(self, kwargs: dict[str, Any], model: str) -> Any:
        """逐级降级：严格 schema → json_object → 纯文本。

        兼容端的能力参差不齐，硬失败不如降级 —— 但每次降级都记住，不重复试探。
        """
        try:
            return self._client.chat.completions.create(**kwargs)
        except Exception as exc:  # noqa: BLE001 — 各家 SDK 异常类型不统一
            msg = str(exc)
            retry = dict(kwargs)
            changed = False

            if "reasoning_effort" in retry and "reasoning_effort" in msg:
                retry.pop("reasoning_effort")
                self._unsupported.add(model)
                changed = True
            if "response_format" in retry and (
                "response_format" in msg or "json_schema" in msg
            ):
                retry["response_format"] = {"type": "json_object"}
                changed = True
            if not changed:
                raise
            try:
                return self._client.chat.completions.create(**retry)
            except Exception:
                retry.pop("response_format", None)
                return self._client.chat.completions.create(**retry)


def _json_schema_format(model: type[BaseModel]) -> dict[str, Any]:
    return {
        "type": "json_schema",
        "json_schema": {
            "name": model.__name__,
            "strict": True,
            "schema": model.model_json_schema(),
        },
    }


def _normalize_usage(usage: Any) -> dict[str, int]:
    """把各家 usage 归一到 Anthropic 语义（input_tokens = 未缓存余量）。"""
    if usage is None:
        return {"input_tokens": 0, "output_tokens": 0, "cache_read": 0, "cache_created": 0}

    prompt_tokens = getattr(usage, "prompt_tokens", 0) or 0
    completion = getattr(usage, "completion_tokens", 0) or 0

    # OpenAI: usage.prompt_tokens_details.cached_tokens
    details = getattr(usage, "prompt_tokens_details", None)
    cached = getattr(details, "cached_tokens", 0) or 0 if details else 0
    # DeepSeek 等：prompt_cache_hit_tokens / prompt_cache_miss_tokens
    if not cached:
        cached = getattr(usage, "prompt_cache_hit_tokens", 0) or 0

    return {
        "input_tokens": max(prompt_tokens - cached, 0),  # 关键：去掉已缓存部分
        "output_tokens": completion,
        "cache_read": cached,
        "cache_created": 0,  # 自动缓存不区分写入，无从统计
    }


def parse_json_lenient(text: str) -> Any:
    """兼容端有时会把 JSON 包在 ```json 围栏里。"""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[-1].rsplit("```", 1)[0]
    return json.loads(cleaned)
