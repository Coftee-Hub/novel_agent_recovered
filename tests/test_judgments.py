# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py
# 来源   : test_judgments.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '评审记录落盘。\n\n方案里写着"judge 阈值 24/35 是拍脑袋的起始值，跑 10 章后按实际分布调"。\n可分数此前跑完就丢：跑了 5 次评审，run_log 里只有 token 和耗时 —— 到第 10 章\n手上仍然是零个数据点。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '评审记录落盘。\n\n方案里写着"judge 阈值 24/35 是拍脑袋的起始值，跑 10 章后按实际分布调"。\n可分数此前跑完就丢：跑了 5 次评审，run_log 里只有 token 和耗时 —— 到第 10 章\n手上仍然是零个数据点。\n',
    10: 'TestWhatGetsRecorded',
    12: 'TestRevisionRounds',
    14: 'TestItNeverBreaksTheRun',
    16: 'TestOnDiskFormat',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('TestWhatGetsRecorded', 0): 'TestWhatGetsRecorded',
    ('test_one_row_per_review', 1): 'py0',
    ('test_one_row_per_review', 2): 'len',
    ('test_one_row_per_review', 3): 'py1',
    ('test_one_row_per_review', 4): 'rows',
    ('test_one_row_per_review', 5): 'py3',
    ('test_one_row_per_review', 6): 'py6',
    ('test_one_row_per_review', 7): 'assert %(py8)s',
    ('test_one_row_per_review', 8): 'py8',
    ('test_seven_dimensions_with_the_total', 1): 'scores',
    ('test_seven_dimensions_with_the_total', 2): 'py0',
    ('test_seven_dimensions_with_the_total', 3): 'len',
    ('test_seven_dimensions_with_the_total', 4): 'py2',
    ('test_seven_dimensions_with_the_total', 5): 'py4',
    ('test_seven_dimensions_with_the_total', 6): 'py7',
    ('test_seven_dimensions_with_the_total', 7): 'assert %(py9)s',
    ('test_seven_dimensions_with_the_total', 8): 'py9',
    ('test_seven_dimensions_with_the_total', 10): 'total',
    ('test_seven_dimensions_with_the_total', 11): 'py1',
    ('test_seven_dimensions_with_the_total', 12): 'py3',
    ('test_seven_dimensions_with_the_total', 13): 'sum',
    ('test_seven_dimensions_with_the_total', 14): 'py5',
    ('test_seven_dimensions_with_the_total', 15): 'py11',
    ('test_seven_dimensions_with_the_total', 16): 'assert %(py13)s',
    ('test_seven_dimensions_with_the_total', 17): 'py13',
    ('test_seven_dimensions_with_the_total', 18): 'lowest',
    ('test_seven_dimensions_with_the_total', 19): 'min',
    ('test_thresholds_travel_with_the_row', 0): '阈值以后会改。不把当时的线记下来，旧数据就没法解读。',
    ('test_thresholds_travel_with_the_row', 1): 'thresholds',
    ('test_thresholds_travel_with_the_row', 2): 'per_dimension',
    ('test_thresholds_travel_with_the_row', 3): 'total',
    ('test_thresholds_travel_with_the_row', 4): 'py1',
    ('test_thresholds_travel_with_the_row', 5): 'py4',
    ('test_thresholds_travel_with_the_row', 6): 'assert %(py6)s',
    ('test_thresholds_travel_with_the_row', 7): 'py6',
    ('test_chapter_and_word_count', 1): 'ch',
    ('test_chapter_and_word_count', 2): 'py1',
    ('test_chapter_and_word_count', 3): 'py4',
    ('test_chapter_and_word_count', 4): 'assert %(py6)s',
    ('test_chapter_and_word_count', 5): 'py6',
    ('test_chapter_and_word_count', 7): 'word_count',
    ('test_failing_notes_name_their_scene', 1): 'notes',
    ('test_failing_notes_name_their_scene', 2): 'ch001_s2',
    ('test_failing_notes_name_their_scene', 3): 'py1',
    ('test_failing_notes_name_their_scene', 4): 'py4',
    ('test_failing_notes_name_their_scene', 5): 'assert %(py6)s',
    ('test_failing_notes_name_their_scene', 6): 'py6',
    ('test_failing_notes_name_their_scene', 8): 'passed',
    ('TestRevisionRounds', 0): 'TestRevisionRounds',
    ('TestRevisionRounds', 1): '修订到底有没有用 —— 同一章修订前后的分数变化，此前完全是黑箱。',
    ('test_each_round_is_recorded_separately', 0): 'revision',
    ('test_each_round_is_recorded_separately', 1): 'py1',
    ('test_each_round_is_recorded_separately', 2): 'py4',
    ('test_each_round_is_recorded_separately', 3): 'assert %(py6)s',
    ('test_each_round_is_recorded_separately', 4): 'py6',
    ('test_each_round_is_recorded_separately', 6): 'passed',
    ('test_gate_failures_do_not_produce_rows', 0): 'gate 不过就不评审，自然也没有分数可记。',
    ('test_gate_failures_do_not_produce_rows', 1): 'revision',
    ('test_gate_failures_do_not_produce_rows', 2): 'py1',
    ('test_gate_failures_do_not_produce_rows', 3): 'py4',
    ('test_gate_failures_do_not_produce_rows', 4): '只有修订后那次评审',
    ('test_gate_failures_do_not_produce_rows', 5): '\n>assert %(py6)s',
    ('test_gate_failures_do_not_produce_rows', 6): 'py6',
    ('TestItNeverBreaksTheRun', 0): 'TestItNeverBreaksTheRun',
    ('test_a_broken_sink_does_not_sink_the_chapter', 0): '记账失败不许拖垮一章 —— 与缝合、归档、卷末压缩同一条原则。',
    ('test_a_broken_sink_does_not_sink_the_chapter', 2): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_a_broken_sink_does_not_sink_the_chapter', 3): 'py0',
    ('test_a_broken_sink_does_not_sink_the_chapter', 4): 'r',
    ('test_a_broken_sink_does_not_sink_the_chapter', 5): 'py2',
    ('boom', 0): '磁盘满了',
    ('test_no_sink_is_fine', 1): 'py0',
    ('test_no_sink_is_fine', 2): 'p',
    ('test_no_sink_is_fine', 3): 'py2',
    ('test_no_sink_is_fine', 4): 'py5',
    ('test_no_sink_is_fine', 5): 'assert %(py7)s',
    ('test_no_sink_is_fine', 6): 'py7',
    ('test_no_sink_is_fine', 7): 'assert %(py12)s\n{%(py12)s = %(py10)s\n{%(py10)s = %(py2)s\n{%(py2)s = %(py0)s.run\n}(%(py3)s, %(py6)s\n{%(py6)s = %(py4)s()\n}, %(py8)s)\n}.passed\n}',
    ('test_no_sink_is_fine', 8): 'py3',
    ('test_no_sink_is_fine', 9): 'sample_state',
    ('test_no_sink_is_fine', 10): 'py4',
    ('test_no_sink_is_fine', 11): 'volume',
    ('test_no_sink_is_fine', 12): 'py6',
    ('test_no_sink_is_fine', 13): 'py8',
    ('test_no_sink_is_fine', 14): 'py10',
    ('test_no_sink_is_fine', 15): 'py12',
    ('TestOnDiskFormat', 0): 'TestOnDiskFormat',
    ('test_rows_are_one_json_object_per_line', 2): 'BOOK',
    ('test_rows_are_one_json_object_per_line', 3): 'ch',
    ('test_rows_are_one_json_object_per_line', 4): 'total',
    ('test_rows_are_one_json_object_per_line', 5): 'judgments.jsonl',
    ('test_rows_are_one_json_object_per_line', 6): 'utf-8',
    ('test_rows_are_one_json_object_per_line', 7): 'py1',
    ('test_rows_are_one_json_object_per_line', 8): 'py4',
    ('test_rows_are_one_json_object_per_line', 9): 'assert %(py6)s',
    ('test_rows_are_one_json_object_per_line', 10): 'py6',
    ('test_chinese_is_readable_not_escaped', 0): '这份文件是给人翻的，中文 那种转义没法读。',
    ('test_chinese_is_readable_not_escaped', 2): 'BOOK',
    ('test_chinese_is_readable_not_escaped', 3): 'note',
    ('test_chinese_is_readable_not_escaped', 4): '情绪推进',
    ('test_chinese_is_readable_not_escaped', 5): 'judgments.jsonl',
    ('test_chinese_is_readable_not_escaped', 6): 'utf-8',
    ('test_chinese_is_readable_not_escaped', 7): 'py1',
    ('test_chinese_is_readable_not_escaped', 8): 'py3',
    ('test_chinese_is_readable_not_escaped', 9): 'tmp_path',
    ('test_chinese_is_readable_not_escaped', 10): 'py5',
    ('test_chinese_is_readable_not_escaped', 11): 'py8',
    ('test_chinese_is_readable_not_escaped', 12): 'py10',
    ('test_chinese_is_readable_not_escaped', 13): 'py12',
    ('test_chinese_is_readable_not_escaped', 14): 'assert %(py14)s',
    ('test_chinese_is_readable_not_escaped', 15): 'py14',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def run(sample_state, stitches, verdicts, **kw):
    pass  # 无 docstring
    # ── 函数体（字节码重建见 BODY 段）──
    # |  23           RESUME                   0
    # |  24           BUILD_LIST               0
    # |               STORE_FAST               4 (rows)
    # |  25           LOAD_GLOBAL              1 (build + NULL)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (stitches, verdicts)
    # |               LOAD_FAST_BORROW         0 (sample_state)
    # |               BUILD_TUPLE              3
    # |               BUILD_MAP                0
    # |               LOAD_FAST_BORROW         3 (kw)
    # |               DICT_MERGE               1
    # |               CALL_FUNCTION_EX
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST_STORE_FAST   86 (p, w)
    # |               STORE_FAST               7 (a)
    # |  26           LOAD_FAST_BORROW         4 (rows)
    # |               LOAD_ATTR                2 (append)
    # |               LOAD_FAST_BORROW         5 (p)
    # |               STORE_ATTR               2 (judgment_sink)
    # |  27           LOAD_FAST_BORROW         5 (p)
    # |               LOAD_ATTR                7 (run + NULL|self)
    # |               LOAD_FAST_BORROW         0 (sample_state)
    # |               LOAD_GLOBAL              9 (volume + NULL)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           1
    # |               CALL                     3
    # |               POP_TOP
    # |  28           LOAD_FAST_BORROW         4 (rows)
    # |               RETURN_VALUE

