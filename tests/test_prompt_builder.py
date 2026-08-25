"""分层 Prompt 与各后端的渲染。

这些断言保护的是本项目最贵的一个不变量：卷内所有章节共享同一个缓存前缀。
断了它不会报错，只会让账单悄悄翻数倍 —— 所以必须由测试守住。
"""

from __future__ import annotations

import pytest

from novel_agent.llm.backends import AnthropicBackend, OpenAIBackend, ProviderConfig
from novel_agent.llm.prompt_builder import Prompt, PromptLayerError, stable_json

SYSTEM = "你是一位言情小说写作者。" * 20
BIBLE = "【人物卡】沈知微：中文系大三，说话习惯是句末带问号。" * 20
VOLUME = "【第一卷大纲】相识与错过。" * 20


def make(**kw) -> Prompt:
    base = dict(system_core=SYSTEM, bible=BIBLE, volume=VOLUME, instruction="写第一个场景。")
    base.update(kw)
    return Prompt(**base)


@pytest.fixture
def anthropic_backend():
    cfg = ProviderConfig(name="anthropic", kind="anthropic", api_key_env="X")
    return AnthropicBackend(cfg, client=object())


@pytest.fixture
def openai_backend():
    cfg = ProviderConfig(name="deepseek", kind="openai", api_key_env="X",
                         base_url="http://x", supports_effort=False)
    return OpenAIBackend(cfg, client=object())


def all_blocks(built: dict) -> list[dict]:
    return built.get("system", []) + [b for m in built["messages"] for b in m["content"]]


# ---------------------------------------------------------------- 供应商中立


class TestLayering:
    def test_fingerprint_stable_across_volatile_changes(self):
        """同一卷内逐章调用，前缀指纹必须恒定 —— 缓存能命中的前提。"""
        fp1 = make(rag_snippets=["第 3 章检索片段"], prev_tail="A").prefix_fingerprint()
        fp2 = make(rag_snippets=["完全不同的片段"], prev_tail="B",
                   instruction="写第七个场景。").prefix_fingerprint()
        assert fp1 == fp2

    def test_fingerprint_changes_when_bible_changes(self):
        assert make().prefix_fingerprint() != make(bible=BIBLE + "新人物").prefix_fingerprint()

    def test_stable_layers_skip_empties(self):
        assert len(Prompt(system_core=SYSTEM, instruction="写。").stable_layers()) == 0
        assert len(make().stable_layers()) == 2

    @pytest.mark.parametrize(
        "poison", ["生成于 2026-08-19 11:23", "会话 550e8400-e29b-41d4-a716-446655440000"]
    )
    def test_poisoned_stable_layer_rejected(self, poison):
        with pytest.raises(PromptLayerError, match="缓存失效源"):
            make(bible=BIBLE + poison).validate()

    def test_volatile_layer_may_contain_timestamps(self):
        make(prev_tail="2026-08-19 11:23 她推开门").validate()

    def test_empty_system_core_rejected(self):
        with pytest.raises(PromptLayerError, match="system_core"):
            Prompt(system_core="  ", instruction="写。").validate()

    def test_empty_instruction_rejected(self):
        with pytest.raises(PromptLayerError, match="instruction"):
            Prompt(system_core=SYSTEM, instruction="").validate()


class TestRagDefense:
    def test_snippets_carry_anti_plagiarism_warning(self):
        """抄袭防线第 1 道：检索片段必须带禁止复用的指令。"""
        text = make(rag_snippets=["某本书的原文段落"]).render_rag()
        assert "严禁复用" in text and "某本书的原文段落" in text


class TestStableJson:
    def test_key_order_deterministic(self):
        assert stable_json({"b": 1, "a": 2}) == stable_json({"a": 2, "b": 1})

    def test_chinese_not_escaped(self):
        assert "沈知微" in stable_json({"name": "沈知微"})


# ---------------------------------------------------------------- Anthropic


class TestAnthropicRender:
    def test_stable_layers_get_breakpoints(self, anthropic_backend):
        built = anthropic_backend.render(make())
        assert "cache_control" in built["system"][0]
        assert len([b for b in all_blocks(built) if "cache_control" in b]) == 3

    def test_volatile_tail_has_no_breakpoint(self, anthropic_backend):
        built = anthropic_backend.render(make(rag_snippets=["片段"], prev_tail="上文"))
        tail = built["messages"][-1]["content"]
        assert all("cache_control" not in b for b in tail), (
            "易变尾部带了断点 —— 每次写入新缓存却永远读不到，纯亏写入费"
        )

    def test_never_exceeds_four_breakpoints(self, anthropic_backend):
        built = anthropic_backend.render(make(rag_snippets=["a", "b", "c"], prev_tail="x"))
        assert len([b for b in all_blocks(built) if "cache_control" in b]) <= 4

    def test_ordering_stable_before_volatile(self, anthropic_backend):
        built = anthropic_backend.render(make(rag_snippets=["参照"], prev_tail="上文"))
        texts = [b["text"] for b in all_blocks(built)]
        assert texts.index(BIBLE) < texts.index(VOLUME)
        assert "写第一个场景。" in texts[-1], "instruction 必须在最后"


# ---------------------------------------------------------------- OpenAI 兼容


