"""路由与成本核算的**算法**。

刻意用合成配置而非真实的 config/models.yaml：价目表和角色分工是会变的配置，
测试不该因为改了一次价格就变红。真实配置的接线意图由 test_config_wiring.py 守。
"""

from __future__ import annotations

from dataclasses import dataclass

import pytest
import yaml

from novel_agent.llm.router import Router

# 取整的合成价目，让成本断言一眼能验算
SYNTHETIC = {
    "default_provider": "main",
    "providers": {
        "main": {"kind": "anthropic", "api_key_env": "MAIN_KEY"},
        "proxy": {"kind": "anthropic", "api_key_env": "PROXY_KEY",
                  "base_url": "https://proxy.example", "auth_style": "bearer"},
        "cheap": {"kind": "openai", "api_key_env": "CHEAP_KEY",
                  "base_url": "https://cheap.example/v1", "supports_effort": False},
    },
    "roles": {
        "writer": {"model": "test-big", "effort": "high", "max_tokens": 8000},
        "judge": {"provider": "cheap", "model": "test-small", "max_tokens": 4000},
        "relay": {"provider": "proxy", "model": "test-big", "max_tokens": 1000},
    },
    "pricing": {
        "test-big": {"input": 10.0, "output": 100.0},
        "test-small": {"input": 1.0, "output": 2.0},
    },
    "cache_multipliers": {"read": 0.1, "write_5m": 1.25, "write_1h": 2.0},
}


@dataclass
class FakeUsage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read: int = 0
    cache_created: int = 0


@pytest.fixture
def router(tmp_path) -> Router:
    path = tmp_path / "models.yaml"
    path.write_text(yaml.safe_dump(SYNTHETIC), "utf-8")
    return Router(path)


class TestRouting:
    def test_role_without_provider_uses_default(self, router):
        assert router.for_role("writer").provider == "main"

    def test_role_can_override_provider(self, router):
        assert router.for_role("judge").provider == "cheap"

    def test_role_fields_loaded(self, router):
        cfg = router.for_role("writer")
        assert (cfg.model, cfg.effort, cfg.max_tokens) == ("test-big", "high", 8000)

    def test_effort_optional(self, router):
        assert router.for_role("judge").effort is None

    def test_unknown_role_names_the_valid_ones(self, router):
        with pytest.raises(KeyError, match="writer"):
            router.for_role("nonexistent")

    def test_providers_in_use_excludes_unreferenced(self, router):
        """没被任何角色引用的供应商不该被构造 —— 否则会去读不存在的环境变量。"""
        assert router.providers_in_use == {"main", "cheap", "proxy"}


class TestProviderConfig:
    def test_auth_style_defaults_to_api_key(self, router):
        assert router.provider("main").auth_style == "api_key"

    def test_auth_style_override(self, router):
        assert router.provider("proxy").auth_style == "bearer"

    def test_supports_effort_defaults_true(self, router):
        assert router.provider("main").supports_effort is True

    def test_supports_effort_override(self, router):
        assert router.provider("cheap").supports_effort is False

    def test_unknown_provider_in_role_fails_loudly(self, tmp_path):
        bad = dict(SYNTHETIC)
        bad["roles"] = {"writer": {"provider": "typo", "model": "m", "max_tokens": 100}}
        path = tmp_path / "bad.yaml"
        path.write_text(yaml.safe_dump(bad), "utf-8")
        with pytest.raises(ValueError, match="typo"):
            Router(path)


class TestCostFormula:
    """价目 test-big = $10/$100 每 1M token，倍率 read=0.1 / write=1.25。"""

    def test_uncached_input_at_full_price(self, router):
        assert router.cost_usd("test-big", FakeUsage(input_tokens=1_000_000)) == pytest.approx(10.0)

    def test_output_at_output_price(self, router):
        assert router.cost_usd("test-big", FakeUsage(output_tokens=1_000_000)) == pytest.approx(100.0)

    def test_cache_read_is_one_tenth(self, router):
        assert router.cost_usd("test-big", FakeUsage(cache_read=1_000_000)) == pytest.approx(1.0)

    def test_cache_write_carries_premium(self, router):
        assert router.cost_usd("test-big", FakeUsage(cache_created=1_000_000)) == pytest.approx(12.5)

    def test_components_are_additive(self, router):
        usage = FakeUsage(input_tokens=1_000_000, output_tokens=1_000_000,
                          cache_read=1_000_000, cache_created=1_000_000)
        assert router.cost_usd("test-big", usage) == pytest.approx(10.0 + 100.0 + 1.0 + 12.5)

    def test_caching_is_an_order_of_magnitude(self, router):
        """本项目成本架构的核心假设：缓存命中 vs 全价重算差约 10 倍。"""
        cached = router.cost_usd("test-big", FakeUsage(cache_read=100_000))
        uncached = router.cost_usd("test-big", FakeUsage(input_tokens=100_000))
        assert uncached / cached == pytest.approx(10.0)

    def test_dated_model_id_matches_by_prefix(self, router):
        """带日期后缀的 model id 要能匹配到基础型号的价目。"""
        assert router.cost_usd("test-small-20260731",
                               FakeUsage(input_tokens=1_000_000)) == pytest.approx(1.0)

    def test_unpriced_model_costs_zero_not_crash(self, router):
        """换用未填价目的模型时，成本记 0 但不该中断跑书。"""
        assert router.cost_usd("some-unpriced-model", FakeUsage(input_tokens=999)) == 0.0