class TestWhatGetsRecorded:
    'TestWhatGetsRecorded'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  31           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestWhatGetsRecorded')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          31
    # |               STORE_NAME               3 (__firstlineno__)
    # |  32           LOAD_CONST               1 (<code object test_one_row_per_review at 0x7ce72b0000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 32>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_one_row_per_review)
    # |  36           LOAD_CONST               2 (<code object test_seven_dimensions_with_the_total at 0x7ce6d74000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 36>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_seven_dimensions_with_the_total)
    # |  42           LOAD_CONST               3 (<code object test_thresholds_travel_with_the_row at 0x7ce7250f00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 42>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_thresholds_travel_with_the_row)
    # |  47           LOAD_CONST               4 (<code object test_chapter_and_word_count at 0x7ce72b0700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 47>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_chapter_and_word_count)
    # |  52           LOAD_CONST               5 (<code object test_failing_notes_name_their_scene at 0x7ce72b0a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 52>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_failing_notes_name_their_scene)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_one_row_per_review at 0x7ce72b0000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 32>:
    # |  32           RESUME                   0
    # |  33           LOAD_GLOBAL              1 (run + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               LOAD_GLOBAL              2 (GOOD)
    # |               BUILD_LIST               1
    # |               LOAD_GLOBAL              4 (PASS)
    # |               BUILD_LIST               1
    # |               CALL                     3
    # |               STORE_FAST               2 (rows)
    # |  34           LOAD_GLOBAL              7 (len + NULL)
    # |               LOAD_FAST_BORROW         2 (rows)
    # |               CALL                     1
    # |               STORE_FAST               3 (@py_assert2)
    # |               LOAD_SMALL_INT           1
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert5, @py_assert2)
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       285 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert2, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('len')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              6 (len)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              6 (len)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('len')
    # |       L3:     LOAD_CONST               3 ('py1')
    # |               LOAD_CONST               4 ('rows')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (rows)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (rows)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               4 ('rows')
    # |       L6:     LOAD_CONST               5 ('py3')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_CONST               7 ('assert %(py8)s')
    # |               LOAD_CONST               8 ('py8')
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format9)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert4, @py_assert5)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_seven_dimensions_with_the_total at 0x7ce6d74000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 36>:
    # |  36            RESUME                   0
    # |  37            LOAD_GLOBAL              1 (run + NULL)
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                LOAD_GLOBAL              2 (GOOD)
    # |                BUILD_LIST               1
    # |                LOAD_GLOBAL              4 (PASS)
    # |                BUILD_LIST               1
    # |                CALL                     3
    # |                LOAD_SMALL_INT           0
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               2 (row)
    # |  38            LOAD_FAST_BORROW         2 (row)
    # |                LOAD_CONST               1 ('scores')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                STORE_FAST               4 (@py_assert3)
    # |                LOAD_SMALL_INT           7
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert6, @py_assert3)
    # |                LOAD_FAST_BORROW         5 (@py_assert6)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       229 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              20 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              21 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert3, @py_assert6)
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
    # |        L3:     LOAD_CONST               4 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py4')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py7')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert6)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format8)
    # |                LOAD_CONST               7 ('assert %(py9)s')
    # |                LOAD_CONST               8 ('py9')
    # |                LOAD_FAST_BORROW         7 (@py_format8)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format10)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format10)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert5, @py_assert6)
    # |  39            LOAD_FAST_BORROW         2 (row)
    # |                LOAD_CONST              10 ('total')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST   146 (@py_assert0, row)
    # |                LOAD_CONST               1 ('scores')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert4, @py_assert4)
    # |                LOAD_ATTR               24 (values)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                STORE_FAST              11 (@py_assert8)
    # |                LOAD_GLOBAL             27 (sum + NULL)
    # |                LOAD_FAST_BORROW        11 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   201 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW        12 (@py_assert10)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   221 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       273 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              20 (('==',))
    # |                LOAD_FAST_BORROW        13 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              22 (('%(py1)s == %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = %(py5)s.values\n}()\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              11 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py3')
    # |                LOAD_CONST              13 ('sum')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             26 (sum)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             26 (sum)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST              13 ('sum')
    # |        L7:     LOAD_CONST              14 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py7')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py9')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py11')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                6
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format12)
    # |                LOAD_CONST              16 ('assert %(py13)s')
    # |                LOAD_CONST              17 ('py13')
    # |                LOAD_FAST_BORROW        14 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format14)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        15 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  188 (@py_assert8, @py_assert10)
    # |  40            LOAD_FAST_BORROW         2 (row)
    # |                LOAD_CONST              18 ('lowest')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST   146 (@py_assert0, row)
    # |                LOAD_CONST               1 ('scores')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert4, @py_assert4)
    # |                LOAD_ATTR               24 (values)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                STORE_FAST              11 (@py_assert8)
    # |                LOAD_GLOBAL             29 (min + NULL)
    # |                LOAD_FAST_BORROW        11 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   201 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW        12 (@py_assert10)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   221 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       273 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              20 (('==',))
    # |                LOAD_FAST_BORROW        13 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              22 (('%(py1)s == %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = %(py5)s.values\n}()\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              11 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py3')
    # |                LOAD_CONST              19 ('min')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             28 (min)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L10)
    # |                NOT_TAKEN
    # |        L9:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             28 (min)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L11)
    # |       L10:     LOAD_CONST              19 ('min')
    # |       L11:     LOAD_CONST              14 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py7')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py9')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py11')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                6
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format12)
    # |                LOAD_CONST              16 ('assert %(py13)s')
    # |                LOAD_CONST              17 ('py13')
    # |                LOAD_FAST_BORROW        14 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format14)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        15 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L12:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  188 (@py_assert8, @py_assert10)
    # |                LOAD_CONST               9 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_thresholds_travel_with_the_row at 0x7ce7250f00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 42>:
    # |  42           RESUME                   0
    # |  44           LOAD_GLOBAL              1 (run + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               LOAD_GLOBAL              2 (GOOD)
    # |               BUILD_LIST               1
    # |               LOAD_GLOBAL              4 (PASS)
    # |               BUILD_LIST               1
    # |               CALL                     3
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (row)
    # |  45           LOAD_FAST_BORROW         2 (row)
    # |               LOAD_CONST               1 ('thresholds')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_CONST               2 ('per_dimension')
    # |               LOAD_SMALL_INT           3
    # |               LOAD_CONST               3 ('total')
    # |               LOAD_SMALL_INT          24
    # |               BUILD_MAP                2
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              10 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_CONST               6 ('assert %(py6)s')
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_chapter_and_word_count at 0x7ce72b0700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 47>:
    # |  47           RESUME                   0
    # |  48           LOAD_GLOBAL              1 (run + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               LOAD_GLOBAL              2 (GOOD)
    # |               BUILD_LIST               1
    # |               LOAD_GLOBAL              4 (PASS)
    # |               BUILD_LIST               1
    # |               CALL                     3
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (row)
    # |  49           LOAD_FAST_BORROW         2 (row)
    # |               LOAD_CONST               1 ('ch')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_SMALL_INT           1
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               9 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_CONST               4 ('assert %(py6)s')
    # |               LOAD_CONST               5 ('py6')
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |  50           LOAD_FAST_BORROW         2 (row)
    # |               LOAD_CONST               7 ('word_count')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_SMALL_INT           0
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               COMPARE_OP             132 (>)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('>',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py1)s > %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_CONST               4 ('assert %(py6)s')
    # |               LOAD_CONST               5 ('py6')
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format7)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_failing_notes_name_their_scene at 0x7ce72b0a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 52>:
    # |  52           RESUME                   0
    # |  53           LOAD_GLOBAL              1 (run + NULL)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               LOAD_GLOBAL              2 (GOOD)
    # |               LOAD_GLOBAL              2 (GOOD)
    # |               BUILD_LIST               2
    # |               LOAD_GLOBAL              4 (FAIL)
    # |               LOAD_GLOBAL              6 (PASS)
    # |               BUILD_LIST               2
    # |               CALL                     3
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (row)
    # |  54           LOAD_FAST_BORROW         2 (row)
    # |               LOAD_CONST               1 ('notes')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_CONST               2 ('ch001_s2')
    # |               BUILD_LIST               1
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_CONST               5 ('assert %(py6)s')
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format7)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |  55           LOAD_FAST_BORROW         2 (row)
    # |               LOAD_CONST               8 ('passed')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_CONST               9 (False)
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               IS_OP                    0 (is)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 (('is',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py1)s is %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_CONST               5 ('assert %(py6)s')
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format7)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE

    def test_one_row_per_review(self, sample_state):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  32           RESUME                   0
        # |  33           LOAD_GLOBAL              1 (run + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               LOAD_GLOBAL              2 (GOOD)
        # |               BUILD_LIST               1
        # |               LOAD_GLOBAL              4 (PASS)
        # |               BUILD_LIST               1
        # |               CALL                     3
        # |               STORE_FAST               2 (rows)
        # |  34           LOAD_GLOBAL              7 (len + NULL)
        # |               LOAD_FAST_BORROW         2 (rows)
        # |               CALL                     1
        # |               STORE_FAST               3 (@py_assert2)
        # |               LOAD_SMALL_INT           1
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert5, @py_assert2)
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       285 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert2, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('len')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              6 (len)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              6 (len)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('len')
        # |       L3:     LOAD_CONST               3 ('py1')
        # |               LOAD_CONST               4 ('rows')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (rows)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (rows)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               4 ('rows')
        # |       L6:     LOAD_CONST               5 ('py3')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_CONST               7 ('assert %(py8)s')
        # |               LOAD_CONST               8 ('py8')
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format9)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert4, @py_assert5)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_seven_dimensions_with_the_total(self, sample_state):
        'scores'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  36            RESUME                   0
        # |  37            LOAD_GLOBAL              1 (run + NULL)
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                LOAD_GLOBAL              2 (GOOD)
        # |                BUILD_LIST               1
        # |                LOAD_GLOBAL              4 (PASS)
        # |                BUILD_LIST               1
        # |                CALL                     3
        # |                LOAD_SMALL_INT           0
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               2 (row)
        # |  38            LOAD_FAST_BORROW         2 (row)
        # |                LOAD_CONST               1 ('scores')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               3 (@py_assert1)
        # |                LOAD_GLOBAL              7 (len + NULL)
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                STORE_FAST               4 (@py_assert3)
        # |                LOAD_SMALL_INT           7
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert6, @py_assert3)
        # |                LOAD_FAST_BORROW         5 (@py_assert6)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       229 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              20 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              21 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert3, @py_assert6)
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
        # |        L3:     LOAD_CONST               4 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py4')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py7')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert6)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format8)
        # |                LOAD_CONST               7 ('assert %(py9)s')
        # |                LOAD_CONST               8 ('py9')
        # |                LOAD_FAST_BORROW         7 (@py_format8)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format10)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format10)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert5, @py_assert6)
        # |  39            LOAD_FAST_BORROW         2 (row)
        # |                LOAD_CONST              10 ('total')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST   146 (@py_assert0, row)
        # |                LOAD_CONST               1 ('scores')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert4, @py_assert4)
        # |                LOAD_ATTR               24 (values)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                STORE_FAST              11 (@py_assert8)
        # |                LOAD_GLOBAL             27 (sum + NULL)
        # |                LOAD_FAST_BORROW        11 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   201 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW        12 (@py_assert10)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   221 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       273 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              20 (('==',))
        # |                LOAD_FAST_BORROW        13 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              22 (('%(py1)s == %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = %(py5)s.values\n}()\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              11 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py3')
        # |                LOAD_CONST              13 ('sum')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             26 (sum)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             26 (sum)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST              13 ('sum')
        # |        L7:     LOAD_CONST              14 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py7')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py9')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py11')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                6
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format12)
        # |                LOAD_CONST              16 ('assert %(py13)s')
        # |                LOAD_CONST              17 ('py13')
        # |                LOAD_FAST_BORROW        14 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format14)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        15 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST              13 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  188 (@py_assert8, @py_assert10)
        # |  40            LOAD_FAST_BORROW         2 (row)
        # |                LOAD_CONST              18 ('lowest')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST   146 (@py_assert0, row)
        # |                LOAD_CONST               1 ('scores')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert4, @py_assert4)
        # |                LOAD_ATTR               24 (values)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                STORE_FAST              11 (@py_assert8)
        # |                LOAD_GLOBAL             29 (min + NULL)
        # |                LOAD_FAST_BORROW        11 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   201 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW        12 (@py_assert10)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   221 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       273 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              20 (('==',))
        # |                LOAD_FAST_BORROW        13 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              22 (('%(py1)s == %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = %(py5)s.values\n}()\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              11 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py3')
        # |                LOAD_CONST              19 ('min')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             28 (min)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L10)
        # |                NOT_TAKEN
        # |        L9:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             28 (min)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L11)
        # |       L10:     LOAD_CONST              19 ('min')
        # |       L11:     LOAD_CONST              14 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py7')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py9')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py11')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                6
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format12)
        # |                LOAD_CONST              16 ('assert %(py13)s')
        # |                LOAD_CONST              17 ('py13')
        # |                LOAD_FAST_BORROW        14 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format14)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        15 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L12:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST              13 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  188 (@py_assert8, @py_assert10)
        # |                LOAD_CONST               9 (None)
        # |                RETURN_VALUE

    def test_thresholds_travel_with_the_row(self, sample_state):
        '阈值以后会改。不把当时的线记下来，旧数据就没法解读。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  42           RESUME                   0
        # |  44           LOAD_GLOBAL              1 (run + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               LOAD_GLOBAL              2 (GOOD)
        # |               BUILD_LIST               1
        # |               LOAD_GLOBAL              4 (PASS)
        # |               BUILD_LIST               1
        # |               CALL                     3
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (row)
        # |  45           LOAD_FAST_BORROW         2 (row)
        # |               LOAD_CONST               1 ('thresholds')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_CONST               2 ('per_dimension')
        # |               LOAD_SMALL_INT           3
        # |               LOAD_CONST               3 ('total')
        # |               LOAD_SMALL_INT          24
        # |               BUILD_MAP                2
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              10 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_CONST               6 ('assert %(py6)s')
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE

    def test_chapter_and_word_count(self, sample_state):
        'ch'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  47           RESUME                   0
        # |  48           LOAD_GLOBAL              1 (run + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               LOAD_GLOBAL              2 (GOOD)
        # |               BUILD_LIST               1
        # |               LOAD_GLOBAL              4 (PASS)
        # |               BUILD_LIST               1
        # |               CALL                     3
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (row)
        # |  49           LOAD_FAST_BORROW         2 (row)
        # |               LOAD_CONST               1 ('ch')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_SMALL_INT           1
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               9 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_CONST               4 ('assert %(py6)s')
        # |               LOAD_CONST               5 ('py6')
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |  50           LOAD_FAST_BORROW         2 (row)
        # |               LOAD_CONST               7 ('word_count')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_SMALL_INT           0
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               COMPARE_OP             132 (>)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('>',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py1)s > %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_CONST               4 ('assert %(py6)s')
        # |               LOAD_CONST               5 ('py6')
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format7)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE

    def test_failing_notes_name_their_scene(self, sample_state):
        'notes'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  52           RESUME                   0
        # |  53           LOAD_GLOBAL              1 (run + NULL)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               LOAD_GLOBAL              2 (GOOD)
        # |               LOAD_GLOBAL              2 (GOOD)
        # |               BUILD_LIST               2
        # |               LOAD_GLOBAL              4 (FAIL)
        # |               LOAD_GLOBAL              6 (PASS)
        # |               BUILD_LIST               2
        # |               CALL                     3
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (row)
        # |  54           LOAD_FAST_BORROW         2 (row)
        # |               LOAD_CONST               1 ('notes')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_CONST               2 ('ch001_s2')
        # |               BUILD_LIST               1
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_CONST               5 ('assert %(py6)s')
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format7)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |  55           LOAD_FAST_BORROW         2 (row)
        # |               LOAD_CONST               8 ('passed')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_CONST               9 (False)
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               IS_OP                    0 (is)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 (('is',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py1)s is %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_CONST               5 ('assert %(py6)s')
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format7)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE


