# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py
# 来源   : test_graph.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = 'LangGraph 编排。\n\n图层相对 pipeline 的唯一实质增益是**章内断点**：一章要跑 6-8 次调用、\n十几分钟，缝合阶段崩了不该让前面写好的场景作废。\n所以测试重点是节点连线与分支是否正确，不是生成质量。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'LangGraph 编排。\n\n图层相对 pipeline 的唯一实质增益是**章内断点**：一章要跑 6-8 次调用、\n十几分钟，缝合阶段崩了不该让前面写好的场景作废。\n所以测试重点是节点连线与分支是否正确，不是生成质量。\n',
    8: 'config',
    9: 'project.yaml',
    16: 'TestHappyPath',
    18: 'TestRevisionRouting',
    20: 'TestSerializability',
    22: 'TestCheckpointResume',
    24: 'TestChapterResultView',
    26: 'TestVolumeCompressionInGraph',
    28: 'TestArchiveFailureInGraph',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('make', 2): '场景一',
    ('make', 3): '场景二',
    ('seed', 0): 'ch',
    ('seed', 1): 'story',
    ('seed', 2): 'volume',
    ('seed', 3): 'note',
    ('TestHappyPath', 0): 'TestHappyPath',
    ('test_reaches_archive', 0): 'done_reason',
    ('test_reaches_archive', 1): 'passed',
    ('test_reaches_archive', 2): 'py1',
    ('test_reaches_archive', 3): 'py4',
    ('test_reaches_archive', 4): 'assert %(py6)s',
    ('test_reaches_archive', 5): 'py6',
    ('test_reaches_archive', 7): 'revisions',
    ('test_reaches_archive', 8): 'py0',
    ('test_reaches_archive', 9): 'a',
    ('test_reaches_archive', 10): 'py2',
    ('test_reaches_archive', 11): 'py5',
    ('test_reaches_archive', 12): 'assert %(py7)s',
    ('test_reaches_archive', 13): 'py7',
    ('test_reaches_archive', 14): 'w',
    ('test_state_advances_in_graph', 0): 'patch',
    ('test_state_advances_in_graph', 2): 'py1',
    ('test_state_advances_in_graph', 3): 'py4',
    ('test_state_advances_in_graph', 4): 'assert %(py6)s',
    ('test_state_advances_in_graph', 5): 'py6',
    ('test_state_advances_in_graph', 6): 'story',
    ('test_state_advances_in_graph', 7): 'chapter_summaries',
    ('test_state_advances_in_graph', 8): 'ch',
    ('test_state_advances_in_graph', 9): 'py3',
    ('test_state_advances_in_graph', 10): 'chs',
    ('test_state_advances_in_graph', 11): 'assert %(py5)s',
    ('test_state_advances_in_graph', 12): 'py5',
    ('TestRevisionRouting', 0): 'TestRevisionRouting',
    ('test_gate_failure_routes_to_revise', 0): 'done_reason',
    ('test_gate_failure_routes_to_revise', 1): 'passed',
    ('test_gate_failure_routes_to_revise', 2): 'py1',
    ('test_gate_failure_routes_to_revise', 3): 'py4',
    ('test_gate_failure_routes_to_revise', 4): 'assert %(py6)s',
    ('test_gate_failure_routes_to_revise', 5): 'py6',
    ('test_gate_failure_routes_to_revise', 7): 'revisions',
    ('test_gate_failure_routes_to_revise', 8): '应当重写过场景',
    ('test_gate_failure_routes_to_revise', 9): '\n>assert %(py2)s\n{%(py2)s = %(py0)s.revised\n}',
    ('test_gate_failure_routes_to_revise', 10): 'py0',
    ('test_gate_failure_routes_to_revise', 11): 'w',
    ('test_gate_failure_routes_to_revise', 12): 'py2',
    ('test_judge_failure_routes_to_revise', 0): 'revisions',
    ('test_judge_failure_routes_to_revise', 1): 'done_reason',
    ('test_judge_failure_routes_to_revise', 2): 'passed',
    ('test_judge_failure_routes_to_revise', 3): 'py3',
    ('test_judge_failure_routes_to_revise', 4): 'py6',
    ('test_judge_failure_routes_to_revise', 5): '%(py8)s',
    ('test_judge_failure_routes_to_revise', 6): 'py8',
    ('test_judge_failure_routes_to_revise', 7): 'py11',
    ('test_judge_failure_routes_to_revise', 8): 'py14',
    ('test_judge_failure_routes_to_revise', 9): '%(py16)s',
    ('test_judge_failure_routes_to_revise', 10): 'py16',
    ('test_judge_failure_routes_to_revise', 11): 'assert %(py19)s',
    ('test_judge_failure_routes_to_revise', 12): 'py19',
    ('test_revise_goes_back_through_stitch', 0): '重写的是场景，缝合必须重做 —— 否则改动不会进入成稿。',
    ('test_revise_goes_back_through_stitch', 1): 'text',
    ('test_revise_goes_back_through_stitch', 2): 'py1',
    ('test_revise_goes_back_through_stitch', 3): 'py3',
    ('test_revise_goes_back_through_stitch', 4): 'GOOD',
    ('test_revise_goes_back_through_stitch', 5): 'assert %(py5)s',
    ('test_revise_goes_back_through_stitch', 6): 'py5',
    ('test_gives_up_at_limit', 2): 'revisions',
    ('test_gives_up_at_limit', 3): 'py1',
    ('test_gives_up_at_limit', 4): 'py4',
    ('test_gives_up_at_limit', 5): 'assert %(py6)s',
    ('test_gives_up_at_limit', 6): 'py6',
    ('test_gives_up_at_limit', 8): '仍未通过',
    ('test_gives_up_at_limit', 9): 'done_reason',
    ('test_gives_up_at_limit', 10): 'py0',
    ('test_gives_up_at_limit', 11): 'a',
    ('test_gives_up_at_limit', 12): 'py2',
    ('test_gives_up_at_limit', 13): 'py5',
    ('test_gives_up_at_limit', 14): '未通过不得归档',
    ('test_gives_up_at_limit', 15): '\n>assert %(py7)s',
    ('test_gives_up_at_limit', 16): 'py7',
    ('test_judge_not_run_when_gate_fails', 2): 'verdict',
    ('test_judge_not_run_when_gate_fails', 4): 'py0',
    ('test_judge_not_run_when_gate_fails', 5): 'out',
    ('test_judge_not_run_when_gate_fails', 6): 'py2',
    ('test_judge_not_run_when_gate_fails', 7): 'py4',
    ('test_judge_not_run_when_gate_fails', 8): 'py6',
    ('test_judge_not_run_when_gate_fails', 9): 'py9',
    ('test_judge_not_run_when_gate_fails', 10): 'assert %(py11)s',
    ('test_judge_not_run_when_gate_fails', 11): 'py11',
    ('TestSerializability', 0): 'TestSerializability',
    ('TestSerializability', 1): '状态要能存进 sqlite，否则断点续跑无从谈起。',
    ('test_state_is_json_serializable', 2): '_',
    ('test_state_is_json_serializable', 5): 'assert %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.dumps\n}(%(py3)s, ensure_ascii=%(py5)s)\n}',
    ('test_state_is_json_serializable', 6): 'py0',
    ('test_state_is_json_serializable', 7): 'json',
    ('test_state_is_json_serializable', 8): 'py2',
    ('test_state_is_json_serializable', 9): 'py3',
    ('test_state_is_json_serializable', 10): 'payload',
    ('test_state_is_json_serializable', 11): 'py5',
    ('test_state_is_json_serializable', 12): 'py7',
    ('TestCheckpointResume', 0): 'TestCheckpointResume',
    ('TestCheckpointResume', 1): '图层存在的唯一理由。第 3 章两次崩在缝合，没有 checkpoint 就得从出细纲\n重来 —— 三场写好的正文（$0.07）连同十几分钟一起作废。',
    ('_pipeline', 2): 'architect',
    ('_pipeline', 3): 'writer',
    ('_pipeline', 4): '场景一',
    ('_pipeline', 5): '场景二',
    ('_pipeline', 6): 'stitcher',
    ('_pipeline', 7): 'gate',
    ('_pipeline', 8): 'judge',
    ('_pipeline', 9): 'archivist',
    ('_pipeline', 10): 'max_revisions',
    ('_pipeline', 11): 'log',
    ('test_resumes_at_the_node_that_crashed', 3): 'FlakyStitcher',
    ('test_resumes_at_the_node_that_crashed', 4): 'cp.sqlite',
    ('test_resumes_at_the_node_that_crashed', 5): 'configurable',
    ('test_resumes_at_the_node_that_crashed', 6): 'thread_id',
    ('test_resumes_at_the_node_that_crashed', 7): 't1',
    ('test_resumes_at_the_node_that_crashed', 9): 'py0',
    ('test_resumes_at_the_node_that_crashed', 10): 'g',
    ('test_resumes_at_the_node_that_crashed', 11): 'py2',
    ('test_resumes_at_the_node_that_crashed', 12): 'py3',
    ('test_resumes_at_the_node_that_crashed', 13): 'cfg',
    ('test_resumes_at_the_node_that_crashed', 14): 'py5',
    ('test_resumes_at_the_node_that_crashed', 15): 'py7',
    ('test_resumes_at_the_node_that_crashed', 16): 'py10',
    ('test_resumes_at_the_node_that_crashed', 17): '该停在崩掉的那个节点前',
    ('test_resumes_at_the_node_that_crashed', 18): '\n>assert %(py12)s',
    ('test_resumes_at_the_node_that_crashed', 19): 'py12',
    ('test_resumes_at_the_node_that_crashed', 20): 'done_reason',
    ('test_resumes_at_the_node_that_crashed', 21): 'passed',
    ('test_resumes_at_the_node_that_crashed', 22): 'py1',
    ('test_resumes_at_the_node_that_crashed', 23): 'py4',
    ('test_resumes_at_the_node_that_crashed', 24): 'assert %(py6)s',
    ('test_resumes_at_the_node_that_crashed', 25): 'py6',
    ('test_resumes_at_the_node_that_crashed', 26): 'p',
    ('test_resumes_at_the_node_that_crashed', 27): '续跑不该重出细纲',
    ('test_resumes_at_the_node_that_crashed', 28): '\n>assert %(py9)s',
    ('test_resumes_at_the_node_that_crashed', 29): 'py9',
    ('test_resumes_at_the_node_that_crashed', 30): '续跑不该重写场景',
    ('test_resumes_at_the_node_that_crashed', 31): 'st',
    ('test_resumes_at_the_node_that_crashed', 32): 'assert %(py7)s',
    ('FlakyStitcher', 0): 'TestCheckpointResume.test_resumes_at_the_node_that_crashed.<locals>.FlakyStitcher',
    ('stitch', 1): '上游 403',
    ('test_a_finished_chapter_has_nothing_left_to_run', 3): 'OkStitcher',
    ('test_a_finished_chapter_has_nothing_left_to_run', 4): 'cp.sqlite',
    ('test_a_finished_chapter_has_nothing_left_to_run', 5): 'configurable',
    ('test_a_finished_chapter_has_nothing_left_to_run', 6): 'thread_id',
    ('test_a_finished_chapter_has_nothing_left_to_run', 7): 't2',
    ('test_a_finished_chapter_has_nothing_left_to_run', 8): 'py0',
    ('test_a_finished_chapter_has_nothing_left_to_run', 9): 'g',
    ('test_a_finished_chapter_has_nothing_left_to_run', 10): 'py2',
    ('test_a_finished_chapter_has_nothing_left_to_run', 11): 'py3',
    ('test_a_finished_chapter_has_nothing_left_to_run', 12): 'cfg',
    ('test_a_finished_chapter_has_nothing_left_to_run', 13): 'py5',
    ('test_a_finished_chapter_has_nothing_left_to_run', 14): 'py7',
    ('test_a_finished_chapter_has_nothing_left_to_run', 15): 'py10',
    ('test_a_finished_chapter_has_nothing_left_to_run', 16): '跑完的章节不该被当成中断',
    ('test_a_finished_chapter_has_nothing_left_to_run', 17): '\n>assert %(py12)s',
    ('test_a_finished_chapter_has_nothing_left_to_run', 18): 'py12',
    ('OkStitcher', 0): 'TestCheckpointResume.test_a_finished_chapter_has_nothing_left_to_run.<locals>.OkStitcher',
    ('test_each_chapter_is_its_own_thread', 0): '同一个 db 里两章互不干扰，否则第 4 章会捡起第 3 章的残局。',
    ('test_each_chapter_is_its_own_thread', 3): 'OkStitcher',
    ('test_each_chapter_is_its_own_thread', 5): 'cp.sqlite',
    ('test_each_chapter_is_its_own_thread', 7): 'configurable',
    ('test_each_chapter_is_its_own_thread', 8): 'thread_id',
    ('test_each_chapter_is_its_own_thread', 9): 'ch1',
    ('test_each_chapter_is_its_own_thread', 10): 'ch2',
    ('test_each_chapter_is_its_own_thread', 11): 'py0',
    ('test_each_chapter_is_its_own_thread', 12): 'g',
    ('test_each_chapter_is_its_own_thread', 13): 'py2',
    ('test_each_chapter_is_its_own_thread', 14): 'py4',
    ('test_each_chapter_is_its_own_thread', 15): 'py6',
    ('test_each_chapter_is_its_own_thread', 16): 'py8',
    ('test_each_chapter_is_its_own_thread', 17): 'py11',
    ('test_each_chapter_is_its_own_thread', 18): 'assert %(py13)s',
    ('test_each_chapter_is_its_own_thread', 19): 'py13',
    ('OkStitcher', 0): 'TestCheckpointResume.test_each_chapter_is_its_own_thread.<locals>.OkStitcher',
    ('test_state_survives_a_real_sqlite_roundtrip', 0): 'GateReport 这类对象曾被塞进图状态；checkpoint 一序列化就可能炸，\n而这条路径上最不该出岔子的就是存档本身。',
    ('test_state_survives_a_real_sqlite_roundtrip', 3): 'OkStitcher',
    ('test_state_survives_a_real_sqlite_roundtrip', 4): 'cp.sqlite',
    ('test_state_survives_a_real_sqlite_roundtrip', 5): 'configurable',
    ('test_state_survives_a_real_sqlite_roundtrip', 6): 'thread_id',
    ('test_state_survives_a_real_sqlite_roundtrip', 7): 't3',
    ('test_state_survives_a_real_sqlite_roundtrip', 9): 'done_reason',
    ('test_state_survives_a_real_sqlite_roundtrip', 10): 'passed',
    ('test_state_survives_a_real_sqlite_roundtrip', 11): 'py1',
    ('test_state_survives_a_real_sqlite_roundtrip', 12): 'py4',
    ('test_state_survives_a_real_sqlite_roundtrip', 13): 'assert %(py6)s',
    ('test_state_survives_a_real_sqlite_roundtrip', 14): 'py6',
    ('test_state_survives_a_real_sqlite_roundtrip', 16): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_state_survives_a_real_sqlite_roundtrip', 17): 'py0',
    ('test_state_survives_a_real_sqlite_roundtrip', 18): 'all',
    ('test_state_survives_a_real_sqlite_roundtrip', 19): 'py2',
    ('OkStitcher', 0): 'TestCheckpointResume.test_state_survives_a_real_sqlite_roundtrip.<locals>.OkStitcher',
    ('<genexpr>', 0): '_',
    ('TestChapterResultView', 0): 'TestChapterResultView',
    ('TestChapterResultView', 1): 'CLI 只认一套结果接口，两条路径才能共用同一段落盘/归档/报错代码。',
    ('test_maps_a_passing_run', 3): 'a',
    ('test_maps_a_passing_run', 4): 'b',
    ('test_maps_a_passing_run', 7): '%(py4)s\n{%(py4)s = %(py2)s.passed\n}',
    ('test_maps_a_passing_run', 8): 'py2',
    ('test_maps_a_passing_run', 9): 'view',
    ('test_maps_a_passing_run', 10): 'py4',
    ('test_maps_a_passing_run', 11): 'py6',
    ('test_maps_a_passing_run', 12): 'py8',
    ('test_maps_a_passing_run', 13): 'py11',
    ('test_maps_a_passing_run', 14): '%(py13)s',
    ('test_maps_a_passing_run', 15): 'py13',
    ('test_maps_a_passing_run', 16): 'assert %(py16)s',
    ('test_maps_a_passing_run', 17): 'py16',
    ('test_maps_a_passing_run', 19): 'py0',
    ('test_maps_a_passing_run', 20): 'GOOD',
    ('test_maps_a_passing_run', 21): 'assert %(py6)s',
    ('test_maps_a_passing_run', 22): 'py5',
    ('test_maps_a_passing_run', 23): 'assert %(py7)s',
    ('test_maps_a_passing_run', 24): 'py7',
    ('test_maps_a_passing_run', 25): 'gate 报告要能重算出来（它不进 checkpoint）',
    ('test_maps_a_passing_run', 26): '\n>assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}',
    ('test_maps_a_passing_run', 28): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_maps_a_passing_run', 29): 'any',
    ('test_maps_a_failing_run', 4): 'a',
    ('test_maps_a_failing_run', 5): 'b',
    ('test_maps_a_failing_run', 8): 'assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_maps_a_failing_run', 9): 'py0',
    ('test_maps_a_failing_run', 10): 'view',
    ('test_maps_a_failing_run', 11): 'py2',
    ('test_maps_a_failing_run', 13): '仍未通过',
    ('test_maps_a_failing_run', 14): 'py1',
    ('test_maps_a_failing_run', 15): 'py4',
    ('test_maps_a_failing_run', 16): 'assert %(py6)s',
    ('test_maps_a_failing_run', 17): 'py6',
    ('test_maps_a_failing_run', 18): 'assert not %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}',
    ('TestVolumeCompressionInGraph', 0): 'TestVolumeCompressionInGraph',
    ('TestVolumeCompressionInGraph', 1): '两条路径行为必须一致，否则走图那条会悄悄少做一件事。',
    ('_graph', 4): '卷末',
    ('_graph', 5): '大学',
    ('_graph', 6): '收束',
    ('_graph', 7): 'ch',
    ('_graph', 8): '03d',
    ('_graph', 9): '_s1',
    ('_graph', 10): '_s2',
    ('_graph', 11): '下一卷',
    ('_graph', 14): 'Arch',
    ('_graph', 15): '场景一',
    ('_graph', 16): '场景二',
    ('Arch', 0): 'TestVolumeCompressionInGraph._graph.<locals>.Arch',
    ('Arch', 1): 'ch',
    ('Arch', 2): 'note',
    ('test_triggered_at_volume_end', 2): '一卷梗概',
    ('test_triggered_at_volume_end', 6): 'done_reason',
    ('test_triggered_at_volume_end', 7): 'passed',
    ('test_triggered_at_volume_end', 8): 'py1',
    ('test_triggered_at_volume_end', 9): 'py4',
    ('test_triggered_at_volume_end', 10): 'assert %(py6)s',
    ('test_triggered_at_volume_end', 11): 'py6',
    ('test_triggered_at_volume_end', 13): 'volume_summary',
    ('test_triggered_at_volume_end', 14): 'summary',
    ('test_triggered_at_volume_end', 15): 'story',
    ('test_triggered_at_volume_end', 16): 'volume_summaries',
    ('test_triggered_at_volume_end', 17): '梗概要并进 state',
    ('test_triggered_at_volume_end', 18): '\n>assert %(py1)s',
    ('test_not_triggered_mid_volume', 2): 'py0',
    ('test_not_triggered_mid_volume', 3): 'calls',
    ('test_not_triggered_mid_volume', 4): 'py3',
    ('test_not_triggered_mid_volume', 5): 'assert %(py5)s',
    ('test_not_triggered_mid_volume', 6): 'py5',
    ('test_not_triggered_mid_volume', 8): 'volume_summary',
    ('test_not_triggered_mid_volume', 9): 'out',
    ('test_not_triggered_mid_volume', 10): 'py2',
    ('test_not_triggered_mid_volume', 11): 'py4',
    ('test_not_triggered_mid_volume', 12): 'py6',
    ('test_not_triggered_mid_volume', 13): 'py9',
    ('test_not_triggered_mid_volume', 14): 'assert %(py11)s',
    ('test_not_triggered_mid_volume', 15): 'py11',
    ('test_failure_is_reported_not_raised', 2): 'done_reason',
    ('test_failure_is_reported_not_raised', 3): 'passed',
    ('test_failure_is_reported_not_raised', 4): 'py1',
    ('test_failure_is_reported_not_raised', 5): 'py4',
    ('test_failure_is_reported_not_raised', 6): '记账失败不该把一章判死',
    ('test_failure_is_reported_not_raised', 7): '\n>assert %(py6)s',
    ('test_failure_is_reported_not_raised', 8): 'py6',
    ('test_failure_is_reported_not_raised', 10): '上游 403',
    ('test_failure_is_reported_not_raised', 11): 'compress_error',
    ('test_failure_is_reported_not_raised', 12): 'assert %(py6)s',
    ('boom', 0): '上游 403',
    ('TestArchiveFailureInGraph', 0): 'TestArchiveFailureInGraph',
    ('TestArchiveFailureInGraph', 2): '两条路径行为必须一致。',
    ('test_chapter_survives_a_failed_archive', 3): '场景一',
    ('test_chapter_survives_a_failed_archive', 4): '场景二',
    ('test_chapter_survives_a_failed_archive', 7): 'done_reason',
    ('test_chapter_survives_a_failed_archive', 8): 'passed',
    ('test_chapter_survives_a_failed_archive', 9): 'py1',
    ('test_chapter_survives_a_failed_archive', 10): 'py4',
    ('test_chapter_survives_a_failed_archive', 11): 'assert %(py6)s',
    ('test_chapter_survives_a_failed_archive', 12): 'py6',
    ('test_chapter_survives_a_failed_archive', 14): '第 0 章',
    ('test_chapter_survives_a_failed_archive', 15): 'archive_error',
    ('test_chapter_survives_a_failed_archive', 16): 'text',
    ('test_chapter_survives_a_failed_archive', 17): 'py3',
    ('test_chapter_survives_a_failed_archive', 18): 'GOOD',
    ('test_chapter_survives_a_failed_archive', 19): '正文要留在结果里',
    ('test_chapter_survives_a_failed_archive', 20): '\n>assert %(py5)s',
    ('test_chapter_survives_a_failed_archive', 21): 'py5',
    ('boom', 0): 'archivist 归档的是第 0 章「」',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def make(stitch_outputs, verdicts, max_revisions):
    '场景一'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  31           RESUME                   0
    # |  32           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('ChapterPipeline',))
    # |               IMPORT_NAME              0 (novel_agent.agents.pipeline)
    # |               IMPORT_FROM              1 (ChapterPipeline)
    # |               STORE_FAST               3 (ChapterPipeline)
    # |               POP_TOP
    # |  34           LOAD_GLOBAL              5 (FakeWriter + NULL)
    # |               LOAD_CONST               2 ('场景一')
    # |               LOAD_CONST               3 ('场景二')
    # |               BUILD_LIST               2
    # |               CALL                     1
    # |               STORE_FAST               4 (w)
    # |  35           LOAD_GLOBAL              7 (FakeArchivist + NULL)
    # |               CALL                     0
    # |               STORE_FAST               5 (a)
    # |  36           LOAD_FAST_BORROW         3 (ChapterPipeline)
    # |               PUSH_NULL
    # |  37           LOAD_GLOBAL              9 (FakeArchitect + NULL)
    # |               CALL                     0
    # |               LOAD_FAST_BORROW         4 (w)
    # |               LOAD_GLOBAL             11 (FakeStitcher + NULL)
    # |               LOAD_FAST_BORROW         0 (stitch_outputs)
    # |               CALL                     1
    # |  38           LOAD_GLOBAL             12 (Gate)
    # |               LOAD_ATTR               14 (from_config)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             16 (CONFIG)
    # |               CALL                     1
    # |               LOAD_GLOBAL             19 (FakeJudge + NULL)
    # |               LOAD_FAST_BORROW         1 (verdicts)
    # |               CALL                     1
    # |               LOAD_FAST_BORROW         5 (a)
    # |  39           LOAD_FAST_BORROW         2 (max_revisions)
    # |               LOAD_CONST               4 (<code object <lambda> at 0x10671ded0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 39>)
    # |               MAKE_FUNCTION
    # |  36           LOAD_CONST               5 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'max_revisions', 'log'))
    # |               CALL_KW                  8
    # |               STORE_FAST               6 (p)
    # |  40           LOAD_GLOBAL             21 (build_graph + NULL)
    # |               LOAD_FAST_BORROW         6 (p)
    # |               CALL                     1
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (w, a)
    # |               BUILD_TUPLE              3
    # |               RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x10671ded0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 39>:
    # |  39           RESUME                   0
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE

def seed(sample_state, ch):
    'ch'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  43           RESUME                   0
    # |  44           LOAD_CONST               0 ('ch')
    # |               LOAD_FAST_BORROW         1 (ch)
    # |               LOAD_CONST               1 ('story')
    # |               LOAD_FAST_BORROW         0 (sample_state)
    # |               LOAD_ATTR                1 (model_dump + NULL|self)
    # |               CALL                     0
    # |  45           LOAD_CONST               2 ('volume')
    # |               LOAD_GLOBAL              3 (volume + NULL)
    # |               CALL                     0
    # |               LOAD_ATTR                1 (model_dump + NULL|self)
    # |               CALL                     0
    # |               LOAD_CONST               3 ('note')
    # |               LOAD_CONST               4 ('')
    # |  44           BUILD_MAP                4
    # |               RETURN_VALUE

