# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py
# 来源   : test_volume_summary.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '两层摘要 —— 卷末压缩与上下文分界。\n\n进上下文的章节摘要只保留"尚未被卷梗概覆盖"的那些。没有压缩，这个窗口会\n一路长到 140 章；压缩把信息压丢了，后面的章节就会写出与前卷矛盾的情节。\n所以这里既测边界计算，也测"压错对象"这类事故。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '两层摘要 —— 卷末压缩与上下文分界。\n\n进上下文的章节摘要只保留"尚未被卷梗概覆盖"的那些。没有压缩，这个窗口会\n一路长到 140 章；压缩把信息压丢了，后面的章节就会写出与前卷矛盾的情节。\n所以这里既测边界计算，也测"压错对象"这类事故。\n',
    8: 'skills',
    11: '第一卷发生的事',
    14: 'TestTwoLayerBoundary',
    16: 'TestApplyVolumeSummary',
    18: 'FakeClient',
    20: 'TestCompressVolume',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('summaries', 0): '第',
    ('summaries', 1): '章',
    ('summaries', 2): '第 ',
    ('summaries', 3): ' 章发生的事',
    ('summaries', 4): '大学',
    ('state_with', 0): '落款',
    ('TestTwoLayerBoundary', 0): 'TestTwoLayerBoundary',
    ('TestTwoLayerBoundary', 1): '分界线由"有没有被卷梗概覆盖"划，不由"最近 N 章"划。',
    ('test_without_any_volume_summary_everything_is_live', 1): 'py1',
    ('test_without_any_volume_summary_everything_is_live', 2): 'py3',
    ('test_without_any_volume_summary_everything_is_live', 3): 'list',
    ('test_without_any_volume_summary_everything_is_live', 4): 'py4',
    ('test_without_any_volume_summary_everything_is_live', 5): 'range',
    ('test_without_any_volume_summary_everything_is_live', 6): 'py6',
    ('test_without_any_volume_summary_everything_is_live', 7): 'py8',
    ('test_without_any_volume_summary_everything_is_live', 8): 'py10',
    ('test_without_any_volume_summary_everything_is_live', 9): 'py12',
    ('test_without_any_volume_summary_everything_is_live', 10): 'assert %(py14)s',
    ('test_without_any_volume_summary_everything_is_live', 11): 'py14',
    ('test_the_gap_the_old_rule_left_open', 0): '旧规则（最近 10 章）在第 11-18 章这段会把第 1-8 章弄丢：\n那时本卷还没结束，卷梗概还没产生，中间谁都不管。',
    ('test_the_gap_the_old_rule_left_open', 1): 'py1',
    ('test_the_gap_the_old_rule_left_open', 2): 'py3',
    ('test_the_gap_the_old_rule_left_open', 3): 'list',
    ('test_the_gap_the_old_rule_left_open', 4): 'py4',
    ('test_the_gap_the_old_rule_left_open', 5): 'range',
    ('test_the_gap_the_old_rule_left_open', 6): 'py6',
    ('test_the_gap_the_old_rule_left_open', 7): 'py8',
    ('test_the_gap_the_old_rule_left_open', 8): 'py10',
    ('test_the_gap_the_old_rule_left_open', 9): 'py12',
    ('test_the_gap_the_old_rule_left_open', 10): 'assert %(py14)s',
    ('test_the_gap_the_old_rule_left_open', 11): 'py14',
    ('test_the_gap_the_old_rule_left_open', 13): '本卷的第 1 章必须还看得见',
    ('test_the_gap_the_old_rule_left_open', 14): '\n>assert %(py6)s',
    ('test_compressed_chapters_drop_out', 2): 'py1',
    ('test_compressed_chapters_drop_out', 3): 'py4',
    ('test_compressed_chapters_drop_out', 4): 'assert %(py6)s',
    ('test_compressed_chapters_drop_out', 5): 'py6',
    ('test_compressed_chapters_drop_out', 7): 'py0',
    ('test_compressed_chapters_drop_out', 8): 's',
    ('test_compressed_chapters_drop_out', 9): 'py2',
    ('test_compressed_chapters_drop_out', 10): 'py7',
    ('test_compressed_chapters_drop_out', 11): 'assert %(py9)s',
    ('test_compressed_chapters_drop_out', 12): 'py9',
    ('test_cap_is_a_safety_valve_not_the_rule', 0): '上限生效就说明某一卷的压缩漏做了 —— 它不该在正常流程里起作用。',
    ('test_cap_is_a_safety_valve_not_the_rule', 2): 'py0',
    ('test_cap_is_a_safety_valve_not_the_rule', 3): 'len',
    ('test_cap_is_a_safety_valve_not_the_rule', 4): 'py1',
    ('test_cap_is_a_safety_valve_not_the_rule', 5): 's',
    ('test_cap_is_a_safety_valve_not_the_rule', 6): 'py3',
    ('test_cap_is_a_safety_valve_not_the_rule', 7): 'py5',
    ('test_cap_is_a_safety_valve_not_the_rule', 8): 'py7',
    ('test_cap_is_a_safety_valve_not_the_rule', 9): 'py9',
    ('test_cap_is_a_safety_valve_not_the_rule', 10): 'py12',
    ('test_cap_is_a_safety_valve_not_the_rule', 11): 'assert %(py14)s',
    ('test_cap_is_a_safety_valve_not_the_rule', 12): 'py14',
    ('test_empty_state', 0): '==',
    ('test_empty_state', 1): 'py0',
    ('test_empty_state', 2): 'state_with',
    ('test_empty_state', 3): 'py2',
    ('test_empty_state', 4): 'py4',
    ('test_empty_state', 5): 'py6',
    ('test_empty_state', 6): 'py8',
    ('test_empty_state', 7): 'py11',
    ('test_empty_state', 8): 'assert %(py13)s',
    ('test_empty_state', 9): 'py13',
    ('TestApplyVolumeSummary', 0): 'TestApplyVolumeSummary',
    ('test_upsert_by_volume_number', 0): '卷末压缩重跑过就该换掉旧梗概，而不是攒出两份第 1 卷。',
    ('test_upsert_by_volume_number', 1): 'summary',
    ('test_upsert_by_volume_number', 2): '改过的',
    ('test_upsert_by_volume_number', 4): 'py0',
    ('test_upsert_by_volume_number', 5): 'len',
    ('test_upsert_by_volume_number', 6): 'py1',
    ('test_upsert_by_volume_number', 7): 's',
    ('test_upsert_by_volume_number', 8): 'py3',
    ('test_upsert_by_volume_number', 9): 'py5',
    ('test_upsert_by_volume_number', 10): 'py8',
    ('test_upsert_by_volume_number', 11): 'assert %(py10)s',
    ('test_upsert_by_volume_number', 12): 'py10',
    ('test_upsert_by_volume_number', 14): 'py6',
    ('test_upsert_by_volume_number', 15): 'assert %(py8)s',
    ('test_cannot_compress_unwritten_chapters', 1): '还没写出来',
    ('test_patch_can_carry_one', 1): '卷末',
    ('test_patch_can_carry_one', 2): 's',
    ('test_patch_can_carry_one', 3): '大学',
    ('test_patch_can_carry_one', 7): 'py1',
    ('test_patch_can_carry_one', 8): 'py4',
    ('test_patch_can_carry_one', 9): 'assert %(py6)s',
    ('test_patch_can_carry_one', 10): 'py6',
    ('test_source_state_untouched', 3): 'py0',
    ('test_source_state_untouched', 4): 's',
    ('test_source_state_untouched', 5): 'py2',
    ('test_source_state_untouched', 6): 'before',
    ('test_source_state_untouched', 7): 'assert %(py4)s',
    ('test_source_state_untouched', 8): 'py4',
    ('FakeClient', 0): 'FakeClient',
    ('parse', 1): 'R',
    ('R', 0): 'FakeClient.parse.<locals>.R',
    ('TestCompressVolume', 0): 'TestCompressVolume',
    ('test_refuses_when_nothing_is_archived', 0): '没有任何章节摘要',
    ('test_wrong_volume_is_caught', 0): '与逐章归档同一类事故：归档/压缩错了对象。卷号最容易机械判定。',
    ('test_wrong_volume_is_caught', 1): 'volume',
    ('test_wrong_volume_is_caught', 3): '第 7 卷',
    ('test_chapter_range_comes_from_the_outline_not_the_model', 0): '模型只负责写那段文字，章号范围由大纲和实际归档情况订正。',
    ('test_chapter_range_comes_from_the_outline_not_the_model', 1): 'ch_start',
    ('test_chapter_range_comes_from_the_outline_not_the_model', 2): 'ch_end',
    ('test_chapter_range_comes_from_the_outline_not_the_model', 4): 'py1',
    ('test_chapter_range_comes_from_the_outline_not_the_model', 5): 'py4',
    ('test_chapter_range_comes_from_the_outline_not_the_model', 6): '只写到第 12 章就只能覆盖到 12',
    ('test_chapter_range_comes_from_the_outline_not_the_model', 7): '\n>assert %(py6)s',
    ('test_chapter_range_comes_from_the_outline_not_the_model', 8): 'py6',
    ('test_only_this_volume_goes_in', 1): '第 18 章',
    ('test_only_this_volume_goes_in', 2): 'py1',
    ('test_only_this_volume_goes_in', 3): 'py3',
    ('test_only_this_volume_goes_in', 4): 'body',
    ('test_only_this_volume_goes_in', 5): 'assert %(py5)s',
    ('test_only_this_volume_goes_in', 6): 'py5',
    ('test_only_this_volume_goes_in', 8): '第 19 章',
    ('test_only_this_volume_goes_in', 9): '下一卷的章节不该混进这一卷的梗概',
    ('test_only_this_volume_goes_in', 10): '\n>assert %(py5)s',
    ('test_bible_is_not_sent', 0): '与逐章归档同样的理由：给了大块参考资料，模型会压错对象。',
    ('test_bible_is_not_sent', 2): 'py0',
    ('test_bible_is_not_sent', 3): 'client',
    ('test_bible_is_not_sent', 4): 'py2',
    ('test_bible_is_not_sent', 5): 'py4',
    ('test_bible_is_not_sent', 6): 'py7',
    ('test_bible_is_not_sent', 7): 'assert %(py9)s',
    ('test_bible_is_not_sent', 8): 'py9',
    ('test_chapter_archive_never_emits_a_volume_summary', 0): '逐章归档时模型顺手填的卷梗概要丢掉 —— 压缩是卷末的独立动作。',
    ('test_chapter_archive_never_emits_a_volume_summary', 2): 't',
    ('test_chapter_archive_never_emits_a_volume_summary', 3): 's',
    ('test_chapter_archive_never_emits_a_volume_summary', 4): '大学',
    ('test_chapter_archive_never_emits_a_volume_summary', 8): 'i',
    ('test_chapter_archive_never_emits_a_volume_summary', 9): 'h',
    ('test_chapter_archive_never_emits_a_volume_summary', 10): 'ch001_s1',
    ('test_chapter_archive_never_emits_a_volume_summary', 11): 'w',
    ('test_chapter_archive_never_emits_a_volume_summary', 12): 'shen',
    ('test_chapter_archive_never_emits_a_volume_summary', 13): 'g',
    ('test_chapter_archive_never_emits_a_volume_summary', 14): 'a',
    ('test_chapter_archive_never_emits_a_volume_summary', 15): 'b',
    ('test_chapter_archive_never_emits_a_volume_summary', 16): 'x',
    ('test_chapter_archive_never_emits_a_volume_summary', 19): 'ch001_s2',
    ('test_chapter_archive_never_emits_a_volume_summary', 21): '正文',
    ('test_chapter_archive_never_emits_a_volume_summary', 23): 'py0',
    ('test_chapter_archive_never_emits_a_volume_summary', 24): 'got',
    ('test_chapter_archive_never_emits_a_volume_summary', 25): 'py2',
    ('test_chapter_archive_never_emits_a_volume_summary', 26): 'py5',
    ('test_chapter_archive_never_emits_a_volume_summary', 27): 'assert %(py7)s',
    ('test_chapter_archive_never_emits_a_volume_summary', 28): 'py7',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def summaries(*chs):
    '第'
    # ── 函数体（字节码重建见 BODY 段）──
    # |   25           RESUME                   0
    # |   27           LOAD_FAST_BORROW         0 (chs)
    # |                GET_ITER
    # |   26           LOAD_FAST_AND_CLEAR      1 (c)
    # |                SWAP                     2
    # |        L1:     BUILD_LIST               0
    # |                SWAP                     2
    # |   27   L2:     FOR_ITER                27 (to L3)
    # |                STORE_FAST               1 (c)
    # |   26           LOAD_GLOBAL              1 (ChapterSummary + NULL)
    # |                LOAD_FAST_BORROW         1 (c)
    # |                LOAD_CONST               0 ('第')
    # |                LOAD_FAST_BORROW         1 (c)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               1 ('章')
    # |                BUILD_STRING             3
    # |                LOAD_CONST               2 ('第 ')
    # |                LOAD_FAST_BORROW         1 (c)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               3 (' 章发生的事')
    # |                BUILD_STRING             3
    # |   27           LOAD_CONST               4 ('大学')
    # |                LOAD_CONST               5 (3000)
    # |   26           LOAD_CONST               6 (('ch', 'title', 'summary', 'stage', 'word_count'))
    # |                CALL_KW                  5
    # |                LIST_APPEND              2
    # |                JUMP_BACKWARD           29 (to L2)
    # |   27   L3:     END_FOR
    # |                POP_ITER
    # |   26   L4:     SWAP                     2
    # |                STORE_FAST               1 (c)
    # |                RETURN_VALUE
    # |   --   L5:     SWAP                     2
    # |                POP_TOP
    # |   26           SWAP                     2
    # |                STORE_FAST               1 (c)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L5 [2]