class TestRevisionRounds:
    'TestRevisionRounds'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  58           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestRevisionRounds')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          58
    # |               STORE_NAME               3 (__firstlineno__)
    # |  59           LOAD_CONST               1 ('修订到底有没有用 —— 同一章修订前后的分数变化，此前完全是黑箱。')
    # |               STORE_NAME               4 (__doc__)
    # |  61           LOAD_CONST               2 (<code object test_each_round_is_recorded_separately at 0x7ce72bdc00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 61>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_each_round_is_recorded_separately)
    # |  66           LOAD_CONST               3 (<code object test_gate_failures_do_not_produce_rows at 0x7ce72bbc00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 66>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_gate_failures_do_not_produce_rows)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_each_round_is_recorded_separately at 0x7ce72bdc00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 61>:
    # |   61            RESUME                   0
    # |   62            LOAD_GLOBAL              1 (run + NULL)
    # |                 LOAD_FAST_BORROW         1 (sample_state)
    # |                 LOAD_GLOBAL              2 (GOOD)
    # |                 LOAD_GLOBAL              2 (GOOD)
    # |                 BUILD_LIST               2
    # |                 LOAD_GLOBAL              4 (FAIL)
    # |                 LOAD_GLOBAL              6 (PASS)
    # |                 BUILD_LIST               2
    # |                 CALL                     3
    # |                 STORE_FAST               2 (rows)
    # |   63            LOAD_FAST_BORROW         2 (rows)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      3 (r)
    # |                 SWAP                     2
    # |         L1:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                11 (to L3)
    # |                 STORE_FAST_LOAD_FAST    51 (r, r)
    # |                 LOAD_CONST               0 ('revision')
    # |                 BINARY_OP               26 ([])
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           13 (to L2)
    # |         L3:     END_FOR
    # |                 POP_ITER
    # |         L4:     STORE_FAST               4 (@py_assert0)
    # |                 STORE_FAST               3 (r)
    # |                 LOAD_SMALL_INT           0
    # |                 LOAD_SMALL_INT           1
    # |                 BUILD_LIST               2
    # |                 STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |                 LOAD_FAST_BORROW         5 (@py_assert3)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       121 (to L5)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST               9 (('==',))
    # |                 LOAD_FAST_BORROW         6 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              10 (('%(py1)s == %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py1')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               2 ('py4')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format5)
    # |                 LOAD_CONST               3 ('assert %(py6)s')
    # |                 LOAD_CONST               4 ('py6')
    # |                 LOAD_FAST_BORROW         7 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format7)
    # |                 LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L5:     LOAD_CONST               5 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # |   64            LOAD_FAST_BORROW         2 (rows)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      3 (r)
    # |                 SWAP                     2
    # |         L6:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L7:     FOR_ITER                11 (to L8)
    # |                 STORE_FAST_LOAD_FAST    51 (r, r)
    # |                 LOAD_CONST               6 ('passed')
    # |                 BINARY_OP               26 ([])
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           13 (to L7)
    # |         L8:     END_FOR
    # |                 POP_ITER
    # |         L9:     STORE_FAST               4 (@py_assert0)
    # |                 STORE_FAST               3 (r)
    # |                 LOAD_CONST               7 (False)
    # |                 LOAD_CONST               8 (True)
    # |                 BUILD_LIST               2
    # |                 STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |                 LOAD_FAST_BORROW         5 (@py_assert3)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       121 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST               9 (('==',))
    # |                 LOAD_FAST_BORROW         6 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              10 (('%(py1)s == %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py1')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               2 ('py4')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               12 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format5)
    # |                 LOAD_CONST               3 ('assert %(py6)s')
    # |                 LOAD_CONST               4 ('py6')
    # |                 LOAD_FAST_BORROW         7 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format7)
    # |                 LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L10:     LOAD_CONST               5 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # |                 LOAD_CONST               5 (None)
    # |                 RETURN_VALUE
    # |   --   L11:     SWAP                     2
    # |                 POP_TOP
    # |   63            SWAP                     2
    # |                 STORE_FAST               3 (r)
    # |                 RERAISE                  0
    # |   --   L12:     SWAP                     2
    # |                 POP_TOP
    # |   64            SWAP                     2
    # |                 STORE_FAST               3 (r)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L11 [2]
    # |   L6 to L9 -> L12 [2]
    # | Disassembly of <code object test_gate_failures_do_not_produce_rows at 0x7ce72bbc00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 66>:
    # |   66           RESUME                   0
    # |   68           LOAD_GLOBAL              1 (run + NULL)
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                LOAD_GLOBAL              2 (BAD)
    # |                LOAD_GLOBAL              4 (GOOD)
    # |                BUILD_LIST               2
    # |                LOAD_GLOBAL              6 (PASS)
    # |                BUILD_LIST               1
    # |                CALL                     3
    # |                STORE_FAST               2 (rows)
    # |   69           LOAD_FAST_BORROW         2 (rows)
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      3 (r)
    # |                SWAP                     2
    # |        L1:     BUILD_LIST               0
    # |                SWAP                     2
    # |        L2:     FOR_ITER                11 (to L3)
    # |                STORE_FAST_LOAD_FAST    51 (r, r)
    # |                LOAD_CONST               1 ('revision')
    # |                BINARY_OP               26 ([])
    # |                LIST_APPEND              2
    # |                JUMP_BACKWARD           13 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |        L4:     STORE_FAST               4 (@py_assert0)
    # |                STORE_FAST               3 (r)
    # |                LOAD_SMALL_INT           1
    # |                BUILD_LIST               1
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       148 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST               8 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               9 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('py4')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format5)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               14 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST               4 ('只有修订后那次评审')
    # |                CALL                     1
    # |                LOAD_CONST               5 ('\n>assert %(py6)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               6 ('py6')
    # |                LOAD_FAST_BORROW         7 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format7)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L5:     LOAD_CONST               7 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               7 (None)
    # |                RETURN_VALUE
    # |   --   L6:     SWAP                     2
    # |                POP_TOP
    # |   69           SWAP                     2
    # |                STORE_FAST               3 (r)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L6 [2]

    def test_each_round_is_recorded_separately(self, sample_state):
        'revision'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   61            RESUME                   0
        # |   62            LOAD_GLOBAL              1 (run + NULL)
        # |                 LOAD_FAST_BORROW         1 (sample_state)
        # |                 LOAD_GLOBAL              2 (GOOD)
        # |                 LOAD_GLOBAL              2 (GOOD)
        # |                 BUILD_LIST               2
        # |                 LOAD_GLOBAL              4 (FAIL)
        # |                 LOAD_GLOBAL              6 (PASS)
        # |                 BUILD_LIST               2
        # |                 CALL                     3
        # |                 STORE_FAST               2 (rows)
        # |   63            LOAD_FAST_BORROW         2 (rows)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      3 (r)
        # |                 SWAP                     2
        # |         L1:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                11 (to L3)
        # |                 STORE_FAST_LOAD_FAST    51 (r, r)
        # |                 LOAD_CONST               0 ('revision')
        # |                 BINARY_OP               26 ([])
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           13 (to L2)
        # |         L3:     END_FOR
        # |                 POP_ITER
        # |         L4:     STORE_FAST               4 (@py_assert0)
        # |                 STORE_FAST               3 (r)
        # |                 LOAD_SMALL_INT           0
        # |                 LOAD_SMALL_INT           1
        # |                 BUILD_LIST               2
        # |                 STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |                 LOAD_FAST_BORROW         5 (@py_assert3)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       121 (to L5)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST               9 (('==',))
        # |                 LOAD_FAST_BORROW         6 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              10 (('%(py1)s == %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py1')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               2 ('py4')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format5)
        # |                 LOAD_CONST               3 ('assert %(py6)s')
        # |                 LOAD_CONST               4 ('py6')
        # |                 LOAD_FAST_BORROW         7 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format7)
        # |                 LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L5:     LOAD_CONST               5 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # |   64            LOAD_FAST_BORROW         2 (rows)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      3 (r)
        # |                 SWAP                     2
        # |         L6:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L7:     FOR_ITER                11 (to L8)
        # |                 STORE_FAST_LOAD_FAST    51 (r, r)
        # |                 LOAD_CONST               6 ('passed')
        # |                 BINARY_OP               26 ([])
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           13 (to L7)
        # |         L8:     END_FOR
        # |                 POP_ITER
        # |         L9:     STORE_FAST               4 (@py_assert0)
        # |                 STORE_FAST               3 (r)
        # |                 LOAD_CONST               7 (False)
        # |                 LOAD_CONST               8 (True)
        # |                 BUILD_LIST               2
        # |                 STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |                 LOAD_FAST_BORROW         5 (@py_assert3)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       121 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST               9 (('==',))
        # |                 LOAD_FAST_BORROW         6 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              10 (('%(py1)s == %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py1')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               2 ('py4')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               12 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format5)
        # |                 LOAD_CONST               3 ('assert %(py6)s')
        # |                 LOAD_CONST               4 ('py6')
        # |                 LOAD_FAST_BORROW         7 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format7)
        # |                 LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L10:     LOAD_CONST               5 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # |                 LOAD_CONST               5 (None)
        # |                 RETURN_VALUE
        # |   --   L11:     SWAP                     2
        # |                 POP_TOP
        # |   63            SWAP                     2
        # |                 STORE_FAST               3 (r)
        # |                 RERAISE                  0
        # |   --   L12:     SWAP                     2
        # |                 POP_TOP
        # |   64            SWAP                     2
        # |                 STORE_FAST               3 (r)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L11 [2]
        # |   L6 to L9 -> L12 [2]

    def test_gate_failures_do_not_produce_rows(self, sample_state):
        'gate 不过就不评审，自然也没有分数可记。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   66           RESUME                   0
        # |   68           LOAD_GLOBAL              1 (run + NULL)
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                LOAD_GLOBAL              2 (BAD)
        # |                LOAD_GLOBAL              4 (GOOD)
        # |                BUILD_LIST               2
        # |                LOAD_GLOBAL              6 (PASS)
        # |                BUILD_LIST               1
        # |                CALL                     3
        # |                STORE_FAST               2 (rows)
        # |   69           LOAD_FAST_BORROW         2 (rows)
        # |                GET_ITER
        # |                LOAD_FAST_AND_CLEAR      3 (r)
        # |                SWAP                     2
        # |        L1:     BUILD_LIST               0
        # |                SWAP                     2
        # |        L2:     FOR_ITER                11 (to L3)
        # |                STORE_FAST_LOAD_FAST    51 (r, r)
        # |                LOAD_CONST               1 ('revision')
        # |                BINARY_OP               26 ([])
        # |                LIST_APPEND              2
        # |                JUMP_BACKWARD           13 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |        L4:     STORE_FAST               4 (@py_assert0)
        # |                STORE_FAST               3 (r)
        # |                LOAD_SMALL_INT           1
        # |                BUILD_LIST               1
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       148 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST               8 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               9 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('py4')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format5)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               14 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST               4 ('只有修订后那次评审')
        # |                CALL                     1
        # |                LOAD_CONST               5 ('\n>assert %(py6)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               6 ('py6')
        # |                LOAD_FAST_BORROW         7 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format7)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L5:     LOAD_CONST               7 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               7 (None)
        # |                RETURN_VALUE
        # |   --   L6:     SWAP                     2
        # |                POP_TOP
        # |   69           SWAP                     2
        # |                STORE_FAST               3 (r)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L6 [2]