class TestHappyPath:
    'TestHappyPath'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  48           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestHappyPath')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          48
    # |               STORE_NAME               3 (__firstlineno__)
    # |  49           LOAD_CONST               1 (<code object test_reaches_archive at 0x7b1909b800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 49>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_reaches_archive)
    # |  57           LOAD_CONST               2 (<code object test_state_advances_in_graph at 0x7b191f1400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 57>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_state_advances_in_graph)
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_reaches_archive at 0x7b1909b800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 49>:
    # |  49            RESUME                   0
    # |  50            LOAD_GLOBAL              1 (make + NULL)
    # |                LOAD_GLOBAL              2 (GOOD)
    # |                BUILD_LIST               1
    # |                LOAD_GLOBAL              4 (PASS)
    # |                BUILD_LIST               1
    # |                CALL                     2
    # |                UNPACK_SEQUENCE          3
    # |                STORE_FAST_STORE_FAST   35 (g, w)
    # |                STORE_FAST               4 (a)
    # |  51            LOAD_FAST_BORROW         2 (g)
    # |                LOAD_ATTR                7 (invoke + NULL|self)
    # |                LOAD_GLOBAL              9 (seed + NULL)
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                CALL                     1
    # |                CALL                     1
    # |                STORE_FAST               5 (out)
    # |  52            LOAD_FAST_BORROW         5 (out)
    # |                LOAD_CONST               0 ('done_reason')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               6 (@py_assert0)
    # |                LOAD_CONST               1 ('passed')
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              15 (('==',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              16 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format5)
    # |                LOAD_CONST               4 ('assert %(py6)s')
    # |                LOAD_CONST               5 ('py6')
    # |                LOAD_FAST_BORROW         9 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L1:     LOAD_CONST               6 (None)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
    # |  53            LOAD_FAST_BORROW         5 (out)
    # |                LOAD_CONST               7 ('revisions')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               6 (@py_assert0)
    # |                LOAD_SMALL_INT           0
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              15 (('==',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              16 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format5)
    # |                LOAD_CONST               4 ('assert %(py6)s')
    # |                LOAD_CONST               5 ('py6')
    # |                LOAD_FAST_BORROW         9 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L2:     LOAD_CONST               6 (None)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
    # |  54            LOAD_FAST_BORROW         4 (a)
    # |                LOAD_ATTR               20 (called)
    # |                STORE_FAST              11 (@py_assert1)
    # |                LOAD_SMALL_INT           1
    # |                STORE_FAST_LOAD_FAST   203 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW        12 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L6)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              15 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.called\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py0')
    # |                LOAD_CONST               9 ('a')
    # |                LOAD_GLOBAL             22 (@py_builtins)
    # |                LOAD_ATTR               24 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L3)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               26 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (a)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L4)
    # |                NOT_TAKEN
    # |        L3:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (a)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L5)
    # |        L4:     LOAD_CONST               9 ('a')
    # |        L5:     LOAD_CONST              10 ('py2')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format6)
    # |                LOAD_CONST              12 ('assert %(py7)s')
    # |                LOAD_CONST              13 ('py7')
    # |                LOAD_FAST_BORROW        13 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format8)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        14 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L6:     LOAD_CONST               6 (None)
    # |                COPY                     1
    # |                STORE_FAST              11 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  124 (@py_assert3, @py_assert4)
    # |  55            LOAD_FAST_BORROW         3 (w)
    # |                LOAD_ATTR               28 (revised)
    # |                STORE_FAST              11 (@py_assert1)
    # |                BUILD_LIST               0
    # |                STORE_FAST_LOAD_FAST   203 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW        12 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              15 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py2)s\n{%(py2)s = %(py0)s.revised\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py0')
    # |                LOAD_CONST              14 ('w')
    # |                LOAD_GLOBAL             22 (@py_builtins)
    # |                LOAD_ATTR               24 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               26 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (w)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (w)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              14 ('w')
    # |        L9:     LOAD_CONST              10 ('py2')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format6)
    # |                LOAD_CONST              12 ('assert %(py7)s')
    # |                LOAD_CONST              13 ('py7')
    # |                LOAD_FAST_BORROW        13 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format8)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        14 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST               6 (None)
    # |                COPY                     1
    # |                STORE_FAST              11 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  124 (@py_assert3, @py_assert4)
    # |                LOAD_CONST               6 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_state_advances_in_graph at 0x7b191f1400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 57>:
    # |   57            RESUME                   0
    # |   58            LOAD_GLOBAL              1 (make + NULL)
    # |                 LOAD_GLOBAL              2 (GOOD)
    # |                 BUILD_LIST               1
    # |                 LOAD_GLOBAL              4 (PASS)
    # |                 BUILD_LIST               1
    # |                 CALL                     2
    # |                 UNPACK_SEQUENCE          3
    # |                 STORE_FAST               2 (g)
    # |                 POP_TOP
    # |                 STORE_FAST               3 (_)
    # |   59            LOAD_FAST_BORROW         2 (g)
    # |                 LOAD_ATTR                7 (invoke + NULL|self)
    # |                 LOAD_GLOBAL              9 (seed + NULL)
    # |                 LOAD_FAST_BORROW         1 (sample_state)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 STORE_FAST               4 (out)
    # |   60            LOAD_FAST_BORROW         4 (out)
    # |                 LOAD_CONST               0 ('patch')
    # |                 BINARY_OP               26 ([])
    # |                 STORE_FAST               5 (@py_assert0)
    # |                 LOAD_CONST               1 (None)
    # |                 STORE_FAST_LOAD_FAST   101 (@py_assert3, @py_assert0)
    # |                 LOAD_FAST_BORROW         6 (@py_assert3)
    # |                 IS_OP                    1 (is not)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       121 (to L1)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              13 (('is not',))
    # |                 LOAD_FAST_BORROW         7 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              14 (('%(py1)s is not %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               2 ('py1')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               3 ('py4')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format5)
    # |                 LOAD_CONST               4 ('assert %(py6)s')
    # |                 LOAD_CONST               5 ('py6')
    # |                 LOAD_FAST_BORROW         8 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format7)
    # |                 LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L1:     LOAD_CONST               1 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  118 (@py_assert2, @py_assert3)
    # |   61            LOAD_FAST_BORROW         4 (out)
    # |                 LOAD_CONST               6 ('story')
    # |                 BINARY_OP               26 ([])
    # |                 LOAD_CONST               7 ('chapter_summaries')
    # |                 BINARY_OP               26 ([])
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR     10 (s)
    # |                 SWAP                     2
    # |         L2:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L3:     FOR_ITER                11 (to L4)
    # |                 STORE_FAST_LOAD_FAST   170 (s, s)
    # |                 LOAD_CONST               8 ('ch')
    # |                 BINARY_OP               26 ([])
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           13 (to L3)
    # |         L4:     END_FOR
    # |                 POP_ITER
    # |         L5:     STORE_FAST              11 (chs)
    # |                 STORE_FAST              10 (s)
    # |   62            LOAD_SMALL_INT           1
    # |                 STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
    # |                 LOAD_FAST_BORROW        11 (chs)
    # |                 CONTAINS_OP              0 (in)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       177 (to L9)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              15 (('in',))
    # |                 LOAD_FAST_BORROW         7 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              16 (('%(py1)s in %(py3)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 91 (@py_assert0, chs)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               2 ('py1')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               9 ('py3')
    # |                 LOAD_CONST              10 ('chs')
    # |                 LOAD_GLOBAL             20 (@py_builtins)
    # |                 LOAD_ATTR               22 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L6)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (chs)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L7)
    # |                 NOT_TAKEN
    # |         L6:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (chs)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L8)
    # |         L7:     LOAD_CONST              10 ('chs')
    # |         L8:     BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format4)
    # |                 LOAD_CONST              11 ('assert %(py5)s')
    # |                 LOAD_CONST              12 ('py5')
    # |                 LOAD_FAST_BORROW        12 (@py_format4)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format6)
    # |                 LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_format6)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L9:     LOAD_CONST               1 (None)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   87 (@py_assert0, @py_assert2)
    # |                 LOAD_CONST               1 (None)
    # |                 RETURN_VALUE
    # |   --   L10:     SWAP                     2
    # |                 POP_TOP
    # |   61            SWAP                     2
    # |                 STORE_FAST              10 (s)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L2 to L5 -> L10 [2]

    def test_reaches_archive(self, sample_state):
        'done_reason'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  49            RESUME                   0
        # |  50            LOAD_GLOBAL              1 (make + NULL)
        # |                LOAD_GLOBAL              2 (GOOD)
        # |                BUILD_LIST               1
        # |                LOAD_GLOBAL              4 (PASS)
        # |                BUILD_LIST               1
        # |                CALL                     2
        # |                UNPACK_SEQUENCE          3
        # |                STORE_FAST_STORE_FAST   35 (g, w)
        # |                STORE_FAST               4 (a)
        # |  51            LOAD_FAST_BORROW         2 (g)
        # |                LOAD_ATTR                7 (invoke + NULL|self)
        # |                LOAD_GLOBAL              9 (seed + NULL)
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                CALL                     1
        # |                CALL                     1
        # |                STORE_FAST               5 (out)
        # |  52            LOAD_FAST_BORROW         5 (out)
        # |                LOAD_CONST               0 ('done_reason')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               6 (@py_assert0)
        # |                LOAD_CONST               1 ('passed')
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              15 (('==',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              16 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('py4')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format5)
        # |                LOAD_CONST               4 ('assert %(py6)s')
        # |                LOAD_CONST               5 ('py6')
        # |                LOAD_FAST_BORROW         9 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L1:     LOAD_CONST               6 (None)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
        # |  53            LOAD_FAST_BORROW         5 (out)
        # |                LOAD_CONST               7 ('revisions')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               6 (@py_assert0)
        # |                LOAD_SMALL_INT           0
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              15 (('==',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              16 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('py4')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format5)
        # |                LOAD_CONST               4 ('assert %(py6)s')
        # |                LOAD_CONST               5 ('py6')
        # |                LOAD_FAST_BORROW         9 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L2:     LOAD_CONST               6 (None)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
        # |  54            LOAD_FAST_BORROW         4 (a)
        # |                LOAD_ATTR               20 (called)
        # |                STORE_FAST              11 (@py_assert1)
        # |                LOAD_SMALL_INT           1
        # |                STORE_FAST_LOAD_FAST   203 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW        12 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L6)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              15 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.called\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py0')
        # |                LOAD_CONST               9 ('a')
        # |                LOAD_GLOBAL             22 (@py_builtins)
        # |                LOAD_ATTR               24 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L3)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               26 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (a)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L4)
        # |                NOT_TAKEN
        # |        L3:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (a)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L5)
        # |        L4:     LOAD_CONST               9 ('a')
        # |        L5:     LOAD_CONST              10 ('py2')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format6)
        # |                LOAD_CONST              12 ('assert %(py7)s')
        # |                LOAD_CONST              13 ('py7')
        # |                LOAD_FAST_BORROW        13 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format8)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        14 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L6:     LOAD_CONST               6 (None)
        # |                COPY                     1
        # |                STORE_FAST              11 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  124 (@py_assert3, @py_assert4)
        # |  55            LOAD_FAST_BORROW         3 (w)
        # |                LOAD_ATTR               28 (revised)
        # |                STORE_FAST              11 (@py_assert1)
        # |                BUILD_LIST               0
        # |                STORE_FAST_LOAD_FAST   203 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW        12 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              15 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py2)s\n{%(py2)s = %(py0)s.revised\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py0')
        # |                LOAD_CONST              14 ('w')
        # |                LOAD_GLOBAL             22 (@py_builtins)
        # |                LOAD_ATTR               24 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               26 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (w)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (w)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              14 ('w')
        # |        L9:     LOAD_CONST              10 ('py2')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format6)
        # |                LOAD_CONST              12 ('assert %(py7)s')
        # |                LOAD_CONST              13 ('py7')
        # |                LOAD_FAST_BORROW        13 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format8)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        14 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST               6 (None)
        # |                COPY                     1
        # |                STORE_FAST              11 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  124 (@py_assert3, @py_assert4)
        # |                LOAD_CONST               6 (None)
        # |                RETURN_VALUE

    def test_state_advances_in_graph(self, sample_state):
        'patch'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   57            RESUME                   0
        # |   58            LOAD_GLOBAL              1 (make + NULL)
        # |                 LOAD_GLOBAL              2 (GOOD)
        # |                 BUILD_LIST               1
        # |                 LOAD_GLOBAL              4 (PASS)
        # |                 BUILD_LIST               1
        # |                 CALL                     2
        # |                 UNPACK_SEQUENCE          3
        # |                 STORE_FAST               2 (g)
        # |                 POP_TOP
        # |                 STORE_FAST               3 (_)
        # |   59            LOAD_FAST_BORROW         2 (g)
        # |                 LOAD_ATTR                7 (invoke + NULL|self)
        # |                 LOAD_GLOBAL              9 (seed + NULL)
        # |                 LOAD_FAST_BORROW         1 (sample_state)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 STORE_FAST               4 (out)
        # |   60            LOAD_FAST_BORROW         4 (out)
        # |                 LOAD_CONST               0 ('patch')
        # |                 BINARY_OP               26 ([])
        # |                 STORE_FAST               5 (@py_assert0)
        # |                 LOAD_CONST               1 (None)
        # |                 STORE_FAST_LOAD_FAST   101 (@py_assert3, @py_assert0)
        # |                 LOAD_FAST_BORROW         6 (@py_assert3)
        # |                 IS_OP                    1 (is not)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       121 (to L1)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              13 (('is not',))
        # |                 LOAD_FAST_BORROW         7 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              14 (('%(py1)s is not %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               2 ('py1')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               3 ('py4')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format5)
        # |                 LOAD_CONST               4 ('assert %(py6)s')
        # |                 LOAD_CONST               5 ('py6')
        # |                 LOAD_FAST_BORROW         8 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format7)
        # |                 LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L1:     LOAD_CONST               1 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  118 (@py_assert2, @py_assert3)
        # |   61            LOAD_FAST_BORROW         4 (out)
        # |                 LOAD_CONST               6 ('story')
        # |                 BINARY_OP               26 ([])
        # |                 LOAD_CONST               7 ('chapter_summaries')
        # |                 BINARY_OP               26 ([])
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR     10 (s)
        # |                 SWAP                     2
        # |         L2:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L3:     FOR_ITER                11 (to L4)
        # |                 STORE_FAST_LOAD_FAST   170 (s, s)
        # |                 LOAD_CONST               8 ('ch')
        # |                 BINARY_OP               26 ([])
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           13 (to L3)
        # |         L4:     END_FOR
        # |                 POP_ITER
        # |         L5:     STORE_FAST              11 (chs)
        # |                 STORE_FAST              10 (s)
        # |   62            LOAD_SMALL_INT           1
        # |                 STORE_FAST_LOAD_FAST    85 (@py_assert0, @py_assert0)
        # |                 LOAD_FAST_BORROW        11 (chs)
        # |                 CONTAINS_OP              0 (in)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       177 (to L9)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              15 (('in',))
        # |                 LOAD_FAST_BORROW         7 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              16 (('%(py1)s in %(py3)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 91 (@py_assert0, chs)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               2 ('py1')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               9 ('py3')
        # |                 LOAD_CONST              10 ('chs')
        # |                 LOAD_GLOBAL             20 (@py_builtins)
        # |                 LOAD_ATTR               22 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L6)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (chs)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L7)
        # |                 NOT_TAKEN
        # |         L6:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (chs)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L8)
        # |         L7:     LOAD_CONST              10 ('chs')
        # |         L8:     BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format4)
        # |                 LOAD_CONST              11 ('assert %(py5)s')
        # |                 LOAD_CONST              12 ('py5')
        # |                 LOAD_FAST_BORROW        12 (@py_format4)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format6)
        # |                 LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_format6)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L9:     LOAD_CONST               1 (None)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   87 (@py_assert0, @py_assert2)
        # |                 LOAD_CONST               1 (None)
        # |                 RETURN_VALUE
        # |   --   L10:     SWAP                     2
        # |                 POP_TOP
        # |   61            SWAP                     2
        # |                 STORE_FAST              10 (s)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L2 to L5 -> L10 [2]


class TestRevisionRouting:
    'TestRevisionRouting'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  65           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestRevisionRouting')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          65
    # |               STORE_NAME               3 (__firstlineno__)
    # |  66           LOAD_CONST               1 (<code object test_gate_failure_routes_to_revise at 0x7b18e21e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 66>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_gate_failure_routes_to_revise)
    # |  73           LOAD_CONST               2 (<code object test_judge_failure_routes_to_revise at 0x7b191f3200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 73>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_judge_failure_routes_to_revise)
    # |  78           LOAD_CONST               3 (<code object test_revise_goes_back_through_stitch at 0x7b18e50700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 78>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_revise_goes_back_through_stitch)
    # |  85           LOAD_CONST               4 (<code object test_gives_up_at_limit at 0x7b18e22400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 85>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_gives_up_at_limit)
    # |  92           LOAD_CONST               5 (<code object test_judge_not_run_when_gate_fails at 0x7b1920e000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 92>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_judge_not_run_when_gate_fails)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_gate_failure_routes_to_revise at 0x7b18e21e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 66>:
    # |  66           RESUME                   0
    # |  67           LOAD_GLOBAL              1 (make + NULL)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               LOAD_GLOBAL              4 (GOOD)
    # |               BUILD_LIST               2
    # |               LOAD_GLOBAL              6 (PASS)
    # |               BUILD_LIST               1
    # |               CALL                     2
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST_STORE_FAST   35 (g, w)
    # |               STORE_FAST               4 (_)
    # |  68           LOAD_FAST_BORROW         2 (g)
    # |               LOAD_ATTR                9 (invoke + NULL|self)
    # |               LOAD_GLOBAL             11 (seed + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               CALL                     1
    # |               STORE_FAST               5 (out)
    # |  69           LOAD_FAST_BORROW         5 (out)
    # |               LOAD_CONST               0 ('done_reason')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               6 (@py_assert0)
    # |               LOAD_CONST               1 ('passed')
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (('==',))
    # |               LOAD_FAST_BORROW         8 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              14 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format5)
    # |               LOAD_CONST               4 ('assert %(py6)s')
    # |               LOAD_CONST               5 ('py6')
    # |               LOAD_FAST_BORROW         9 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
    # |  70           LOAD_FAST_BORROW         5 (out)
    # |               LOAD_CONST               7 ('revisions')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               6 (@py_assert0)
    # |               LOAD_SMALL_INT           1
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (('==',))
    # |               LOAD_FAST_BORROW         8 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              14 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format5)
    # |               LOAD_CONST               4 ('assert %(py6)s')
    # |               LOAD_CONST               5 ('py6')
    # |               LOAD_FAST_BORROW         9 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
    # |  71           LOAD_FAST_BORROW         3 (w)
    # |               LOAD_ATTR               22 (revised)
    # |               STORE_FAST_LOAD_FAST   187 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       168 (to L6)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 ('应当重写过场景')
    # |               CALL                     1
    # |               LOAD_CONST               9 ('\n>assert %(py2)s\n{%(py2)s = %(py0)s.revised\n}')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST              10 ('py0')
    # |               LOAD_CONST              11 ('w')
    # |               LOAD_GLOBAL             26 (@py_builtins)
    # |               LOAD_ATTR               28 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               30 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (w)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L4)
    # |               NOT_TAKEN
    # |       L3:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (w)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L5)
    # |       L4:     LOAD_CONST              11 ('w')
    # |       L5:     LOAD_CONST              12 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_assert1)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format3)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        12 (@py_format3)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L6:     LOAD_CONST               6 (None)
    # |               STORE_FAST              11 (@py_assert1)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_judge_failure_routes_to_revise at 0x7b191f3200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 73>:
    # |  73           RESUME                   0
    # |  74           LOAD_GLOBAL              1 (make + NULL)
    # |               LOAD_GLOBAL              2 (GOOD)
    # |               LOAD_GLOBAL              2 (GOOD)
    # |               BUILD_LIST               2
    # |               LOAD_GLOBAL              4 (FAIL)
    # |               LOAD_GLOBAL              6 (PASS)
    # |               BUILD_LIST               2
    # |               CALL                     2
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST_STORE_FAST   35 (g, w)
    # |               STORE_FAST               4 (_)
    # |  75           LOAD_FAST_BORROW         2 (g)
    # |               LOAD_ATTR                9 (invoke + NULL|self)
    # |               LOAD_GLOBAL             11 (seed + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               CALL                     1
    # |               STORE_FAST               5 (out)
    # |  76           BUILD_LIST               0
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert1, out)
    # |               LOAD_CONST               0 ('revisions')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               7 (@py_assert2)
    # |               LOAD_SMALL_INT           1
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert5, @py_assert2)
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert4, @py_assert4)
    # |               STORE_FAST_LOAD_FAST   169 (@py_assert0, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       17 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_FAST_BORROW         5 (out)
    # |               LOAD_CONST               1 ('done_reason')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST              11 (@py_assert10)
    # |               LOAD_CONST               2 ('passed')
    # |               STORE_FAST_LOAD_FAST   203 (@py_assert13, @py_assert10)
    # |               LOAD_FAST_BORROW        12 (@py_assert13)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   221 (@py_assert12, @py_assert12)
    # |               STORE_FAST              10 (@py_assert0)
    # |       L1:     LOAD_FAST_BORROW        10 (@py_assert0)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       293 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('==',))
    # |               LOAD_FAST_BORROW         9 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py3)s == %(py6)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert2, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py6')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              14 (@py_format7)
    # |               LOAD_CONST               5 ('%(py8)s')
    # |               LOAD_CONST               6 ('py8')
    # |               LOAD_FAST_BORROW        14 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   246 (@py_format9, @py_assert1)
    # |               LOAD_ATTR               19 (append + NULL|self)
    # |               LOAD_FAST_BORROW        15 (@py_format9)
    # |               CALL                     1
    # |               POP_TOP
    # |               LOAD_FAST_BORROW         9 (@py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE      108 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('==',))
    # |               LOAD_FAST_CHECK         13 (@py_assert12)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py11)s == %(py14)s',))
    # |               LOAD_FAST_CHECK         11 (@py_assert10)
    # |               LOAD_FAST_CHECK         12 (@py_assert13)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py11')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_assert10)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py14')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        12 (@py_assert13)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              16 (@py_format15)
    # |               LOAD_CONST               9 ('%(py16)s')
    # |               LOAD_CONST              10 ('py16')
    # |               LOAD_FAST_BORROW        16 (@py_format15)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              17 (@py_format17)
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               LOAD_ATTR               19 (append + NULL|self)
    # |               LOAD_FAST_BORROW        17 (@py_format17)
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
    # |               STORE_FAST              18 (@py_format18)
    # |               LOAD_CONST              11 ('assert %(py19)s')
    # |               LOAD_CONST              12 ('py19')
    # |               LOAD_FAST_BORROW        18 (@py_format18)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              19 (@py_format20)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        19 (@py_format20)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L3:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST              10 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST              11 (@py_assert10)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  220 (@py_assert12, @py_assert13)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_revise_goes_back_through_stitch at 0x7b18e50700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 78>:
    # |  78           RESUME                   0
    # |  80           LOAD_GLOBAL              1 (FakeStitcher + NULL)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               LOAD_GLOBAL              4 (GOOD)
    # |               BUILD_LIST               2
    # |               CALL                     1
    # |               STORE_FAST               2 (st)
    # |  81           LOAD_GLOBAL              7 (make + NULL)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               LOAD_GLOBAL              4 (GOOD)
    # |               BUILD_LIST               2
    # |               LOAD_GLOBAL              8 (PASS)
    # |               BUILD_LIST               1
    # |               CALL                     2
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST               3 (g)
    # |               POP_TOP
    # |               STORE_FAST               4 (_)
    # |  82           LOAD_FAST_BORROW         3 (g)
    # |               LOAD_ATTR               11 (invoke + NULL|self)
    # |               LOAD_GLOBAL             13 (seed + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               CALL                     1
    # |               STORE_FAST               5 (out)
    # |  83           LOAD_FAST_BORROW         5 (out)
    # |               LOAD_CONST               1 ('text')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert0, @py_assert0)
    # |               LOAD_GLOBAL              4 (GOOD)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       190 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               16 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 (('==',))
    # |               LOAD_FAST_BORROW         7 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               9 (('%(py1)s == %(py3)s',))
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               LOAD_GLOBAL              4 (GOOD)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_CONST               4 ('GOOD')
    # |               LOAD_GLOBAL             20 (@py_builtins)
    # |               LOAD_ATTR               22 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (GOOD)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (GOOD)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('GOOD')
    # |       L3:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format4)
    # |               LOAD_CONST               5 ('assert %(py5)s')
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_FAST_BORROW         8 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format6)
    # |               LOAD_GLOBAL             27 (AssertionError + NULL)
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               28 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  103 (@py_assert0, @py_assert2)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_gives_up_at_limit at 0x7b18e22400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 85>:
    # |  85           RESUME                   0
    # |  86           LOAD_GLOBAL              1 (make + NULL)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               BUILD_LIST               4
    # |               LOAD_GLOBAL              4 (PASS)
    # |               BUILD_LIST               1
    # |               LOAD_SMALL_INT           2
    # |               LOAD_CONST               1 (('max_revisions',))
    # |               CALL_KW                  3
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST_STORE_FAST   35 (g, _)
    # |               STORE_FAST               4 (a)
    # |  87           LOAD_FAST_BORROW         2 (g)
    # |               LOAD_ATTR                7 (invoke + NULL|self)
    # |               LOAD_GLOBAL              9 (seed + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               CALL                     1
    # |               STORE_FAST               5 (out)
    # |  88           LOAD_FAST_BORROW         5 (out)
    # |               LOAD_CONST               2 ('revisions')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               6 (@py_assert0)
    # |               LOAD_SMALL_INT           2
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('==',))
    # |               LOAD_FAST_BORROW         8 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format5)
    # |               LOAD_CONST               5 ('assert %(py6)s')
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_FAST_BORROW         9 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
    # |  89           LOAD_CONST               8 ('仍未通过')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert0, out)
    # |               LOAD_CONST               9 ('done_reason')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              19 (('in',))
    # |               LOAD_FAST_BORROW         8 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              20 (('%(py1)s in %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format5)
    # |               LOAD_CONST               5 ('assert %(py6)s')
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_FAST_BORROW         9 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
    # |  90           LOAD_FAST_BORROW         4 (a)
    # |               LOAD_ATTR               20 (called)
    # |               STORE_FAST              11 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               STORE_FAST_LOAD_FAST   203 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW        12 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       226 (to L6)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('==',))
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              21 (('%(py2)s\n{%(py2)s = %(py0)s.called\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              10 ('py0')
    # |               LOAD_CONST              11 ('a')
    # |               LOAD_GLOBAL             22 (@py_builtins)
    # |               LOAD_ATTR               24 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               26 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (a)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L4)
    # |               NOT_TAKEN
    # |       L3:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (a)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L5)
    # |       L4:     LOAD_CONST              11 ('a')
    # |       L5:     LOAD_CONST              12 ('py2')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              13 ('py5')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        12 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format6)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               28 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 ('未通过不得归档')
    # |               CALL                     1
    # |               LOAD_CONST              15 ('\n>assert %(py7)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST              16 ('py7')
    # |               LOAD_FAST_BORROW        13 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              14 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        14 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L6:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST              11 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  124 (@py_assert3, @py_assert4)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_judge_not_run_when_gate_fails at 0x7b1920e000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 92>:
    # |  92           RESUME                   0
    # |  93           LOAD_GLOBAL              1 (make + NULL)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               LOAD_GLOBAL              2 (BAD)
    # |               BUILD_LIST               3
    # |               LOAD_GLOBAL              4 (PASS)
    # |               BUILD_LIST               1
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               1 (('max_revisions',))
    # |               CALL_KW                  3
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST               2 (g)
    # |               POP_TOP
    # |               STORE_FAST               3 (_)
    # |  94           LOAD_FAST_BORROW         2 (g)
    # |               LOAD_ATTR                7 (invoke + NULL|self)
    # |               LOAD_GLOBAL              9 (seed + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               CALL                     1
    # |               STORE_FAST               4 (out)
    # |  95           LOAD_FAST_BORROW         4 (out)
    # |               LOAD_ATTR               10 (get)
    # |               STORE_FAST               5 (@py_assert1)
    # |               LOAD_CONST               2 ('verdict')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST               7 (@py_assert5)
    # |               LOAD_CONST               3 (None)
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert8, @py_assert5)
    # |               LOAD_FAST_BORROW         8 (@py_assert8)
    # |               IS_OP                    0 (is)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       243 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 (('is',))
    # |               LOAD_FAST_BORROW         9 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} is %(py9)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert5, @py_assert8)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST               5 ('out')
    # |               LOAD_GLOBAL             16 (@py_builtins)
    # |               LOAD_ATTR               18 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (out)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (out)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('out')
    # |       L3:     LOAD_CONST               6 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py6')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py9')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format10)
    # |               LOAD_CONST              10 ('assert %(py11)s')
    # |               LOAD_CONST              11 ('py11')
    # |               LOAD_FAST_BORROW        10 (@py_format10)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format12)
    # |               LOAD_GLOBAL             25 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               26 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format12)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               3 (None)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  152 (@py_assert7, @py_assert8)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE

    def test_gate_failure_routes_to_revise(self, sample_state):
        'done_reason'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  66           RESUME                   0
        # |  67           LOAD_GLOBAL              1 (make + NULL)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               LOAD_GLOBAL              4 (GOOD)
        # |               BUILD_LIST               2
        # |               LOAD_GLOBAL              6 (PASS)
        # |               BUILD_LIST               1
        # |               CALL                     2
        # |               UNPACK_SEQUENCE          3
        # |               STORE_FAST_STORE_FAST   35 (g, w)
        # |               STORE_FAST               4 (_)
        # |  68           LOAD_FAST_BORROW         2 (g)
        # |               LOAD_ATTR                9 (invoke + NULL|self)
        # |               LOAD_GLOBAL             11 (seed + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               CALL                     1
        # |               STORE_FAST               5 (out)
        # |  69           LOAD_FAST_BORROW         5 (out)
        # |               LOAD_CONST               0 ('done_reason')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               6 (@py_assert0)
        # |               LOAD_CONST               1 ('passed')
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (('==',))
        # |               LOAD_FAST_BORROW         8 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              14 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format5)
        # |               LOAD_CONST               4 ('assert %(py6)s')
        # |               LOAD_CONST               5 ('py6')
        # |               LOAD_FAST_BORROW         9 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
        # |  70           LOAD_FAST_BORROW         5 (out)
        # |               LOAD_CONST               7 ('revisions')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               6 (@py_assert0)
        # |               LOAD_SMALL_INT           1
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (('==',))
        # |               LOAD_FAST_BORROW         8 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              14 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format5)
        # |               LOAD_CONST               4 ('assert %(py6)s')
        # |               LOAD_CONST               5 ('py6')
        # |               LOAD_FAST_BORROW         9 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
        # |  71           LOAD_FAST_BORROW         3 (w)
        # |               LOAD_ATTR               22 (revised)
        # |               STORE_FAST_LOAD_FAST   187 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       168 (to L6)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 ('应当重写过场景')
        # |               CALL                     1
        # |               LOAD_CONST               9 ('\n>assert %(py2)s\n{%(py2)s = %(py0)s.revised\n}')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST              10 ('py0')
        # |               LOAD_CONST              11 ('w')
        # |               LOAD_GLOBAL             26 (@py_builtins)
        # |               LOAD_ATTR               28 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L3)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               30 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (w)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L4)
        # |               NOT_TAKEN
        # |       L3:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (w)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L5)
        # |       L4:     LOAD_CONST              11 ('w')
        # |       L5:     LOAD_CONST              12 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_assert1)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format3)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        12 (@py_format3)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L6:     LOAD_CONST               6 (None)
        # |               STORE_FAST              11 (@py_assert1)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE

    def test_judge_failure_routes_to_revise(self, sample_state):
        'revisions'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  73           RESUME                   0
        # |  74           LOAD_GLOBAL              1 (make + NULL)
        # |               LOAD_GLOBAL              2 (GOOD)
        # |               LOAD_GLOBAL              2 (GOOD)
        # |               BUILD_LIST               2
        # |               LOAD_GLOBAL              4 (FAIL)
        # |               LOAD_GLOBAL              6 (PASS)
        # |               BUILD_LIST               2
        # |               CALL                     2
        # |               UNPACK_SEQUENCE          3
        # |               STORE_FAST_STORE_FAST   35 (g, w)
        # |               STORE_FAST               4 (_)
        # |  75           LOAD_FAST_BORROW         2 (g)
        # |               LOAD_ATTR                9 (invoke + NULL|self)
        # |               LOAD_GLOBAL             11 (seed + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               CALL                     1
        # |               STORE_FAST               5 (out)
        # |  76           BUILD_LIST               0
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert1, out)
        # |               LOAD_CONST               0 ('revisions')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               7 (@py_assert2)
        # |               LOAD_SMALL_INT           1
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert5, @py_assert2)
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert4, @py_assert4)
        # |               STORE_FAST_LOAD_FAST   169 (@py_assert0, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       17 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_FAST_BORROW         5 (out)
        # |               LOAD_CONST               1 ('done_reason')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST              11 (@py_assert10)
        # |               LOAD_CONST               2 ('passed')
        # |               STORE_FAST_LOAD_FAST   203 (@py_assert13, @py_assert10)
        # |               LOAD_FAST_BORROW        12 (@py_assert13)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   221 (@py_assert12, @py_assert12)
        # |               STORE_FAST              10 (@py_assert0)
        # |       L1:     LOAD_FAST_BORROW        10 (@py_assert0)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       293 (to L3)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('==',))
        # |               LOAD_FAST_BORROW         9 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              15 (('%(py3)s == %(py6)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert2, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py6')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              14 (@py_format7)
        # |               LOAD_CONST               5 ('%(py8)s')
        # |               LOAD_CONST               6 ('py8')
        # |               LOAD_FAST_BORROW        14 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   246 (@py_format9, @py_assert1)
        # |               LOAD_ATTR               19 (append + NULL|self)
        # |               LOAD_FAST_BORROW        15 (@py_format9)
        # |               CALL                     1
        # |               POP_TOP
        # |               LOAD_FAST_BORROW         9 (@py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE      108 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('==',))
        # |               LOAD_FAST_CHECK         13 (@py_assert12)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py11)s == %(py14)s',))
        # |               LOAD_FAST_CHECK         11 (@py_assert10)
        # |               LOAD_FAST_CHECK         12 (@py_assert13)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py11')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_assert10)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py14')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        12 (@py_assert13)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              16 (@py_format15)
        # |               LOAD_CONST               9 ('%(py16)s')
        # |               LOAD_CONST              10 ('py16')
        # |               LOAD_FAST_BORROW        16 (@py_format15)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              17 (@py_format17)
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               LOAD_ATTR               19 (append + NULL|self)
        # |               LOAD_FAST_BORROW        17 (@py_format17)
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
        # |               STORE_FAST              18 (@py_format18)
        # |               LOAD_CONST              11 ('assert %(py19)s')
        # |               LOAD_CONST              12 ('py19')
        # |               LOAD_FAST_BORROW        18 (@py_format18)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              19 (@py_format20)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        19 (@py_format20)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L3:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST              10 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST              11 (@py_assert10)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  220 (@py_assert12, @py_assert13)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE

    def test_revise_goes_back_through_stitch(self, sample_state):
        '重写的是场景，缝合必须重做 —— 否则改动不会进入成稿。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  78           RESUME                   0
        # |  80           LOAD_GLOBAL              1 (FakeStitcher + NULL)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               LOAD_GLOBAL              4 (GOOD)
        # |               BUILD_LIST               2
        # |               CALL                     1
        # |               STORE_FAST               2 (st)
        # |  81           LOAD_GLOBAL              7 (make + NULL)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               LOAD_GLOBAL              4 (GOOD)
        # |               BUILD_LIST               2
        # |               LOAD_GLOBAL              8 (PASS)
        # |               BUILD_LIST               1
        # |               CALL                     2
        # |               UNPACK_SEQUENCE          3
        # |               STORE_FAST               3 (g)
        # |               POP_TOP
        # |               STORE_FAST               4 (_)
        # |  82           LOAD_FAST_BORROW         3 (g)
        # |               LOAD_ATTR               11 (invoke + NULL|self)
        # |               LOAD_GLOBAL             13 (seed + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               CALL                     1
        # |               STORE_FAST               5 (out)
        # |  83           LOAD_FAST_BORROW         5 (out)
        # |               LOAD_CONST               1 ('text')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert0, @py_assert0)
        # |               LOAD_GLOBAL              4 (GOOD)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       190 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               16 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 (('==',))
        # |               LOAD_FAST_BORROW         7 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               9 (('%(py1)s == %(py3)s',))
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               LOAD_GLOBAL              4 (GOOD)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_CONST               4 ('GOOD')
        # |               LOAD_GLOBAL             20 (@py_builtins)
        # |               LOAD_ATTR               22 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (GOOD)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (GOOD)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('GOOD')
        # |       L3:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format4)
        # |               LOAD_CONST               5 ('assert %(py5)s')
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_FAST_BORROW         8 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format6)
        # |               LOAD_GLOBAL             27 (AssertionError + NULL)
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               28 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  103 (@py_assert0, @py_assert2)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_gives_up_at_limit(self, sample_state):
        'revisions'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  85           RESUME                   0
        # |  86           LOAD_GLOBAL              1 (make + NULL)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               BUILD_LIST               4
        # |               LOAD_GLOBAL              4 (PASS)
        # |               BUILD_LIST               1
        # |               LOAD_SMALL_INT           2
        # |               LOAD_CONST               1 (('max_revisions',))
        # |               CALL_KW                  3
        # |               UNPACK_SEQUENCE          3
        # |               STORE_FAST_STORE_FAST   35 (g, _)
        # |               STORE_FAST               4 (a)
        # |  87           LOAD_FAST_BORROW         2 (g)
        # |               LOAD_ATTR                7 (invoke + NULL|self)
        # |               LOAD_GLOBAL              9 (seed + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               CALL                     1
        # |               STORE_FAST               5 (out)
        # |  88           LOAD_FAST_BORROW         5 (out)
        # |               LOAD_CONST               2 ('revisions')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               6 (@py_assert0)
        # |               LOAD_SMALL_INT           2
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('==',))
        # |               LOAD_FAST_BORROW         8 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format5)
        # |               LOAD_CONST               5 ('assert %(py6)s')
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_FAST_BORROW         9 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
        # |  89           LOAD_CONST               8 ('仍未通过')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert0, out)
        # |               LOAD_CONST               9 ('done_reason')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              19 (('in',))
        # |               LOAD_FAST_BORROW         8 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              20 (('%(py1)s in %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format5)
        # |               LOAD_CONST               5 ('assert %(py6)s')
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_FAST_BORROW         9 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
        # |  90           LOAD_FAST_BORROW         4 (a)
        # |               LOAD_ATTR               20 (called)
        # |               STORE_FAST              11 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               STORE_FAST_LOAD_FAST   203 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW        12 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       226 (to L6)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('==',))
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              21 (('%(py2)s\n{%(py2)s = %(py0)s.called\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              10 ('py0')
        # |               LOAD_CONST              11 ('a')
        # |               LOAD_GLOBAL             22 (@py_builtins)
        # |               LOAD_ATTR               24 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L3)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               26 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (a)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L4)
        # |               NOT_TAKEN
        # |       L3:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (a)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L5)
        # |       L4:     LOAD_CONST              11 ('a')
        # |       L5:     LOAD_CONST              12 ('py2')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              13 ('py5')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        12 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format6)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               28 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 ('未通过不得归档')
        # |               CALL                     1
        # |               LOAD_CONST              15 ('\n>assert %(py7)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST              16 ('py7')
        # |               LOAD_FAST_BORROW        13 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              14 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        14 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L6:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST              11 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  124 (@py_assert3, @py_assert4)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_judge_not_run_when_gate_fails(self, sample_state):
        'verdict'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  92           RESUME                   0
        # |  93           LOAD_GLOBAL              1 (make + NULL)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               LOAD_GLOBAL              2 (BAD)
        # |               BUILD_LIST               3
        # |               LOAD_GLOBAL              4 (PASS)
        # |               BUILD_LIST               1
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               1 (('max_revisions',))
        # |               CALL_KW                  3
        # |               UNPACK_SEQUENCE          3
        # |               STORE_FAST               2 (g)
        # |               POP_TOP
        # |               STORE_FAST               3 (_)
        # |  94           LOAD_FAST_BORROW         2 (g)
        # |               LOAD_ATTR                7 (invoke + NULL|self)
        # |               LOAD_GLOBAL              9 (seed + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               CALL                     1
        # |               STORE_FAST               4 (out)
        # |  95           LOAD_FAST_BORROW         4 (out)
        # |               LOAD_ATTR               10 (get)
        # |               STORE_FAST               5 (@py_assert1)
        # |               LOAD_CONST               2 ('verdict')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST               7 (@py_assert5)
        # |               LOAD_CONST               3 (None)
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert8, @py_assert5)
        # |               LOAD_FAST_BORROW         8 (@py_assert8)
        # |               IS_OP                    0 (is)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       243 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 (('is',))
        # |               LOAD_FAST_BORROW         9 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} is %(py9)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert5, @py_assert8)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST               5 ('out')
        # |               LOAD_GLOBAL             16 (@py_builtins)
        # |               LOAD_ATTR               18 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (out)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (out)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('out')
        # |       L3:     LOAD_CONST               6 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py6')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py9')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format10)
        # |               LOAD_CONST              10 ('assert %(py11)s')
        # |               LOAD_CONST              11 ('py11')
        # |               LOAD_FAST_BORROW        10 (@py_format10)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format12)
        # |               LOAD_GLOBAL             25 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               26 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format12)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               3 (None)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  152 (@py_assert7, @py_assert8)
        # |               LOAD_CONST               3 (None)
        # |               RETURN_VALUE


class TestSerializability:
    'TestSerializability'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  98           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestSerializability')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          98
    # |               STORE_NAME               3 (__firstlineno__)
    # |  99           LOAD_CONST               1 ('状态要能存进 sqlite，否则断点续跑无从谈起。')
    # |               STORE_NAME               4 (__doc__)
    # | 101           LOAD_CONST               2 (<code object test_state_is_json_serializable at 0x7b190c3700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 101>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_state_is_json_serializable)
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_state_is_json_serializable at 0x7b190c3700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 101>:
    # |  101            RESUME                   0
    # |  102            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               1 (None)
    # |                 IMPORT_NAME              0 (json)
    # |                 STORE_FAST               2 (json)
    # |  104            LOAD_GLOBAL              3 (make + NULL)
    # |                 LOAD_GLOBAL              4 (GOOD)
    # |                 BUILD_LIST               1
    # |                 LOAD_GLOBAL              6 (PASS)
    # |                 BUILD_LIST               1
    # |                 CALL                     2
    # |                 UNPACK_SEQUENCE          3
    # |                 STORE_FAST               3 (g)
    # |                 POP_TOP
    # |                 STORE_FAST               4 (_)
    # |  105            LOAD_FAST_BORROW         3 (g)
    # |                 LOAD_ATTR                9 (invoke + NULL|self)
    # |                 LOAD_GLOBAL             11 (seed + NULL)
    # |                 LOAD_FAST_BORROW         1 (sample_state)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 STORE_FAST               5 (out)
    # |  106            LOAD_FAST_BORROW         5 (out)
    # |                 LOAD_ATTR               13 (items + NULL|self)
    # |                 CALL                     0
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      6 (k)
    # |                 LOAD_FAST_AND_CLEAR      7 (v)
    # |                 SWAP                     3
    # |         L1:     BUILD_MAP                0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                32 (to L5)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST  103 (k, v)
    # |                 LOAD_FAST_BORROW         6 (k)
    # |                 LOAD_ATTR               15 (startswith + NULL|self)
    # |                 LOAD_CONST               2 ('_')
    # |                 CALL                     1
    # |                 TO_BOOL
    # |         L3:     POP_JUMP_IF_FALSE        3 (to L4)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD           30 (to L2)
    # |         L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (k, v)
    # |                 MAP_ADD                  2
    # |                 JUMP_BACKWARD           34 (to L2)
    # |         L5:     END_FOR
    # |                 POP_ITER
    # |         L6:     STORE_FAST               8 (payload)
    # |                 STORE_FAST               6 (k)
    # |                 STORE_FAST               7 (v)
    # |  107            LOAD_FAST_BORROW         2 (json)
    # |                 LOAD_ATTR               16 (dumps)
    # |                 STORE_FAST               9 (@py_assert1)
    # |                 LOAD_CONST               3 (False)
    # |                 STORE_FAST_LOAD_FAST   169 (@py_assert4, @py_assert1)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 138 (payload, @py_assert4)
    # |                 LOAD_CONST               4 (('ensure_ascii',))
    # |                 CALL_KW                  2
    # |                 STORE_FAST_LOAD_FAST   187 (@py_assert6, @py_assert6)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       263 (to L13)
    # |                 NOT_TAKEN
    # |                 LOAD_CONST               5 ('assert %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.dumps\n}(%(py3)s, ensure_ascii=%(py5)s)\n}')
    # |                 LOAD_CONST               6 ('py0')
    # |                 LOAD_CONST               7 ('json')
    # |                 LOAD_GLOBAL             18 (@py_builtins)
    # |                 LOAD_ATTR               20 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (json)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L8)
    # |                 NOT_TAKEN
    # |         L7:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (json)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L9)
    # |         L8:     LOAD_CONST               7 ('json')
    # |         L9:     LOAD_CONST               8 ('py2')
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST               9 ('py3')
    # |                 LOAD_CONST              10 ('payload')
    # |                 LOAD_GLOBAL             18 (@py_builtins)
    # |                 LOAD_ATTR               20 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (payload)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L11)
    # |                 NOT_TAKEN
    # |        L10:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (payload)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L12)
    # |        L11:     LOAD_CONST              10 ('payload')
    # |        L12:     LOAD_CONST              11 ('py5')
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py7')
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                5
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format8)
    # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_format8)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L13:     LOAD_CONST               1 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               9 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  171 (@py_assert4, @py_assert6)
    # |                 LOAD_CONST               1 (None)
    # |                 RETURN_VALUE
    # |   --   L14:     SWAP                     2
    # |                 POP_TOP
    # |  106            SWAP                     3
    # |                 STORE_FAST               7 (v)
    # |                 STORE_FAST               6 (k)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L3 -> L14 [3]
    # |   L4 to L6 -> L14 [3]

    def test_state_is_json_serializable(self, sample_state):
        '_'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  101            RESUME                   0
        # |  102            LOAD_SMALL_INT           0
        # |                 LOAD_CONST               1 (None)
        # |                 IMPORT_NAME              0 (json)
        # |                 STORE_FAST               2 (json)
        # |  104            LOAD_GLOBAL              3 (make + NULL)
        # |                 LOAD_GLOBAL              4 (GOOD)
        # |                 BUILD_LIST               1
        # |                 LOAD_GLOBAL              6 (PASS)
        # |                 BUILD_LIST               1
        # |                 CALL                     2
        # |                 UNPACK_SEQUENCE          3
        # |                 STORE_FAST               3 (g)
        # |                 POP_TOP
        # |                 STORE_FAST               4 (_)
        # |  105            LOAD_FAST_BORROW         3 (g)
        # |                 LOAD_ATTR                9 (invoke + NULL|self)
        # |                 LOAD_GLOBAL             11 (seed + NULL)
        # |                 LOAD_FAST_BORROW         1 (sample_state)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 STORE_FAST               5 (out)
        # |  106            LOAD_FAST_BORROW         5 (out)
        # |                 LOAD_ATTR               13 (items + NULL|self)
        # |                 CALL                     0
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      6 (k)
        # |                 LOAD_FAST_AND_CLEAR      7 (v)
        # |                 SWAP                     3
        # |         L1:     BUILD_MAP                0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                32 (to L5)
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST_STORE_FAST  103 (k, v)
        # |                 LOAD_FAST_BORROW         6 (k)
        # |                 LOAD_ATTR               15 (startswith + NULL|self)
        # |                 LOAD_CONST               2 ('_')
        # |                 CALL                     1
        # |                 TO_BOOL
        # |         L3:     POP_JUMP_IF_FALSE        3 (to L4)
        # |                 NOT_TAKEN
        # |                 JUMP_BACKWARD           30 (to L2)
        # |         L4:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (k, v)
        # |                 MAP_ADD                  2
        # |                 JUMP_BACKWARD           34 (to L2)
        # |         L5:     END_FOR
        # |                 POP_ITER
        # |         L6:     STORE_FAST               8 (payload)
        # |                 STORE_FAST               6 (k)
        # |                 STORE_FAST               7 (v)
        # |  107            LOAD_FAST_BORROW         2 (json)
        # |                 LOAD_ATTR               16 (dumps)
        # |                 STORE_FAST               9 (@py_assert1)
        # |                 LOAD_CONST               3 (False)
        # |                 STORE_FAST_LOAD_FAST   169 (@py_assert4, @py_assert1)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 138 (payload, @py_assert4)
        # |                 LOAD_CONST               4 (('ensure_ascii',))
        # |                 CALL_KW                  2
        # |                 STORE_FAST_LOAD_FAST   187 (@py_assert6, @py_assert6)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       263 (to L13)
        # |                 NOT_TAKEN
        # |                 LOAD_CONST               5 ('assert %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.dumps\n}(%(py3)s, ensure_ascii=%(py5)s)\n}')
        # |                 LOAD_CONST               6 ('py0')
        # |                 LOAD_CONST               7 ('json')
        # |                 LOAD_GLOBAL             18 (@py_builtins)
        # |                 LOAD_ATTR               20 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (json)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L8)
        # |                 NOT_TAKEN
        # |         L7:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (json)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L9)
        # |         L8:     LOAD_CONST               7 ('json')
        # |         L9:     LOAD_CONST               8 ('py2')
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST               9 ('py3')
        # |                 LOAD_CONST              10 ('payload')
        # |                 LOAD_GLOBAL             18 (@py_builtins)
        # |                 LOAD_ATTR               20 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (payload)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L11)
        # |                 NOT_TAKEN
        # |        L10:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (payload)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L12)
        # |        L11:     LOAD_CONST              10 ('payload')
        # |        L12:     LOAD_CONST              11 ('py5')
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py7')
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                5
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format8)
        # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_format8)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L13:     LOAD_CONST               1 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               9 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  171 (@py_assert4, @py_assert6)
        # |                 LOAD_CONST               1 (None)
        # |                 RETURN_VALUE
        # |   --   L14:     SWAP                     2
        # |                 POP_TOP
        # |  106            SWAP                     3
        # |                 STORE_FAST               7 (v)
        # |                 STORE_FAST               6 (k)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L3 -> L14 [3]
        # |   L4 to L6 -> L14 [3]


