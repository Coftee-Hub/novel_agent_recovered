"""状态 schema、patch 合并、bible 渲染。"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from novel_agent.state import (
    Character, CharacterArc, CharacterArcUpdate, ChapterSummary, EmotionalDebt,
    PatchError, Relationship, StatePatch, StateStore, StoryState, UsedBeat,
    apply_patch, render,
)


def summary(ch: int = 13) -> ChapterSummary:
    return ChapterSummary(ch=ch, title="伞", summary="两人在雨里谁也没先开口。",
                          stage="大学", word_count=3120)


class TestSchemaGuards:
    def test_debt_due_must_follow_planting(self):
        with pytest.raises(ValidationError, match="不晚于"):
            EmotionalDebt(id="x", kind="误会", desc="d", planted_ch=10, due_by_ch=10)

    def test_affection_bounded(self):
        with pytest.raises(ValidationError, match="越界"):
            Relationship(a_id="a", b_id="b", stage="好感",
                         tension_source="t", affection={"a": 140})

    def test_core_traits_count_enforced(self):
        with pytest.raises(ValidationError):
            Character(id="x", name="x", core_traits=["只有一个"],
                      speech_habits="s", core_wound="w", value_line="v")

    def test_relationship_key_is_order_independent(self):
        a = Relationship(a_id="shen", b_id="lu", stage="好感", tension_source="t")
        b = Relationship(a_id="lu", b_id="shen", stage="好感", tension_source="t")
        assert a.key == b.key

    def test_extra_fields_rejected(self):
        """LLM 输出漂移出多余字段时必须立刻报错，而非静默吞掉。"""
        with pytest.raises(ValidationError):
            ChapterSummary(ch=1, title="t", summary="s", stage="大学",
                           word_count=100, mood="忧伤")


class TestCoreIdentityImmutable:
    def test_patch_has_no_path_to_core_fields(self):
        """跨阶段恒定的字段在类型上就够不到 —— 不靠提示词自觉。"""
        assert set(CharacterArcUpdate.model_fields) == {"character_id", "arc"}
        for forbidden in ("core_wound", "speech_habits", "value_line", "core_traits"):
            assert forbidden not in CharacterArc.model_fields

    def test_arc_update_leaves_core_intact(self, sample_state):
        before = sample_state.character("shen").core_wound
        patch = StatePatch(
            chapter_summary=summary(),
            arc_updates=[CharacterArcUpdate(character_id="shen", arc=CharacterArc(
                stage="职场", age=23, identity="出版社编辑",
                outer_goal="做出第一本书", inner_want="被人认真问一次想要什么",
                status="独居"))],
        )
        after = apply_patch(sample_state, patch)
        assert after.character("shen").core_wound == before
        assert after.character("shen").arc_at("职场").identity == "出版社编辑"

    def test_same_stage_arc_is_replaced_not_duplicated(self, sample_state):
        patch = StatePatch(
            chapter_summary=summary(),
            arc_updates=[CharacterArcUpdate(character_id="shen", arc=CharacterArc(
                stage="大学", age=21, identity="中文系大四", outer_goal="保研落定",
                inner_want="被人认真问一次想要什么", status="搬出宿舍"))],
        )
        after = apply_patch(sample_state, patch)
        arcs = after.character("shen").arcs
        assert len([a for a in arcs if a.stage == "大学"]) == 1
        assert arcs[0].identity == "中文系大四"


class TestReferentialIntegrity:
    def test_unknown_character_in_arc_update_raises(self, sample_state):
        patch = StatePatch(
            chapter_summary=summary(),
            arc_updates=[CharacterArcUpdate(character_id="ghost", arc=CharacterArc(
                stage="大学", age=20, identity="x", outer_goal="y",
                inner_want="z", status="w"))],
        )
        with pytest.raises(PatchError, match="ghost"):
            apply_patch(sample_state, patch)

    def test_unknown_character_in_relationship_raises(self, sample_state):
        patch = StatePatch(
            chapter_summary=summary(),
            relationship_updates=[Relationship(a_id="shen", b_id="ghost",
                                               stage="好感", tension_source="t")],
        )
        with pytest.raises(PatchError, match="ghost"):
            apply_patch(sample_state, patch)

    def test_unknown_debt_resolution_raises(self, sample_state):
        patch = StatePatch(chapter_summary=summary(), resolved_debt_ids=["nope"])
        with pytest.raises(PatchError, match="nope"):
            apply_patch(sample_state, patch)


class TestPatchMerge:
    def test_advances_current_chapter(self, sample_state):
        assert apply_patch(sample_state, StatePatch(chapter_summary=summary(13))).current_chapter == 13

    def test_rerunning_same_chapter_replaces(self, sample_state):
        s = apply_patch(sample_state, StatePatch(chapter_summary=summary(13)))
        again = summary(13).model_copy(update={"summary": "改写后的版本。"})
        s = apply_patch(s, StatePatch(chapter_summary=again))
        at13 = [x for x in s.chapter_summaries if x.ch == 13]
        assert len(at13) == 1 and at13[0].summary == "改写后的版本。"

    def test_relationship_upserts_regardless_of_order(self, sample_state):
        patch = StatePatch(
            chapter_summary=summary(),
            relationship_updates=[Relationship(a_id="lu", b_id="shen", stage="确认",
                                               tension_source="已挑明",
                                               affection={"shen": 80, "lu": 78},
                                               last_advanced_ch=13)],
        )
        after = apply_patch(sample_state, patch)
        assert len(after.relationships) == 1
        assert after.relationship("shen", "lu").stage == "确认"

    def test_debt_resolution(self, sample_state):
        after = apply_patch(sample_state, StatePatch(
            chapter_summary=summary(), resolved_debt_ids=["d_call"]))
        assert next(d for d in after.debts if d.id == "d_call").status == "paid"
        assert "d_call" not in {d.id for d in after.open_debts()}

    def test_existing_character_not_overwritten(self, sample_state):
        intruder = Character(id="shen", name="冒牌", core_traits=["a", "b", "c"],
                             speech_habits="x", core_wound="y", value_line="z")
        after = apply_patch(sample_state, StatePatch(
            chapter_summary=summary(), new_characters=[intruder]))
        assert after.character("shen").name == "沈知微"

    def test_source_state_not_mutated(self, sample_state):
        apply_patch(sample_state, StatePatch(chapter_summary=summary(99),
                                             used_beats=[UsedBeat(beat_type="雨中送伞", ch=99, one_line="x")]))
        assert sample_state.current_chapter == 12
        assert sample_state.used_beats == []


class TestQueries:
    def test_overdue_debts(self, sample_state):
        overdue = sample_state.overdue_debts()
        assert [d.id for d in overdue] == ["d_call"]  # d_umbrella 到期章 30，未逾期

    def test_used_beat_types_deduplicated(self):
        s = StoryState(used_beats=[
            UsedBeat(beat_type="雨中送伞", ch=1, one_line="a"),
            UsedBeat(beat_type="雨中送伞", ch=9, one_line="b"),
            UsedBeat(beat_type="醉酒告白", ch=5, one_line="c"),
        ])
        assert s.used_beat_types() == ["雨中送伞", "醉酒告白"]

    def test_recent_summaries_are_the_last_n(self):
        s = StoryState(chapter_summaries=[summary(i) for i in range(1, 21)])
        assert [x.ch for x in s.recent_summaries(3)] == [18, 19, 20]


class TestStore:
    def test_roundtrip(self, tmp_path, sample_state):
        store = StateStore(tmp_path / "story_state.json")
        store.save(sample_state)
        assert store.load() == sample_state

    def test_missing_file_yields_empty_state(self, tmp_path):
        assert StateStore(tmp_path / "absent.json").load().current_chapter == 0

    def test_no_temp_files_left_behind(self, tmp_path, sample_state):
        store = StateStore(tmp_path / "s.json")
        store.save(sample_state)
        assert list(tmp_path.glob("*.tmp")) == []


class TestBible:
    def test_renders_key_sections(self, sample_state):
        md = render(sample_state)
        for expected in ("沈知微", "核心创伤", "关系", "未回收的情感债", "手改无效"):
            assert expected in md

    def test_overdue_debts_surface_at_top(self, sample_state):
        md = render(sample_state)
        assert "⚠ 逾期未回收的情感债" in md
        assert md.index("逾期未回收") < md.index("## 人物")

    def test_arc_table_rendered(self, sample_state):
        assert "| 大学 | 20 | 中文系大三 |" in render(sample_state)

    def test_empty_state_renders_without_crashing(self):
        assert "设定集" in render(StoryState())


class TestPunctuationNormalization:
    """结构化输出会进入 writer 的上下文。实测一份卷大纲带 44 处半角逗号 ——
    writer 每写一个场景都看到 44 个错误示范，而 format_spec 同时在要求全角。
    与其事后检查，不如在数据进入系统时就统一口径。"""

    def test_halfwidth_comma_converted(self):
        from novel_agent.agents.schemas import TurningPoint

        tp = TurningPoint(ch=3, what="他没有问她,只是把名字挪到第一行")
        assert "，" in tp.what and "," not in tp.what

    def test_ellipsis_and_dash_normalized(self):
        from novel_agent.agents.schemas import TurningPoint

        assert TurningPoint(ch=1, what="他愣住了...").what.endswith("……")
        assert "——" in TurningPoint(ch=1, what="她开口--声音很轻").what

    def test_ids_and_latin_untouched(self):
        """只在紧邻汉字时转换，id、英文、小数不能被误伤。"""
        from novel_agent.agents.schemas import SceneSpec

        s = SceneSpec(id="ch012_s1", where="Wi-Fi 覆盖的 3.5 层", when="周四",
                      present=["shen"], goal="g", entry_emotion="a",
                      exit_emotion="b", beat_type="x", target_words=800)
        assert s.id == "ch012_s1"
        assert s.where == "Wi-Fi 覆盖的 3.5 层"

    def test_list_fields_normalized(self):
        from novel_agent.state.schema import Character

        c = Character(id="x", name="测试", core_traits=["克制", "沉默", "细心"],
                      speech_habits="s", core_wound="w", value_line="v",
                      voice_samples=["你不是要走吗?", "没关系,我可以"])
        assert all("?" not in v and "," not in v for v in c.voice_samples)

    def test_state_roundtrip_keeps_normalized_form(self, tmp_path, sample_state):
        from novel_agent.state import StateStore

        store = StateStore(tmp_path / "s.json")
        store.save(sample_state)
        assert store.load() == sample_state


class TestDuplicateCharacterGuard:
    """实测事故：archivist 把已有的四个人物用 shen_zhiwei / lu_shiyu 这类
    新 id 重新登记了一遍，于是 state 里出现两套人物、两组关系。
    关系检查没拦住是因为顺序 —— new_characters 先进 known，检查自然通过。"""

    def test_same_name_new_id_rejected(self, sample_state):
        from novel_agent.state.schema import Character

        dup = Character(id="shen_zhiwei", name="沈知微",
                        core_traits=["克制", "沉默", "细心"],
                        speech_habits="s", core_wound="w", value_line="v")
        with pytest.raises(PatchError, match="重名"):
            apply_patch(sample_state, StatePatch(
                chapter_summary=summary(), new_characters=[dup]))

    def test_genuinely_new_character_accepted(self, sample_state):
        from novel_agent.state.schema import Character

        fresh = Character(id="zhou", name="周聿",
                          core_traits=["固执", "较真", "不转弯"],
                          speech_habits="s", core_wound="w", value_line="v")
        after = apply_patch(sample_state, StatePatch(
            chapter_summary=summary(), new_characters=[fresh]))
        assert after.character("zhou") is not None

    def test_same_id_still_ignored(self, sample_state):
        """同 id 重复提交是幂等的，不该报错。"""
        from novel_agent.state.schema import Character

        again = Character(id="shen", name="沈知微",
                          core_traits=["a", "b", "c"],
                          speech_habits="x", core_wound="y", value_line="z")
        after = apply_patch(sample_state, StatePatch(
            chapter_summary=summary(), new_characters=[again]))
        assert len(after.characters) == len(sample_state.characters)
        assert after.character("shen").speech_habits != "x", "不得覆盖内核字段"
