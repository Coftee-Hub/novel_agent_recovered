# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py
# 来源   : test_writer.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = 'writer / stitcher 的上下文分层与指令组装。\n\n不打真实 API：用假 client 捕获 Prompt，验证该进稳定层的进了稳定层、\n该进易变层的进了易变层。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'writer / stitcher 的上下文分层与指令组装。\n\n不打真实 API：用假 client 捕获 Prompt，验证该进稳定层的进了稳定层、\n该进易变层的进了易变层。\n',
    6: 'skills',
    12: 'FakeClient',
    16: 'TestWriterLayering',
    18: 'TestCachePrefix',
    20: 'TestSceneSequencing',
    22: 'TestStitcher',
    24: 'TestStitchCompleteness',
    26: 'TestTrailingNotesAreStripped',
    28: 'TestQuoteNormalisation',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'SceneSpec',
    ('scene', 0): '图书馆',
    ('scene', 1): '周四傍晚',
    ('scene', 2): 'shen',
    ('scene', 3): 'lu',
    ('scene', 4): '让她第一次没说出那句没关系',
    ('scene', 5): '戒备',
    ('scene', 6): '动摇',
    ('scene', 7): '雨中共伞',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'ChapterOutline',
    ('outline', 1): '值班',
    ('outline', 2): '大学',
    ('outline', 3): '初次靠近',
    ('outline', 4): 'ch012_s1',
    ('outline', 5): 'ch012_s2',
    ('outline', 6): '动摇',
    ('outline', 7): '不肯承认',
    ('outline', 9): '伞留在了她手里',
    ('FakeClient', 0): 'FakeClient',
    ('complete', 1): 'R',
    ('R', 0): 'FakeClient.complete.<locals>.R',
    ('TestWriterLayering', 0): 'TestWriterLayering',
    ('test_design_time_skills_absent', 0): 'writer 拿的是设计的产物，不该背着设计方法。',
    ('test_design_time_skills_absent', 1): '叙述语感',
    ('test_design_time_skills_absent', 2): '对话技法',
    ('test_design_time_skills_absent', 3): 'py3',
    ('test_design_time_skills_absent', 4): 'py5',
    ('test_design_time_skills_absent', 5): 'core',
    ('test_design_time_skills_absent', 6): '%(py7)s',
    ('test_design_time_skills_absent', 7): 'py7',
    ('test_design_time_skills_absent', 8): 'py10',
    ('test_design_time_skills_absent', 9): 'py12',
    ('test_design_time_skills_absent', 10): '%(py14)s',
    ('test_design_time_skills_absent', 11): 'py14',
    ('test_design_time_skills_absent', 12): 'assert %(py17)s',
    ('test_design_time_skills_absent', 13): 'py17',
    ('test_design_time_skills_absent', 15): '人物设计法',
    ('test_design_time_skills_absent', 16): 'py1',
    ('test_design_time_skills_absent', 17): 'assert %(py5)s',
    ('test_design_time_skills_absent', 18): '情绪节拍模板库',
    ('test_scene_spec_lives_in_volatile_layer', 1): 'ch012_s1',
    ('test_scene_spec_lives_in_volatile_layer', 2): 'py1',
    ('test_scene_spec_lives_in_volatile_layer', 3): 'py3',
    ('test_scene_spec_lives_in_volatile_layer', 4): 'p',
    ('test_scene_spec_lives_in_volatile_layer', 5): 'py5',
    ('test_scene_spec_lives_in_volatile_layer', 6): 'assert %(py7)s',
    ('test_scene_spec_lives_in_volatile_layer', 7): 'py7',
    ('test_scene_spec_lives_in_volatile_layer', 9): 'py6',
    ('test_scene_spec_lives_in_volatile_layer', 10): 'py8',
    ('test_scene_spec_lives_in_volatile_layer', 11): 'assert %(py11)s',
    ('test_scene_spec_lives_in_volatile_layer', 12): 'py11',
    ('test_emotion_shift_is_emphasised', 1): '戒备 → 动摇',
    ('test_emotion_shift_is_emphasised', 2): 'py1',
    ('test_emotion_shift_is_emphasised', 3): 'py4',
    ('test_emotion_shift_is_emphasised', 4): 'py6',
    ('test_emotion_shift_is_emphasised', 5): 'assert %(py8)s',
    ('test_emotion_shift_is_emphasised', 6): 'py8',
    ('test_character_names_resolved_from_state', 0): '规格里存的是 id，指令里要给人名。',
    ('test_character_names_resolved_from_state', 1): '沈知微',
    ('test_character_names_resolved_from_state', 2): 'py1',
    ('test_character_names_resolved_from_state', 3): 'py4',
    ('test_character_names_resolved_from_state', 4): 'py6',
    ('test_character_names_resolved_from_state', 5): 'assert %(py8)s',
    ('test_character_names_resolved_from_state', 6): 'py8',
    ('test_prev_tail_truncated_and_placed_volatile', 2): 'py0',
    ('test_prev_tail_truncated_and_placed_volatile', 3): 'len',
    ('test_prev_tail_truncated_and_placed_volatile', 4): 'py1',
    ('test_prev_tail_truncated_and_placed_volatile', 5): 'p',
    ('test_prev_tail_truncated_and_placed_volatile', 6): 'py3',
    ('test_prev_tail_truncated_and_placed_volatile', 7): 'py5',
    ('test_prev_tail_truncated_and_placed_volatile', 8): 'py7',
    ('test_prev_tail_truncated_and_placed_volatile', 9): 'w',
    ('test_prev_tail_truncated_and_placed_volatile', 10): 'py9',
    ('test_prev_tail_truncated_and_placed_volatile', 11): 'assert %(py11)s',
    ('test_prev_tail_truncated_and_placed_volatile', 12): 'py11',
    ('test_prev_tail_truncated_and_placed_volatile', 14): 'py2',
    ('test_prev_tail_truncated_and_placed_volatile', 15): 'py4',
    ('test_prev_tail_truncated_and_placed_volatile', 16): 'py6',
    ('test_prev_tail_truncated_and_placed_volatile', 17): 'py13',
    ('test_prev_tail_truncated_and_placed_volatile', 18): 'assert %(py16)s',
    ('test_prev_tail_truncated_and_placed_volatile', 19): 'py16',
    ('test_prev_tail_truncated_and_placed_volatile', 20): '上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上',
    ('test_intimacy_level_instruction', 0): 'L2',
    ('test_intimacy_level_instruction', 2): 'ch012_s2',
    ('test_intimacy_level_instruction', 3): 'a',
    ('test_intimacy_level_instruction', 4): 'b',
    ('test_intimacy_level_instruction', 7): '收住',
    ('test_intimacy_level_instruction', 8): 'py3',
    ('test_intimacy_level_instruction', 9): 'py6',
    ('test_intimacy_level_instruction', 10): 'py8',
    ('test_intimacy_level_instruction', 11): '%(py10)s',
    ('test_intimacy_level_instruction', 12): 'py10',
    ('test_intimacy_level_instruction', 13): 'py13',
    ('test_intimacy_level_instruction', 14): 'py16',
    ('test_intimacy_level_instruction', 15): 'py18',
    ('test_intimacy_level_instruction', 16): '%(py20)s',
    ('test_intimacy_level_instruction', 17): 'py20',
    ('test_intimacy_level_instruction', 18): 'assert %(py23)s',
    ('test_intimacy_level_instruction', 19): 'py23',
    ('test_must_not_surfaced', 0): '提到那把伞的来历',
    ('test_must_not_surfaced', 2): 'ch012_s2',
    ('test_must_not_surfaced', 3): 'a',
    ('test_must_not_surfaced', 4): 'b',
    ('test_must_not_surfaced', 7): '禁止出现',
    ('test_must_not_surfaced', 8): 'py1',
    ('test_must_not_surfaced', 9): 'py4',
    ('test_must_not_surfaced', 10): 'py6',
    ('test_must_not_surfaced', 11): 'assert %(py8)s',
    ('test_must_not_surfaced', 12): 'py8',
    ('TestCachePrefix', 0): 'TestCachePrefix',
    ('test_prefix_constant_across_scenes_in_a_chapter', 0): '同一章的各场景必须共享缓存前缀 —— 这是分场景写不额外烧钱的前提。',
    ('test_prefix_constant_across_scenes_in_a_chapter', 1): 'py0',
    ('test_prefix_constant_across_scenes_in_a_chapter', 2): 'len',
    ('test_prefix_constant_across_scenes_in_a_chapter', 3): 'py1',
    ('test_prefix_constant_across_scenes_in_a_chapter', 4): 'prints',
    ('test_prefix_constant_across_scenes_in_a_chapter', 5): 'py3',
    ('test_prefix_constant_across_scenes_in_a_chapter', 6): 'py6',
    ('test_prefix_constant_across_scenes_in_a_chapter', 7): '场景间前缀发生变化：',
    ('test_prefix_constant_across_scenes_in_a_chapter', 8): '\n>assert %(py8)s',
    ('test_prefix_constant_across_scenes_in_a_chapter', 9): 'py8',
    ('test_bible_not_trimmed_per_scene', 0): '按出场人物裁剪 bible 会击穿前缀，省的 token 不值这个代价。',
    ('test_bible_not_trimmed_per_scene', 1): '陆时予',
    ('test_bible_not_trimmed_per_scene', 2): 'py1',
    ('test_bible_not_trimmed_per_scene', 3): 'py4',
    ('test_bible_not_trimmed_per_scene', 4): 'py6',
    ('test_bible_not_trimmed_per_scene', 5): 'assert %(py8)s',
    ('test_bible_not_trimmed_per_scene', 6): 'py8',
    ('test_rag_goes_volatile', 1): '某段风格参照',
    ('test_rag_goes_volatile', 3): 'py0',
    ('test_rag_goes_volatile', 4): 'p',
    ('test_rag_goes_volatile', 5): 'py2',
    ('test_rag_goes_volatile', 6): 'py5',
    ('test_rag_goes_volatile', 7): 'assert %(py7)s',
    ('test_rag_goes_volatile', 8): 'py7',
    ('test_rag_goes_volatile', 10): 'py1',
    ('test_rag_goes_volatile', 11): 'py3',
    ('test_rag_goes_volatile', 12): 'py6',
    ('test_rag_goes_volatile', 13): 'py8',
    ('test_rag_goes_volatile', 14): 'py10',
    ('test_rag_goes_volatile', 15): 'py12',
    ('test_rag_goes_volatile', 16): 'assert %(py15)s',
    ('test_rag_goes_volatile', 17): 'py15',
    ('TestSceneSequencing', 0): 'TestSceneSequencing',
    ('test_writes_every_scene_in_order', 1): 'py0',
    ('test_writes_every_scene_in_order', 2): 'len',
    ('test_writes_every_scene_in_order', 3): 'py1',
    ('test_writes_every_scene_in_order', 4): 'texts',
    ('test_writes_every_scene_in_order', 5): 'py3',
    ('test_writes_every_scene_in_order', 6): 'py6',
    ('test_writes_every_scene_in_order', 7): 'assert %(py8)s',
    ('test_writes_every_scene_in_order', 8): 'py8',
    ('test_writes_every_scene_in_order', 10): '**',
    ('test_writes_every_scene_in_order', 11): 'ch012_s1',
    ('test_writes_every_scene_in_order', 12): 'ch012_s2',
    ('test_writes_every_scene_in_order', 13): 'py4',
    ('test_writes_every_scene_in_order', 14): 'assert %(py6)s',
    ('test_each_scene_sees_previous_tail', 2): 'py1',
    ('test_each_scene_sees_previous_tail', 3): 'py3',
    ('test_each_scene_sees_previous_tail', 4): 'py6',
    ('test_each_scene_sees_previous_tail', 5): 'assert %(py8)s',
    ('test_each_scene_sees_previous_tail', 6): 'py8',
    ('test_uses_writer_role', 1): 'writer',
    ('test_uses_writer_role', 2): 'py1',
    ('test_uses_writer_role', 3): 'py4',
    ('test_uses_writer_role', 4): 'assert %(py6)s',
    ('test_uses_writer_role', 5): 'py6',
    ('TestStitcher', 0): 'TestStitcher',
    ('test_receives_all_scenes', 0): '第一场正文。',
    ('test_receives_all_scenes', 1): '第二场正文。',
    ('test_receives_all_scenes', 2): 'py3',
    ('test_receives_all_scenes', 3): 'py5',
    ('test_receives_all_scenes', 4): 'instr',
    ('test_receives_all_scenes', 5): '%(py7)s',
    ('test_receives_all_scenes', 6): 'py7',
    ('test_receives_all_scenes', 7): 'py10',
    ('test_receives_all_scenes', 8): 'py12',
    ('test_receives_all_scenes', 9): '%(py14)s',
    ('test_receives_all_scenes', 10): 'py14',
    ('test_receives_all_scenes', 11): 'assert %(py17)s',
    ('test_receives_all_scenes', 12): 'py17',
    ('test_told_not_to_rewrite', 0): '越权重写会掩盖场景本身的问题，让检查环节抓不到。',
    ('test_told_not_to_rewrite', 1): 'a',
    ('test_told_not_to_rewrite', 2): 'b',
    ('test_told_not_to_rewrite', 3): '不要重写内容',
    ('test_told_not_to_rewrite', 4): 'py1',
    ('test_told_not_to_rewrite', 5): 'py4',
    ('test_told_not_to_rewrite', 6): 'py6',
    ('test_told_not_to_rewrite', 7): 'assert %(py8)s',
    ('test_told_not_to_rewrite', 8): 'py8',
    ('test_title_and_hook_passed', 0): 'a',
    ('test_title_and_hook_passed', 1): 'b',
    ('test_title_and_hook_passed', 2): '## 第12章 值班',
    ('test_title_and_hook_passed', 3): 'py1',
    ('test_title_and_hook_passed', 4): 'py3',
    ('test_title_and_hook_passed', 5): 'instr',
    ('test_title_and_hook_passed', 6): 'assert %(py5)s',
    ('test_title_and_hook_passed', 7): 'py5',
    ('test_title_and_hook_passed', 9): '伞留在了她手里',
    ('test_uses_stitcher_role', 0): 'a',
    ('test_uses_stitcher_role', 1): 'b',
    ('test_uses_stitcher_role', 2): 'stitcher',
    ('test_uses_stitcher_role', 3): 'py1',
    ('test_uses_stitcher_role', 4): 'py4',
    ('test_uses_stitcher_role', 5): 'assert %(py6)s',
    ('test_uses_stitcher_role', 6): 'py6',
    ('test_shares_writer_skills', 0): '缝合要按同样的文风判断接缝，所以共享 writer 的 skills。',
    ('test_shares_writer_skills', 1): '叙述语感',
    ('test_shares_writer_skills', 2): 'py1',
    ('test_shares_writer_skills', 3): 'py3',
    ('test_shares_writer_skills', 4): 's',
    ('test_shares_writer_skills', 5): 'py5',
    ('test_shares_writer_skills', 6): 'py7',
    ('test_shares_writer_skills', 7): 'assert %(py9)s',
    ('test_shares_writer_skills', 8): 'py9',
    ('TestStitchCompleteness', 0): 'TestStitchCompleteness',
    ('TestStitchCompleteness', 1): '实测一次 stitcher 只吐 87 字就 end_turn 收工（场景总和 4,491 字），\n正文停在半个词上。stop_reason 不是 length，光看它发现不了。',
    ('test_truncated_stitch_is_rejected', 0): '## 第12章 值班\n\n沈知微把一叠诗稿抖齐，指腹压',
    ('test_truncated_stitch_is_rejected', 1): '缝合失败',
    ('test_truncated_stitch_is_rejected', 4): '正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。',
    ('test_retry_before_giving_up', 0): '太短。',
    ('test_retry_before_giving_up', 2): 'py0',
    ('test_retry_before_giving_up', 3): 'len',
    ('test_retry_before_giving_up', 4): 'py1',
    ('test_retry_before_giving_up', 5): 'c',
    ('test_retry_before_giving_up', 6): 'py3',
    ('test_retry_before_giving_up', 7): 'py5',
    ('test_retry_before_giving_up', 8): 'py8',
    ('test_retry_before_giving_up', 9): '应当重试一次再放弃',
    ('test_retry_before_giving_up', 10): '\n>assert %(py10)s',
    ('test_retry_before_giving_up', 11): 'py10',
    ('test_retry_before_giving_up', 12): '正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。',
    ('test_retry_carries_a_warning', 0): '太短。',
    ('test_retry_carries_a_warning', 2): '严重不完整',
    ('test_retry_carries_a_warning', 3): 'py1',
    ('test_retry_carries_a_warning', 4): 'py4',
    ('test_retry_carries_a_warning', 5): 'py6',
    ('test_retry_carries_a_warning', 6): 'assert %(py8)s',
    ('test_retry_carries_a_warning', 7): 'py8',
    ('test_retry_carries_a_warning', 8): '正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。',
    ('test_complete_stitch_passes', 0): '这是一段完整的正文。',
    ('test_complete_stitch_passes', 1): '## 第12章 值班\n\n',
    ('test_complete_stitch_passes', 2): 'assert %(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}.stitch\n}(%(py9)s\n{%(py9)s = %(py7)s()\n}, %(py11)s)\n}',
    ('test_complete_stitch_passes', 3): 'py0',
    ('test_complete_stitch_passes', 4): 'Stitcher',
    ('test_complete_stitch_passes', 5): 'py1',
    ('test_complete_stitch_passes', 6): 'c',
    ('test_complete_stitch_passes', 7): 'py2',
    ('test_complete_stitch_passes', 8): 'SKILLS',
    ('test_complete_stitch_passes', 9): 'py4',
    ('test_complete_stitch_passes', 10): 'py6',
    ('test_complete_stitch_passes', 11): 'py7',
    ('test_complete_stitch_passes', 12): 'outline',
    ('test_complete_stitch_passes', 13): 'py9',
    ('test_complete_stitch_passes', 14): 'py11',
    ('test_complete_stitch_passes', 15): 'py13',
    ('test_complete_stitch_passes', 17): '这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。',
    ('test_complete_stitch_passes', 18): '正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。',
    ('test_shortening_is_allowed_within_reason', 0): '缝合本来就要删重复，适度变短是正常的。',
    ('test_shortening_is_allowed_within_reason', 5): '。',
    ('test_shortening_is_allowed_within_reason', 6): 'assert %(py12)s\n{%(py12)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}.stitch\n}(%(py9)s\n{%(py9)s = %(py7)s()\n}, %(py10)s)\n}',
    ('test_shortening_is_allowed_within_reason', 7): 'py0',
    ('test_shortening_is_allowed_within_reason', 8): 'Stitcher',
    ('test_shortening_is_allowed_within_reason', 9): 'py1',
    ('test_shortening_is_allowed_within_reason', 10): 'c',
    ('test_shortening_is_allowed_within_reason', 11): 'py2',
    ('test_shortening_is_allowed_within_reason', 12): 'SKILLS',
    ('test_shortening_is_allowed_within_reason', 13): 'py4',
    ('test_shortening_is_allowed_within_reason', 14): 'py6',
    ('test_shortening_is_allowed_within_reason', 15): 'py7',
    ('test_shortening_is_allowed_within_reason', 16): 'outline',
    ('test_shortening_is_allowed_within_reason', 17): 'py9',
    ('test_shortening_is_allowed_within_reason', 18): 'py10',
    ('test_shortening_is_allowed_within_reason', 19): 'scenes',
    ('test_shortening_is_allowed_within_reason', 20): 'py12',
    ('test_shortening_is_allowed_within_reason', 21): '正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。',
    ('TestTrailingNotesAreStripped', 0): 'TestTrailingNotesAreStripped',
    ('TestTrailingNotesAreStripped', 1): '实测：stitcher 三次缝合三次都在正文后面加了一段 `---` + 缝合说明\n（「年份原本三个场景各说一套…我按 s2 统一为…」）。输出是原样存盘的，\n说明就成了小说的一部分。而修订环修不掉它 —— 重写场景改不了 stitcher\n的习惯，每重缝一次就再加一遍，两轮上限白烧。',
    ('test_strips_from_the_separator', 2): '## 第3章 问号那一处\n\n她转过身。\n\n---\n\n缝合说明：统一了年份。',
    ('test_strips_from_the_separator', 3): '## 第3章 问号那一处\n\n她转过身。',
    ('test_strips_from_the_separator', 4): 'py0',
    ('test_strips_from_the_separator', 5): '_strip_trailing_notes',
    ('test_strips_from_the_separator', 6): 'py1',
    ('test_strips_from_the_separator', 7): 'text',
    ('test_strips_from_the_separator', 8): 'py3',
    ('test_strips_from_the_separator', 9): 'py6',
    ('test_strips_from_the_separator', 10): 'assert %(py8)s',
    ('test_strips_from_the_separator', 11): 'py8',
    ('test_keeps_chapters_that_have_no_notes', 2): '## 第1章 值班\n\n她接下了那份稿子。',
    ('test_keeps_chapters_that_have_no_notes', 3): 'py0',
    ('test_keeps_chapters_that_have_no_notes', 4): '_strip_trailing_notes',
    ('test_keeps_chapters_that_have_no_notes', 5): 'py1',
    ('test_keeps_chapters_that_have_no_notes', 6): 'text',
    ('test_keeps_chapters_that_have_no_notes', 7): 'py3',
    ('test_keeps_chapters_that_have_no_notes', 8): 'py5',
    ('test_keeps_chapters_that_have_no_notes', 9): 'assert %(py7)s',
    ('test_keeps_chapters_that_have_no_notes', 10): 'py7',
    ('test_does_not_touch_em_dashes_in_prose', 0): '正文里的 —— 是规范要求的破折号，不是分隔线。',
    ('test_does_not_touch_em_dashes_in_prose', 2): '## 第1章 值班\n\n她想说什么——最终没有说。',
    ('test_does_not_touch_em_dashes_in_prose', 3): 'py0',
    ('test_does_not_touch_em_dashes_in_prose', 4): '_strip_trailing_notes',
    ('test_does_not_touch_em_dashes_in_prose', 5): 'py1',
    ('test_does_not_touch_em_dashes_in_prose', 6): 'text',
    ('test_does_not_touch_em_dashes_in_prose', 7): 'py3',
    ('test_does_not_touch_em_dashes_in_prose', 8): 'py5',
    ('test_does_not_touch_em_dashes_in_prose', 9): 'assert %(py7)s',
    ('test_does_not_touch_em_dashes_in_prose', 10): 'py7',
    ('test_handles_other_separator_styles', 2): '## 第1章 值班\n\n正文。\n\n',
    ('test_handles_other_separator_styles', 3): '\n\n说明文字',
    ('test_handles_other_separator_styles', 4): '正文。',
    ('test_handles_other_separator_styles', 5): '\n>assert %(py9)s\n{%(py9)s = %(py5)s\n{%(py5)s = %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}.endswith\n}(%(py7)s)\n}',
    ('test_handles_other_separator_styles', 6): 'py0',
    ('test_handles_other_separator_styles', 7): '_strip_trailing_notes',
    ('test_handles_other_separator_styles', 8): 'py1',
    ('test_handles_other_separator_styles', 9): 'text',
    ('test_handles_other_separator_styles', 10): 'py3',
    ('test_handles_other_separator_styles', 11): 'py5',
    ('test_handles_other_separator_styles', 12): 'py7',
    ('test_handles_other_separator_styles', 13): 'py9',
    ('TestQuoteNormalisation', 0): 'TestQuoteNormalisation',
    ('TestQuoteNormalisation', 2): '两次事故都出在 ASCII 引号上：一轮修订后整章冒出 46 处 `"`，gate 全判错；\n更早一次「整章对话占比 0.0%」也是它 —— 对话占比只认全角引号。',
    ('test_pairs_are_opened_and_closed', 2): '她说"我知道了"。',
    ('test_pairs_are_opened_and_closed', 3): '她说“我知道了”。',
    ('test_pairs_are_opened_and_closed', 4): 'py0',
    ('test_pairs_are_opened_and_closed', 5): '_normalize_quotes',
    ('test_pairs_are_opened_and_closed', 6): 'py2',
    ('test_pairs_are_opened_and_closed', 7): 'py4',
    ('test_pairs_are_opened_and_closed', 8): 'py7',
    ('test_pairs_are_opened_and_closed', 9): 'assert %(py9)s',
    ('test_pairs_are_opened_and_closed', 10): 'py9',
    ('test_pairing_resets_each_line', 0): '对话跨段时一行里的引号常常不闭合，跨行累计会把后面全弄反。',
    ('test_pairing_resets_each_line', 2): '"第一句"\n"第二句"',
    ('test_pairing_resets_each_line', 3): '“第一句”\n“第二句”',
    ('test_pairing_resets_each_line', 4): 'py0',
    ('test_pairing_resets_each_line', 5): 'got',
    ('test_pairing_resets_each_line', 6): 'py3',
    ('test_pairing_resets_each_line', 7): 'assert %(py5)s',
    ('test_pairing_resets_each_line', 8): 'py5',
    ('test_single_quotes_are_left_alone', 0): '英文缩写里的撇号会被误伤。',
    ('test_single_quotes_are_left_alone', 2): "don't",
    ('test_single_quotes_are_left_alone', 3): 'py0',
    ('test_single_quotes_are_left_alone', 4): '_normalize_quotes',
    ('test_single_quotes_are_left_alone', 5): 'py2',
    ('test_single_quotes_are_left_alone', 6): 'py4',
    ('test_single_quotes_are_left_alone', 7): 'py7',
    ('test_single_quotes_are_left_alone', 8): 'assert %(py9)s',
    ('test_single_quotes_are_left_alone', 9): 'py9',
    ('test_postprocess_strips_before_normalising', 0): '顺序反了的话 `---` 会先被规范化成 `——-`，剥离规则就匹配不上。',
    ('test_postprocess_strips_before_normalising', 2): '## 第1章 值班\n\n正文。\n\n---\n\n缝合说明：略。',
    ('test_postprocess_strips_before_normalising', 3): '## 第1章 值班\n\n正文。',
    ('test_postprocess_strips_before_normalising', 4): 'py0',
    ('test_postprocess_strips_before_normalising', 5): 'got',
    ('test_postprocess_strips_before_normalising', 6): 'py3',
    ('test_postprocess_strips_before_normalising', 7): 'assert %(py5)s',
    ('test_postprocess_strips_before_normalising', 8): 'py5',
    ('test_ellipsis_and_dashes_are_normalised', 2): '她没说话...他也是--两个人就这么站着。',
    ('test_ellipsis_and_dashes_are_normalised', 3): '……',
    ('test_ellipsis_and_dashes_are_normalised', 4): '——',
    ('test_ellipsis_and_dashes_are_normalised', 5): '...',
    ('test_ellipsis_and_dashes_are_normalised', 6): 'py3',
    ('test_ellipsis_and_dashes_are_normalised', 7): 'py5',
    ('test_ellipsis_and_dashes_are_normalised', 8): 'got',
    ('test_ellipsis_and_dashes_are_normalised', 9): '%(py7)s',
    ('test_ellipsis_and_dashes_are_normalised', 10): 'py7',
    ('test_ellipsis_and_dashes_are_normalised', 11): 'py10',
    ('test_ellipsis_and_dashes_are_normalised', 12): 'py12',
    ('test_ellipsis_and_dashes_are_normalised', 13): '%(py14)s',
    ('test_ellipsis_and_dashes_are_normalised', 14): 'py14',
    ('test_ellipsis_and_dashes_are_normalised', 15): 'py17',
    ('test_ellipsis_and_dashes_are_normalised', 16): 'py19',
    ('test_ellipsis_and_dashes_are_normalised', 17): '%(py21)s',
    ('test_ellipsis_and_dashes_are_normalised', 18): 'py21',
    ('test_ellipsis_and_dashes_are_normalised', 19): 'assert %(py24)s',
    ('test_ellipsis_and_dashes_are_normalised', 20): 'py24',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def scene(sid, **kw):
    '图书馆'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  19           RESUME                   0
    # |  20           LOAD_GLOBAL              1 (dict + NULL)
    # |               LOAD_FAST_BORROW         0 (sid)
    # |               LOAD_CONST               0 ('图书馆')
    # |               LOAD_CONST               1 ('周四傍晚')
    # |               LOAD_CONST               2 ('shen')
    # |               LOAD_CONST               3 ('lu')
    # |               BUILD_LIST               2
    # |  21           LOAD_CONST               4 ('让她第一次没说出那句没关系')
    # |               LOAD_CONST               5 ('戒备')
    # |  22           LOAD_CONST               6 ('动摇')
    # |               LOAD_CONST               7 ('雨中共伞')
    # |               LOAD_CONST               8 (1200)
    # |  20           LOAD_CONST               9 (('id', 'where', 'when', 'present', 'goal', 'entry_emotion', 'exit_emotion', 'beat_type', 'target_words'))
    # |               CALL_KW                  9
    # |               STORE_FAST               2 (base)
    # |  23           LOAD_FAST_BORROW         2 (base)
    # |               LOAD_ATTR                3 (update + NULL|self)
    # |               LOAD_FAST_BORROW         1 (kw)
    # |               CALL                     1
    # |               POP_TOP
    # |  24           LOAD_GLOBAL              5 (SceneSpec + NULL)
    # |               LOAD_CONST              10 (())
    # |               BUILD_MAP                0
    # |               LOAD_FAST_BORROW         2 (base)
    # |               DICT_MERGE               1
    # |               CALL_FUNCTION_EX
    # |               RETURN_VALUE