class TestCheckpointResume:
    'TestCheckpointResume'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 110           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestCheckpointResume')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         110
    # |               STORE_NAME               3 (__firstlineno__)
    # | 111           LOAD_CONST               1 ('图层存在的唯一理由。第 3 章两次崩在缝合，没有 checkpoint 就得从出细纲\n重来 —— 三场写好的正文（$0.07）连同十几分钟一起作废。')
    # |               STORE_NAME               4 (__doc__)
    # | 114           LOAD_NAME                5 (PASS)
    # |               BUILD_TUPLE              1
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               2 (<code object _pipeline at 0x101b4a0b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 114>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE   1 (defaults)
    # |               STORE_NAME               6 (_pipeline)
    # | 123           LOAD_CONST               3 (<code object test_resumes_at_the_node_that_crashed at 0x7b191fea00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 123>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_resumes_at_the_node_that_crashed)
    # | 151           LOAD_CONST               4 (<code object test_a_finished_chapter_has_nothing_left_to_run at 0x7b191e2300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 151>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_a_finished_chapter_has_nothing_left_to_run)
    # | 163           LOAD_CONST               5 (<code object test_each_chapter_is_its_own_thread at 0x7b191e1e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 163>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_each_chapter_is_its_own_thread)
    # | 176           LOAD_CONST               6 (<code object test_state_survives_a_real_sqlite_roundtrip at 0x7b18e22a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 176>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_state_survives_a_real_sqlite_roundtrip)
    # |               LOAD_CONST               7 (())
    # |               STORE_NAME              11 (__static_attributes__)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object _pipeline at 0x101b4a0b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 114>:
    # | 114           RESUME                   0
    # | 115           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('ChapterPipeline',))
    # |               IMPORT_NAME              0 (novel_agent.agents.pipeline)
    # |               IMPORT_FROM              1 (ChapterPipeline)
    # |               STORE_FAST               4 (ChapterPipeline)
    # |               POP_TOP
    # | 117           LOAD_FAST_BORROW         4 (ChapterPipeline)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (())
    # |               LOAD_CONST               2 ('architect')
    # | 118           LOAD_GLOBAL              5 (FakeArchitect + NULL)
    # |               CALL                     0
    # | 117           LOAD_CONST               3 ('writer')
    # | 118           LOAD_GLOBAL              7 (FakeWriter + NULL)
    # |               LOAD_CONST               4 ('场景一')
    # |               LOAD_CONST               5 ('场景二')
    # |               BUILD_LIST               2
    # |               CALL                     1
    # | 117           LOAD_CONST               6 ('stitcher')
    # | 119           LOAD_FAST_BORROW         1 (stitcher)
    # | 117           LOAD_CONST               7 ('gate')
    # | 119           LOAD_GLOBAL              8 (Gate)
    # |               LOAD_ATTR               10 (from_config)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             12 (CONFIG)
    # |               CALL                     1
    # | 117           LOAD_CONST               8 ('judge')
    # | 120           LOAD_GLOBAL             15 (FakeJudge + NULL)
    # |               LOAD_GLOBAL             17 (list + NULL)
    # |               LOAD_FAST_BORROW         2 (verdicts)
    # |               CALL                     1
    # |               CALL                     1
    # | 117           LOAD_CONST               9 ('archivist')
    # | 120           LOAD_GLOBAL             19 (FakeArchivist + NULL)
    # |               CALL                     0
    # | 117           LOAD_CONST              10 ('max_revisions')
    # | 121           LOAD_SMALL_INT           2
    # | 117           LOAD_CONST              11 ('log')
    # | 121           LOAD_CONST              12 (<code object <lambda> at 0x10671dfb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 121>)
    # |               MAKE_FUNCTION
    # | 117           BUILD_MAP                8
    # | 121           LOAD_FAST_BORROW         3 (kw)
    # | 117           DICT_MERGE               1
    # |               CALL_FUNCTION_EX
    # |               RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x10671dfb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 121>:
    # | 121           RESUME                   0
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_resumes_at_the_node_that_crashed at 0x7b191fea00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 123>:
    # |  123            RESUME                   0
    # |  124            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               1 (('checkpointed_graph',))
    # |                 IMPORT_NAME              0 (novel_agent.graph.build)
    # |                 IMPORT_FROM              1 (checkpointed_graph)
    # |                 STORE_FAST               3 (checkpointed_graph)
    # |                 POP_TOP
    # |  126            LOAD_BUILD_CLASS
    # |                 PUSH_NULL
    # |                 LOAD_CONST               2 (<code object FlakyStitcher at 0x10664f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 126>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_CONST               3 ('FlakyStitcher')
    # |                 CALL                     2
    # |                 STORE_FAST               4 (FlakyStitcher)
    # |  134            LOAD_FAST_BORROW         4 (FlakyStitcher)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 STORE_FAST               5 (st)
    # |  135            LOAD_FAST_BORROW         0 (self)
    # |                 LOAD_ATTR                5 (_pipeline + NULL|self)
    # |                 LOAD_FAST_BORROW         5 (st)
    # |                 CALL                     1
    # |                 STORE_FAST               6 (p)
    # |  136            LOAD_FAST_BORROW         2 (tmp_path)
    # |                 LOAD_CONST               4 ('cp.sqlite')
    # |                 BINARY_OP               11 (/)
    # |                 LOAD_CONST               5 ('configurable')
    # |                 LOAD_CONST               6 ('thread_id')
    # |                 LOAD_CONST               7 ('t1')
    # |                 BUILD_MAP                1
    # |                 BUILD_MAP                1
    # |                 STORE_FAST_STORE_FAST  135 (cfg, db)
    # |  138            LOAD_FAST_BORROW         3 (checkpointed_graph)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (p, db)
    # |                 CALL                     2
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     STORE_FAST               9 (g)
    # |  139            LOAD_GLOBAL              6 (pytest)
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
    # |         L2:     POP_TOP
    # |  140            LOAD_FAST_BORROW         9 (g)
    # |                 LOAD_ATTR               13 (invoke + NULL|self)
    # |                 LOAD_GLOBAL             15 (seed + NULL)
    # |                 LOAD_FAST_BORROW         1 (sample_state)
    # |                 CALL                     1
    # |                 LOAD_FAST_BORROW         8 (cfg)
    # |                 CALL                     2
    # |                 POP_TOP
    # |  139    L3:     LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  138    L4:     LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  142    L5:     LOAD_FAST_BORROW         3 (checkpointed_graph)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (p, db)
    # |                 CALL                     2
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L6:     STORE_FAST               9 (g)
    # |  143            LOAD_FAST_BORROW         9 (g)
    # |                 LOAD_ATTR               16 (get_state)
    # |                 STORE_FAST_LOAD_FAST   170 (@py_assert1, @py_assert1)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (cfg)
    # |                 CALL                     1
    # |                 STORE_FAST_LOAD_FAST   187 (@py_assert4, @py_assert4)
    # |                 LOAD_ATTR               18 (next)
    # |                 STORE_FAST              12 (@py_assert6)
    # |                 LOAD_CONST              33 (('stitch',))
    # |                 STORE_FAST_LOAD_FAST   220 (@py_assert9, @py_assert6)
    # |                 LOAD_FAST_BORROW        13 (@py_assert9)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   238 (@py_assert8, @py_assert8)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       348 (to L15)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              34 (('==',))
    # |                 LOAD_FAST_BORROW        14 (@py_assert8)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              35 (('%(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.get_state\n}(%(py3)s)\n}.next\n} == %(py10)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 205 (@py_assert6, @py_assert9)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               9 ('py0')
    # |                 LOAD_CONST              10 ('g')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (g)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L9)
    # |         L7:     NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (g)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST              10 ('g')
    # |        L10:     LOAD_CONST              11 ('py2')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py3')
    # |                 LOAD_CONST              13 ('cfg')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L12)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (cfg)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L13)
    # |        L11:     NOT_TAKEN
    # |        L12:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (cfg)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L14)
    # |        L13:     LOAD_CONST              13 ('cfg')
    # |        L14:     LOAD_CONST              14 ('py5')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py7')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 CALL                     1
    # |                 LOAD_CONST              16 ('py10')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_assert9)
    # |                 CALL                     1
    # |                 BUILD_MAP                6
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              15 (@py_format11)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              17 ('该停在崩掉的那个节点前')
    # |                 CALL                     1
    # |                 LOAD_CONST              18 ('\n>assert %(py12)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              19 ('py12')
    # |                 LOAD_FAST_BORROW        15 (@py_format11)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              16 (@py_format13)
    # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               36 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        16 (@py_format13)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L15:     LOAD_CONST               8 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST              11 (@py_assert4)
    # |                 COPY                     1
    # |                 STORE_FAST              12 (@py_assert6)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  237 (@py_assert8, @py_assert9)
    # |  144            LOAD_FAST_BORROW         9 (g)
    # |                 LOAD_ATTR               13 (invoke + NULL|self)
    # |                 LOAD_CONST               8 (None)
    # |                 LOAD_FAST_BORROW         8 (cfg)
    # |                 CALL                     2
    # |                 STORE_FAST              17 (out)
    # |  142   L16:     LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  146   L17:     LOAD_FAST_CHECK         17 (out)
    # |                 LOAD_CONST              20 ('done_reason')
    # |                 BINARY_OP               26 ([])
    # |                 STORE_FAST              18 (@py_assert0)
    # |                 LOAD_CONST              21 ('passed')
    # |                 STORE_FAST              19 (@py_assert3)
    # |                 LOAD_FAST_BORROW        18 (@py_assert0)
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST              20 (@py_assert2)
    # |                 LOAD_FAST_BORROW        20 (@py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       122 (to L18)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              34 (('==',))
    # |                 LOAD_FAST_BORROW        20 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              36 (('%(py1)s == %(py4)s',))
    # |                 LOAD_FAST_BORROW        18 (@py_assert0)
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST              22 ('py1')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        18 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST              23 ('py4')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              21 (@py_format5)
    # |                 LOAD_CONST              24 ('assert %(py6)s')
    # |                 LOAD_CONST              25 ('py6')
    # |                 LOAD_FAST_BORROW        21 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              22 (@py_format7)
    # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               36 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        22 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L18:     LOAD_CONST               8 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              18 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST              20 (@py_assert2)
    # |                 STORE_FAST              19 (@py_assert3)
    # |  147            LOAD_FAST_BORROW         6 (p)
    # |                 LOAD_ATTR               38 (architect)
    # |                 STORE_FAST_LOAD_FAST   170 (@py_assert1, @py_assert1)
    # |                 LOAD_ATTR               40 (calls)
    # |                 STORE_FAST              19 (@py_assert3)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST              12 (@py_assert6)
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST              23 (@py_assert5)
    # |                 LOAD_FAST_BORROW        23 (@py_assert5)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       249 (to L22)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              34 (('==',))
    # |                 LOAD_FAST_BORROW        23 (@py_assert5)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              37 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.architect\n}.calls\n} == %(py7)s',))
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               9 ('py0')
    # |                 LOAD_CONST              26 ('p')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L19)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (p)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L20)
    # |                 NOT_TAKEN
    # |        L19:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (p)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L21)
    # |        L20:     LOAD_CONST              26 ('p')
    # |        L21:     LOAD_CONST              11 ('py2')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              23 ('py4')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py7')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              24 (@py_format8)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              27 ('续跑不该重出细纲')
    # |                 CALL                     1
    # |                 LOAD_CONST              28 ('\n>assert %(py9)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              29 ('py9')
    # |                 LOAD_FAST_BORROW        24 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              25 (@py_format10)
    # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               36 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        25 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L22:     LOAD_CONST               8 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST              19 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST              23 (@py_assert5)
    # |                 STORE_FAST              12 (@py_assert6)
    # |  148            LOAD_FAST_BORROW         6 (p)
    # |                 LOAD_ATTR               42 (writer)
    # |                 STORE_FAST_LOAD_FAST   170 (@py_assert1, @py_assert1)
    # |                 LOAD_ATTR               40 (calls)
    # |                 STORE_FAST              19 (@py_assert3)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST              12 (@py_assert6)
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST              23 (@py_assert5)
    # |                 LOAD_FAST_BORROW        23 (@py_assert5)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       249 (to L26)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              34 (('==',))
    # |                 LOAD_FAST_BORROW        23 (@py_assert5)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              38 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.calls\n} == %(py7)s',))
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               9 ('py0')
    # |                 LOAD_CONST              26 ('p')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L23)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (p)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L24)
    # |                 NOT_TAKEN
    # |        L23:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (p)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L25)
    # |        L24:     LOAD_CONST              26 ('p')
    # |        L25:     LOAD_CONST              11 ('py2')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              23 ('py4')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py7')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              24 (@py_format8)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              30 ('续跑不该重写场景')
    # |                 CALL                     1
    # |                 LOAD_CONST              28 ('\n>assert %(py9)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              29 ('py9')
    # |                 LOAD_FAST_BORROW        24 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              25 (@py_format10)
    # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               36 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        25 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L26:     LOAD_CONST               8 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST              19 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST              23 (@py_assert5)
    # |                 STORE_FAST              12 (@py_assert6)
    # |  149            LOAD_FAST_BORROW         5 (st)
    # |                 LOAD_ATTR               40 (calls)
    # |                 STORE_FAST              10 (@py_assert1)
    # |                 LOAD_SMALL_INT           2
    # |                 STORE_FAST_LOAD_FAST   186 (@py_assert4, @py_assert1)
    # |                 LOAD_FAST_BORROW        11 (@py_assert4)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST              19 (@py_assert3)
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       199 (to L30)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              34 (('==',))
    # |                 LOAD_FAST_BORROW        19 (@py_assert3)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              39 (('%(py2)s\n{%(py2)s = %(py0)s.calls\n} == %(py5)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert1, @py_assert4)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               9 ('py0')
    # |                 LOAD_CONST              31 ('st')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L27)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (st)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L28)
    # |                 NOT_TAKEN
    # |        L27:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (st)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L29)
    # |        L28:     LOAD_CONST              31 ('st')
    # |        L29:     LOAD_CONST              11 ('py2')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              14 ('py5')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert4)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              26 (@py_format6)
    # |                 LOAD_CONST              32 ('assert %(py7)s')
    # |                 LOAD_CONST              15 ('py7')
    # |                 LOAD_FAST_BORROW        26 (@py_format6)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              24 (@py_format8)
    # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               36 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        24 (@py_format8)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L30:     LOAD_CONST               8 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST              19 (@py_assert3)
    # |                 STORE_FAST              11 (@py_assert4)
    # |                 LOAD_CONST               8 (None)
    # |                 RETURN_VALUE
    # |  139   L31:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L32)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L32:     POP_TOP
    # |        L33:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             5
    # |                 JUMP_BACKWARD_NO_INTERRUPT 1439 (to L4)
    # |   --   L34:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # |  138   L35:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L36)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L36:     POP_TOP
    # |        L37:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             5
    # |                 JUMP_BACKWARD_NO_INTERRUPT 1451 (to L5)
    # |   --   L38:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # |  142   L39:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L40)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L40:     POP_TOP
    # |        L41:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             4
    # |                 JUMP_BACKWARD_NO_INTERRUPT 1028 (to L17)
    # |   --   L42:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L35 [2] lasti
    # |   L2 to L3 -> L31 [4] lasti
    # |   L3 to L4 -> L35 [2] lasti
    # |   L6 to L7 -> L39 [2] lasti
    # |   L8 to L11 -> L39 [2] lasti
    # |   L12 to L16 -> L39 [2] lasti
    # |   L31 to L33 -> L34 [6] lasti
    # |   L33 to L35 -> L35 [2] lasti
    # |   L35 to L37 -> L38 [4] lasti
    # |   L39 to L41 -> L42 [4] lasti
    # | Disassembly of <code object FlakyStitcher at 0x10664f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 126>:
    # | 126           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestCheckpointResume.test_resumes_at_the_node_that_crashed.<locals>.FlakyStitcher')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         126
    # |               STORE_NAME               3 (__firstlineno__)
    # | 127           LOAD_CONST               1 (<code object __init__ at 0x10666ac40, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 127>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (__init__)
    # | 128           LOAD_CONST               2 (<code object stitch at 0x106690960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 128>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (stitch)
    # |               LOAD_CONST               3 (('calls',))
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x10666ac40, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 127>:
    # | 127           RESUME                   0
    # |               LOAD_SMALL_INT           0
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               0 (calls)
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object stitch at 0x106690960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 128>:
    # | 128           RESUME                   0
    # | 129           LOAD_FAST_BORROW         0 (self)
    # |               COPY                     1
    # |               LOAD_ATTR                0 (calls)
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               13 (+=)
    # |               SWAP                     2
    # |               STORE_ATTR               0 (calls)
    # | 130           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (calls)
    # |               LOAD_SMALL_INT           1
    # |               COMPARE_OP              88 (bool(==))
    # |               POP_JUMP_IF_FALSE       12 (to L1)
    # |               NOT_TAKEN
    # | 131           LOAD_GLOBAL              3 (RuntimeError + NULL)
    # |               LOAD_CONST               1 ('上游 403')
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # | 132   L1:     LOAD_GLOBAL              4 (GOOD)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_a_finished_chapter_has_nothing_left_to_run at 0x7b191e2300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 151>:
    # |  151            RESUME                   0
    # |  152            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               1 (('checkpointed_graph',))
    # |                 IMPORT_NAME              0 (novel_agent.graph.build)
    # |                 IMPORT_FROM              1 (checkpointed_graph)
    # |                 STORE_FAST               3 (checkpointed_graph)
    # |                 POP_TOP
    # |  154            LOAD_BUILD_CLASS
    # |                 PUSH_NULL
    # |                 LOAD_CONST               2 (<code object OkStitcher at 0x10666a880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 154>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_CONST               3 ('OkStitcher')
    # |                 CALL                     2
    # |                 STORE_FAST               4 (OkStitcher)
    # |  157            LOAD_FAST_BORROW         0 (self)
    # |                 LOAD_ATTR                5 (_pipeline + NULL|self)
    # |                 LOAD_FAST_BORROW         4 (OkStitcher)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 STORE_FAST               5 (p)
    # |  158            LOAD_FAST_BORROW         2 (tmp_path)
    # |                 LOAD_CONST               4 ('cp.sqlite')
    # |                 BINARY_OP               11 (/)
    # |                 LOAD_CONST               5 ('configurable')
    # |                 LOAD_CONST               6 ('thread_id')
    # |                 LOAD_CONST               7 ('t2')
    # |                 BUILD_MAP                1
    # |                 BUILD_MAP                1
    # |                 STORE_FAST_STORE_FAST  118 (cfg, db)
    # |  159            LOAD_FAST_BORROW         3 (checkpointed_graph)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (p, db)
    # |                 CALL                     2
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     STORE_FAST               8 (g)
    # |  160            LOAD_FAST_BORROW         8 (g)
    # |                 LOAD_ATTR                7 (invoke + NULL|self)
    # |                 LOAD_GLOBAL              9 (seed + NULL)
    # |                 LOAD_FAST_BORROW         1 (sample_state)
    # |                 CALL                     1
    # |                 LOAD_FAST_BORROW         7 (cfg)
    # |                 CALL                     2
    # |                 POP_TOP
    # |  161            LOAD_FAST_BORROW         8 (g)
    # |                 LOAD_ATTR               10 (get_state)
    # |                 STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (cfg)
    # |                 CALL                     1
    # |                 STORE_FAST_LOAD_FAST   170 (@py_assert4, @py_assert4)
    # |                 LOAD_ATTR               12 (next)
    # |                 STORE_FAST              11 (@py_assert6)
    # |                 LOAD_CONST              20 (())
    # |                 STORE_FAST_LOAD_FAST   203 (@py_assert9, @py_assert6)
    # |                 LOAD_FAST_BORROW        12 (@py_assert9)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   221 (@py_assert8, @py_assert8)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       348 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              21 (('==',))
    # |                 LOAD_FAST_BORROW        13 (@py_assert8)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              22 (('%(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.get_state\n}(%(py3)s)\n}.next\n} == %(py10)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert6, @py_assert9)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               8 ('py0')
    # |                 LOAD_CONST               9 ('g')
    # |                 LOAD_GLOBAL             18 (@py_builtins)
    # |                 LOAD_ATTR               20 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L3)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (g)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L4)
    # |         L2:     NOT_TAKEN
    # |         L3:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (g)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L5)
    # |         L4:     LOAD_CONST               9 ('g')
    # |         L5:     LOAD_CONST              10 ('py2')
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              11 ('py3')
    # |                 LOAD_CONST              12 ('cfg')
    # |                 LOAD_GLOBAL             18 (@py_builtins)
    # |                 LOAD_ATTR               20 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (cfg)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L8)
    # |         L6:     NOT_TAKEN
    # |         L7:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (cfg)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L9)
    # |         L8:     LOAD_CONST              12 ('cfg')
    # |         L9:     LOAD_CONST              13 ('py5')
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST              14 ('py7')
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert6)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py10')
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_assert9)
    # |                 CALL                     1
    # |                 BUILD_MAP                6
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              14 (@py_format11)
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              16 ('跑完的章节不该被当成中断')
    # |                 CALL                     1
    # |                 LOAD_CONST              17 ('\n>assert %(py12)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              18 ('py12')
    # |                 LOAD_FAST_BORROW        14 (@py_format11)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              15 (@py_format13)
    # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        15 (@py_format13)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L10:     LOAD_CONST              19 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               9 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert4)
    # |                 COPY                     1
    # |                 STORE_FAST              11 (@py_assert6)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  220 (@py_assert8, @py_assert9)
    # |  159   L11:     LOAD_CONST              19 (None)
    # |                 LOAD_CONST              19 (None)
    # |                 LOAD_CONST              19 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |                 LOAD_CONST              19 (None)
    # |                 RETURN_VALUE
    # |        L12:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L13)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L13:     POP_TOP
    # |        L14:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 LOAD_CONST              19 (None)
    # |                 RETURN_VALUE
    # |   --   L15:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L12 [2] lasti
    # |   L3 to L6 -> L12 [2] lasti
    # |   L7 to L11 -> L12 [2] lasti
    # |   L12 to L14 -> L15 [4] lasti
    # | Disassembly of <code object OkStitcher at 0x10666a880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 154>:
    # | 154           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestCheckpointResume.test_a_finished_chapter_has_nothing_left_to_run.<locals>.OkStitcher')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         154
    # |               STORE_NAME               3 (__firstlineno__)
    # | 155           LOAD_CONST               1 (<code object stitch at 0x10671e170, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 155>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (stitch)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object stitch at 0x10671e170, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 155>:
    # | 155           RESUME                   0
    # |               LOAD_GLOBAL              0 (GOOD)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_each_chapter_is_its_own_thread at 0x7b191e1e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 163>:
    # |  163            RESUME                   0
    # |  165            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               1 (('checkpointed_graph',))
    # |                 IMPORT_NAME              0 (novel_agent.graph.build)
    # |                 IMPORT_FROM              1 (checkpointed_graph)
    # |                 STORE_FAST               3 (checkpointed_graph)
    # |                 POP_TOP
    # |  167            LOAD_BUILD_CLASS
    # |                 PUSH_NULL
    # |                 LOAD_CONST               2 (<code object OkStitcher at 0x10666b2d0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 167>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_CONST               3 ('OkStitcher')
    # |                 CALL                     2
    # |                 STORE_FAST               4 (OkStitcher)
    # |  170            LOAD_FAST_BORROW         0 (self)
    # |                 LOAD_ATTR                5 (_pipeline + NULL|self)
    # |                 LOAD_FAST_BORROW         4 (OkStitcher)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 LOAD_GLOBAL              6 (PASS)
    # |                 LOAD_GLOBAL              6 (PASS)
    # |                 BUILD_TUPLE              2
    # |                 LOAD_CONST               4 (('verdicts',))
    # |                 CALL_KW                  2
    # |                 STORE_FAST               5 (p)
    # |  171            LOAD_FAST_BORROW         2 (tmp_path)
    # |                 LOAD_CONST               5 ('cp.sqlite')
    # |                 BINARY_OP               11 (/)
    # |                 STORE_FAST               6 (db)
    # |  172            LOAD_FAST_BORROW         3 (checkpointed_graph)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (p, db)
    # |                 CALL                     2
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     STORE_FAST               7 (g)
    # |  173            LOAD_FAST_BORROW         7 (g)
    # |                 LOAD_ATTR                9 (invoke + NULL|self)
    # |                 LOAD_GLOBAL             11 (seed + NULL)
    # |                 LOAD_FAST_BORROW         1 (sample_state)
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_CONST               6 (('ch',))
    # |                 CALL_KW                  2
    # |                 LOAD_CONST               7 ('configurable')
    # |                 LOAD_CONST               8 ('thread_id')
    # |                 LOAD_CONST               9 ('ch1')
    # |                 BUILD_MAP                1
    # |                 BUILD_MAP                1
    # |                 CALL                     2
    # |                 POP_TOP
    # |  174            LOAD_FAST_BORROW         7 (g)
    # |                 LOAD_ATTR               12 (get_state)
    # |                 STORE_FAST               8 (@py_assert1)
    # |                 LOAD_CONST               7 ('configurable')
    # |                 LOAD_CONST               8 ('thread_id')
    # |                 LOAD_CONST              10 ('ch2')
    # |                 BUILD_MAP                1
    # |                 BUILD_MAP                1
    # |                 STORE_FAST_LOAD_FAST   152 (@py_assert3, @py_assert1)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert3)
    # |                 CALL                     1
    # |                 STORE_FAST_LOAD_FAST   170 (@py_assert5, @py_assert5)
    # |                 LOAD_ATTR               14 (next)
    # |                 STORE_FAST              11 (@py_assert7)
    # |                 LOAD_CONST              21 (())
    # |                 STORE_FAST_LOAD_FAST   203 (@py_assert10, @py_assert7)
    # |                 LOAD_FAST_BORROW        12 (@py_assert10)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   221 (@py_assert9, @py_assert9)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       265 (to L6)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              22 (('==',))
    # |                 LOAD_FAST_BORROW        13 (@py_assert9)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              23 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get_state\n}(%(py4)s)\n}.next\n} == %(py11)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert7, @py_assert10)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST              11 ('py0')
    # |                 LOAD_CONST              12 ('g')
    # |                 LOAD_GLOBAL             20 (@py_builtins)
    # |                 LOAD_ATTR               22 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L3)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (g)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L4)
    # |         L2:     NOT_TAKEN
    # |         L3:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (g)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L5)
    # |         L4:     LOAD_CONST              12 ('g')
    # |         L5:     LOAD_CONST              13 ('py2')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              14 ('py4')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py6')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert5)
    # |                 CALL                     1
    # |                 LOAD_CONST              16 ('py8')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert7)
    # |                 CALL                     1
    # |                 LOAD_CONST              17 ('py11')
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_assert10)
    # |                 CALL                     1
    # |                 BUILD_MAP                6
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              14 (@py_format12)
    # |                 LOAD_CONST              18 ('assert %(py13)s')
    # |                 LOAD_CONST              19 ('py13')
    # |                 LOAD_FAST_BORROW        14 (@py_format12)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              15 (@py_format14)
    # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             16 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        15 (@py_format14)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L6:     LOAD_CONST              20 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               8 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST               9 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert5)
    # |                 COPY                     1
    # |                 STORE_FAST              11 (@py_assert7)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  220 (@py_assert9, @py_assert10)
    # |  172    L7:     LOAD_CONST              20 (None)
    # |                 LOAD_CONST              20 (None)
    # |                 LOAD_CONST              20 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |                 LOAD_CONST              20 (None)
    # |                 RETURN_VALUE
    # |         L8:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L9)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |         L9:     POP_TOP
    # |        L10:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 LOAD_CONST              20 (None)
    # |                 RETURN_VALUE
    # |   --   L11:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L8 [2] lasti
    # |   L3 to L7 -> L8 [2] lasti
    # |   L8 to L10 -> L11 [4] lasti
    # | Disassembly of <code object OkStitcher at 0x10666b2d0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 167>:
    # | 167           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestCheckpointResume.test_each_chapter_is_its_own_thread.<locals>.OkStitcher')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         167
    # |               STORE_NAME               3 (__firstlineno__)
    # | 168           LOAD_CONST               1 (<code object stitch at 0x10671e250, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 168>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (stitch)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object stitch at 0x10671e250, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 168>:
    # | 168           RESUME                   0
    # |               LOAD_GLOBAL              0 (GOOD)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_state_survives_a_real_sqlite_roundtrip at 0x7b18e22a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 176>:
    # |  176            RESUME                   0
    # |  179            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               1 (('checkpointed_graph',))
    # |                 IMPORT_NAME              0 (novel_agent.graph.build)
    # |                 IMPORT_FROM              1 (checkpointed_graph)
    # |                 STORE_FAST               3 (checkpointed_graph)
    # |                 POP_TOP
    # |  181            LOAD_BUILD_CLASS
    # |                 PUSH_NULL
    # |                 LOAD_CONST               2 (<code object OkStitcher at 0x10666b3c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 181>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_CONST               3 ('OkStitcher')
    # |                 CALL                     2
    # |                 STORE_FAST               4 (OkStitcher)
    # |  184            LOAD_FAST_BORROW         0 (self)
    # |                 LOAD_ATTR                5 (_pipeline + NULL|self)
    # |                 LOAD_FAST_BORROW         4 (OkStitcher)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 STORE_FAST               5 (p)
    # |  185            LOAD_FAST_BORROW         2 (tmp_path)
    # |                 LOAD_CONST               4 ('cp.sqlite')
    # |                 BINARY_OP               11 (/)
    # |                 LOAD_CONST               5 ('configurable')
    # |                 LOAD_CONST               6 ('thread_id')
    # |                 LOAD_CONST               7 ('t3')
    # |                 BUILD_MAP                1
    # |                 BUILD_MAP                1
    # |                 STORE_FAST_STORE_FAST  118 (cfg, db)
    # |  186            LOAD_FAST_BORROW         3 (checkpointed_graph)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (p, db)
    # |                 CALL                     2
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     STORE_FAST               8 (g)
    # |  187            LOAD_FAST_BORROW         8 (g)
    # |                 LOAD_ATTR                7 (invoke + NULL|self)
    # |                 LOAD_GLOBAL              9 (seed + NULL)
    # |                 LOAD_FAST_BORROW         1 (sample_state)
    # |                 CALL                     1
    # |                 LOAD_FAST_BORROW         7 (cfg)
    # |                 CALL                     2
    # |                 POP_TOP
    # |  186    L2:     LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  188    L3:     LOAD_FAST_BORROW         3 (checkpointed_graph)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (p, db)
    # |                 CALL                     2
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L4:     STORE_FAST               8 (g)
    # |  189            LOAD_FAST_BORROW         8 (g)
    # |                 LOAD_ATTR               11 (get_state + NULL|self)
    # |                 LOAD_FAST_BORROW         7 (cfg)
    # |                 CALL                     1
    # |                 LOAD_ATTR               12 (values)
    # |                 STORE_FAST               9 (values)
    # |  188    L5:     LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 LOAD_CONST               8 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  190    L6:     LOAD_FAST_CHECK          9 (values)
    # |                 LOAD_CONST               9 ('done_reason')
    # |                 BINARY_OP               26 ([])
    # |                 STORE_FAST              10 (@py_assert0)
    # |                 LOAD_CONST              10 ('passed')
    # |                 STORE_FAST_LOAD_FAST   186 (@py_assert3, @py_assert0)
    # |                 LOAD_FAST_BORROW        11 (@py_assert3)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   204 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       121 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              20 (('==',))
    # |                 LOAD_FAST_BORROW        12 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              21 (('%(py1)s == %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST              11 ('py1')
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py4')
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format5)
    # |                 LOAD_CONST              13 ('assert %(py6)s')
    # |                 LOAD_CONST              14 ('py6')
    # |                 LOAD_FAST_BORROW        13 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              14 (@py_format7)
    # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        14 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST               8 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  203 (@py_assert2, @py_assert3)
    # |  191            LOAD_CONST              15 (<code object <genexpr> at 0x10666eaf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 191>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_FAST_BORROW         9 (values)
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 STORE_FAST              15 (@py_assert1)
    # |                 LOAD_GLOBAL             25 (all + NULL)
    # |                 LOAD_FAST_BORROW        15 (@py_assert1)
    # |                 CALL                     1
    # |                 STORE_FAST_LOAD_FAST   187 (@py_assert3, @py_assert3)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       171 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_CONST              16 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |                 LOAD_CONST              17 ('py0')
    # |                 LOAD_CONST              18 ('all')
    # |                 LOAD_GLOBAL             26 (@py_builtins)
    # |                 LOAD_ATTR               28 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             24 (all)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             24 (all)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST              18 ('all')
    # |        L10:     LOAD_CONST              19 ('py2')
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        15 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py4')
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format5)
    # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_format5)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST               8 (None)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  251 (@py_assert1, @py_assert3)
    # |                 LOAD_CONST               8 (None)
    # |                 RETURN_VALUE
    # |  186   L12:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L13)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L13:     POP_TOP
    # |        L14:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             1
    # |                 JUMP_BACKWARD_NO_INTERRUPT 418 (to L3)
    # |   --   L15:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # |  188   L16:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L17)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L17:     POP_TOP
    # |        L18:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 EXTENDED_ARG             1
    # |                 JUMP_BACKWARD_NO_INTERRUPT 386 (to L6)
    # |   --   L19:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L12 [2] lasti
    # |   L4 to L5 -> L16 [2] lasti
    # |   L12 to L14 -> L15 [4] lasti
    # |   L16 to L18 -> L19 [4] lasti
    # | Disassembly of <code object OkStitcher at 0x10666b3c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 181>:
    # | 181           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestCheckpointResume.test_state_survives_a_real_sqlite_roundtrip.<locals>.OkStitcher')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         181
    # |               STORE_NAME               3 (__firstlineno__)
    # | 182           LOAD_CONST               1 (<code object stitch at 0x10671e410, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 182>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (stitch)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object stitch at 0x10671e410, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 182>:
    # | 182           RESUME                   0
    # |               LOAD_GLOBAL              0 (GOOD)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10666eaf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 191>:
    # |  191           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                26 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (k, k)
    # |                LOAD_ATTR                1 (startswith + NULL|self)
    # |                LOAD_CONST               0 ('_')
    # |                CALL                     1
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           28 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti

    def _pipeline(self, stitcher, verdicts, **kw):
        'architect'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 114           RESUME                   0
        # | 115           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('ChapterPipeline',))
        # |               IMPORT_NAME              0 (novel_agent.agents.pipeline)
        # |               IMPORT_FROM              1 (ChapterPipeline)
        # |               STORE_FAST               4 (ChapterPipeline)
        # |               POP_TOP
        # | 117           LOAD_FAST_BORROW         4 (ChapterPipeline)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (())
        # |               LOAD_CONST               2 ('architect')
        # | 118           LOAD_GLOBAL              5 (FakeArchitect + NULL)
        # |               CALL                     0
        # | 117           LOAD_CONST               3 ('writer')
        # | 118           LOAD_GLOBAL              7 (FakeWriter + NULL)
        # |               LOAD_CONST               4 ('场景一')
        # |               LOAD_CONST               5 ('场景二')
        # |               BUILD_LIST               2
        # |               CALL                     1
        # | 117           LOAD_CONST               6 ('stitcher')
        # | 119           LOAD_FAST_BORROW         1 (stitcher)
        # | 117           LOAD_CONST               7 ('gate')
        # | 119           LOAD_GLOBAL              8 (Gate)
        # |               LOAD_ATTR               10 (from_config)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             12 (CONFIG)
        # |               CALL                     1
        # | 117           LOAD_CONST               8 ('judge')
        # | 120           LOAD_GLOBAL             15 (FakeJudge + NULL)
        # |               LOAD_GLOBAL             17 (list + NULL)
        # |               LOAD_FAST_BORROW         2 (verdicts)
        # |               CALL                     1
        # |               CALL                     1
        # | 117           LOAD_CONST               9 ('archivist')
        # | 120           LOAD_GLOBAL             19 (FakeArchivist + NULL)
        # |               CALL                     0
        # | 117           LOAD_CONST              10 ('max_revisions')
        # | 121           LOAD_SMALL_INT           2
        # | 117           LOAD_CONST              11 ('log')
        # | 121           LOAD_CONST              12 (<code object <lambda> at 0x10671dfb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 121>)
        # |               MAKE_FUNCTION
        # | 117           BUILD_MAP                8
        # | 121           LOAD_FAST_BORROW         3 (kw)
        # | 117           DICT_MERGE               1
        # |               CALL_FUNCTION_EX
        # |               RETURN_VALUE
        # | Disassembly of <code object <lambda> at 0x10671dfb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 121>:
        # | 121           RESUME                   0
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE

    def test_resumes_at_the_node_that_crashed(self, sample_state, tmp_path):
        'FlakyStitcher'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  123            RESUME                   0
        # |  124            LOAD_SMALL_INT           0
        # |                 LOAD_CONST               1 (('checkpointed_graph',))
        # |                 IMPORT_NAME              0 (novel_agent.graph.build)
        # |                 IMPORT_FROM              1 (checkpointed_graph)
        # |                 STORE_FAST               3 (checkpointed_graph)
        # |                 POP_TOP
        # |  126            LOAD_BUILD_CLASS
        # |                 PUSH_NULL
        # |                 LOAD_CONST               2 (<code object FlakyStitcher at 0x10664f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 126>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_CONST               3 ('FlakyStitcher')
        # |                 CALL                     2
        # |                 STORE_FAST               4 (FlakyStitcher)
        # |  134            LOAD_FAST_BORROW         4 (FlakyStitcher)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 STORE_FAST               5 (st)
        # |  135            LOAD_FAST_BORROW         0 (self)
        # |                 LOAD_ATTR                5 (_pipeline + NULL|self)
        # |                 LOAD_FAST_BORROW         5 (st)
        # |                 CALL                     1
        # |                 STORE_FAST               6 (p)
        # |  136            LOAD_FAST_BORROW         2 (tmp_path)
        # |                 LOAD_CONST               4 ('cp.sqlite')
        # |                 BINARY_OP               11 (/)
        # |                 LOAD_CONST               5 ('configurable')
        # |                 LOAD_CONST               6 ('thread_id')
        # |                 LOAD_CONST               7 ('t1')
        # |                 BUILD_MAP                1
        # |                 BUILD_MAP                1
        # |                 STORE_FAST_STORE_FAST  135 (cfg, db)
        # |  138            LOAD_FAST_BORROW         3 (checkpointed_graph)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (p, db)
        # |                 CALL                     2
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     STORE_FAST               9 (g)
        # |  139            LOAD_GLOBAL              6 (pytest)
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
        # |         L2:     POP_TOP
        # |  140            LOAD_FAST_BORROW         9 (g)
        # |                 LOAD_ATTR               13 (invoke + NULL|self)
        # |                 LOAD_GLOBAL             15 (seed + NULL)
        # |                 LOAD_FAST_BORROW         1 (sample_state)
        # |                 CALL                     1
        # |                 LOAD_FAST_BORROW         8 (cfg)
        # |                 CALL                     2
        # |                 POP_TOP
        # |  139    L3:     LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  138    L4:     LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  142    L5:     LOAD_FAST_BORROW         3 (checkpointed_graph)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (p, db)
        # |                 CALL                     2
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L6:     STORE_FAST               9 (g)
        # |  143            LOAD_FAST_BORROW         9 (g)
        # |                 LOAD_ATTR               16 (get_state)
        # |                 STORE_FAST_LOAD_FAST   170 (@py_assert1, @py_assert1)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (cfg)
        # |                 CALL                     1
        # |                 STORE_FAST_LOAD_FAST   187 (@py_assert4, @py_assert4)
        # |                 LOAD_ATTR               18 (next)
        # |                 STORE_FAST              12 (@py_assert6)
        # |                 LOAD_CONST              33 (('stitch',))
        # |                 STORE_FAST_LOAD_FAST   220 (@py_assert9, @py_assert6)
        # |                 LOAD_FAST_BORROW        13 (@py_assert9)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   238 (@py_assert8, @py_assert8)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       348 (to L15)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              34 (('==',))
        # |                 LOAD_FAST_BORROW        14 (@py_assert8)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              35 (('%(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.get_state\n}(%(py3)s)\n}.next\n} == %(py10)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 205 (@py_assert6, @py_assert9)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               9 ('py0')
        # |                 LOAD_CONST              10 ('g')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (g)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L9)
        # |         L7:     NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (g)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST              10 ('g')
        # |        L10:     LOAD_CONST              11 ('py2')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py3')
        # |                 LOAD_CONST              13 ('cfg')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L12)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (cfg)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L13)
        # |        L11:     NOT_TAKEN
        # |        L12:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (cfg)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L14)
        # |        L13:     LOAD_CONST              13 ('cfg')
        # |        L14:     LOAD_CONST              14 ('py5')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py7')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 CALL                     1
        # |                 LOAD_CONST              16 ('py10')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_assert9)
        # |                 CALL                     1
        # |                 BUILD_MAP                6
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              15 (@py_format11)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              17 ('该停在崩掉的那个节点前')
        # |                 CALL                     1
        # |                 LOAD_CONST              18 ('\n>assert %(py12)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              19 ('py12')
        # |                 LOAD_FAST_BORROW        15 (@py_format11)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              16 (@py_format13)
        # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               36 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        16 (@py_format13)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L15:     LOAD_CONST               8 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST              11 (@py_assert4)
        # |                 COPY                     1
        # |                 STORE_FAST              12 (@py_assert6)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  237 (@py_assert8, @py_assert9)
        # |  144            LOAD_FAST_BORROW         9 (g)
        # |                 LOAD_ATTR               13 (invoke + NULL|self)
        # |                 LOAD_CONST               8 (None)
        # |                 LOAD_FAST_BORROW         8 (cfg)
        # |                 CALL                     2
        # |                 STORE_FAST              17 (out)
        # |  142   L16:     LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  146   L17:     LOAD_FAST_CHECK         17 (out)
        # |                 LOAD_CONST              20 ('done_reason')
        # |                 BINARY_OP               26 ([])
        # |                 STORE_FAST              18 (@py_assert0)
        # |                 LOAD_CONST              21 ('passed')
        # |                 STORE_FAST              19 (@py_assert3)
        # |                 LOAD_FAST_BORROW        18 (@py_assert0)
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST              20 (@py_assert2)
        # |                 LOAD_FAST_BORROW        20 (@py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       122 (to L18)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              34 (('==',))
        # |                 LOAD_FAST_BORROW        20 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              36 (('%(py1)s == %(py4)s',))
        # |                 LOAD_FAST_BORROW        18 (@py_assert0)
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST              22 ('py1')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        18 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST              23 ('py4')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              21 (@py_format5)
        # |                 LOAD_CONST              24 ('assert %(py6)s')
        # |                 LOAD_CONST              25 ('py6')
        # |                 LOAD_FAST_BORROW        21 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              22 (@py_format7)
        # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               36 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        22 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L18:     LOAD_CONST               8 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              18 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST              20 (@py_assert2)
        # |                 STORE_FAST              19 (@py_assert3)
        # |  147            LOAD_FAST_BORROW         6 (p)
        # |                 LOAD_ATTR               38 (architect)
        # |                 STORE_FAST_LOAD_FAST   170 (@py_assert1, @py_assert1)
        # |                 LOAD_ATTR               40 (calls)
        # |                 STORE_FAST              19 (@py_assert3)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST              12 (@py_assert6)
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST              23 (@py_assert5)
        # |                 LOAD_FAST_BORROW        23 (@py_assert5)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       249 (to L22)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              34 (('==',))
        # |                 LOAD_FAST_BORROW        23 (@py_assert5)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              37 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.architect\n}.calls\n} == %(py7)s',))
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               9 ('py0')
        # |                 LOAD_CONST              26 ('p')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L19)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (p)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L20)
        # |                 NOT_TAKEN
        # |        L19:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (p)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L21)
        # |        L20:     LOAD_CONST              26 ('p')
        # |        L21:     LOAD_CONST              11 ('py2')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              23 ('py4')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py7')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              24 (@py_format8)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              27 ('续跑不该重出细纲')
        # |                 CALL                     1
        # |                 LOAD_CONST              28 ('\n>assert %(py9)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              29 ('py9')
        # |                 LOAD_FAST_BORROW        24 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              25 (@py_format10)
        # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               36 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        25 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L22:     LOAD_CONST               8 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST              19 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST              23 (@py_assert5)
        # |                 STORE_FAST              12 (@py_assert6)
        # |  148            LOAD_FAST_BORROW         6 (p)
        # |                 LOAD_ATTR               42 (writer)
        # |                 STORE_FAST_LOAD_FAST   170 (@py_assert1, @py_assert1)
        # |                 LOAD_ATTR               40 (calls)
        # |                 STORE_FAST              19 (@py_assert3)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST              12 (@py_assert6)
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST              23 (@py_assert5)
        # |                 LOAD_FAST_BORROW        23 (@py_assert5)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       249 (to L26)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              34 (('==',))
        # |                 LOAD_FAST_BORROW        23 (@py_assert5)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              38 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.calls\n} == %(py7)s',))
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               9 ('py0')
        # |                 LOAD_CONST              26 ('p')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L23)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (p)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L24)
        # |                 NOT_TAKEN
        # |        L23:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (p)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L25)
        # |        L24:     LOAD_CONST              26 ('p')
        # |        L25:     LOAD_CONST              11 ('py2')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              23 ('py4')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py7')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              24 (@py_format8)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              30 ('续跑不该重写场景')
        # |                 CALL                     1
        # |                 LOAD_CONST              28 ('\n>assert %(py9)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              29 ('py9')
        # |                 LOAD_FAST_BORROW        24 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              25 (@py_format10)
        # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               36 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        25 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L26:     LOAD_CONST               8 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST              19 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST              23 (@py_assert5)
        # |                 STORE_FAST              12 (@py_assert6)
        # |  149            LOAD_FAST_BORROW         5 (st)
        # |                 LOAD_ATTR               40 (calls)
        # |                 STORE_FAST              10 (@py_assert1)
        # |                 LOAD_SMALL_INT           2
        # |                 STORE_FAST_LOAD_FAST   186 (@py_assert4, @py_assert1)
        # |                 LOAD_FAST_BORROW        11 (@py_assert4)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST              19 (@py_assert3)
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       199 (to L30)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              34 (('==',))
        # |                 LOAD_FAST_BORROW        19 (@py_assert3)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              39 (('%(py2)s\n{%(py2)s = %(py0)s.calls\n} == %(py5)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert1, @py_assert4)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               9 ('py0')
        # |                 LOAD_CONST              31 ('st')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L27)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (st)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L28)
        # |                 NOT_TAKEN
        # |        L27:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (st)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L29)
        # |        L28:     LOAD_CONST              31 ('st')
        # |        L29:     LOAD_CONST              11 ('py2')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              14 ('py5')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert4)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              26 (@py_format6)
        # |                 LOAD_CONST              32 ('assert %(py7)s')
        # |                 LOAD_CONST              15 ('py7')
        # |                 LOAD_FAST_BORROW        26 (@py_format6)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              24 (@py_format8)
        # |                 LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               36 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        24 (@py_format8)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L30:     LOAD_CONST               8 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST              19 (@py_assert3)
        # |                 STORE_FAST              11 (@py_assert4)
        # |                 LOAD_CONST               8 (None)
        # |                 RETURN_VALUE
        # |  139   L31:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L32)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L32:     POP_TOP
        # |        L33:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             5
        # |                 JUMP_BACKWARD_NO_INTERRUPT 1439 (to L4)
        # |   --   L34:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # |  138   L35:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L36)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L36:     POP_TOP
        # |        L37:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             5
        # |                 JUMP_BACKWARD_NO_INTERRUPT 1451 (to L5)
        # |   --   L38:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # |  142   L39:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L40)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L40:     POP_TOP
        # |        L41:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             4
        # |                 JUMP_BACKWARD_NO_INTERRUPT 1028 (to L17)
        # |   --   L42:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L35 [2] lasti
        # |   L2 to L3 -> L31 [4] lasti
        # |   L3 to L4 -> L35 [2] lasti
        # |   L6 to L7 -> L39 [2] lasti
        # |   L8 to L11 -> L39 [2] lasti
        # |   L12 to L16 -> L39 [2] lasti
        # |   L31 to L33 -> L34 [6] lasti
        # |   L33 to L35 -> L35 [2] lasti
        # |   L35 to L37 -> L38 [4] lasti
        # |   L39 to L41 -> L42 [4] lasti
        # | Disassembly of <code object FlakyStitcher at 0x10664f030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 126>:
        # | 126           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestCheckpointResume.test_resumes_at_the_node_that_crashed.<locals>.FlakyStitcher')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         126
        # |               STORE_NAME               3 (__firstlineno__)
        # | 127           LOAD_CONST               1 (<code object __init__ at 0x10666ac40, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 127>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               4 (__init__)
        # | 128           LOAD_CONST               2 (<code object stitch at 0x106690960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 128>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               5 (stitch)
        # |               LOAD_CONST               3 (('calls',))
        # |               STORE_NAME               6 (__static_attributes__)
        # |               LOAD_CONST               4 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object __init__ at 0x10666ac40, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 127>:
        # | 127           RESUME                   0
        # |               LOAD_SMALL_INT           0
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               0 (calls)
        # |               LOAD_CONST               1 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object stitch at 0x106690960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 128>:
        # | 128           RESUME                   0
        # | 129           LOAD_FAST_BORROW         0 (self)
        # |               COPY                     1
        # |               LOAD_ATTR                0 (calls)
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               13 (+=)
        # |               SWAP                     2
        # |               STORE_ATTR               0 (calls)
        # | 130           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (calls)
        # |               LOAD_SMALL_INT           1
        # |               COMPARE_OP              88 (bool(==))
        # |               POP_JUMP_IF_FALSE       12 (to L1)
        # |               NOT_TAKEN
        # | 131           LOAD_GLOBAL              3 (RuntimeError + NULL)
        # |               LOAD_CONST               1 ('上游 403')
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # | 132   L1:     LOAD_GLOBAL              4 (GOOD)
        # |               RETURN_VALUE

        class FlakyStitcher:
            'TestCheckpointResume.test_resumes_at_the_node_that_crashed.<locals>.FlakyStitcher'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 126           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestCheckpointResume.test_resumes_at_the_node_that_crashed.<locals>.FlakyStitcher')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         126
            # |               STORE_NAME               3 (__firstlineno__)
            # | 127           LOAD_CONST               1 (<code object __init__ at 0x10666ac40, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 127>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               4 (__init__)
            # | 128           LOAD_CONST               2 (<code object stitch at 0x106690960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 128>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               5 (stitch)
            # |               LOAD_CONST               3 (('calls',))
            # |               STORE_NAME               6 (__static_attributes__)
            # |               LOAD_CONST               4 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object __init__ at 0x10666ac40, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 127>:
            # | 127           RESUME                   0
            # |               LOAD_SMALL_INT           0
            # |               LOAD_FAST_BORROW         0 (self)
            # |               STORE_ATTR               0 (calls)
            # |               LOAD_CONST               1 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object stitch at 0x106690960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 128>:
            # | 128           RESUME                   0
            # | 129           LOAD_FAST_BORROW         0 (self)
            # |               COPY                     1
            # |               LOAD_ATTR                0 (calls)
            # |               LOAD_SMALL_INT           1
            # |               BINARY_OP               13 (+=)
            # |               SWAP                     2
            # |               STORE_ATTR               0 (calls)
            # | 130           LOAD_FAST_BORROW         0 (self)
            # |               LOAD_ATTR                0 (calls)
            # |               LOAD_SMALL_INT           1
            # |               COMPARE_OP              88 (bool(==))
            # |               POP_JUMP_IF_FALSE       12 (to L1)
            # |               NOT_TAKEN
            # | 131           LOAD_GLOBAL              3 (RuntimeError + NULL)
            # |               LOAD_CONST               1 ('上游 403')
            # |               CALL                     1
            # |               RAISE_VARARGS            1
            # | 132   L1:     LOAD_GLOBAL              4 (GOOD)
            # |               RETURN_VALUE

            def __init__(self):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # | 127           RESUME                   0
                # |               LOAD_SMALL_INT           0
                # |               LOAD_FAST_BORROW         0 (self)
                # |               STORE_ATTR               0 (calls)
                # |               LOAD_CONST               1 (None)
                # |               RETURN_VALUE

            def stitch(self, o, scenes, **kw):
                '上游 403'
                # ── 函数体（字节码重建见 BODY 段）──
                # | 128           RESUME                   0
                # | 129           LOAD_FAST_BORROW         0 (self)
                # |               COPY                     1
                # |               LOAD_ATTR                0 (calls)
                # |               LOAD_SMALL_INT           1
                # |               BINARY_OP               13 (+=)
                # |               SWAP                     2
                # |               STORE_ATTR               0 (calls)
                # | 130           LOAD_FAST_BORROW         0 (self)
                # |               LOAD_ATTR                0 (calls)
                # |               LOAD_SMALL_INT           1
                # |               COMPARE_OP              88 (bool(==))
                # |               POP_JUMP_IF_FALSE       12 (to L1)
                # |               NOT_TAKEN
                # | 131           LOAD_GLOBAL              3 (RuntimeError + NULL)
                # |               LOAD_CONST               1 ('上游 403')
                # |               CALL                     1
                # |               RAISE_VARARGS            1
                # | 132   L1:     LOAD_GLOBAL              4 (GOOD)
                # |               RETURN_VALUE



    def test_a_finished_chapter_has_nothing_left_to_run(self, sample_state, tmp_path):
        'OkStitcher'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  151            RESUME                   0
        # |  152            LOAD_SMALL_INT           0
        # |                 LOAD_CONST               1 (('checkpointed_graph',))
        # |                 IMPORT_NAME              0 (novel_agent.graph.build)
        # |                 IMPORT_FROM              1 (checkpointed_graph)
        # |                 STORE_FAST               3 (checkpointed_graph)
        # |                 POP_TOP
        # |  154            LOAD_BUILD_CLASS
        # |                 PUSH_NULL
        # |                 LOAD_CONST               2 (<code object OkStitcher at 0x10666a880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 154>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_CONST               3 ('OkStitcher')
        # |                 CALL                     2
        # |                 STORE_FAST               4 (OkStitcher)
        # |  157            LOAD_FAST_BORROW         0 (self)
        # |                 LOAD_ATTR                5 (_pipeline + NULL|self)
        # |                 LOAD_FAST_BORROW         4 (OkStitcher)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CALL                     1
        # |                 STORE_FAST               5 (p)
        # |  158            LOAD_FAST_BORROW         2 (tmp_path)
        # |                 LOAD_CONST               4 ('cp.sqlite')
        # |                 BINARY_OP               11 (/)
        # |                 LOAD_CONST               5 ('configurable')
        # |                 LOAD_CONST               6 ('thread_id')
        # |                 LOAD_CONST               7 ('t2')
        # |                 BUILD_MAP                1
        # |                 BUILD_MAP                1
        # |                 STORE_FAST_STORE_FAST  118 (cfg, db)
        # |  159            LOAD_FAST_BORROW         3 (checkpointed_graph)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (p, db)
        # |                 CALL                     2
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     STORE_FAST               8 (g)
        # |  160            LOAD_FAST_BORROW         8 (g)
        # |                 LOAD_ATTR                7 (invoke + NULL|self)
        # |                 LOAD_GLOBAL              9 (seed + NULL)
        # |                 LOAD_FAST_BORROW         1 (sample_state)
        # |                 CALL                     1
        # |                 LOAD_FAST_BORROW         7 (cfg)
        # |                 CALL                     2
        # |                 POP_TOP
        # |  161            LOAD_FAST_BORROW         8 (g)
        # |                 LOAD_ATTR               10 (get_state)
        # |                 STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (cfg)
        # |                 CALL                     1
        # |                 STORE_FAST_LOAD_FAST   170 (@py_assert4, @py_assert4)
        # |                 LOAD_ATTR               12 (next)
        # |                 STORE_FAST              11 (@py_assert6)
        # |                 LOAD_CONST              20 (())
        # |                 STORE_FAST_LOAD_FAST   203 (@py_assert9, @py_assert6)
        # |                 LOAD_FAST_BORROW        12 (@py_assert9)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   221 (@py_assert8, @py_assert8)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       348 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              21 (('==',))
        # |                 LOAD_FAST_BORROW        13 (@py_assert8)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              22 (('%(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.get_state\n}(%(py3)s)\n}.next\n} == %(py10)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert6, @py_assert9)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               8 ('py0')
        # |                 LOAD_CONST               9 ('g')
        # |                 LOAD_GLOBAL             18 (@py_builtins)
        # |                 LOAD_ATTR               20 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L3)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (g)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L4)
        # |         L2:     NOT_TAKEN
        # |         L3:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (g)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L5)
        # |         L4:     LOAD_CONST               9 ('g')
        # |         L5:     LOAD_CONST              10 ('py2')
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              11 ('py3')
        # |                 LOAD_CONST              12 ('cfg')
        # |                 LOAD_GLOBAL             18 (@py_builtins)
        # |                 LOAD_ATTR               20 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (cfg)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L8)
        # |         L6:     NOT_TAKEN
        # |         L7:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (cfg)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L9)
        # |         L8:     LOAD_CONST              12 ('cfg')
        # |         L9:     LOAD_CONST              13 ('py5')
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST              14 ('py7')
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert6)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py10')
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_assert9)
        # |                 CALL                     1
        # |                 BUILD_MAP                6
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              14 (@py_format11)
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              16 ('跑完的章节不该被当成中断')
        # |                 CALL                     1
        # |                 LOAD_CONST              17 ('\n>assert %(py12)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              18 ('py12')
        # |                 LOAD_FAST_BORROW        14 (@py_format11)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              15 (@py_format13)
        # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        15 (@py_format13)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L10:     LOAD_CONST              19 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               9 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert4)
        # |                 COPY                     1
        # |                 STORE_FAST              11 (@py_assert6)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  220 (@py_assert8, @py_assert9)
        # |  159   L11:     LOAD_CONST              19 (None)
        # |                 LOAD_CONST              19 (None)
        # |                 LOAD_CONST              19 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |                 LOAD_CONST              19 (None)
        # |                 RETURN_VALUE
        # |        L12:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L13)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L13:     POP_TOP
        # |        L14:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 LOAD_CONST              19 (None)
        # |                 RETURN_VALUE
        # |   --   L15:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L12 [2] lasti
        # |   L3 to L6 -> L12 [2] lasti
        # |   L7 to L11 -> L12 [2] lasti
        # |   L12 to L14 -> L15 [4] lasti
        # | Disassembly of <code object OkStitcher at 0x10666a880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 154>:
        # | 154           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestCheckpointResume.test_a_finished_chapter_has_nothing_left_to_run.<locals>.OkStitcher')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         154
        # |               STORE_NAME               3 (__firstlineno__)
        # | 155           LOAD_CONST               1 (<code object stitch at 0x10671e170, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 155>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               4 (stitch)
        # |               LOAD_CONST               2 (())
        # |               STORE_NAME               5 (__static_attributes__)
        # |               LOAD_CONST               3 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object stitch at 0x10671e170, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 155>:
        # | 155           RESUME                   0
        # |               LOAD_GLOBAL              0 (GOOD)
        # |               RETURN_VALUE

        class OkStitcher:
            'TestCheckpointResume.test_a_finished_chapter_has_nothing_left_to_run.<locals>.OkStitcher'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 154           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestCheckpointResume.test_a_finished_chapter_has_nothing_left_to_run.<locals>.OkStitcher')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         154
            # |               STORE_NAME               3 (__firstlineno__)
            # | 155           LOAD_CONST               1 (<code object stitch at 0x10671e170, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 155>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               4 (stitch)
            # |               LOAD_CONST               2 (())
            # |               STORE_NAME               5 (__static_attributes__)
            # |               LOAD_CONST               3 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object stitch at 0x10671e170, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 155>:
            # | 155           RESUME                   0
            # |               LOAD_GLOBAL              0 (GOOD)
            # |               RETURN_VALUE

            def stitch(self, o, scenes, **kw):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # | 155           RESUME                   0
                # |               LOAD_GLOBAL              0 (GOOD)
                # |               RETURN_VALUE



    def test_each_chapter_is_its_own_thread(self, sample_state, tmp_path):
        '同一个 db 里两章互不干扰，否则第 4 章会捡起第 3 章的残局。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  163            RESUME                   0
        # |  165            LOAD_SMALL_INT           0
        # |                 LOAD_CONST               1 (('checkpointed_graph',))
        # |                 IMPORT_NAME              0 (novel_agent.graph.build)
        # |                 IMPORT_FROM              1 (checkpointed_graph)
        # |                 STORE_FAST               3 (checkpointed_graph)
        # |                 POP_TOP
        # |  167            LOAD_BUILD_CLASS
        # |                 PUSH_NULL
        # |                 LOAD_CONST               2 (<code object OkStitcher at 0x10666b2d0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 167>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_CONST               3 ('OkStitcher')
        # |                 CALL                     2
        # |                 STORE_FAST               4 (OkStitcher)
        # |  170            LOAD_FAST_BORROW         0 (self)
        # |                 LOAD_ATTR                5 (_pipeline + NULL|self)
        # |                 LOAD_FAST_BORROW         4 (OkStitcher)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 LOAD_GLOBAL              6 (PASS)
        # |                 LOAD_GLOBAL              6 (PASS)
        # |                 BUILD_TUPLE              2
        # |                 LOAD_CONST               4 (('verdicts',))
        # |                 CALL_KW                  2
        # |                 STORE_FAST               5 (p)
        # |  171            LOAD_FAST_BORROW         2 (tmp_path)
        # |                 LOAD_CONST               5 ('cp.sqlite')
        # |                 BINARY_OP               11 (/)
        # |                 STORE_FAST               6 (db)
        # |  172            LOAD_FAST_BORROW         3 (checkpointed_graph)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (p, db)
        # |                 CALL                     2
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     STORE_FAST               7 (g)
        # |  173            LOAD_FAST_BORROW         7 (g)
        # |                 LOAD_ATTR                9 (invoke + NULL|self)
        # |                 LOAD_GLOBAL             11 (seed + NULL)
        # |                 LOAD_FAST_BORROW         1 (sample_state)
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_CONST               6 (('ch',))
        # |                 CALL_KW                  2
        # |                 LOAD_CONST               7 ('configurable')
        # |                 LOAD_CONST               8 ('thread_id')
        # |                 LOAD_CONST               9 ('ch1')
        # |                 BUILD_MAP                1
        # |                 BUILD_MAP                1
        # |                 CALL                     2
        # |                 POP_TOP
        # |  174            LOAD_FAST_BORROW         7 (g)
        # |                 LOAD_ATTR               12 (get_state)
        # |                 STORE_FAST               8 (@py_assert1)
        # |                 LOAD_CONST               7 ('configurable')
        # |                 LOAD_CONST               8 ('thread_id')
        # |                 LOAD_CONST              10 ('ch2')
        # |                 BUILD_MAP                1
        # |                 BUILD_MAP                1
        # |                 STORE_FAST_LOAD_FAST   152 (@py_assert3, @py_assert1)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert3)
        # |                 CALL                     1
        # |                 STORE_FAST_LOAD_FAST   170 (@py_assert5, @py_assert5)
        # |                 LOAD_ATTR               14 (next)
        # |                 STORE_FAST              11 (@py_assert7)
        # |                 LOAD_CONST              21 (())
        # |                 STORE_FAST_LOAD_FAST   203 (@py_assert10, @py_assert7)
        # |                 LOAD_FAST_BORROW        12 (@py_assert10)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   221 (@py_assert9, @py_assert9)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       265 (to L6)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              22 (('==',))
        # |                 LOAD_FAST_BORROW        13 (@py_assert9)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              23 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get_state\n}(%(py4)s)\n}.next\n} == %(py11)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert7, @py_assert10)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST              11 ('py0')
        # |                 LOAD_CONST              12 ('g')
        # |                 LOAD_GLOBAL             20 (@py_builtins)
        # |                 LOAD_ATTR               22 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L3)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (g)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L4)
        # |         L2:     NOT_TAKEN
        # |         L3:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (g)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L5)
        # |         L4:     LOAD_CONST              12 ('g')
        # |         L5:     LOAD_CONST              13 ('py2')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              14 ('py4')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py6')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert5)
        # |                 CALL                     1
        # |                 LOAD_CONST              16 ('py8')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert7)
        # |                 CALL                     1
        # |                 LOAD_CONST              17 ('py11')
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_assert10)
        # |                 CALL                     1
        # |                 BUILD_MAP                6
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              14 (@py_format12)
        # |                 LOAD_CONST              18 ('assert %(py13)s')
        # |                 LOAD_CONST              19 ('py13')
        # |                 LOAD_FAST_BORROW        14 (@py_format12)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              15 (@py_format14)
        # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             16 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        15 (@py_format14)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L6:     LOAD_CONST              20 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               8 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST               9 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert5)
        # |                 COPY                     1
        # |                 STORE_FAST              11 (@py_assert7)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  220 (@py_assert9, @py_assert10)
        # |  172    L7:     LOAD_CONST              20 (None)
        # |                 LOAD_CONST              20 (None)
        # |                 LOAD_CONST              20 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |                 LOAD_CONST              20 (None)
        # |                 RETURN_VALUE
        # |         L8:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L9)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |         L9:     POP_TOP
        # |        L10:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 LOAD_CONST              20 (None)
        # |                 RETURN_VALUE
        # |   --   L11:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L8 [2] lasti
        # |   L3 to L7 -> L8 [2] lasti
        # |   L8 to L10 -> L11 [4] lasti
        # | Disassembly of <code object OkStitcher at 0x10666b2d0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 167>:
        # | 167           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestCheckpointResume.test_each_chapter_is_its_own_thread.<locals>.OkStitcher')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         167
        # |               STORE_NAME               3 (__firstlineno__)
        # | 168           LOAD_CONST               1 (<code object stitch at 0x10671e250, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 168>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               4 (stitch)
        # |               LOAD_CONST               2 (())
        # |               STORE_NAME               5 (__static_attributes__)
        # |               LOAD_CONST               3 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object stitch at 0x10671e250, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 168>:
        # | 168           RESUME                   0
        # |               LOAD_GLOBAL              0 (GOOD)
        # |               RETURN_VALUE

        class OkStitcher:
            'TestCheckpointResume.test_each_chapter_is_its_own_thread.<locals>.OkStitcher'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 167           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestCheckpointResume.test_each_chapter_is_its_own_thread.<locals>.OkStitcher')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         167
            # |               STORE_NAME               3 (__firstlineno__)
            # | 168           LOAD_CONST               1 (<code object stitch at 0x10671e250, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 168>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               4 (stitch)
            # |               LOAD_CONST               2 (())
            # |               STORE_NAME               5 (__static_attributes__)
            # |               LOAD_CONST               3 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object stitch at 0x10671e250, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 168>:
            # | 168           RESUME                   0
            # |               LOAD_GLOBAL              0 (GOOD)
            # |               RETURN_VALUE

            def stitch(self, o, scenes, **kw):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # | 168           RESUME                   0
                # |               LOAD_GLOBAL              0 (GOOD)
                # |               RETURN_VALUE



    def test_state_survives_a_real_sqlite_roundtrip(self, sample_state, tmp_path):
        'GateReport 这类对象曾被塞进图状态；checkpoint 一序列化就可能炸，\n而这条路径上最不该出岔子的就是存档本身。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  176            RESUME                   0
        # |  179            LOAD_SMALL_INT           0
        # |                 LOAD_CONST               1 (('checkpointed_graph',))
        # |                 IMPORT_NAME              0 (novel_agent.graph.build)
        # |                 IMPORT_FROM              1 (checkpointed_graph)
        # |                 STORE_FAST               3 (checkpointed_graph)
        # |                 POP_TOP
        # |  181            LOAD_BUILD_CLASS
        # |                 PUSH_NULL
        # |                 LOAD_CONST               2 (<code object OkStitcher at 0x10666b3c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 181>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_CONST               3 ('OkStitcher')
        # |                 CALL                     2
        # |                 STORE_FAST               4 (OkStitcher)
        # |  184            LOAD_FAST_BORROW         0 (self)
        # |                 LOAD_ATTR                5 (_pipeline + NULL|self)
        # |                 LOAD_FAST_BORROW         4 (OkStitcher)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CALL                     1
        # |                 STORE_FAST               5 (p)
        # |  185            LOAD_FAST_BORROW         2 (tmp_path)
        # |                 LOAD_CONST               4 ('cp.sqlite')
        # |                 BINARY_OP               11 (/)
        # |                 LOAD_CONST               5 ('configurable')
        # |                 LOAD_CONST               6 ('thread_id')
        # |                 LOAD_CONST               7 ('t3')
        # |                 BUILD_MAP                1
        # |                 BUILD_MAP                1
        # |                 STORE_FAST_STORE_FAST  118 (cfg, db)
        # |  186            LOAD_FAST_BORROW         3 (checkpointed_graph)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (p, db)
        # |                 CALL                     2
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     STORE_FAST               8 (g)
        # |  187            LOAD_FAST_BORROW         8 (g)
        # |                 LOAD_ATTR                7 (invoke + NULL|self)
        # |                 LOAD_GLOBAL              9 (seed + NULL)
        # |                 LOAD_FAST_BORROW         1 (sample_state)
        # |                 CALL                     1
        # |                 LOAD_FAST_BORROW         7 (cfg)
        # |                 CALL                     2
        # |                 POP_TOP
        # |  186    L2:     LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  188    L3:     LOAD_FAST_BORROW         3 (checkpointed_graph)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (p, db)
        # |                 CALL                     2
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L4:     STORE_FAST               8 (g)
        # |  189            LOAD_FAST_BORROW         8 (g)
        # |                 LOAD_ATTR               11 (get_state + NULL|self)
        # |                 LOAD_FAST_BORROW         7 (cfg)
        # |                 CALL                     1
        # |                 LOAD_ATTR               12 (values)
        # |                 STORE_FAST               9 (values)
        # |  188    L5:     LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 LOAD_CONST               8 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  190    L6:     LOAD_FAST_CHECK          9 (values)
        # |                 LOAD_CONST               9 ('done_reason')
        # |                 BINARY_OP               26 ([])
        # |                 STORE_FAST              10 (@py_assert0)
        # |                 LOAD_CONST              10 ('passed')
        # |                 STORE_FAST_LOAD_FAST   186 (@py_assert3, @py_assert0)
        # |                 LOAD_FAST_BORROW        11 (@py_assert3)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   204 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       121 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              20 (('==',))
        # |                 LOAD_FAST_BORROW        12 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              21 (('%(py1)s == %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST              11 ('py1')
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py4')
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format5)
        # |                 LOAD_CONST              13 ('assert %(py6)s')
        # |                 LOAD_CONST              14 ('py6')
        # |                 LOAD_FAST_BORROW        13 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              14 (@py_format7)
        # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        14 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST               8 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  203 (@py_assert2, @py_assert3)
        # |  191            LOAD_CONST              15 (<code object <genexpr> at 0x10666eaf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 191>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_FAST_BORROW         9 (values)
        # |                 GET_ITER
        # |                 CALL                     0
        # |                 STORE_FAST              15 (@py_assert1)
        # |                 LOAD_GLOBAL             25 (all + NULL)
        # |                 LOAD_FAST_BORROW        15 (@py_assert1)
        # |                 CALL                     1
        # |                 STORE_FAST_LOAD_FAST   187 (@py_assert3, @py_assert3)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       171 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_CONST              16 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |                 LOAD_CONST              17 ('py0')
        # |                 LOAD_CONST              18 ('all')
        # |                 LOAD_GLOBAL             26 (@py_builtins)
        # |                 LOAD_ATTR               28 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             24 (all)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             24 (all)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST              18 ('all')
        # |        L10:     LOAD_CONST              19 ('py2')
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        15 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py4')
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format5)
        # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_format5)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST               8 (None)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  251 (@py_assert1, @py_assert3)
        # |                 LOAD_CONST               8 (None)
        # |                 RETURN_VALUE
        # |  186   L12:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L13)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L13:     POP_TOP
        # |        L14:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             1
        # |                 JUMP_BACKWARD_NO_INTERRUPT 418 (to L3)
        # |   --   L15:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # |  188   L16:     PUSH_EXC_INFO
        # |                 WITH_EXCEPT_START
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE         2 (to L17)
        # |                 NOT_TAKEN
        # |                 RERAISE                  2
        # |        L17:     POP_TOP
        # |        L18:     POP_EXCEPT
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 POP_TOP
        # |                 EXTENDED_ARG             1
        # |                 JUMP_BACKWARD_NO_INTERRUPT 386 (to L6)
        # |   --   L19:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L12 [2] lasti
        # |   L4 to L5 -> L16 [2] lasti
        # |   L12 to L14 -> L15 [4] lasti
        # |   L16 to L18 -> L19 [4] lasti
        # | Disassembly of <code object OkStitcher at 0x10666b3c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 181>:
        # | 181           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestCheckpointResume.test_state_survives_a_real_sqlite_roundtrip.<locals>.OkStitcher')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         181
        # |               STORE_NAME               3 (__firstlineno__)
        # | 182           LOAD_CONST               1 (<code object stitch at 0x10671e410, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 182>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               4 (stitch)
        # |               LOAD_CONST               2 (())
        # |               STORE_NAME               5 (__static_attributes__)
        # |               LOAD_CONST               3 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object stitch at 0x10671e410, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 182>:
        # | 182           RESUME                   0
        # |               LOAD_GLOBAL              0 (GOOD)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x10666eaf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 191>:
        # |  191           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                26 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (k, k)
        # |                LOAD_ATTR                1 (startswith + NULL|self)
        # |                LOAD_CONST               0 ('_')
        # |                CALL                     1
        # |                TO_BOOL
        # |                UNARY_NOT
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           28 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti

        class OkStitcher:
            'TestCheckpointResume.test_state_survives_a_real_sqlite_roundtrip.<locals>.OkStitcher'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 181           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestCheckpointResume.test_state_survives_a_real_sqlite_roundtrip.<locals>.OkStitcher')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         181
            # |               STORE_NAME               3 (__firstlineno__)
            # | 182           LOAD_CONST               1 (<code object stitch at 0x10671e410, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 182>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               4 (stitch)
            # |               LOAD_CONST               2 (())
            # |               STORE_NAME               5 (__static_attributes__)
            # |               LOAD_CONST               3 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object stitch at 0x10671e410, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 182>:
            # | 182           RESUME                   0
            # |               LOAD_GLOBAL              0 (GOOD)
            # |               RETURN_VALUE

            def stitch(self, o, scenes, **kw):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # | 182           RESUME                   0
                # |               LOAD_GLOBAL              0 (GOOD)
                # |               RETURN_VALUE




