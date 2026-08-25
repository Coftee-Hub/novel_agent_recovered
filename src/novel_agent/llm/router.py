# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/llm/router.py
# 来源   : router.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '模型分层路由 + 成本核算。'

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .backends.base import ProviderConfig

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '模型分层路由 + 成本核算。',
    10: 'RoleConfig',
    12: 'Router',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('RoleConfig', 0): 'RoleConfig',
    ('RoleConfig', 1): 'str',
    ('RoleConfig', 2): 'role',
    ('RoleConfig', 3): 'provider',
    ('RoleConfig', 4): 'model',
    ('RoleConfig', 5): 'str | None',
    ('RoleConfig', 6): 'effort',
    ('RoleConfig', 7): 'int',
    ('RoleConfig', 8): 'max_tokens',
    ('RoleConfig', 9): 'tuple[tuple[str, str], ...]',
    ('RoleConfig', 10): 'fallbacks',
    ('Router', 0): 'Router',
    ('__annotate__', 1): 'config_path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('__init__', 0): 'utf-8',
    ('__init__', 1): 'default_provider',
    ('__init__', 2): 'anthropic',
    ('__init__', 3): 'providers',
    ('__init__', 4): 'kind',
    ('__init__', 5): 'api_key_env',
    ('__init__', 6): 'base_url',
    ('__init__', 7): 'supports_effort',
    ('__init__', 9): 'auth_style',
    ('__init__', 10): 'api_key',
    ('__init__', 11): 'max_retries',
    ('__init__', 12): 'retry_on_status',
    ('__init__', 13): 'retry_max_wait',
    ('__init__', 15): 'supports_structured_output',
    ('__init__', 16): 'merge_consecutive_user',
    ('__init__', 18): 'roles',
    ('__init__', 19): 'provider',
    ('__init__', 20): ', ',
    ('__init__', 21): '角色 ',
    ('__init__', 22): ' 指定了未定义的供应商 ',
    ('__init__', 23): '。已定义：',
    ('__init__', 24): 'fallbacks',
    ('__init__', 25): ' 的降级链引用了未定义的供应商 ',
    ('__init__', 26): 'model',
    ('__init__', 27): 'effort',
    ('__init__', 28): 'max_tokens',
    ('__init__', 30): 'pricing',
    ('__init__', 31): 'cache_multipliers',
    ('__annotate__', 1): 'role',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'RoleConfig',
    ('for_role', 0): ', ',
    ('for_role', 1): '未知角色 ',
    ('for_role', 2): '，已配置的角色：',
    ('__annotate__', 1): 'name',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'ProviderConfig',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'set[str]',
    ('__annotate__', 1): 'model',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict[str, float] | None',
    ('__annotate__', 1): 'model',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'usage',
    ('__annotate__', 4): 'Any',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'float',
    ('cost_usd', 0): '按 usage 算这次调用的美元成本。未在计价表里的模型返回 0。',
    ('cost_usd', 3): 'input',
    ('cost_usd', 4): 'output',
    ('cost_usd', 5): 'input_tokens',
    ('cost_usd', 6): 'cache_created',
    ('cost_usd', 7): 'write_5m',
    ('cost_usd', 8): 'cache_read',
    ('cost_usd', 9): 'read',
    ('cost_usd', 10): 'output_tokens',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
@dataclass
class RoleConfig:
    role: str
    provider: str
    model: str
    effort: str | None
    max_tokens: int
    fallbacks: tuple[tuple[str, str], ...] = ()


class Router:
    def __init__(self, config_path: str | Path) -> None:
        'utf-8'
        data = yaml.safe_load(Path(config_path).read_text('utf-8'))
        default = data.get('default_provider', 'anthropic')
        self._providers = {
            name: ProviderConfig(
                name=name,
                kind=cfg['kind'],
                api_key_env=cfg['api_key_env'],
                base_url=cfg.get('base_url'),
                supports_effort=cfg.get('supports_effort', True),
                auth_style=cfg.get('auth_style', 'api_key'),
                max_retries=cfg.get('max_retries', 4),
                retry_on_status=cfg.get('retry_on_status', []),
                retry_max_wait=cfg.get('retry_max_wait', 8.0),
                supports_structured_output=cfg.get('supports_structured_output'),
                merge_consecutive_user=cfg.get('merge_consecutive_user', True),
            )
            for name, cfg in data['providers'].items()
        }
        self._roles = {}
        for name, cfg in data['roles'].items():
            provider = cfg.get('provider', default)
            if provider not in self._providers:
                known = ', '.join(sorted(self._providers))
                raise ValueError('角色 ' + repr(name) + ' 指定了未定义的供应商 ' + repr(provider) + '。已定义：' + known)
            fallbacks = []
            for fb in cfg.get('fallbacks', []):
                fb_provider = fb['provider']
                if fb_provider not in self._providers:
                    raise ValueError('角色 ' + repr(name) + ' 的降级链引用了未定义的供应商 ' + repr(fb_provider))
                fallbacks.append((fb_provider, fb.get('model', cfg['model'])))
            self._roles[name] = RoleConfig(
                role=name,
                provider=provider,
                model=cfg['model'],
                effort=cfg.get('effort'),
                max_tokens=cfg['max_tokens'],
                fallbacks=tuple(fallbacks),
            )
        self._pricing = data.get('pricing', {})
        self._mult = data['cache_multipliers']

    def for_role(self, role: str) -> RoleConfig:
        ', '
        try:
            return self._roles[role]
        except KeyError:
            known = ', '.join(sorted(self._roles))
            raise KeyError('未知角色 ' + repr(role) + '，已配置的角色：' + known) from None

    def provider(self, name: str) -> ProviderConfig:
        return self._providers[name]

    @property
    def providers_in_use(self) -> set[str]:
        used = {r.provider for r in self._roles.values()}
        for r in self._roles.values():
            used |= {p for p, _ in r.fallbacks}
        return used

    def _prices(self, model: str) -> dict[str, float] | None:
        if model in self._pricing:
            return self._pricing[model]
        for key, prices in self._pricing.items():
            if model.startswith(key):
                return prices
        return None

    def cost_usd(self, model: str, usage: Any) -> float:
        '按 usage 算这次调用的美元成本。未在计价表里的模型返回 0。'
        prices = self._prices(model)
        if prices is None:
            return 0.0
        get = lambda field: getattr(usage, field, None) or 0
        in_price, out_price = prices['input'], prices['output']
        total = (
            get('input_tokens') * in_price
            + get('cache_created') * in_price * self._mult['write_5m']
            + get('cache_read') * in_price * self._mult['read']
            + get('output_tokens') * out_price
        )
        return total / 1000000