def outline(**kw):
    '值班'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  27           RESUME                   0
    # |  28           LOAD_GLOBAL              1 (dict + NULL)
    # |               LOAD_SMALL_INT          12
    # |               LOAD_CONST               1 ('值班')
    # |               LOAD_CONST               2 ('大学')
    # |               LOAD_CONST               3 ('初次靠近')
    # |  29           LOAD_GLOBAL              3 (scene + NULL)
    # |               LOAD_CONST               4 ('ch012_s1')
    # |               CALL                     1
    # |               LOAD_GLOBAL              3 (scene + NULL)
    # |               LOAD_CONST               5 ('ch012_s2')
    # |               LOAD_CONST               6 ('动摇')
    # |  30           LOAD_CONST               7 ('不肯承认')
    # |  29           LOAD_CONST               8 (('entry_emotion', 'exit_emotion'))
    # |               CALL_KW                  3
    # |               BUILD_LIST               2
    # |  31           LOAD_CONST               9 ('伞留在了她手里')
    # |  28           LOAD_CONST              10 (('ch', 'title', 'stage', 'intent', 'scenes', 'hook'))
    # |               CALL_KW                  6
    # |               STORE_FAST               1 (base)
    # |  32           LOAD_FAST_BORROW         1 (base)
    # |               LOAD_ATTR                5 (update + NULL|self)
    # |               LOAD_FAST_BORROW         0 (kw)
    # |               CALL                     1
    # |               POP_TOP
    # |  33           LOAD_GLOBAL              7 (ChapterOutline + NULL)
    # |               LOAD_CONST              11 (())
    # |               BUILD_MAP                0
    # |               LOAD_FAST_BORROW         1 (base)
    # |               DICT_MERGE               1
    # |               CALL_FUNCTION_EX
    # |               RETURN_VALUE