def state_with(chs, vols):
    '落款'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  30           RESUME                   0
    # |  31           LOAD_GLOBAL              1 (StoryState + NULL)
    # |               LOAD_CONST               0 ('落款')
    # |               LOAD_FAST_BORROW         0 (chs)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       12 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              3 (max + NULL)
    # |               LOAD_FAST_BORROW         0 (chs)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L2)
    # |       L1:     LOAD_SMALL_INT           0
    # |  32   L2:     LOAD_GLOBAL              5 (summaries + NULL)
    # |               LOAD_FAST_BORROW         0 (chs)
    # |               PUSH_NULL
    # |               CALL_FUNCTION_EX
    # |  33           LOAD_GLOBAL              7 (list + NULL)
    # |               LOAD_FAST_BORROW         1 (vols)
    # |               CALL                     1
    # |  31           LOAD_CONST               1 (('title', 'current_chapter', 'chapter_summaries', 'volume_summaries'))
    # |               CALL_KW                  4
    # |               RETURN_VALUE

class TestTwoLayerBoundary:
    'TestTwoLayerBoundary'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  39           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestTwoLayerBoundary')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          39
    # |               STORE_NAME               3 (__firstlineno__)
    # |  40           LOAD_CONST               1 ('分界线由"有没有被卷梗概覆盖"划，不由"最近 N 章"划。')
    # |               STORE_NAME               4 (__doc__)
    # |  42           LOAD_CONST               2 (<code object test_without_any_volume_summary_everything_is_live at 0x7c2b1fca00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 42>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_without_any_volume_summary_everything_is_live)
    # |  46           LOAD_CONST               3 (<code object test_the_gap_the_old_rule_left_open at 0x7c2b0aea00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 46>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_the_gap_the_old_rule_left_open)
    # |  53           LOAD_CONST               4 (<code object test_compressed_chapters_drop_out at 0x7c2b1fe300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 53>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_compressed_chapters_drop_out)
    # |  58           LOAD_CONST               5 (<code object test_cap_is_a_safety_valve_not_the_rule at 0x7c2ac63800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 58>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_cap_is_a_safety_valve_not_the_rule)
    # |  64           LOAD_CONST               6 (<code object test_empty_state at 0x7c2ae29e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 64>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_empty_state)
    # |               LOAD_CONST               7 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_without_any_volume_summary_everything_is_live at 0x7c2b1fca00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 42>:
    # |   42            RESUME                   0
    # |   43            LOAD_GLOBAL              1 (state_with + NULL)
    # |                 LOAD_GLOBAL              3 (range + NULL)
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_SMALL_INT          13
    # |                 CALL                     2
    # |                 CALL                     1
    # |                 STORE_FAST               1 (s)
    # |   44            LOAD_FAST_BORROW         1 (s)
    # |                 LOAD_ATTR                5 (live_summaries + NULL|self)
    # |                 CALL                     0
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      2 (x)
    # |                 SWAP                     2
    # |         L1:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                14 (to L3)
    # |                 STORE_FAST_LOAD_FAST    34 (x, x)
    # |                 LOAD_ATTR                6 (ch)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           16 (to L2)
    # |         L3:     END_FOR
    # |                 POP_ITER
    # |         L4:     STORE_FAST               3 (@py_assert0)
    # |                 STORE_FAST               2 (x)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST               4 (@py_assert5)
    # |                 LOAD_SMALL_INT          13
    # |                 STORE_FAST               5 (@py_assert7)
    # |                 LOAD_GLOBAL              3 (range + NULL)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert5, @py_assert7)
    # |                 CALL                     2
    # |                 STORE_FAST               6 (@py_assert9)
    # |                 LOAD_GLOBAL              9 (list + NULL)
    # |                 LOAD_FAST_BORROW         6 (@py_assert9)
    # |                 CALL                     1
    # |                 STORE_FAST_LOAD_FAST   115 (@py_assert11, @py_assert0)
    # |                 LOAD_FAST_BORROW         7 (@py_assert11)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       359 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              13 (('==',))
    # |                 LOAD_FAST_BORROW         8 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              14 (('%(py1)s == %(py12)s\n{%(py12)s = %(py3)s(%(py10)s\n{%(py10)s = %(py4)s(%(py6)s, %(py8)s)\n})\n}',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (@py_assert0, @py_assert11)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py1')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               2 ('py3')
    # |                 LOAD_CONST               3 ('list')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L5)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              8 (list)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L6)
    # |                 NOT_TAKEN
    # |         L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              8 (list)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L7)
    # |         L6:     LOAD_CONST               3 ('list')
    # |         L7:     LOAD_CONST               4 ('py4')
    # |                 LOAD_CONST               5 ('range')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              2 (range)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              2 (range)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST               5 ('range')
    # |        L10:     LOAD_CONST               6 ('py6')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert5)
    # |                 CALL                     1
    # |                 LOAD_CONST               7 ('py8')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert7)
    # |                 CALL                     1
    # |                 LOAD_CONST               8 ('py10')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert9)
    # |                 CALL                     1
    # |                 LOAD_CONST               9 ('py12')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert11)
    # |                 CALL                     1
    # |                 BUILD_MAP                7
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format13)
    # |                 LOAD_CONST              10 ('assert %(py14)s')
    # |                 LOAD_CONST              11 ('py14')
    # |                 LOAD_FAST_BORROW         9 (@py_format13)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              10 (@py_format15)
    # |                 LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_format15)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST              12 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               3 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST               8 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert5)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert7)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  103 (@py_assert9, @py_assert11)
    # |                 LOAD_CONST              12 (None)
    # |                 RETURN_VALUE
    # |   --   L12:     SWAP                     2
    # |                 POP_TOP
    # |   44            SWAP                     2
    # |                 STORE_FAST               2 (x)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L12 [2]
    # | Disassembly of <code object test_the_gap_the_old_rule_left_open at 0x7c2b0aea00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 46>:
    # |   46            RESUME                   0
    # |   49            LOAD_GLOBAL              1 (state_with + NULL)
    # |                 LOAD_GLOBAL              3 (range + NULL)
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_SMALL_INT          13
    # |                 CALL                     2
    # |                 CALL                     1
    # |                 STORE_FAST               1 (s)
    # |   50            LOAD_FAST_BORROW         1 (s)
    # |                 LOAD_ATTR                5 (recent_summaries + NULL|self)
    # |                 LOAD_SMALL_INT          10
    # |                 CALL                     1
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      2 (x)
    # |                 SWAP                     2
    # |         L1:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                14 (to L3)
    # |                 STORE_FAST_LOAD_FAST    34 (x, x)
    # |                 LOAD_ATTR                6 (ch)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           16 (to L2)
    # |         L3:     END_FOR
    # |                 POP_ITER
    # |         L4:     STORE_FAST               3 (@py_assert0)
    # |                 STORE_FAST               2 (x)
    # |                 LOAD_SMALL_INT           3
    # |                 STORE_FAST               4 (@py_assert5)
    # |                 LOAD_SMALL_INT          13
    # |                 STORE_FAST               5 (@py_assert7)
    # |                 LOAD_GLOBAL              3 (range + NULL)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert5, @py_assert7)
    # |                 CALL                     2
    # |                 STORE_FAST               6 (@py_assert9)
    # |                 LOAD_GLOBAL              9 (list + NULL)
    # |                 LOAD_FAST_BORROW         6 (@py_assert9)
    # |                 CALL                     1
    # |                 STORE_FAST_LOAD_FAST   115 (@py_assert11, @py_assert0)
    # |                 LOAD_FAST_BORROW         7 (@py_assert11)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       359 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              15 (('==',))
    # |                 LOAD_FAST_BORROW         8 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              16 (('%(py1)s == %(py12)s\n{%(py12)s = %(py3)s(%(py10)s\n{%(py10)s = %(py4)s(%(py6)s, %(py8)s)\n})\n}',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (@py_assert0, @py_assert11)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py1')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               2 ('py3')
    # |                 LOAD_CONST               3 ('list')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L5)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              8 (list)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L6)
    # |                 NOT_TAKEN
    # |         L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              8 (list)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L7)
    # |         L6:     LOAD_CONST               3 ('list')
    # |         L7:     LOAD_CONST               4 ('py4')
    # |                 LOAD_CONST               5 ('range')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              2 (range)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              2 (range)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST               5 ('range')
    # |        L10:     LOAD_CONST               6 ('py6')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert5)
    # |                 CALL                     1
    # |                 LOAD_CONST               7 ('py8')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert7)
    # |                 CALL                     1
    # |                 LOAD_CONST               8 ('py10')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert9)
    # |                 CALL                     1
    # |                 LOAD_CONST               9 ('py12')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert11)
    # |                 CALL                     1
    # |                 BUILD_MAP                7
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format13)
    # |                 LOAD_CONST              10 ('assert %(py14)s')
    # |                 LOAD_CONST              11 ('py14')
    # |                 LOAD_FAST_BORROW         9 (@py_format13)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              10 (@py_format15)
    # |                 LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_format15)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST              12 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               3 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST               8 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert5)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert7)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  103 (@py_assert9, @py_assert11)
    # |   51            LOAD_SMALL_INT           1
    # |                 STORE_FAST_LOAD_FAST    49 (@py_assert0, s)
    # |                 LOAD_ATTR               27 (live_summaries + NULL|self)
    # |                 CALL                     0
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      2 (x)
    # |                 SWAP                     2
    # |        L12:     BUILD_LIST               0
    # |                 SWAP                     2
    # |        L13:     FOR_ITER                14 (to L14)
    # |                 STORE_FAST_LOAD_FAST    34 (x, x)
    # |                 LOAD_ATTR                6 (ch)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           16 (to L13)
    # |        L14:     END_FOR
    # |                 POP_ITER
    # |        L15:     STORE_FAST              11 (@py_assert3)
    # |                 STORE_FAST               2 (x)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 59 (@py_assert0, @py_assert3)
    # |                 CONTAINS_OP              0 (in)
    # |                 STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       148 (to L16)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              17 (('in',))
    # |                 LOAD_FAST_BORROW         8 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              18 (('%(py1)s in %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 59 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py1')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               4 ('py4')
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format5)
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              13 ('本卷的第 1 章必须还看得见')
    # |                 CALL                     1
    # |                 LOAD_CONST              14 ('\n>assert %(py6)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST               6 ('py6')
    # |                 LOAD_FAST_BORROW        12 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format7)
    # |                 LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             10 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L16:     LOAD_CONST              12 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               3 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  139 (@py_assert2, @py_assert3)
    # |                 LOAD_CONST              12 (None)
    # |                 RETURN_VALUE
    # |   --   L17:     SWAP                     2
    # |                 POP_TOP
    # |   50            SWAP                     2
    # |                 STORE_FAST               2 (x)
    # |                 RERAISE                  0
    # |   --   L18:     SWAP                     2
    # |                 POP_TOP
    # |   51            SWAP                     2
    # |                 STORE_FAST               2 (x)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L17 [2]
    # |   L12 to L15 -> L18 [2]
    # | Disassembly of <code object test_compressed_chapters_drop_out at 0x7c2b1fe300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 53>:
    # |   53            RESUME                   0
    # |   54            LOAD_GLOBAL              1 (state_with + NULL)
    # |                 LOAD_GLOBAL              3 (list + NULL)
    # |                 LOAD_GLOBAL              5 (range + NULL)
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_SMALL_INT          21
    # |                 CALL                     2
    # |                 CALL                     1
    # |                 LOAD_GLOBAL              6 (VOL1)
    # |                 BUILD_LIST               1
    # |                 LOAD_CONST               1 (('vols',))
    # |                 CALL_KW                  2
    # |                 STORE_FAST               1 (s)
    # |   55            LOAD_FAST_BORROW         1 (s)
    # |                 LOAD_ATTR                9 (live_summaries + NULL|self)
    # |                 CALL                     0
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      2 (x)
    # |                 SWAP                     2
    # |         L1:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                14 (to L3)
    # |                 STORE_FAST_LOAD_FAST    34 (x, x)
    # |                 LOAD_ATTR               10 (ch)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           16 (to L2)
    # |         L3:     END_FOR
    # |                 POP_ITER
    # |         L4:     STORE_FAST               3 (@py_assert0)
    # |                 STORE_FAST               2 (x)
    # |                 LOAD_SMALL_INT          19
    # |                 LOAD_SMALL_INT          20
    # |                 BUILD_LIST               2
    # |                 STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |                 LOAD_FAST_BORROW         4 (@py_assert3)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       121 (to L5)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              13 (('==',))
    # |                 LOAD_FAST_BORROW         5 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              14 (('%(py1)s == %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               2 ('py1')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               3 ('py4')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               6 (@py_format5)
    # |                 LOAD_CONST               4 ('assert %(py6)s')
    # |                 LOAD_CONST               5 ('py6')
    # |                 LOAD_FAST_BORROW         6 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format7)
    # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L5:     LOAD_CONST               6 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               3 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |   56            LOAD_FAST_BORROW         1 (s)
    # |                 LOAD_ATTR               22 (compressed_through)
    # |                 STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 STORE_FAST               4 (@py_assert3)
    # |                 LOAD_SMALL_INT          18
    # |                 STORE_FAST_LOAD_FAST   148 (@py_assert6, @py_assert3)
    # |                 LOAD_FAST_BORROW         9 (@py_assert6)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   170 (@py_assert5, @py_assert5)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       221 (to L9)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              13 (('==',))
    # |                 LOAD_FAST_BORROW        10 (@py_assert5)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              15 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.compressed_through\n}()\n} == %(py7)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert3, @py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               7 ('py0')
    # |                 LOAD_CONST               8 ('s')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L6)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (s)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L7)
    # |                 NOT_TAKEN
    # |         L6:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (s)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L8)
    # |         L7:     LOAD_CONST               8 ('s')
    # |         L8:     LOAD_CONST               9 ('py2')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST               3 ('py4')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST              10 ('py7')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              11 (@py_format8)
    # |                 LOAD_CONST              11 ('assert %(py9)s')
    # |                 LOAD_CONST              12 ('py9')
    # |                 LOAD_FAST_BORROW        11 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format10)
    # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L9:     LOAD_CONST               6 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               8 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  169 (@py_assert5, @py_assert6)
    # |                 LOAD_CONST               6 (None)
    # |                 RETURN_VALUE
    # |   --   L10:     SWAP                     2
    # |                 POP_TOP
    # |   55            SWAP                     2
    # |                 STORE_FAST               2 (x)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L10 [2]
    # | Disassembly of <code object test_cap_is_a_safety_valve_not_the_rule at 0x7c2ac63800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 58>:
    # |  58            RESUME                   0
    # |  60            LOAD_GLOBAL              1 (state_with + NULL)
    # |                LOAD_GLOBAL              3 (range + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_SMALL_INT          31
    # |                CALL                     2
    # |                CALL                     1
    # |                STORE_FAST               1 (s)
    # |  61            LOAD_FAST_BORROW         1 (s)
    # |                LOAD_ATTR                4 (live_summaries)
    # |                STORE_FAST               2 (@py_assert2)
    # |                LOAD_SMALL_INT          24
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert2)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                LOAD_CONST               1 (('cap',))
    # |                CALL_KW                  1
    # |                STORE_FAST               4 (@py_assert6)
    # |                LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert6)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_SMALL_INT          24
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert8)
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert10, @py_assert10)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       351 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              14 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              15 (('%(py9)s\n{%(py9)s = %(py0)s(%(py7)s\n{%(py7)s = %(py3)s\n{%(py3)s = %(py1)s.live_summaries\n}(cap=%(py5)s)\n})\n} == %(py12)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert11)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('len')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (len)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (len)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               3 ('len')
    # |        L3:     LOAD_CONST               4 ('py1')
    # |                LOAD_CONST               5 ('s')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (s)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (s)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               5 ('s')
    # |        L6:     LOAD_CONST               6 ('py3')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py9')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py12')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format13)
    # |                LOAD_CONST              11 ('assert %(py14)s')
    # |                LOAD_CONST              12 ('py14')
    # |                LOAD_FAST_BORROW         8 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format15)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format15)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST              13 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  118 (@py_assert10, @py_assert11)
    # |  62            LOAD_FAST_BORROW         1 (s)
    # |                LOAD_ATTR                4 (live_summaries)
    # |                STORE_FAST               2 (@py_assert2)
    # |                LOAD_CONST              13 (None)
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert2)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                LOAD_CONST               1 (('cap',))
    # |                CALL_KW                  1
    # |                STORE_FAST               4 (@py_assert6)
    # |                LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert6)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_SMALL_INT          30
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert8)
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert10, @py_assert10)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       351 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              14 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              15 (('%(py9)s\n{%(py9)s = %(py0)s(%(py7)s\n{%(py7)s = %(py3)s\n{%(py3)s = %(py1)s.live_summaries\n}(cap=%(py5)s)\n})\n} == %(py12)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert11)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('len')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (len)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (len)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               3 ('len')
    # |       L10:     LOAD_CONST               4 ('py1')
    # |                LOAD_CONST               5 ('s')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (s)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L12)
    # |                NOT_TAKEN
    # |       L11:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (s)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L13)
    # |       L12:     LOAD_CONST               5 ('s')
    # |       L13:     LOAD_CONST               6 ('py3')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py9')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py12')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format13)
    # |                LOAD_CONST              11 ('assert %(py14)s')
    # |                LOAD_CONST              12 ('py14')
    # |                LOAD_FAST_BORROW         8 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format15)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format15)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L14:     LOAD_CONST              13 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  118 (@py_assert10, @py_assert11)
    # |                LOAD_CONST              13 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_empty_state at 0x7c2ae29e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 64>:
    # |  64           RESUME                   0
    # |  65           BUILD_LIST               0
    # |               STORE_FAST               1 (@py_assert1)
    # |               LOAD_GLOBAL              1 (state_with + NULL)
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    34 (@py_assert3, @py_assert3)
    # |               LOAD_ATTR                2 (live_summaries)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert5, @py_assert5)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               STORE_FAST               4 (@py_assert7)
    # |               BUILD_LIST               0
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert10, @py_assert7)
    # |               LOAD_FAST_BORROW         5 (@py_assert10)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert9, @py_assert9)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       273 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         6 (@py_assert9)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}.live_summaries\n}()\n} == %(py11)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert7, @py_assert10)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('state_with')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (state_with)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (state_with)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('state_with')
    # |       L3:     LOAD_CONST               3 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py8')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert7)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py11')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert10)
    # |               CALL                     1
    # |               BUILD_MAP                6
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format12)
    # |               LOAD_CONST               8 ('assert %(py13)s')
    # |               LOAD_CONST               9 ('py13')
    # |               LOAD_FAST_BORROW         7 (@py_format12)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format14)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format14)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert9, @py_assert10)
    # |  66           BUILD_LIST               0
    # |               STORE_FAST               1 (@py_assert1)
    # |               LOAD_GLOBAL              1 (state_with + NULL)
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    34 (@py_assert3, @py_assert3)
    # |               LOAD_ATTR               20 (compressed_through)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert5, @py_assert5)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               STORE_FAST               4 (@py_assert7)
    # |               LOAD_SMALL_INT           0
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert10, @py_assert7)
    # |               LOAD_FAST_BORROW         5 (@py_assert10)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert9, @py_assert9)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       273 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         6 (@py_assert9)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}.compressed_through\n}()\n} == %(py11)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert7, @py_assert10)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('state_with')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (state_with)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (state_with)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               2 ('state_with')
    # |       L7:     LOAD_CONST               3 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py8')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert7)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py11')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert10)
    # |               CALL                     1
    # |               BUILD_MAP                6
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format12)
    # |               LOAD_CONST               8 ('assert %(py13)s')
    # |               LOAD_CONST               9 ('py13')
    # |               LOAD_FAST_BORROW         7 (@py_format12)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format14)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format14)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert9, @py_assert10)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE

    def test_without_any_volume_summary_everything_is_live(self):
        'py1'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   42            RESUME                   0
        # |   43            LOAD_GLOBAL              1 (state_with + NULL)
        # |                 LOAD_GLOBAL              3 (range + NULL)
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_SMALL_INT          13
        # |                 CALL                     2
        # |                 CALL                     1
        # |                 STORE_FAST               1 (s)
        # |   44            LOAD_FAST_BORROW         1 (s)
        # |                 LOAD_ATTR                5 (live_summaries + NULL|self)
        # |                 CALL                     0
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      2 (x)
        # |                 SWAP                     2
        # |         L1:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                14 (to L3)
        # |                 STORE_FAST_LOAD_FAST    34 (x, x)
        # |                 LOAD_ATTR                6 (ch)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           16 (to L2)
        # |         L3:     END_FOR
        # |                 POP_ITER
        # |         L4:     STORE_FAST               3 (@py_assert0)
        # |                 STORE_FAST               2 (x)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST               4 (@py_assert5)
        # |                 LOAD_SMALL_INT          13
        # |                 STORE_FAST               5 (@py_assert7)
        # |                 LOAD_GLOBAL              3 (range + NULL)
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert5, @py_assert7)
        # |                 CALL                     2
        # |                 STORE_FAST               6 (@py_assert9)
        # |                 LOAD_GLOBAL              9 (list + NULL)
        # |                 LOAD_FAST_BORROW         6 (@py_assert9)
        # |                 CALL                     1
        # |                 STORE_FAST_LOAD_FAST   115 (@py_assert11, @py_assert0)
        # |                 LOAD_FAST_BORROW         7 (@py_assert11)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       359 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              13 (('==',))
        # |                 LOAD_FAST_BORROW         8 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              14 (('%(py1)s == %(py12)s\n{%(py12)s = %(py3)s(%(py10)s\n{%(py10)s = %(py4)s(%(py6)s, %(py8)s)\n})\n}',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (@py_assert0, @py_assert11)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py1')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               2 ('py3')
        # |                 LOAD_CONST               3 ('list')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L5)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              8 (list)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L6)
        # |                 NOT_TAKEN
        # |         L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              8 (list)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L7)
        # |         L6:     LOAD_CONST               3 ('list')
        # |         L7:     LOAD_CONST               4 ('py4')
        # |                 LOAD_CONST               5 ('range')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              2 (range)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              2 (range)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST               5 ('range')
        # |        L10:     LOAD_CONST               6 ('py6')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert5)
        # |                 CALL                     1
        # |                 LOAD_CONST               7 ('py8')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert7)
        # |                 CALL                     1
        # |                 LOAD_CONST               8 ('py10')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert9)
        # |                 CALL                     1
        # |                 LOAD_CONST               9 ('py12')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert11)
        # |                 CALL                     1
        # |                 BUILD_MAP                7
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format13)
        # |                 LOAD_CONST              10 ('assert %(py14)s')
        # |                 LOAD_CONST              11 ('py14')
        # |                 LOAD_FAST_BORROW         9 (@py_format13)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              10 (@py_format15)
        # |                 LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_format15)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST              12 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               3 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST               8 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert5)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert7)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  103 (@py_assert9, @py_assert11)
        # |                 LOAD_CONST              12 (None)
        # |                 RETURN_VALUE
        # |   --   L12:     SWAP                     2
        # |                 POP_TOP
        # |   44            SWAP                     2
        # |                 STORE_FAST               2 (x)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L12 [2]

    def test_the_gap_the_old_rule_left_open(self):
        '旧规则（最近 10 章）在第 11-18 章这段会把第 1-8 章弄丢：\n那时本卷还没结束，卷梗概还没产生，中间谁都不管。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   46            RESUME                   0
        # |   49            LOAD_GLOBAL              1 (state_with + NULL)
        # |                 LOAD_GLOBAL              3 (range + NULL)
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_SMALL_INT          13
        # |                 CALL                     2
        # |                 CALL                     1
        # |                 STORE_FAST               1 (s)
        # |   50            LOAD_FAST_BORROW         1 (s)
        # |                 LOAD_ATTR                5 (recent_summaries + NULL|self)
        # |                 LOAD_SMALL_INT          10
        # |                 CALL                     1
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      2 (x)
        # |                 SWAP                     2
        # |         L1:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                14 (to L3)
        # |                 STORE_FAST_LOAD_FAST    34 (x, x)
        # |                 LOAD_ATTR                6 (ch)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           16 (to L2)
        # |         L3:     END_FOR
        # |                 POP_ITER
        # |         L4:     STORE_FAST               3 (@py_assert0)
        # |                 STORE_FAST               2 (x)
        # |                 LOAD_SMALL_INT           3
        # |                 STORE_FAST               4 (@py_assert5)
        # |                 LOAD_SMALL_INT          13
        # |                 STORE_FAST               5 (@py_assert7)
        # |                 LOAD_GLOBAL              3 (range + NULL)
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert5, @py_assert7)
        # |                 CALL                     2
        # |                 STORE_FAST               6 (@py_assert9)
        # |                 LOAD_GLOBAL              9 (list + NULL)
        # |                 LOAD_FAST_BORROW         6 (@py_assert9)
        # |                 CALL                     1
        # |                 STORE_FAST_LOAD_FAST   115 (@py_assert11, @py_assert0)
        # |                 LOAD_FAST_BORROW         7 (@py_assert11)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       359 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              15 (('==',))
        # |                 LOAD_FAST_BORROW         8 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              16 (('%(py1)s == %(py12)s\n{%(py12)s = %(py3)s(%(py10)s\n{%(py10)s = %(py4)s(%(py6)s, %(py8)s)\n})\n}',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (@py_assert0, @py_assert11)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py1')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               2 ('py3')
        # |                 LOAD_CONST               3 ('list')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L5)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              8 (list)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L6)
        # |                 NOT_TAKEN
        # |         L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              8 (list)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L7)
        # |         L6:     LOAD_CONST               3 ('list')
        # |         L7:     LOAD_CONST               4 ('py4')
        # |                 LOAD_CONST               5 ('range')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              2 (range)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              2 (range)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST               5 ('range')
        # |        L10:     LOAD_CONST               6 ('py6')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert5)
        # |                 CALL                     1
        # |                 LOAD_CONST               7 ('py8')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert7)
        # |                 CALL                     1
        # |                 LOAD_CONST               8 ('py10')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert9)
        # |                 CALL                     1
        # |                 LOAD_CONST               9 ('py12')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert11)
        # |                 CALL                     1
        # |                 BUILD_MAP                7
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format13)
        # |                 LOAD_CONST              10 ('assert %(py14)s')
        # |                 LOAD_CONST              11 ('py14')
        # |                 LOAD_FAST_BORROW         9 (@py_format13)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              10 (@py_format15)
        # |                 LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_format15)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST              12 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               3 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST               8 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert5)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert7)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  103 (@py_assert9, @py_assert11)
        # |   51            LOAD_SMALL_INT           1
        # |                 STORE_FAST_LOAD_FAST    49 (@py_assert0, s)
        # |                 LOAD_ATTR               27 (live_summaries + NULL|self)
        # |                 CALL                     0
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      2 (x)
        # |                 SWAP                     2
        # |        L12:     BUILD_LIST               0
        # |                 SWAP                     2
        # |        L13:     FOR_ITER                14 (to L14)
        # |                 STORE_FAST_LOAD_FAST    34 (x, x)
        # |                 LOAD_ATTR                6 (ch)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           16 (to L13)
        # |        L14:     END_FOR
        # |                 POP_ITER
        # |        L15:     STORE_FAST              11 (@py_assert3)
        # |                 STORE_FAST               2 (x)
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 59 (@py_assert0, @py_assert3)
        # |                 CONTAINS_OP              0 (in)
        # |                 STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       148 (to L16)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              17 (('in',))
        # |                 LOAD_FAST_BORROW         8 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              18 (('%(py1)s in %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 59 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py1')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               4 ('py4')
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format5)
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              13 ('本卷的第 1 章必须还看得见')
        # |                 CALL                     1
        # |                 LOAD_CONST              14 ('\n>assert %(py6)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST               6 ('py6')
        # |                 LOAD_FAST_BORROW        12 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format7)
        # |                 LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             10 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L16:     LOAD_CONST              12 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               3 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  139 (@py_assert2, @py_assert3)
        # |                 LOAD_CONST              12 (None)
        # |                 RETURN_VALUE
        # |   --   L17:     SWAP                     2
        # |                 POP_TOP
        # |   50            SWAP                     2
        # |                 STORE_FAST               2 (x)
        # |                 RERAISE                  0
        # |   --   L18:     SWAP                     2
        # |                 POP_TOP
        # |   51            SWAP                     2
        # |                 STORE_FAST               2 (x)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L17 [2]
        # |   L12 to L15 -> L18 [2]

    def test_compressed_chapters_drop_out(self):
        'py1'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   53            RESUME                   0
        # |   54            LOAD_GLOBAL              1 (state_with + NULL)
        # |                 LOAD_GLOBAL              3 (list + NULL)
        # |                 LOAD_GLOBAL              5 (range + NULL)
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_SMALL_INT          21
        # |                 CALL                     2
        # |                 CALL                     1
        # |                 LOAD_GLOBAL              6 (VOL1)
        # |                 BUILD_LIST               1
        # |                 LOAD_CONST               1 (('vols',))
        # |                 CALL_KW                  2
        # |                 STORE_FAST               1 (s)
        # |   55            LOAD_FAST_BORROW         1 (s)
        # |                 LOAD_ATTR                9 (live_summaries + NULL|self)
        # |                 CALL                     0
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      2 (x)
        # |                 SWAP                     2
        # |         L1:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                14 (to L3)
        # |                 STORE_FAST_LOAD_FAST    34 (x, x)
        # |                 LOAD_ATTR               10 (ch)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           16 (to L2)
        # |         L3:     END_FOR
        # |                 POP_ITER
        # |         L4:     STORE_FAST               3 (@py_assert0)
        # |                 STORE_FAST               2 (x)
        # |                 LOAD_SMALL_INT          19
        # |                 LOAD_SMALL_INT          20
        # |                 BUILD_LIST               2
        # |                 STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |                 LOAD_FAST_BORROW         4 (@py_assert3)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       121 (to L5)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              13 (('==',))
        # |                 LOAD_FAST_BORROW         5 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              14 (('%(py1)s == %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               2 ('py1')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               3 ('py4')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               6 (@py_format5)
        # |                 LOAD_CONST               4 ('assert %(py6)s')
        # |                 LOAD_CONST               5 ('py6')
        # |                 LOAD_FAST_BORROW         6 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format7)
        # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L5:     LOAD_CONST               6 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               3 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |   56            LOAD_FAST_BORROW         1 (s)
        # |                 LOAD_ATTR               22 (compressed_through)
        # |                 STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 STORE_FAST               4 (@py_assert3)
        # |                 LOAD_SMALL_INT          18
        # |                 STORE_FAST_LOAD_FAST   148 (@py_assert6, @py_assert3)
        # |                 LOAD_FAST_BORROW         9 (@py_assert6)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   170 (@py_assert5, @py_assert5)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       221 (to L9)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              13 (('==',))
        # |                 LOAD_FAST_BORROW        10 (@py_assert5)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              15 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.compressed_through\n}()\n} == %(py7)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert3, @py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               7 ('py0')
        # |                 LOAD_CONST               8 ('s')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L6)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (s)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L7)
        # |                 NOT_TAKEN
        # |         L6:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (s)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L8)
        # |         L7:     LOAD_CONST               8 ('s')
        # |         L8:     LOAD_CONST               9 ('py2')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST               3 ('py4')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST              10 ('py7')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              11 (@py_format8)
        # |                 LOAD_CONST              11 ('assert %(py9)s')
        # |                 LOAD_CONST              12 ('py9')
        # |                 LOAD_FAST_BORROW        11 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format10)
        # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L9:     LOAD_CONST               6 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               8 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  169 (@py_assert5, @py_assert6)
        # |                 LOAD_CONST               6 (None)
        # |                 RETURN_VALUE
        # |   --   L10:     SWAP                     2
        # |                 POP_TOP
        # |   55            SWAP                     2
        # |                 STORE_FAST               2 (x)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L10 [2]

    def test_cap_is_a_safety_valve_not_the_rule(self):
        '上限生效就说明某一卷的压缩漏做了 —— 它不该在正常流程里起作用。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  58            RESUME                   0
        # |  60            LOAD_GLOBAL              1 (state_with + NULL)
        # |                LOAD_GLOBAL              3 (range + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_SMALL_INT          31
        # |                CALL                     2
        # |                CALL                     1
        # |                STORE_FAST               1 (s)
        # |  61            LOAD_FAST_BORROW         1 (s)
        # |                LOAD_ATTR                4 (live_summaries)
        # |                STORE_FAST               2 (@py_assert2)
        # |                LOAD_SMALL_INT          24
        # |                STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert2)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                LOAD_CONST               1 (('cap',))
        # |                CALL_KW                  1
        # |                STORE_FAST               4 (@py_assert6)
        # |                LOAD_GLOBAL              7 (len + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert6)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_SMALL_INT          24
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert8)
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert10, @py_assert10)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       351 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              14 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              15 (('%(py9)s\n{%(py9)s = %(py0)s(%(py7)s\n{%(py7)s = %(py3)s\n{%(py3)s = %(py1)s.live_summaries\n}(cap=%(py5)s)\n})\n} == %(py12)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert11)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               3 ('len')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (len)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (len)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               3 ('len')
        # |        L3:     LOAD_CONST               4 ('py1')
        # |                LOAD_CONST               5 ('s')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (s)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (s)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               5 ('s')
        # |        L6:     LOAD_CONST               6 ('py3')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py9')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py12')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format13)
        # |                LOAD_CONST              11 ('assert %(py14)s')
        # |                LOAD_CONST              12 ('py14')
        # |                LOAD_FAST_BORROW         8 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format15)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format15)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST              13 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  118 (@py_assert10, @py_assert11)
        # |  62            LOAD_FAST_BORROW         1 (s)
        # |                LOAD_ATTR                4 (live_summaries)
        # |                STORE_FAST               2 (@py_assert2)
        # |                LOAD_CONST              13 (None)
        # |                STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert2)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                LOAD_CONST               1 (('cap',))
        # |                CALL_KW                  1
        # |                STORE_FAST               4 (@py_assert6)
        # |                LOAD_GLOBAL              7 (len + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert6)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_SMALL_INT          30
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert8)
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert10, @py_assert10)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       351 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              14 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              15 (('%(py9)s\n{%(py9)s = %(py0)s(%(py7)s\n{%(py7)s = %(py3)s\n{%(py3)s = %(py1)s.live_summaries\n}(cap=%(py5)s)\n})\n} == %(py12)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert8, @py_assert11)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               3 ('len')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (len)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (len)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               3 ('len')
        # |       L10:     LOAD_CONST               4 ('py1')
        # |                LOAD_CONST               5 ('s')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (s)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L12)
        # |                NOT_TAKEN
        # |       L11:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (s)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L13)
        # |       L12:     LOAD_CONST               5 ('s')
        # |       L13:     LOAD_CONST               6 ('py3')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py9')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py12')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format13)
        # |                LOAD_CONST              11 ('assert %(py14)s')
        # |                LOAD_CONST              12 ('py14')
        # |                LOAD_FAST_BORROW         8 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format15)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format15)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L14:     LOAD_CONST              13 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  118 (@py_assert10, @py_assert11)
        # |                LOAD_CONST              13 (None)
        # |                RETURN_VALUE

    def test_empty_state(self):
        '=='
        # ── 函数体（字节码重建见 BODY 段）──
        # |  64           RESUME                   0
        # |  65           BUILD_LIST               0
        # |               STORE_FAST               1 (@py_assert1)
        # |               LOAD_GLOBAL              1 (state_with + NULL)
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    34 (@py_assert3, @py_assert3)
        # |               LOAD_ATTR                2 (live_summaries)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert5, @py_assert5)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               STORE_FAST               4 (@py_assert7)
        # |               BUILD_LIST               0
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert10, @py_assert7)
        # |               LOAD_FAST_BORROW         5 (@py_assert10)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert9, @py_assert9)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       273 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         6 (@py_assert9)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}.live_summaries\n}()\n} == %(py11)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert7, @py_assert10)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('state_with')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (state_with)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (state_with)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('state_with')
        # |       L3:     LOAD_CONST               3 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py8')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert7)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py11')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert10)
        # |               CALL                     1
        # |               BUILD_MAP                6
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format12)
        # |               LOAD_CONST               8 ('assert %(py13)s')
        # |               LOAD_CONST               9 ('py13')
        # |               LOAD_FAST_BORROW         7 (@py_format12)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format14)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format14)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert9, @py_assert10)
        # |  66           BUILD_LIST               0
        # |               STORE_FAST               1 (@py_assert1)
        # |               LOAD_GLOBAL              1 (state_with + NULL)
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    34 (@py_assert3, @py_assert3)
        # |               LOAD_ATTR               20 (compressed_through)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert5, @py_assert5)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               STORE_FAST               4 (@py_assert7)
        # |               LOAD_SMALL_INT           0
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert10, @py_assert7)
        # |               LOAD_FAST_BORROW         5 (@py_assert10)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert9, @py_assert9)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       273 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         6 (@py_assert9)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py8)s\n{%(py8)s = %(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}.compressed_through\n}()\n} == %(py11)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert7, @py_assert10)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('state_with')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (state_with)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (state_with)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               2 ('state_with')
        # |       L7:     LOAD_CONST               3 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py8')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert7)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py11')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert10)
        # |               CALL                     1
        # |               BUILD_MAP                6
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format12)
        # |               LOAD_CONST               8 ('assert %(py13)s')
        # |               LOAD_CONST               9 ('py13')
        # |               LOAD_FAST_BORROW         7 (@py_format12)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format14)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format14)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert9, @py_assert10)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE


class TestApplyVolumeSummary:
    'TestApplyVolumeSummary'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  69           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestApplyVolumeSummary')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          69
    # |               STORE_NAME               3 (__firstlineno__)
    # |  70           LOAD_CONST               1 (<code object test_upsert_by_volume_number at 0x7c2ae2a400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 70>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_upsert_by_volume_number)
    # |  78           LOAD_CONST               2 (<code object test_cannot_compress_unwritten_chapters at 0x103b0f120, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 78>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_cannot_compress_unwritten_chapters)
    # |  83           LOAD_CONST               3 (<code object test_patch_can_carry_one at 0x7c2ae47900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 83>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_patch_can_carry_one)
    # |  92           LOAD_CONST               4 (<code object test_source_state_untouched at 0x7c2ae3c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 92>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_source_state_untouched)
    # |               LOAD_CONST               5 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_upsert_by_volume_number at 0x7c2ae2a400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 70>:
    # |  70           RESUME                   0
    # |  72           LOAD_GLOBAL              1 (state_with + NULL)
    # |               LOAD_GLOBAL              3 (range + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_SMALL_INT          19
    # |               CALL                     2
    # |               CALL                     1
    # |               STORE_FAST               1 (s)
    # |  73           LOAD_GLOBAL              5 (apply_volume_summary + NULL)
    # |               LOAD_FAST_BORROW         1 (s)
    # |               LOAD_GLOBAL              6 (VOL1)
    # |               CALL                     2
    # |               STORE_FAST               1 (s)
    # |  74           LOAD_GLOBAL              5 (apply_volume_summary + NULL)
    # |               LOAD_FAST_BORROW         1 (s)
    # |               LOAD_GLOBAL              6 (VOL1)
    # |               LOAD_ATTR                9 (model_copy + NULL|self)
    # |               LOAD_CONST               1 ('summary')
    # |               LOAD_CONST               2 ('改过的')
    # |               BUILD_MAP                1
    # |               LOAD_CONST               3 (('update',))
    # |               CALL_KW                  1
    # |               CALL                     2
    # |               STORE_FAST               1 (s)
    # |  75           LOAD_FAST_BORROW         1 (s)
    # |               LOAD_ATTR               10 (volume_summaries)
    # |               STORE_FAST               2 (@py_assert2)
    # |               LOAD_GLOBAL             13 (len + NULL)
    # |               LOAD_FAST_BORROW         2 (@py_assert2)
    # |               CALL                     1
    # |               STORE_FAST               3 (@py_assert4)
    # |               LOAD_SMALL_INT           1
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert7, @py_assert4)
    # |               LOAD_FAST_BORROW         4 (@py_assert7)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       307 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               16 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert6)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s.volume_summaries\n})\n} == %(py8)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert4, @py_assert7)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST               5 ('len')
    # |               LOAD_GLOBAL             18 (@py_builtins)
    # |               LOAD_ATTR               20 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               22 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             12 (len)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             12 (len)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('len')
    # |       L3:     LOAD_CONST               6 ('py1')
    # |               LOAD_CONST               7 ('s')
    # |               LOAD_GLOBAL             18 (@py_builtins)
    # |               LOAD_ATTR               20 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               22 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (s)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (s)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               7 ('s')
    # |       L6:     LOAD_CONST               8 ('py3')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py5')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py8')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert7)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format9)
    # |               LOAD_CONST              11 ('assert %(py10)s')
    # |               LOAD_CONST              12 ('py10')
    # |               LOAD_FAST_BORROW         6 (@py_format9)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format11)
    # |               LOAD_GLOBAL             27 (AssertionError + NULL)
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               28 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format11)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert6, @py_assert7)
    # |  76           LOAD_FAST_BORROW         1 (s)
    # |               LOAD_ATTR               10 (volume_summaries)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert0, @py_assert0)
    # |               LOAD_ATTR               30 (summary)
    # |               STORE_FAST               2 (@py_assert2)
    # |               LOAD_CONST               2 ('改过的')
    # |               STORE_FAST_LOAD_FAST   146 (@py_assert5, @py_assert2)
    # |               LOAD_FAST_BORROW         9 (@py_assert5)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               16 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW         3 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py3)s\n{%(py3)s = %(py1)s.summary\n} == %(py6)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 41 (@py_assert2, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               6 ('py1')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py3')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST              14 ('py6')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format7)
    # |               LOAD_CONST              15 ('assert %(py8)s')
    # |               LOAD_CONST              10 ('py8')
    # |               LOAD_FAST_BORROW        10 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format9)
    # |               LOAD_GLOBAL             27 (AssertionError + NULL)
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               28 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   57 (@py_assert4, @py_assert5)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_cannot_compress_unwritten_chapters at 0x103b0f120, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 78>:
    # |   78           RESUME                   0
    # |   79           LOAD_GLOBAL              1 (state_with + NULL)
    # |                LOAD_GLOBAL              3 (range + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_SMALL_INT           6
    # |                CALL                     2
    # |                CALL                     1
    # |                STORE_FAST               1 (s)
    # |   80           LOAD_GLOBAL              4 (pytest)
    # |                LOAD_ATTR                6 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (PatchError)
    # |                LOAD_CONST               1 ('还没写出来')
    # |                LOAD_CONST               2 (('match',))
    # |                CALL_KW                  2
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |   81           LOAD_GLOBAL             11 (apply_volume_summary + NULL)
    # |                LOAD_FAST_BORROW         1 (s)
    # |                LOAD_GLOBAL             12 (VOL1)
    # |                CALL                     2
    # |                POP_TOP
    # |   80   L2:     LOAD_CONST               3 (None)
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
    # | Disassembly of <code object test_patch_can_carry_one at 0x7c2ae47900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 83>:
    # |   83           RESUME                   0
    # |   84           LOAD_GLOBAL              1 (state_with + NULL)
    # |                LOAD_GLOBAL              3 (range + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_SMALL_INT          18
    # |                CALL                     2
    # |                CALL                     1
    # |                STORE_FAST               1 (s)
    # |   85           LOAD_GLOBAL              5 (StatePatch + NULL)
    # |   86           LOAD_GLOBAL              7 (ChapterSummary + NULL)
    # |                LOAD_SMALL_INT          18
    # |                LOAD_CONST               1 ('卷末')
    # |                LOAD_CONST               2 ('s')
    # |   87           LOAD_CONST               3 ('大学')
    # |                LOAD_CONST               4 (3000)
    # |   86           LOAD_CONST               5 (('ch', 'title', 'summary', 'stage', 'word_count'))
    # |                CALL_KW                  5
    # |   88           LOAD_GLOBAL              8 (VOL1)
    # |   85           LOAD_CONST               6 (('chapter_summary', 'volume_summary'))
    # |                CALL_KW                  2
    # |                STORE_FAST               2 (patch)
    # |   89           LOAD_GLOBAL             11 (apply_patch + NULL)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (s, patch)
    # |                CALL                     2
    # |                STORE_FAST               3 (after)
    # |   90           LOAD_FAST_BORROW         3 (after)
    # |                LOAD_ATTR               12 (volume_summaries)
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      4 (v)
    # |                SWAP                     2
    # |        L1:     BUILD_LIST               0
    # |                SWAP                     2
    # |        L2:     FOR_ITER                14 (to L3)
    # |                STORE_FAST_LOAD_FAST    68 (v, v)
    # |                LOAD_ATTR               14 (volume)
    # |                LIST_APPEND              2
    # |                JUMP_BACKWARD           16 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |        L4:     STORE_FAST               5 (@py_assert0)
    # |                STORE_FAST               4 (v)
    # |                LOAD_SMALL_INT           1
    # |                BUILD_LIST               1
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              12 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              13 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               7 ('py1')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py4')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format5)
    # |                LOAD_CONST               9 ('assert %(py6)s')
    # |                LOAD_CONST              10 ('py6')
    # |                LOAD_FAST_BORROW         8 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format7)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L5:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  118 (@py_assert2, @py_assert3)
    # |                LOAD_CONST              11 (None)
    # |                RETURN_VALUE
    # |   --   L6:     SWAP                     2
    # |                POP_TOP
    # |   90           SWAP                     2
    # |                STORE_FAST               4 (v)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L6 [2]
    # | Disassembly of <code object test_source_state_untouched at 0x7c2ae3c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 92>:
    # |  92           RESUME                   0
    # |  93           LOAD_GLOBAL              1 (state_with + NULL)
    # |               LOAD_GLOBAL              3 (range + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_SMALL_INT          19
    # |               CALL                     2
    # |               CALL                     1
    # |               STORE_FAST               1 (s)
    # |  94           LOAD_FAST_BORROW         1 (s)
    # |               LOAD_ATTR                5 (model_copy + NULL|self)
    # |               LOAD_CONST               1 (True)
    # |               LOAD_CONST               2 (('deep',))
    # |               CALL_KW                  1
    # |               STORE_FAST               2 (before)
    # |  95           LOAD_GLOBAL              7 (apply_volume_summary + NULL)
    # |               LOAD_FAST_BORROW         1 (s)
    # |               LOAD_GLOBAL              8 (VOL1)
    # |               CALL                     2
    # |               POP_TOP
    # |  96           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (s, before)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       233 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('==',))
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py0)s == %(py2)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (s, before)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('s')
    # |               LOAD_GLOBAL             14 (@py_builtins)
    # |               LOAD_ATTR               16 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (s)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (s)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('s')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_CONST               6 ('before')
    # |               LOAD_GLOBAL             14 (@py_builtins)
    # |               LOAD_ATTR               16 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (before)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (before)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               6 ('before')
    # |       L6:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               4 (@py_format3)
    # |               LOAD_CONST               7 ('assert %(py4)s')
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_FAST_BORROW         4 (@py_format3)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST               9 (None)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE

    def test_upsert_by_volume_number(self):
        '卷末压缩重跑过就该换掉旧梗概，而不是攒出两份第 1 卷。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  70           RESUME                   0
        # |  72           LOAD_GLOBAL              1 (state_with + NULL)
        # |               LOAD_GLOBAL              3 (range + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_SMALL_INT          19
        # |               CALL                     2
        # |               CALL                     1
        # |               STORE_FAST               1 (s)
        # |  73           LOAD_GLOBAL              5 (apply_volume_summary + NULL)
        # |               LOAD_FAST_BORROW         1 (s)
        # |               LOAD_GLOBAL              6 (VOL1)
        # |               CALL                     2
        # |               STORE_FAST               1 (s)
        # |  74           LOAD_GLOBAL              5 (apply_volume_summary + NULL)
        # |               LOAD_FAST_BORROW         1 (s)
        # |               LOAD_GLOBAL              6 (VOL1)
        # |               LOAD_ATTR                9 (model_copy + NULL|self)
        # |               LOAD_CONST               1 ('summary')
        # |               LOAD_CONST               2 ('改过的')
        # |               BUILD_MAP                1
        # |               LOAD_CONST               3 (('update',))
        # |               CALL_KW                  1
        # |               CALL                     2
        # |               STORE_FAST               1 (s)
        # |  75           LOAD_FAST_BORROW         1 (s)
        # |               LOAD_ATTR               10 (volume_summaries)
        # |               STORE_FAST               2 (@py_assert2)
        # |               LOAD_GLOBAL             13 (len + NULL)
        # |               LOAD_FAST_BORROW         2 (@py_assert2)
        # |               CALL                     1
        # |               STORE_FAST               3 (@py_assert4)
        # |               LOAD_SMALL_INT           1
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert7, @py_assert4)
        # |               LOAD_FAST_BORROW         4 (@py_assert7)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       307 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               16 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert6)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s.volume_summaries\n})\n} == %(py8)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert4, @py_assert7)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST               5 ('len')
        # |               LOAD_GLOBAL             18 (@py_builtins)
        # |               LOAD_ATTR               20 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               22 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             12 (len)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             12 (len)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('len')
        # |       L3:     LOAD_CONST               6 ('py1')
        # |               LOAD_CONST               7 ('s')
        # |               LOAD_GLOBAL             18 (@py_builtins)
        # |               LOAD_ATTR               20 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               22 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (s)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (s)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               7 ('s')
        # |       L6:     LOAD_CONST               8 ('py3')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py5')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py8')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert7)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format9)
        # |               LOAD_CONST              11 ('assert %(py10)s')
        # |               LOAD_CONST              12 ('py10')
        # |               LOAD_FAST_BORROW         6 (@py_format9)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format11)
        # |               LOAD_GLOBAL             27 (AssertionError + NULL)
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               28 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format11)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert6, @py_assert7)
        # |  76           LOAD_FAST_BORROW         1 (s)
        # |               LOAD_ATTR               10 (volume_summaries)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert0, @py_assert0)
        # |               LOAD_ATTR               30 (summary)
        # |               STORE_FAST               2 (@py_assert2)
        # |               LOAD_CONST               2 ('改过的')
        # |               STORE_FAST_LOAD_FAST   146 (@py_assert5, @py_assert2)
        # |               LOAD_FAST_BORROW         9 (@py_assert5)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               16 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW         3 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py3)s\n{%(py3)s = %(py1)s.summary\n} == %(py6)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 41 (@py_assert2, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               6 ('py1')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py3')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST              14 ('py6')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format7)
        # |               LOAD_CONST              15 ('assert %(py8)s')
        # |               LOAD_CONST              10 ('py8')
        # |               LOAD_FAST_BORROW        10 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format9)
        # |               LOAD_GLOBAL             27 (AssertionError + NULL)
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               28 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   57 (@py_assert4, @py_assert5)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE

    def test_cannot_compress_unwritten_chapters(self):
        '还没写出来'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   78           RESUME                   0
        # |   79           LOAD_GLOBAL              1 (state_with + NULL)
        # |                LOAD_GLOBAL              3 (range + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_SMALL_INT           6
        # |                CALL                     2
        # |                CALL                     1
        # |                STORE_FAST               1 (s)
        # |   80           LOAD_GLOBAL              4 (pytest)
        # |                LOAD_ATTR                6 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (PatchError)
        # |                LOAD_CONST               1 ('还没写出来')
        # |                LOAD_CONST               2 (('match',))
        # |                CALL_KW                  2
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |   81           LOAD_GLOBAL             11 (apply_volume_summary + NULL)
        # |                LOAD_FAST_BORROW         1 (s)
        # |                LOAD_GLOBAL             12 (VOL1)
        # |                CALL                     2
        # |                POP_TOP
        # |   80   L2:     LOAD_CONST               3 (None)
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

    def test_patch_can_carry_one(self):
        '卷末'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   83           RESUME                   0
        # |   84           LOAD_GLOBAL              1 (state_with + NULL)
        # |                LOAD_GLOBAL              3 (range + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_SMALL_INT          18
        # |                CALL                     2
        # |                CALL                     1
        # |                STORE_FAST               1 (s)
        # |   85           LOAD_GLOBAL              5 (StatePatch + NULL)
        # |   86           LOAD_GLOBAL              7 (ChapterSummary + NULL)
        # |                LOAD_SMALL_INT          18
        # |                LOAD_CONST               1 ('卷末')
        # |                LOAD_CONST               2 ('s')
        # |   87           LOAD_CONST               3 ('大学')
        # |                LOAD_CONST               4 (3000)
        # |   86           LOAD_CONST               5 (('ch', 'title', 'summary', 'stage', 'word_count'))
        # |                CALL_KW                  5
        # |   88           LOAD_GLOBAL              8 (VOL1)
        # |   85           LOAD_CONST               6 (('chapter_summary', 'volume_summary'))
        # |                CALL_KW                  2
        # |                STORE_FAST               2 (patch)
        # |   89           LOAD_GLOBAL             11 (apply_patch + NULL)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (s, patch)
        # |                CALL                     2
        # |                STORE_FAST               3 (after)
        # |   90           LOAD_FAST_BORROW         3 (after)
        # |                LOAD_ATTR               12 (volume_summaries)
        # |                GET_ITER
        # |                LOAD_FAST_AND_CLEAR      4 (v)
        # |                SWAP                     2
        # |        L1:     BUILD_LIST               0
        # |                SWAP                     2
        # |        L2:     FOR_ITER                14 (to L3)
        # |                STORE_FAST_LOAD_FAST    68 (v, v)
        # |                LOAD_ATTR               14 (volume)
        # |                LIST_APPEND              2
        # |                JUMP_BACKWARD           16 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |        L4:     STORE_FAST               5 (@py_assert0)
        # |                STORE_FAST               4 (v)
        # |                LOAD_SMALL_INT           1
        # |                BUILD_LIST               1
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              12 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              13 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               7 ('py1')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py4')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format5)
        # |                LOAD_CONST               9 ('assert %(py6)s')
        # |                LOAD_CONST              10 ('py6')
        # |                LOAD_FAST_BORROW         8 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format7)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L5:     LOAD_CONST              11 (None)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  118 (@py_assert2, @py_assert3)
        # |                LOAD_CONST              11 (None)
        # |                RETURN_VALUE
        # |   --   L6:     SWAP                     2
        # |                POP_TOP
        # |   90           SWAP                     2
        # |                STORE_FAST               4 (v)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L6 [2]

    def test_source_state_untouched(self):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  92           RESUME                   0
        # |  93           LOAD_GLOBAL              1 (state_with + NULL)
        # |               LOAD_GLOBAL              3 (range + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_SMALL_INT          19
        # |               CALL                     2
        # |               CALL                     1
        # |               STORE_FAST               1 (s)
        # |  94           LOAD_FAST_BORROW         1 (s)
        # |               LOAD_ATTR                5 (model_copy + NULL|self)
        # |               LOAD_CONST               1 (True)
        # |               LOAD_CONST               2 (('deep',))
        # |               CALL_KW                  1
        # |               STORE_FAST               2 (before)
        # |  95           LOAD_GLOBAL              7 (apply_volume_summary + NULL)
        # |               LOAD_FAST_BORROW         1 (s)
        # |               LOAD_GLOBAL              8 (VOL1)
        # |               CALL                     2
        # |               POP_TOP
        # |  96           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (s, before)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       233 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('==',))
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py0)s == %(py2)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (s, before)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('s')
        # |               LOAD_GLOBAL             14 (@py_builtins)
        # |               LOAD_ATTR               16 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (s)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (s)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('s')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_CONST               6 ('before')
        # |               LOAD_GLOBAL             14 (@py_builtins)
        # |               LOAD_ATTR               16 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (before)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (before)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               6 ('before')
        # |       L6:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               4 (@py_format3)
        # |               LOAD_CONST               7 ('assert %(py4)s')
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_FAST_BORROW         4 (@py_format3)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST               9 (None)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE


class FakeClient:
    'FakeClient'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  99           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('FakeClient')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          99
    # |               STORE_NAME               3 (__firstlineno__)
    # | 100           LOAD_CONST               1 (<code object __init__ at 0x103b9b030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 100>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (__init__)
    # | 101           LOAD_CONST               2 (<code object parse at 0x103c26170, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 101>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (parse)
    # |               LOAD_CONST               3 (('parsed', 'seen'))
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x103b9b030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 100>:
    # | 100           RESUME                   0
    # |               LOAD_FAST_BORROW         1 (parsed)
    # |               LOAD_CONST               0 (None)
    # |               SWAP                     2
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               0 (parsed)
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               1 (seen)
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object parse at 0x103c26170, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 101>:
    # | 101           RESUME                   0
    # | 102           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (prompt, self)
    # |               STORE_ATTR               0 (seen)
    # | 103           LOAD_BUILD_CLASS
    # |               PUSH_NULL
    # |               LOAD_CONST               0 (<code object R at 0x103bbe5b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 103>)
    # |               MAKE_FUNCTION
    # |               LOAD_CONST               1 ('R')
    # |               CALL                     2
    # |               STORE_FAST               5 (R)
    # | 104           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                2 (parsed)
    # |               LOAD_FAST_BORROW         5 (R)
    # |               STORE_ATTR               1 (parsed)
    # | 105           LOAD_FAST_BORROW         5 (R)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               RETURN_VALUE
    # | Disassembly of <code object R at 0x103bbe5b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 103>:
    # | 103           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('FakeClient.parse.<locals>.R')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         103
    # |               STORE_NAME               3 (__firstlineno__)
    # |               LOAD_CONST               1 (())
    # |               STORE_NAME               4 (__static_attributes__)
    # |               LOAD_CONST               2 (None)
    # |               RETURN_VALUE

    def __init__(self, parsed):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # | 100           RESUME                   0
        # |               LOAD_FAST_BORROW         1 (parsed)
        # |               LOAD_CONST               0 (None)
        # |               SWAP                     2
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               0 (parsed)
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               1 (seen)
        # |               LOAD_CONST               0 (None)
        # |               RETURN_VALUE

    def parse(self, role, prompt, fmt, **kw):
        'R'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 101           RESUME                   0
        # | 102           LOAD_FAST_BORROW_LOAD_FAST_BORROW 32 (prompt, self)
        # |               STORE_ATTR               0 (seen)
        # | 103           LOAD_BUILD_CLASS
        # |               PUSH_NULL
        # |               LOAD_CONST               0 (<code object R at 0x103bbe5b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 103>)
        # |               MAKE_FUNCTION
        # |               LOAD_CONST               1 ('R')
        # |               CALL                     2
        # |               STORE_FAST               5 (R)
        # | 104           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                2 (parsed)
        # |               LOAD_FAST_BORROW         5 (R)
        # |               STORE_ATTR               1 (parsed)
        # | 105           LOAD_FAST_BORROW         5 (R)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               RETURN_VALUE
        # | Disassembly of <code object R at 0x103bbe5b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 103>:
        # | 103           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('FakeClient.parse.<locals>.R')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         103
        # |               STORE_NAME               3 (__firstlineno__)
        # |               LOAD_CONST               1 (())
        # |               STORE_NAME               4 (__static_attributes__)
        # |               LOAD_CONST               2 (None)
        # |               RETURN_VALUE

        class R:
            'FakeClient.parse.<locals>.R'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 103           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('FakeClient.parse.<locals>.R')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         103
            # |               STORE_NAME               3 (__firstlineno__)
            # |               LOAD_CONST               1 (())
            # |               STORE_NAME               4 (__static_attributes__)
            # |               LOAD_CONST               2 (None)
            # |               RETURN_VALUE



