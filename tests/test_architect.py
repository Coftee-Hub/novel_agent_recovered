"""architect 的输出契约与上下文分层。

不打真实 API：用假 client 捕获组装出的 Prompt，验证分层是否正确。
"""

from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from novel_agent.agents.architect import Architect
from novel_agent.agents.schemas import (
    ChapterOutline, DebtPlan, RelationTarget, SceneSpec, TurningPoint, VolumeOutline,
)

SKILLS = Path(__file__).resolve().parent.parent / "skills"


def scene(sid="ch001_s1", entry="戒备", exit_="动摇", **kw) -> SceneSpec:
    base = dict(id=sid, where="图书馆", when="周四傍晚", present=["shen", "lu"],
                goal="让她第一次没有说出那句没关系", entry_emotion=entry,
                exit_emotion=exit_, beat_type="雨中共伞", target_words=1200)
    base.update(kw)
    return SceneSpec(**base)


def volume_outline(**kw) -> VolumeOutline:
    base = dict(
        volume=1, stage="大学", ch_start=1, ch_end=18,
        premise="她习惯了不开口，他习惯了不问。",
        relation_targets=[RelationTarget(a_id="shen", b_id="lu", from_stage="陌生",
                                         to_stage="暧昧", via="社团值班表把两人排在同一晚")],
        turning_points=[TurningPoint(ch=9, what="她第一次主动留下")],
        ends_on="他在楼下等了一夜，她始终没有下来",
    )
    base.update(kw)
    return VolumeOutline(**base)


class FakeClient:
    """捕获组装出的 Prompt，不发请求。"""

    def __init__(self, reply):
        self.reply = reply
        self.prompts = []

    def parse(self, role, prompt, output_format, **kw):
        self.prompts.append((role, prompt))
        prompt.validate()  # 仍然跑护栏，确保分层合法

        class R:
            parsed = self.reply

        return R()


@pytest.fixture
def architect(sample_state):
    outline = ChapterOutline(ch=1, title="值班", stage="大学", intent="初遇",
                             scenes=[scene("ch001_s1"), scene("ch001_s2", entry="动摇",
                                                             exit_="不肯承认")],
                             hook="伞留在了她手里")
    return Architect(FakeClient(outline), SKILLS), sample_state


# ---------------------------------------------------------------- schema


class TestSceneSpec:
    def test_emotion_must_shift(self):
        """情绪无位移的场景在言情里是废戏，出图阶段就该拦住。"""
        with pytest.raises(ValidationError, match="起止情绪相同"):
            scene(entry="戒备", exit_="戒备")

    def test_whitespace_does_not_fake_a_shift(self):
        with pytest.raises(ValidationError, match="起止情绪相同"):
            scene(entry="戒备", exit_=" 戒备 ")

    def test_needs_someone_present(self):
        with pytest.raises(ValidationError):
            scene(present=[])

    def test_target_words_bounded(self):
        with pytest.raises(ValidationError):
            scene(target_words=5000)

    def test_intimacy_defaults_to_l0(self):
        assert scene().intimacy_level == "L0"

    def test_intimacy_rejects_out_of_range(self):
        with pytest.raises(ValidationError):
            scene(intimacy_level="L3")


class TestDebtPlan:
    def test_planting_requires_deadline(self):
        """没有到期章的伏笔在长篇里必然被遗忘。"""
        with pytest.raises(ValidationError, match="due_by_ch"):
            DebtPlan(debt_id="d1", action="plant", kind="误会", desc="x")

    def test_paying_needs_no_deadline(self):
        DebtPlan(debt_id="d1", action="pay", desc="收掉那个误会")


class TestChapterOutline:
    def test_scene_count_bounded(self):
        with pytest.raises(ValidationError):
            ChapterOutline(ch=1, title="t", stage="大学", intent="i",
                           scenes=[scene()], hook="h")

    def test_duplicate_scene_ids_rejected(self):
        with pytest.raises(ValidationError, match="重复的场景 id"):
            ChapterOutline(ch=1, title="t", stage="大学", intent="i",
                           scenes=[scene("a"), scene("a", entry="x", exit_="y")], hook="h")

    def test_target_words_sums_scenes(self):
        o = ChapterOutline(ch=1, title="t", stage="大学", intent="i",
                           scenes=[scene("a"), scene("b", entry="x", exit_="y")], hook="h")
        assert o.target_words == 2400


class TestVolumeOutline:
    def test_turning_point_must_be_inside_range(self):
        with pytest.raises(ValidationError, match="超出本卷区间"):
            volume_outline(turning_points=[TurningPoint(ch=99, what="x")])

    def test_reversed_range_rejected(self):
        with pytest.raises(ValidationError, match="区间颠倒"):
            volume_outline(ch_start=20, ch_end=5,
                           turning_points=[TurningPoint(ch=7, what="x")])

    def test_chapter_count(self):
        assert volume_outline().chapter_count == 18

    def test_markdown_is_readable(self):
        """卷大纲是作者要在两分钟内判断的东西，渲染必须人话。"""
        md = volume_outline().to_markdown()
        for expected in ("第 1 卷", "主线", "关系推进", "陌生 → **暧昧**",
                         "第 9 章", "卷末停在"):
            assert expected in md


# ---------------------------------------------------------------- 上下文分层