class FakeClient:
    'FakeClient'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  36           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('FakeClient')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          36
    # |               STORE_NAME               3 (__firstlineno__)
    # |  37           LOAD_CONST               5 (('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。',))
    # |               LOAD_CONST               1 (<code object __init__ at 0x105577e30, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 37>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE   1 (defaults)
    # |               STORE_NAME               4 (__init__)
    # |  40           LOAD_CONST               2 (<code object complete at 0x105585e70, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 40>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (complete)
    # |               LOAD_CONST               3 (('calls', 'reply'))
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x105577e30, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 37>:
    # |  37           RESUME                   0
    # |  38           LOAD_FAST_BORROW         1 (reply)
    # |               BUILD_LIST               0
    # |               SWAP                     2
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               0 (reply)
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               1 (calls)
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object complete at 0x105585e70, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 40>:
    # |   --           MAKE_CELL                0 (self)
    # |   40           RESUME                   0
    # |   41           LOAD_FAST_BORROW         2 (prompt)
    # |                LOAD_ATTR                1 (validate + NULL|self)
    # |                CALL                     0
    # |                POP_TOP
    # |   42           LOAD_DEREF               0 (self)
    # |                LOAD_ATTR                2 (calls)
    # |                LOAD_ATTR                5 (append + NULL|self)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (role, prompt)
    # |                BUILD_TUPLE              2
    # |                CALL                     1
    # |                POP_TOP
    # |   44           LOAD_BUILD_CLASS
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (self)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               0 (<code object R at 0x10571bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 44>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_CONST               1 ('R')
    # |                CALL                     2
    # |                STORE_FAST               4 (R)
    # |   47           LOAD_FAST_BORROW         4 (R)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                RETURN_VALUE
    # | Disassembly of <code object R at 0x10571bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 44>:
    # |   --           COPY_FREE_VARS           1
    # |   44           RESUME                   0
    # |                LOAD_NAME                0 (__name__)
    # |                STORE_NAME               1 (__module__)
    # |                LOAD_CONST               0 ('FakeClient.complete.<locals>.R')
    # |                STORE_NAME               2 (__qualname__)
    # |                LOAD_SMALL_INT          44
    # |                STORE_NAME               3 (__firstlineno__)
    # |   45           LOAD_LOCALS
    # |                LOAD_FROM_DICT_OR_DEREF  0 (self)
    # |                LOAD_ATTR                8 (reply)
    # |                STORE_NAME               5 (text)
    # |                LOAD_CONST               1 (())
    # |                STORE_NAME               6 (__static_attributes__)
    # |                LOAD_CONST               2 (None)
    # |                RETURN_VALUE

    def __init__(self, reply):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  37           RESUME                   0
        # |  38           LOAD_FAST_BORROW         1 (reply)
        # |               BUILD_LIST               0
        # |               SWAP                     2
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               0 (reply)
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               1 (calls)
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE

    def complete(self, role, prompt, **kw):
        'R'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                0 (self)
        # |   40           RESUME                   0
        # |   41           LOAD_FAST_BORROW         2 (prompt)
        # |                LOAD_ATTR                1 (validate + NULL|self)
        # |                CALL                     0
        # |                POP_TOP
        # |   42           LOAD_DEREF               0 (self)
        # |                LOAD_ATTR                2 (calls)
        # |                LOAD_ATTR                5 (append + NULL|self)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (role, prompt)
        # |                BUILD_TUPLE              2
        # |                CALL                     1
        # |                POP_TOP
        # |   44           LOAD_BUILD_CLASS
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         0 (self)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               0 (<code object R at 0x10571bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 44>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_CONST               1 ('R')
        # |                CALL                     2
        # |                STORE_FAST               4 (R)
        # |   47           LOAD_FAST_BORROW         4 (R)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                RETURN_VALUE
        # | Disassembly of <code object R at 0x10571bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 44>:
        # |   --           COPY_FREE_VARS           1
        # |   44           RESUME                   0
        # |                LOAD_NAME                0 (__name__)
        # |                STORE_NAME               1 (__module__)
        # |                LOAD_CONST               0 ('FakeClient.complete.<locals>.R')
        # |                STORE_NAME               2 (__qualname__)
        # |                LOAD_SMALL_INT          44
        # |                STORE_NAME               3 (__firstlineno__)
        # |   45           LOAD_LOCALS
        # |                LOAD_FROM_DICT_OR_DEREF  0 (self)
        # |                LOAD_ATTR                8 (reply)
        # |                STORE_NAME               5 (text)
        # |                LOAD_CONST               1 (())
        # |                STORE_NAME               6 (__static_attributes__)
        # |                LOAD_CONST               2 (None)
        # |                RETURN_VALUE

        class R:
            'FakeClient.complete.<locals>.R'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |   44           RESUME                   0
            # |                LOAD_NAME                0 (__name__)
            # |                STORE_NAME               1 (__module__)
            # |                LOAD_CONST               0 ('FakeClient.complete.<locals>.R')
            # |                STORE_NAME               2 (__qualname__)
            # |                LOAD_SMALL_INT          44
            # |                STORE_NAME               3 (__firstlineno__)
            # |   45           LOAD_LOCALS
            # |                LOAD_FROM_DICT_OR_DEREF  0 (self)
            # |                LOAD_ATTR                8 (reply)
            # |                STORE_NAME               5 (text)
            # |                LOAD_CONST               1 (())
            # |                STORE_NAME               6 (__static_attributes__)
            # |                LOAD_CONST               2 (None)
            # |                RETURN_VALUE



def writer():
    pass  # 无 docstring
    # ── 函数体（字节码重建见 BODY 段）──
    # |  50           RESUME                   0
    # |  52           LOAD_GLOBAL              1 (FakeClient + NULL)
    # |               CALL                     0
    # |               STORE_FAST               0 (c)
    # |  53           LOAD_GLOBAL              3 (Writer + NULL)
    # |               LOAD_FAST_BORROW         0 (c)
    # |               LOAD_GLOBAL              4 (SKILLS)
    # |               CALL                     2
    # |               LOAD_FAST_BORROW         0 (c)
    # |               BUILD_TUPLE              2
    # |               RETURN_VALUE

def stitcher():
    pass  # 无 docstring
    # ── 函数体（字节码重建见 BODY 段）──
    # |  56           RESUME                   0
    # |  58           LOAD_GLOBAL              1 (FakeClient + NULL)
    # |               CALL                     0
    # |               STORE_FAST               0 (c)
    # |  59           LOAD_GLOBAL              3 (Stitcher + NULL)
    # |               LOAD_FAST_BORROW         0 (c)
    # |               LOAD_GLOBAL              4 (SKILLS)
    # |               CALL                     2
    # |               LOAD_FAST_BORROW         0 (c)
    # |               BUILD_TUPLE              2
    # |               RETURN_VALUE

class TestWriterLayering:
    'TestWriterLayering'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  62           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestWriterLayering')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          62
    # |               STORE_NAME               3 (__firstlineno__)
    # |  63           LOAD_CONST               1 (<code object test_design_time_skills_absent at 0x755ec63800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 63>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_design_time_skills_absent)
    # |  71           LOAD_CONST               2 (<code object test_scene_spec_lives_in_volatile_layer at 0x755ee29800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 71>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_scene_spec_lives_in_volatile_layer)
    # |  79           LOAD_CONST               3 (<code object test_emotion_shift_is_emphasised at 0x755ee47900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 79>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_emotion_shift_is_emphasised)
    # |  85           LOAD_CONST               4 (<code object test_character_names_resolved_from_state at 0x755ee47c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 85>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_character_names_resolved_from_state)
    # |  92           LOAD_CONST               5 (<code object test_prev_tail_truncated_and_placed_volatile at 0x755f1ed400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 92>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_prev_tail_truncated_and_placed_volatile)
    # | 100           LOAD_CONST               6 (<code object test_intimacy_level_instruction at 0x755ee29e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 100>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_intimacy_level_instruction)
    # | 107           LOAD_CONST               7 (<code object test_must_not_surfaced at 0x755ee27c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 107>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_must_not_surfaced)
    # |               LOAD_CONST               8 (())
    # |               STORE_NAME              11 (__static_attributes__)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_design_time_skills_absent at 0x755ec63800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 63>:
    # |  63            RESUME                   0
    # |  65            LOAD_FAST_BORROW         1 (writer)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   52 (w, _)
    # |  66            LOAD_FAST_BORROW         3 (w)
    # |                LOAD_ATTR                1 (system_core + NULL|self)
    # |                CALL                     0
    # |                STORE_FAST               5 (core)
    # |  67            BUILD_LIST               0
    # |                STORE_FAST               6 (@py_assert1)
    # |                LOAD_CONST               1 ('叙述语感')
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert0, @py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        8 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_CONST               2 ('对话技法')
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert11, @py_assert11)
    # |                STORE_FAST               9 (@py_assert0)
    # |        L1:     LOAD_FAST_BORROW         9 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       404 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('in',))
    # |                LOAD_FAST_BORROW         8 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py3)s in %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (@py_assert2, core)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py3')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                6 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py5')
    # |                LOAD_CONST               5 ('core')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                6 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST               5 ('core')
    # |        L4:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format6)
    # |                LOAD_CONST               6 ('%(py7)s')
    # |                LOAD_CONST               7 ('py7')
    # |                LOAD_FAST_BORROW        12 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   214 (@py_format8, @py_assert1)
    # |                LOAD_ATTR               15 (append + NULL|self)
    # |                LOAD_FAST_BORROW        13 (@py_format8)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW         8 (@py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      163 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('in',))
    # |                LOAD_FAST_CHECK         11 (@py_assert11)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              21 (('%(py10)s in %(py12)s',))
    # |                LOAD_FAST_CHECK         10 (@py_assert9)
    # |                LOAD_FAST_BORROW         5 (core)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py10')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                6 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py12')
    # |                LOAD_CONST               5 ('core')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                6 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               5 ('core')
    # |        L7:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format13)
    # |                LOAD_CONST              10 ('%(py14)s')
    # |                LOAD_CONST              11 ('py14')
    # |                LOAD_FAST_BORROW        14 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   246 (@py_format15, @py_assert1)
    # |                LOAD_ATTR               15 (append + NULL|self)
    # |                LOAD_FAST_BORROW        15 (@py_format15)
    # |                CALL                     1
    # |                POP_TOP
    # |        L8:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format16)
    # |                LOAD_CONST              12 ('assert %(py17)s')
    # |                LOAD_CONST              13 ('py17')
    # |                LOAD_FAST_BORROW        16 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format18)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        17 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L9:     LOAD_CONST              14 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  171 (@py_assert9, @py_assert11)
    # |  68            LOAD_CONST              15 ('人物设计法')
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       177 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 (('not in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              23 (('%(py1)s not in %(py3)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 149 (@py_assert0, core)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              16 ('py1')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                6 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('py3')
    # |                LOAD_CONST               5 ('core')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                6 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST               5 ('core')
    # |       L12:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format4)
    # |                LOAD_CONST              17 ('assert %(py5)s')
    # |                LOAD_CONST               4 ('py5')
    # |                LOAD_FAST_BORROW        18 (@py_format4)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format6)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format6)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L13:     LOAD_CONST              14 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  151 (@py_assert0, @py_assert2)
    # |  69            LOAD_CONST              18 ('情绪节拍模板库')
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       177 (to L17)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 (('not in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              23 (('%(py1)s not in %(py3)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 149 (@py_assert0, core)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              16 ('py1')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                6 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('py3')
    # |                LOAD_CONST               5 ('core')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L15)
    # |                NOT_TAKEN
    # |       L14:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                6 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (core)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L16)
    # |       L15:     LOAD_CONST               5 ('core')
    # |       L16:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format4)
    # |                LOAD_CONST              17 ('assert %(py5)s')
    # |                LOAD_CONST               4 ('py5')
    # |                LOAD_FAST_BORROW        18 (@py_format4)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format6)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format6)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L17:     LOAD_CONST              14 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  151 (@py_assert0, @py_assert2)
    # |                LOAD_CONST              14 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_scene_spec_lives_in_volatile_layer at 0x755ee29800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 71>:
    # |  71            RESUME                   0
    # |  72            LOAD_FAST_BORROW         1 (writer)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   52 (w, c)
    # |  73            LOAD_GLOBAL              1 (outline + NULL)
    # |                CALL                     0
    # |                STORE_FAST               5 (o)
    # |  74            LOAD_FAST_BORROW         3 (w)
    # |                LOAD_ATTR                3 (write_scene + NULL|self)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |                LOAD_FAST_BORROW         5 (o)
    # |                LOAD_ATTR                4 (scenes)
    # |                LOAD_SMALL_INT           0
    # |                BINARY_OP               26 ([])
    # |                CALL                     3
    # |                POP_TOP
    # |  75            LOAD_FAST_BORROW         4 (c)
    # |                LOAD_ATTR                6 (calls)
    # |                LOAD_CONST              13 (-1)
    # |                BINARY_OP               26 ([])
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST  103 (_, p)
    # |  76            LOAD_CONST               1 ('ch012_s1')
    # |                STORE_FAST_LOAD_FAST   135 (@py_assert0, p)
    # |                LOAD_ATTR                8 (instruction)
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert0)
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              14 (('in',))
    # |                LOAD_FAST_BORROW        10 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              15 (('%(py1)s in %(py5)s\n{%(py5)s = %(py3)s.instruction\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert0, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('py3')
    # |                LOAD_CONST               4 ('p')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('p')
    # |        L3:     LOAD_CONST               5 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format6)
    # |                LOAD_CONST               6 ('assert %(py7)s')
    # |                LOAD_CONST               7 ('py7')
    # |                LOAD_FAST_BORROW        11 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format8)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  169 (@py_assert2, @py_assert4)
    # |  77            LOAD_CONST               1 ('ch012_s1')
    # |                STORE_FAST_LOAD_FAST   135 (@py_assert0, p)
    # |                LOAD_ATTR               26 (system_core)
    # |                STORE_FAST_LOAD_FAST   151 (@py_assert4, p)
    # |                LOAD_ATTR               28 (bible)
    # |                STORE_FAST_LOAD_FAST   217 (@py_assert7, @py_assert4)
    # |                LOAD_FAST_BORROW        13 (@py_assert7)
    # |                BINARY_OP                0 (+)
    # |                STORE_FAST_LOAD_FAST   232 (@py_assert9, @py_assert0)
    # |                LOAD_FAST_BORROW        14 (@py_assert9)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       299 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('not in',))
    # |                LOAD_FAST_BORROW        10 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py1)s not in (%(py5)s\n{%(py5)s = %(py3)s.system_core\n} + %(py8)s\n{%(py8)s = %(py6)s.bible\n})',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 142 (@py_assert0, @py_assert9)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('py3')
    # |                LOAD_CONST               4 ('p')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               4 ('p')
    # |        L7:     LOAD_CONST               5 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py6')
    # |                LOAD_CONST               4 ('p')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               4 ('p')
    # |       L10:     LOAD_CONST              10 ('py8')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_assert7)
    # |                CALL                     1
    # |                BUILD_MAP                5
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format10)
    # |                LOAD_CONST              11 ('assert %(py11)s')
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_FAST_BORROW        15 (@py_format10)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format12)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        16 (@py_format12)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L11:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  222 (@py_assert7, @py_assert9)
    # |                LOAD_CONST               8 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_emotion_shift_is_emphasised at 0x755ee47900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 79>:
    # |  79           RESUME                   0
    # |  80           LOAD_FAST_BORROW         1 (writer)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   52 (w, c)
    # |  81           LOAD_GLOBAL              1 (outline + NULL)
    # |               CALL                     0
    # |               STORE_FAST               5 (o)
    # |  82           LOAD_FAST_BORROW         3 (w)
    # |               LOAD_ATTR                3 (write_scene + NULL|self)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |               LOAD_FAST_BORROW         5 (o)
    # |               LOAD_ATTR                4 (scenes)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               CALL                     3
    # |               POP_TOP
    # |  83           LOAD_CONST               1 ('戒备 → 动摇')
    # |               STORE_FAST_LOAD_FAST   100 (@py_assert0, c)
    # |               LOAD_ATTR                6 (calls)
    # |               LOAD_CONST               8 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |               LOAD_ATTR                8 (instruction)
    # |               STORE_FAST_LOAD_FAST   134 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 (('in',))
    # |               LOAD_FAST_BORROW         9 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              10 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.instruction\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py6')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_CONST               5 ('assert %(py8)s')
    # |               LOAD_CONST               6 ('py8')
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format9)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_character_names_resolved_from_state at 0x755ee47c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 85>:
    # |  85           RESUME                   0
    # |  87           LOAD_FAST_BORROW         1 (writer)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   52 (w, c)
    # |  88           LOAD_GLOBAL              1 (outline + NULL)
    # |               CALL                     0
    # |               STORE_FAST               5 (o)
    # |  89           LOAD_FAST_BORROW         3 (w)
    # |               LOAD_ATTR                3 (write_scene + NULL|self)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |               LOAD_FAST_BORROW         5 (o)
    # |               LOAD_ATTR                4 (scenes)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               CALL                     3
    # |               POP_TOP
    # |  90           LOAD_CONST               1 ('沈知微')
    # |               STORE_FAST_LOAD_FAST   100 (@py_assert0, c)
    # |               LOAD_ATTR                6 (calls)
    # |               LOAD_CONST               8 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |               LOAD_ATTR                8 (instruction)
    # |               STORE_FAST_LOAD_FAST   134 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 (('in',))
    # |               LOAD_FAST_BORROW         9 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              10 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.instruction\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py6')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_CONST               5 ('assert %(py8)s')
    # |               LOAD_CONST               6 ('py8')
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format9)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_prev_tail_truncated_and_placed_volatile at 0x755f1ed400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 92>:
    # |  92            RESUME                   0
    # |  93            LOAD_FAST_BORROW         1 (writer)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   52 (w, c)
    # |  94            LOAD_GLOBAL              1 (outline + NULL)
    # |                CALL                     0
    # |                STORE_FAST               5 (o)
    # |  95            LOAD_FAST_BORROW         3 (w)
    # |                LOAD_ATTR                3 (write_scene + NULL|self)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |                LOAD_FAST_BORROW         5 (o)
    # |                LOAD_ATTR                4 (scenes)
    # |                LOAD_SMALL_INT           0
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              20 ('上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上')
    # |                LOAD_CONST               1 (('prev_text',))
    # |                CALL_KW                  4
    # |                POP_TOP
    # |  96            LOAD_FAST_BORROW         4 (c)
    # |                LOAD_ATTR                6 (calls)
    # |                LOAD_CONST              21 (-1)
    # |                BINARY_OP               26 ([])
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST  103 (_, p)
    # |  97            LOAD_FAST_BORROW         7 (p)
    # |                LOAD_ATTR                8 (prev_tail)
    # |                STORE_FAST               8 (@py_assert2)
    # |                LOAD_GLOBAL             11 (len + NULL)
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   147 (@py_assert4, w)
    # |                LOAD_ATTR               12 (prev_tail_chars)
    # |                STORE_FAST_LOAD_FAST   169 (@py_assert8, @py_assert4)
    # |                LOAD_FAST_BORROW        10 (@py_assert8)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert6, @py_assert6)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       385 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 (('==',))
    # |                LOAD_FAST_BORROW        11 (@py_assert6)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              23 (('%(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s.prev_tail\n})\n} == %(py9)s\n{%(py9)s = %(py7)s.prev_tail_chars\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert4, @py_assert8)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('len')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (len)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (len)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               3 ('len')
    # |        L3:     LOAD_CONST               4 ('py1')
    # |                LOAD_CONST               5 ('p')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               5 ('p')
    # |        L6:     LOAD_CONST               6 ('py3')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py5')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_CONST               9 ('w')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (w)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (w)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               9 ('w')
    # |        L9:     LOAD_CONST              10 ('py9')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert8)
    # |                CALL                     1
    # |                BUILD_MAP                6
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format10)
    # |                LOAD_CONST              11 ('assert %(py11)s')
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_FAST_BORROW        12 (@py_format10)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format12)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_format12)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              13 (None)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  186 (@py_assert6, @py_assert8)
    # |  98            LOAD_FAST_BORROW         7 (p)
    # |                LOAD_ATTR                8 (prev_tail)
    # |                STORE_FAST_LOAD_FAST   231 (@py_assert1, p)
    # |                LOAD_ATTR               30 (system_core)
    # |                STORE_FAST_LOAD_FAST   247 (@py_assert5, p)
    # |                LOAD_ATTR               32 (bible)
    # |                STORE_FAST_LOAD_FAST   175 (@py_assert8, @py_assert5)
    # |                LOAD_FAST_BORROW        10 (@py_assert8)
    # |                BINARY_OP                0 (+)
    # |                STORE_FAST              16 (@py_assert10)
    # |                LOAD_FAST_BORROW         7 (p)
    # |                LOAD_ATTR               34 (volume)
    # |                STORE_FAST              17 (@py_assert12)
    # |                LOAD_FAST_BORROW        16 (@py_assert10)
    # |                LOAD_FAST_BORROW        17 (@py_assert12)
    # |                BINARY_OP                0 (+)
    # |                STORE_FAST              18 (@py_assert14)
    # |                LOAD_FAST_BORROW        14 (@py_assert1)
    # |                LOAD_FAST_BORROW        18 (@py_assert14)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST              19 (@py_assert3)
    # |                LOAD_FAST_BORROW        19 (@py_assert3)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       478 (to L23)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              24 (('not in',))
    # |                LOAD_FAST_BORROW        19 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              25 (('%(py2)s\n{%(py2)s = %(py0)s.prev_tail\n} not in ((%(py6)s\n{%(py6)s = %(py4)s.system_core\n} + %(py9)s\n{%(py9)s = %(py7)s.bible\n}) + %(py13)s\n{%(py13)s = %(py11)s.volume\n})',))
    # |                LOAD_FAST_BORROW        14 (@py_assert1)
    # |                LOAD_FAST_BORROW        18 (@py_assert14)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               5 ('p')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L12)
    # |                NOT_TAKEN
    # |       L11:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L13)
    # |       L12:     LOAD_CONST               5 ('p')
    # |       L13:     LOAD_CONST              14 ('py2')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        14 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py4')
    # |                LOAD_CONST               5 ('p')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L15)
    # |                NOT_TAKEN
    # |       L14:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L16)
    # |       L15:     LOAD_CONST               5 ('p')
    # |       L16:     LOAD_CONST              16 ('py6')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        15 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_CONST               5 ('p')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L17)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L18)
    # |                NOT_TAKEN
    # |       L17:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L19)
    # |       L18:     LOAD_CONST               5 ('p')
    # |       L19:     LOAD_CONST              10 ('py9')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_CONST               5 ('p')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L20)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L21)
    # |                NOT_TAKEN
    # |       L20:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L22)
    # |       L21:     LOAD_CONST               5 ('p')
    # |       L22:     LOAD_CONST              17 ('py13')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        17 (@py_assert12)
    # |                CALL                     1
    # |                BUILD_MAP                8
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              20 (@py_format15)
    # |                LOAD_CONST              18 ('assert %(py16)s')
    # |                LOAD_CONST              19 ('py16')
    # |                LOAD_FAST_BORROW        20 (@py_format15)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              21 (@py_format17)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        21 (@py_format17)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L23:     LOAD_CONST              13 (None)
    # |                COPY                     1
    # |                STORE_FAST              14 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST              19 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST              15 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST              16 (@py_assert10)
    # |                COPY                     1
    # |                STORE_FAST              17 (@py_assert12)
    # |                STORE_FAST              18 (@py_assert14)
    # |                LOAD_CONST              13 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_intimacy_level_instruction at 0x755ee29e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 100>:
    # | 100           RESUME                   0
    # | 101           LOAD_FAST_BORROW         1 (writer)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   52 (w, c)
    # | 102           LOAD_GLOBAL              1 (outline + NULL)
    # |               LOAD_GLOBAL              3 (scene + NULL)
    # |               LOAD_CONST               0 ('L2')
    # |               LOAD_CONST               1 (('intimacy_level',))
    # |               CALL_KW                  1
    # | 103           LOAD_GLOBAL              3 (scene + NULL)
    # |               LOAD_CONST               2 ('ch012_s2')
    # |               LOAD_CONST               3 ('a')
    # |               LOAD_CONST               4 ('b')
    # |               LOAD_CONST               5 (('entry_emotion', 'exit_emotion'))
    # |               CALL_KW                  3
    # | 102           BUILD_LIST               2
    # |               LOAD_CONST               6 (('scenes',))
    # |               CALL_KW                  1
    # |               STORE_FAST               5 (o)
    # | 104           LOAD_FAST_BORROW         3 (w)
    # |               LOAD_ATTR                5 (write_scene + NULL|self)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |               LOAD_FAST_BORROW         5 (o)
    # |               LOAD_ATTR                6 (scenes)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               CALL                     3
    # |               POP_TOP
    # | 105           BUILD_LIST               0
    # |               STORE_FAST               6 (@py_assert1)
    # |               LOAD_CONST               0 ('L2')
    # |               STORE_FAST_LOAD_FAST   116 (@py_assert2, c)
    # |               LOAD_ATTR                8 (calls)
    # |               LOAD_CONST              21 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert5, @py_assert5)
    # |               LOAD_ATTR               10 (instruction)
    # |               STORE_FAST_LOAD_FAST   151 (@py_assert7, @py_assert2)
    # |               LOAD_FAST_BORROW         9 (@py_assert7)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert4, @py_assert4)
    # |               STORE_FAST_LOAD_FAST   186 (@py_assert0, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       44 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_CONST               7 ('收住')
    # |               STORE_FAST_LOAD_FAST   196 (@py_assert12, c)
    # |               LOAD_ATTR                8 (calls)
    # |               LOAD_CONST              21 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   221 (@py_assert15, @py_assert15)
    # |               LOAD_ATTR               10 (instruction)
    # |               STORE_FAST_LOAD_FAST   236 (@py_assert17, @py_assert12)
    # |               LOAD_FAST_BORROW        14 (@py_assert17)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   255 (@py_assert14, @py_assert14)
    # |               STORE_FAST              11 (@py_assert0)
    # |       L1:     LOAD_FAST_BORROW        11 (@py_assert0)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       338 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              22 (('in',))
    # |               LOAD_FAST_BORROW        10 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              23 (('%(py3)s in %(py8)s\n{%(py8)s = %(py6)s.instruction\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 121 (@py_assert2, @py_assert7)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               8 ('py3')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py6')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py8')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert7)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              16 (@py_format9)
    # |               LOAD_CONST              11 ('%(py10)s')
    # |               LOAD_CONST              12 ('py10')
    # |               LOAD_FAST_BORROW        16 (@py_format9)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              17 (@py_format11)
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               LOAD_ATTR               19 (append + NULL|self)
    # |               LOAD_FAST_BORROW        17 (@py_format11)
    # |               CALL                     1
    # |               POP_TOP
    # |               LOAD_FAST_BORROW        10 (@py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE      130 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              22 (('in',))
    # |               LOAD_FAST_CHECK         15 (@py_assert14)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              24 (('%(py13)s in %(py18)s\n{%(py18)s = %(py16)s.instruction\n}',))
    # |               LOAD_FAST_CHECK         12 (@py_assert12)
    # |               LOAD_FAST_CHECK         14 (@py_assert17)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              13 ('py13')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        12 (@py_assert12)
    # |               CALL                     1
    # |               LOAD_CONST              14 ('py16')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_CHECK         13 (@py_assert15)
    # |               CALL                     1
    # |               LOAD_CONST              15 ('py18')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        14 (@py_assert17)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              18 (@py_format19)
    # |               LOAD_CONST              16 ('%(py20)s')
    # |               LOAD_CONST              17 ('py20')
    # |               LOAD_FAST_BORROW        18 (@py_format19)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              19 (@py_format21)
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               LOAD_ATTR               19 (append + NULL|self)
    # |               LOAD_FAST_BORROW        19 (@py_format21)
    # |               CALL                     1
    # |               POP_TOP
    # |       L2:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_boolop)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BUILD_MAP                0
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              20 (@py_format22)
    # |               LOAD_CONST              18 ('assert %(py23)s')
    # |               LOAD_CONST              19 ('py23')
    # |               LOAD_FAST_BORROW        20 (@py_format22)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              21 (@py_format24)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        21 (@py_format24)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L3:     LOAD_CONST              20 (None)
    # |               COPY                     1
    # |               STORE_FAST              11 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST              10 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST              12 (@py_assert12)
    # |               COPY                     1
    # |               STORE_FAST              15 (@py_assert14)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  222 (@py_assert15, @py_assert17)
    # |               LOAD_CONST              20 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_must_not_surfaced at 0x755ee27c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 107>:
    # | 107           RESUME                   0
    # | 108           LOAD_FAST_BORROW         1 (writer)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   52 (w, c)
    # | 109           LOAD_GLOBAL              1 (outline + NULL)
    # |               LOAD_GLOBAL              3 (scene + NULL)
    # |               LOAD_CONST               0 ('提到那把伞的来历')
    # |               BUILD_LIST               1
    # |               LOAD_CONST               1 (('must_not',))
    # |               CALL_KW                  1
    # | 110           LOAD_GLOBAL              3 (scene + NULL)
    # |               LOAD_CONST               2 ('ch012_s2')
    # |               LOAD_CONST               3 ('a')
    # |               LOAD_CONST               4 ('b')
    # |               LOAD_CONST               5 (('entry_emotion', 'exit_emotion'))
    # |               CALL_KW                  3
    # | 109           BUILD_LIST               2
    # |               LOAD_CONST               6 (('scenes',))
    # |               CALL_KW                  1
    # |               STORE_FAST               5 (o)
    # | 111           LOAD_FAST_BORROW         3 (w)
    # |               LOAD_ATTR                5 (write_scene + NULL|self)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |               LOAD_FAST_BORROW         5 (o)
    # |               LOAD_ATTR                6 (scenes)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               CALL                     3
    # |               POP_TOP
    # | 112           LOAD_CONST               7 ('禁止出现')
    # |               STORE_FAST_LOAD_FAST   100 (@py_assert0, c)
    # |               LOAD_ATTR                8 (calls)
    # |               LOAD_CONST              14 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |               LOAD_ATTR               10 (instruction)
    # |               STORE_FAST_LOAD_FAST   134 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('in',))
    # |               LOAD_FAST_BORROW         9 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.instruction\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               8 ('py1')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py6')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_CONST              11 ('assert %(py8)s')
    # |               LOAD_CONST              12 ('py8')
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format9)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert3, @py_assert5)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE

    def test_design_time_skills_absent(self, writer, sample_state):
        'writer 拿的是设计的产物，不该背着设计方法。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  63            RESUME                   0
        # |  65            LOAD_FAST_BORROW         1 (writer)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   52 (w, _)
        # |  66            LOAD_FAST_BORROW         3 (w)
        # |                LOAD_ATTR                1 (system_core + NULL|self)
        # |                CALL                     0
        # |                STORE_FAST               5 (core)
        # |  67            BUILD_LIST               0
        # |                STORE_FAST               6 (@py_assert1)
        # |                LOAD_CONST               1 ('叙述语感')
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
        # |                STORE_FAST_LOAD_FAST   152 (@py_assert0, @py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE        8 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_CONST               2 ('对话技法')
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert11, @py_assert11)
        # |                STORE_FAST               9 (@py_assert0)
        # |        L1:     LOAD_FAST_BORROW         9 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       404 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('in',))
        # |                LOAD_FAST_BORROW         8 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py3)s in %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 117 (@py_assert2, core)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py3')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                6 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py5')
        # |                LOAD_CONST               5 ('core')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                6 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST               5 ('core')
        # |        L4:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format6)
        # |                LOAD_CONST               6 ('%(py7)s')
        # |                LOAD_CONST               7 ('py7')
        # |                LOAD_FAST_BORROW        12 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   214 (@py_format8, @py_assert1)
        # |                LOAD_ATTR               15 (append + NULL|self)
        # |                LOAD_FAST_BORROW        13 (@py_format8)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW         8 (@py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      163 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('in',))
        # |                LOAD_FAST_CHECK         11 (@py_assert11)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              21 (('%(py10)s in %(py12)s',))
        # |                LOAD_FAST_CHECK         10 (@py_assert9)
        # |                LOAD_FAST_BORROW         5 (core)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py10')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                6 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert9)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py12')
        # |                LOAD_CONST               5 ('core')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                6 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               5 ('core')
        # |        L7:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format13)
        # |                LOAD_CONST              10 ('%(py14)s')
        # |                LOAD_CONST              11 ('py14')
        # |                LOAD_FAST_BORROW        14 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   246 (@py_format15, @py_assert1)
        # |                LOAD_ATTR               15 (append + NULL|self)
        # |                LOAD_FAST_BORROW        15 (@py_format15)
        # |                CALL                     1
        # |                POP_TOP
        # |        L8:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format16)
        # |                LOAD_CONST              12 ('assert %(py17)s')
        # |                LOAD_CONST              13 ('py17')
        # |                LOAD_FAST_BORROW        16 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format18)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        17 (@py_format18)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L9:     LOAD_CONST              14 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  171 (@py_assert9, @py_assert11)
        # |  68            LOAD_CONST              15 ('人物设计法')
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       177 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              22 (('not in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              23 (('%(py1)s not in %(py3)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 149 (@py_assert0, core)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              16 ('py1')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                6 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('py3')
        # |                LOAD_CONST               5 ('core')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                6 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST               5 ('core')
        # |       L12:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format4)
        # |                LOAD_CONST              17 ('assert %(py5)s')
        # |                LOAD_CONST               4 ('py5')
        # |                LOAD_FAST_BORROW        18 (@py_format4)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format6)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format6)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L13:     LOAD_CONST              14 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  151 (@py_assert0, @py_assert2)
        # |  69            LOAD_CONST              18 ('情绪节拍模板库')
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       177 (to L17)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              22 (('not in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              23 (('%(py1)s not in %(py3)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 149 (@py_assert0, core)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              16 ('py1')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                6 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('py3')
        # |                LOAD_CONST               5 ('core')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L15)
        # |                NOT_TAKEN
        # |       L14:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                6 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (core)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L16)
        # |       L15:     LOAD_CONST               5 ('core')
        # |       L16:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format4)
        # |                LOAD_CONST              17 ('assert %(py5)s')
        # |                LOAD_CONST               4 ('py5')
        # |                LOAD_FAST_BORROW        18 (@py_format4)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format6)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format6)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L17:     LOAD_CONST              14 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  151 (@py_assert0, @py_assert2)
        # |                LOAD_CONST              14 (None)
        # |                RETURN_VALUE

    def test_scene_spec_lives_in_volatile_layer(self, writer, sample_state):
        'ch012_s1'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  71            RESUME                   0
        # |  72            LOAD_FAST_BORROW         1 (writer)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   52 (w, c)
        # |  73            LOAD_GLOBAL              1 (outline + NULL)
        # |                CALL                     0
        # |                STORE_FAST               5 (o)
        # |  74            LOAD_FAST_BORROW         3 (w)
        # |                LOAD_ATTR                3 (write_scene + NULL|self)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |                LOAD_FAST_BORROW         5 (o)
        # |                LOAD_ATTR                4 (scenes)
        # |                LOAD_SMALL_INT           0
        # |                BINARY_OP               26 ([])
        # |                CALL                     3
        # |                POP_TOP
        # |  75            LOAD_FAST_BORROW         4 (c)
        # |                LOAD_ATTR                6 (calls)
        # |                LOAD_CONST              13 (-1)
        # |                BINARY_OP               26 ([])
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST  103 (_, p)
        # |  76            LOAD_CONST               1 ('ch012_s1')
        # |                STORE_FAST_LOAD_FAST   135 (@py_assert0, p)
        # |                LOAD_ATTR                8 (instruction)
        # |                STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert0)
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              14 (('in',))
        # |                LOAD_FAST_BORROW        10 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              15 (('%(py1)s in %(py5)s\n{%(py5)s = %(py3)s.instruction\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert0, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('py3')
        # |                LOAD_CONST               4 ('p')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('p')
        # |        L3:     LOAD_CONST               5 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format6)
        # |                LOAD_CONST               6 ('assert %(py7)s')
        # |                LOAD_CONST               7 ('py7')
        # |                LOAD_FAST_BORROW        11 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format8)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  169 (@py_assert2, @py_assert4)
        # |  77            LOAD_CONST               1 ('ch012_s1')
        # |                STORE_FAST_LOAD_FAST   135 (@py_assert0, p)
        # |                LOAD_ATTR               26 (system_core)
        # |                STORE_FAST_LOAD_FAST   151 (@py_assert4, p)
        # |                LOAD_ATTR               28 (bible)
        # |                STORE_FAST_LOAD_FAST   217 (@py_assert7, @py_assert4)
        # |                LOAD_FAST_BORROW        13 (@py_assert7)
        # |                BINARY_OP                0 (+)
        # |                STORE_FAST_LOAD_FAST   232 (@py_assert9, @py_assert0)
        # |                LOAD_FAST_BORROW        14 (@py_assert9)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       299 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('not in',))
        # |                LOAD_FAST_BORROW        10 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py1)s not in (%(py5)s\n{%(py5)s = %(py3)s.system_core\n} + %(py8)s\n{%(py8)s = %(py6)s.bible\n})',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 142 (@py_assert0, @py_assert9)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('py3')
        # |                LOAD_CONST               4 ('p')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               4 ('p')
        # |        L7:     LOAD_CONST               5 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py6')
        # |                LOAD_CONST               4 ('p')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               4 ('p')
        # |       L10:     LOAD_CONST              10 ('py8')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_assert7)
        # |                CALL                     1
        # |                BUILD_MAP                5
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format10)
        # |                LOAD_CONST              11 ('assert %(py11)s')
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_FAST_BORROW        15 (@py_format10)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format12)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        16 (@py_format12)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L11:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  222 (@py_assert7, @py_assert9)
        # |                LOAD_CONST               8 (None)
        # |                RETURN_VALUE

    def test_emotion_shift_is_emphasised(self, writer, sample_state):
        '戒备 → 动摇'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  79           RESUME                   0
        # |  80           LOAD_FAST_BORROW         1 (writer)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   52 (w, c)
        # |  81           LOAD_GLOBAL              1 (outline + NULL)
        # |               CALL                     0
        # |               STORE_FAST               5 (o)
        # |  82           LOAD_FAST_BORROW         3 (w)
        # |               LOAD_ATTR                3 (write_scene + NULL|self)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |               LOAD_FAST_BORROW         5 (o)
        # |               LOAD_ATTR                4 (scenes)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               CALL                     3
        # |               POP_TOP
        # |  83           LOAD_CONST               1 ('戒备 → 动摇')
        # |               STORE_FAST_LOAD_FAST   100 (@py_assert0, c)
        # |               LOAD_ATTR                6 (calls)
        # |               LOAD_CONST               8 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |               LOAD_ATTR                8 (instruction)
        # |               STORE_FAST_LOAD_FAST   134 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 (('in',))
        # |               LOAD_FAST_BORROW         9 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              10 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.instruction\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py6')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_CONST               5 ('assert %(py8)s')
        # |               LOAD_CONST               6 ('py8')
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format9)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_character_names_resolved_from_state(self, writer, sample_state):
        '规格里存的是 id，指令里要给人名。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  85           RESUME                   0
        # |  87           LOAD_FAST_BORROW         1 (writer)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   52 (w, c)
        # |  88           LOAD_GLOBAL              1 (outline + NULL)
        # |               CALL                     0
        # |               STORE_FAST               5 (o)
        # |  89           LOAD_FAST_BORROW         3 (w)
        # |               LOAD_ATTR                3 (write_scene + NULL|self)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |               LOAD_FAST_BORROW         5 (o)
        # |               LOAD_ATTR                4 (scenes)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               CALL                     3
        # |               POP_TOP
        # |  90           LOAD_CONST               1 ('沈知微')
        # |               STORE_FAST_LOAD_FAST   100 (@py_assert0, c)
        # |               LOAD_ATTR                6 (calls)
        # |               LOAD_CONST               8 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |               LOAD_ATTR                8 (instruction)
        # |               STORE_FAST_LOAD_FAST   134 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 (('in',))
        # |               LOAD_FAST_BORROW         9 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              10 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.instruction\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py6')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_CONST               5 ('assert %(py8)s')
        # |               LOAD_CONST               6 ('py8')
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format9)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_prev_tail_truncated_and_placed_volatile(self, writer, sample_state):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  92            RESUME                   0
        # |  93            LOAD_FAST_BORROW         1 (writer)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   52 (w, c)
        # |  94            LOAD_GLOBAL              1 (outline + NULL)
        # |                CALL                     0
        # |                STORE_FAST               5 (o)
        # |  95            LOAD_FAST_BORROW         3 (w)
        # |                LOAD_ATTR                3 (write_scene + NULL|self)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |                LOAD_FAST_BORROW         5 (o)
        # |                LOAD_ATTR                4 (scenes)
        # |                LOAD_SMALL_INT           0
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              20 ('上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上上')
        # |                LOAD_CONST               1 (('prev_text',))
        # |                CALL_KW                  4
        # |                POP_TOP
        # |  96            LOAD_FAST_BORROW         4 (c)
        # |                LOAD_ATTR                6 (calls)
        # |                LOAD_CONST              21 (-1)
        # |                BINARY_OP               26 ([])
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST  103 (_, p)
        # |  97            LOAD_FAST_BORROW         7 (p)
        # |                LOAD_ATTR                8 (prev_tail)
        # |                STORE_FAST               8 (@py_assert2)
        # |                LOAD_GLOBAL             11 (len + NULL)
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   147 (@py_assert4, w)
        # |                LOAD_ATTR               12 (prev_tail_chars)
        # |                STORE_FAST_LOAD_FAST   169 (@py_assert8, @py_assert4)
        # |                LOAD_FAST_BORROW        10 (@py_assert8)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert6, @py_assert6)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       385 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              22 (('==',))
        # |                LOAD_FAST_BORROW        11 (@py_assert6)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              23 (('%(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s.prev_tail\n})\n} == %(py9)s\n{%(py9)s = %(py7)s.prev_tail_chars\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert4, @py_assert8)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               3 ('len')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (len)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (len)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               3 ('len')
        # |        L3:     LOAD_CONST               4 ('py1')
        # |                LOAD_CONST               5 ('p')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               5 ('p')
        # |        L6:     LOAD_CONST               6 ('py3')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py5')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_CONST               9 ('w')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (w)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (w)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               9 ('w')
        # |        L9:     LOAD_CONST              10 ('py9')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert8)
        # |                CALL                     1
        # |                BUILD_MAP                6
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format10)
        # |                LOAD_CONST              11 ('assert %(py11)s')
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_FAST_BORROW        12 (@py_format10)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format12)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_format12)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              13 (None)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  186 (@py_assert6, @py_assert8)
        # |  98            LOAD_FAST_BORROW         7 (p)
        # |                LOAD_ATTR                8 (prev_tail)
        # |                STORE_FAST_LOAD_FAST   231 (@py_assert1, p)
        # |                LOAD_ATTR               30 (system_core)
        # |                STORE_FAST_LOAD_FAST   247 (@py_assert5, p)
        # |                LOAD_ATTR               32 (bible)
        # |                STORE_FAST_LOAD_FAST   175 (@py_assert8, @py_assert5)
        # |                LOAD_FAST_BORROW        10 (@py_assert8)
        # |                BINARY_OP                0 (+)
        # |                STORE_FAST              16 (@py_assert10)
        # |                LOAD_FAST_BORROW         7 (p)
        # |                LOAD_ATTR               34 (volume)
        # |                STORE_FAST              17 (@py_assert12)
        # |                LOAD_FAST_BORROW        16 (@py_assert10)
        # |                LOAD_FAST_BORROW        17 (@py_assert12)
        # |                BINARY_OP                0 (+)
        # |                STORE_FAST              18 (@py_assert14)
        # |                LOAD_FAST_BORROW        14 (@py_assert1)
        # |                LOAD_FAST_BORROW        18 (@py_assert14)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST              19 (@py_assert3)
        # |                LOAD_FAST_BORROW        19 (@py_assert3)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       478 (to L23)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              24 (('not in',))
        # |                LOAD_FAST_BORROW        19 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              25 (('%(py2)s\n{%(py2)s = %(py0)s.prev_tail\n} not in ((%(py6)s\n{%(py6)s = %(py4)s.system_core\n} + %(py9)s\n{%(py9)s = %(py7)s.bible\n}) + %(py13)s\n{%(py13)s = %(py11)s.volume\n})',))
        # |                LOAD_FAST_BORROW        14 (@py_assert1)
        # |                LOAD_FAST_BORROW        18 (@py_assert14)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               5 ('p')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L12)
        # |                NOT_TAKEN
        # |       L11:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L13)
        # |       L12:     LOAD_CONST               5 ('p')
        # |       L13:     LOAD_CONST              14 ('py2')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        14 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py4')
        # |                LOAD_CONST               5 ('p')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L15)
        # |                NOT_TAKEN
        # |       L14:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L16)
        # |       L15:     LOAD_CONST               5 ('p')
        # |       L16:     LOAD_CONST              16 ('py6')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        15 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_CONST               5 ('p')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L17)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L18)
        # |                NOT_TAKEN
        # |       L17:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L19)
        # |       L18:     LOAD_CONST               5 ('p')
        # |       L19:     LOAD_CONST              10 ('py9')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_CONST               5 ('p')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L20)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L21)
        # |                NOT_TAKEN
        # |       L20:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L22)
        # |       L21:     LOAD_CONST               5 ('p')
        # |       L22:     LOAD_CONST              17 ('py13')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        17 (@py_assert12)
        # |                CALL                     1
        # |                BUILD_MAP                8
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              20 (@py_format15)
        # |                LOAD_CONST              18 ('assert %(py16)s')
        # |                LOAD_CONST              19 ('py16')
        # |                LOAD_FAST_BORROW        20 (@py_format15)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              21 (@py_format17)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        21 (@py_format17)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L23:     LOAD_CONST              13 (None)
        # |                COPY                     1
        # |                STORE_FAST              14 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST              19 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST              15 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST              16 (@py_assert10)
        # |                COPY                     1
        # |                STORE_FAST              17 (@py_assert12)
        # |                STORE_FAST              18 (@py_assert14)
        # |                LOAD_CONST              13 (None)
        # |                RETURN_VALUE

    def test_intimacy_level_instruction(self, writer, sample_state):
        'L2'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 100           RESUME                   0
        # | 101           LOAD_FAST_BORROW         1 (writer)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   52 (w, c)
        # | 102           LOAD_GLOBAL              1 (outline + NULL)
        # |               LOAD_GLOBAL              3 (scene + NULL)
        # |               LOAD_CONST               0 ('L2')
        # |               LOAD_CONST               1 (('intimacy_level',))
        # |               CALL_KW                  1
        # | 103           LOAD_GLOBAL              3 (scene + NULL)
        # |               LOAD_CONST               2 ('ch012_s2')
        # |               LOAD_CONST               3 ('a')
        # |               LOAD_CONST               4 ('b')
        # |               LOAD_CONST               5 (('entry_emotion', 'exit_emotion'))
        # |               CALL_KW                  3
        # | 102           BUILD_LIST               2
        # |               LOAD_CONST               6 (('scenes',))
        # |               CALL_KW                  1
        # |               STORE_FAST               5 (o)
        # | 104           LOAD_FAST_BORROW         3 (w)
        # |               LOAD_ATTR                5 (write_scene + NULL|self)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |               LOAD_FAST_BORROW         5 (o)
        # |               LOAD_ATTR                6 (scenes)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               CALL                     3
        # |               POP_TOP
        # | 105           BUILD_LIST               0
        # |               STORE_FAST               6 (@py_assert1)
        # |               LOAD_CONST               0 ('L2')
        # |               STORE_FAST_LOAD_FAST   116 (@py_assert2, c)
        # |               LOAD_ATTR                8 (calls)
        # |               LOAD_CONST              21 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert5, @py_assert5)
        # |               LOAD_ATTR               10 (instruction)
        # |               STORE_FAST_LOAD_FAST   151 (@py_assert7, @py_assert2)
        # |               LOAD_FAST_BORROW         9 (@py_assert7)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert4, @py_assert4)
        # |               STORE_FAST_LOAD_FAST   186 (@py_assert0, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       44 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_CONST               7 ('收住')
        # |               STORE_FAST_LOAD_FAST   196 (@py_assert12, c)
        # |               LOAD_ATTR                8 (calls)
        # |               LOAD_CONST              21 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   221 (@py_assert15, @py_assert15)
        # |               LOAD_ATTR               10 (instruction)
        # |               STORE_FAST_LOAD_FAST   236 (@py_assert17, @py_assert12)
        # |               LOAD_FAST_BORROW        14 (@py_assert17)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   255 (@py_assert14, @py_assert14)
        # |               STORE_FAST              11 (@py_assert0)
        # |       L1:     LOAD_FAST_BORROW        11 (@py_assert0)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       338 (to L3)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              22 (('in',))
        # |               LOAD_FAST_BORROW        10 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              23 (('%(py3)s in %(py8)s\n{%(py8)s = %(py6)s.instruction\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 121 (@py_assert2, @py_assert7)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               8 ('py3')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py6')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py8')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert7)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              16 (@py_format9)
        # |               LOAD_CONST              11 ('%(py10)s')
        # |               LOAD_CONST              12 ('py10')
        # |               LOAD_FAST_BORROW        16 (@py_format9)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              17 (@py_format11)
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               LOAD_ATTR               19 (append + NULL|self)
        # |               LOAD_FAST_BORROW        17 (@py_format11)
        # |               CALL                     1
        # |               POP_TOP
        # |               LOAD_FAST_BORROW        10 (@py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE      130 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              22 (('in',))
        # |               LOAD_FAST_CHECK         15 (@py_assert14)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              24 (('%(py13)s in %(py18)s\n{%(py18)s = %(py16)s.instruction\n}',))
        # |               LOAD_FAST_CHECK         12 (@py_assert12)
        # |               LOAD_FAST_CHECK         14 (@py_assert17)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              13 ('py13')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        12 (@py_assert12)
        # |               CALL                     1
        # |               LOAD_CONST              14 ('py16')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_CHECK         13 (@py_assert15)
        # |               CALL                     1
        # |               LOAD_CONST              15 ('py18')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        14 (@py_assert17)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              18 (@py_format19)
        # |               LOAD_CONST              16 ('%(py20)s')
        # |               LOAD_CONST              17 ('py20')
        # |               LOAD_FAST_BORROW        18 (@py_format19)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              19 (@py_format21)
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               LOAD_ATTR               19 (append + NULL|self)
        # |               LOAD_FAST_BORROW        19 (@py_format21)
        # |               CALL                     1
        # |               POP_TOP
        # |       L2:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_boolop)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BUILD_MAP                0
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              20 (@py_format22)
        # |               LOAD_CONST              18 ('assert %(py23)s')
        # |               LOAD_CONST              19 ('py23')
        # |               LOAD_FAST_BORROW        20 (@py_format22)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              21 (@py_format24)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        21 (@py_format24)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L3:     LOAD_CONST              20 (None)
        # |               COPY                     1
        # |               STORE_FAST              11 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST              10 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST              12 (@py_assert12)
        # |               COPY                     1
        # |               STORE_FAST              15 (@py_assert14)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  222 (@py_assert15, @py_assert17)
        # |               LOAD_CONST              20 (None)
        # |               RETURN_VALUE

    def test_must_not_surfaced(self, writer, sample_state):
        '提到那把伞的来历'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 107           RESUME                   0
        # | 108           LOAD_FAST_BORROW         1 (writer)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   52 (w, c)
        # | 109           LOAD_GLOBAL              1 (outline + NULL)
        # |               LOAD_GLOBAL              3 (scene + NULL)
        # |               LOAD_CONST               0 ('提到那把伞的来历')
        # |               BUILD_LIST               1
        # |               LOAD_CONST               1 (('must_not',))
        # |               CALL_KW                  1
        # | 110           LOAD_GLOBAL              3 (scene + NULL)
        # |               LOAD_CONST               2 ('ch012_s2')
        # |               LOAD_CONST               3 ('a')
        # |               LOAD_CONST               4 ('b')
        # |               LOAD_CONST               5 (('entry_emotion', 'exit_emotion'))
        # |               CALL_KW                  3
        # | 109           BUILD_LIST               2
        # |               LOAD_CONST               6 (('scenes',))
        # |               CALL_KW                  1
        # |               STORE_FAST               5 (o)
        # | 111           LOAD_FAST_BORROW         3 (w)
        # |               LOAD_ATTR                5 (write_scene + NULL|self)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |               LOAD_FAST_BORROW         5 (o)
        # |               LOAD_ATTR                6 (scenes)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               CALL                     3
        # |               POP_TOP
        # | 112           LOAD_CONST               7 ('禁止出现')
        # |               STORE_FAST_LOAD_FAST   100 (@py_assert0, c)
        # |               LOAD_ATTR                8 (calls)
        # |               LOAD_CONST              14 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |               LOAD_ATTR               10 (instruction)
        # |               STORE_FAST_LOAD_FAST   134 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('in',))
        # |               LOAD_FAST_BORROW         9 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.instruction\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               8 ('py1')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py6')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_CONST              11 ('assert %(py8)s')
        # |               LOAD_CONST              12 ('py8')
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format9)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert3, @py_assert5)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE


class TestCachePrefix:
    'TestCachePrefix'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 115           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestCachePrefix')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         115
    # |               STORE_NAME               3 (__firstlineno__)
    # | 116           LOAD_CONST               1 (<code object test_prefix_constant_across_scenes_in_a_chapter at 0x755f222300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 116>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_prefix_constant_across_scenes_in_a_chapter)
    # | 124           LOAD_CONST               2 (<code object test_bible_not_trimmed_per_scene at 0x755ee18c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 124>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_bible_not_trimmed_per_scene)
    # | 131           LOAD_CONST               3 (<code object test_rag_goes_volatile at 0x755f0af800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 131>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_rag_goes_volatile)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_prefix_constant_across_scenes_in_a_chapter at 0x755f222300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 116>:
    # |  116            RESUME                   0
    # |  118            LOAD_FAST_BORROW         1 (writer)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST   52 (w, c)
    # |  119            LOAD_GLOBAL              1 (outline + NULL)
    # |                 CALL                     0
    # |                 STORE_FAST               5 (o)
    # |  120            LOAD_FAST_BORROW         3 (w)
    # |                 LOAD_ATTR                3 (write_chapter_scenes + NULL|self)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |                 CALL                     2
    # |                 POP_TOP
    # |  121            LOAD_FAST_BORROW         4 (c)
    # |                 LOAD_ATTR                4 (calls)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      6 (_)
    # |                 LOAD_FAST_AND_CLEAR      7 (p)
    # |                 SWAP                     3
    # |         L1:     BUILD_SET                0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                21 (to L3)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST  103 (_, p)
    # |                 LOAD_FAST_BORROW         7 (p)
    # |                 LOAD_ATTR                7 (prefix_fingerprint + NULL|self)
    # |                 CALL                     0
    # |                 SET_ADD                  2
    # |                 JUMP_BACKWARD           23 (to L2)
    # |         L3:     END_FOR
    # |                 POP_ITER
    # |         L4:     STORE_FAST               8 (prints)
    # |                 STORE_FAST               6 (_)
    # |                 STORE_FAST               7 (p)
    # |  122            LOAD_GLOBAL              9 (len + NULL)
    # |                 LOAD_FAST_BORROW         8 (prints)
    # |                 CALL                     1
    # |                 STORE_FAST               9 (@py_assert2)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST_LOAD_FAST   169 (@py_assert5, @py_assert2)
    # |                 LOAD_FAST_BORROW        10 (@py_assert5)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   187 (@py_assert4, @py_assert4)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       315 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              11 (('==',))
    # |                 LOAD_FAST_BORROW        11 (@py_assert4)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              12 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert2, @py_assert5)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py0')
    # |                 LOAD_CONST               2 ('len')
    # |                 LOAD_GLOBAL             14 (@py_builtins)
    # |                 LOAD_ATTR               16 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L5)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              8 (len)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L6)
    # |                 NOT_TAKEN
    # |         L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              8 (len)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L7)
    # |         L6:     LOAD_CONST               2 ('len')
    # |         L7:     LOAD_CONST               3 ('py1')
    # |                 LOAD_CONST               4 ('prints')
    # |                 LOAD_GLOBAL             14 (@py_builtins)
    # |                 LOAD_ATTR               16 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (prints)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (prints)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST               4 ('prints')
    # |        L10:     LOAD_CONST               5 ('py3')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert2)
    # |                 CALL                     1
    # |                 LOAD_CONST               6 ('py6')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert5)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format7)
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST               7 ('场景间前缀发生变化：')
    # |                 LOAD_FAST_BORROW         8 (prints)
    # |                 FORMAT_SIMPLE
    # |                 BUILD_STRING             2
    # |                 CALL                     1
    # |                 LOAD_CONST               8 ('\n>assert %(py8)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST               9 ('py8')
    # |                 LOAD_FAST_BORROW        12 (@py_format7)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format9)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST              10 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               9 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  186 (@py_assert4, @py_assert5)
    # |                 LOAD_CONST              10 (None)
    # |                 RETURN_VALUE
    # |   --   L12:     SWAP                     2
    # |                 POP_TOP
    # |  121            SWAP                     3
    # |                 STORE_FAST               7 (p)
    # |                 STORE_FAST               6 (_)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L12 [3]
    # | Disassembly of <code object test_bible_not_trimmed_per_scene at 0x755ee18c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 124>:
    # | 124           RESUME                   0
    # | 126           LOAD_FAST_BORROW         1 (writer)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   52 (w, c)
    # | 127           LOAD_GLOBAL              1 (outline + NULL)
    # |               CALL                     0
    # |               STORE_FAST               5 (o)
    # | 128           LOAD_FAST_BORROW         3 (w)
    # |               LOAD_ATTR                3 (write_chapter_scenes + NULL|self)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |               CALL                     2
    # |               POP_TOP
    # | 129           LOAD_CONST               1 ('陆时予')
    # |               STORE_FAST_LOAD_FAST   100 (@py_assert0, c)
    # |               LOAD_ATTR                4 (calls)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |               LOAD_ATTR                6 (bible)
    # |               STORE_FAST_LOAD_FAST   134 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 (('in',))
    # |               LOAD_FAST_BORROW         9 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               9 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.bible\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_CONST               5 ('assert %(py8)s')
    # |               LOAD_CONST               6 ('py8')
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format9)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_rag_goes_volatile at 0x755f0af800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 131>:
    # | 131            RESUME                   0
    # | 132            LOAD_FAST_BORROW         1 (writer)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   52 (w, c)
    # | 133            LOAD_GLOBAL              1 (outline + NULL)
    # |                CALL                     0
    # |                STORE_FAST               5 (o)
    # | 134            LOAD_FAST_BORROW         3 (w)
    # |                LOAD_ATTR                3 (write_scene + NULL|self)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
    # |                LOAD_FAST_BORROW         5 (o)
    # |                LOAD_ATTR                4 (scenes)
    # |                LOAD_SMALL_INT           0
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST               1 ('某段风格参照')
    # |                BUILD_LIST               1
    # |                LOAD_CONST               2 (('rag_snippets',))
    # |                CALL_KW                  4
    # |                POP_TOP
    # | 135            LOAD_FAST_BORROW         4 (c)
    # |                LOAD_ATTR                6 (calls)
    # |                LOAD_CONST              18 (-1)
    # |                BINARY_OP               26 ([])
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST  103 (_, p)
    # | 136            LOAD_FAST_BORROW         7 (p)
    # |                LOAD_ATTR                8 (rag_snippets)
    # |                STORE_FAST               8 (@py_assert1)
    # |                LOAD_CONST               1 ('某段风格参照')
    # |                BUILD_LIST               1
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py2)s\n{%(py2)s = %(py0)s.rag_snippets\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('p')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('p')
    # |        L3:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format6)
    # |                LOAD_CONST               7 ('assert %(py7)s')
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_FAST_BORROW        11 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format8)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  169 (@py_assert3, @py_assert4)
    # | 137            LOAD_CONST               1 ('某段风格参照')
    # |                STORE_FAST_LOAD_FAST   215 (@py_assert0, p)
    # |                LOAD_ATTR               26 (system_core)
    # |                STORE_FAST_LOAD_FAST   151 (@py_assert4, p)
    # |                LOAD_ATTR               28 (bible)
    # |                STORE_FAST_LOAD_FAST   233 (@py_assert7, @py_assert4)
    # |                LOAD_FAST_BORROW        14 (@py_assert7)
    # |                BINARY_OP                0 (+)
    # |                STORE_FAST_LOAD_FAST   247 (@py_assert9, p)
    # |                LOAD_ATTR               30 (volume)
    # |                STORE_FAST              16 (@py_assert11)
    # |                LOAD_FAST_BORROW        15 (@py_assert9)
    # |                LOAD_FAST_BORROW        16 (@py_assert11)
    # |                BINARY_OP                0 (+)
    # |                STORE_FAST              17 (@py_assert13)
    # |                LOAD_FAST_BORROW        13 (@py_assert0)
    # |                LOAD_FAST_BORROW        17 (@py_assert13)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST              18 (@py_assert2)
    # |                LOAD_FAST_BORROW        18 (@py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       400 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              21 (('not in',))
    # |                LOAD_FAST_BORROW        18 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              22 (('%(py1)s not in ((%(py5)s\n{%(py5)s = %(py3)s.system_core\n} + %(py8)s\n{%(py8)s = %(py6)s.bible\n}) + %(py12)s\n{%(py12)s = %(py10)s.volume\n})',))
    # |                LOAD_FAST_BORROW        13 (@py_assert0)
    # |                LOAD_FAST_BORROW        17 (@py_assert13)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              10 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py3')
    # |                LOAD_CONST               4 ('p')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               4 ('p')
    # |        L7:     LOAD_CONST               6 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py6')
    # |                LOAD_CONST               4 ('p')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               4 ('p')
    # |       L10:     LOAD_CONST              13 ('py8')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        14 (@py_assert7)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py10')
    # |                LOAD_CONST               4 ('p')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L12)
    # |                NOT_TAKEN
    # |       L11:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L13)
    # |       L12:     LOAD_CONST               4 ('p')
    # |       L13:     LOAD_CONST              15 ('py12')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        16 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              19 (@py_format14)
    # |                LOAD_CONST              16 ('assert %(py15)s')
    # |                LOAD_CONST              17 ('py15')
    # |                LOAD_FAST_BORROW        19 (@py_format14)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              20 (@py_format16)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        20 (@py_format16)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L14:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST              18 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST              14 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST              15 (@py_assert9)
    # |                COPY                     1
    # |                STORE_FAST              16 (@py_assert11)
    # |                STORE_FAST              17 (@py_assert13)
    # |                LOAD_CONST               9 (None)
    # |                RETURN_VALUE

    def test_prefix_constant_across_scenes_in_a_chapter(self, writer, sample_state):
        '同一章的各场景必须共享缓存前缀 —— 这是分场景写不额外烧钱的前提。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  116            RESUME                   0
        # |  118            LOAD_FAST_BORROW         1 (writer)
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST_STORE_FAST   52 (w, c)
        # |  119            LOAD_GLOBAL              1 (outline + NULL)
        # |                 CALL                     0
        # |                 STORE_FAST               5 (o)
        # |  120            LOAD_FAST_BORROW         3 (w)
        # |                 LOAD_ATTR                3 (write_chapter_scenes + NULL|self)
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |                 CALL                     2
        # |                 POP_TOP
        # |  121            LOAD_FAST_BORROW         4 (c)
        # |                 LOAD_ATTR                4 (calls)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      6 (_)
        # |                 LOAD_FAST_AND_CLEAR      7 (p)
        # |                 SWAP                     3
        # |         L1:     BUILD_SET                0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                21 (to L3)
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST_STORE_FAST  103 (_, p)
        # |                 LOAD_FAST_BORROW         7 (p)
        # |                 LOAD_ATTR                7 (prefix_fingerprint + NULL|self)
        # |                 CALL                     0
        # |                 SET_ADD                  2
        # |                 JUMP_BACKWARD           23 (to L2)
        # |         L3:     END_FOR
        # |                 POP_ITER
        # |         L4:     STORE_FAST               8 (prints)
        # |                 STORE_FAST               6 (_)
        # |                 STORE_FAST               7 (p)
        # |  122            LOAD_GLOBAL              9 (len + NULL)
        # |                 LOAD_FAST_BORROW         8 (prints)
        # |                 CALL                     1
        # |                 STORE_FAST               9 (@py_assert2)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST_LOAD_FAST   169 (@py_assert5, @py_assert2)
        # |                 LOAD_FAST_BORROW        10 (@py_assert5)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   187 (@py_assert4, @py_assert4)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       315 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              11 (('==',))
        # |                 LOAD_FAST_BORROW        11 (@py_assert4)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              12 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert2, @py_assert5)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py0')
        # |                 LOAD_CONST               2 ('len')
        # |                 LOAD_GLOBAL             14 (@py_builtins)
        # |                 LOAD_ATTR               16 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L5)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              8 (len)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L6)
        # |                 NOT_TAKEN
        # |         L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              8 (len)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L7)
        # |         L6:     LOAD_CONST               2 ('len')
        # |         L7:     LOAD_CONST               3 ('py1')
        # |                 LOAD_CONST               4 ('prints')
        # |                 LOAD_GLOBAL             14 (@py_builtins)
        # |                 LOAD_ATTR               16 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (prints)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (prints)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST               4 ('prints')
        # |        L10:     LOAD_CONST               5 ('py3')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert2)
        # |                 CALL                     1
        # |                 LOAD_CONST               6 ('py6')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert5)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format7)
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST               7 ('场景间前缀发生变化：')
        # |                 LOAD_FAST_BORROW         8 (prints)
        # |                 FORMAT_SIMPLE
        # |                 BUILD_STRING             2
        # |                 CALL                     1
        # |                 LOAD_CONST               8 ('\n>assert %(py8)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST               9 ('py8')
        # |                 LOAD_FAST_BORROW        12 (@py_format7)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format9)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST              10 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               9 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  186 (@py_assert4, @py_assert5)
        # |                 LOAD_CONST              10 (None)
        # |                 RETURN_VALUE
        # |   --   L12:     SWAP                     2
        # |                 POP_TOP
        # |  121            SWAP                     3
        # |                 STORE_FAST               7 (p)
        # |                 STORE_FAST               6 (_)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L12 [3]

    def test_bible_not_trimmed_per_scene(self, writer, sample_state):
        '按出场人物裁剪 bible 会击穿前缀，省的 token 不值这个代价。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 124           RESUME                   0
        # | 126           LOAD_FAST_BORROW         1 (writer)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   52 (w, c)
        # | 127           LOAD_GLOBAL              1 (outline + NULL)
        # |               CALL                     0
        # |               STORE_FAST               5 (o)
        # | 128           LOAD_FAST_BORROW         3 (w)
        # |               LOAD_ATTR                3 (write_chapter_scenes + NULL|self)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |               CALL                     2
        # |               POP_TOP
        # | 129           LOAD_CONST               1 ('陆时予')
        # |               STORE_FAST_LOAD_FAST   100 (@py_assert0, c)
        # |               LOAD_ATTR                4 (calls)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |               LOAD_ATTR                6 (bible)
        # |               STORE_FAST_LOAD_FAST   134 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 (('in',))
        # |               LOAD_FAST_BORROW         9 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               9 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.bible\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_CONST               5 ('assert %(py8)s')
        # |               LOAD_CONST               6 ('py8')
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format9)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_rag_goes_volatile(self, writer, sample_state):
        '某段风格参照'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 131            RESUME                   0
        # | 132            LOAD_FAST_BORROW         1 (writer)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   52 (w, c)
        # | 133            LOAD_GLOBAL              1 (outline + NULL)
        # |                CALL                     0
        # |                STORE_FAST               5 (o)
        # | 134            LOAD_FAST_BORROW         3 (w)
        # |                LOAD_ATTR                3 (write_scene + NULL|self)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 37 (sample_state, o)
        # |                LOAD_FAST_BORROW         5 (o)
        # |                LOAD_ATTR                4 (scenes)
        # |                LOAD_SMALL_INT           0
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST               1 ('某段风格参照')
        # |                BUILD_LIST               1
        # |                LOAD_CONST               2 (('rag_snippets',))
        # |                CALL_KW                  4
        # |                POP_TOP
        # | 135            LOAD_FAST_BORROW         4 (c)
        # |                LOAD_ATTR                6 (calls)
        # |                LOAD_CONST              18 (-1)
        # |                BINARY_OP               26 ([])
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST  103 (_, p)
        # | 136            LOAD_FAST_BORROW         7 (p)
        # |                LOAD_ATTR                8 (rag_snippets)
        # |                STORE_FAST               8 (@py_assert1)
        # |                LOAD_CONST               1 ('某段风格参照')
        # |                BUILD_LIST               1
        # |                STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('==',))
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py2)s\n{%(py2)s = %(py0)s.rag_snippets\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('p')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('p')
        # |        L3:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format6)
        # |                LOAD_CONST               7 ('assert %(py7)s')
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_FAST_BORROW        11 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format8)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  169 (@py_assert3, @py_assert4)
        # | 137            LOAD_CONST               1 ('某段风格参照')
        # |                STORE_FAST_LOAD_FAST   215 (@py_assert0, p)
        # |                LOAD_ATTR               26 (system_core)
        # |                STORE_FAST_LOAD_FAST   151 (@py_assert4, p)
        # |                LOAD_ATTR               28 (bible)
        # |                STORE_FAST_LOAD_FAST   233 (@py_assert7, @py_assert4)
        # |                LOAD_FAST_BORROW        14 (@py_assert7)
        # |                BINARY_OP                0 (+)
        # |                STORE_FAST_LOAD_FAST   247 (@py_assert9, p)
        # |                LOAD_ATTR               30 (volume)
        # |                STORE_FAST              16 (@py_assert11)
        # |                LOAD_FAST_BORROW        15 (@py_assert9)
        # |                LOAD_FAST_BORROW        16 (@py_assert11)
        # |                BINARY_OP                0 (+)
        # |                STORE_FAST              17 (@py_assert13)
        # |                LOAD_FAST_BORROW        13 (@py_assert0)
        # |                LOAD_FAST_BORROW        17 (@py_assert13)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST              18 (@py_assert2)
        # |                LOAD_FAST_BORROW        18 (@py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       400 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              21 (('not in',))
        # |                LOAD_FAST_BORROW        18 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              22 (('%(py1)s not in ((%(py5)s\n{%(py5)s = %(py3)s.system_core\n} + %(py8)s\n{%(py8)s = %(py6)s.bible\n}) + %(py12)s\n{%(py12)s = %(py10)s.volume\n})',))
        # |                LOAD_FAST_BORROW        13 (@py_assert0)
        # |                LOAD_FAST_BORROW        17 (@py_assert13)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              10 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py3')
        # |                LOAD_CONST               4 ('p')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               4 ('p')
        # |        L7:     LOAD_CONST               6 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py6')
        # |                LOAD_CONST               4 ('p')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               4 ('p')
        # |       L10:     LOAD_CONST              13 ('py8')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        14 (@py_assert7)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py10')
        # |                LOAD_CONST               4 ('p')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L12)
        # |                NOT_TAKEN
        # |       L11:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L13)
        # |       L12:     LOAD_CONST               4 ('p')
        # |       L13:     LOAD_CONST              15 ('py12')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        16 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              19 (@py_format14)
        # |                LOAD_CONST              16 ('assert %(py15)s')
        # |                LOAD_CONST              17 ('py15')
        # |                LOAD_FAST_BORROW        19 (@py_format14)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              20 (@py_format16)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        20 (@py_format16)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L14:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST              13 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST              18 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST              14 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST              15 (@py_assert9)
        # |                COPY                     1
        # |                STORE_FAST              16 (@py_assert11)
        # |                STORE_FAST              17 (@py_assert13)
        # |                LOAD_CONST               9 (None)
        # |                RETURN_VALUE