class TestCompressVolume:
    'TestCompressVolume'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 108           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestCompressVolume')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         108
    # |               STORE_NAME               3 (__firstlineno__)
    # | 109           LOAD_CONST               1 (<code object test_refuses_when_nothing_is_archived at 0x103a660d0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 109>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_refuses_when_nothing_is_archived)
    # | 114           LOAD_CONST               2 (<code object test_wrong_volume_is_caught at 0x7c2ad59680, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 114>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_wrong_volume_is_caught)
    # | 120           LOAD_CONST               3 (<code object test_chapter_range_comes_from_the_outline_not_the_model at 0x7c2ae3c700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 120>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_chapter_range_comes_from_the_outline_not_the_model)
    # | 126           LOAD_CONST               4 (<code object test_only_this_volume_goes_in at 0x7c2b1ff200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 126>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_only_this_volume_goes_in)
    # | 134           LOAD_CONST               5 (<code object test_bible_is_not_sent at 0x7c2ae3ca80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 134>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_bible_is_not_sent)
    # | 140           LOAD_CONST               6 (<code object test_chapter_archive_never_emits_a_volume_summary at 0x7c2ae4a400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 140>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_chapter_archive_never_emits_a_volume_summary)
    # |               LOAD_CONST               7 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_refuses_when_nothing_is_archived at 0x103a660d0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 109>:
    # |  109           RESUME                   0
    # |  110           LOAD_GLOBAL              1 (Archivist + NULL)
    # |                LOAD_GLOBAL              3 (FakeClient + NULL)
    # |                LOAD_GLOBAL              4 (VOL1)
    # |                CALL                     1
    # |                CALL                     1
    # |                STORE_FAST               1 (a)
    # |  111           LOAD_GLOBAL              6 (pytest)
    # |                LOAD_ATTR                8 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (ValueError)
    # |                LOAD_CONST               0 ('没有任何章节摘要')
    # |                LOAD_CONST               1 (('match',))
    # |                CALL_KW                  2
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |  112           LOAD_FAST_BORROW         1 (a)
    # |                LOAD_ATTR               13 (compress_volume + NULL|self)
    # |                LOAD_GLOBAL             15 (state_with + NULL)
    # |                BUILD_LIST               0
    # |                CALL                     1
    # |                LOAD_GLOBAL             17 (make_volume + NULL)
    # |                CALL                     0
    # |                CALL                     2
    # |                POP_TOP
    # |  111   L2:     LOAD_CONST               2 (None)
    # |                LOAD_CONST               2 (None)
    # |                LOAD_CONST               2 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |                LOAD_CONST               2 (None)
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
    # |                LOAD_CONST               2 (None)
    # |                RETURN_VALUE
    # |   --   L6:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L3 [2] lasti
    # |   L3 to L5 -> L6 [4] lasti
    # | Disassembly of <code object test_wrong_volume_is_caught at 0x7c2ad59680, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 114>:
    # |  114           RESUME                   0
    # |  116           LOAD_GLOBAL              1 (Archivist + NULL)
    # |                LOAD_GLOBAL              3 (FakeClient + NULL)
    # |                LOAD_GLOBAL              4 (VOL1)
    # |                LOAD_ATTR                7 (model_copy + NULL|self)
    # |                LOAD_CONST               1 ('volume')
    # |                LOAD_SMALL_INT           7
    # |                BUILD_MAP                1
    # |                LOAD_CONST               2 (('update',))
    # |                CALL_KW                  1
    # |                CALL                     1
    # |                CALL                     1
    # |                STORE_FAST               1 (a)
    # |  117           LOAD_GLOBAL              8 (pytest)
    # |                LOAD_ATTR               10 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             12 (ValueError)
    # |                LOAD_CONST               3 ('第 7 卷')
    # |                LOAD_CONST               4 (('match',))
    # |                CALL_KW                  2
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |  118           LOAD_FAST_BORROW         1 (a)
    # |                LOAD_ATTR               15 (compress_volume + NULL|self)
    # |                LOAD_GLOBAL             17 (state_with + NULL)
    # |                LOAD_GLOBAL             19 (range + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_SMALL_INT          19
    # |                CALL                     2
    # |                CALL                     1
    # |                LOAD_GLOBAL             21 (make_volume + NULL)
    # |                CALL                     0
    # |                CALL                     2
    # |                POP_TOP
    # |  117   L2:     LOAD_CONST               5 (None)
    # |                LOAD_CONST               5 (None)
    # |                LOAD_CONST               5 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |                LOAD_CONST               5 (None)
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
    # |                LOAD_CONST               5 (None)
    # |                RETURN_VALUE
    # |   --   L6:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L3 [2] lasti
    # |   L3 to L5 -> L6 [4] lasti
    # | Disassembly of <code object test_chapter_range_comes_from_the_outline_not_the_model at 0x7c2ae3c700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 120>:
    # | 120           RESUME                   0
    # | 122           LOAD_GLOBAL              1 (Archivist + NULL)
    # |               LOAD_GLOBAL              3 (FakeClient + NULL)
    # |               LOAD_GLOBAL              4 (VOL1)
    # |               LOAD_ATTR                7 (model_copy + NULL|self)
    # |               LOAD_CONST               1 ('ch_start')
    # |               LOAD_SMALL_INT           3
    # |               LOAD_CONST               2 ('ch_end')
    # |               LOAD_SMALL_INT          99
    # |               BUILD_MAP                2
    # |               LOAD_CONST               3 (('update',))
    # |               CALL_KW                  1
    # |               CALL                     1
    # |               CALL                     1
    # |               STORE_FAST               1 (a)
    # | 123           LOAD_FAST_BORROW         1 (a)
    # |               LOAD_ATTR                9 (compress_volume + NULL|self)
    # |               LOAD_GLOBAL             11 (state_with + NULL)
    # |               LOAD_GLOBAL             13 (range + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_SMALL_INT          13
    # |               CALL                     2
    # |               CALL                     1
    # |               LOAD_GLOBAL             15 (make_volume + NULL)
    # |               CALL                     0
    # |               CALL                     2
    # |               STORE_FAST               2 (got)
    # | 124           LOAD_FAST_BORROW         2 (got)
    # |               LOAD_ATTR               16 (ch_start)
    # |               LOAD_FAST_BORROW         2 (got)
    # |               LOAD_ATTR               18 (ch_end)
    # |               BUILD_TUPLE              2
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_CONST              10 ((1, 12))
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       148 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               22 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py1')
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               26 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST               6 ('只写到第 12 章就只能覆盖到 12')
    # |               CALL                     1
    # |               LOAD_CONST               7 ('\n>assert %(py6)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               8 ('py6')
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format7)
    # |               LOAD_GLOBAL             29 (AssertionError + NULL)
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               30 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_only_this_volume_goes_in at 0x7c2b1ff200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 126>:
    # | 126           RESUME                   0
    # | 127           LOAD_GLOBAL              1 (FakeClient + NULL)
    # |               LOAD_GLOBAL              2 (VOL1)
    # |               CALL                     1
    # |               STORE_FAST               1 (client)
    # | 128           LOAD_GLOBAL              5 (state_with + NULL)
    # |               LOAD_GLOBAL              7 (range + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_SMALL_INT          25
    # |               CALL                     2
    # |               CALL                     1
    # |               STORE_FAST               2 (s)
    # | 129           LOAD_GLOBAL              9 (Archivist + NULL)
    # |               LOAD_FAST_BORROW         1 (client)
    # |               CALL                     1
    # |               LOAD_ATTR               11 (compress_volume + NULL|self)
    # |               LOAD_FAST_BORROW         2 (s)
    # |               LOAD_GLOBAL             13 (make_volume + NULL)
    # |               CALL                     0
    # |               CALL                     2
    # |               POP_TOP
    # | 130           LOAD_FAST_BORROW         1 (client)
    # |               LOAD_ATTR               14 (seen)
    # |               LOAD_ATTR               16 (instruction)
    # |               STORE_FAST               3 (body)
    # | 131           LOAD_CONST               1 ('第 18 章')
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert0, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (body)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               20 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('in',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py1)s in %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (@py_assert0, body)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_CONST               4 ('body')
    # |               LOAD_GLOBAL             24 (@py_builtins)
    # |               LOAD_ATTR               26 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               28 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (body)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (body)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('body')
    # |       L3:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format4)
    # |               LOAD_CONST               5 ('assert %(py5)s')
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_FAST_BORROW         6 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format6)
    # |               LOAD_GLOBAL             31 (AssertionError + NULL)
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               32 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert0, @py_assert2)
    # | 132           LOAD_CONST               8 ('第 19 章')
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert0, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (body)
    # |               CONTAINS_OP              1 (not in)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       204 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               20 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (('not in',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              14 (('%(py1)s not in %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (@py_assert0, body)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_CONST               4 ('body')
    # |               LOAD_GLOBAL             24 (@py_builtins)
    # |               LOAD_ATTR               26 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               28 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (body)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (body)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               4 ('body')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format4)
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               34 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 ('下一卷的章节不该混进这一卷的梗概')
    # |               CALL                     1
    # |               LOAD_CONST              10 ('\n>assert %(py5)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_FAST_BORROW         6 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format6)
    # |               LOAD_GLOBAL             31 (AssertionError + NULL)
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               32 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert0, @py_assert2)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_bible_is_not_sent at 0x7c2ae3ca80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 134>:
    # | 134           RESUME                   0
    # | 136           LOAD_GLOBAL              1 (FakeClient + NULL)
    # |               LOAD_GLOBAL              2 (VOL1)
    # |               CALL                     1
    # |               STORE_FAST               1 (client)
    # | 137           LOAD_GLOBAL              5 (Archivist + NULL)
    # |               LOAD_FAST_BORROW         1 (client)
    # |               CALL                     1
    # |               LOAD_ATTR                7 (compress_volume + NULL|self)
    # |               LOAD_GLOBAL              9 (state_with + NULL)
    # |               LOAD_GLOBAL             11 (range + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_SMALL_INT          19
    # |               CALL                     2
    # |               CALL                     1
    # |               LOAD_GLOBAL             13 (make_volume + NULL)
    # |               CALL                     0
    # |               CALL                     2
    # |               POP_TOP
    # | 138           LOAD_FAST_BORROW         1 (client)
    # |               LOAD_ATTR               14 (seen)
    # |               STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
    # |               LOAD_ATTR               16 (bible)
    # |               STORE_FAST               3 (@py_assert3)
    # |               LOAD_CONST               1 ('')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       221 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               20 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.seen\n}.bible\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('client')
    # |               LOAD_GLOBAL             22 (@py_builtins)
    # |               LOAD_ATTR               24 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               26 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (client)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               28 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (client)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('client')
    # |       L3:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               28 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               28 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py7')
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               28 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_CONST               7 ('assert %(py9)s')
    # |               LOAD_CONST               8 ('py9')
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format10)
    # |               LOAD_GLOBAL             31 (AssertionError + NULL)
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               32 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert5, @py_assert6)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_chapter_archive_never_emits_a_volume_summary at 0x7c2ae4a400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_volume_summary.py", line 140>:
    # | 140           RESUME                   0
    # | 142           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('ChapterOutline', 'SceneSpec'))
    # |               IMPORT_NAME              0 (novel_agent.agents.schemas)
    # |               IMPORT_FROM              1 (ChapterOutline)
    # |               STORE_FAST               1 (ChapterOutline)
    # |               IMPORT_FROM              2 (SceneSpec)
    # |               STORE_FAST               2 (SceneSpec)
    # |               POP_TOP
    # | 144           LOAD_GLOBAL              7 (StatePatch + NULL)
    # | 145           LOAD_GLOBAL              9 (ChapterSummary + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               2 ('t')
    # |               LOAD_CONST               3 ('s')
    # | 146           LOAD_CONST               4 ('大学')
    # |               LOAD_CONST               5 (3000)
    # | 145           LOAD_CONST               6 (('ch', 'title', 'summary', 'stage', 'word_count'))
    # |               CALL_KW                  5
    # | 147           LOAD_GLOBAL             10 (VOL1)
    # | 144           LOAD_CONST               7 (('chapter_summary', 'volume_summary'))
    # |               CALL_KW                  2
    # |               STORE_FAST               3 (patch)
    # | 148           LOAD_GLOBAL             13 (FakeClient + NULL)
    # |               LOAD_FAST_BORROW         3 (patch)
    # |               CALL                     1
    # |               STORE_FAST               4 (client)
    # | 149           LOAD_FAST_BORROW         1 (ChapterOutline)
    # |               PUSH_NULL
    # | 150           LOAD_SMALL_INT           1
    # |               LOAD_CONST               2 ('t')
    # |               LOAD_CONST               4 ('大学')
    # |               LOAD_CONST               8 ('i')
    # |               LOAD_CONST               9 ('h')
    # | 151           LOAD_FAST_BORROW         2 (SceneSpec)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 ('ch001_s1')
    # |               LOAD_CONST              11 ('w')
    # |               LOAD_CONST              11 ('w')
    # |               LOAD_CONST              12 ('shen')
    # |               BUILD_LIST               1
    # | 152           LOAD_CONST              13 ('g')
    # |               LOAD_CONST              14 ('a')
    # |               LOAD_CONST              15 ('b')
    # | 153           LOAD_CONST              16 ('x')
    # |               LOAD_CONST              17 (1000)
    # | 151           LOAD_CONST              18 (('id', 'where', 'when', 'present', 'goal', 'entry_emotion', 'exit_emotion', 'beat_type', 'target_words'))
    # |               CALL_KW                  9
    # | 154           LOAD_FAST_BORROW         2 (SceneSpec)
    # |               PUSH_NULL
    # |               LOAD_CONST              19 ('ch001_s2')
    # |               LOAD_CONST              11 ('w')
    # |               LOAD_CONST              11 ('w')
    # |               LOAD_CONST              12 ('shen')
    # |               BUILD_LIST               1
    # | 155           LOAD_CONST              13 ('g')
    # |               LOAD_CONST              14 ('a')
    # |               LOAD_CONST              15 ('b')
    # | 156           LOAD_CONST              16 ('x')
    # |               LOAD_CONST              17 (1000)
    # | 154           LOAD_CONST              18 (('id', 'where', 'when', 'present', 'goal', 'entry_emotion', 'exit_emotion', 'beat_type', 'target_words'))
    # |               CALL_KW                  9
    # | 151           BUILD_LIST               2
    # | 149           LOAD_CONST              20 (('ch', 'title', 'stage', 'intent', 'hook', 'scenes'))
    # |               CALL_KW                  6
    # |               STORE_FAST               5 (outline)
    # | 157           LOAD_GLOBAL             15 (Archivist + NULL)
    # |               LOAD_FAST_BORROW         4 (client)
    # |               CALL                     1
    # |               LOAD_ATTR               17 (archive + NULL|self)
    # |               LOAD_GLOBAL             19 (state_with + NULL)
    # |               BUILD_LIST               0
    # |               CALL                     1
    # |               LOAD_FAST_BORROW         5 (outline)
    # |               LOAD_CONST              21 ('正文')
    # |               CALL                     3
    # |               STORE_FAST               6 (got)
    # | 158           LOAD_FAST_BORROW         6 (got)
    # |               LOAD_ATTR               20 (volume_summary)
    # |               STORE_FAST               7 (@py_assert1)
    # |               LOAD_CONST              22 (None)
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         8 (@py_assert4)
    # |               IS_OP                    0 (is)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             22 (@pytest_ar)
    # |               LOAD_ATTR               24 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              29 (('is',))
    # |               LOAD_FAST_BORROW         9 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              30 (('%(py2)s\n{%(py2)s = %(py0)s.volume_summary\n} is %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              23 ('py0')
    # |               LOAD_CONST              24 ('got')
    # |               LOAD_GLOBAL             26 (@py_builtins)
    # |               LOAD_ATTR               28 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             22 (@pytest_ar)
    # |               LOAD_ATTR               30 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (got)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             22 (@pytest_ar)
    # |               LOAD_ATTR               32 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (got)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST              24 ('got')
    # |       L3:     LOAD_CONST              25 ('py2')
    # |               LOAD_GLOBAL             22 (@pytest_ar)
    # |               LOAD_ATTR               32 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              26 ('py5')
    # |               LOAD_GLOBAL             22 (@pytest_ar)
    # |               LOAD_ATTR               32 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format6)
    # |               LOAD_CONST              27 ('assert %(py7)s')
    # |               LOAD_CONST              28 ('py7')
    # |               LOAD_FAST_BORROW        10 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format8)
    # |               LOAD_GLOBAL             35 (AssertionError + NULL)
    # |               LOAD_GLOBAL             22 (@pytest_ar)
    # |               LOAD_ATTR               36 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              22 (None)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  152 (@py_assert3, @py_assert4)
    # |               LOAD_CONST              22 (None)
    # |               RETURN_VALUE

    def test_refuses_when_nothing_is_archived(self):
        '没有任何章节摘要'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  109           RESUME                   0
        # |  110           LOAD_GLOBAL              1 (Archivist + NULL)
        # |                LOAD_GLOBAL              3 (FakeClient + NULL)
        # |                LOAD_GLOBAL              4 (VOL1)
        # |                CALL                     1
        # |                CALL                     1
        # |                STORE_FAST               1 (a)
        # |  111           LOAD_GLOBAL              6 (pytest)
        # |                LOAD_ATTR                8 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (ValueError)
        # |                LOAD_CONST               0 ('没有任何章节摘要')
        # |                LOAD_CONST               1 (('match',))
        # |                CALL_KW                  2
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |  112           LOAD_FAST_BORROW         1 (a)
        # |                LOAD_ATTR               13 (compress_volume + NULL|self)
        # |                LOAD_GLOBAL             15 (state_with + NULL)
        # |                BUILD_LIST               0
        # |                CALL                     1
        # |                LOAD_GLOBAL             17 (make_volume + NULL)
        # |                CALL                     0
        # |                CALL                     2
        # |                POP_TOP
        # |  111   L2:     LOAD_CONST               2 (None)
        # |                LOAD_CONST               2 (None)
        # |                LOAD_CONST               2 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |                LOAD_CONST               2 (None)
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
        # |                LOAD_CONST               2 (None)
        # |                RETURN_VALUE
        # |   --   L6:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L3 [2] lasti
        # |   L3 to L5 -> L6 [4] lasti

    def test_wrong_volume_is_caught(self):
        '与逐章归档同一类事故：归档/压缩错了对象。卷号最容易机械判定。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  114           RESUME                   0
        # |  116           LOAD_GLOBAL              1 (Archivist + NULL)
        # |                LOAD_GLOBAL              3 (FakeClient + NULL)
        # |                LOAD_GLOBAL              4 (VOL1)
        # |                LOAD_ATTR                7 (model_copy + NULL|self)
        # |                LOAD_CONST               1 ('volume')
        # |                LOAD_SMALL_INT           7
        # |                BUILD_MAP                1
        # |                LOAD_CONST               2 (('update',))
        # |                CALL_KW                  1
        # |                CALL                     1
        # |                CALL                     1
        # |                STORE_FAST               1 (a)
        # |  117           LOAD_GLOBAL              8 (pytest)
        # |                LOAD_ATTR               10 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             12 (ValueError)
        # |                LOAD_CONST               3 ('第 7 卷')
        # |                LOAD_CONST               4 (('match',))
        # |                CALL_KW                  2
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |  118           LOAD_FAST_BORROW         1 (a)
        # |                LOAD_ATTR               15 (compress_volume + NULL|self)
        # |                LOAD_GLOBAL             17 (state_with + NULL)
        # |                LOAD_GLOBAL             19 (range + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_SMALL_INT          19
        # |                CALL                     2
        # |                CALL                     1
        # |                LOAD_GLOBAL             21 (make_volume + NULL)
        # |                CALL                     0
        # |                CALL                     2
        # |                POP_TOP
        # |  117   L2:     LOAD_CONST               5 (None)
        # |                LOAD_CONST               5 (None)
        # |                LOAD_CONST               5 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |                LOAD_CONST               5 (None)
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
        # |                LOAD_CONST               5 (None)
        # |                RETURN_VALUE
        # |   --   L6:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L3 [2] lasti
        # |   L3 to L5 -> L6 [4] lasti

    def test_chapter_range_comes_from_the_outline_not_the_model(self):
        '模型只负责写那段文字，章号范围由大纲和实际归档情况订正。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 120           RESUME                   0
        # | 122           LOAD_GLOBAL              1 (Archivist + NULL)
        # |               LOAD_GLOBAL              3 (FakeClient + NULL)
        # |               LOAD_GLOBAL              4 (VOL1)
        # |               LOAD_ATTR                7 (model_copy + NULL|self)
        # |               LOAD_CONST               1 ('ch_start')
        # |               LOAD_SMALL_INT           3
        # |               LOAD_CONST               2 ('ch_end')
        # |               LOAD_SMALL_INT          99
        # |               BUILD_MAP                2
        # |               LOAD_CONST               3 (('update',))
        # |               CALL_KW                  1
        # |               CALL                     1
        # |               CALL                     1
        # |               STORE_FAST               1 (a)
        # | 123           LOAD_FAST_BORROW         1 (a)
        # |               LOAD_ATTR                9 (compress_volume + NULL|self)
        # |               LOAD_GLOBAL             11 (state_with + NULL)
        # |               LOAD_GLOBAL             13 (range + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_SMALL_INT          13
        # |               CALL                     2
        # |               CALL                     1
        # |               LOAD_GLOBAL             15 (make_volume + NULL)
        # |               CALL                     0
        # |               CALL                     2
        # |               STORE_FAST               2 (got)
        # | 124           LOAD_FAST_BORROW         2 (got)
        # |               LOAD_ATTR               16 (ch_start)
        # |               LOAD_FAST_BORROW         2 (got)
        # |               LOAD_ATTR               18 (ch_end)
        # |               BUILD_TUPLE              2
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_CONST              10 ((1, 12))
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       148 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               22 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py1')
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               26 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST               6 ('只写到第 12 章就只能覆盖到 12')
        # |               CALL                     1
        # |               LOAD_CONST               7 ('\n>assert %(py6)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               8 ('py6')
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format7)
        # |               LOAD_GLOBAL             29 (AssertionError + NULL)
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               30 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_only_this_volume_goes_in(self):
        '第 18 章'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 126           RESUME                   0
        # | 127           LOAD_GLOBAL              1 (FakeClient + NULL)
        # |               LOAD_GLOBAL              2 (VOL1)
        # |               CALL                     1
        # |               STORE_FAST               1 (client)
        # | 128           LOAD_GLOBAL              5 (state_with + NULL)
        # |               LOAD_GLOBAL              7 (range + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_SMALL_INT          25
        # |               CALL                     2
        # |               CALL                     1
        # |               STORE_FAST               2 (s)
        # | 129           LOAD_GLOBAL              9 (Archivist + NULL)
        # |               LOAD_FAST_BORROW         1 (client)
        # |               CALL                     1
        # |               LOAD_ATTR               11 (compress_volume + NULL|self)
        # |               LOAD_FAST_BORROW         2 (s)
        # |               LOAD_GLOBAL             13 (make_volume + NULL)
        # |               CALL                     0
        # |               CALL                     2
        # |               POP_TOP
        # | 130           LOAD_FAST_BORROW         1 (client)
        # |               LOAD_ATTR               14 (seen)
        # |               LOAD_ATTR               16 (instruction)
        # |               STORE_FAST               3 (body)
        # | 131           LOAD_CONST               1 ('第 18 章')
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert0, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (body)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       177 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               20 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('in',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py1)s in %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (@py_assert0, body)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_CONST               4 ('body')
        # |               LOAD_GLOBAL             24 (@py_builtins)
        # |               LOAD_ATTR               26 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               28 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (body)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (body)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('body')
        # |       L3:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format4)
        # |               LOAD_CONST               5 ('assert %(py5)s')
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_FAST_BORROW         6 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format6)
        # |               LOAD_GLOBAL             31 (AssertionError + NULL)
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               32 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert0, @py_assert2)
        # | 132           LOAD_CONST               8 ('第 19 章')
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert0, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (body)
        # |               CONTAINS_OP              1 (not in)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       204 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               20 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (('not in',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              14 (('%(py1)s not in %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (@py_assert0, body)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_CONST               4 ('body')
        # |               LOAD_GLOBAL             24 (@py_builtins)
        # |               LOAD_ATTR               26 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               28 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (body)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (body)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               4 ('body')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format4)
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               34 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 ('下一卷的章节不该混进这一卷的梗概')
        # |               CALL                     1
        # |               LOAD_CONST              10 ('\n>assert %(py5)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_FAST_BORROW         6 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format6)
        # |               LOAD_GLOBAL             31 (AssertionError + NULL)
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               32 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert0, @py_assert2)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_bible_is_not_sent(self):
        '与逐章归档同样的理由：给了大块参考资料，模型会压错对象。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 134           RESUME                   0
        # | 136           LOAD_GLOBAL              1 (FakeClient + NULL)
        # |               LOAD_GLOBAL              2 (VOL1)
        # |               CALL                     1
        # |               STORE_FAST               1 (client)
        # | 137           LOAD_GLOBAL              5 (Archivist + NULL)
        # |               LOAD_FAST_BORROW         1 (client)
        # |               CALL                     1
        # |               LOAD_ATTR                7 (compress_volume + NULL|self)
        # |               LOAD_GLOBAL              9 (state_with + NULL)
        # |               LOAD_GLOBAL             11 (range + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_SMALL_INT          19
        # |               CALL                     2
        # |               CALL                     1
        # |               LOAD_GLOBAL             13 (make_volume + NULL)
        # |               CALL                     0
        # |               CALL                     2
        # |               POP_TOP
        # | 138           LOAD_FAST_BORROW         1 (client)
        # |               LOAD_ATTR               14 (seen)
        # |               STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
        # |               LOAD_ATTR               16 (bible)
        # |               STORE_FAST               3 (@py_assert3)
        # |               LOAD_CONST               1 ('')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       221 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               20 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.seen\n}.bible\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('client')
        # |               LOAD_GLOBAL             22 (@py_builtins)
        # |               LOAD_ATTR               24 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               26 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (client)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               28 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (client)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('client')
        # |       L3:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               28 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               28 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py7')
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               28 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_CONST               7 ('assert %(py9)s')
        # |               LOAD_CONST               8 ('py9')
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format10)
        # |               LOAD_GLOBAL             31 (AssertionError + NULL)
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               32 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert5, @py_assert6)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_chapter_archive_never_emits_a_volume_summary(self):
        '逐章归档时模型顺手填的卷梗概要丢掉 —— 压缩是卷末的独立动作。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 140           RESUME                   0
        # | 142           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('ChapterOutline', 'SceneSpec'))
        # |               IMPORT_NAME              0 (novel_agent.agents.schemas)
        # |               IMPORT_FROM              1 (ChapterOutline)
        # |               STORE_FAST               1 (ChapterOutline)
        # |               IMPORT_FROM              2 (SceneSpec)
        # |               STORE_FAST               2 (SceneSpec)
        # |               POP_TOP
        # | 144           LOAD_GLOBAL              7 (StatePatch + NULL)
        # | 145           LOAD_GLOBAL              9 (ChapterSummary + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               2 ('t')
        # |               LOAD_CONST               3 ('s')
        # | 146           LOAD_CONST               4 ('大学')
        # |               LOAD_CONST               5 (3000)
        # | 145           LOAD_CONST               6 (('ch', 'title', 'summary', 'stage', 'word_count'))
        # |               CALL_KW                  5
        # | 147           LOAD_GLOBAL             10 (VOL1)
        # | 144           LOAD_CONST               7 (('chapter_summary', 'volume_summary'))
        # |               CALL_KW                  2
        # |               STORE_FAST               3 (patch)
        # | 148           LOAD_GLOBAL             13 (FakeClient + NULL)
        # |               LOAD_FAST_BORROW         3 (patch)
        # |               CALL                     1
        # |               STORE_FAST               4 (client)
        # | 149           LOAD_FAST_BORROW         1 (ChapterOutline)
        # |               PUSH_NULL
        # | 150           LOAD_SMALL_INT           1
        # |               LOAD_CONST               2 ('t')
        # |               LOAD_CONST               4 ('大学')
        # |               LOAD_CONST               8 ('i')
        # |               LOAD_CONST               9 ('h')
        # | 151           LOAD_FAST_BORROW         2 (SceneSpec)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 ('ch001_s1')
        # |               LOAD_CONST              11 ('w')
        # |               LOAD_CONST              11 ('w')
        # |               LOAD_CONST              12 ('shen')
        # |               BUILD_LIST               1
        # | 152           LOAD_CONST              13 ('g')
        # |               LOAD_CONST              14 ('a')
        # |               LOAD_CONST              15 ('b')
        # | 153           LOAD_CONST              16 ('x')
        # |               LOAD_CONST              17 (1000)
        # | 151           LOAD_CONST              18 (('id', 'where', 'when', 'present', 'goal', 'entry_emotion', 'exit_emotion', 'beat_type', 'target_words'))
        # |               CALL_KW                  9
        # | 154           LOAD_FAST_BORROW         2 (SceneSpec)
        # |               PUSH_NULL
        # |               LOAD_CONST              19 ('ch001_s2')
        # |               LOAD_CONST              11 ('w')
        # |               LOAD_CONST              11 ('w')
        # |               LOAD_CONST              12 ('shen')
        # |               BUILD_LIST               1
        # | 155           LOAD_CONST              13 ('g')
        # |               LOAD_CONST              14 ('a')
        # |               LOAD_CONST              15 ('b')
        # | 156           LOAD_CONST              16 ('x')
        # |               LOAD_CONST              17 (1000)
        # | 154           LOAD_CONST              18 (('id', 'where', 'when', 'present', 'goal', 'entry_emotion', 'exit_emotion', 'beat_type', 'target_words'))
        # |               CALL_KW                  9
        # | 151           BUILD_LIST               2
        # | 149           LOAD_CONST              20 (('ch', 'title', 'stage', 'intent', 'hook', 'scenes'))
        # |               CALL_KW                  6
        # |               STORE_FAST               5 (outline)
        # | 157           LOAD_GLOBAL             15 (Archivist + NULL)
        # |               LOAD_FAST_BORROW         4 (client)
        # |               CALL                     1
        # |               LOAD_ATTR               17 (archive + NULL|self)
        # |               LOAD_GLOBAL             19 (state_with + NULL)
        # |               BUILD_LIST               0
        # |               CALL                     1
        # |               LOAD_FAST_BORROW         5 (outline)
        # |               LOAD_CONST              21 ('正文')
        # |               CALL                     3
        # |               STORE_FAST               6 (got)
        # | 158           LOAD_FAST_BORROW         6 (got)
        # |               LOAD_ATTR               20 (volume_summary)
        # |               STORE_FAST               7 (@py_assert1)
        # |               LOAD_CONST              22 (None)
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         8 (@py_assert4)
        # |               IS_OP                    0 (is)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             22 (@pytest_ar)
        # |               LOAD_ATTR               24 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              29 (('is',))
        # |               LOAD_FAST_BORROW         9 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              30 (('%(py2)s\n{%(py2)s = %(py0)s.volume_summary\n} is %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              23 ('py0')
        # |               LOAD_CONST              24 ('got')
        # |               LOAD_GLOBAL             26 (@py_builtins)
        # |               LOAD_ATTR               28 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             22 (@pytest_ar)
        # |               LOAD_ATTR               30 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (got)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             22 (@pytest_ar)
        # |               LOAD_ATTR               32 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (got)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST              24 ('got')
        # |       L3:     LOAD_CONST              25 ('py2')
        # |               LOAD_GLOBAL             22 (@pytest_ar)
        # |               LOAD_ATTR               32 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              26 ('py5')
        # |               LOAD_GLOBAL             22 (@pytest_ar)
        # |               LOAD_ATTR               32 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format6)
        # |               LOAD_CONST              27 ('assert %(py7)s')
        # |               LOAD_CONST              28 ('py7')
        # |               LOAD_FAST_BORROW        10 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format8)
        # |               LOAD_GLOBAL             35 (AssertionError + NULL)
        # |               LOAD_GLOBAL             22 (@pytest_ar)
        # |               LOAD_ATTR               36 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              22 (None)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  152 (@py_assert3, @py_assert4)
        # |               LOAD_CONST              22 (None)
        # |               RETURN_VALUE