class TestContextLayering:
    def test_system_core_has_role_and_survives_missing_skills(self, architect):
        """语料未到位时，多数 skill 尚未萃取，仍要能拼出可用的 system_core。"""
        arch, _ = architect
        core = arch.system_core()
        assert "结构设计者" in core
        assert "亲密尺度分档" in core  # 已写的 skill 进来了
        assert len(core) > 500

    def test_bible_layer_from_state(self, architect):
        arch, state = architect
        assert "沈知微" in arch.bible_layer(state)

    def test_empty_state_yields_empty_bible(self, architect):
        from novel_agent.state.schema import StoryState

        arch, _ = architect
        assert arch.bible_layer(StoryState()) == ""

    def test_used_beats_are_surfaced(self, architect):
        """防重复：用过的桥段必须明确摆进上下文。"""
        from novel_agent.state.schema import UsedBeat

        arch, state = architect
        state.used_beats.append(UsedBeat(beat_type="醉酒告白", ch=7, one_line="x"))
        layer = arch.history_layer(state)
        assert "已用桥段·禁止重复" in layer and "醉酒告白" in layer

    def test_open_debts_carry_deadline(self, architect):
        arch, state = architect
        layer = arch.history_layer(state)
        assert "未回收的情感债" in layer
        assert "应在第 30 章前回收" in layer

    def test_confirmed_volume_enters_stable_layer(self, architect):
        arch, state = architect
        layer = arch.history_layer(state, volume_outline())
        assert "本卷大纲·已确认" in layer


class TestCachePrefixStability:
    """整个分层设计的意义所在。"""

    def test_prefix_constant_across_chapters_in_a_volume(self, architect):
        arch, state = architect
        vol = volume_outline()
        arch.plan_chapter(state, vol, ch=5)
        arch.plan_chapter(state, vol, ch=6)
        arch.plan_chapter(state, vol, ch=7, note="这章慢一点")

        prints = [p.prefix_fingerprint() for _, p in arch.client.prompts]
        assert len(set(prints)) == 1, (
            f"同卷内逐章调用的缓存前缀发生了变化：{prints}。"
            f"说明有随章节变化的内容漏进了稳定层。"
        )

    def test_chapter_number_lives_in_volatile_layer(self, architect):
        """当前规划的章号只能出现在易变层。

        注意不能粗暴断言"第 N 章"三个字不在稳定层 —— 设定集里本就有
        "第 5 章埋下"这类**历史**信息，那是稳定的。要断言的是当前任务的措辞。
        """
        arch, state = architect
        arch.plan_chapter(state, volume_outline(), ch=5)
        _, prompt = arch.client.prompts[-1]
        task = "设计第 5 章的细纲"
        assert task in prompt.instruction
        assert task not in prompt.system_core + prompt.bible + prompt.volume

    def test_prefix_changes_when_volume_changes(self, architect):
        """换卷时前缀本就该变 —— 那是一次性代价，之后整卷复用。"""
        arch, state = architect
        arch.plan_chapter(state, volume_outline(volume=1), ch=5)
        arch.plan_chapter(state, volume_outline(
            volume=2, ch_start=19, ch_end=36,
            turning_points=[TurningPoint(ch=25, what="y")]), ch=20)
        a, b = [p.prefix_fingerprint() for _, p in arch.client.prompts]
        assert a != b

    def test_turning_point_chapter_gets_flagged(self, architect):
        arch, state = architect
        arch.plan_chapter(state, volume_outline(), ch=9)  # 卷大纲里第 9 章是转折点
        assert "本章是本卷的转折点" in arch.client.prompts[-1][1].instruction

    def test_uses_architect_role_for_routing(self, architect):
        arch, state = architect
        arch.plan_chapter(state, volume_outline(), ch=5)
        assert arch.client.prompts[-1][0] == "architect"


class TestCharacterIdIntegrity:
    """模型会自己造 id（实测把 `shen` 写成 `shen_zhiwei`），必须当场拦住。"""

    def test_roster_is_in_context(self, architect):
        arch, state = architect
        layer = arch.bible_layer(state)
        assert "人物 id 表" in layer
        assert "`shen` = 沈知微" in layer

    def test_invented_id_in_volume_rejected(self, sample_state):
        bad = volume_outline(relation_targets=[RelationTarget(
            a_id="shen_zhiwei", b_id="lu_shiyu", from_stage="陌生",
            to_stage="暧昧", via="x")])
        arch = Architect(FakeClient(bad), SKILLS)
        with pytest.raises(ValueError, match="不存在的人物 id"):
            arch.plan_volume(sample_state, volume=1, ch_start=1, ch_end=18, stage="大学")

    def test_error_names_the_valid_ids(self, sample_state):
        bad = volume_outline(relation_targets=[RelationTarget(
            a_id="ghost", b_id="lu", from_stage="陌生", to_stage="暧昧", via="x")])
        arch = Architect(FakeClient(bad), SKILLS)
        with pytest.raises(ValueError, match="'lu', 'shen'"):
            arch.plan_volume(sample_state, volume=1, ch_start=1, ch_end=18, stage="大学")

    def test_valid_ids_pass(self, sample_state):
        arch = Architect(FakeClient(volume_outline()), SKILLS)
        arch.plan_volume(sample_state, volume=1, ch_start=1, ch_end=18, stage="大学")

    def test_scene_present_ids_checked(self, sample_state):
        bad = ChapterOutline(ch=1, title="t", stage="大学", intent="i", hook="h",
            scenes=[scene("a", present=["shen", "nobody"]),
                    scene("b", entry="x", exit_="y")])
        arch = Architect(FakeClient(bad), SKILLS)
        with pytest.raises(ValueError, match="nobody"):
            arch.plan_chapter(sample_state, volume_outline(), ch=1)