class TestSceneSequencing:
    'TestSceneSequencing'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 140           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestSceneSequencing')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         140
    # |               STORE_NAME               3 (__firstlineno__)
    # | 141           LOAD_CONST               1 (<code object test_writes_every_scene_in_order at 0x755ee2a400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 141>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_writes_every_scene_in_order)
    # | 147           LOAD_CONST               2 (<code object test_each_scene_sees_previous_tail at 0x755f222d00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 147>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_each_scene_sees_previous_tail)
    # | 153           LOAD_CONST               3 (<code object test_uses_writer_role at 0x755ee4c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 153>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_uses_writer_role)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_writes_every_scene_in_order at 0x755ee2a400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 141>:
    # |  141            RESUME                   0
    # |  142            LOAD_FAST_BORROW         1 (writer)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST   52 (w, c)
    # |  143            LOAD_FAST_BORROW         3 (w)
    # |                 LOAD_ATTR                1 (write_chapter_scenes + NULL|self)
    # |                 LOAD_FAST_BORROW         2 (sample_state)
    # |                 LOAD_GLOBAL              3 (outline + NULL)
    # |                 CALL                     0
    # |                 CALL                     2
    # |                 STORE_FAST               5 (texts)
    # |  144            LOAD_GLOBAL              5 (len + NULL)
    # |                 LOAD_FAST_BORROW         5 (texts)
    # |                 CALL                     1
    # |                 STORE_FAST               6 (@py_assert2)
    # |                 LOAD_SMALL_INT           2
    # |                 STORE_FAST_LOAD_FAST   118 (@py_assert5, @py_assert2)
    # |                 LOAD_FAST_BORROW         7 (@py_assert5)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       285 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR                8 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              15 (('==',))
    # |                 LOAD_FAST_BORROW         8 (@py_assert4)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              16 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert2, @py_assert5)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py0')
    # |                 LOAD_CONST               2 ('len')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L1)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              4 (len)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L2)
    # |                 NOT_TAKEN
    # |         L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              4 (len)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L3)
    # |         L2:     LOAD_CONST               2 ('len')
    # |         L3:     LOAD_CONST               3 ('py1')
    # |                 LOAD_CONST               4 ('texts')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (texts)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (texts)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               4 ('texts')
    # |         L6:     LOAD_CONST               5 ('py3')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert2)
    # |                 CALL                     1
    # |                 LOAD_CONST               6 ('py6')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert5)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format7)
    # |                 LOAD_CONST               7 ('assert %(py8)s')
    # |                 LOAD_CONST               8 ('py8')
    # |                 LOAD_FAST_BORROW         9 (@py_format7)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              10 (@py_format9)
    # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST               9 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               6 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  135 (@py_assert4, @py_assert5)
    # |  145            LOAD_FAST_BORROW         4 (c)
    # |                 LOAD_ATTR               22 (calls)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR     11 (_)
    # |                 LOAD_FAST_AND_CLEAR     12 (p)
    # |                 SWAP                     3
    # |         L8:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L9:     FOR_ITER                39 (to L10)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST  188 (_, p)
    # |                 LOAD_FAST_BORROW        12 (p)
    # |                 LOAD_ATTR               24 (instruction)
    # |                 LOAD_ATTR               27 (split + NULL|self)
    # |                 LOAD_CONST              10 ('**')
    # |                 CALL                     1
    # |                 LOAD_SMALL_INT           1
    # |                 BINARY_OP               26 ([])
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           41 (to L9)
    # |        L10:     END_FOR
    # |                 POP_ITER
    # |        L11:     STORE_FAST              13 (@py_assert0)
    # |                 STORE_FAST              11 (_)
    # |                 STORE_FAST              12 (p)
    # |                 LOAD_CONST              11 ('ch012_s1')
    # |                 LOAD_CONST              12 ('ch012_s2')
    # |                 BUILD_LIST               2
    # |                 STORE_FAST_LOAD_FAST   237 (@py_assert3, @py_assert0)
    # |                 LOAD_FAST_BORROW        14 (@py_assert3)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       121 (to L12)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR                8 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              15 (('==',))
    # |                 LOAD_FAST_BORROW         6 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              17 (('%(py1)s == %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 222 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               3 ('py1')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST              13 ('py4')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        14 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              15 (@py_format5)
    # |                 LOAD_CONST              14 ('assert %(py6)s')
    # |                 LOAD_CONST               6 ('py6')
    # |                 LOAD_FAST_BORROW        15 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format7)
    # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L12:     LOAD_CONST               9 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              13 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  110 (@py_assert2, @py_assert3)
    # |                 LOAD_CONST               9 (None)
    # |                 RETURN_VALUE
    # |   --   L13:     SWAP                     2
    # |                 POP_TOP
    # |  145            SWAP                     3
    # |                 STORE_FAST              12 (p)
    # |                 STORE_FAST              11 (_)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L8 to L11 -> L13 [3]
    # | Disassembly of <code object test_each_scene_sees_previous_tail at 0x755f222d00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 147>:
    # | 147           RESUME                   0
    # | 148           LOAD_FAST_BORROW         1 (writer)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   52 (w, c)
    # | 149           LOAD_FAST_BORROW         3 (w)
    # |               LOAD_ATTR                1 (write_chapter_scenes + NULL|self)
    # |               LOAD_FAST_BORROW         2 (sample_state)
    # |               LOAD_GLOBAL              3 (outline + NULL)
    # |               CALL                     0
    # |               CALL                     2
    # |               POP_TOP
    # | 150           LOAD_FAST_BORROW         4 (c)
    # |               LOAD_ATTR                4 (calls)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
    # |               LOAD_ATTR                6 (prev_tail)
    # |               STORE_FAST               6 (@py_assert2)
    # |               LOAD_CONST               1 ('')
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert5, @py_assert2)
    # |               LOAD_FAST_BORROW         7 (@py_assert5)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 (('==',))
    # |               LOAD_FAST_BORROW         8 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               9 (('%(py3)s\n{%(py3)s = %(py1)s.prev_tail\n} == %(py6)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert2, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format7)
    # |               LOAD_CONST               5 ('assert %(py8)s')
    # |               LOAD_CONST               6 ('py8')
    # |               LOAD_FAST_BORROW         9 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format9)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert4, @py_assert5)
    # | 151           LOAD_FAST_BORROW         4 (c)
    # |               LOAD_ATTR                4 (calls)
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
    # |               LOAD_ATTR                6 (prev_tail)
    # |               STORE_FAST               6 (@py_assert2)
    # |               LOAD_CONST               1 ('')
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert5, @py_assert2)
    # |               LOAD_FAST_BORROW         7 (@py_assert5)
    # |               COMPARE_OP             103 (!=)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('!=',))
    # |               LOAD_FAST_BORROW         8 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py3)s\n{%(py3)s = %(py1)s.prev_tail\n} != %(py6)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert2, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format7)
    # |               LOAD_CONST               5 ('assert %(py8)s')
    # |               LOAD_CONST               6 ('py8')
    # |               LOAD_FAST_BORROW         9 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format9)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert4, @py_assert5)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_uses_writer_role at 0x755ee4c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 153>:
    # | 153           RESUME                   0
    # | 154           LOAD_FAST_BORROW         1 (writer)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   52 (w, c)
    # | 155           LOAD_FAST_BORROW         3 (w)
    # |               LOAD_ATTR                1 (write_scene + NULL|self)
    # |               LOAD_FAST_BORROW         2 (sample_state)
    # |               LOAD_GLOBAL              3 (outline + NULL)
    # |               CALL                     0
    # |               LOAD_GLOBAL              3 (outline + NULL)
    # |               CALL                     0
    # |               LOAD_ATTR                4 (scenes)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               CALL                     3
    # |               POP_TOP
    # | 156           LOAD_FAST_BORROW         4 (c)
    # |               LOAD_ATTR                6 (calls)
    # |               LOAD_CONST               7 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               5 (@py_assert0)
    # |               LOAD_CONST               1 ('writer')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         6 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 (('==',))
    # |               LOAD_FAST_BORROW         7 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               9 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format5)
    # |               LOAD_CONST               4 ('assert %(py6)s')
    # |               LOAD_CONST               5 ('py6')
    # |               LOAD_FAST_BORROW         8 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format7)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  118 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE

    def test_writes_every_scene_in_order(self, writer, sample_state):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  141            RESUME                   0
        # |  142            LOAD_FAST_BORROW         1 (writer)
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST_STORE_FAST   52 (w, c)
        # |  143            LOAD_FAST_BORROW         3 (w)
        # |                 LOAD_ATTR                1 (write_chapter_scenes + NULL|self)
        # |                 LOAD_FAST_BORROW         2 (sample_state)
        # |                 LOAD_GLOBAL              3 (outline + NULL)
        # |                 CALL                     0
        # |                 CALL                     2
        # |                 STORE_FAST               5 (texts)
        # |  144            LOAD_GLOBAL              5 (len + NULL)
        # |                 LOAD_FAST_BORROW         5 (texts)
        # |                 CALL                     1
        # |                 STORE_FAST               6 (@py_assert2)
        # |                 LOAD_SMALL_INT           2
        # |                 STORE_FAST_LOAD_FAST   118 (@py_assert5, @py_assert2)
        # |                 LOAD_FAST_BORROW         7 (@py_assert5)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       285 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR                8 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              15 (('==',))
        # |                 LOAD_FAST_BORROW         8 (@py_assert4)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              16 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert2, @py_assert5)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py0')
        # |                 LOAD_CONST               2 ('len')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L1)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              4 (len)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L2)
        # |                 NOT_TAKEN
        # |         L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              4 (len)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L3)
        # |         L2:     LOAD_CONST               2 ('len')
        # |         L3:     LOAD_CONST               3 ('py1')
        # |                 LOAD_CONST               4 ('texts')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (texts)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (texts)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               4 ('texts')
        # |         L6:     LOAD_CONST               5 ('py3')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert2)
        # |                 CALL                     1
        # |                 LOAD_CONST               6 ('py6')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert5)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format7)
        # |                 LOAD_CONST               7 ('assert %(py8)s')
        # |                 LOAD_CONST               8 ('py8')
        # |                 LOAD_FAST_BORROW         9 (@py_format7)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              10 (@py_format9)
        # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST               9 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               6 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  135 (@py_assert4, @py_assert5)
        # |  145            LOAD_FAST_BORROW         4 (c)
        # |                 LOAD_ATTR               22 (calls)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR     11 (_)
        # |                 LOAD_FAST_AND_CLEAR     12 (p)
        # |                 SWAP                     3
        # |         L8:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L9:     FOR_ITER                39 (to L10)
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST_STORE_FAST  188 (_, p)
        # |                 LOAD_FAST_BORROW        12 (p)
        # |                 LOAD_ATTR               24 (instruction)
        # |                 LOAD_ATTR               27 (split + NULL|self)
        # |                 LOAD_CONST              10 ('**')
        # |                 CALL                     1
        # |                 LOAD_SMALL_INT           1
        # |                 BINARY_OP               26 ([])
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           41 (to L9)
        # |        L10:     END_FOR
        # |                 POP_ITER
        # |        L11:     STORE_FAST              13 (@py_assert0)
        # |                 STORE_FAST              11 (_)
        # |                 STORE_FAST              12 (p)
        # |                 LOAD_CONST              11 ('ch012_s1')
        # |                 LOAD_CONST              12 ('ch012_s2')
        # |                 BUILD_LIST               2
        # |                 STORE_FAST_LOAD_FAST   237 (@py_assert3, @py_assert0)
        # |                 LOAD_FAST_BORROW        14 (@py_assert3)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       121 (to L12)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR                8 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              15 (('==',))
        # |                 LOAD_FAST_BORROW         6 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              17 (('%(py1)s == %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 222 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               3 ('py1')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST              13 ('py4')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        14 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              15 (@py_format5)
        # |                 LOAD_CONST              14 ('assert %(py6)s')
        # |                 LOAD_CONST               6 ('py6')
        # |                 LOAD_FAST_BORROW        15 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format7)
        # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L12:     LOAD_CONST               9 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              13 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  110 (@py_assert2, @py_assert3)
        # |                 LOAD_CONST               9 (None)
        # |                 RETURN_VALUE
        # |   --   L13:     SWAP                     2
        # |                 POP_TOP
        # |  145            SWAP                     3
        # |                 STORE_FAST              12 (p)
        # |                 STORE_FAST              11 (_)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L8 to L11 -> L13 [3]

    def test_each_scene_sees_previous_tail(self, writer, sample_state):
        'py1'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 147           RESUME                   0
        # | 148           LOAD_FAST_BORROW         1 (writer)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   52 (w, c)
        # | 149           LOAD_FAST_BORROW         3 (w)
        # |               LOAD_ATTR                1 (write_chapter_scenes + NULL|self)
        # |               LOAD_FAST_BORROW         2 (sample_state)
        # |               LOAD_GLOBAL              3 (outline + NULL)
        # |               CALL                     0
        # |               CALL                     2
        # |               POP_TOP
        # | 150           LOAD_FAST_BORROW         4 (c)
        # |               LOAD_ATTR                4 (calls)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
        # |               LOAD_ATTR                6 (prev_tail)
        # |               STORE_FAST               6 (@py_assert2)
        # |               LOAD_CONST               1 ('')
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert5, @py_assert2)
        # |               LOAD_FAST_BORROW         7 (@py_assert5)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 (('==',))
        # |               LOAD_FAST_BORROW         8 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               9 (('%(py3)s\n{%(py3)s = %(py1)s.prev_tail\n} == %(py6)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert2, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format7)
        # |               LOAD_CONST               5 ('assert %(py8)s')
        # |               LOAD_CONST               6 ('py8')
        # |               LOAD_FAST_BORROW         9 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format9)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert4, @py_assert5)
        # | 151           LOAD_FAST_BORROW         4 (c)
        # |               LOAD_ATTR                4 (calls)
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
        # |               LOAD_ATTR                6 (prev_tail)
        # |               STORE_FAST               6 (@py_assert2)
        # |               LOAD_CONST               1 ('')
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert5, @py_assert2)
        # |               LOAD_FAST_BORROW         7 (@py_assert5)
        # |               COMPARE_OP             103 (!=)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('!=',))
        # |               LOAD_FAST_BORROW         8 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py3)s\n{%(py3)s = %(py1)s.prev_tail\n} != %(py6)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert2, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format7)
        # |               LOAD_CONST               5 ('assert %(py8)s')
        # |               LOAD_CONST               6 ('py8')
        # |               LOAD_FAST_BORROW         9 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format9)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert4, @py_assert5)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_uses_writer_role(self, writer, sample_state):
        'writer'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 153           RESUME                   0
        # | 154           LOAD_FAST_BORROW         1 (writer)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   52 (w, c)
        # | 155           LOAD_FAST_BORROW         3 (w)
        # |               LOAD_ATTR                1 (write_scene + NULL|self)
        # |               LOAD_FAST_BORROW         2 (sample_state)
        # |               LOAD_GLOBAL              3 (outline + NULL)
        # |               CALL                     0
        # |               LOAD_GLOBAL              3 (outline + NULL)
        # |               CALL                     0
        # |               LOAD_ATTR                4 (scenes)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               CALL                     3
        # |               POP_TOP
        # | 156           LOAD_FAST_BORROW         4 (c)
        # |               LOAD_ATTR                6 (calls)
        # |               LOAD_CONST               7 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               5 (@py_assert0)
        # |               LOAD_CONST               1 ('writer')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         6 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 (('==',))
        # |               LOAD_FAST_BORROW         7 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               9 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format5)
        # |               LOAD_CONST               4 ('assert %(py6)s')
        # |               LOAD_CONST               5 ('py6')
        # |               LOAD_FAST_BORROW         8 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format7)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  118 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE


class TestStitcher:
    'TestStitcher'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 159           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestStitcher')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         159
    # |               STORE_NAME               3 (__firstlineno__)
    # | 160           LOAD_CONST               1 (<code object test_receives_all_scenes at 0x755f223700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 160>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_receives_all_scenes)
    # | 166           LOAD_CONST               2 (<code object test_told_not_to_rewrite at 0x755ee4c300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 166>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_told_not_to_rewrite)
    # | 172           LOAD_CONST               3 (<code object test_title_and_hook_passed at 0x755f1f9e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 172>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_title_and_hook_passed)
    # | 179           LOAD_CONST               4 (<code object test_uses_stitcher_role at 0x755ed5a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 179>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_uses_stitcher_role)
    # | 184           LOAD_CONST               5 (<code object test_shares_writer_skills at 0x755ee4c600, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 184>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_shares_writer_skills)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_receives_all_scenes at 0x755f223700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 160>:
    # | 160           RESUME                   0
    # | 161           LOAD_FAST_BORROW         1 (stitcher)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   35 (s, c)
    # | 162           LOAD_FAST_BORROW         2 (s)
    # |               LOAD_ATTR                1 (stitch + NULL|self)
    # |               LOAD_GLOBAL              3 (outline + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               0 ('第一场正文。')
    # |               LOAD_CONST               1 ('第二场正文。')
    # |               BUILD_LIST               2
    # |               CALL                     2
    # |               POP_TOP
    # | 163           LOAD_FAST_BORROW         3 (c)
    # |               LOAD_ATTR                4 (calls)
    # |               LOAD_CONST              14 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               LOAD_ATTR                6 (instruction)
    # |               STORE_FAST               4 (instr)
    # | 164           BUILD_LIST               0
    # |               STORE_FAST               5 (@py_assert1)
    # |               LOAD_CONST               0 ('第一场正文。')
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert0, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE        8 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('第二场正文。')
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert9, @py_assert9)
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert11, @py_assert11)
    # |               STORE_FAST               8 (@py_assert0)
    # |       L1:     LOAD_FAST_BORROW         8 (@py_assert0)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       404 (to L9)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('in',))
    # |               LOAD_FAST_BORROW         7 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py3)s in %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (@py_assert2, instr)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py3')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py5')
    # |               LOAD_CONST               4 ('instr')
    # |               LOAD_GLOBAL             14 (@py_builtins)
    # |               LOAD_ATTR               16 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               4 ('instr')
    # |       L4:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format6)
    # |               LOAD_CONST               5 ('%(py7)s')
    # |               LOAD_CONST               6 ('py7')
    # |               LOAD_FAST_BORROW        11 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   197 (@py_format8, @py_assert1)
    # |               LOAD_ATTR               21 (append + NULL|self)
    # |               LOAD_FAST_BORROW        12 (@py_format8)
    # |               CALL                     1
    # |               POP_TOP
    # |               LOAD_FAST_BORROW         7 (@py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE      163 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('in',))
    # |               LOAD_FAST_CHECK         10 (@py_assert11)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py10)s in %(py12)s',))
    # |               LOAD_FAST_CHECK          9 (@py_assert9)
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py10')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert9)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py12')
    # |               LOAD_CONST               4 ('instr')
    # |               LOAD_GLOBAL             14 (@py_builtins)
    # |               LOAD_ATTR               16 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               4 ('instr')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format13)
    # |               LOAD_CONST               9 ('%(py14)s')
    # |               LOAD_CONST              10 ('py14')
    # |               LOAD_FAST_BORROW        13 (@py_format13)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   229 (@py_format15, @py_assert1)
    # |               LOAD_ATTR               21 (append + NULL|self)
    # |               LOAD_FAST_BORROW        14 (@py_format15)
    # |               CALL                     1
    # |               POP_TOP
    # |       L8:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_boolop)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BUILD_MAP                0
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              15 (@py_format16)
    # |               LOAD_CONST              11 ('assert %(py17)s')
    # |               LOAD_CONST              12 ('py17')
    # |               LOAD_FAST_BORROW        15 (@py_format16)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              16 (@py_format18)
    # |               LOAD_GLOBAL             25 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               26 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        16 (@py_format18)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L9:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  154 (@py_assert9, @py_assert11)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_told_not_to_rewrite at 0x755ee4c300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 166>:
    # | 166           RESUME                   0
    # | 168           LOAD_FAST_BORROW         1 (stitcher)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   35 (s, c)
    # | 169           LOAD_FAST_BORROW         2 (s)
    # |               LOAD_ATTR                1 (stitch + NULL|self)
    # |               LOAD_GLOBAL              3 (outline + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               1 ('a')
    # |               LOAD_CONST               2 ('b')
    # |               BUILD_LIST               2
    # |               CALL                     2
    # |               POP_TOP
    # | 170           LOAD_CONST               3 ('不要重写内容')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert0, c)
    # |               LOAD_ATTR                4 (calls)
    # |               LOAD_CONST              10 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               LOAD_ATTR                6 (system_core)
    # |               STORE_FAST_LOAD_FAST   100 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         6 (@py_assert5)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('in',))
    # |               LOAD_FAST_BORROW         7 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.system_core\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format7)
    # |               LOAD_CONST               7 ('assert %(py8)s')
    # |               LOAD_CONST               8 ('py8')
    # |               LOAD_FAST_BORROW         8 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format9)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   86 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_title_and_hook_passed at 0x755f1f9e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 172>:
    # | 172           RESUME                   0
    # | 173           LOAD_FAST_BORROW         1 (stitcher)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   35 (s, c)
    # | 174           LOAD_FAST_BORROW         2 (s)
    # |               LOAD_ATTR                1 (stitch + NULL|self)
    # |               LOAD_GLOBAL              3 (outline + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               0 ('a')
    # |               LOAD_CONST               1 ('b')
    # |               BUILD_LIST               2
    # |               CALL                     2
    # |               POP_TOP
    # | 175           LOAD_FAST_BORROW         3 (c)
    # |               LOAD_ATTR                4 (calls)
    # |               LOAD_CONST              10 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               LOAD_ATTR                6 (instruction)
    # |               STORE_FAST               4 (instr)
    # | 176           LOAD_CONST               2 ('## 第12章 值班')
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('in',))
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py1)s in %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (@py_assert0, instr)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py3')
    # |               LOAD_CONST               5 ('instr')
    # |               LOAD_GLOBAL             14 (@py_builtins)
    # |               LOAD_ATTR               16 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('instr')
    # |       L3:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format4)
    # |               LOAD_CONST               6 ('assert %(py5)s')
    # |               LOAD_CONST               7 ('py5')
    # |               LOAD_FAST_BORROW         7 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format6)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   86 (@py_assert0, @py_assert2)
    # | 177           LOAD_CONST               9 ('伞留在了她手里')
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('in',))
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py1)s in %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (@py_assert0, instr)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py3')
    # |               LOAD_CONST               5 ('instr')
    # |               LOAD_GLOBAL             14 (@py_builtins)
    # |               LOAD_ATTR               16 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (instr)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               5 ('instr')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format4)
    # |               LOAD_CONST               6 ('assert %(py5)s')
    # |               LOAD_CONST               7 ('py5')
    # |               LOAD_FAST_BORROW         7 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format6)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   86 (@py_assert0, @py_assert2)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_uses_stitcher_role at 0x755ed5a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 179>:
    # | 179           RESUME                   0
    # | 180           LOAD_FAST_BORROW         1 (stitcher)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   35 (s, c)
    # | 181           LOAD_FAST_BORROW         2 (s)
    # |               LOAD_ATTR                1 (stitch + NULL|self)
    # |               LOAD_GLOBAL              3 (outline + NULL)
    # |               CALL                     0
    # |               LOAD_CONST               0 ('a')
    # |               LOAD_CONST               1 ('b')
    # |               BUILD_LIST               2
    # |               CALL                     2
    # |               POP_TOP
    # | 182           LOAD_FAST_BORROW         3 (c)
    # |               LOAD_ATTR                4 (calls)
    # |               LOAD_CONST               8 (-1)
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               4 (@py_assert0)
    # |               LOAD_CONST               2 ('stitcher')
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 (('==',))
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              10 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format5)
    # |               LOAD_CONST               5 ('assert %(py6)s')
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_FAST_BORROW         7 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_shares_writer_skills at 0x755ee4c600, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 184>:
    # | 184           RESUME                   0
    # | 186           LOAD_FAST_BORROW         1 (stitcher)
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   35 (s, _)
    # | 187           LOAD_CONST               1 ('叙述语感')
    # |               STORE_FAST_LOAD_FAST    66 (@py_assert0, s)
    # |               LOAD_ATTR                0 (system_core)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               STORE_FAST_LOAD_FAST   100 (@py_assert6, @py_assert0)
    # |               LOAD_FAST_BORROW         6 (@py_assert6)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       221 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('in',))
    # |               LOAD_FAST_BORROW         7 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.system_core\n}()\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (@py_assert0, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_CONST               4 ('s')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (s)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (s)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('s')
    # |       L3:     LOAD_CONST               5 ('py5')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py7')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format8)
    # |               LOAD_CONST               7 ('assert %(py9)s')
    # |               LOAD_CONST               8 ('py9')
    # |               LOAD_FAST_BORROW         8 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format10)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   86 (@py_assert4, @py_assert6)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE

    def test_receives_all_scenes(self, stitcher):
        '第一场正文。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 160           RESUME                   0
        # | 161           LOAD_FAST_BORROW         1 (stitcher)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   35 (s, c)
        # | 162           LOAD_FAST_BORROW         2 (s)
        # |               LOAD_ATTR                1 (stitch + NULL|self)
        # |               LOAD_GLOBAL              3 (outline + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               0 ('第一场正文。')
        # |               LOAD_CONST               1 ('第二场正文。')
        # |               BUILD_LIST               2
        # |               CALL                     2
        # |               POP_TOP
        # | 163           LOAD_FAST_BORROW         3 (c)
        # |               LOAD_ATTR                4 (calls)
        # |               LOAD_CONST              14 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               LOAD_ATTR                6 (instruction)
        # |               STORE_FAST               4 (instr)
        # | 164           BUILD_LIST               0
        # |               STORE_FAST               5 (@py_assert1)
        # |               LOAD_CONST               0 ('第一场正文。')
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert0, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE        8 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('第二场正文。')
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert9, @py_assert9)
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert11, @py_assert11)
        # |               STORE_FAST               8 (@py_assert0)
        # |       L1:     LOAD_FAST_BORROW         8 (@py_assert0)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       404 (to L9)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('in',))
        # |               LOAD_FAST_BORROW         7 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py3)s in %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (@py_assert2, instr)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py3')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py5')
        # |               LOAD_CONST               4 ('instr')
        # |               LOAD_GLOBAL             14 (@py_builtins)
        # |               LOAD_ATTR               16 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               4 ('instr')
        # |       L4:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format6)
        # |               LOAD_CONST               5 ('%(py7)s')
        # |               LOAD_CONST               6 ('py7')
        # |               LOAD_FAST_BORROW        11 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   197 (@py_format8, @py_assert1)
        # |               LOAD_ATTR               21 (append + NULL|self)
        # |               LOAD_FAST_BORROW        12 (@py_format8)
        # |               CALL                     1
        # |               POP_TOP
        # |               LOAD_FAST_BORROW         7 (@py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE      163 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('in',))
        # |               LOAD_FAST_CHECK         10 (@py_assert11)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py10)s in %(py12)s',))
        # |               LOAD_FAST_CHECK          9 (@py_assert9)
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py10')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert9)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py12')
        # |               LOAD_CONST               4 ('instr')
        # |               LOAD_GLOBAL             14 (@py_builtins)
        # |               LOAD_ATTR               16 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               4 ('instr')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format13)
        # |               LOAD_CONST               9 ('%(py14)s')
        # |               LOAD_CONST              10 ('py14')
        # |               LOAD_FAST_BORROW        13 (@py_format13)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   229 (@py_format15, @py_assert1)
        # |               LOAD_ATTR               21 (append + NULL|self)
        # |               LOAD_FAST_BORROW        14 (@py_format15)
        # |               CALL                     1
        # |               POP_TOP
        # |       L8:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_boolop)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BUILD_MAP                0
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              15 (@py_format16)
        # |               LOAD_CONST              11 ('assert %(py17)s')
        # |               LOAD_CONST              12 ('py17')
        # |               LOAD_FAST_BORROW        15 (@py_format16)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              16 (@py_format18)
        # |               LOAD_GLOBAL             25 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               26 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        16 (@py_format18)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L9:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  154 (@py_assert9, @py_assert11)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE

    def test_told_not_to_rewrite(self, stitcher):
        '越权重写会掩盖场景本身的问题，让检查环节抓不到。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 166           RESUME                   0
        # | 168           LOAD_FAST_BORROW         1 (stitcher)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   35 (s, c)
        # | 169           LOAD_FAST_BORROW         2 (s)
        # |               LOAD_ATTR                1 (stitch + NULL|self)
        # |               LOAD_GLOBAL              3 (outline + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               1 ('a')
        # |               LOAD_CONST               2 ('b')
        # |               BUILD_LIST               2
        # |               CALL                     2
        # |               POP_TOP
        # | 170           LOAD_CONST               3 ('不要重写内容')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert0, c)
        # |               LOAD_ATTR                4 (calls)
        # |               LOAD_CONST              10 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               LOAD_ATTR                6 (system_core)
        # |               STORE_FAST_LOAD_FAST   100 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         6 (@py_assert5)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('in',))
        # |               LOAD_FAST_BORROW         7 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.system_core\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format7)
        # |               LOAD_CONST               7 ('assert %(py8)s')
        # |               LOAD_CONST               8 ('py8')
        # |               LOAD_FAST_BORROW         8 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format9)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   86 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_title_and_hook_passed(self, stitcher):
        'a'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 172           RESUME                   0
        # | 173           LOAD_FAST_BORROW         1 (stitcher)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   35 (s, c)
        # | 174           LOAD_FAST_BORROW         2 (s)
        # |               LOAD_ATTR                1 (stitch + NULL|self)
        # |               LOAD_GLOBAL              3 (outline + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               0 ('a')
        # |               LOAD_CONST               1 ('b')
        # |               BUILD_LIST               2
        # |               CALL                     2
        # |               POP_TOP
        # | 175           LOAD_FAST_BORROW         3 (c)
        # |               LOAD_ATTR                4 (calls)
        # |               LOAD_CONST              10 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               LOAD_ATTR                6 (instruction)
        # |               STORE_FAST               4 (instr)
        # | 176           LOAD_CONST               2 ('## 第12章 值班')
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       177 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('in',))
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py1)s in %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (@py_assert0, instr)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py3')
        # |               LOAD_CONST               5 ('instr')
        # |               LOAD_GLOBAL             14 (@py_builtins)
        # |               LOAD_ATTR               16 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('instr')
        # |       L3:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format4)
        # |               LOAD_CONST               6 ('assert %(py5)s')
        # |               LOAD_CONST               7 ('py5')
        # |               LOAD_FAST_BORROW         7 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format6)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   86 (@py_assert0, @py_assert2)
        # | 177           LOAD_CONST               9 ('伞留在了她手里')
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       177 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('in',))
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py1)s in %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 84 (@py_assert0, instr)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py3')
        # |               LOAD_CONST               5 ('instr')
        # |               LOAD_GLOBAL             14 (@py_builtins)
        # |               LOAD_ATTR               16 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (instr)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               5 ('instr')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format4)
        # |               LOAD_CONST               6 ('assert %(py5)s')
        # |               LOAD_CONST               7 ('py5')
        # |               LOAD_FAST_BORROW         7 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format6)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   86 (@py_assert0, @py_assert2)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE

    def test_uses_stitcher_role(self, stitcher):
        'a'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 179           RESUME                   0
        # | 180           LOAD_FAST_BORROW         1 (stitcher)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   35 (s, c)
        # | 181           LOAD_FAST_BORROW         2 (s)
        # |               LOAD_ATTR                1 (stitch + NULL|self)
        # |               LOAD_GLOBAL              3 (outline + NULL)
        # |               CALL                     0
        # |               LOAD_CONST               0 ('a')
        # |               LOAD_CONST               1 ('b')
        # |               BUILD_LIST               2
        # |               CALL                     2
        # |               POP_TOP
        # | 182           LOAD_FAST_BORROW         3 (c)
        # |               LOAD_ATTR                4 (calls)
        # |               LOAD_CONST               8 (-1)
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               4 (@py_assert0)
        # |               LOAD_CONST               2 ('stitcher')
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 (('==',))
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              10 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format5)
        # |               LOAD_CONST               5 ('assert %(py6)s')
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_FAST_BORROW         7 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_shares_writer_skills(self, stitcher):
        '缝合要按同样的文风判断接缝，所以共享 writer 的 skills。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 184           RESUME                   0
        # | 186           LOAD_FAST_BORROW         1 (stitcher)
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   35 (s, _)
        # | 187           LOAD_CONST               1 ('叙述语感')
        # |               STORE_FAST_LOAD_FAST    66 (@py_assert0, s)
        # |               LOAD_ATTR                0 (system_core)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               STORE_FAST_LOAD_FAST   100 (@py_assert6, @py_assert0)
        # |               LOAD_FAST_BORROW         6 (@py_assert6)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       221 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('in',))
        # |               LOAD_FAST_BORROW         7 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.system_core\n}()\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 70 (@py_assert0, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_CONST               4 ('s')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (s)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (s)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('s')
        # |       L3:     LOAD_CONST               5 ('py5')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py7')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format8)
        # |               LOAD_CONST               7 ('assert %(py9)s')
        # |               LOAD_CONST               8 ('py9')
        # |               LOAD_FAST_BORROW         8 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format10)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   86 (@py_assert4, @py_assert6)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE


class TestStitchCompleteness:
    'TestStitchCompleteness'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 190           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestStitchCompleteness')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         190
    # |               STORE_NAME               3 (__firstlineno__)
    # | 191           LOAD_CONST               1 ('实测一次 stitcher 只吐 87 字就 end_turn 收工（场景总和 4,491 字），\n正文停在半个词上。stop_reason 不是 length，光看它发现不了。')
    # |               STORE_NAME               4 (__doc__)
    # | 194           LOAD_CONST               2 (<code object test_truncated_stitch_is_rejected at 0x105562470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 194>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_truncated_stitch_is_rejected)
    # | 200           LOAD_CONST               3 (<code object test_retry_before_giving_up at 0x755f1f9400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 200>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_retry_before_giving_up)
    # | 207           LOAD_CONST               4 (<code object test_retry_carries_a_warning at 0x755ee3ca80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 207>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_retry_carries_a_warning)
    # | 214           LOAD_CONST               5 (<code object test_complete_stitch_passes at 0x755ee2aa00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 214>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_complete_stitch_passes)
    # | 219           LOAD_CONST               6 (<code object test_shortening_is_allowed_within_reason at 0x755f24c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 219>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_shortening_is_allowed_within_reason)
    # |               LOAD_CONST               7 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_truncated_stitch_is_rejected at 0x105562470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 194>:
    # |  194           RESUME                   0
    # |  195           LOAD_GLOBAL              1 (FakeClient + NULL)
    # |                LOAD_CONST               0 ('## 第12章 值班\n\n沈知微把一叠诗稿抖齐，指腹压')
    # |                CALL                     1
    # |                STORE_FAST               1 (c)
    # |  196           LOAD_GLOBAL              3 (Stitcher + NULL)
    # |                LOAD_FAST_BORROW         1 (c)
    # |                LOAD_GLOBAL              4 (SKILLS)
    # |                CALL                     2
    # |                STORE_FAST               2 (s)
    # |  197           LOAD_GLOBAL              6 (pytest)
    # |                LOAD_ATTR                8 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (RuntimeError)
    # |                LOAD_CONST               1 ('缝合失败')
    # |                LOAD_CONST               2 (('match',))
    # |                CALL_KW                  2
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |  198           LOAD_FAST_BORROW         2 (s)
    # |                LOAD_ATTR               13 (stitch + NULL|self)
    # |                LOAD_GLOBAL             15 (outline + NULL)
    # |                CALL                     0
    # |                LOAD_CONST               4 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
    # |                LOAD_CONST               4 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
    # |                BUILD_LIST               2
    # |                CALL                     2
    # |                POP_TOP
    # |  197   L2:     LOAD_CONST               3 (None)
    # |                LOAD_CONST               3 (None)
    # |                LOAD_CONST               3 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |                LOAD_CONST               3 (None)
    # |                RETURN_VALUE
    # |        L3:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L4)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L4:     POP_TOP
    # |        L5:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                LOAD_CONST               3 (None)
    # |                RETURN_VALUE
    # |   --   L6:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L3 [2] lasti
    # |   L3 to L5 -> L6 [4] lasti
    # | Disassembly of <code object test_retry_before_giving_up at 0x755f1f9400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 200>:
    # |  200            RESUME                   0
    # |  201            LOAD_GLOBAL              1 (FakeClient + NULL)
    # |                 LOAD_CONST               0 ('太短。')
    # |                 CALL                     1
    # |                 STORE_FAST               1 (c)
    # |  202            LOAD_GLOBAL              3 (Stitcher + NULL)
    # |                 LOAD_FAST_BORROW         1 (c)
    # |                 LOAD_GLOBAL              4 (SKILLS)
    # |                 CALL                     2
    # |                 STORE_FAST               2 (s)
    # |  203            LOAD_GLOBAL              6 (pytest)
    # |                 LOAD_ATTR                8 (raises)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             10 (RuntimeError)
    # |                 CALL                     1
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     POP_TOP
    # |  204            LOAD_FAST_BORROW         2 (s)
    # |                 LOAD_ATTR               13 (stitch + NULL|self)
    # |                 LOAD_GLOBAL             15 (outline + NULL)
    # |                 CALL                     0
    # |                 LOAD_CONST              12 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
    # |                 LOAD_CONST              12 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
    # |                 BUILD_LIST               2
    # |                 CALL                     2
    # |                 POP_TOP
    # |  203    L2:     LOAD_CONST               1 (None)
    # |                 LOAD_CONST               1 (None)
    # |                 LOAD_CONST               1 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  205    L3:     LOAD_FAST_BORROW         1 (c)
    # |                 LOAD_ATTR               16 (calls)
    # |                 STORE_FAST               3 (@py_assert2)
    # |                 LOAD_GLOBAL             19 (len + NULL)
    # |                 LOAD_FAST_BORROW         3 (@py_assert2)
    # |                 CALL                     1
    # |                 STORE_FAST               4 (@py_assert4)
    # |                 LOAD_SMALL_INT           2
    # |                 STORE_FAST_LOAD_FAST    84 (@py_assert7, @py_assert4)
    # |                 LOAD_FAST_BORROW         5 (@py_assert7)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   102 (@py_assert6, @py_assert6)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       334 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              13 (('==',))
    # |                 LOAD_FAST_BORROW         6 (@py_assert6)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              14 (('%(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s.calls\n})\n} == %(py8)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert4, @py_assert7)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               2 ('py0')
    # |                 LOAD_CONST               3 ('len')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             18 (len)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             18 (len)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               3 ('len')
    # |         L6:     LOAD_CONST               4 ('py1')
    # |                 LOAD_CONST               5 ('c')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (c)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L8)
    # |                 NOT_TAKEN
    # |         L7:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (c)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L9)
    # |         L8:     LOAD_CONST               5 ('c')
    # |         L9:     LOAD_CONST               6 ('py3')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert2)
    # |                 CALL                     1
    # |                 LOAD_CONST               7 ('py5')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST               8 ('py8')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert7)
    # |                 CALL                     1
    # |                 BUILD_MAP                5
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format9)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST               9 ('应当重试一次再放弃')
    # |                 CALL                     1
    # |                 LOAD_CONST              10 ('\n>assert %(py10)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              11 ('py10')
    # |                 LOAD_FAST_BORROW         7 (@py_format9)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format11)
    # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               36 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_format11)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L10:     LOAD_CONST               1 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               3 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert4)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  101 (@py_assert6, @py_assert7)
    # |                 LOAD_CONST               1 (None)
    # |                 RETURN_VALUE
    # |  203   L11:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L12)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L12:     POP_TOP
    # |        L13:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             1
    # |                 JUMP_BACKWARD_NO_INTERRUPT 396 (to L3)
    # |   --   L14:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L11 [2] lasti
    # |   L11 to L13 -> L14 [4] lasti
    # | Disassembly of <code object test_retry_carries_a_warning at 0x755ee3ca80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 207>:
    # |  207           RESUME                   0
    # |  208           LOAD_GLOBAL              1 (FakeClient + NULL)
    # |                LOAD_CONST               0 ('太短。')
    # |                CALL                     1
    # |                STORE_FAST               1 (c)
    # |  209           LOAD_GLOBAL              3 (Stitcher + NULL)
    # |                LOAD_FAST_BORROW         1 (c)
    # |                LOAD_GLOBAL              4 (SKILLS)
    # |                CALL                     2
    # |                STORE_FAST               2 (s)
    # |  210           LOAD_GLOBAL              6 (pytest)
    # |                LOAD_ATTR                8 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (RuntimeError)
    # |                CALL                     1
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |  211           LOAD_FAST_BORROW         2 (s)
    # |                LOAD_ATTR               13 (stitch + NULL|self)
    # |                LOAD_GLOBAL             15 (outline + NULL)
    # |                CALL                     0
    # |                LOAD_CONST               8 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
    # |                LOAD_CONST               8 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
    # |                BUILD_LIST               2
    # |                CALL                     2
    # |                POP_TOP
    # |  210   L2:     LOAD_CONST               1 (None)
    # |                LOAD_CONST               1 (None)
    # |                LOAD_CONST               1 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |  212   L3:     LOAD_CONST               2 ('严重不完整')
    # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, c)
    # |                LOAD_ATTR               16 (calls)
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |                LOAD_ATTR               18 (instruction)
    # |                STORE_FAST_LOAD_FAST    83 (@py_assert5, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (@py_assert5)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       143 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               22 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST               9 (('in',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              10 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.instruction\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (@py_assert0, @py_assert5)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py4')
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py6')
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format7)
    # |                LOAD_CONST               6 ('assert %(py8)s')
    # |                LOAD_CONST               7 ('py8')
    # |                LOAD_FAST_BORROW         7 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format9)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |  210   L5:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L6)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L6:     POP_TOP
    # |        L7:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                JUMP_BACKWARD_NO_INTERRUPT 216 (to L3)
    # |   --   L8:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L5 [2] lasti
    # |   L5 to L7 -> L8 [4] lasti
    # | Disassembly of <code object test_complete_stitch_passes at 0x755ee2aa00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 214>:
    # | 214            RESUME                   0
    # | 215            LOAD_CONST              17 ('这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。')
    # |                STORE_FAST               1 (body)
    # | 216            LOAD_GLOBAL              1 (FakeClient + NULL)
    # |                LOAD_CONST               1 ('## 第12章 值班\n\n')
    # |                LOAD_FAST_BORROW         1 (body)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                STORE_FAST               2 (c)
    # | 217            LOAD_GLOBAL              3 (Stitcher + NULL)
    # |                LOAD_FAST_BORROW         2 (c)
    # |                LOAD_GLOBAL              4 (SKILLS)
    # |                CALL                     2
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
    # |                LOAD_ATTR                6 (stitch)
    # |                STORE_FAST               4 (@py_assert5)
    # |                LOAD_GLOBAL              9 (outline + NULL)
    # |                CALL                     0
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_CONST              18 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
    # |                LOAD_CONST              18 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
    # |                BUILD_LIST               2
    # |                STORE_FAST_LOAD_FAST   100 (@py_assert10, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert10)
    # |                CALL                     2
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert12, @py_assert12)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       487 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_CONST               2 ('assert %(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}.stitch\n}(%(py9)s\n{%(py9)s = %(py7)s()\n}, %(py11)s)\n}')
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('Stitcher')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (Stitcher)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (Stitcher)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('Stitcher')
    # |        L3:     LOAD_CONST               5 ('py1')
    # |                LOAD_CONST               6 ('c')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (c)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (c)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               6 ('c')
    # |        L6:     LOAD_CONST               7 ('py2')
    # |                LOAD_CONST               8 ('SKILLS')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (SKILLS)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (SKILLS)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               8 ('SKILLS')
    # |        L9:     LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py6')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py7')
    # |                LOAD_CONST              12 ('outline')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (outline)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (outline)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST              12 ('outline')
    # |       L12:     LOAD_CONST              13 ('py9')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py11')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py13')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert12)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format14)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L13:     LOAD_CONST              16 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert10, @py_assert12)
    # |                LOAD_CONST              16 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_shortening_is_allowed_within_reason at 0x755f24c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 219>:
    # | 219            RESUME                   0
    # | 221            LOAD_CONST              21 ('正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。')
    # |                LOAD_CONST              21 ('正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。')
    # |                BUILD_LIST               2
    # |                STORE_FAST               1 (scenes)
    # | 222            LOAD_CONST               1 ('')
    # |                LOAD_ATTR                1 (join + NULL|self)
    # |                LOAD_FAST_BORROW         1 (scenes)
    # |                CALL                     1
    # |                LOAD_CONST               2 (None)
    # |                LOAD_GLOBAL              3 (int + NULL)
    # |                LOAD_GLOBAL              5 (sum + NULL)
    # |                LOAD_CONST               3 (<code object <genexpr> at 0x105770690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 222>)
    # |                MAKE_FUNCTION
    # |                LOAD_FAST_BORROW         1 (scenes)
    # |                GET_ITER
    # |                CALL                     0
    # |                CALL                     1
    # |                LOAD_CONST               4 (0.75)
    # |                BINARY_OP                5 (*)
    # |                CALL                     1
    # |                BINARY_SLICE
    # |                LOAD_CONST               5 ('。')
    # |                BINARY_OP                0 (+)
    # |                STORE_FAST               2 (kept)
    # | 223            LOAD_GLOBAL              7 (FakeClient + NULL)
    # |                LOAD_FAST_BORROW         2 (kept)
    # |                CALL                     1
    # |                STORE_FAST               3 (c)
    # | 224            LOAD_GLOBAL              9 (Stitcher + NULL)
    # |                LOAD_FAST_BORROW         3 (c)
    # |                LOAD_GLOBAL             10 (SKILLS)
    # |                CALL                     2
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |                LOAD_ATTR               12 (stitch)
    # |                STORE_FAST               5 (@py_assert5)
    # |                LOAD_GLOBAL             15 (outline + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert8, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (@py_assert8, scenes)
    # |                CALL                     2
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert11, @py_assert11)
    # |                TO_BOOL
    # |                EXTENDED_ARG             2
    # |                POP_JUMP_IF_TRUE       543 (to L16)
    # |                NOT_TAKEN
    # |                LOAD_CONST               6 ('assert %(py12)s\n{%(py12)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}.stitch\n}(%(py9)s\n{%(py9)s = %(py7)s()\n}, %(py10)s)\n}')
    # |                LOAD_CONST               7 ('py0')
    # |                LOAD_CONST               8 ('Stitcher')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (Stitcher)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (Stitcher)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               8 ('Stitcher')
    # |        L3:     LOAD_CONST               9 ('py1')
    # |                LOAD_CONST              10 ('c')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (c)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (c)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST              10 ('c')
    # |        L6:     LOAD_CONST              11 ('py2')
    # |                LOAD_CONST              12 ('SKILLS')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (SKILLS)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (SKILLS)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              12 ('SKILLS')
    # |        L9:     LOAD_CONST              13 ('py4')
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py6')
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py7')
    # |                LOAD_CONST              16 ('outline')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (outline)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (outline)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST              16 ('outline')
    # |       L12:     LOAD_CONST              17 ('py9')
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              18 ('py10')
    # |                LOAD_CONST              19 ('scenes')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (scenes)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L14)
    # |                NOT_TAKEN
    # |       L13:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (scenes)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L15)
    # |       L14:     LOAD_CONST              19 ('scenes')
    # |       L15:     LOAD_CONST              20 ('py12')
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format13)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL             20 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format13)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L16:     LOAD_CONST               2 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert8, @py_assert11)
    # |                LOAD_CONST               2 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x105770690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 222>:
    # |  222           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST               1 (s)
    # |                LOAD_GLOBAL              1 (len + NULL)
    # |                LOAD_FAST_BORROW         1 (s)
    # |                CALL                     1
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           18 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti

    def test_truncated_stitch_is_rejected(self):
        '## 第12章 值班\n\n沈知微把一叠诗稿抖齐，指腹压'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  194           RESUME                   0
        # |  195           LOAD_GLOBAL              1 (FakeClient + NULL)
        # |                LOAD_CONST               0 ('## 第12章 值班\n\n沈知微把一叠诗稿抖齐，指腹压')
        # |                CALL                     1
        # |                STORE_FAST               1 (c)
        # |  196           LOAD_GLOBAL              3 (Stitcher + NULL)
        # |                LOAD_FAST_BORROW         1 (c)
        # |                LOAD_GLOBAL              4 (SKILLS)
        # |                CALL                     2
        # |                STORE_FAST               2 (s)
        # |  197           LOAD_GLOBAL              6 (pytest)
        # |                LOAD_ATTR                8 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (RuntimeError)
        # |                LOAD_CONST               1 ('缝合失败')
        # |                LOAD_CONST               2 (('match',))
        # |                CALL_KW                  2
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |  198           LOAD_FAST_BORROW         2 (s)
        # |                LOAD_ATTR               13 (stitch + NULL|self)
        # |                LOAD_GLOBAL             15 (outline + NULL)
        # |                CALL                     0
        # |                LOAD_CONST               4 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
        # |                LOAD_CONST               4 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
        # |                BUILD_LIST               2
        # |                CALL                     2
        # |                POP_TOP
        # |  197   L2:     LOAD_CONST               3 (None)
        # |                LOAD_CONST               3 (None)
        # |                LOAD_CONST               3 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |                LOAD_CONST               3 (None)
        # |                RETURN_VALUE
        # |        L3:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L4)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L4:     POP_TOP
        # |        L5:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                LOAD_CONST               3 (None)
        # |                RETURN_VALUE
        # |   --   L6:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L3 [2] lasti
        # |   L3 to L5 -> L6 [4] lasti

    def test_retry_before_giving_up(self):
        '太短。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  200            RESUME                   0
        # |  201            LOAD_GLOBAL              1 (FakeClient + NULL)
        # |                 LOAD_CONST               0 ('太短。')
        # |                 CALL                     1
        # |                 STORE_FAST               1 (c)
        # |  202            LOAD_GLOBAL              3 (Stitcher + NULL)
        # |                 LOAD_FAST_BORROW         1 (c)
        # |                 LOAD_GLOBAL              4 (SKILLS)
        # |                 CALL                     2
        # |                 STORE_FAST               2 (s)
        # |  203            LOAD_GLOBAL              6 (pytest)
        # |                 LOAD_ATTR                8 (raises)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             10 (RuntimeError)
        # |                 CALL                     1
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     POP_TOP
        # |  204            LOAD_FAST_BORROW         2 (s)
        # |                 LOAD_ATTR               13 (stitch + NULL|self)
        # |                 LOAD_GLOBAL             15 (outline + NULL)
        # |                 CALL                     0
        # |                 LOAD_CONST              12 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
        # |                 LOAD_CONST              12 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
        # |                 BUILD_LIST               2
        # |                 CALL                     2
        # |                 POP_TOP
        # |  203    L2:     LOAD_CONST               1 (None)
        # |                 LOAD_CONST               1 (None)
        # |                 LOAD_CONST               1 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  205    L3:     LOAD_FAST_BORROW         1 (c)
        # |                 LOAD_ATTR               16 (calls)
        # |                 STORE_FAST               3 (@py_assert2)
        # |                 LOAD_GLOBAL             19 (len + NULL)
        # |                 LOAD_FAST_BORROW         3 (@py_assert2)
        # |                 CALL                     1
        # |                 STORE_FAST               4 (@py_assert4)
        # |                 LOAD_SMALL_INT           2
        # |                 STORE_FAST_LOAD_FAST    84 (@py_assert7, @py_assert4)
        # |                 LOAD_FAST_BORROW         5 (@py_assert7)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   102 (@py_assert6, @py_assert6)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       334 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              13 (('==',))
        # |                 LOAD_FAST_BORROW         6 (@py_assert6)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              14 (('%(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s.calls\n})\n} == %(py8)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert4, @py_assert7)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               2 ('py0')
        # |                 LOAD_CONST               3 ('len')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             18 (len)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             18 (len)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               3 ('len')
        # |         L6:     LOAD_CONST               4 ('py1')
        # |                 LOAD_CONST               5 ('c')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (c)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L8)
        # |                 NOT_TAKEN
        # |         L7:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (c)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L9)
        # |         L8:     LOAD_CONST               5 ('c')
        # |         L9:     LOAD_CONST               6 ('py3')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert2)
        # |                 CALL                     1
        # |                 LOAD_CONST               7 ('py5')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST               8 ('py8')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert7)
        # |                 CALL                     1
        # |                 BUILD_MAP                5
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format9)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST               9 ('应当重试一次再放弃')
        # |                 CALL                     1
        # |                 LOAD_CONST              10 ('\n>assert %(py10)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              11 ('py10')
        # |                 LOAD_FAST_BORROW         7 (@py_format9)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format11)
        # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               36 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_format11)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L10:     LOAD_CONST               1 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               3 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert4)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  101 (@py_assert6, @py_assert7)
        # |                 LOAD_CONST               1 (None)
        # |                 RETURN_VALUE
        # |  203   L11:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L12)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L12:     POP_TOP
        # |        L13:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             1
        # |                 JUMP_BACKWARD_NO_INTERRUPT 396 (to L3)
        # |   --   L14:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L11 [2] lasti
        # |   L11 to L13 -> L14 [4] lasti

    def test_retry_carries_a_warning(self):
        '太短。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  207           RESUME                   0
        # |  208           LOAD_GLOBAL              1 (FakeClient + NULL)
        # |                LOAD_CONST               0 ('太短。')
        # |                CALL                     1
        # |                STORE_FAST               1 (c)
        # |  209           LOAD_GLOBAL              3 (Stitcher + NULL)
        # |                LOAD_FAST_BORROW         1 (c)
        # |                LOAD_GLOBAL              4 (SKILLS)
        # |                CALL                     2
        # |                STORE_FAST               2 (s)
        # |  210           LOAD_GLOBAL              6 (pytest)
        # |                LOAD_ATTR                8 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (RuntimeError)
        # |                CALL                     1
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |  211           LOAD_FAST_BORROW         2 (s)
        # |                LOAD_ATTR               13 (stitch + NULL|self)
        # |                LOAD_GLOBAL             15 (outline + NULL)
        # |                CALL                     0
        # |                LOAD_CONST               8 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
        # |                LOAD_CONST               8 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
        # |                BUILD_LIST               2
        # |                CALL                     2
        # |                POP_TOP
        # |  210   L2:     LOAD_CONST               1 (None)
        # |                LOAD_CONST               1 (None)
        # |                LOAD_CONST               1 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |  212   L3:     LOAD_CONST               2 ('严重不完整')
        # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, c)
        # |                LOAD_ATTR               16 (calls)
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |                LOAD_ATTR               18 (instruction)
        # |                STORE_FAST_LOAD_FAST    83 (@py_assert5, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (@py_assert5)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       143 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               22 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST               9 (('in',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              10 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.instruction\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (@py_assert0, @py_assert5)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py4')
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py6')
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format7)
        # |                LOAD_CONST               6 ('assert %(py8)s')
        # |                LOAD_CONST               7 ('py8')
        # |                LOAD_FAST_BORROW         7 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format9)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format9)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |  210   L5:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L6)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L6:     POP_TOP
        # |        L7:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                JUMP_BACKWARD_NO_INTERRUPT 216 (to L3)
        # |   --   L8:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L5 [2] lasti
        # |   L5 to L7 -> L8 [4] lasti

    def test_complete_stitch_passes(self):
        '这是一段完整的正文。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 214            RESUME                   0
        # | 215            LOAD_CONST              17 ('这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。这是一段完整的正文。')
        # |                STORE_FAST               1 (body)
        # | 216            LOAD_GLOBAL              1 (FakeClient + NULL)
        # |                LOAD_CONST               1 ('## 第12章 值班\n\n')
        # |                LOAD_FAST_BORROW         1 (body)
        # |                FORMAT_SIMPLE
        # |                BUILD_STRING             2
        # |                CALL                     1
        # |                STORE_FAST               2 (c)
        # | 217            LOAD_GLOBAL              3 (Stitcher + NULL)
        # |                LOAD_FAST_BORROW         2 (c)
        # |                LOAD_GLOBAL              4 (SKILLS)
        # |                CALL                     2
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert3, @py_assert3)
        # |                LOAD_ATTR                6 (stitch)
        # |                STORE_FAST               4 (@py_assert5)
        # |                LOAD_GLOBAL              9 (outline + NULL)
        # |                CALL                     0
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_CONST              18 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
        # |                LOAD_CONST              18 ('正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。正文。')
        # |                BUILD_LIST               2
        # |                STORE_FAST_LOAD_FAST   100 (@py_assert10, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert10)
        # |                CALL                     2
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert12, @py_assert12)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       487 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_CONST               2 ('assert %(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}.stitch\n}(%(py9)s\n{%(py9)s = %(py7)s()\n}, %(py11)s)\n}')
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('Stitcher')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (Stitcher)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (Stitcher)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('Stitcher')
        # |        L3:     LOAD_CONST               5 ('py1')
        # |                LOAD_CONST               6 ('c')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (c)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (c)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               6 ('c')
        # |        L6:     LOAD_CONST               7 ('py2')
        # |                LOAD_CONST               8 ('SKILLS')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (SKILLS)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (SKILLS)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               8 ('SKILLS')
        # |        L9:     LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py6')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py7')
        # |                LOAD_CONST              12 ('outline')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (outline)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (outline)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST              12 ('outline')
        # |       L12:     LOAD_CONST              13 ('py9')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py11')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py13')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert12)
        # |                CALL                     1
        # |                BUILD_MAP                9
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format14)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L13:     LOAD_CONST              16 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert10, @py_assert12)
        # |                LOAD_CONST              16 (None)
        # |                RETURN_VALUE

    def test_shortening_is_allowed_within_reason(self):
        '缝合本来就要删重复，适度变短是正常的。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 219            RESUME                   0
        # | 221            LOAD_CONST              21 ('正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。')
        # |                LOAD_CONST              21 ('正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。正文内容。')
        # |                BUILD_LIST               2
        # |                STORE_FAST               1 (scenes)
        # | 222            LOAD_CONST               1 ('')
        # |                LOAD_ATTR                1 (join + NULL|self)
        # |                LOAD_FAST_BORROW         1 (scenes)
        # |                CALL                     1
        # |                LOAD_CONST               2 (None)
        # |                LOAD_GLOBAL              3 (int + NULL)
        # |                LOAD_GLOBAL              5 (sum + NULL)
        # |                LOAD_CONST               3 (<code object <genexpr> at 0x105770690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 222>)
        # |                MAKE_FUNCTION
        # |                LOAD_FAST_BORROW         1 (scenes)
        # |                GET_ITER
        # |                CALL                     0
        # |                CALL                     1
        # |                LOAD_CONST               4 (0.75)
        # |                BINARY_OP                5 (*)
        # |                CALL                     1
        # |                BINARY_SLICE
        # |                LOAD_CONST               5 ('。')
        # |                BINARY_OP                0 (+)
        # |                STORE_FAST               2 (kept)
        # | 223            LOAD_GLOBAL              7 (FakeClient + NULL)
        # |                LOAD_FAST_BORROW         2 (kept)
        # |                CALL                     1
        # |                STORE_FAST               3 (c)
        # | 224            LOAD_GLOBAL              9 (Stitcher + NULL)
        # |                LOAD_FAST_BORROW         3 (c)
        # |                LOAD_GLOBAL             10 (SKILLS)
        # |                CALL                     2
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |                LOAD_ATTR               12 (stitch)
        # |                STORE_FAST               5 (@py_assert5)
        # |                LOAD_GLOBAL             15 (outline + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert8, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (@py_assert8, scenes)
        # |                CALL                     2
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert11, @py_assert11)
        # |                TO_BOOL
        # |                EXTENDED_ARG             2
        # |                POP_JUMP_IF_TRUE       543 (to L16)
        # |                NOT_TAKEN
        # |                LOAD_CONST               6 ('assert %(py12)s\n{%(py12)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}.stitch\n}(%(py9)s\n{%(py9)s = %(py7)s()\n}, %(py10)s)\n}')
        # |                LOAD_CONST               7 ('py0')
        # |                LOAD_CONST               8 ('Stitcher')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (Stitcher)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (Stitcher)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               8 ('Stitcher')
        # |        L3:     LOAD_CONST               9 ('py1')
        # |                LOAD_CONST              10 ('c')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (c)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (c)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST              10 ('c')
        # |        L6:     LOAD_CONST              11 ('py2')
        # |                LOAD_CONST              12 ('SKILLS')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (SKILLS)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (SKILLS)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              12 ('SKILLS')
        # |        L9:     LOAD_CONST              13 ('py4')
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py6')
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py7')
        # |                LOAD_CONST              16 ('outline')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (outline)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (outline)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST              16 ('outline')
        # |       L12:     LOAD_CONST              17 ('py9')
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              18 ('py10')
        # |                LOAD_CONST              19 ('scenes')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (scenes)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L14)
        # |                NOT_TAKEN
        # |       L13:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (scenes)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L15)
        # |       L14:     LOAD_CONST              19 ('scenes')
        # |       L15:     LOAD_CONST              20 ('py12')
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                9
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format13)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL             20 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format13)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L16:     LOAD_CONST               2 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert8, @py_assert11)
        # |                LOAD_CONST               2 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x105770690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 222>:
        # |  222           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                16 (to L3)
        # |                STORE_FAST               1 (s)
        # |                LOAD_GLOBAL              1 (len + NULL)
        # |                LOAD_FAST_BORROW         1 (s)
        # |                CALL                     1
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           18 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               0 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti


class TestTrailingNotesAreStripped:
    'TestTrailingNotesAreStripped'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 227           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestTrailingNotesAreStripped')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         227
    # |               STORE_NAME               3 (__firstlineno__)
    # | 228           LOAD_CONST               1 ('实测：stitcher 三次缝合三次都在正文后面加了一段 `---` + 缝合说明\n（「年份原本三个场景各说一套…我按 s2 统一为…」）。输出是原样存盘的，\n说明就成了小说的一部分。而修订环修不掉它 —— 重写场景改不了 stitcher\n的习惯，每重缝一次就再加一遍，两轮上限白烧。')
    # |               STORE_NAME               4 (__doc__)
    # | 233           LOAD_CONST               2 (<code object test_strips_from_the_separator at 0x755ee3ce00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 233>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_strips_from_the_separator)
    # | 239           LOAD_CONST               3 (<code object test_keeps_chapters_that_have_no_notes at 0x755ee4a000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 239>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_keeps_chapters_that_have_no_notes)
    # | 245           LOAD_CONST               4 (<code object test_does_not_touch_em_dashes_in_prose at 0x755ee4a400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 245>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_does_not_touch_em_dashes_in_prose)
    # | 252           LOAD_CONST               5 (<code object test_handles_other_separator_styles at 0x755ee4a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 252>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_handles_other_separator_styles)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_strips_from_the_separator at 0x755ee3ce00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 233>:
    # | 233           RESUME                   0
    # | 234           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('_strip_trailing_notes',))
    # |               IMPORT_NAME              0 (novel_agent.agents.writer)
    # |               IMPORT_FROM              1 (_strip_trailing_notes)
    # |               STORE_FAST               1 (_strip_trailing_notes)
    # |               POP_TOP
    # | 236           LOAD_CONST               2 ('## 第3章 问号那一处\n\n她转过身。\n\n---\n\n缝合说明：统一了年份。')
    # |               STORE_FAST               2 (text)
    # | 237           LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (text)
    # |               CALL                     1
    # |               STORE_FAST               3 (@py_assert2)
    # |               LOAD_CONST               3 ('## 第3章 问号那一处\n\n她转过身。')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert5, @py_assert2)
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       277 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              14 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert2, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST               5 ('_strip_trailing_notes')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('_strip_trailing_notes')
    # |       L3:     LOAD_CONST               6 ('py1')
    # |               LOAD_CONST               7 ('text')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (text)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (text)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               7 ('text')
    # |       L6:     LOAD_CONST               8 ('py3')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_CONST              10 ('assert %(py8)s')
    # |               LOAD_CONST              11 ('py8')
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format9)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert4, @py_assert5)
    # |               LOAD_CONST              12 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_keeps_chapters_that_have_no_notes at 0x755ee4a000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 239>:
    # | 239            RESUME                   0
    # | 240            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('_strip_trailing_notes',))
    # |                IMPORT_NAME              0 (novel_agent.agents.writer)
    # |                IMPORT_FROM              1 (_strip_trailing_notes)
    # |                STORE_FAST               1 (_strip_trailing_notes)
    # |                POP_TOP
    # | 242            LOAD_CONST               2 ('## 第1章 值班\n\n她接下了那份稿子。')
    # |                STORE_FAST               2 (text)
    # | 243            LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         2 (text)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       333 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              12 (('==',))
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              13 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (@py_assert2, text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('_strip_trailing_notes')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('_strip_trailing_notes')
    # |        L3:     LOAD_CONST               5 ('py1')
    # |                LOAD_CONST               6 ('text')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               6 ('text')
    # |        L6:     LOAD_CONST               7 ('py3')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py5')
    # |                LOAD_CONST               6 ('text')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               6 ('text')
    # |        L9:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format6)
    # |                LOAD_CONST               9 ('assert %(py7)s')
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_FAST_BORROW         5 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format8)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   52 (@py_assert2, @py_assert4)
    # |                LOAD_CONST              11 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_does_not_touch_em_dashes_in_prose at 0x755ee4a400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 245>:
    # | 245            RESUME                   0
    # | 247            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('_strip_trailing_notes',))
    # |                IMPORT_NAME              0 (novel_agent.agents.writer)
    # |                IMPORT_FROM              1 (_strip_trailing_notes)
    # |                STORE_FAST               1 (_strip_trailing_notes)
    # |                POP_TOP
    # | 249            LOAD_CONST               2 ('## 第1章 值班\n\n她想说什么——最终没有说。')
    # |                STORE_FAST               2 (text)
    # | 250            LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         2 (text)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       333 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              12 (('==',))
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              13 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (@py_assert2, text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('_strip_trailing_notes')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('_strip_trailing_notes')
    # |        L3:     LOAD_CONST               5 ('py1')
    # |                LOAD_CONST               6 ('text')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               6 ('text')
    # |        L6:     LOAD_CONST               7 ('py3')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py5')
    # |                LOAD_CONST               6 ('text')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               6 ('text')
    # |        L9:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format6)
    # |                LOAD_CONST               9 ('assert %(py7)s')
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_FAST_BORROW         5 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format8)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   52 (@py_assert2, @py_assert4)
    # |                LOAD_CONST              11 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_handles_other_separator_styles at 0x755ee4a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 252>:
    # | 252           RESUME                   0
    # | 253           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('_strip_trailing_notes',))
    # |               IMPORT_NAME              0 (novel_agent.agents.writer)
    # |               IMPORT_FROM              1 (_strip_trailing_notes)
    # |               STORE_FAST               1 (_strip_trailing_notes)
    # |               POP_TOP
    # | 255           LOAD_CONST              15 (('---', '***', '___', '-----'))
    # |               GET_ITER
    # |       L1:     EXTENDED_ARG             1
    # |               FOR_ITER               364 (to L9)
    # |               STORE_FAST               2 (sep)
    # | 256           LOAD_CONST               2 ('## 第1章 值班\n\n正文。\n\n')
    # |               LOAD_FAST_BORROW         2 (sep)
    # |               FORMAT_SIMPLE
    # |               LOAD_CONST               3 ('\n\n说明文字')
    # |               BUILD_STRING             3
    # |               STORE_FAST               3 (text)
    # | 257           LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (text)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               LOAD_ATTR                4 (endswith)
    # |               STORE_FAST               5 (@py_assert4)
    # |               LOAD_CONST               4 ('正文。')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert6, @py_assert4)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert6)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert8, @py_assert8)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       312 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (sep)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('\n>assert %(py9)s\n{%(py9)s = %(py5)s\n{%(py5)s = %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}.endswith\n}(%(py7)s)\n}')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               6 ('py0')
    # |               LOAD_CONST               7 ('_strip_trailing_notes')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (_strip_trailing_notes)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               7 ('_strip_trailing_notes')
    # |       L4:     LOAD_CONST               8 ('py1')
    # |               LOAD_CONST               9 ('text')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (text)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (text)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               9 ('text')
    # |       L7:     LOAD_CONST              10 ('py3')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py5')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py7')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert6)
    # |               CALL                     1
    # |               LOAD_CONST              13 ('py9')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                6
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format10)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST              14 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  103 (@py_assert6, @py_assert8)
    # |               EXTENDED_ARG             1
    # |               JUMP_BACKWARD          367 (to L1)
    # | 255   L9:     END_FOR
    # |               POP_ITER
    # |               LOAD_CONST              14 (None)
    # |               RETURN_VALUE

    def test_strips_from_the_separator(self):
        '## 第3章 问号那一处\n\n她转过身。\n\n---\n\n缝合说明：统一了年份。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 233           RESUME                   0
        # | 234           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('_strip_trailing_notes',))
        # |               IMPORT_NAME              0 (novel_agent.agents.writer)
        # |               IMPORT_FROM              1 (_strip_trailing_notes)
        # |               STORE_FAST               1 (_strip_trailing_notes)
        # |               POP_TOP
        # | 236           LOAD_CONST               2 ('## 第3章 问号那一处\n\n她转过身。\n\n---\n\n缝合说明：统一了年份。')
        # |               STORE_FAST               2 (text)
        # | 237           LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (text)
        # |               CALL                     1
        # |               STORE_FAST               3 (@py_assert2)
        # |               LOAD_CONST               3 ('## 第3章 问号那一处\n\n她转过身。')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert5, @py_assert2)
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       277 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              14 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert2, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST               5 ('_strip_trailing_notes')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('_strip_trailing_notes')
        # |       L3:     LOAD_CONST               6 ('py1')
        # |               LOAD_CONST               7 ('text')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (text)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (text)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               7 ('text')
        # |       L6:     LOAD_CONST               8 ('py3')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_CONST              10 ('assert %(py8)s')
        # |               LOAD_CONST              11 ('py8')
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format9)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              12 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert4, @py_assert5)
        # |               LOAD_CONST              12 (None)
        # |               RETURN_VALUE

    def test_keeps_chapters_that_have_no_notes(self):
        '## 第1章 值班\n\n她接下了那份稿子。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 239            RESUME                   0
        # | 240            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('_strip_trailing_notes',))
        # |                IMPORT_NAME              0 (novel_agent.agents.writer)
        # |                IMPORT_FROM              1 (_strip_trailing_notes)
        # |                STORE_FAST               1 (_strip_trailing_notes)
        # |                POP_TOP
        # | 242            LOAD_CONST               2 ('## 第1章 值班\n\n她接下了那份稿子。')
        # |                STORE_FAST               2 (text)
        # | 243            LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         2 (text)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       333 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              12 (('==',))
        # |                LOAD_FAST_BORROW         4 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              13 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (@py_assert2, text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('_strip_trailing_notes')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('_strip_trailing_notes')
        # |        L3:     LOAD_CONST               5 ('py1')
        # |                LOAD_CONST               6 ('text')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               6 ('text')
        # |        L6:     LOAD_CONST               7 ('py3')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py5')
        # |                LOAD_CONST               6 ('text')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               6 ('text')
        # |        L9:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format6)
        # |                LOAD_CONST               9 ('assert %(py7)s')
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_FAST_BORROW         5 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format8)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              11 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   52 (@py_assert2, @py_assert4)
        # |                LOAD_CONST              11 (None)
        # |                RETURN_VALUE

    def test_does_not_touch_em_dashes_in_prose(self):
        '正文里的 —— 是规范要求的破折号，不是分隔线。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 245            RESUME                   0
        # | 247            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('_strip_trailing_notes',))
        # |                IMPORT_NAME              0 (novel_agent.agents.writer)
        # |                IMPORT_FROM              1 (_strip_trailing_notes)
        # |                STORE_FAST               1 (_strip_trailing_notes)
        # |                POP_TOP
        # | 249            LOAD_CONST               2 ('## 第1章 值班\n\n她想说什么——最终没有说。')
        # |                STORE_FAST               2 (text)
        # | 250            LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         2 (text)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       333 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              12 (('==',))
        # |                LOAD_FAST_BORROW         4 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              13 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (@py_assert2, text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('_strip_trailing_notes')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('_strip_trailing_notes')
        # |        L3:     LOAD_CONST               5 ('py1')
        # |                LOAD_CONST               6 ('text')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               6 ('text')
        # |        L6:     LOAD_CONST               7 ('py3')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py5')
        # |                LOAD_CONST               6 ('text')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               6 ('text')
        # |        L9:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format6)
        # |                LOAD_CONST               9 ('assert %(py7)s')
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_FAST_BORROW         5 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format8)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              11 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   52 (@py_assert2, @py_assert4)
        # |                LOAD_CONST              11 (None)
        # |                RETURN_VALUE

    def test_handles_other_separator_styles(self):
        '## 第1章 值班\n\n正文。\n\n'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 252           RESUME                   0
        # | 253           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('_strip_trailing_notes',))
        # |               IMPORT_NAME              0 (novel_agent.agents.writer)
        # |               IMPORT_FROM              1 (_strip_trailing_notes)
        # |               STORE_FAST               1 (_strip_trailing_notes)
        # |               POP_TOP
        # | 255           LOAD_CONST              15 (('---', '***', '___', '-----'))
        # |               GET_ITER
        # |       L1:     EXTENDED_ARG             1
        # |               FOR_ITER               364 (to L9)
        # |               STORE_FAST               2 (sep)
        # | 256           LOAD_CONST               2 ('## 第1章 值班\n\n正文。\n\n')
        # |               LOAD_FAST_BORROW         2 (sep)
        # |               FORMAT_SIMPLE
        # |               LOAD_CONST               3 ('\n\n说明文字')
        # |               BUILD_STRING             3
        # |               STORE_FAST               3 (text)
        # | 257           LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (text)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               LOAD_ATTR                4 (endswith)
        # |               STORE_FAST               5 (@py_assert4)
        # |               LOAD_CONST               4 ('正文。')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert6, @py_assert4)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert6)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert8, @py_assert8)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       312 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (sep)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('\n>assert %(py9)s\n{%(py9)s = %(py5)s\n{%(py5)s = %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}.endswith\n}(%(py7)s)\n}')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               6 ('py0')
        # |               LOAD_CONST               7 ('_strip_trailing_notes')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (_strip_trailing_notes)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               7 ('_strip_trailing_notes')
        # |       L4:     LOAD_CONST               8 ('py1')
        # |               LOAD_CONST               9 ('text')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (text)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (text)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               9 ('text')
        # |       L7:     LOAD_CONST              10 ('py3')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py5')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py7')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert6)
        # |               CALL                     1
        # |               LOAD_CONST              13 ('py9')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                6
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format10)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST              14 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  103 (@py_assert6, @py_assert8)
        # |               EXTENDED_ARG             1
        # |               JUMP_BACKWARD          367 (to L1)
        # | 255   L9:     END_FOR
        # |               POP_ITER
        # |               LOAD_CONST              14 (None)
        # |               RETURN_VALUE


class TestQuoteNormalisation:
    'TestQuoteNormalisation'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 260           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestQuoteNormalisation')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_CONST               1 (260)
    # |               STORE_NAME               3 (__firstlineno__)
    # | 261           LOAD_CONST               2 ('两次事故都出在 ASCII 引号上：一轮修订后整章冒出 46 处 `"`，gate 全判错；\n更早一次「整章对话占比 0.0%」也是它 —— 对话占比只认全角引号。')
    # |               STORE_NAME               4 (__doc__)
    # | 264           LOAD_CONST               3 (<code object test_pairs_are_opened_and_closed at 0x755ee4d500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 264>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_pairs_are_opened_and_closed)
    # | 269           LOAD_CONST               4 (<code object test_pairing_resets_each_line at 0x755ed5b480, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 269>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_pairing_resets_each_line)
    # | 276           LOAD_CONST               5 (<code object test_single_quotes_are_left_alone at 0x755ee4d800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 276>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_single_quotes_are_left_alone)
    # | 282           LOAD_CONST               6 (<code object test_postprocess_strips_before_normalising at 0x755ed5b980, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 282>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_postprocess_strips_before_normalising)
    # | 289           LOAD_CONST               7 (<code object test_ellipsis_and_dashes_are_normalised at 0x755ed61e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 289>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_ellipsis_and_dashes_are_normalised)
    # |               LOAD_CONST               8 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_pairs_are_opened_and_closed at 0x755ee4d500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 264>:
    # | 264           RESUME                   0
    # | 265           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('_normalize_quotes',))
    # |               IMPORT_NAME              0 (novel_agent.agents.writer)
    # |               IMPORT_FROM              1 (_normalize_quotes)
    # |               STORE_FAST               1 (_normalize_quotes)
    # |               POP_TOP
    # | 267           LOAD_CONST               2 ('她说"我知道了"。')
    # |               STORE_FAST_LOAD_FAST    33 (@py_assert1, _normalize_quotes)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               LOAD_CONST               3 ('她说“我知道了”。')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       221 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST               5 ('_normalize_quotes')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (_normalize_quotes)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (_normalize_quotes)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('_normalize_quotes')
    # |       L3:     LOAD_CONST               6 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_CONST               9 ('assert %(py9)s')
    # |               LOAD_CONST              10 ('py9')
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format10)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert5, @py_assert6)
    # |               LOAD_CONST              11 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_pairing_resets_each_line at 0x755ed5b480, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 269>:
    # | 269           RESUME                   0
    # | 271           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('_normalize_quotes',))
    # |               IMPORT_NAME              0 (novel_agent.agents.writer)
    # |               IMPORT_FROM              1 (_normalize_quotes)
    # |               STORE_FAST               1 (_normalize_quotes)
    # |               POP_TOP
    # | 273           LOAD_FAST_BORROW         1 (_normalize_quotes)
    # |               PUSH_NULL
    # |               LOAD_CONST               2 ('"第一句"\n"第二句"')
    # |               CALL                     1
    # |               STORE_FAST               2 (got)
    # | 274           LOAD_CONST               3 ('“第一句”\n“第二句”')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert2, got)
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py0)s == %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (got, @py_assert2)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST               5 ('got')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (got)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (got)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('got')
    # |       L3:     LOAD_CONST               6 ('py3')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format4)
    # |               LOAD_CONST               7 ('assert %(py5)s')
    # |               LOAD_CONST               8 ('py5')
    # |               LOAD_FAST_BORROW         5 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert1, @py_assert2)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_single_quotes_are_left_alone at 0x755ee4d800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 276>:
    # | 276           RESUME                   0
    # | 278           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('_normalize_quotes',))
    # |               IMPORT_NAME              0 (novel_agent.agents.writer)
    # |               IMPORT_FROM              1 (_normalize_quotes)
    # |               STORE_FAST               1 (_normalize_quotes)
    # |               POP_TOP
    # | 280           LOAD_CONST               2 ("don't")
    # |               STORE_FAST_LOAD_FAST    33 (@py_assert1, _normalize_quotes)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               LOAD_CONST               2 ("don't")
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       221 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('_normalize_quotes')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (_normalize_quotes)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (_normalize_quotes)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('_normalize_quotes')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py7')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_CONST               8 ('assert %(py9)s')
    # |               LOAD_CONST               9 ('py9')
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format10)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert5, @py_assert6)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_postprocess_strips_before_normalising at 0x755ed5b980, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 282>:
    # | 282           RESUME                   0
    # | 284           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('_postprocess',))
    # |               IMPORT_NAME              0 (novel_agent.agents.writer)
    # |               IMPORT_FROM              1 (_postprocess)
    # |               STORE_FAST               1 (_postprocess)
    # |               POP_TOP
    # | 286           LOAD_FAST_BORROW         1 (_postprocess)
    # |               PUSH_NULL
    # |               LOAD_CONST               2 ('## 第1章 值班\n\n正文。\n\n---\n\n缝合说明：略。')
    # |               CALL                     1
    # |               STORE_FAST               2 (got)
    # | 287           LOAD_CONST               3 ('## 第1章 值班\n\n正文。')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert2, got)
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py0)s == %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (got, @py_assert2)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST               5 ('got')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (got)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (got)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('got')
    # |       L3:     LOAD_CONST               6 ('py3')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format4)
    # |               LOAD_CONST               7 ('assert %(py5)s')
    # |               LOAD_CONST               8 ('py5')
    # |               LOAD_FAST_BORROW         5 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert1, @py_assert2)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_ellipsis_and_dashes_are_normalised at 0x755ed61e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_writer.py", line 289>:
    # | 289            RESUME                   0
    # | 290            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('_postprocess',))
    # |                IMPORT_NAME              0 (novel_agent.agents.writer)
    # |                IMPORT_FROM              1 (_postprocess)
    # |                STORE_FAST               1 (_postprocess)
    # |                POP_TOP
    # | 292            LOAD_FAST_BORROW         1 (_postprocess)
    # |                PUSH_NULL
    # |                LOAD_CONST               2 ('她没说话...他也是--两个人就这么站着。')
    # |                CALL                     1
    # |                STORE_FAST               2 (got)
    # | 293            BUILD_LIST               0
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_CONST               3 ('……')
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert0, @py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       22 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_CONST               4 ('——')
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert9, @py_assert9)
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert11, @py_assert11)
    # |                STORE_FAST_LOAD_FAST   104 (@py_assert0, @py_assert11)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        8 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_CONST               5 ('...')
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert16, @py_assert16)
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert18, @py_assert18)
    # |                STORE_FAST               6 (@py_assert0)
    # |        L1:     LOAD_FAST_BORROW         6 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             2
    # |                POP_JUMP_IF_TRUE       576 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 (('in',))
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              23 (('%(py3)s in %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (@py_assert2, got)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               6 ('py3')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                8 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py5')
    # |                LOAD_CONST               8 ('got')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                8 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST               8 ('got')
    # |        L4:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format6)
    # |                LOAD_CONST               9 ('%(py7)s')
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_FAST_BORROW        11 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   195 (@py_format8, @py_assert1)
    # |                LOAD_ATTR               17 (append + NULL|self)
    # |                LOAD_FAST_BORROW        12 (@py_format8)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_FALSE      334 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 (('in',))
    # |                LOAD_FAST_CHECK          8 (@py_assert11)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              24 (('%(py10)s in %(py12)s',))
    # |                LOAD_FAST_CHECK          7 (@py_assert9)
    # |                LOAD_FAST_BORROW         2 (got)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              11 ('py10')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                8 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py12')
    # |                LOAD_CONST               8 ('got')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                8 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               8 ('got')
    # |        L7:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format13)
    # |                LOAD_CONST              13 ('%(py14)s')
    # |                LOAD_CONST              14 ('py14')
    # |                LOAD_FAST_BORROW        13 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   227 (@py_format15, @py_assert1)
    # |                LOAD_ATTR               17 (append + NULL|self)
    # |                LOAD_FAST_BORROW        14 (@py_format15)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW         8 (@py_assert11)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      164 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              25 (('not in',))
    # |                LOAD_FAST_CHECK         10 (@py_assert18)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              26 (('%(py17)s not in %(py19)s',))
    # |                LOAD_FAST_CHECK          9 (@py_assert16)
    # |                LOAD_FAST_BORROW         2 (got)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              15 ('py17')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                8 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert16)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py19')
    # |                LOAD_CONST               8 ('got')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                8 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (got)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               8 ('got')
    # |       L10:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format20)
    # |                LOAD_CONST              17 ('%(py21)s')
    # |                LOAD_CONST              18 ('py21')
    # |                LOAD_FAST_BORROW        15 (@py_format20)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format22)
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                LOAD_ATTR               17 (append + NULL|self)
    # |                LOAD_FAST_BORROW        16 (@py_format22)
    # |                CALL                     1
    # |                POP_TOP
    # |       L11:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format23)
    # |                LOAD_CONST              19 ('assert %(py24)s')
    # |                LOAD_CONST              20 ('py24')
    # |                LOAD_FAST_BORROW        17 (@py_format23)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format25)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        18 (@py_format25)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L12:     LOAD_CONST              21 (None)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert9)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert11)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  154 (@py_assert16, @py_assert18)
    # |                LOAD_CONST              21 (None)
    # |                RETURN_VALUE

    def test_pairs_are_opened_and_closed(self):
        '她说"我知道了"。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 264           RESUME                   0
        # | 265           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('_normalize_quotes',))
        # |               IMPORT_NAME              0 (novel_agent.agents.writer)
        # |               IMPORT_FROM              1 (_normalize_quotes)
        # |               STORE_FAST               1 (_normalize_quotes)
        # |               POP_TOP
        # | 267           LOAD_CONST               2 ('她说"我知道了"。')
        # |               STORE_FAST_LOAD_FAST    33 (@py_assert1, _normalize_quotes)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               LOAD_CONST               3 ('她说“我知道了”。')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       221 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST               5 ('_normalize_quotes')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (_normalize_quotes)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (_normalize_quotes)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('_normalize_quotes')
        # |       L3:     LOAD_CONST               6 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_CONST               9 ('assert %(py9)s')
        # |               LOAD_CONST              10 ('py9')
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format10)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert5, @py_assert6)
        # |               LOAD_CONST              11 (None)
        # |               RETURN_VALUE

    def test_pairing_resets_each_line(self):
        '对话跨段时一行里的引号常常不闭合，跨行累计会把后面全弄反。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 269           RESUME                   0
        # | 271           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('_normalize_quotes',))
        # |               IMPORT_NAME              0 (novel_agent.agents.writer)
        # |               IMPORT_FROM              1 (_normalize_quotes)
        # |               STORE_FAST               1 (_normalize_quotes)
        # |               POP_TOP
        # | 273           LOAD_FAST_BORROW         1 (_normalize_quotes)
        # |               PUSH_NULL
        # |               LOAD_CONST               2 ('"第一句"\n"第二句"')
        # |               CALL                     1
        # |               STORE_FAST               2 (got)
        # | 274           LOAD_CONST               3 ('“第一句”\n“第二句”')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert2, got)
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       177 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py0)s == %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (got, @py_assert2)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST               5 ('got')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (got)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (got)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('got')
        # |       L3:     LOAD_CONST               6 ('py3')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format4)
        # |               LOAD_CONST               7 ('assert %(py5)s')
        # |               LOAD_CONST               8 ('py5')
        # |               LOAD_FAST_BORROW         5 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert1, @py_assert2)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_single_quotes_are_left_alone(self):
        '英文缩写里的撇号会被误伤。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 276           RESUME                   0
        # | 278           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('_normalize_quotes',))
        # |               IMPORT_NAME              0 (novel_agent.agents.writer)
        # |               IMPORT_FROM              1 (_normalize_quotes)
        # |               STORE_FAST               1 (_normalize_quotes)
        # |               POP_TOP
        # | 280           LOAD_CONST               2 ("don't")
        # |               STORE_FAST_LOAD_FAST    33 (@py_assert1, _normalize_quotes)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               LOAD_CONST               2 ("don't")
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       221 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('_normalize_quotes')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (_normalize_quotes)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (_normalize_quotes)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('_normalize_quotes')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py7')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_CONST               8 ('assert %(py9)s')
        # |               LOAD_CONST               9 ('py9')
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format10)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert5, @py_assert6)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE

    def test_postprocess_strips_before_normalising(self):
        '顺序反了的话 `---` 会先被规范化成 `——-`，剥离规则就匹配不上。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 282           RESUME                   0
        # | 284           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('_postprocess',))
        # |               IMPORT_NAME              0 (novel_agent.agents.writer)
        # |               IMPORT_FROM              1 (_postprocess)
        # |               STORE_FAST               1 (_postprocess)
        # |               POP_TOP
        # | 286           LOAD_FAST_BORROW         1 (_postprocess)
        # |               PUSH_NULL
        # |               LOAD_CONST               2 ('## 第1章 值班\n\n正文。\n\n---\n\n缝合说明：略。')
        # |               CALL                     1
        # |               STORE_FAST               2 (got)
        # | 287           LOAD_CONST               3 ('## 第1章 值班\n\n正文。')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert2, got)
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       177 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py0)s == %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (got, @py_assert2)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST               5 ('got')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (got)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (got)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('got')
        # |       L3:     LOAD_CONST               6 ('py3')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format4)
        # |               LOAD_CONST               7 ('assert %(py5)s')
        # |               LOAD_CONST               8 ('py5')
        # |               LOAD_FAST_BORROW         5 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert1, @py_assert2)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_ellipsis_and_dashes_are_normalised(self):
        '她没说话...他也是--两个人就这么站着。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 289            RESUME                   0
        # | 290            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('_postprocess',))
        # |                IMPORT_NAME              0 (novel_agent.agents.writer)
        # |                IMPORT_FROM              1 (_postprocess)
        # |                STORE_FAST               1 (_postprocess)
        # |                POP_TOP
        # | 292            LOAD_FAST_BORROW         1 (_postprocess)
        # |                PUSH_NULL
        # |                LOAD_CONST               2 ('她没说话...他也是--两个人就这么站着。')
        # |                CALL                     1
        # |                STORE_FAST               2 (got)
        # | 293            BUILD_LIST               0
        # |                STORE_FAST               3 (@py_assert1)
        # |                LOAD_CONST               3 ('……')
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert0, @py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       22 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_CONST               4 ('——')
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert9, @py_assert9)
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert11, @py_assert11)
        # |                STORE_FAST_LOAD_FAST   104 (@py_assert0, @py_assert11)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE        8 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_CONST               5 ('...')
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert16, @py_assert16)
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert18, @py_assert18)
        # |                STORE_FAST               6 (@py_assert0)
        # |        L1:     LOAD_FAST_BORROW         6 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             2
        # |                POP_JUMP_IF_TRUE       576 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              22 (('in',))
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              23 (('%(py3)s in %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (@py_assert2, got)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               6 ('py3')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                8 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py5')
        # |                LOAD_CONST               8 ('got')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                8 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST               8 ('got')
        # |        L4:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format6)
        # |                LOAD_CONST               9 ('%(py7)s')
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_FAST_BORROW        11 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   195 (@py_format8, @py_assert1)
        # |                LOAD_ATTR               17 (append + NULL|self)
        # |                LOAD_FAST_BORROW        12 (@py_format8)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_FALSE      334 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              22 (('in',))
        # |                LOAD_FAST_CHECK          8 (@py_assert11)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              24 (('%(py10)s in %(py12)s',))
        # |                LOAD_FAST_CHECK          7 (@py_assert9)
        # |                LOAD_FAST_BORROW         2 (got)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              11 ('py10')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                8 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert9)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py12')
        # |                LOAD_CONST               8 ('got')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                8 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               8 ('got')
        # |        L7:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format13)
        # |                LOAD_CONST              13 ('%(py14)s')
        # |                LOAD_CONST              14 ('py14')
        # |                LOAD_FAST_BORROW        13 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   227 (@py_format15, @py_assert1)
        # |                LOAD_ATTR               17 (append + NULL|self)
        # |                LOAD_FAST_BORROW        14 (@py_format15)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW         8 (@py_assert11)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      164 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              25 (('not in',))
        # |                LOAD_FAST_CHECK         10 (@py_assert18)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              26 (('%(py17)s not in %(py19)s',))
        # |                LOAD_FAST_CHECK          9 (@py_assert16)
        # |                LOAD_FAST_BORROW         2 (got)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              15 ('py17')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                8 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert16)
        # |                CALL                     1
        # |                LOAD_CONST              16 ('py19')
        # |                LOAD_CONST               8 ('got')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                8 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (got)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               8 ('got')
        # |       L10:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format20)
        # |                LOAD_CONST              17 ('%(py21)s')
        # |                LOAD_CONST              18 ('py21')
        # |                LOAD_FAST_BORROW        15 (@py_format20)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format22)
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                LOAD_ATTR               17 (append + NULL|self)
        # |                LOAD_FAST_BORROW        16 (@py_format22)
        # |                CALL                     1
        # |                POP_TOP
        # |       L11:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format23)
        # |                LOAD_CONST              19 ('assert %(py24)s')
        # |                LOAD_CONST              20 ('py24')
        # |                LOAD_FAST_BORROW        17 (@py_format23)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format25)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        18 (@py_format25)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L12:     LOAD_CONST              21 (None)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert9)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert11)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  154 (@py_assert16, @py_assert18)
        # |                LOAD_CONST              21 (None)
        # |                RETURN_VALUE