class TestOpenAIRender:
    def test_system_first_then_user(self, openai_backend):
        msgs = openai_backend.render(make())["messages"]
        assert msgs[0]["role"] == "system" and msgs[0]["content"] == SYSTEM
        assert all(m["role"] == "user" for m in msgs[1:])

    def test_merges_consecutive_user_by_default(self, openai_backend):
        """部分兼容端要求 user/assistant 严格交替，合并可避免 400。"""
        msgs = openai_backend.render(make())["messages"]
        assert len(msgs) == 2
        body = msgs[1]["content"]
        assert body.index(BIBLE) < body.index(VOLUME) < body.index("写第一个场景。")

    def test_can_keep_messages_separate(self):
        cfg = ProviderConfig(name="x", kind="openai", api_key_env="X",
                             merge_consecutive_user=False)
        msgs = OpenAIBackend(cfg, client=object()).render(make())["messages"]
        assert len(msgs) == 4

    def test_no_cache_control_leaks_into_openai_payload(self, openai_backend):
        """cache_control 是 Anthropic 专属，混进去会被拒。"""
        assert "cache_control" not in str(openai_backend.render(make()))

    def test_ordering_survives_backend_swap(self, anthropic_backend, openai_backend):
        """两个后端渲染出的层序必须一致 —— 换供应商不该改变缓存行为。"""
        oa = openai_backend.render(make(rag_snippets=["参照"]))["messages"][1]["content"]
        an = "".join(b["text"] for b in all_blocks(anthropic_backend.render(
            make(rag_snippets=["参照"]))))
        for haystack in (oa, an):
            assert haystack.index(BIBLE) < haystack.index(VOLUME)
            assert haystack.index(VOLUME) < haystack.index("参照")


class TestUsageNormalization:
    """OpenAI 的 prompt_tokens 含已缓存部分，Anthropic 的不含。不归一化会重复计费。"""

    def test_openai_cached_tokens_subtracted(self):
        from novel_agent.llm.backends.openai_backend import _normalize_usage

        class Details:
            cached_tokens = 8000

        class Usage:
            prompt_tokens = 10000
            completion_tokens = 500
            prompt_tokens_details = Details()

        u = _normalize_usage(Usage())
        assert u["input_tokens"] == 2000, "未减去缓存部分 → 成本会被重复计算"
        assert u["cache_read"] == 8000

    def test_deepseek_style_cache_field(self):
        from novel_agent.llm.backends.openai_backend import _normalize_usage

        class Usage:
            prompt_tokens = 10000
            completion_tokens = 500
            prompt_cache_hit_tokens = 6000

        u = _normalize_usage(Usage())
        assert u["input_tokens"] == 4000 and u["cache_read"] == 6000

    def test_missing_usage_is_zeros(self):
        from novel_agent.llm.backends.openai_backend import _normalize_usage

        assert _normalize_usage(None)["input_tokens"] == 0


class TestJsonModeFallback:
    """端点不支持 output_config.format 时的兜底路径。"""

    def test_augment_survives_literal_braces(self):
        """模板与 schema 里都有字面量花括号，不能用 str.format。"""
        from novel_agent.llm import json_mode
        from novel_agent.agents.schemas import VolumeOutline

        out = json_mode.augment("写一份卷大纲。", VolumeOutline)
        assert "写一份卷大纲。" in out
        assert "第一个字符必须是 `{`" in out
        assert '"properties"' in out

    @pytest.mark.parametrize(
        "reply",
        ['{"a": 1}',
         '```json\n{"a": 1}\n```',
         '好的，这是结果：\n\n{"a": 1}\n\n希望有帮助。',
         '```\n{"a": 1}\n```'],
    )
    def test_extract_strips_noise(self, reply):
        from novel_agent.llm import json_mode

        assert json_mode.extract(reply) == '{"a": 1}'

    def test_extract_rejects_prose(self):
        from novel_agent.llm import json_mode

        with pytest.raises(ValueError, match="找不到 JSON"):
            json_mode.extract("# 第 2 卷大纲\n\n主线：她习惯了不开口。")

    def test_looks_like_json_detects_swallowed_param(self):
        """自动探测的判据：请求了结构化输出却回来散文。"""
        from novel_agent.llm import json_mode

        assert json_mode.looks_like_json('{"a": 1}')
        assert not json_mode.looks_like_json("# 第 2 卷大纲")
        assert not json_mode.looks_like_json('{"a": 1')  # 截断的 JSON


class TestSynthesisTruncationGuard:
    """思考模型会把预算耗在推理上，正文写一半戛然而止且 stop_reason 仍报 stop。
    这种残缺草稿看起来是正常文件，必须靠结尾标点识别出来。"""

    @pytest.mark.parametrize(
        "text,complete",
        [("一句完整的话。", True), ("以问号结尾？", True), ("省略号收尾……", True),
         ("引文收尾。”", True), ("| 表格 | 行 |", True),
         ("相悖的规则：", False), ("写到一半的句子", False),
         ("以逗号断开，", False), ("", False)],
    )
    def test_detects_truncation(self, text, complete):
        from novel_agent.corpus.extract import _looks_complete

        assert _looks_complete(text) is complete