class TestChapterResultView:
    'TestChapterResultView'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 194           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestChapterResultView')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         194
    # |               STORE_NAME               3 (__firstlineno__)
    # | 195           LOAD_CONST               1 ('CLI 只认一套结果接口，两条路径才能共用同一段落盘/归档/报错代码。')
    # |               STORE_NAME               4 (__doc__)
    # | 197           LOAD_CONST               2 (<code object test_maps_a_passing_run at 0x7b18c0a000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 197>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_maps_a_passing_run)
    # | 218           LOAD_CONST               3 (<code object test_maps_a_failing_run at 0x7b190d3100, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 218>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_maps_a_failing_run)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_maps_a_passing_run at 0x7b18c0a000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 197>:
    # | 197            RESUME                   0
    # | 198            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('ChapterResultView',))
    # |                IMPORT_NAME              0 (novel_agent.graph.build)
    # |                IMPORT_FROM              1 (ChapterResultView)
    # |                STORE_FAST               2 (ChapterResultView)
    # |                POP_TOP
    # | 200            LOAD_SMALL_INT           0
    # |                LOAD_CONST               2 (('ChapterPipeline',))
    # |                IMPORT_NAME              2 (novel_agent.agents.pipeline)
    # |                IMPORT_FROM              3 (ChapterPipeline)
    # |                STORE_FAST               3 (ChapterPipeline)
    # |                POP_TOP
    # | 202            LOAD_GLOBAL              9 (make + NULL)
    # |                LOAD_GLOBAL             10 (GOOD)
    # |                BUILD_LIST               1
    # |                LOAD_GLOBAL             12 (PASS)
    # |                BUILD_LIST               1
    # |                CALL                     2
    # |                UNPACK_SEQUENCE          3
    # |                STORE_FAST               4 (g)
    # |                POP_TOP
    # |                STORE_FAST               5 (_)
    # | 204            LOAD_FAST_BORROW         3 (ChapterPipeline)
    # |                PUSH_NULL
    # | 205            LOAD_GLOBAL             15 (FakeArchitect + NULL)
    # |                CALL                     0
    # |                LOAD_GLOBAL             17 (FakeWriter + NULL)
    # |                LOAD_CONST               3 ('a')
    # |                LOAD_CONST               4 ('b')
    # |                BUILD_LIST               2
    # |                CALL                     1
    # | 206            LOAD_GLOBAL             19 (FakeStitcher + NULL)
    # |                LOAD_GLOBAL             10 (GOOD)
    # |                BUILD_LIST               1
    # |                CALL                     1
    # |                LOAD_GLOBAL             20 (Gate)
    # |                LOAD_ATTR               22 (from_config)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             24 (CONFIG)
    # |                CALL                     1
    # | 207            LOAD_GLOBAL             27 (FakeJudge + NULL)
    # |                LOAD_GLOBAL             12 (PASS)
    # |                BUILD_LIST               1
    # |                CALL                     1
    # |                LOAD_GLOBAL             29 (FakeArchivist + NULL)
    # |                CALL                     0
    # | 208            LOAD_CONST               5 (<code object <lambda> at 0x10671e4f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 208>)
    # |                MAKE_FUNCTION
    # | 204            LOAD_CONST               6 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'log'))
    # |                CALL_KW                  7
    # |                STORE_FAST               6 (pl)
    # | 209            LOAD_FAST_BORROW         4 (g)
    # |                LOAD_ATTR               31 (invoke + NULL|self)
    # |                LOAD_GLOBAL             33 (seed + NULL)
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                CALL                     1
    # |                CALL                     1
    # |                STORE_FAST               7 (out)
    # | 210            LOAD_FAST_BORROW         2 (ChapterResultView)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (out, pl)
    # |                CALL                     2
    # |                STORE_FAST               8 (view)
    # | 211            BUILD_LIST               0
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert1, view)
    # |                LOAD_ATTR               34 (passed)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
    # |                STORE_FAST_LOAD_FAST   186 (@py_assert0, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       20 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         8 (view)
    # |                LOAD_ATTR               36 (notes)
    # |                STORE_FAST              12 (@py_assert7)
    # |                BUILD_LIST               0
    # |                STORE_FAST_LOAD_FAST   220 (@py_assert10, @py_assert7)
    # |                LOAD_FAST_BORROW        13 (@py_assert10)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   238 (@py_assert9, @py_assert9)
    # |                STORE_FAST              11 (@py_assert0)
    # |        L1:     LOAD_FAST_BORROW        11 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       391 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_CONST               7 ('%(py4)s\n{%(py4)s = %(py2)s.passed\n}')
    # |                LOAD_CONST               8 ('py2')
    # |                LOAD_CONST               9 ('view')
    # |                LOAD_GLOBAL             38 (@py_builtins)
    # |                LOAD_ATTR               40 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               44 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST               9 ('view')
    # |        L4:     LOAD_CONST              10 ('py4')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   249 (@py_format5, @py_assert1)
    # |                LOAD_ATTR               49 (append + NULL|self)
    # |                LOAD_FAST_BORROW        15 (@py_format5)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      186 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               50 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              30 (('==',))
    # |                LOAD_FAST_CHECK         14 (@py_assert9)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              31 (('%(py8)s\n{%(py8)s = %(py6)s.notes\n} == %(py11)s',))
    # |                LOAD_FAST_CHECK         12 (@py_assert7)
    # |                LOAD_FAST_CHECK         13 (@py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              11 ('py6')
    # |                LOAD_CONST               9 ('view')
    # |                LOAD_GLOBAL             38 (@py_builtins)
    # |                LOAD_ATTR               40 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               44 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               9 ('view')
    # |        L7:     LOAD_CONST              12 ('py8')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert7)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py11')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format12)
    # |                LOAD_CONST              14 ('%(py13)s')
    # |                LOAD_CONST              15 ('py13')
    # |                LOAD_FAST_BORROW        16 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format14)
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                LOAD_ATTR               49 (append + NULL|self)
    # |                LOAD_FAST_BORROW        17 (@py_format14)
    # |                CALL                     1
    # |                POP_TOP
    # |        L8:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               52 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format15)
    # |                LOAD_CONST              16 ('assert %(py16)s')
    # |                LOAD_CONST              17 ('py16')
    # |                LOAD_FAST_BORROW        18 (@py_format15)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              19 (@py_format17)
    # |                LOAD_GLOBAL             55 (AssertionError + NULL)
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               56 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        19 (@py_format17)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L9:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST              11 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST              12 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  237 (@py_assert9, @py_assert10)
    # | 212            LOAD_FAST_BORROW         8 (view)
    # |                LOAD_ATTR               58 (text)
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
    # |                LOAD_GLOBAL             10 (GOOD)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       268 (to L16)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               50 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              30 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              32 (('%(py2)s\n{%(py2)s = %(py0)s.text\n} == %(py4)s',))
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                LOAD_GLOBAL             10 (GOOD)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              19 ('py0')
    # |                LOAD_CONST               9 ('view')
    # |                LOAD_GLOBAL             38 (@py_builtins)
    # |                LOAD_ATTR               40 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               44 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST               9 ('view')
    # |       L12:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py4')
    # |                LOAD_CONST              20 ('GOOD')
    # |                LOAD_GLOBAL             38 (@py_builtins)
    # |                LOAD_ATTR               40 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               44 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (GOOD)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L14)
    # |                NOT_TAKEN
    # |       L13:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (GOOD)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L15)
    # |       L14:     LOAD_CONST              20 ('GOOD')
    # |       L15:     BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format5)
    # |                LOAD_CONST              21 ('assert %(py6)s')
    # |                LOAD_CONST              11 ('py6')
    # |                LOAD_FAST_BORROW        15 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              20 (@py_format7)
    # |                LOAD_GLOBAL             55 (AssertionError + NULL)
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               56 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        20 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L16:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  154 (@py_assert1, @py_assert3)
    # | 213            LOAD_FAST_BORROW         8 (view)
    # |                LOAD_ATTR               60 (revisions)
    # |                STORE_FAST               9 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                STORE_FAST              21 (@py_assert4)
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                LOAD_FAST_BORROW        21 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       200 (to L20)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               50 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              30 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              33 (('%(py2)s\n{%(py2)s = %(py0)s.revisions\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                LOAD_FAST_BORROW        21 (@py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              19 ('py0')
    # |                LOAD_CONST               9 ('view')
    # |                LOAD_GLOBAL             38 (@py_builtins)
    # |                LOAD_ATTR               40 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L17)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               44 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L18)
    # |                NOT_TAKEN
    # |       L17:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L19)
    # |       L18:     LOAD_CONST               9 ('view')
    # |       L19:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              22 ('py5')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        21 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              22 (@py_format6)
    # |                LOAD_CONST              23 ('assert %(py7)s')
    # |                LOAD_CONST              24 ('py7')
    # |                LOAD_FAST_BORROW        22 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              23 (@py_format8)
    # |                LOAD_GLOBAL             55 (AssertionError + NULL)
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               56 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        23 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L20:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert3)
    # |                STORE_FAST              21 (@py_assert4)
    # | 214            LOAD_FAST_BORROW         8 (view)
    # |                LOAD_ATTR               62 (verdict)
    # |                STORE_FAST               9 (@py_assert1)
    # |                LOAD_CONST              18 (None)
    # |                STORE_FAST              21 (@py_assert4)
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                LOAD_FAST_BORROW        21 (@py_assert4)
    # |                IS_OP                    1 (is not)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       200 (to L24)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               50 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              34 (('is not',))
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              35 (('%(py2)s\n{%(py2)s = %(py0)s.verdict\n} is not %(py5)s',))
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                LOAD_FAST_BORROW        21 (@py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              19 ('py0')
    # |                LOAD_CONST               9 ('view')
    # |                LOAD_GLOBAL             38 (@py_builtins)
    # |                LOAD_ATTR               40 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L21)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               44 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L22)
    # |                NOT_TAKEN
    # |       L21:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L23)
    # |       L22:     LOAD_CONST               9 ('view')
    # |       L23:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              22 ('py5')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        21 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              22 (@py_format6)
    # |                LOAD_CONST              23 ('assert %(py7)s')
    # |                LOAD_CONST              24 ('py7')
    # |                LOAD_FAST_BORROW        22 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              23 (@py_format8)
    # |                LOAD_GLOBAL             55 (AssertionError + NULL)
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               56 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        23 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L24:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert3)
    # |                STORE_FAST              21 (@py_assert4)
    # | 215            LOAD_FAST_BORROW         8 (view)
    # |                LOAD_ATTR               64 (gate)
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
    # |                LOAD_ATTR               34 (passed)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       190 (to L28)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               66 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              25 ('gate 报告要能重算出来（它不进 checkpoint）')
    # |                CALL                     1
    # |                LOAD_CONST              26 ('\n>assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              19 ('py0')
    # |                LOAD_CONST               9 ('view')
    # |                LOAD_GLOBAL             38 (@py_builtins)
    # |                LOAD_ATTR               40 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L25)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               44 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L26)
    # |                NOT_TAKEN
    # |       L25:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (view)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L27)
    # |       L26:     LOAD_CONST               9 ('view')
    # |       L27:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py4')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format5)
    # |                LOAD_GLOBAL             55 (AssertionError + NULL)
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               56 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        15 (@py_format5)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L28:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  154 (@py_assert1, @py_assert3)
    # | 216            LOAD_CONST              27 (<code object <genexpr> at 0x106720690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 216>)
    # |                MAKE_FUNCTION
    # |                LOAD_FAST_BORROW         8 (view)
    # |                LOAD_ATTR               68 (state)
    # |                LOAD_ATTR               70 (chapter_summaries)
    # |                GET_ITER
    # |                CALL                     0
    # |                STORE_FAST               9 (@py_assert1)
    # |                LOAD_GLOBAL             73 (any + NULL)
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       171 (to L32)
    # |                NOT_TAKEN
    # |                LOAD_CONST              28 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |                LOAD_CONST              19 ('py0')
    # |                LOAD_CONST              29 ('any')
    # |                LOAD_GLOBAL             38 (@py_builtins)
    # |                LOAD_ATTR               40 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L29)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               44 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             72 (any)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L30)
    # |                NOT_TAKEN
    # |       L29:     LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             72 (any)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L31)
    # |       L30:     LOAD_CONST              29 ('any')
    # |       L31:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py4')
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               46 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format5)
    # |                LOAD_GLOBAL             55 (AssertionError + NULL)
    # |                LOAD_GLOBAL             42 (@pytest_ar)
    # |                LOAD_ATTR               56 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        15 (@py_format5)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L32:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  154 (@py_assert1, @py_assert3)
    # |                LOAD_CONST              18 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x10671e4f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 208>:
    # | 208           RESUME                   0
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x106720690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 216>:
    # |  216           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                19 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (s, s)
    # |                LOAD_ATTR                0 (ch)
    # |                LOAD_SMALL_INT           1
    # |                COMPARE_OP              72 (==)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           21 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
    # | Disassembly of <code object test_maps_a_failing_run at 0x7b190d3100, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 218>:
    # | 218           RESUME                   0
    # | 219           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('ChapterPipeline',))
    # |               IMPORT_NAME              0 (novel_agent.agents.pipeline)
    # |               IMPORT_FROM              1 (ChapterPipeline)
    # |               STORE_FAST               2 (ChapterPipeline)
    # |               POP_TOP
    # | 220           LOAD_SMALL_INT           0
    # |               LOAD_CONST               2 (('ChapterResultView',))
    # |               IMPORT_NAME              2 (novel_agent.graph.build)
    # |               IMPORT_FROM              3 (ChapterResultView)
    # |               STORE_FAST               3 (ChapterResultView)
    # |               POP_TOP
    # | 222           LOAD_GLOBAL              9 (make + NULL)
    # |               LOAD_GLOBAL             10 (BAD)
    # |               LOAD_GLOBAL             10 (BAD)
    # |               LOAD_GLOBAL             10 (BAD)
    # |               LOAD_GLOBAL             10 (BAD)
    # |               BUILD_LIST               4
    # |               LOAD_GLOBAL             12 (PASS)
    # |               BUILD_LIST               1
    # |               LOAD_SMALL_INT           2
    # |               LOAD_CONST               3 (('max_revisions',))
    # |               CALL_KW                  3
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST               4 (g)
    # |               POP_TOP
    # |               STORE_FAST               5 (_)
    # | 223           LOAD_FAST_BORROW         2 (ChapterPipeline)
    # |               PUSH_NULL
    # | 224           LOAD_GLOBAL             15 (FakeArchitect + NULL)
    # |               CALL                     0
    # |               LOAD_GLOBAL             17 (FakeWriter + NULL)
    # |               LOAD_CONST               4 ('a')
    # |               LOAD_CONST               5 ('b')
    # |               BUILD_LIST               2
    # |               CALL                     1
    # | 225           LOAD_GLOBAL             19 (FakeStitcher + NULL)
    # |               LOAD_GLOBAL             10 (BAD)
    # |               BUILD_LIST               1
    # |               CALL                     1
    # |               LOAD_GLOBAL             20 (Gate)
    # |               LOAD_ATTR               22 (from_config)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             24 (CONFIG)
    # |               CALL                     1
    # | 226           LOAD_GLOBAL             27 (FakeJudge + NULL)
    # |               LOAD_GLOBAL             12 (PASS)
    # |               BUILD_LIST               1
    # |               CALL                     1
    # |               LOAD_GLOBAL             29 (FakeArchivist + NULL)
    # |               CALL                     0
    # | 227           LOAD_CONST               6 (<code object <lambda> at 0x10671e6b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 227>)
    # |               MAKE_FUNCTION
    # | 223           LOAD_CONST               7 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'log'))
    # |               CALL_KW                  7
    # |               STORE_FAST               6 (pl)
    # | 228           LOAD_FAST_BORROW         3 (ChapterResultView)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (g)
    # |               LOAD_ATTR               31 (invoke + NULL|self)
    # |               LOAD_GLOBAL             33 (seed + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               CALL                     1
    # |               LOAD_FAST_BORROW         6 (pl)
    # |               CALL                     2
    # |               STORE_FAST               7 (view)
    # | 229           LOAD_FAST_BORROW         7 (view)
    # |               LOAD_ATTR               34 (passed)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       141 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               8 ('assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |               LOAD_CONST               9 ('py0')
    # |               LOAD_CONST              10 ('view')
    # |               LOAD_GLOBAL             36 (@py_builtins)
    # |               LOAD_ATTR               38 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               42 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (view)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               44 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (view)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST              10 ('view')
    # |       L3:     LOAD_CONST              11 ('py2')
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               44 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert1)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format4)
    # |               LOAD_GLOBAL             47 (AssertionError + NULL)
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               48 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format4)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  137 (@py_assert1, @py_assert3)
    # | 230           LOAD_CONST              13 ('仍未通过')
    # |               STORE_FAST_LOAD_FAST   183 (@py_assert0, view)
    # |               LOAD_ATTR               50 (notes)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   155 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         9 (@py_assert3)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   204 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               52 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              19 (('in',))
    # |               LOAD_FAST_BORROW        12 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              20 (('%(py1)s in %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 185 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              14 ('py1')
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               44 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST              15 ('py4')
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               44 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format5)
    # |               LOAD_CONST              16 ('assert %(py6)s')
    # |               LOAD_CONST              17 ('py6')
    # |               LOAD_FAST_BORROW        13 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              14 (@py_format7)
    # |               LOAD_GLOBAL             47 (AssertionError + NULL)
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               48 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        14 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L5:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST              11 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  201 (@py_assert2, @py_assert3)
    # | 231           LOAD_FAST_BORROW         7 (view)
    # |               LOAD_ATTR               54 (gate)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
    # |               LOAD_ATTR               34 (passed)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST   255 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       163 (to L9)
    # |               NOT_TAKEN
    # |               LOAD_CONST              18 ('assert not %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}')
    # |               LOAD_CONST               9 ('py0')
    # |               LOAD_CONST              10 ('view')
    # |               LOAD_GLOBAL             36 (@py_builtins)
    # |               LOAD_ATTR               38 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L6)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               42 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (view)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L7)
    # |               NOT_TAKEN
    # |       L6:     LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               44 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (view)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L8)
    # |       L7:     LOAD_CONST              10 ('view')
    # |       L8:     LOAD_CONST              11 ('py2')
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               44 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              15 ('py4')
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               44 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              16 (@py_format6)
    # |               LOAD_GLOBAL             47 (AssertionError + NULL)
    # |               LOAD_GLOBAL             40 (@pytest_ar)
    # |               LOAD_ATTR               48 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        16 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L9:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  159 (@py_assert3, @py_assert5)
    # |               LOAD_CONST              12 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x10671e6b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 227>:
    # | 227           RESUME                   0
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE

    def test_maps_a_passing_run(self, sample_state):
        'a'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 197            RESUME                   0
        # | 198            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('ChapterResultView',))
        # |                IMPORT_NAME              0 (novel_agent.graph.build)
        # |                IMPORT_FROM              1 (ChapterResultView)
        # |                STORE_FAST               2 (ChapterResultView)
        # |                POP_TOP
        # | 200            LOAD_SMALL_INT           0
        # |                LOAD_CONST               2 (('ChapterPipeline',))
        # |                IMPORT_NAME              2 (novel_agent.agents.pipeline)
        # |                IMPORT_FROM              3 (ChapterPipeline)
        # |                STORE_FAST               3 (ChapterPipeline)
        # |                POP_TOP
        # | 202            LOAD_GLOBAL              9 (make + NULL)
        # |                LOAD_GLOBAL             10 (GOOD)
        # |                BUILD_LIST               1
        # |                LOAD_GLOBAL             12 (PASS)
        # |                BUILD_LIST               1
        # |                CALL                     2
        # |                UNPACK_SEQUENCE          3
        # |                STORE_FAST               4 (g)
        # |                POP_TOP
        # |                STORE_FAST               5 (_)
        # | 204            LOAD_FAST_BORROW         3 (ChapterPipeline)
        # |                PUSH_NULL
        # | 205            LOAD_GLOBAL             15 (FakeArchitect + NULL)
        # |                CALL                     0
        # |                LOAD_GLOBAL             17 (FakeWriter + NULL)
        # |                LOAD_CONST               3 ('a')
        # |                LOAD_CONST               4 ('b')
        # |                BUILD_LIST               2
        # |                CALL                     1
        # | 206            LOAD_GLOBAL             19 (FakeStitcher + NULL)
        # |                LOAD_GLOBAL             10 (GOOD)
        # |                BUILD_LIST               1
        # |                CALL                     1
        # |                LOAD_GLOBAL             20 (Gate)
        # |                LOAD_ATTR               22 (from_config)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             24 (CONFIG)
        # |                CALL                     1
        # | 207            LOAD_GLOBAL             27 (FakeJudge + NULL)
        # |                LOAD_GLOBAL             12 (PASS)
        # |                BUILD_LIST               1
        # |                CALL                     1
        # |                LOAD_GLOBAL             29 (FakeArchivist + NULL)
        # |                CALL                     0
        # | 208            LOAD_CONST               5 (<code object <lambda> at 0x10671e4f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 208>)
        # |                MAKE_FUNCTION
        # | 204            LOAD_CONST               6 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'log'))
        # |                CALL_KW                  7
        # |                STORE_FAST               6 (pl)
        # | 209            LOAD_FAST_BORROW         4 (g)
        # |                LOAD_ATTR               31 (invoke + NULL|self)
        # |                LOAD_GLOBAL             33 (seed + NULL)
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                CALL                     1
        # |                CALL                     1
        # |                STORE_FAST               7 (out)
        # | 210            LOAD_FAST_BORROW         2 (ChapterResultView)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 118 (out, pl)
        # |                CALL                     2
        # |                STORE_FAST               8 (view)
        # | 211            BUILD_LIST               0
        # |                STORE_FAST_LOAD_FAST   152 (@py_assert1, view)
        # |                LOAD_ATTR               34 (passed)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
        # |                STORE_FAST_LOAD_FAST   186 (@py_assert0, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       20 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_FAST_BORROW         8 (view)
        # |                LOAD_ATTR               36 (notes)
        # |                STORE_FAST              12 (@py_assert7)
        # |                BUILD_LIST               0
        # |                STORE_FAST_LOAD_FAST   220 (@py_assert10, @py_assert7)
        # |                LOAD_FAST_BORROW        13 (@py_assert10)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   238 (@py_assert9, @py_assert9)
        # |                STORE_FAST              11 (@py_assert0)
        # |        L1:     LOAD_FAST_BORROW        11 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       391 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_CONST               7 ('%(py4)s\n{%(py4)s = %(py2)s.passed\n}')
        # |                LOAD_CONST               8 ('py2')
        # |                LOAD_CONST               9 ('view')
        # |                LOAD_GLOBAL             38 (@py_builtins)
        # |                LOAD_ATTR               40 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               44 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST               9 ('view')
        # |        L4:     LOAD_CONST              10 ('py4')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   249 (@py_format5, @py_assert1)
        # |                LOAD_ATTR               49 (append + NULL|self)
        # |                LOAD_FAST_BORROW        15 (@py_format5)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      186 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               50 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              30 (('==',))
        # |                LOAD_FAST_CHECK         14 (@py_assert9)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              31 (('%(py8)s\n{%(py8)s = %(py6)s.notes\n} == %(py11)s',))
        # |                LOAD_FAST_CHECK         12 (@py_assert7)
        # |                LOAD_FAST_CHECK         13 (@py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              11 ('py6')
        # |                LOAD_CONST               9 ('view')
        # |                LOAD_GLOBAL             38 (@py_builtins)
        # |                LOAD_ATTR               40 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               44 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               9 ('view')
        # |        L7:     LOAD_CONST              12 ('py8')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert7)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py11')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format12)
        # |                LOAD_CONST              14 ('%(py13)s')
        # |                LOAD_CONST              15 ('py13')
        # |                LOAD_FAST_BORROW        16 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format14)
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                LOAD_ATTR               49 (append + NULL|self)
        # |                LOAD_FAST_BORROW        17 (@py_format14)
        # |                CALL                     1
        # |                POP_TOP
        # |        L8:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               52 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format15)
        # |                LOAD_CONST              16 ('assert %(py16)s')
        # |                LOAD_CONST              17 ('py16')
        # |                LOAD_FAST_BORROW        18 (@py_format15)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              19 (@py_format17)
        # |                LOAD_GLOBAL             55 (AssertionError + NULL)
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               56 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        19 (@py_format17)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L9:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST              11 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST              12 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  237 (@py_assert9, @py_assert10)
        # | 212            LOAD_FAST_BORROW         8 (view)
        # |                LOAD_ATTR               58 (text)
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
        # |                LOAD_GLOBAL             10 (GOOD)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       268 (to L16)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               50 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              30 (('==',))
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              32 (('%(py2)s\n{%(py2)s = %(py0)s.text\n} == %(py4)s',))
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                LOAD_GLOBAL             10 (GOOD)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              19 ('py0')
        # |                LOAD_CONST               9 ('view')
        # |                LOAD_GLOBAL             38 (@py_builtins)
        # |                LOAD_ATTR               40 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               44 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST               9 ('view')
        # |       L12:     LOAD_CONST               8 ('py2')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py4')
        # |                LOAD_CONST              20 ('GOOD')
        # |                LOAD_GLOBAL             38 (@py_builtins)
        # |                LOAD_ATTR               40 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               44 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (GOOD)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L14)
        # |                NOT_TAKEN
        # |       L13:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (GOOD)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L15)
        # |       L14:     LOAD_CONST              20 ('GOOD')
        # |       L15:     BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format5)
        # |                LOAD_CONST              21 ('assert %(py6)s')
        # |                LOAD_CONST              11 ('py6')
        # |                LOAD_FAST_BORROW        15 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              20 (@py_format7)
        # |                LOAD_GLOBAL             55 (AssertionError + NULL)
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               56 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        20 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L16:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  154 (@py_assert1, @py_assert3)
        # | 213            LOAD_FAST_BORROW         8 (view)
        # |                LOAD_ATTR               60 (revisions)
        # |                STORE_FAST               9 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                STORE_FAST              21 (@py_assert4)
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                LOAD_FAST_BORROW        21 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       200 (to L20)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               50 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              30 (('==',))
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              33 (('%(py2)s\n{%(py2)s = %(py0)s.revisions\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                LOAD_FAST_BORROW        21 (@py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              19 ('py0')
        # |                LOAD_CONST               9 ('view')
        # |                LOAD_GLOBAL             38 (@py_builtins)
        # |                LOAD_ATTR               40 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L17)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               44 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L18)
        # |                NOT_TAKEN
        # |       L17:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L19)
        # |       L18:     LOAD_CONST               9 ('view')
        # |       L19:     LOAD_CONST               8 ('py2')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              22 ('py5')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        21 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              22 (@py_format6)
        # |                LOAD_CONST              23 ('assert %(py7)s')
        # |                LOAD_CONST              24 ('py7')
        # |                LOAD_FAST_BORROW        22 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              23 (@py_format8)
        # |                LOAD_GLOBAL             55 (AssertionError + NULL)
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               56 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        23 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L20:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert3)
        # |                STORE_FAST              21 (@py_assert4)
        # | 214            LOAD_FAST_BORROW         8 (view)
        # |                LOAD_ATTR               62 (verdict)
        # |                STORE_FAST               9 (@py_assert1)
        # |                LOAD_CONST              18 (None)
        # |                STORE_FAST              21 (@py_assert4)
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                LOAD_FAST_BORROW        21 (@py_assert4)
        # |                IS_OP                    1 (is not)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       200 (to L24)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               50 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              34 (('is not',))
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              35 (('%(py2)s\n{%(py2)s = %(py0)s.verdict\n} is not %(py5)s',))
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                LOAD_FAST_BORROW        21 (@py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              19 ('py0')
        # |                LOAD_CONST               9 ('view')
        # |                LOAD_GLOBAL             38 (@py_builtins)
        # |                LOAD_ATTR               40 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L21)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               44 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L22)
        # |                NOT_TAKEN
        # |       L21:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L23)
        # |       L22:     LOAD_CONST               9 ('view')
        # |       L23:     LOAD_CONST               8 ('py2')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              22 ('py5')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        21 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              22 (@py_format6)
        # |                LOAD_CONST              23 ('assert %(py7)s')
        # |                LOAD_CONST              24 ('py7')
        # |                LOAD_FAST_BORROW        22 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              23 (@py_format8)
        # |                LOAD_GLOBAL             55 (AssertionError + NULL)
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               56 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        23 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L24:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert3)
        # |                STORE_FAST              21 (@py_assert4)
        # | 215            LOAD_FAST_BORROW         8 (view)
        # |                LOAD_ATTR               64 (gate)
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
        # |                LOAD_ATTR               34 (passed)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       190 (to L28)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               66 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              25 ('gate 报告要能重算出来（它不进 checkpoint）')
        # |                CALL                     1
        # |                LOAD_CONST              26 ('\n>assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              19 ('py0')
        # |                LOAD_CONST               9 ('view')
        # |                LOAD_GLOBAL             38 (@py_builtins)
        # |                LOAD_ATTR               40 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L25)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               44 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L26)
        # |                NOT_TAKEN
        # |       L25:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (view)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L27)
        # |       L26:     LOAD_CONST               9 ('view')
        # |       L27:     LOAD_CONST               8 ('py2')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py4')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format5)
        # |                LOAD_GLOBAL             55 (AssertionError + NULL)
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               56 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        15 (@py_format5)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L28:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  154 (@py_assert1, @py_assert3)
        # | 216            LOAD_CONST              27 (<code object <genexpr> at 0x106720690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 216>)
        # |                MAKE_FUNCTION
        # |                LOAD_FAST_BORROW         8 (view)
        # |                LOAD_ATTR               68 (state)
        # |                LOAD_ATTR               70 (chapter_summaries)
        # |                GET_ITER
        # |                CALL                     0
        # |                STORE_FAST               9 (@py_assert1)
        # |                LOAD_GLOBAL             73 (any + NULL)
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       171 (to L32)
        # |                NOT_TAKEN
        # |                LOAD_CONST              28 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |                LOAD_CONST              19 ('py0')
        # |                LOAD_CONST              29 ('any')
        # |                LOAD_GLOBAL             38 (@py_builtins)
        # |                LOAD_ATTR               40 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L29)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               44 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             72 (any)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L30)
        # |                NOT_TAKEN
        # |       L29:     LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             72 (any)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L31)
        # |       L30:     LOAD_CONST              29 ('any')
        # |       L31:     LOAD_CONST               8 ('py2')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py4')
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               46 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format5)
        # |                LOAD_GLOBAL             55 (AssertionError + NULL)
        # |                LOAD_GLOBAL             42 (@pytest_ar)
        # |                LOAD_ATTR               56 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        15 (@py_format5)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L32:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  154 (@py_assert1, @py_assert3)
        # |                LOAD_CONST              18 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object <lambda> at 0x10671e4f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 208>:
        # | 208           RESUME                   0
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x106720690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 216>:
        # |  216           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                19 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (s, s)
        # |                LOAD_ATTR                0 (ch)
        # |                LOAD_SMALL_INT           1
        # |                COMPARE_OP              72 (==)
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           21 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti

    def test_maps_a_failing_run(self, sample_state):
        'a'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 218           RESUME                   0
        # | 219           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('ChapterPipeline',))
        # |               IMPORT_NAME              0 (novel_agent.agents.pipeline)
        # |               IMPORT_FROM              1 (ChapterPipeline)
        # |               STORE_FAST               2 (ChapterPipeline)
        # |               POP_TOP
        # | 220           LOAD_SMALL_INT           0
        # |               LOAD_CONST               2 (('ChapterResultView',))
        # |               IMPORT_NAME              2 (novel_agent.graph.build)
        # |               IMPORT_FROM              3 (ChapterResultView)
        # |               STORE_FAST               3 (ChapterResultView)
        # |               POP_TOP
        # | 222           LOAD_GLOBAL              9 (make + NULL)
        # |               LOAD_GLOBAL             10 (BAD)
        # |               LOAD_GLOBAL             10 (BAD)
        # |               LOAD_GLOBAL             10 (BAD)
        # |               LOAD_GLOBAL             10 (BAD)
        # |               BUILD_LIST               4
        # |               LOAD_GLOBAL             12 (PASS)
        # |               BUILD_LIST               1
        # |               LOAD_SMALL_INT           2
        # |               LOAD_CONST               3 (('max_revisions',))
        # |               CALL_KW                  3
        # |               UNPACK_SEQUENCE          3
        # |               STORE_FAST               4 (g)
        # |               POP_TOP
        # |               STORE_FAST               5 (_)
        # | 223           LOAD_FAST_BORROW         2 (ChapterPipeline)
        # |               PUSH_NULL
        # | 224           LOAD_GLOBAL             15 (FakeArchitect + NULL)
        # |               CALL                     0
        # |               LOAD_GLOBAL             17 (FakeWriter + NULL)
        # |               LOAD_CONST               4 ('a')
        # |               LOAD_CONST               5 ('b')
        # |               BUILD_LIST               2
        # |               CALL                     1
        # | 225           LOAD_GLOBAL             19 (FakeStitcher + NULL)
        # |               LOAD_GLOBAL             10 (BAD)
        # |               BUILD_LIST               1
        # |               CALL                     1
        # |               LOAD_GLOBAL             20 (Gate)
        # |               LOAD_ATTR               22 (from_config)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             24 (CONFIG)
        # |               CALL                     1
        # | 226           LOAD_GLOBAL             27 (FakeJudge + NULL)
        # |               LOAD_GLOBAL             12 (PASS)
        # |               BUILD_LIST               1
        # |               CALL                     1
        # |               LOAD_GLOBAL             29 (FakeArchivist + NULL)
        # |               CALL                     0
        # | 227           LOAD_CONST               6 (<code object <lambda> at 0x10671e6b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 227>)
        # |               MAKE_FUNCTION
        # | 223           LOAD_CONST               7 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'log'))
        # |               CALL_KW                  7
        # |               STORE_FAST               6 (pl)
        # | 228           LOAD_FAST_BORROW         3 (ChapterResultView)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (g)
        # |               LOAD_ATTR               31 (invoke + NULL|self)
        # |               LOAD_GLOBAL             33 (seed + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               CALL                     1
        # |               LOAD_FAST_BORROW         6 (pl)
        # |               CALL                     2
        # |               STORE_FAST               7 (view)
        # | 229           LOAD_FAST_BORROW         7 (view)
        # |               LOAD_ATTR               34 (passed)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       141 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               8 ('assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |               LOAD_CONST               9 ('py0')
        # |               LOAD_CONST              10 ('view')
        # |               LOAD_GLOBAL             36 (@py_builtins)
        # |               LOAD_ATTR               38 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               42 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (view)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               44 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (view)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST              10 ('view')
        # |       L3:     LOAD_CONST              11 ('py2')
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               44 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert1)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format4)
        # |               LOAD_GLOBAL             47 (AssertionError + NULL)
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               48 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format4)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              12 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  137 (@py_assert1, @py_assert3)
        # | 230           LOAD_CONST              13 ('仍未通过')
        # |               STORE_FAST_LOAD_FAST   183 (@py_assert0, view)
        # |               LOAD_ATTR               50 (notes)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   155 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         9 (@py_assert3)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   204 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               52 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              19 (('in',))
        # |               LOAD_FAST_BORROW        12 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              20 (('%(py1)s in %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 185 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              14 ('py1')
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               44 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST              15 ('py4')
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               44 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format5)
        # |               LOAD_CONST              16 ('assert %(py6)s')
        # |               LOAD_CONST              17 ('py6')
        # |               LOAD_FAST_BORROW        13 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              14 (@py_format7)
        # |               LOAD_GLOBAL             47 (AssertionError + NULL)
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               48 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        14 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L5:     LOAD_CONST              12 (None)
        # |               COPY                     1
        # |               STORE_FAST              11 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  201 (@py_assert2, @py_assert3)
        # | 231           LOAD_FAST_BORROW         7 (view)
        # |               LOAD_ATTR               54 (gate)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
        # |               LOAD_ATTR               34 (passed)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST   255 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       163 (to L9)
        # |               NOT_TAKEN
        # |               LOAD_CONST              18 ('assert not %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}')
        # |               LOAD_CONST               9 ('py0')
        # |               LOAD_CONST              10 ('view')
        # |               LOAD_GLOBAL             36 (@py_builtins)
        # |               LOAD_ATTR               38 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L6)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               42 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (view)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L7)
        # |               NOT_TAKEN
        # |       L6:     LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               44 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (view)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L8)
        # |       L7:     LOAD_CONST              10 ('view')
        # |       L8:     LOAD_CONST              11 ('py2')
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               44 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              15 ('py4')
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               44 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              16 (@py_format6)
        # |               LOAD_GLOBAL             47 (AssertionError + NULL)
        # |               LOAD_GLOBAL             40 (@pytest_ar)
        # |               LOAD_ATTR               48 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        16 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L9:     LOAD_CONST              12 (None)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  159 (@py_assert3, @py_assert5)
        # |               LOAD_CONST              12 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <lambda> at 0x10671e6b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 227>:
        # | 227           RESUME                   0
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE


class TestVolumeCompressionInGraph:
    'TestVolumeCompressionInGraph'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 234           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestVolumeCompressionInGraph')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         234
    # |               STORE_NAME               3 (__firstlineno__)
    # | 235           LOAD_CONST               1 ('两条路径行为必须一致，否则走图那条会悄悄少做一件事。')
    # |               STORE_NAME               4 (__doc__)
    # | 237           LOAD_CONST               2 (<code object _graph at 0x7b190e5680, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 237>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (_graph)
    # | 258           LOAD_CONST               3 (<code object test_triggered_at_volume_end at 0x7b191e0500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 258>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_triggered_at_volume_end)
    # | 267           LOAD_CONST               4 (<code object test_not_triggered_mid_volume at 0x7b19210500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 267>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_not_triggered_mid_volume)
    # | 273           LOAD_CONST               5 (<code object test_failure_is_reported_not_raised at 0x7b1920f400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 273>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_failure_is_reported_not_raised)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object _graph at 0x7b190e5680, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 237>:
    # |   --           MAKE_CELL                2 (ch)
    # |                MAKE_CELL                8 (o)
    # |  237           RESUME                   0
    # |  238           LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('ChapterPipeline',))
    # |                IMPORT_NAME              0 (novel_agent.agents.pipeline)
    # |                IMPORT_FROM              1 (ChapterPipeline)
    # |                STORE_FAST               3 (ChapterPipeline)
    # |                POP_TOP
    # |  239           LOAD_SMALL_INT           0
    # |                LOAD_CONST               2 (('ChapterOutline',))
    # |                IMPORT_NAME              2 (novel_agent.agents.schemas)
    # |                IMPORT_FROM              3 (ChapterOutline)
    # |                STORE_FAST               4 (ChapterOutline)
    # |                POP_TOP
    # |  240           LOAD_SMALL_INT           0
    # |                LOAD_CONST               3 (('scene',))
    # |                IMPORT_NAME              4 (test_pipeline)
    # |                IMPORT_FROM              5 (scene)
    # |                STORE_FAST               5 (scene)
    # |                POP_TOP
    # |  242           LOAD_FAST_BORROW         4 (ChapterOutline)
    # |                PUSH_NULL
    # |                LOAD_DEREF               2 (ch)
    # |                LOAD_CONST               4 ('卷末')
    # |                LOAD_CONST               5 ('大学')
    # |                LOAD_CONST               6 ('收束')
    # |  243           LOAD_FAST_BORROW         5 (scene)
    # |                PUSH_NULL
    # |                LOAD_CONST               7 ('ch')
    # |                LOAD_DEREF               2 (ch)
    # |                LOAD_CONST               8 ('03d')
    # |                FORMAT_WITH_SPEC
    # |                LOAD_CONST               9 ('_s1')
    # |                BUILD_STRING             3
    # |                CALL                     1
    # |                LOAD_FAST_BORROW         5 (scene)
    # |                PUSH_NULL
    # |                LOAD_CONST               7 ('ch')
    # |                LOAD_DEREF               2 (ch)
    # |                LOAD_CONST               8 ('03d')
    # |                FORMAT_WITH_SPEC
    # |                LOAD_CONST              10 ('_s2')
    # |                BUILD_STRING             3
    # |                CALL                     1
    # |                BUILD_LIST               2
    # |  244           LOAD_CONST              11 ('下一卷')
    # |  242           LOAD_CONST              12 (('ch', 'title', 'stage', 'intent', 'scenes', 'hook'))
    # |                CALL_KW                  6
    # |                STORE_DEREF              8 (o)
    # |  246           LOAD_BUILD_CLASS
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (ch)
    # |                LOAD_FAST_BORROW         8 (o)
    # |                BUILD_TUPLE              2
    # |                LOAD_CONST              13 (<code object Arch at 0x1067209c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 246>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_CONST              14 ('Arch')
    # |                CALL                     2
    # |                STORE_FAST               6 (Arch)
    # |  250           LOAD_FAST_BORROW         3 (ChapterPipeline)
    # |                PUSH_NULL
    # |  251           LOAD_FAST_BORROW         6 (Arch)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                LOAD_GLOBAL             13 (FakeWriter + NULL)
    # |                LOAD_CONST              15 ('场景一')
    # |                LOAD_CONST              16 ('场景二')
    # |                BUILD_LIST               2
    # |                CALL                     1
    # |  252           LOAD_GLOBAL             15 (FakeStitcher + NULL)
    # |                LOAD_GLOBAL             17 (make_chapter + NULL)
    # |                LOAD_DEREF               2 (ch)
    # |                LOAD_CONST              17 (('ch',))
    # |                CALL_KW                  1
    # |                BUILD_LIST               1
    # |                CALL                     1
    # |  253           LOAD_GLOBAL             18 (Gate)
    # |                LOAD_ATTR               20 (from_config)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             22 (CONFIG)
    # |                CALL                     1
    # |                LOAD_GLOBAL             25 (FakeJudge + NULL)
    # |                LOAD_GLOBAL             26 (PASS)
    # |                BUILD_LIST               1
    # |                CALL                     1
    # |  254           LOAD_GLOBAL             29 (FakeArchivist + NULL)
    # |                CALL                     0
    # |                LOAD_SMALL_INT           2
    # |                LOAD_CONST              18 (<code object <lambda> at 0x10671e870, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 254>)
    # |                MAKE_FUNCTION
    # |  250           LOAD_CONST              19 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'max_revisions', 'log'))
    # |                CALL_KW                  8
    # |                STORE_FAST               7 (p)
    # |  255           LOAD_FAST_BORROW_LOAD_FAST_BORROW 23 (compressor, p)
    # |                LOAD_ATTR               30 (archivist)
    # |                STORE_ATTR              16 (compress_volume)
    # |  256           LOAD_GLOBAL             35 (build_graph + NULL)
    # |                LOAD_FAST_BORROW         7 (p)
    # |                CALL                     1
    # |                RETURN_VALUE
    # | Disassembly of <code object Arch at 0x1067209c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 246>:
    # |   --           COPY_FREE_VARS           2
    # |  246           RESUME                   0
    # |                LOAD_NAME                0 (__name__)
    # |                STORE_NAME               1 (__module__)
    # |                LOAD_CONST               0 ('TestVolumeCompressionInGraph._graph.<locals>.Arch')
    # |                STORE_NAME               2 (__qualname__)
    # |                LOAD_SMALL_INT         246
    # |                STORE_NAME               3 (__firstlineno__)
    # |  247           LOAD_SMALL_INT           0
    # |                STORE_NAME               4 (calls)
    # |  248           LOAD_CONST               1 ('ch')
    # |                LOAD_LOCALS
    # |                LOAD_FROM_DICT_OR_DEREF  0 (ch)
    # |                LOAD_CONST               2 ('note')
    # |                LOAD_CONST               3 ('')
    # |                BUILD_MAP                2
    # |                LOAD_FAST_BORROW         1 (o)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               4 (<code object plan_chapter at 0x10671e790, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 248>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
    # |                STORE_NAME               5 (plan_chapter)
    # |                LOAD_CONST               5 (())
    # |                STORE_NAME               6 (__static_attributes__)
    # |                LOAD_CONST               6 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object plan_chapter at 0x10671e790, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 248>:
    # |   --           COPY_FREE_VARS           1
    # |  248           RESUME                   0
    # |                LOAD_DEREF               5 (o)
    # |                RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x10671e870, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 254>:
    # | 254           RESUME                   0
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_triggered_at_volume_end at 0x7b191e0500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 258>:
    # |   --           MAKE_CELL               10 (vs)
    # |  258           RESUME                   0
    # |  259           LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('VolumeSummary',))
    # |                IMPORT_NAME              0 (novel_agent.state.schema)
    # |                IMPORT_FROM              1 (VolumeSummary)
    # |                STORE_FAST               2 (VolumeSummary)
    # |                POP_TOP
    # |  261           LOAD_FAST_BORROW         2 (VolumeSummary)
    # |                PUSH_NULL
    # |                LOAD_SMALL_INT           1
    # |                LOAD_SMALL_INT           1
    # |                LOAD_SMALL_INT          18
    # |                LOAD_CONST               2 ('一卷梗概')
    # |                LOAD_CONST               3 (('volume', 'ch_start', 'ch_end', 'summary'))
    # |                CALL_KW                  4
    # |                STORE_DEREF             10 (vs)
    # |  262           LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                5 (_graph + NULL|self)
    # |                LOAD_FAST_BORROW        10 (vs)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               4 (<code object <lambda> at 0x10671eb10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 262>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_SMALL_INT          18
    # |                CALL                     2
    # |                LOAD_ATTR                7 (invoke + NULL|self)
    # |                LOAD_GLOBAL              9 (seed + NULL)
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                LOAD_SMALL_INT          18
    # |                LOAD_CONST               5 (('ch',))
    # |                CALL_KW                  2
    # |                CALL                     1
    # |                STORE_FAST               3 (out)
    # |  263           LOAD_FAST_BORROW         3 (out)
    # |                LOAD_CONST               6 ('done_reason')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               4 (@py_assert0)
    # |                LOAD_CONST               7 ('passed')
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format5)
    # |                LOAD_CONST              10 ('assert %(py6)s')
    # |                LOAD_CONST              11 ('py6')
    # |                LOAD_FAST_BORROW         7 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L1:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # |  264           LOAD_FAST_BORROW         3 (out)
    # |                LOAD_CONST              13 ('volume_summary')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              14 ('summary')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               4 (@py_assert0)
    # |                LOAD_CONST               2 ('一卷梗概')
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format5)
    # |                LOAD_CONST              10 ('assert %(py6)s')
    # |                LOAD_CONST              11 ('py6')
    # |                LOAD_FAST_BORROW         7 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L2:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # |  265           LOAD_FAST_BORROW         3 (out)
    # |                LOAD_CONST              15 ('story')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              16 ('volume_summaries')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert0, @py_assert0)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE        90 (to L3)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 ('梗概要并进 state')
    # |                CALL                     1
    # |                LOAD_CONST              18 ('\n>assert %(py1)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               8 ('py1')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format2)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format2)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L3:     LOAD_CONST              12 (None)
    # |                STORE_FAST               4 (@py_assert0)
    # |                LOAD_CONST              12 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x10671eb10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 262>:
    # |   --           COPY_FREE_VARS           1
    # |  262           RESUME                   0
    # |                LOAD_DEREF               1 (vs)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_not_triggered_mid_volume at 0x7b19210500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 267>:
    # |   --           MAKE_CELL               13 (calls)
    # |  267           RESUME                   0
    # |  268           BUILD_LIST               0
    # |                STORE_DEREF             13 (calls)
    # |  269           LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                1 (_graph + NULL|self)
    # |                LOAD_FAST_BORROW        13 (calls)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               0 (<code object <lambda> at 0x10664e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 269>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_SMALL_INT           5
    # |                CALL                     2
    # |                LOAD_ATTR                3 (invoke + NULL|self)
    # |                LOAD_GLOBAL              5 (seed + NULL)
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                LOAD_SMALL_INT           5
    # |                LOAD_CONST               1 (('ch',))
    # |                CALL_KW                  2
    # |                CALL                     1
    # |                STORE_FAST               2 (out)
    # |  270           BUILD_LIST               0
    # |                STORE_FAST               3 (@py_assert2)
    # |                LOAD_DEREF              13 (calls)
    # |                LOAD_FAST_BORROW         3 (@py_assert2)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       178 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('==',))
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py0)s == %(py3)s',))
    # |                LOAD_DEREF              13 (calls)
    # |                LOAD_FAST_BORROW         3 (@py_assert2)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('calls')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_DEREF              13 (calls)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_DEREF              13 (calls)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               3 ('calls')
    # |        L3:     LOAD_CONST               4 ('py3')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert2)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format4)
    # |                LOAD_CONST               5 ('assert %(py5)s')
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_FAST_BORROW         5 (@py_format4)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format6)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format6)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               7 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   67 (@py_assert1, @py_assert2)
    # |  271           LOAD_FAST_BORROW         2 (out)
    # |                LOAD_ATTR               22 (get)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_CONST               8 ('volume_summary')
    # |                STORE_FAST_LOAD_FAST   116 (@py_assert3, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                CALL                     1
    # |                STORE_FAST               8 (@py_assert5)
    # |                LOAD_CONST               7 (None)
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert8, @py_assert5)
    # |                LOAD_FAST_BORROW         9 (@py_assert8)
    # |                IS_OP                    0 (is)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert7, @py_assert7)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       243 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              18 (('is',))
    # |                LOAD_FAST_BORROW        10 (@py_assert7)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} is %(py9)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert5, @py_assert8)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               9 ('out')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (out)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (out)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               9 ('out')
    # |        L7:     LOAD_CONST              10 ('py2')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py4')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert8)
    # |                CALL                     1
    # |                BUILD_MAP                5
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format10)
    # |                LOAD_CONST              14 ('assert %(py11)s')
    # |                LOAD_CONST              15 ('py11')
    # |                LOAD_FAST_BORROW        11 (@py_format10)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format12)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format12)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST               7 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  169 (@py_assert7, @py_assert8)
    # |                LOAD_CONST               7 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x10664e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 269>:
    # |   --           COPY_FREE_VARS           1
    # |  269           RESUME                   0
    # |                LOAD_DEREF               1 (calls)
    # |                LOAD_ATTR                1 (append + NULL|self)
    # |                LOAD_FAST_BORROW         0 (a)
    # |                CALL                     1
    # |                RETURN_VALUE
    # | Disassembly of <code object test_failure_is_reported_not_raised at 0x7b1920f400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 273>:
    # | 273           RESUME                   0
    # | 274           LOAD_CONST               0 (<code object boom at 0x10666b5a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 274>)
    # |               MAKE_FUNCTION
    # |               STORE_FAST               2 (boom)
    # | 277           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                1 (_graph + NULL|self)
    # |               LOAD_FAST_BORROW         2 (boom)
    # |               LOAD_SMALL_INT          18
    # |               CALL                     2
    # |               LOAD_ATTR                3 (invoke + NULL|self)
    # |               LOAD_GLOBAL              5 (seed + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               LOAD_SMALL_INT          18
    # |               LOAD_CONST               1 (('ch',))
    # |               CALL_KW                  2
    # |               CALL                     1
    # |               STORE_FAST               3 (out)
    # | 278           LOAD_FAST_BORROW         3 (out)
    # |               LOAD_CONST               2 ('done_reason')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               4 (@py_assert0)
    # |               LOAD_CONST               3 ('passed')
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       148 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (('==',))
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              14 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format5)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               12 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST               6 ('记账失败不该把一章判死')
    # |               CALL                     1
    # |               LOAD_CONST               7 ('\n>assert %(py6)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               8 ('py6')
    # |               LOAD_FAST_BORROW         7 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format7)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # | 279           LOAD_CONST              10 ('上游 403')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert0, out)
    # |               LOAD_CONST              11 ('compress_error')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('in',))
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py1)s in %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format5)
    # |               LOAD_CONST              12 ('assert %(py6)s')
    # |               LOAD_CONST               8 ('py6')
    # |               LOAD_FAST_BORROW         7 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format7)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object boom at 0x10666b5a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 274>:
    # | 274           RESUME                   0
    # | 275           LOAD_GLOBAL              1 (RuntimeError + NULL)
    # |               LOAD_CONST               0 ('上游 403')
    # |               CALL                     1
    # |               RAISE_VARARGS            1

    def _graph(self, compressor, ch):
        '卷末'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                2 (ch)
        # |                MAKE_CELL                8 (o)
        # |  237           RESUME                   0
        # |  238           LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('ChapterPipeline',))
        # |                IMPORT_NAME              0 (novel_agent.agents.pipeline)
        # |                IMPORT_FROM              1 (ChapterPipeline)
        # |                STORE_FAST               3 (ChapterPipeline)
        # |                POP_TOP
        # |  239           LOAD_SMALL_INT           0
        # |                LOAD_CONST               2 (('ChapterOutline',))
        # |                IMPORT_NAME              2 (novel_agent.agents.schemas)
        # |                IMPORT_FROM              3 (ChapterOutline)
        # |                STORE_FAST               4 (ChapterOutline)
        # |                POP_TOP
        # |  240           LOAD_SMALL_INT           0
        # |                LOAD_CONST               3 (('scene',))
        # |                IMPORT_NAME              4 (test_pipeline)
        # |                IMPORT_FROM              5 (scene)
        # |                STORE_FAST               5 (scene)
        # |                POP_TOP
        # |  242           LOAD_FAST_BORROW         4 (ChapterOutline)
        # |                PUSH_NULL
        # |                LOAD_DEREF               2 (ch)
        # |                LOAD_CONST               4 ('卷末')
        # |                LOAD_CONST               5 ('大学')
        # |                LOAD_CONST               6 ('收束')
        # |  243           LOAD_FAST_BORROW         5 (scene)
        # |                PUSH_NULL
        # |                LOAD_CONST               7 ('ch')
        # |                LOAD_DEREF               2 (ch)
        # |                LOAD_CONST               8 ('03d')
        # |                FORMAT_WITH_SPEC
        # |                LOAD_CONST               9 ('_s1')
        # |                BUILD_STRING             3
        # |                CALL                     1
        # |                LOAD_FAST_BORROW         5 (scene)
        # |                PUSH_NULL
        # |                LOAD_CONST               7 ('ch')
        # |                LOAD_DEREF               2 (ch)
        # |                LOAD_CONST               8 ('03d')
        # |                FORMAT_WITH_SPEC
        # |                LOAD_CONST              10 ('_s2')
        # |                BUILD_STRING             3
        # |                CALL                     1
        # |                BUILD_LIST               2
        # |  244           LOAD_CONST              11 ('下一卷')
        # |  242           LOAD_CONST              12 (('ch', 'title', 'stage', 'intent', 'scenes', 'hook'))
        # |                CALL_KW                  6
        # |                STORE_DEREF              8 (o)
        # |  246           LOAD_BUILD_CLASS
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (ch)
        # |                LOAD_FAST_BORROW         8 (o)
        # |                BUILD_TUPLE              2
        # |                LOAD_CONST              13 (<code object Arch at 0x1067209c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 246>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_CONST              14 ('Arch')
        # |                CALL                     2
        # |                STORE_FAST               6 (Arch)
        # |  250           LOAD_FAST_BORROW         3 (ChapterPipeline)
        # |                PUSH_NULL
        # |  251           LOAD_FAST_BORROW         6 (Arch)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                LOAD_GLOBAL             13 (FakeWriter + NULL)
        # |                LOAD_CONST              15 ('场景一')
        # |                LOAD_CONST              16 ('场景二')
        # |                BUILD_LIST               2
        # |                CALL                     1
        # |  252           LOAD_GLOBAL             15 (FakeStitcher + NULL)
        # |                LOAD_GLOBAL             17 (make_chapter + NULL)
        # |                LOAD_DEREF               2 (ch)
        # |                LOAD_CONST              17 (('ch',))
        # |                CALL_KW                  1
        # |                BUILD_LIST               1
        # |                CALL                     1
        # |  253           LOAD_GLOBAL             18 (Gate)
        # |                LOAD_ATTR               20 (from_config)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             22 (CONFIG)
        # |                CALL                     1
        # |                LOAD_GLOBAL             25 (FakeJudge + NULL)
        # |                LOAD_GLOBAL             26 (PASS)
        # |                BUILD_LIST               1
        # |                CALL                     1
        # |  254           LOAD_GLOBAL             29 (FakeArchivist + NULL)
        # |                CALL                     0
        # |                LOAD_SMALL_INT           2
        # |                LOAD_CONST              18 (<code object <lambda> at 0x10671e870, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 254>)
        # |                MAKE_FUNCTION
        # |  250           LOAD_CONST              19 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'max_revisions', 'log'))
        # |                CALL_KW                  8
        # |                STORE_FAST               7 (p)
        # |  255           LOAD_FAST_BORROW_LOAD_FAST_BORROW 23 (compressor, p)
        # |                LOAD_ATTR               30 (archivist)
        # |                STORE_ATTR              16 (compress_volume)
        # |  256           LOAD_GLOBAL             35 (build_graph + NULL)
        # |                LOAD_FAST_BORROW         7 (p)
        # |                CALL                     1
        # |                RETURN_VALUE
        # | Disassembly of <code object Arch at 0x1067209c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 246>:
        # |   --           COPY_FREE_VARS           2
        # |  246           RESUME                   0
        # |                LOAD_NAME                0 (__name__)
        # |                STORE_NAME               1 (__module__)
        # |                LOAD_CONST               0 ('TestVolumeCompressionInGraph._graph.<locals>.Arch')
        # |                STORE_NAME               2 (__qualname__)
        # |                LOAD_SMALL_INT         246
        # |                STORE_NAME               3 (__firstlineno__)
        # |  247           LOAD_SMALL_INT           0
        # |                STORE_NAME               4 (calls)
        # |  248           LOAD_CONST               1 ('ch')
        # |                LOAD_LOCALS
        # |                LOAD_FROM_DICT_OR_DEREF  0 (ch)
        # |                LOAD_CONST               2 ('note')
        # |                LOAD_CONST               3 ('')
        # |                BUILD_MAP                2
        # |                LOAD_FAST_BORROW         1 (o)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               4 (<code object plan_chapter at 0x10671e790, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 248>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
        # |                STORE_NAME               5 (plan_chapter)
        # |                LOAD_CONST               5 (())
        # |                STORE_NAME               6 (__static_attributes__)
        # |                LOAD_CONST               6 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object plan_chapter at 0x10671e790, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 248>:
        # |   --           COPY_FREE_VARS           1
        # |  248           RESUME                   0
        # |                LOAD_DEREF               5 (o)
        # |                RETURN_VALUE
        # | Disassembly of <code object <lambda> at 0x10671e870, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 254>:
        # | 254           RESUME                   0
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE

        def Arch():
            'TestVolumeCompressionInGraph._graph.<locals>.Arch'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           2
            # |  246           RESUME                   0
            # |                LOAD_NAME                0 (__name__)
            # |                STORE_NAME               1 (__module__)
            # |                LOAD_CONST               0 ('TestVolumeCompressionInGraph._graph.<locals>.Arch')
            # |                STORE_NAME               2 (__qualname__)
            # |                LOAD_SMALL_INT         246
            # |                STORE_NAME               3 (__firstlineno__)
            # |  247           LOAD_SMALL_INT           0
            # |                STORE_NAME               4 (calls)
            # |  248           LOAD_CONST               1 ('ch')
            # |                LOAD_LOCALS
            # |                LOAD_FROM_DICT_OR_DEREF  0 (ch)
            # |                LOAD_CONST               2 ('note')
            # |                LOAD_CONST               3 ('')
            # |                BUILD_MAP                2
            # |                LOAD_FAST_BORROW         1 (o)
            # |                BUILD_TUPLE              1
            # |                LOAD_CONST               4 (<code object plan_chapter at 0x10671e790, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 248>)
            # |                MAKE_FUNCTION
            # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
            # |                SET_FUNCTION_ATTRIBUTE   2 (kwdefaults)
            # |                STORE_NAME               5 (plan_chapter)
            # |                LOAD_CONST               5 (())
            # |                STORE_NAME               6 (__static_attributes__)
            # |                LOAD_CONST               6 (None)
            # |                RETURN_VALUE
            # | Disassembly of <code object plan_chapter at 0x10671e790, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 248>:
            # |   --           COPY_FREE_VARS           1
            # |  248           RESUME                   0
            # |                LOAD_DEREF               5 (o)
            # |                RETURN_VALUE

            def plan_chapter(self, state, vol, *, ch, note):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # |   --           COPY_FREE_VARS           1
                # |  248           RESUME                   0
                # |                LOAD_DEREF               5 (o)
                # |                RETURN_VALUE



    def test_triggered_at_volume_end(self, sample_state):
        '一卷梗概'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL               10 (vs)
        # |  258           RESUME                   0
        # |  259           LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('VolumeSummary',))
        # |                IMPORT_NAME              0 (novel_agent.state.schema)
        # |                IMPORT_FROM              1 (VolumeSummary)
        # |                STORE_FAST               2 (VolumeSummary)
        # |                POP_TOP
        # |  261           LOAD_FAST_BORROW         2 (VolumeSummary)
        # |                PUSH_NULL
        # |                LOAD_SMALL_INT           1
        # |                LOAD_SMALL_INT           1
        # |                LOAD_SMALL_INT          18
        # |                LOAD_CONST               2 ('一卷梗概')
        # |                LOAD_CONST               3 (('volume', 'ch_start', 'ch_end', 'summary'))
        # |                CALL_KW                  4
        # |                STORE_DEREF             10 (vs)
        # |  262           LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                5 (_graph + NULL|self)
        # |                LOAD_FAST_BORROW        10 (vs)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               4 (<code object <lambda> at 0x10671eb10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 262>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_SMALL_INT          18
        # |                CALL                     2
        # |                LOAD_ATTR                7 (invoke + NULL|self)
        # |                LOAD_GLOBAL              9 (seed + NULL)
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                LOAD_SMALL_INT          18
        # |                LOAD_CONST               5 (('ch',))
        # |                CALL_KW                  2
        # |                CALL                     1
        # |                STORE_FAST               3 (out)
        # |  263           LOAD_FAST_BORROW         3 (out)
        # |                LOAD_CONST               6 ('done_reason')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               4 (@py_assert0)
        # |                LOAD_CONST               7 ('passed')
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format5)
        # |                LOAD_CONST              10 ('assert %(py6)s')
        # |                LOAD_CONST              11 ('py6')
        # |                LOAD_FAST_BORROW         7 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L1:     LOAD_CONST              12 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # |  264           LOAD_FAST_BORROW         3 (out)
        # |                LOAD_CONST              13 ('volume_summary')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              14 ('summary')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               4 (@py_assert0)
        # |                LOAD_CONST               2 ('一卷梗概')
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format5)
        # |                LOAD_CONST              10 ('assert %(py6)s')
        # |                LOAD_CONST              11 ('py6')
        # |                LOAD_FAST_BORROW         7 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L2:     LOAD_CONST              12 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # |  265           LOAD_FAST_BORROW         3 (out)
        # |                LOAD_CONST              15 ('story')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              16 ('volume_summaries')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert0, @py_assert0)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE        90 (to L3)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 ('梗概要并进 state')
        # |                CALL                     1
        # |                LOAD_CONST              18 ('\n>assert %(py1)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               8 ('py1')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format2)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format2)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L3:     LOAD_CONST              12 (None)
        # |                STORE_FAST               4 (@py_assert0)
        # |                LOAD_CONST              12 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object <lambda> at 0x10671eb10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 262>:
        # |   --           COPY_FREE_VARS           1
        # |  262           RESUME                   0
        # |                LOAD_DEREF               1 (vs)
        # |                RETURN_VALUE

    def test_not_triggered_mid_volume(self, sample_state):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL               13 (calls)
        # |  267           RESUME                   0
        # |  268           BUILD_LIST               0
        # |                STORE_DEREF             13 (calls)
        # |  269           LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                1 (_graph + NULL|self)
        # |                LOAD_FAST_BORROW        13 (calls)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               0 (<code object <lambda> at 0x10664e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 269>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_SMALL_INT           5
        # |                CALL                     2
        # |                LOAD_ATTR                3 (invoke + NULL|self)
        # |                LOAD_GLOBAL              5 (seed + NULL)
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                LOAD_SMALL_INT           5
        # |                LOAD_CONST               1 (('ch',))
        # |                CALL_KW                  2
        # |                CALL                     1
        # |                STORE_FAST               2 (out)
        # |  270           BUILD_LIST               0
        # |                STORE_FAST               3 (@py_assert2)
        # |                LOAD_DEREF              13 (calls)
        # |                LOAD_FAST_BORROW         3 (@py_assert2)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       178 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('==',))
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py0)s == %(py3)s',))
        # |                LOAD_DEREF              13 (calls)
        # |                LOAD_FAST_BORROW         3 (@py_assert2)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               3 ('calls')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_DEREF              13 (calls)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_DEREF              13 (calls)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               3 ('calls')
        # |        L3:     LOAD_CONST               4 ('py3')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert2)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format4)
        # |                LOAD_CONST               5 ('assert %(py5)s')
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_FAST_BORROW         5 (@py_format4)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format6)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format6)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               7 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   67 (@py_assert1, @py_assert2)
        # |  271           LOAD_FAST_BORROW         2 (out)
        # |                LOAD_ATTR               22 (get)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_CONST               8 ('volume_summary')
        # |                STORE_FAST_LOAD_FAST   116 (@py_assert3, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                CALL                     1
        # |                STORE_FAST               8 (@py_assert5)
        # |                LOAD_CONST               7 (None)
        # |                STORE_FAST_LOAD_FAST   152 (@py_assert8, @py_assert5)
        # |                LOAD_FAST_BORROW         9 (@py_assert8)
        # |                IS_OP                    0 (is)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert7, @py_assert7)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       243 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              18 (('is',))
        # |                LOAD_FAST_BORROW        10 (@py_assert7)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.get\n}(%(py4)s)\n} is %(py9)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert5, @py_assert8)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               9 ('out')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (out)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (out)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               9 ('out')
        # |        L7:     LOAD_CONST              10 ('py2')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py4')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert8)
        # |                CALL                     1
        # |                BUILD_MAP                5
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format10)
        # |                LOAD_CONST              14 ('assert %(py11)s')
        # |                LOAD_CONST              15 ('py11')
        # |                LOAD_FAST_BORROW        11 (@py_format10)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format12)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format12)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST               7 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  169 (@py_assert7, @py_assert8)
        # |                LOAD_CONST               7 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object <lambda> at 0x10664e730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 269>:
        # |   --           COPY_FREE_VARS           1
        # |  269           RESUME                   0
        # |                LOAD_DEREF               1 (calls)
        # |                LOAD_ATTR                1 (append + NULL|self)
        # |                LOAD_FAST_BORROW         0 (a)
        # |                CALL                     1
        # |                RETURN_VALUE

    def test_failure_is_reported_not_raised(self, sample_state):
        'done_reason'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 273           RESUME                   0
        # | 274           LOAD_CONST               0 (<code object boom at 0x10666b5a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 274>)
        # |               MAKE_FUNCTION
        # |               STORE_FAST               2 (boom)
        # | 277           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                1 (_graph + NULL|self)
        # |               LOAD_FAST_BORROW         2 (boom)
        # |               LOAD_SMALL_INT          18
        # |               CALL                     2
        # |               LOAD_ATTR                3 (invoke + NULL|self)
        # |               LOAD_GLOBAL              5 (seed + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               LOAD_SMALL_INT          18
        # |               LOAD_CONST               1 (('ch',))
        # |               CALL_KW                  2
        # |               CALL                     1
        # |               STORE_FAST               3 (out)
        # | 278           LOAD_FAST_BORROW         3 (out)
        # |               LOAD_CONST               2 ('done_reason')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               4 (@py_assert0)
        # |               LOAD_CONST               3 ('passed')
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       148 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (('==',))
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              14 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format5)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               12 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST               6 ('记账失败不该把一章判死')
        # |               CALL                     1
        # |               LOAD_CONST               7 ('\n>assert %(py6)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               8 ('py6')
        # |               LOAD_FAST_BORROW         7 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format7)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # | 279           LOAD_CONST              10 ('上游 403')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert0, out)
        # |               LOAD_CONST              11 ('compress_error')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('in',))
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py1)s in %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format5)
        # |               LOAD_CONST              12 ('assert %(py6)s')
        # |               LOAD_CONST               8 ('py6')
        # |               LOAD_FAST_BORROW         7 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format7)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object boom at 0x10666b5a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 274>:
        # | 274           RESUME                   0
        # | 275           LOAD_GLOBAL              1 (RuntimeError + NULL)
        # |               LOAD_CONST               0 ('上游 403')
        # |               CALL                     1
        # |               RAISE_VARARGS            1

        def boom(*a):
            '上游 403'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 274           RESUME                   0
            # | 275           LOAD_GLOBAL              1 (RuntimeError + NULL)
            # |               LOAD_CONST               0 ('上游 403')
            # |               CALL                     1
            # |               RAISE_VARARGS            1