class TestItNeverBreaksTheRun:
    'TestItNeverBreaksTheRun'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  72           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestItNeverBreaksTheRun')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          72
    # |               STORE_NAME               3 (__firstlineno__)
    # |  73           LOAD_CONST               1 (<code object test_a_broken_sink_does_not_sink_the_chapter at 0x7ce7283900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 73>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_a_broken_sink_does_not_sink_the_chapter)
    # |  83           LOAD_CONST               2 (<code object test_no_sink_is_fine at 0x7ce70ab100, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 83>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_no_sink_is_fine)
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_a_broken_sink_does_not_sink_the_chapter at 0x7ce7283900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 73>:
    # |  73           RESUME                   0
    # |  75           LOAD_CONST               1 (<code object boom at 0x109d8a6a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 75>)
    # |               MAKE_FUNCTION
    # |               STORE_FAST               2 (boom)
    # |  78           LOAD_GLOBAL              1 (build + NULL)
    # |               LOAD_GLOBAL              2 (GOOD)
    # |               BUILD_LIST               1
    # |               LOAD_GLOBAL              4 (PASS)
    # |               BUILD_LIST               1
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     3
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST               3 (p)
    # |               POP_TOP
    # |               STORE_FAST               4 (_)
    # |  79           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (boom, p)
    # |               STORE_ATTR               3 (judgment_sink)
    # |  80           LOAD_FAST_BORROW         3 (p)
    # |               LOAD_ATTR                9 (run + NULL|self)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               LOAD_GLOBAL             11 (volume + NULL)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           1
    # |               CALL                     3
    # |               STORE_FAST               5 (r)
    # |  81           LOAD_FAST_BORROW         5 (r)
    # |               LOAD_ATTR               12 (passed)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       141 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               2 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('r')
    # |               LOAD_GLOBAL             14 (@py_builtins)
    # |               LOAD_ATTR               16 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               20 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('r')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               22 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format3)
    # |               LOAD_GLOBAL             25 (AssertionError + NULL)
    # |               LOAD_GLOBAL             18 (@pytest_ar)
    # |               LOAD_ATTR               26 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format3)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               6 (None)
    # |               STORE_FAST               6 (@py_assert1)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object boom at 0x109d8a6a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 75>:
    # |  75           RESUME                   0
    # |  76           LOAD_GLOBAL              1 (OSError + NULL)
    # |               LOAD_CONST               0 ('磁盘满了')
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # | Disassembly of <code object test_no_sink_is_fine at 0x7ce70ab100, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 83>:
    # |  83            RESUME                   0
    # |  84            LOAD_GLOBAL              1 (build + NULL)
    # |                LOAD_GLOBAL              2 (GOOD)
    # |                BUILD_LIST               1
    # |                LOAD_GLOBAL              4 (PASS)
    # |                BUILD_LIST               1
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                CALL                     3
    # |                UNPACK_SEQUENCE          3
    # |                STORE_FAST               2 (p)
    # |                POP_TOP
    # |                STORE_FAST               3 (_)
    # |  85            LOAD_FAST_BORROW         2 (p)
    # |                LOAD_ATTR                6 (judgment_sink)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_CONST               0 (None)
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                IS_OP                    0 (is)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('is',))
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.judgment_sink\n} is %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('p')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               2 ('p')
    # |        L3:     LOAD_CONST               3 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format6)
    # |                LOAD_CONST               5 ('assert %(py7)s')
    # |                LOAD_CONST               6 ('py7')
    # |                LOAD_FAST_BORROW         7 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format8)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               0 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
    # |  86            LOAD_FAST_BORROW         2 (p)
    # |                LOAD_ATTR               24 (run)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_GLOBAL             27 (volume + NULL)
    # |                CALL                     0
    # |                STORE_FAST               9 (@py_assert5)
    # |                LOAD_SMALL_INT           1
    # |                STORE_FAST_LOAD_FAST   164 (@py_assert7, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 25 (sample_state, @py_assert5)
    # |                LOAD_FAST_BORROW        10 (@py_assert7)
    # |                CALL                     3
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert9, @py_assert9)
    # |                LOAD_ATTR               28 (passed)
    # |                STORE_FAST_LOAD_FAST   204 (@py_assert11, @py_assert11)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       393 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_CONST               7 ('assert %(py12)s\n{%(py12)s = %(py10)s\n{%(py10)s = %(py2)s\n{%(py2)s = %(py0)s.run\n}(%(py3)s, %(py6)s\n{%(py6)s = %(py4)s()\n}, %(py8)s)\n}.passed\n}')
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('p')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (p)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (p)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               2 ('p')
    # |        L7:     LOAD_CONST               3 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py3')
    # |                LOAD_CONST               9 ('sample_state')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               9 ('sample_state')
    # |       L10:     LOAD_CONST              10 ('py4')
    # |                LOAD_CONST              11 ('volume')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             26 (volume)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L12)
    # |                NOT_TAKEN
    # |       L11:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             26 (volume)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L13)
    # |       L12:     LOAD_CONST              11 ('volume')
    # |       L13:     LOAD_CONST              12 ('py6')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py8')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert7)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py10')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py12')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                8
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format13)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_format13)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L14:     LOAD_CONST               0 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  188 (@py_assert9, @py_assert11)
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE

    def test_a_broken_sink_does_not_sink_the_chapter(self, sample_state):
        '记账失败不许拖垮一章 —— 与缝合、归档、卷末压缩同一条原则。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  73           RESUME                   0
        # |  75           LOAD_CONST               1 (<code object boom at 0x109d8a6a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 75>)
        # |               MAKE_FUNCTION
        # |               STORE_FAST               2 (boom)
        # |  78           LOAD_GLOBAL              1 (build + NULL)
        # |               LOAD_GLOBAL              2 (GOOD)
        # |               BUILD_LIST               1
        # |               LOAD_GLOBAL              4 (PASS)
        # |               BUILD_LIST               1
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     3
        # |               UNPACK_SEQUENCE          3
        # |               STORE_FAST               3 (p)
        # |               POP_TOP
        # |               STORE_FAST               4 (_)
        # |  79           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (boom, p)
        # |               STORE_ATTR               3 (judgment_sink)
        # |  80           LOAD_FAST_BORROW         3 (p)
        # |               LOAD_ATTR                9 (run + NULL|self)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               LOAD_GLOBAL             11 (volume + NULL)
        # |               CALL                     0
        # |               LOAD_SMALL_INT           1
        # |               CALL                     3
        # |               STORE_FAST               5 (r)
        # |  81           LOAD_FAST_BORROW         5 (r)
        # |               LOAD_ATTR               12 (passed)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       141 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               2 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('r')
        # |               LOAD_GLOBAL             14 (@py_builtins)
        # |               LOAD_ATTR               16 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               20 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('r')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               22 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format3)
        # |               LOAD_GLOBAL             25 (AssertionError + NULL)
        # |               LOAD_GLOBAL             18 (@pytest_ar)
        # |               LOAD_ATTR               26 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format3)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               6 (None)
        # |               STORE_FAST               6 (@py_assert1)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object boom at 0x109d8a6a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 75>:
        # |  75           RESUME                   0
        # |  76           LOAD_GLOBAL              1 (OSError + NULL)
        # |               LOAD_CONST               0 ('磁盘满了')
        # |               CALL                     1
        # |               RAISE_VARARGS            1

        def boom(_row):
            '磁盘满了'
            # ── 函数体（字节码重建见 BODY 段）──
            # |  75           RESUME                   0
            # |  76           LOAD_GLOBAL              1 (OSError + NULL)
            # |               LOAD_CONST               0 ('磁盘满了')
            # |               CALL                     1
            # |               RAISE_VARARGS            1


    def test_no_sink_is_fine(self, sample_state):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  83            RESUME                   0
        # |  84            LOAD_GLOBAL              1 (build + NULL)
        # |                LOAD_GLOBAL              2 (GOOD)
        # |                BUILD_LIST               1
        # |                LOAD_GLOBAL              4 (PASS)
        # |                BUILD_LIST               1
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                CALL                     3
        # |                UNPACK_SEQUENCE          3
        # |                STORE_FAST               2 (p)
        # |                POP_TOP
        # |                STORE_FAST               3 (_)
        # |  85            LOAD_FAST_BORROW         2 (p)
        # |                LOAD_ATTR                6 (judgment_sink)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_CONST               0 (None)
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                IS_OP                    0 (is)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('is',))
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.judgment_sink\n} is %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('p')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               2 ('p')
        # |        L3:     LOAD_CONST               3 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format6)
        # |                LOAD_CONST               5 ('assert %(py7)s')
        # |                LOAD_CONST               6 ('py7')
        # |                LOAD_FAST_BORROW         7 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format8)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               0 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
        # |  86            LOAD_FAST_BORROW         2 (p)
        # |                LOAD_ATTR               24 (run)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_GLOBAL             27 (volume + NULL)
        # |                CALL                     0
        # |                STORE_FAST               9 (@py_assert5)
        # |                LOAD_SMALL_INT           1
        # |                STORE_FAST_LOAD_FAST   164 (@py_assert7, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 25 (sample_state, @py_assert5)
        # |                LOAD_FAST_BORROW        10 (@py_assert7)
        # |                CALL                     3
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert9, @py_assert9)
        # |                LOAD_ATTR               28 (passed)
        # |                STORE_FAST_LOAD_FAST   204 (@py_assert11, @py_assert11)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       393 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_CONST               7 ('assert %(py12)s\n{%(py12)s = %(py10)s\n{%(py10)s = %(py2)s\n{%(py2)s = %(py0)s.run\n}(%(py3)s, %(py6)s\n{%(py6)s = %(py4)s()\n}, %(py8)s)\n}.passed\n}')
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('p')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (p)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (p)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               2 ('p')
        # |        L7:     LOAD_CONST               3 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py3')
        # |                LOAD_CONST               9 ('sample_state')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               9 ('sample_state')
        # |       L10:     LOAD_CONST              10 ('py4')
        # |                LOAD_CONST              11 ('volume')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             26 (volume)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L12)
        # |                NOT_TAKEN
        # |       L11:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             26 (volume)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L13)
        # |       L12:     LOAD_CONST              11 ('volume')
        # |       L13:     LOAD_CONST              12 ('py6')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py8')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert7)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py10')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert9)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py12')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                8
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format13)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_format13)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L14:     LOAD_CONST               0 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  188 (@py_assert9, @py_assert11)
        # |                LOAD_CONST               0 (None)
        # |                RETURN_VALUE


