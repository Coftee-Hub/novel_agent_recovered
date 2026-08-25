from .anthropic_backend import AnthropicBackend
from .base import Backend, ProviderConfig, RawResult
from .openai_backend import OpenAIBackend

_BY_KIND: dict[str, type[Backend]] = {
    "anthropic": AnthropicBackend,
    "openai": OpenAIBackend,
}


def build_backend(config: ProviderConfig, client=None) -> Backend:
    try:
        cls = _BY_KIND[config.kind]
    except KeyError:
        known = ", ".join(sorted(_BY_KIND))
        raise ValueError(
            f"未知的供应商类型 {config.kind!r}（供应商 {config.name!r}）。可用：{known}"
        ) from None
    return cls(config, client=client)


__all__ = ["AnthropicBackend", "Backend", "OpenAIBackend", "ProviderConfig",
           "RawResult", "build_backend"]