class TestArchiveFailureInGraph:
    'TestArchiveFailureInGraph'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 282           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestArchiveFailureInGraph')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_CONST               1 (282)
    # |               STORE_NAME               3 (__firstlineno__)
    # | 283           LOAD_CONST               2 ('两条路径行为必须一致。')
    # |               STORE_NAME               4 (__doc__)
    # | 285           LOAD_CONST               3 (<code object test_chapter_survives_a_failed_archive at 0x7b190d3800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 285>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_chapter_survives_a_failed_archive)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_chapter_survives_a_failed_archive at 0x7b190d3800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 285>:
    # | 285           RESUME                   0
    # | 286           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('ChapterPipeline',))
    # |               IMPORT_NAME              0 (novel_agent.agents.pipeline)
    # |               IMPORT_FROM              1 (ChapterPipeline)
    # |               STORE_FAST               2 (ChapterPipeline)
    # |               POP_TOP
    # | 288           LOAD_GLOBAL              5 (FakeArchivist + NULL)
    # |               CALL                     0
    # |               STORE_FAST               3 (a)
    # | 289           LOAD_CONST               2 (<code object boom at 0x10666b690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 289>)
    # |               MAKE_FUNCTION
    # |               STORE_FAST               4 (boom)
    # | 291           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (boom, a)
    # |               STORE_ATTR               3 (archive)
    # | 292           LOAD_FAST_BORROW         2 (ChapterPipeline)
    # |               PUSH_NULL
    # | 293           LOAD_GLOBAL              9 (FakeArchitect + NULL)
    # |               CALL                     0
    # |               LOAD_GLOBAL             11 (FakeWriter + NULL)
    # |               LOAD_CONST               3 ('场景一')
    # |               LOAD_CONST               4 ('场景二')
    # |               BUILD_LIST               2
    # |               CALL                     1
    # | 294           LOAD_GLOBAL             13 (FakeStitcher + NULL)
    # |               LOAD_GLOBAL             14 (GOOD)
    # |               BUILD_LIST               1
    # |               CALL                     1
    # |               LOAD_GLOBAL             16 (Gate)
    # |               LOAD_ATTR               18 (from_config)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             20 (CONFIG)
    # |               CALL                     1
    # | 295           LOAD_GLOBAL             23 (FakeJudge + NULL)
    # |               LOAD_GLOBAL             24 (PASS)
    # |               BUILD_LIST               1
    # |               CALL                     1
    # |               LOAD_FAST_BORROW         3 (a)
    # |               LOAD_SMALL_INT           2
    # | 296           LOAD_CONST               5 (<code object <lambda> at 0x10671ebf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 296>)
    # |               MAKE_FUNCTION
    # | 292           LOAD_CONST               6 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'max_revisions', 'log'))
    # |               CALL_KW                  8
    # |               STORE_FAST               5 (p)
    # | 297           LOAD_GLOBAL             27 (build_graph + NULL)
    # |               LOAD_FAST_BORROW         5 (p)
    # |               CALL                     1
    # |               LOAD_ATTR               29 (invoke + NULL|self)
    # |               LOAD_GLOBAL             31 (seed + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               CALL                     1
    # |               STORE_FAST               6 (out)
    # | 298           LOAD_FAST_BORROW         6 (out)
    # |               LOAD_CONST               7 ('done_reason')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               7 (@py_assert0)
    # |               LOAD_CONST               8 ('passed')
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         8 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               34 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              22 (('==',))
    # |               LOAD_FAST_BORROW         9 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              23 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               9 ('py1')
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               36 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py4')
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               36 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format5)
    # |               LOAD_CONST              11 ('assert %(py6)s')
    # |               LOAD_CONST              12 ('py6')
    # |               LOAD_FAST_BORROW        10 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format7)
    # |               LOAD_GLOBAL             39 (AssertionError + NULL)
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               40 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  152 (@py_assert2, @py_assert3)
    # | 299           LOAD_CONST              14 ('第 0 章')
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert0, out)
    # |               LOAD_CONST              15 ('archive_error')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         8 (@py_assert3)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               34 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              24 (('in',))
    # |               LOAD_FAST_BORROW         9 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              25 (('%(py1)s in %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               9 ('py1')
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               36 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py4')
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               36 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format5)
    # |               LOAD_CONST              11 ('assert %(py6)s')
    # |               LOAD_CONST              12 ('py6')
    # |               LOAD_FAST_BORROW        10 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format7)
    # |               LOAD_GLOBAL             39 (AssertionError + NULL)
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               40 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  152 (@py_assert2, @py_assert3)
    # | 300           LOAD_FAST_BORROW         6 (out)
    # |               LOAD_CONST              16 ('text')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert0, @py_assert0)
    # |               LOAD_GLOBAL             14 (GOOD)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       217 (to L6)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               34 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              22 (('==',))
    # |               LOAD_FAST_BORROW         9 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              26 (('%(py1)s == %(py3)s',))
    # |               LOAD_FAST_BORROW         7 (@py_assert0)
    # |               LOAD_GLOBAL             14 (GOOD)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               9 ('py1')
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               36 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST              17 ('py3')
    # |               LOAD_CONST              18 ('GOOD')
    # |               LOAD_GLOBAL             42 (@py_builtins)
    # |               LOAD_ATTR               44 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               46 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             14 (GOOD)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L4)
    # |               NOT_TAKEN
    # |       L3:     LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               36 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             14 (GOOD)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L5)
    # |       L4:     LOAD_CONST              18 ('GOOD')
    # |       L5:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format4)
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               48 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST              19 ('正文要留在结果里')
    # |               CALL                     1
    # |               LOAD_CONST              20 ('\n>assert %(py5)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST              21 ('py5')
    # |               LOAD_FAST_BORROW        12 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format6)
    # |               LOAD_GLOBAL             39 (AssertionError + NULL)
    # |               LOAD_GLOBAL             32 (@pytest_ar)
    # |               LOAD_ATTR               40 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        13 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L6:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  121 (@py_assert0, @py_assert2)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object boom at 0x10666b690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 289>:
    # | 289           RESUME                   0
    # | 290           LOAD_GLOBAL              1 (ValueError + NULL)
    # |               LOAD_CONST               0 ('archivist 归档的是第 0 章「」')
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # | Disassembly of <code object <lambda> at 0x10671ebf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 296>:
    # | 296           RESUME                   0
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE

    def test_chapter_survives_a_failed_archive(self, sample_state):
        '场景一'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 285           RESUME                   0
        # | 286           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('ChapterPipeline',))
        # |               IMPORT_NAME              0 (novel_agent.agents.pipeline)
        # |               IMPORT_FROM              1 (ChapterPipeline)
        # |               STORE_FAST               2 (ChapterPipeline)
        # |               POP_TOP
        # | 288           LOAD_GLOBAL              5 (FakeArchivist + NULL)
        # |               CALL                     0
        # |               STORE_FAST               3 (a)
        # | 289           LOAD_CONST               2 (<code object boom at 0x10666b690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 289>)
        # |               MAKE_FUNCTION
        # |               STORE_FAST               4 (boom)
        # | 291           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (boom, a)
        # |               STORE_ATTR               3 (archive)
        # | 292           LOAD_FAST_BORROW         2 (ChapterPipeline)
        # |               PUSH_NULL
        # | 293           LOAD_GLOBAL              9 (FakeArchitect + NULL)
        # |               CALL                     0
        # |               LOAD_GLOBAL             11 (FakeWriter + NULL)
        # |               LOAD_CONST               3 ('场景一')
        # |               LOAD_CONST               4 ('场景二')
        # |               BUILD_LIST               2
        # |               CALL                     1
        # | 294           LOAD_GLOBAL             13 (FakeStitcher + NULL)
        # |               LOAD_GLOBAL             14 (GOOD)
        # |               BUILD_LIST               1
        # |               CALL                     1
        # |               LOAD_GLOBAL             16 (Gate)
        # |               LOAD_ATTR               18 (from_config)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             20 (CONFIG)
        # |               CALL                     1
        # | 295           LOAD_GLOBAL             23 (FakeJudge + NULL)
        # |               LOAD_GLOBAL             24 (PASS)
        # |               BUILD_LIST               1
        # |               CALL                     1
        # |               LOAD_FAST_BORROW         3 (a)
        # |               LOAD_SMALL_INT           2
        # | 296           LOAD_CONST               5 (<code object <lambda> at 0x10671ebf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 296>)
        # |               MAKE_FUNCTION
        # | 292           LOAD_CONST               6 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'max_revisions', 'log'))
        # |               CALL_KW                  8
        # |               STORE_FAST               5 (p)
        # | 297           LOAD_GLOBAL             27 (build_graph + NULL)
        # |               LOAD_FAST_BORROW         5 (p)
        # |               CALL                     1
        # |               LOAD_ATTR               29 (invoke + NULL|self)
        # |               LOAD_GLOBAL             31 (seed + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               CALL                     1
        # |               STORE_FAST               6 (out)
        # | 298           LOAD_FAST_BORROW         6 (out)
        # |               LOAD_CONST               7 ('done_reason')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               7 (@py_assert0)
        # |               LOAD_CONST               8 ('passed')
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         8 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               34 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              22 (('==',))
        # |               LOAD_FAST_BORROW         9 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              23 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               9 ('py1')
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               36 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py4')
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               36 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format5)
        # |               LOAD_CONST              11 ('assert %(py6)s')
        # |               LOAD_CONST              12 ('py6')
        # |               LOAD_FAST_BORROW        10 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format7)
        # |               LOAD_GLOBAL             39 (AssertionError + NULL)
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               40 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  152 (@py_assert2, @py_assert3)
        # | 299           LOAD_CONST              14 ('第 0 章')
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert0, out)
        # |               LOAD_CONST              15 ('archive_error')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         8 (@py_assert3)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               34 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              24 (('in',))
        # |               LOAD_FAST_BORROW         9 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              25 (('%(py1)s in %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               9 ('py1')
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               36 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py4')
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               36 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format5)
        # |               LOAD_CONST              11 ('assert %(py6)s')
        # |               LOAD_CONST              12 ('py6')
        # |               LOAD_FAST_BORROW        10 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format7)
        # |               LOAD_GLOBAL             39 (AssertionError + NULL)
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               40 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  152 (@py_assert2, @py_assert3)
        # | 300           LOAD_FAST_BORROW         6 (out)
        # |               LOAD_CONST              16 ('text')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert0, @py_assert0)
        # |               LOAD_GLOBAL             14 (GOOD)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       217 (to L6)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               34 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              22 (('==',))
        # |               LOAD_FAST_BORROW         9 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              26 (('%(py1)s == %(py3)s',))
        # |               LOAD_FAST_BORROW         7 (@py_assert0)
        # |               LOAD_GLOBAL             14 (GOOD)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               9 ('py1')
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               36 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST              17 ('py3')
        # |               LOAD_CONST              18 ('GOOD')
        # |               LOAD_GLOBAL             42 (@py_builtins)
        # |               LOAD_ATTR               44 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L3)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               46 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             14 (GOOD)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L4)
        # |               NOT_TAKEN
        # |       L3:     LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               36 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             14 (GOOD)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L5)
        # |       L4:     LOAD_CONST              18 ('GOOD')
        # |       L5:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format4)
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               48 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST              19 ('正文要留在结果里')
        # |               CALL                     1
        # |               LOAD_CONST              20 ('\n>assert %(py5)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST              21 ('py5')
        # |               LOAD_FAST_BORROW        12 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format6)
        # |               LOAD_GLOBAL             39 (AssertionError + NULL)
        # |               LOAD_GLOBAL             32 (@pytest_ar)
        # |               LOAD_ATTR               40 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        13 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L6:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  121 (@py_assert0, @py_assert2)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object boom at 0x10666b690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 289>:
        # | 289           RESUME                   0
        # | 290           LOAD_GLOBAL              1 (ValueError + NULL)
        # |               LOAD_CONST               0 ('archivist 归档的是第 0 章「」')
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # | Disassembly of <code object <lambda> at 0x10671ebf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_graph.py", line 296>:
        # | 296           RESUME                   0
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE

        def boom(*args, **kw):
            'archivist 归档的是第 0 章「」'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 289           RESUME                   0
            # | 290           LOAD_GLOBAL              1 (ValueError + NULL)
            # |               LOAD_CONST               0 ('archivist 归档的是第 0 章「」')
            # |               CALL                     1
            # |               RAISE_VARARGS            1