class TestOnDiskFormat:
    'TestOnDiskFormat'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  89           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestOnDiskFormat')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          89
    # |               STORE_NAME               3 (__firstlineno__)
    # |  90           LOAD_CONST               1 (<code object test_rows_are_one_json_object_per_line at 0x7ce72b1180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 90>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_rows_are_one_json_object_per_line)
    # |  99           LOAD_CONST               2 (<code object test_chinese_is_readable_not_escaped at 0x7ce72be000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 99>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_chinese_is_readable_not_escaped)
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_rows_are_one_json_object_per_line at 0x7ce72b1180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 90>:
    # |   90           RESUME                   0
    # |   91           LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (None)
    # |                IMPORT_NAME              0 (novel_agent.cli)
    # |                IMPORT_FROM              1 (cli)
    # |                STORE_FAST               3 (cli)
    # |                POP_TOP
    # |   93           LOAD_FAST_BORROW         2 (monkeypatch)
    # |                LOAD_ATTR                5 (setattr + NULL|self)
    # |                LOAD_FAST_BORROW         3 (cli)
    # |                LOAD_CONST               2 ('BOOK')
    # |                LOAD_FAST_BORROW         1 (tmp_path)
    # |                CALL                     3
    # |                POP_TOP
    # |   94           LOAD_FAST_BORROW         3 (cli)
    # |                LOAD_ATTR                7 (save_judgment + NULL|self)
    # |                LOAD_CONST               3 ('ch')
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               4 ('total')
    # |                LOAD_SMALL_INT          31
    # |                BUILD_MAP                2
    # |                CALL                     1
    # |                POP_TOP
    # |   95           LOAD_FAST_BORROW         3 (cli)
    # |                LOAD_ATTR                7 (save_judgment + NULL|self)
    # |                LOAD_CONST               3 ('ch')
    # |                LOAD_SMALL_INT           2
    # |                LOAD_CONST               4 ('total')
    # |                LOAD_SMALL_INT          28
    # |                BUILD_MAP                2
    # |                CALL                     1
    # |                POP_TOP
    # |   96           LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               5 ('judgments.jsonl')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR                9 (read_text + NULL|self)
    # |                LOAD_CONST               6 ('utf-8')
    # |                CALL                     1
    # |                LOAD_ATTR               11 (splitlines + NULL|self)
    # |                CALL                     0
    # |                STORE_FAST               4 (lines)
    # |   97           LOAD_FAST_BORROW         4 (lines)
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      5 (l)
    # |                SWAP                     2
    # |        L1:     BUILD_LIST               0
    # |                SWAP                     2
    # |        L2:     FOR_ITER                32 (to L3)
    # |                STORE_FAST               5 (l)
    # |                LOAD_GLOBAL             12 (json)
    # |                LOAD_ATTR               14 (loads)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (l)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('ch')
    # |                BINARY_OP               26 ([])
    # |                LIST_APPEND              2
    # |                JUMP_BACKWARD           34 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |        L4:     STORE_FAST               6 (@py_assert0)
    # |                STORE_FAST               5 (l)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_SMALL_INT           2
    # |                BUILD_LIST               2
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              11 (('==',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              12 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               7 ('py1')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py4')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format5)
    # |                LOAD_CONST               9 ('assert %(py6)s')
    # |                LOAD_CONST              10 ('py6')
    # |                LOAD_FAST_BORROW         9 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format7)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L5:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L6:     SWAP                     2
    # |                POP_TOP
    # |   97           SWAP                     2
    # |                STORE_FAST               5 (l)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L6 [2]
    # | Disassembly of <code object test_chinese_is_readable_not_escaped at 0x7ce72be000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_judgments.py", line 99>:
    # |  99           RESUME                   0
    # | 101           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (None)
    # |               IMPORT_NAME              0 (novel_agent.cli)
    # |               IMPORT_FROM              1 (cli)
    # |               STORE_FAST               3 (cli)
    # |               POP_TOP
    # | 103           LOAD_FAST_BORROW         2 (monkeypatch)
    # |               LOAD_ATTR                5 (setattr + NULL|self)
    # |               LOAD_FAST_BORROW         3 (cli)
    # |               LOAD_CONST               2 ('BOOK')
    # |               LOAD_FAST_BORROW         1 (tmp_path)
    # |               CALL                     3
    # |               POP_TOP
    # | 104           LOAD_FAST_BORROW         3 (cli)
    # |               LOAD_ATTR                7 (save_judgment + NULL|self)
    # |               LOAD_CONST               3 ('note')
    # |               LOAD_CONST               4 ('情绪推进')
    # |               BUILD_MAP                1
    # |               CALL                     1
    # |               POP_TOP
    # | 105           LOAD_CONST               4 ('情绪推进')
    # |               STORE_FAST               4 (@py_assert0)
    # |               LOAD_CONST               5 ('judgments.jsonl')
    # |               STORE_FAST_LOAD_FAST    81 (@py_assert4, tmp_path)
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               BINARY_OP               11 (/)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert6, @py_assert6)
    # |               LOAD_ATTR                8 (read_text)
    # |               STORE_FAST               7 (@py_assert7)
    # |               LOAD_CONST               6 ('utf-8')
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert9, @py_assert7)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert9)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   148 (@py_assert11, @py_assert0)
    # |               LOAD_FAST_BORROW         9 (@py_assert11)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       265 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('in',))
    # |               LOAD_FAST_BORROW        10 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py1)s in %(py12)s\n{%(py12)s = %(py8)s\n{%(py8)s = (%(py3)s / %(py5)s).read_text\n}(%(py10)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert0, @py_assert11)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py3')
    # |               LOAD_CONST               9 ('tmp_path')
    # |               LOAD_GLOBAL             16 (@py_builtins)
    # |               LOAD_ATTR               18 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               20 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (tmp_path)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (tmp_path)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               9 ('tmp_path')
    # |       L3:     LOAD_CONST              10 ('py5')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py8')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert7)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py10')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert9)
    # |               CALL                     1
    # |               LOAD_CONST              13 ('py12')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert11)
    # |               CALL                     1
    # |               BUILD_MAP                6
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format13)
    # |               LOAD_CONST              14 ('assert %(py14)s')
    # |               LOAD_CONST              15 ('py14')
    # |               LOAD_FAST_BORROW        11 (@py_format13)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format15)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        12 (@py_format15)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               1 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST              10 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert6)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  137 (@py_assert9, @py_assert11)
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE

    def test_rows_are_one_json_object_per_line(self, tmp_path, monkeypatch):
        'BOOK'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   90           RESUME                   0
        # |   91           LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (None)
        # |                IMPORT_NAME              0 (novel_agent.cli)
        # |                IMPORT_FROM              1 (cli)
        # |                STORE_FAST               3 (cli)
        # |                POP_TOP
        # |   93           LOAD_FAST_BORROW         2 (monkeypatch)
        # |                LOAD_ATTR                5 (setattr + NULL|self)
        # |                LOAD_FAST_BORROW         3 (cli)
        # |                LOAD_CONST               2 ('BOOK')
        # |                LOAD_FAST_BORROW         1 (tmp_path)
        # |                CALL                     3
        # |                POP_TOP
        # |   94           LOAD_FAST_BORROW         3 (cli)
        # |                LOAD_ATTR                7 (save_judgment + NULL|self)
        # |                LOAD_CONST               3 ('ch')
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               4 ('total')
        # |                LOAD_SMALL_INT          31
        # |                BUILD_MAP                2
        # |                CALL                     1
        # |                POP_TOP
        # |   95           LOAD_FAST_BORROW         3 (cli)
        # |                LOAD_ATTR                7 (save_judgment + NULL|self)
        # |                LOAD_CONST               3 ('ch')
        # |                LOAD_SMALL_INT           2
        # |                LOAD_CONST               4 ('total')
        # |                LOAD_SMALL_INT          28
        # |                BUILD_MAP                2
        # |                CALL                     1
        # |                POP_TOP
        # |   96           LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               5 ('judgments.jsonl')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR                9 (read_text + NULL|self)
        # |                LOAD_CONST               6 ('utf-8')
        # |                CALL                     1
        # |                LOAD_ATTR               11 (splitlines + NULL|self)
        # |                CALL                     0
        # |                STORE_FAST               4 (lines)
        # |   97           LOAD_FAST_BORROW         4 (lines)
        # |                GET_ITER
        # |                LOAD_FAST_AND_CLEAR      5 (l)
        # |                SWAP                     2
        # |        L1:     BUILD_LIST               0
        # |                SWAP                     2
        # |        L2:     FOR_ITER                32 (to L3)
        # |                STORE_FAST               5 (l)
        # |                LOAD_GLOBAL             12 (json)
        # |                LOAD_ATTR               14 (loads)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (l)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('ch')
        # |                BINARY_OP               26 ([])
        # |                LIST_APPEND              2
        # |                JUMP_BACKWARD           34 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |        L4:     STORE_FAST               6 (@py_assert0)
        # |                STORE_FAST               5 (l)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_SMALL_INT           2
        # |                BUILD_LIST               2
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              11 (('==',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              12 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               7 ('py1')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py4')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format5)
        # |                LOAD_CONST               9 ('assert %(py6)s')
        # |                LOAD_CONST              10 ('py6')
        # |                LOAD_FAST_BORROW         9 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format7)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L5:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L6:     SWAP                     2
        # |                POP_TOP
        # |   97           SWAP                     2
        # |                STORE_FAST               5 (l)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L6 [2]

    def test_chinese_is_readable_not_escaped(self, tmp_path, monkeypatch):
        '这份文件是给人翻的，中文 那种转义没法读。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  99           RESUME                   0
        # | 101           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (None)
        # |               IMPORT_NAME              0 (novel_agent.cli)
        # |               IMPORT_FROM              1 (cli)
        # |               STORE_FAST               3 (cli)
        # |               POP_TOP
        # | 103           LOAD_FAST_BORROW         2 (monkeypatch)
        # |               LOAD_ATTR                5 (setattr + NULL|self)
        # |               LOAD_FAST_BORROW         3 (cli)
        # |               LOAD_CONST               2 ('BOOK')
        # |               LOAD_FAST_BORROW         1 (tmp_path)
        # |               CALL                     3
        # |               POP_TOP
        # | 104           LOAD_FAST_BORROW         3 (cli)
        # |               LOAD_ATTR                7 (save_judgment + NULL|self)
        # |               LOAD_CONST               3 ('note')
        # |               LOAD_CONST               4 ('情绪推进')
        # |               BUILD_MAP                1
        # |               CALL                     1
        # |               POP_TOP
        # | 105           LOAD_CONST               4 ('情绪推进')
        # |               STORE_FAST               4 (@py_assert0)
        # |               LOAD_CONST               5 ('judgments.jsonl')
        # |               STORE_FAST_LOAD_FAST    81 (@py_assert4, tmp_path)
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               BINARY_OP               11 (/)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert6, @py_assert6)
        # |               LOAD_ATTR                8 (read_text)
        # |               STORE_FAST               7 (@py_assert7)
        # |               LOAD_CONST               6 ('utf-8')
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert9, @py_assert7)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert9)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   148 (@py_assert11, @py_assert0)
        # |               LOAD_FAST_BORROW         9 (@py_assert11)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       265 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('in',))
        # |               LOAD_FAST_BORROW        10 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py1)s in %(py12)s\n{%(py12)s = %(py8)s\n{%(py8)s = (%(py3)s / %(py5)s).read_text\n}(%(py10)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert0, @py_assert11)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py3')
        # |               LOAD_CONST               9 ('tmp_path')
        # |               LOAD_GLOBAL             16 (@py_builtins)
        # |               LOAD_ATTR               18 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               20 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (tmp_path)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (tmp_path)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               9 ('tmp_path')
        # |       L3:     LOAD_CONST              10 ('py5')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py8')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert7)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py10')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert9)
        # |               CALL                     1
        # |               LOAD_CONST              13 ('py12')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert11)
        # |               CALL                     1
        # |               BUILD_MAP                6
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format13)
        # |               LOAD_CONST              14 ('assert %(py14)s')
        # |               LOAD_CONST              15 ('py14')
        # |               LOAD_FAST_BORROW        11 (@py_format13)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format15)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        12 (@py_format15)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               1 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST              10 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert6)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  137 (@py_assert9, @py_assert11)
        # |               LOAD_CONST               1 (None)
        # |               RETURN_VALUE

