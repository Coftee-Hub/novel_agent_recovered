# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py
# 来源   : test_skills.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = 'skills 加载与拼装。\n\n核心断言：拼装结果必须字节稳定。它进的是缓存前缀，不稳定 = 缓存永远 miss。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'skills 加载与拼装。\n\n核心断言：拼装结果必须字节稳定。它进的是缓存前缀，不稳定 = 缓存永远 miss。\n',
    5: 'skills',
    9: 'TestLoading',
    11: 'TestComposition',
    13: 'TestRealSkills',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'SkillLibrary',
    ('lib', 0): 'a.md',
    ('lib', 1): 'A 的内容',
    ('lib', 2): 'utf-8',
    ('lib', 3): 'b.md',
    ('lib', 4): 'B 的内容',
    ('lib', 5): 'c.md',
    ('lib', 6): 'C 的内容',
    ('TestLoading', 0): 'TestLoading',
    ('test_available_sorted', 0): 'a',
    ('test_available_sorted', 1): 'py0',
    ('test_available_sorted', 2): 'lib',
    ('test_available_sorted', 3): 'py2',
    ('test_available_sorted', 4): 'py4',
    ('test_available_sorted', 5): 'py7',
    ('test_available_sorted', 6): 'assert %(py9)s',
    ('test_available_sorted', 7): 'py9',
    ('test_load', 0): 'a',
    ('test_load', 1): 'A 的内容',
    ('test_load', 2): 'py0',
    ('test_load', 3): 'lib',
    ('test_load', 4): 'py2',
    ('test_load', 5): 'py4',
    ('test_load', 6): 'py6',
    ('test_load', 7): 'py9',
    ('test_load', 8): 'assert %(py11)s',
    ('test_load', 9): 'py11',
    ('test_missing_names_the_available_ones', 0): 'a、b、c',
    ('test_missing_names_the_available_ones', 2): 'nope',
    ('TestComposition', 0): 'TestComposition',
    ('test_respects_given_order', 0): 'c',
    ('test_respects_given_order', 1): 'C 的内容',
    ('test_respects_given_order', 2): 'A 的内容',
    ('test_respects_given_order', 3): 'B 的内容',
    ('test_respects_given_order', 4): 'py0',
    ('test_respects_given_order', 5): 'out',
    ('test_respects_given_order', 6): 'py2',
    ('test_respects_given_order', 7): 'py4',
    ('test_respects_given_order', 8): 'py6',
    ('test_respects_given_order', 9): 'py9',
    ('test_respects_given_order', 10): 'py11',
    ('test_respects_given_order', 11): 'py13',
    ('test_respects_given_order', 12): 'py15',
    ('test_respects_given_order', 13): 'py16',
    ('test_respects_given_order', 14): 'py18',
    ('test_respects_given_order', 15): 'py20',
    ('test_respects_given_order', 16): 'py22',
    ('test_respects_given_order', 17): 'assert %(py24)s',
    ('test_respects_given_order', 18): 'py24',
    ('test_byte_stable_across_calls', 0): '同样的输入必须产出同样的字节 —— 否则缓存前缀每次都变。',
    ('test_byte_stable_across_calls', 1): 'a',
    ('test_byte_stable_across_calls', 2): 'b',
    ('test_byte_stable_across_calls', 3): 'py0',
    ('test_byte_stable_across_calls', 4): 'lib',
    ('test_byte_stable_across_calls', 5): 'py2',
    ('test_byte_stable_across_calls', 6): 'py4',
    ('test_byte_stable_across_calls', 7): 'py6',
    ('test_byte_stable_across_calls', 8): 'py8',
    ('test_byte_stable_across_calls', 9): 'py10',
    ('test_byte_stable_across_calls', 10): 'py12',
    ('test_byte_stable_across_calls', 11): 'py14',
    ('test_byte_stable_across_calls', 12): 'assert %(py16)s',
    ('test_byte_stable_across_calls', 13): 'py16',
    ('test_order_change_changes_bytes', 0): '反过来说，顺序变了字节就该变 —— 提醒调用方顺序是有代价的。',
    ('test_order_change_changes_bytes', 1): 'a',
    ('test_order_change_changes_bytes', 2): 'b',
    ('test_order_change_changes_bytes', 3): 'py0',
    ('test_order_change_changes_bytes', 4): 'lib',
    ('test_order_change_changes_bytes', 5): 'py2',
    ('test_order_change_changes_bytes', 6): 'py4',
    ('test_order_change_changes_bytes', 7): 'py6',
    ('test_order_change_changes_bytes', 8): 'py8',
    ('test_order_change_changes_bytes', 9): 'py10',
    ('test_order_change_changes_bytes', 10): 'py12',
    ('test_order_change_changes_bytes', 11): 'py14',
    ('test_order_change_changes_bytes', 12): 'assert %(py16)s',
    ('test_order_change_changes_bytes', 13): 'py16',
    ('test_strict_by_default', 0): 'a',
    ('test_strict_by_default', 1): 'missing',
    ('test_lenient_skips_missing', 0): '语料未到位时，部分 skill 尚未萃取，要能先跑起来。',
    ('test_lenient_skips_missing', 1): 'a',
    ('test_lenient_skips_missing', 2): 'b',
    ('test_lenient_skips_missing', 5): 'py0',
    ('test_lenient_skips_missing', 6): 'lib',
    ('test_lenient_skips_missing', 7): 'py2',
    ('test_lenient_skips_missing', 8): 'py4',
    ('test_lenient_skips_missing', 9): 'py6',
    ('test_lenient_skips_missing', 10): 'py8',
    ('test_lenient_skips_missing', 11): 'py10',
    ('test_lenient_skips_missing', 12): 'py12',
    ('test_lenient_skips_missing', 13): 'py14',
    ('test_lenient_skips_missing', 14): 'py16',
    ('test_lenient_skips_missing', 15): 'assert %(py18)s',
    ('test_lenient_skips_missing', 16): 'py18',
    ('TestRealSkills', 0): 'TestRealSkills',
    ('test_written_skills_load', 0): 'format_spec',
    ('test_written_skills_load', 1): 'py1',
    ('test_written_skills_load', 2): 'py3',
    ('test_written_skills_load', 3): 'lib',
    ('test_written_skills_load', 4): 'py5',
    ('test_written_skills_load', 5): 'py7',
    ('test_written_skills_load', 6): 'assert %(py9)s',
    ('test_written_skills_load', 7): 'py9',
    ('test_written_skills_load', 9): 'intimacy_levels',
    ('test_format_spec_matches_config', 0): 'skills 里写给模型看的规范，必须和 gate 实际执行的一致。',
    ('test_format_spec_matches_config', 2): 'config',
    ('test_format_spec_matches_config', 3): 'project.yaml',
    ('test_format_spec_matches_config', 4): 'utf-8',
    ('test_format_spec_matches_config', 5): 'format_spec',
    ('test_format_spec_matches_config', 6): 'length',
    ('test_format_spec_matches_config', 7): 'chapter_min',
    ('test_format_spec_matches_config', 8): 'py0',
    ('test_format_spec_matches_config', 9): 'str',
    ('test_format_spec_matches_config', 10): 'py2',
    ('test_format_spec_matches_config', 11): 'py4',
    ('test_format_spec_matches_config', 12): 'py6',
    ('test_format_spec_matches_config', 13): 'text',
    ('test_format_spec_matches_config', 14): 'assert %(py8)s',
    ('test_format_spec_matches_config', 15): 'py8',
    ('test_format_spec_matches_config', 16): 'chapter_max',
    ('test_format_spec_matches_config', 17): 'paragraph_max_chars',
    ('test_format_spec_matches_config', 18): 'dialogue_ratio_min',
    ('test_format_spec_matches_config', 19): '.0%',
    ('test_format_spec_matches_config', 20): 'py1',
    ('test_format_spec_matches_config', 21): 'py3',
    ('test_format_spec_matches_config', 22): 'assert %(py5)s',
    ('test_format_spec_matches_config', 23): 'py5',
    ('test_format_spec_matches_config', 24): 'dialogue_ratio_max',
    ('test_intimacy_levels_covers_all_configured_levels', 0): 'intimacy_levels',
    ('test_intimacy_levels_covers_all_configured_levels', 1): 'py0',
    ('test_intimacy_levels_covers_all_configured_levels', 2): 'level',
    ('test_intimacy_levels_covers_all_configured_levels', 3): 'py2',
    ('test_intimacy_levels_covers_all_configured_levels', 4): 'text',
    ('test_intimacy_levels_covers_all_configured_levels', 5): 'assert %(py4)s',
    ('test_intimacy_levels_covers_all_configured_levels', 6): 'py4',
    ('test_every_referenced_skill_exists_somewhere', 0): '引用的 skill 要么已在 skills/，要么还在 _drafts/ 待审。\n出现第三种情况就是名字拼错了。',
    ('test_every_referenced_skill_exists_somewhere', 1): '_drafts',
    ('test_every_referenced_skill_exists_somewhere', 2): '*.md',
    ('test_every_referenced_skill_exists_somewhere', 3): '引用了不存在的 skill：',
    ('test_every_referenced_skill_exists_somewhere', 4): '\n>assert not %(py0)s',
    ('test_every_referenced_skill_exists_somewhere', 5): 'py0',
    ('test_every_referenced_skill_exists_somewhere', 6): 'missing',
    ('test_lenient_compose_works_today', 0): '语料没到位也要能拼出可用的 system_core。',
    ('test_lenient_compose_works_today', 3): '格式硬规范',
    ('test_lenient_compose_works_today', 4): '亲密尺度分档',
    ('test_lenient_compose_works_today', 5): 'py3',
    ('test_lenient_compose_works_today', 6): 'py5',
    ('test_lenient_compose_works_today', 7): 'out',
    ('test_lenient_compose_works_today', 8): '%(py7)s',
    ('test_lenient_compose_works_today', 9): 'py7',
    ('test_lenient_compose_works_today', 10): 'py10',
    ('test_lenient_compose_works_today', 11): 'py12',
    ('test_lenient_compose_works_today', 12): '%(py14)s',
    ('test_lenient_compose_works_today', 13): 'py14',
    ('test_lenient_compose_works_today', 14): 'assert %(py17)s',
    ('test_lenient_compose_works_today', 15): 'py17',
    ('test_design_time_skills_kept_out_of_writer', 0): 'writer 一次只写一个 scene，拿到的是设计的**产物**（人物卡来自\nstory_state、节拍类型在 scene spec 里），不需要知道它们怎么被设计。\n\n把设计期技能塞给 writer 会让它的 system_core 从 22K 涨到 41K tokens，\n多出来的规则只会争夺注意力。这条断言防止它们被顺手加回去。',
    ('test_design_time_skills_kept_out_of_writer', 1): 'py0',
    ('test_design_time_skills_kept_out_of_writer', 2): 'design_time',
    ('test_design_time_skills_kept_out_of_writer', 3): 'py1',
    ('test_design_time_skills_kept_out_of_writer', 4): 'set',
    ('test_design_time_skills_kept_out_of_writer', 5): 'py2',
    ('test_design_time_skills_kept_out_of_writer', 6): 'WRITER_SKILLS',
    ('test_design_time_skills_kept_out_of_writer', 7): 'py4',
    ('test_design_time_skills_kept_out_of_writer', 8): 'py7',
    ('test_design_time_skills_kept_out_of_writer', 9): 'py9',
    ('test_design_time_skills_kept_out_of_writer', 10): 'assert %(py11)s',
    ('test_design_time_skills_kept_out_of_writer', 11): 'py11',
    ('test_design_time_skills_kept_out_of_writer', 13): 'py3',
    ('test_design_time_skills_kept_out_of_writer', 14): 'ARCHITECT_SKILLS',
    ('test_design_time_skills_kept_out_of_writer', 15): 'py5',
    ('test_design_time_skills_kept_out_of_writer', 16): 'assert %(py7)s',
    ('test_writer_keeps_the_craft_skills', 0): '反过来，落笔相关的必须在 writer 手里。',
    ('test_writer_keeps_the_craft_skills', 1): 'py1',
    ('test_writer_keeps_the_craft_skills', 2): 'py3',
    ('test_writer_keeps_the_craft_skills', 3): 'set',
    ('test_writer_keeps_the_craft_skills', 4): 'py4',
    ('test_writer_keeps_the_craft_skills', 5): 'WRITER_SKILLS',
    ('test_writer_keeps_the_craft_skills', 6): 'py6',
    ('test_writer_keeps_the_craft_skills', 7): 'assert %(py8)s',
    ('test_writer_keeps_the_craft_skills', 8): 'py8',
    ('test_format_spec_is_last', 0): '格式规范放最后，最靠近指令 —— 模型对结尾要求服从度更高。',
    ('test_format_spec_is_last', 1): 'format_spec',
    ('test_format_spec_is_last', 2): 'py1',
    ('test_format_spec_is_last', 3): 'py4',
    ('test_format_spec_is_last', 4): 'assert %(py6)s',
    ('test_format_spec_is_last', 5): 'py6',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def lib(tmp_path):
    'a.md'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  19           RESUME                   0
    # |  21           LOAD_FAST_BORROW         0 (tmp_path)
    # |               LOAD_CONST               0 ('a.md')
    # |               BINARY_OP               11 (/)
    # |               LOAD_ATTR                1 (write_text + NULL|self)
    # |               LOAD_CONST               1 ('A 的内容')
    # |               LOAD_CONST               2 ('utf-8')
    # |               CALL                     2
    # |               POP_TOP
    # |  22           LOAD_FAST_BORROW         0 (tmp_path)
    # |               LOAD_CONST               3 ('b.md')
    # |               BINARY_OP               11 (/)
    # |               LOAD_ATTR                1 (write_text + NULL|self)
    # |               LOAD_CONST               4 ('B 的内容')
    # |               LOAD_CONST               2 ('utf-8')
    # |               CALL                     2
    # |               POP_TOP
    # |  23           LOAD_FAST_BORROW         0 (tmp_path)
    # |               LOAD_CONST               5 ('c.md')
    # |               BINARY_OP               11 (/)
    # |               LOAD_ATTR                1 (write_text + NULL|self)
    # |               LOAD_CONST               6 ('C 的内容')
    # |               LOAD_CONST               2 ('utf-8')
    # |               CALL                     2
    # |               POP_TOP
    # |  24           LOAD_GLOBAL              3 (SkillLibrary + NULL)
    # |               LOAD_FAST_BORROW         0 (tmp_path)
    # |               CALL                     1
    # |               RETURN_VALUE

class TestLoading:
    'TestLoading'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  27           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestLoading')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          27
    # |               STORE_NAME               3 (__firstlineno__)
    # |  28           LOAD_CONST               1 (<code object test_available_sorted at 0x75052f3300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 28>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_available_sorted)
    # |  31           LOAD_CONST               2 (<code object test_load at 0x75052ec000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 31>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_load)
    # |  34           LOAD_CONST               3 (<code object test_missing_names_the_available_ones at 0x105e22730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 34>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_missing_names_the_available_ones)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_available_sorted at 0x75052f3300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 28>:
    # |  28           RESUME                   0
    # |  29           LOAD_FAST_BORROW         1 (lib)
    # |               LOAD_ATTR                0 (available)
    # |               STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               STORE_FAST               3 (@py_assert3)
    # |               BUILD_LIST               0
    # |               LOAD_CONST               9 (('a', 'b', 'c'))
    # |               LIST_EXTEND              1
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       221 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.available\n}()\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('lib')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('lib')
    # |       L3:     LOAD_CONST               3 ('py2')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py7')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_CONST               6 ('assert %(py9)s')
    # |               LOAD_CONST               7 ('py9')
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format10)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert5, @py_assert6)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_load at 0x75052ec000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 31>:
    # |  31           RESUME                   0
    # |  32           LOAD_FAST_BORROW         1 (lib)
    # |               LOAD_ATTR                0 (load)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               0 ('a')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               LOAD_CONST               1 ('A 的内容')
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert8, @py_assert5)
    # |               LOAD_FAST_BORROW         5 (@py_assert8)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       243 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         6 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.load\n}(%(py4)s)\n} == %(py9)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert5, @py_assert8)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('lib')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('lib')
    # |       L3:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py9')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format10)
    # |               LOAD_CONST               8 ('assert %(py11)s')
    # |               LOAD_CONST               9 ('py11')
    # |               LOAD_FAST_BORROW         7 (@py_format10)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format12)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format12)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert7, @py_assert8)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_missing_names_the_available_ones at 0x105e22730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 34>:
    # |   34           RESUME                   0
    # |   35           LOAD_GLOBAL              0 (pytest)
    # |                LOAD_ATTR                2 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (SkillNotFound)
    # |                LOAD_CONST               0 ('a、b、c')
    # |                LOAD_CONST               1 (('match',))
    # |                CALL_KW                  2
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |   36           LOAD_FAST_BORROW         1 (lib)
    # |                LOAD_ATTR                7 (load + NULL|self)
    # |                LOAD_CONST               2 ('nope')
    # |                CALL                     1
    # |                POP_TOP
    # |   35   L2:     LOAD_CONST               3 (None)
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

    def test_available_sorted(self, lib):
        'a'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  28           RESUME                   0
        # |  29           LOAD_FAST_BORROW         1 (lib)
        # |               LOAD_ATTR                0 (available)
        # |               STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               STORE_FAST               3 (@py_assert3)
        # |               BUILD_LIST               0
        # |               LOAD_CONST               9 (('a', 'b', 'c'))
        # |               LIST_EXTEND              1
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       221 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.available\n}()\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('lib')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('lib')
        # |       L3:     LOAD_CONST               3 ('py2')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py7')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_CONST               6 ('assert %(py9)s')
        # |               LOAD_CONST               7 ('py9')
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format10)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert5, @py_assert6)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE

    def test_load(self, lib):
        'a'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  31           RESUME                   0
        # |  32           LOAD_FAST_BORROW         1 (lib)
        # |               LOAD_ATTR                0 (load)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               0 ('a')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               LOAD_CONST               1 ('A 的内容')
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert8, @py_assert5)
        # |               LOAD_FAST_BORROW         5 (@py_assert8)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       243 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         6 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.load\n}(%(py4)s)\n} == %(py9)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert5, @py_assert8)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('lib')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('lib')
        # |       L3:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py9')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format10)
        # |               LOAD_CONST               8 ('assert %(py11)s')
        # |               LOAD_CONST               9 ('py11')
        # |               LOAD_FAST_BORROW         7 (@py_format10)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format12)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format12)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert7, @py_assert8)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE

    def test_missing_names_the_available_ones(self, lib):
        'a、b、c'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   34           RESUME                   0
        # |   35           LOAD_GLOBAL              0 (pytest)
        # |                LOAD_ATTR                2 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (SkillNotFound)
        # |                LOAD_CONST               0 ('a、b、c')
        # |                LOAD_CONST               1 (('match',))
        # |                CALL_KW                  2
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |   36           LOAD_FAST_BORROW         1 (lib)
        # |                LOAD_ATTR                7 (load + NULL|self)
        # |                LOAD_CONST               2 ('nope')
        # |                CALL                     1
        # |                POP_TOP
        # |   35   L2:     LOAD_CONST               3 (None)
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


class TestComposition:
    'TestComposition'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  39           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestComposition')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          39
    # |               STORE_NAME               3 (__firstlineno__)
    # |  40           LOAD_CONST               1 (<code object test_respects_given_order at 0x75052c5800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 40>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_respects_given_order)
    # |  44           LOAD_CONST               2 (<code object test_byte_stable_across_calls at 0x7504d88a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 44>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_byte_stable_across_calls)
    # |  48           LOAD_CONST               3 (<code object test_order_change_changes_bytes at 0x7504d8a300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 48>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_order_change_changes_bytes)
    # |  52           LOAD_CONST               4 (<code object test_strict_by_default at 0x105e23630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 52>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_strict_by_default)
    # |  56           LOAD_CONST               5 (<code object test_lenient_skips_missing at 0x7504d8a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 56>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_lenient_skips_missing)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_respects_given_order at 0x75052c5800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 40>:
    # |  40            RESUME                   0
    # |  41            LOAD_FAST_BORROW         1 (lib)
    # |                LOAD_ATTR                1 (compose + NULL|self)
    # |                BUILD_LIST               0
    # |                LOAD_CONST              20 (('c', 'a', 'b'))
    # |                LIST_EXTEND              1
    # |                CALL                     1
    # |                STORE_FAST               2 (out)
    # |  42            LOAD_FAST_BORROW         2 (out)
    # |                LOAD_ATTR                2 (index)
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_CONST               1 ('C 的内容')
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert3)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    82 (@py_assert5, out)
    # |                LOAD_ATTR                2 (index)
    # |                STORE_FAST               6 (@py_assert10)
    # |                LOAD_CONST               2 ('A 的内容')
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert12, @py_assert10)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert12)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   133 (@py_assert14, @py_assert5)
    # |                LOAD_FAST_BORROW         8 (@py_assert14)
    # |                COMPARE_OP               2 (<)
    # |                STORE_FAST_LOAD_FAST   146 (@py_assert7, out)
    # |                LOAD_ATTR                2 (index)
    # |                STORE_FAST              10 (@py_assert17)
    # |                LOAD_CONST               3 ('B 的内容')
    # |                STORE_FAST_LOAD_FAST   186 (@py_assert19, @py_assert17)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert19)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   200 (@py_assert21, @py_assert14)
    # |                LOAD_FAST_BORROW        12 (@py_assert21)
    # |                COMPARE_OP               2 (<)
    # |                STORE_FAST_LOAD_FAST   217 (@py_assert8, @py_assert7)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       10 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW        13 (@py_assert8)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       510 (to L11)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              21 (('<', '<'))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 157 (@py_assert7, @py_assert8)
    # |                BUILD_TUPLE              2
    # |                LOAD_CONST              22 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.index\n}(%(py4)s)\n} < %(py15)s\n{%(py15)s = %(py11)s\n{%(py11)s = %(py9)s.index\n}(%(py13)s)\n}', '%(py15)s\n{%(py15)s = %(py11)s\n{%(py11)s = %(py9)s.index\n}(%(py13)s)\n} < %(py22)s\n{%(py22)s = %(py18)s\n{%(py18)s = %(py16)s.index\n}(%(py20)s)\n}'))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 88 (@py_assert5, @py_assert14)
    # |                LOAD_FAST_BORROW        12 (@py_assert21)
    # |                BUILD_TUPLE              3
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py0')
    # |                LOAD_CONST               5 ('out')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (out)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (out)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST               5 ('out')
    # |        L4:     LOAD_CONST               6 ('py2')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py4')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py9')
    # |                LOAD_CONST               5 ('out')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (out)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (out)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               5 ('out')
    # |        L7:     LOAD_CONST              10 ('py11')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py13')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert12)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py15')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert14)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py16')
    # |                LOAD_CONST               5 ('out')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (out)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (out)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               5 ('out')
    # |       L10:     LOAD_CONST              14 ('py18')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert17)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py20')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert19)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py22')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert21)
    # |                CALL                     1
    # |                BUILD_MAP               12
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format23)
    # |                LOAD_CONST              17 ('assert %(py24)s')
    # |                LOAD_CONST              18 ('py24')
    # |                LOAD_FAST_BORROW        14 (@py_format23)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format25)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        15 (@py_format25)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L11:     LOAD_CONST              19 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert10)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert12)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert14)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert17)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  188 (@py_assert19, @py_assert21)
    # |                LOAD_CONST              19 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_byte_stable_across_calls at 0x7504d88a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 44>:
    # |  44           RESUME                   0
    # |  46           LOAD_FAST_BORROW         1 (lib)
    # |               LOAD_ATTR                0 (compose)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               1 ('a')
    # |               LOAD_CONST               2 ('b')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    65 (@py_assert5, lib)
    # |               LOAD_ATTR                0 (compose)
    # |               STORE_FAST               5 (@py_assert9)
    # |               LOAD_CONST               1 ('a')
    # |               LOAD_CONST               2 ('b')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert9)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert11)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   116 (@py_assert13, @py_assert5)
    # |               LOAD_FAST_BORROW         7 (@py_assert13)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       365 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('==',))
    # |               LOAD_FAST_BORROW         8 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.compose\n}(%(py4)s)\n} == %(py14)s\n{%(py14)s = %(py10)s\n{%(py10)s = %(py8)s.compose\n}(%(py12)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert5, @py_assert13)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('lib')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('lib')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py8')
    # |               LOAD_CONST               4 ('lib')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               4 ('lib')
    # |       L6:     LOAD_CONST               9 ('py10')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert9)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py12')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert11)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py14')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert13)
    # |               CALL                     1
    # |               BUILD_MAP                8
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format15)
    # |               LOAD_CONST              12 ('assert %(py16)s')
    # |               LOAD_CONST              13 ('py16')
    # |               LOAD_FAST_BORROW         9 (@py_format15)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format17)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format17)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              14 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert9)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  103 (@py_assert11, @py_assert13)
    # |               LOAD_CONST              14 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_order_change_changes_bytes at 0x7504d8a300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 48>:
    # |  48           RESUME                   0
    # |  50           LOAD_FAST_BORROW         1 (lib)
    # |               LOAD_ATTR                0 (compose)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               1 ('a')
    # |               LOAD_CONST               2 ('b')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    65 (@py_assert5, lib)
    # |               LOAD_ATTR                0 (compose)
    # |               STORE_FAST               5 (@py_assert9)
    # |               LOAD_CONST               2 ('b')
    # |               LOAD_CONST               1 ('a')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert9)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert11)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   116 (@py_assert13, @py_assert5)
    # |               LOAD_FAST_BORROW         7 (@py_assert13)
    # |               COMPARE_OP             103 (!=)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       365 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('!=',))
    # |               LOAD_FAST_BORROW         8 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.compose\n}(%(py4)s)\n} != %(py14)s\n{%(py14)s = %(py10)s\n{%(py10)s = %(py8)s.compose\n}(%(py12)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert5, @py_assert13)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('lib')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('lib')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py8')
    # |               LOAD_CONST               4 ('lib')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               4 ('lib')
    # |       L6:     LOAD_CONST               9 ('py10')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert9)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py12')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert11)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py14')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert13)
    # |               CALL                     1
    # |               BUILD_MAP                8
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format15)
    # |               LOAD_CONST              12 ('assert %(py16)s')
    # |               LOAD_CONST              13 ('py16')
    # |               LOAD_FAST_BORROW         9 (@py_format15)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format17)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format17)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              14 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert9)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  103 (@py_assert11, @py_assert13)
    # |               LOAD_CONST              14 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_strict_by_default at 0x105e23630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 52>:
    # |   52           RESUME                   0
    # |   53           LOAD_GLOBAL              0 (pytest)
    # |                LOAD_ATTR                2 (raises)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (SkillNotFound)
    # |                CALL                     1
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     POP_TOP
    # |   54           LOAD_FAST_BORROW         1 (lib)
    # |                LOAD_ATTR                7 (compose + NULL|self)
    # |                LOAD_CONST               0 ('a')
    # |                LOAD_CONST               1 ('missing')
    # |                BUILD_LIST               2
    # |                CALL                     1
    # |                POP_TOP
    # |   53   L2:     LOAD_CONST               2 (None)
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
    # | Disassembly of <code object test_lenient_skips_missing at 0x7504d8a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 56>:
    # |  56           RESUME                   0
    # |  58           LOAD_FAST_BORROW         1 (lib)
    # |               LOAD_ATTR                0 (compose)
    # |               STORE_FAST               2 (@py_assert1)
    # |               BUILD_LIST               0
    # |               LOAD_CONST              18 (('a', 'missing', 'b'))
    # |               LIST_EXTEND              1
    # |               STORE_FAST               3 (@py_assert3)
    # |               LOAD_CONST               3 (False)
    # |               STORE_FAST_LOAD_FAST    66 (@py_assert5, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               4 (('strict',))
    # |               CALL_KW                  2
    # |               STORE_FAST_LOAD_FAST    81 (@py_assert7, lib)
    # |               LOAD_ATTR                0 (compose)
    # |               STORE_FAST               6 (@py_assert11)
    # |               LOAD_CONST               1 ('a')
    # |               LOAD_CONST               2 ('b')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert13, @py_assert11)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert13)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   133 (@py_assert15, @py_assert7)
    # |               LOAD_FAST_BORROW         8 (@py_assert15)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert9, @py_assert9)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       387 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              19 (('==',))
    # |               LOAD_FAST_BORROW         9 (@py_assert9)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              20 (('%(py8)s\n{%(py8)s = %(py2)s\n{%(py2)s = %(py0)s.compose\n}(%(py4)s, strict=%(py6)s)\n} == %(py16)s\n{%(py16)s = %(py12)s\n{%(py12)s = %(py10)s.compose\n}(%(py14)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 88 (@py_assert7, @py_assert15)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST               6 ('lib')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               6 ('lib')
    # |       L3:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py6')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py8')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert7)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py10')
    # |               LOAD_CONST               6 ('lib')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               6 ('lib')
    # |       L6:     LOAD_CONST              12 ('py12')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert11)
    # |               CALL                     1
    # |               LOAD_CONST              13 ('py14')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert13)
    # |               CALL                     1
    # |               LOAD_CONST              14 ('py16')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert15)
    # |               CALL                     1
    # |               BUILD_MAP                9
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format17)
    # |               LOAD_CONST              15 ('assert %(py18)s')
    # |               LOAD_CONST              16 ('py18')
    # |               LOAD_FAST_BORROW        10 (@py_format17)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format19)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format19)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              17 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert9)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert11)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert13, @py_assert15)
    # |               LOAD_CONST              17 (None)
    # |               RETURN_VALUE

    def test_respects_given_order(self, lib):
        'c'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  40            RESUME                   0
        # |  41            LOAD_FAST_BORROW         1 (lib)
        # |                LOAD_ATTR                1 (compose + NULL|self)
        # |                BUILD_LIST               0
        # |                LOAD_CONST              20 (('c', 'a', 'b'))
        # |                LIST_EXTEND              1
        # |                CALL                     1
        # |                STORE_FAST               2 (out)
        # |  42            LOAD_FAST_BORROW         2 (out)
        # |                LOAD_ATTR                2 (index)
        # |                STORE_FAST               3 (@py_assert1)
        # |                LOAD_CONST               1 ('C 的内容')
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert3)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    82 (@py_assert5, out)
        # |                LOAD_ATTR                2 (index)
        # |                STORE_FAST               6 (@py_assert10)
        # |                LOAD_CONST               2 ('A 的内容')
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert12, @py_assert10)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert12)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   133 (@py_assert14, @py_assert5)
        # |                LOAD_FAST_BORROW         8 (@py_assert14)
        # |                COMPARE_OP               2 (<)
        # |                STORE_FAST_LOAD_FAST   146 (@py_assert7, out)
        # |                LOAD_ATTR                2 (index)
        # |                STORE_FAST              10 (@py_assert17)
        # |                LOAD_CONST               3 ('B 的内容')
        # |                STORE_FAST_LOAD_FAST   186 (@py_assert19, @py_assert17)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert19)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   200 (@py_assert21, @py_assert14)
        # |                LOAD_FAST_BORROW        12 (@py_assert21)
        # |                COMPARE_OP               2 (<)
        # |                STORE_FAST_LOAD_FAST   217 (@py_assert8, @py_assert7)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       10 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_FAST_BORROW        13 (@py_assert8)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       510 (to L11)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              21 (('<', '<'))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 157 (@py_assert7, @py_assert8)
        # |                BUILD_TUPLE              2
        # |                LOAD_CONST              22 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.index\n}(%(py4)s)\n} < %(py15)s\n{%(py15)s = %(py11)s\n{%(py11)s = %(py9)s.index\n}(%(py13)s)\n}', '%(py15)s\n{%(py15)s = %(py11)s\n{%(py11)s = %(py9)s.index\n}(%(py13)s)\n} < %(py22)s\n{%(py22)s = %(py18)s\n{%(py18)s = %(py16)s.index\n}(%(py20)s)\n}'))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 88 (@py_assert5, @py_assert14)
        # |                LOAD_FAST_BORROW        12 (@py_assert21)
        # |                BUILD_TUPLE              3
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py0')
        # |                LOAD_CONST               5 ('out')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (out)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (out)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST               5 ('out')
        # |        L4:     LOAD_CONST               6 ('py2')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py4')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py9')
        # |                LOAD_CONST               5 ('out')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (out)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (out)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               5 ('out')
        # |        L7:     LOAD_CONST              10 ('py11')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py13')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert12)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py15')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert14)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py16')
        # |                LOAD_CONST               5 ('out')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (out)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (out)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               5 ('out')
        # |       L10:     LOAD_CONST              14 ('py18')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert17)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py20')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert19)
        # |                CALL                     1
        # |                LOAD_CONST              16 ('py22')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert21)
        # |                CALL                     1
        # |                BUILD_MAP               12
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format23)
        # |                LOAD_CONST              17 ('assert %(py24)s')
        # |                LOAD_CONST              18 ('py24')
        # |                LOAD_FAST_BORROW        14 (@py_format23)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format25)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        15 (@py_format25)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L11:     LOAD_CONST              19 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST              13 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert10)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert12)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert14)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert17)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  188 (@py_assert19, @py_assert21)
        # |                LOAD_CONST              19 (None)
        # |                RETURN_VALUE

    def test_byte_stable_across_calls(self, lib):
        '同样的输入必须产出同样的字节 —— 否则缓存前缀每次都变。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  44           RESUME                   0
        # |  46           LOAD_FAST_BORROW         1 (lib)
        # |               LOAD_ATTR                0 (compose)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               1 ('a')
        # |               LOAD_CONST               2 ('b')
        # |               BUILD_LIST               2
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    65 (@py_assert5, lib)
        # |               LOAD_ATTR                0 (compose)
        # |               STORE_FAST               5 (@py_assert9)
        # |               LOAD_CONST               1 ('a')
        # |               LOAD_CONST               2 ('b')
        # |               BUILD_LIST               2
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert9)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert11)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   116 (@py_assert13, @py_assert5)
        # |               LOAD_FAST_BORROW         7 (@py_assert13)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       365 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('==',))
        # |               LOAD_FAST_BORROW         8 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.compose\n}(%(py4)s)\n} == %(py14)s\n{%(py14)s = %(py10)s\n{%(py10)s = %(py8)s.compose\n}(%(py12)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert5, @py_assert13)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('lib')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('lib')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py8')
        # |               LOAD_CONST               4 ('lib')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               4 ('lib')
        # |       L6:     LOAD_CONST               9 ('py10')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert9)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py12')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert11)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py14')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert13)
        # |               CALL                     1
        # |               BUILD_MAP                8
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format15)
        # |               LOAD_CONST              12 ('assert %(py16)s')
        # |               LOAD_CONST              13 ('py16')
        # |               LOAD_FAST_BORROW         9 (@py_format15)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format17)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format17)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              14 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert9)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  103 (@py_assert11, @py_assert13)
        # |               LOAD_CONST              14 (None)
        # |               RETURN_VALUE

    def test_order_change_changes_bytes(self, lib):
        '反过来说，顺序变了字节就该变 —— 提醒调用方顺序是有代价的。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  48           RESUME                   0
        # |  50           LOAD_FAST_BORROW         1 (lib)
        # |               LOAD_ATTR                0 (compose)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               1 ('a')
        # |               LOAD_CONST               2 ('b')
        # |               BUILD_LIST               2
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    65 (@py_assert5, lib)
        # |               LOAD_ATTR                0 (compose)
        # |               STORE_FAST               5 (@py_assert9)
        # |               LOAD_CONST               2 ('b')
        # |               LOAD_CONST               1 ('a')
        # |               BUILD_LIST               2
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert9)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert11)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   116 (@py_assert13, @py_assert5)
        # |               LOAD_FAST_BORROW         7 (@py_assert13)
        # |               COMPARE_OP             103 (!=)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       365 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('!=',))
        # |               LOAD_FAST_BORROW         8 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.compose\n}(%(py4)s)\n} != %(py14)s\n{%(py14)s = %(py10)s\n{%(py10)s = %(py8)s.compose\n}(%(py12)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert5, @py_assert13)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('lib')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('lib')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py8')
        # |               LOAD_CONST               4 ('lib')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               4 ('lib')
        # |       L6:     LOAD_CONST               9 ('py10')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert9)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py12')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert11)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py14')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert13)
        # |               CALL                     1
        # |               BUILD_MAP                8
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format15)
        # |               LOAD_CONST              12 ('assert %(py16)s')
        # |               LOAD_CONST              13 ('py16')
        # |               LOAD_FAST_BORROW         9 (@py_format15)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format17)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format17)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              14 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert9)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  103 (@py_assert11, @py_assert13)
        # |               LOAD_CONST              14 (None)
        # |               RETURN_VALUE

    def test_strict_by_default(self, lib):
        'a'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   52           RESUME                   0
        # |   53           LOAD_GLOBAL              0 (pytest)
        # |                LOAD_ATTR                2 (raises)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (SkillNotFound)
        # |                CALL                     1
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     POP_TOP
        # |   54           LOAD_FAST_BORROW         1 (lib)
        # |                LOAD_ATTR                7 (compose + NULL|self)
        # |                LOAD_CONST               0 ('a')
        # |                LOAD_CONST               1 ('missing')
        # |                BUILD_LIST               2
        # |                CALL                     1
        # |                POP_TOP
        # |   53   L2:     LOAD_CONST               2 (None)
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

    def test_lenient_skips_missing(self, lib):
        '语料未到位时，部分 skill 尚未萃取，要能先跑起来。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  56           RESUME                   0
        # |  58           LOAD_FAST_BORROW         1 (lib)
        # |               LOAD_ATTR                0 (compose)
        # |               STORE_FAST               2 (@py_assert1)
        # |               BUILD_LIST               0
        # |               LOAD_CONST              18 (('a', 'missing', 'b'))
        # |               LIST_EXTEND              1
        # |               STORE_FAST               3 (@py_assert3)
        # |               LOAD_CONST               3 (False)
        # |               STORE_FAST_LOAD_FAST    66 (@py_assert5, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               4 (('strict',))
        # |               CALL_KW                  2
        # |               STORE_FAST_LOAD_FAST    81 (@py_assert7, lib)
        # |               LOAD_ATTR                0 (compose)
        # |               STORE_FAST               6 (@py_assert11)
        # |               LOAD_CONST               1 ('a')
        # |               LOAD_CONST               2 ('b')
        # |               BUILD_LIST               2
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert13, @py_assert11)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert13)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   133 (@py_assert15, @py_assert7)
        # |               LOAD_FAST_BORROW         8 (@py_assert15)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert9, @py_assert9)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       387 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              19 (('==',))
        # |               LOAD_FAST_BORROW         9 (@py_assert9)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              20 (('%(py8)s\n{%(py8)s = %(py2)s\n{%(py2)s = %(py0)s.compose\n}(%(py4)s, strict=%(py6)s)\n} == %(py16)s\n{%(py16)s = %(py12)s\n{%(py12)s = %(py10)s.compose\n}(%(py14)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 88 (@py_assert7, @py_assert15)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST               6 ('lib')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               6 ('lib')
        # |       L3:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py6')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py8')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert7)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py10')
        # |               LOAD_CONST               6 ('lib')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               6 ('lib')
        # |       L6:     LOAD_CONST              12 ('py12')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert11)
        # |               CALL                     1
        # |               LOAD_CONST              13 ('py14')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert13)
        # |               CALL                     1
        # |               LOAD_CONST              14 ('py16')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert15)
        # |               CALL                     1
        # |               BUILD_MAP                9
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format17)
        # |               LOAD_CONST              15 ('assert %(py18)s')
        # |               LOAD_CONST              16 ('py18')
        # |               LOAD_FAST_BORROW        10 (@py_format17)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format19)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format19)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              17 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert9)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert11)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert13, @py_assert15)
        # |               LOAD_CONST              17 (None)
        # |               RETURN_VALUE


class TestRealSkills:
    'TestRealSkills'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  61           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestRealSkills')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          61
    # |               STORE_NAME               3 (__firstlineno__)
    # |  62           LOAD_CONST               1 (<code object test_written_skills_load at 0x7504d8b200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 62>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_written_skills_load)
    # |  67           LOAD_CONST               2 (<code object test_format_spec_matches_config at 0x75052c9c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 67>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_format_spec_matches_config)
    # |  81           LOAD_CONST               3 (<code object test_intimacy_levels_covers_all_configured_levels at 0x75052eca80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 81>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_intimacy_levels_covers_all_configured_levels)
    # |  86           LOAD_CONST               4 (<code object test_every_referenced_skill_exists_somewhere at 0x75052ece00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 86>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_every_referenced_skill_exists_somewhere)
    # |  95           LOAD_CONST               5 (<code object test_lenient_compose_works_today at 0x7504d8b700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 95>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_lenient_compose_works_today)
    # | 100           LOAD_CONST               6 (<code object test_design_time_skills_kept_out_of_writer at 0x7505097000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 100>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_design_time_skills_kept_out_of_writer)
    # | 110           LOAD_CONST               7 (<code object test_writer_keeps_the_craft_skills at 0x75052ed180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 110>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_writer_keeps_the_craft_skills)
    # | 114           LOAD_CONST               8 (<code object test_format_spec_is_last at 0x7504d72080, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 114>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              11 (test_format_spec_is_last)
    # |               LOAD_CONST               9 (())
    # |               STORE_NAME              12 (__static_attributes__)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_written_skills_load at 0x7504d8b200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 62>:
    # |  62           RESUME                   0
    # |  63           LOAD_GLOBAL              1 (SkillLibrary + NULL)
    # |               LOAD_GLOBAL              2 (REAL_SKILLS)
    # |               CALL                     1
    # |               STORE_FAST               1 (lib)
    # |  64           LOAD_CONST               0 ('format_spec')
    # |               STORE_FAST_LOAD_FAST    33 (@py_assert0, lib)
    # |               LOAD_ATTR                4 (available)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       221 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('in',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.available\n}()\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               2 ('py3')
    # |               LOAD_CONST               3 ('lib')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('lib')
    # |       L3:     LOAD_CONST               4 ('py5')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py7')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_CONST               6 ('assert %(py9)s')
    # |               LOAD_CONST               7 ('py9')
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format10)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
    # |  65           LOAD_CONST               9 ('intimacy_levels')
    # |               STORE_FAST_LOAD_FAST    33 (@py_assert0, lib)
    # |               LOAD_ATTR                4 (available)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       221 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('in',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.available\n}()\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               2 ('py3')
    # |               LOAD_CONST               3 ('lib')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (lib)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               3 ('lib')
    # |       L7:     LOAD_CONST               4 ('py5')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py7')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_CONST               6 ('assert %(py9)s')
    # |               LOAD_CONST               7 ('py9')
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format10)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_format_spec_matches_config at 0x75052c9c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 67>:
    # |  67            RESUME                   0
    # |  69            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (None)
    # |                IMPORT_NAME              0 (yaml)
    # |                STORE_FAST               1 (yaml)
    # |  71            LOAD_FAST_BORROW         1 (yaml)
    # |                LOAD_ATTR                3 (safe_load + NULL|self)
    # |  72            LOAD_GLOBAL              4 (REAL_SKILLS)
    # |                LOAD_ATTR                6 (parent)
    # |                LOAD_CONST               2 ('config')
    # |                BINARY_OP               11 (/)
    # |                LOAD_CONST               3 ('project.yaml')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR                9 (read_text + NULL|self)
    # |                LOAD_CONST               4 ('utf-8')
    # |                CALL                     1
    # |  71            CALL                     1
    # |                STORE_FAST               2 (cfg)
    # |  74            LOAD_GLOBAL             11 (SkillLibrary + NULL)
    # |                LOAD_GLOBAL              4 (REAL_SKILLS)
    # |                CALL                     1
    # |                LOAD_ATTR               13 (load + NULL|self)
    # |                LOAD_CONST               5 ('format_spec')
    # |                CALL                     1
    # |                STORE_FAST               3 (text)
    # |  75            LOAD_FAST_BORROW         2 (cfg)
    # |                LOAD_CONST               6 ('length')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST               7 ('chapter_min')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_GLOBAL             15 (str + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       285 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              25 (('in',))
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              26 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} in %(py6)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (@py_assert3, text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py0')
    # |                LOAD_CONST               9 ('str')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (str)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (str)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               9 ('str')
    # |        L3:     LOAD_CONST              10 ('py2')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py4')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py6')
    # |                LOAD_CONST              13 ('text')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST              13 ('text')
    # |        L6:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format7)
    # |                LOAD_CONST              14 ('assert %(py8)s')
    # |                LOAD_CONST              15 ('py8')
    # |                LOAD_FAST_BORROW         7 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format9)
    # |                LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               30 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert3, @py_assert5)
    # |  76            LOAD_FAST_BORROW         2 (cfg)
    # |                LOAD_CONST               6 ('length')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              16 ('chapter_max')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_GLOBAL             15 (str + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       285 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              25 (('in',))
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              26 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} in %(py6)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (@py_assert3, text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py0')
    # |                LOAD_CONST               9 ('str')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (str)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (str)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               9 ('str')
    # |       L10:     LOAD_CONST              10 ('py2')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py4')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py6')
    # |                LOAD_CONST              13 ('text')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L12)
    # |                NOT_TAKEN
    # |       L11:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L13)
    # |       L12:     LOAD_CONST              13 ('text')
    # |       L13:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format7)
    # |                LOAD_CONST              14 ('assert %(py8)s')
    # |                LOAD_CONST              15 ('py8')
    # |                LOAD_FAST_BORROW         7 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format9)
    # |                LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               30 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L14:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert3, @py_assert5)
    # |  77            LOAD_FAST_BORROW         2 (cfg)
    # |                LOAD_CONST               6 ('length')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              17 ('paragraph_max_chars')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_GLOBAL             15 (str + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       285 (to L21)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              25 (('in',))
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              26 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} in %(py6)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (@py_assert3, text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py0')
    # |                LOAD_CONST               9 ('str')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L15)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (str)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L16)
    # |                NOT_TAKEN
    # |       L15:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             14 (str)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L17)
    # |       L16:     LOAD_CONST               9 ('str')
    # |       L17:     LOAD_CONST              10 ('py2')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py4')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py6')
    # |                LOAD_CONST              13 ('text')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L18)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L19)
    # |                NOT_TAKEN
    # |       L18:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L20)
    # |       L19:     LOAD_CONST              13 ('text')
    # |       L20:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format7)
    # |                LOAD_CONST              14 ('assert %(py8)s')
    # |                LOAD_CONST              15 ('py8')
    # |                LOAD_FAST_BORROW         7 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format9)
    # |                LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               30 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L21:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert3, @py_assert5)
    # |  78            LOAD_FAST_BORROW         2 (cfg)
    # |                LOAD_CONST               6 ('length')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              18 ('dialogue_ratio_min')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              19 ('.0%')
    # |                FORMAT_WITH_SPEC
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       177 (to L25)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              25 (('in',))
    # |                LOAD_FAST_BORROW        10 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              27 (('%(py1)s in %(py3)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (@py_assert0, text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              20 ('py1')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              21 ('py3')
    # |                LOAD_CONST              13 ('text')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L22)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L23)
    # |                NOT_TAKEN
    # |       L22:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L24)
    # |       L23:     LOAD_CONST              13 ('text')
    # |       L24:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format4)
    # |                LOAD_CONST              22 ('assert %(py5)s')
    # |                LOAD_CONST              23 ('py5')
    # |                LOAD_FAST_BORROW        11 (@py_format4)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format6)
    # |                LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               30 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format6)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L25:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  154 (@py_assert0, @py_assert2)
    # |  79            LOAD_FAST_BORROW         2 (cfg)
    # |                LOAD_CONST               6 ('length')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              24 ('dialogue_ratio_max')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              19 ('.0%')
    # |                FORMAT_WITH_SPEC
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       177 (to L29)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              25 (('in',))
    # |                LOAD_FAST_BORROW        10 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              27 (('%(py1)s in %(py3)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (@py_assert0, text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              20 ('py1')
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              21 ('py3')
    # |                LOAD_CONST              13 ('text')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L26)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L27)
    # |                NOT_TAKEN
    # |       L26:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L28)
    # |       L27:     LOAD_CONST              13 ('text')
    # |       L28:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format4)
    # |                LOAD_CONST              22 ('assert %(py5)s')
    # |                LOAD_CONST              23 ('py5')
    # |                LOAD_FAST_BORROW        11 (@py_format4)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format6)
    # |                LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               30 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_format6)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L29:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  154 (@py_assert0, @py_assert2)
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_intimacy_levels_covers_all_configured_levels at 0x75052eca80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 81>:
    # |  81           RESUME                   0
    # |  82           LOAD_GLOBAL              1 (SkillLibrary + NULL)
    # |               LOAD_GLOBAL              2 (REAL_SKILLS)
    # |               CALL                     1
    # |               LOAD_ATTR                5 (load + NULL|self)
    # |               LOAD_CONST               0 ('intimacy_levels')
    # |               CALL                     1
    # |               STORE_FAST               1 (text)
    # |  83           LOAD_CONST               8 (('L0', 'L1', 'L2'))
    # |               GET_ITER
    # |       L1:     FOR_ITER               248 (to L9)
    # |               STORE_FAST               2 (level)
    # |  84           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (level, text)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       233 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 (('in',))
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              10 (('%(py0)s in %(py2)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (level, text)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('level')
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
    # |               LOAD_FAST_BORROW         2 (level)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (level)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               2 ('level')
    # |       L4:     LOAD_CONST               3 ('py2')
    # |               LOAD_CONST               4 ('text')
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
    # |               LOAD_FAST_BORROW         1 (text)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (text)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               4 ('text')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               4 (@py_format3)
    # |               LOAD_CONST               5 ('assert %(py4)s')
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_FAST_BORROW         4 (@py_format3)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               7 (None)
    # |               STORE_FAST               3 (@py_assert1)
    # |               JUMP_BACKWARD          250 (to L1)
    # |  83   L9:     END_FOR
    # |               POP_ITER
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_every_referenced_skill_exists_somewhere at 0x75052ece00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 86>:
    # |   86           RESUME                   0
    # |   89           LOAD_GLOBAL              1 (SkillLibrary + NULL)
    # |                LOAD_GLOBAL              2 (REAL_SKILLS)
    # |                CALL                     1
    # |                STORE_FAST               1 (lib)
    # |   90           LOAD_GLOBAL              2 (REAL_SKILLS)
    # |                LOAD_CONST               1 ('_drafts')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR                5 (glob + NULL|self)
    # |                LOAD_CONST               2 ('*.md')
    # |                CALL                     1
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      2 (p)
    # |                SWAP                     2
    # |        L1:     BUILD_SET                0
    # |                SWAP                     2
    # |        L2:     FOR_ITER                14 (to L3)
    # |                STORE_FAST_LOAD_FAST    34 (p, p)
    # |                LOAD_ATTR                6 (stem)
    # |                SET_ADD                  2
    # |                JUMP_BACKWARD           16 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |        L4:     STORE_FAST               3 (drafts)
    # |                STORE_FAST               2 (p)
    # |   91           LOAD_GLOBAL              9 (set + NULL)
    # |                LOAD_FAST_BORROW         1 (lib)
    # |                LOAD_ATTR               11 (available + NULL|self)
    # |                CALL                     0
    # |                CALL                     1
    # |                LOAD_FAST_BORROW         3 (drafts)
    # |                BINARY_OP                7 (|)
    # |                STORE_FAST               4 (have)
    # |   92           LOAD_GLOBAL              9 (set + NULL)
    # |                LOAD_GLOBAL             12 (WRITER_SKILLS)
    # |                CALL                     1
    # |                LOAD_GLOBAL              9 (set + NULL)
    # |                LOAD_GLOBAL             14 (ARCHITECT_SKILLS)
    # |                CALL                     1
    # |                BINARY_OP                7 (|)
    # |                LOAD_FAST_BORROW         4 (have)
    # |                BINARY_OP               10 (-)
    # |                STORE_FAST               5 (missing)
    # |   93           LOAD_FAST_BORROW         5 (missing)
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       149 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST               3 ('引用了不存在的 skill：')
    # |                LOAD_FAST_BORROW         5 (missing)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                LOAD_CONST               4 ('\n>assert not %(py0)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('missing')
    # |                LOAD_GLOBAL             20 (@py_builtins)
    # |                LOAD_ATTR               22 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (missing)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (missing)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               6 ('missing')
    # |        L7:     BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format2)
    # |                LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                LOAD_GLOBAL             16 (@pytest_ar)
    # |                LOAD_ATTR               30 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format2)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST               7 (None)
    # |                STORE_FAST               6 (@py_assert1)
    # |                LOAD_CONST               7 (None)
    # |                RETURN_VALUE
    # |   --   L9:     SWAP                     2
    # |                POP_TOP
    # |   90           SWAP                     2
    # |                STORE_FAST               2 (p)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L9 [2]
    # | Disassembly of <code object test_lenient_compose_works_today at 0x7504d8b700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 95>:
    # |  95           RESUME                   0
    # |  97           LOAD_GLOBAL              1 (SkillLibrary + NULL)
    # |               LOAD_GLOBAL              2 (REAL_SKILLS)
    # |               CALL                     1
    # |               LOAD_ATTR                5 (compose + NULL|self)
    # |               LOAD_GLOBAL              6 (WRITER_SKILLS)
    # |               LOAD_CONST               1 (False)
    # |               LOAD_CONST               2 (('strict',))
    # |               CALL_KW                  2
    # |               STORE_FAST               1 (out)
    # |  98           BUILD_LIST               0
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               3 ('格式硬规范')
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
    # |               LOAD_FAST_BORROW         1 (out)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert0, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE        8 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_CONST               4 ('亲密尺度分档')
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert9, @py_assert9)
    # |               LOAD_FAST_BORROW         1 (out)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert11, @py_assert11)
    # |               STORE_FAST               5 (@py_assert0)
    # |       L1:     LOAD_FAST_BORROW         5 (@py_assert0)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       404 (to L9)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('in',))
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py3)s in %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (@py_assert2, out)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               5 ('py3')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py5')
    # |               LOAD_CONST               7 ('out')
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
    # |               LOAD_FAST_BORROW         1 (out)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (out)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               7 ('out')
    # |       L4:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format6)
    # |               LOAD_CONST               8 ('%(py7)s')
    # |               LOAD_CONST               9 ('py7')
    # |               LOAD_FAST_BORROW         8 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   146 (@py_format8, @py_assert1)
    # |               LOAD_ATTR               21 (append + NULL|self)
    # |               LOAD_FAST_BORROW         9 (@py_format8)
    # |               CALL                     1
    # |               POP_TOP
    # |               LOAD_FAST_BORROW         4 (@py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE      163 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('in',))
    # |               LOAD_FAST_CHECK          7 (@py_assert11)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              19 (('%(py10)s in %(py12)s',))
    # |               LOAD_FAST_CHECK          6 (@py_assert9)
    # |               LOAD_FAST_BORROW         1 (out)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              10 ('py10')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert9)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py12')
    # |               LOAD_CONST               7 ('out')
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
    # |               LOAD_FAST_BORROW         1 (out)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (out)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               7 ('out')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format13)
    # |               LOAD_CONST              12 ('%(py14)s')
    # |               LOAD_CONST              13 ('py14')
    # |               LOAD_FAST_BORROW        10 (@py_format13)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   178 (@py_format15, @py_assert1)
    # |               LOAD_ATTR               21 (append + NULL|self)
    # |               LOAD_FAST_BORROW        11 (@py_format15)
    # |               CALL                     1
    # |               POP_TOP
    # |       L8:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_boolop)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BUILD_MAP                0
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format16)
    # |               LOAD_CONST              14 ('assert %(py17)s')
    # |               LOAD_CONST              15 ('py17')
    # |               LOAD_FAST_BORROW        12 (@py_format16)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format18)
    # |               LOAD_GLOBAL             25 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               26 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        13 (@py_format18)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L9:     LOAD_CONST              16 (None)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  103 (@py_assert9, @py_assert11)
    # |               LOAD_CONST              16 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_design_time_skills_kept_out_of_writer at 0x7505097000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 100>:
    # | 100            RESUME                   0
    # | 106            BUILD_SET                0
    # |                LOAD_CONST              17 (frozenset({'romance_beats', 'character_design', 'campus_to_career'}))
    # |                SET_UPDATE               1
    # |                STORE_FAST               1 (design_time)
    # | 107            LOAD_GLOBAL              1 (set + NULL)
    # |                LOAD_GLOBAL              2 (WRITER_SKILLS)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    33 (@py_assert3, design_time)
    # |                LOAD_FAST_BORROW         2 (@py_assert3)
    # |                BINARY_OP                1 (&)
    # |                STORE_FAST               3 (@py_assert5)
    # |                LOAD_GLOBAL              1 (set + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert8, @py_assert5)
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       457 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              18 (('==',))
    # |                LOAD_FAST_BORROW         5 (@py_assert6)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('(%(py0)s & %(py4)s\n{%(py4)s = %(py1)s(%(py2)s)\n}) == %(py9)s\n{%(py9)s = %(py7)s()\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert5, @py_assert8)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('design_time')
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
    # |                LOAD_FAST_BORROW         1 (design_time)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (design_time)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               2 ('design_time')
    # |        L3:     LOAD_CONST               3 ('py1')
    # |                LOAD_CONST               4 ('set')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (set)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (set)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               4 ('set')
    # |        L6:     LOAD_CONST               5 ('py2')
    # |                LOAD_CONST               6 ('WRITER_SKILLS')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (WRITER_SKILLS)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (WRITER_SKILLS)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               6 ('WRITER_SKILLS')
    # |        L9:     LOAD_CONST               7 ('py4')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_CONST               4 ('set')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (set)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (set)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST               4 ('set')
    # |       L12:     LOAD_CONST               9 ('py9')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                CALL                     1
    # |                BUILD_MAP                6
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format10)
    # |                LOAD_CONST              10 ('assert %(py11)s')
    # |                LOAD_CONST              11 ('py11')
    # |                LOAD_FAST_BORROW         6 (@py_format10)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format12)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format12)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L13:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   84 (@py_assert6, @py_assert8)
    # | 108            LOAD_GLOBAL              1 (set + NULL)
    # |                LOAD_GLOBAL             20 (ARCHITECT_SKILLS)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   129 (@py_assert4, design_time)
    # |                LOAD_FAST_BORROW         8 (@py_assert4)
    # |                COMPARE_OP              42 (<=)
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       349 (to L23)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              20 (('<=',))
    # |                LOAD_FAST_BORROW         9 (@py_assert1)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              21 (('%(py0)s <= %(py5)s\n{%(py5)s = %(py2)s(%(py3)s)\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 24 (design_time, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('design_time')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (design_time)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L15)
    # |                NOT_TAKEN
    # |       L14:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (design_time)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L16)
    # |       L15:     LOAD_CONST               2 ('design_time')
    # |       L16:     LOAD_CONST               5 ('py2')
    # |                LOAD_CONST               4 ('set')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L17)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (set)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L18)
    # |                NOT_TAKEN
    # |       L17:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (set)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L19)
    # |       L18:     LOAD_CONST               4 ('set')
    # |       L19:     LOAD_CONST              13 ('py3')
    # |                LOAD_CONST              14 ('ARCHITECT_SKILLS')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L20)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             20 (ARCHITECT_SKILLS)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L21)
    # |                NOT_TAKEN
    # |       L20:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             20 (ARCHITECT_SKILLS)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L22)
    # |       L21:     LOAD_CONST              14 ('ARCHITECT_SKILLS')
    # |       L22:     LOAD_CONST              15 ('py5')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format6)
    # |                LOAD_CONST              16 ('assert %(py7)s')
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_FAST_BORROW        10 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format8)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L23:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  152 (@py_assert1, @py_assert4)
    # |                LOAD_CONST              12 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_writer_keeps_the_craft_skills at 0x75052ed180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 110>:
    # | 110           RESUME                   0
    # | 112           BUILD_SET                0
    # |               LOAD_CONST              10 (frozenset({'dialogue', 'style_voice', 'format_spec'}))
    # |               SET_UPDATE               1
    # |               STORE_FAST               1 (@py_assert0)
    # |               LOAD_GLOBAL              1 (set + NULL)
    # |               LOAD_GLOBAL              2 (WRITER_SKILLS)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    33 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         2 (@py_assert5)
    # |               COMPARE_OP              42 (<=)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       293 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('<=',))
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py1)s <= %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               2 ('py3')
    # |               LOAD_CONST               3 ('set')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (set)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (set)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('set')
    # |       L3:     LOAD_CONST               4 ('py4')
    # |               LOAD_CONST               5 ('WRITER_SKILLS')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              2 (WRITER_SKILLS)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              2 (WRITER_SKILLS)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               5 ('WRITER_SKILLS')
    # |       L6:     LOAD_CONST               6 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               4 (@py_format7)
    # |               LOAD_CONST               7 ('assert %(py8)s')
    # |               LOAD_CONST               8 ('py8')
    # |               LOAD_FAST_BORROW         4 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format9)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   50 (@py_assert2, @py_assert5)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_format_spec_is_last at 0x7504d72080, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_skills.py", line 114>:
    # | 114           RESUME                   0
    # | 116           LOAD_GLOBAL              0 (WRITER_SKILLS)
    # |               LOAD_CONST               7 (-1)
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               1 (@py_assert0)
    # |               LOAD_CONST               1 ('format_spec')
    # |               STORE_FAST_LOAD_FAST    33 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         2 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 (('==',))
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               9 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               4 (@py_format5)
    # |               LOAD_CONST               4 ('assert %(py6)s')
    # |               LOAD_CONST               5 ('py6')
    # |               LOAD_FAST_BORROW         4 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format7)
    # |               LOAD_GLOBAL              9 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   50 (@py_assert2, @py_assert3)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE

    def test_written_skills_load(self):
        'format_spec'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  62           RESUME                   0
        # |  63           LOAD_GLOBAL              1 (SkillLibrary + NULL)
        # |               LOAD_GLOBAL              2 (REAL_SKILLS)
        # |               CALL                     1
        # |               STORE_FAST               1 (lib)
        # |  64           LOAD_CONST               0 ('format_spec')
        # |               STORE_FAST_LOAD_FAST    33 (@py_assert0, lib)
        # |               LOAD_ATTR                4 (available)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       221 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('in',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.available\n}()\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               2 ('py3')
        # |               LOAD_CONST               3 ('lib')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('lib')
        # |       L3:     LOAD_CONST               4 ('py5')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py7')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_CONST               6 ('assert %(py9)s')
        # |               LOAD_CONST               7 ('py9')
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format10)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
        # |  65           LOAD_CONST               9 ('intimacy_levels')
        # |               STORE_FAST_LOAD_FAST    33 (@py_assert0, lib)
        # |               LOAD_ATTR                4 (available)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       221 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('in',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.available\n}()\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               2 ('py3')
        # |               LOAD_CONST               3 ('lib')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (lib)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               3 ('lib')
        # |       L7:     LOAD_CONST               4 ('py5')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py7')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_CONST               6 ('assert %(py9)s')
        # |               LOAD_CONST               7 ('py9')
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format10)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE

    def test_format_spec_matches_config(self):
        'skills 里写给模型看的规范，必须和 gate 实际执行的一致。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  67            RESUME                   0
        # |  69            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (None)
        # |                IMPORT_NAME              0 (yaml)
        # |                STORE_FAST               1 (yaml)
        # |  71            LOAD_FAST_BORROW         1 (yaml)
        # |                LOAD_ATTR                3 (safe_load + NULL|self)
        # |  72            LOAD_GLOBAL              4 (REAL_SKILLS)
        # |                LOAD_ATTR                6 (parent)
        # |                LOAD_CONST               2 ('config')
        # |                BINARY_OP               11 (/)
        # |                LOAD_CONST               3 ('project.yaml')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR                9 (read_text + NULL|self)
        # |                LOAD_CONST               4 ('utf-8')
        # |                CALL                     1
        # |  71            CALL                     1
        # |                STORE_FAST               2 (cfg)
        # |  74            LOAD_GLOBAL             11 (SkillLibrary + NULL)
        # |                LOAD_GLOBAL              4 (REAL_SKILLS)
        # |                CALL                     1
        # |                LOAD_ATTR               13 (load + NULL|self)
        # |                LOAD_CONST               5 ('format_spec')
        # |                CALL                     1
        # |                STORE_FAST               3 (text)
        # |  75            LOAD_FAST_BORROW         2 (cfg)
        # |                LOAD_CONST               6 ('length')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST               7 ('chapter_min')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_GLOBAL             15 (str + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       285 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              25 (('in',))
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              26 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} in %(py6)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (@py_assert3, text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py0')
        # |                LOAD_CONST               9 ('str')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (str)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (str)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               9 ('str')
        # |        L3:     LOAD_CONST              10 ('py2')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py4')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py6')
        # |                LOAD_CONST              13 ('text')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST              13 ('text')
        # |        L6:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format7)
        # |                LOAD_CONST              14 ('assert %(py8)s')
        # |                LOAD_CONST              15 ('py8')
        # |                LOAD_FAST_BORROW         7 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format9)
        # |                LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               30 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format9)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert3, @py_assert5)
        # |  76            LOAD_FAST_BORROW         2 (cfg)
        # |                LOAD_CONST               6 ('length')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              16 ('chapter_max')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_GLOBAL             15 (str + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       285 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              25 (('in',))
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              26 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} in %(py6)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (@py_assert3, text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py0')
        # |                LOAD_CONST               9 ('str')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (str)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (str)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               9 ('str')
        # |       L10:     LOAD_CONST              10 ('py2')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py4')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py6')
        # |                LOAD_CONST              13 ('text')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L12)
        # |                NOT_TAKEN
        # |       L11:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L13)
        # |       L12:     LOAD_CONST              13 ('text')
        # |       L13:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format7)
        # |                LOAD_CONST              14 ('assert %(py8)s')
        # |                LOAD_CONST              15 ('py8')
        # |                LOAD_FAST_BORROW         7 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format9)
        # |                LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               30 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format9)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L14:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert3, @py_assert5)
        # |  77            LOAD_FAST_BORROW         2 (cfg)
        # |                LOAD_CONST               6 ('length')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              17 ('paragraph_max_chars')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_GLOBAL             15 (str + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       285 (to L21)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              25 (('in',))
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              26 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} in %(py6)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 83 (@py_assert3, text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py0')
        # |                LOAD_CONST               9 ('str')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L15)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (str)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L16)
        # |                NOT_TAKEN
        # |       L15:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             14 (str)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L17)
        # |       L16:     LOAD_CONST               9 ('str')
        # |       L17:     LOAD_CONST              10 ('py2')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py4')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py6')
        # |                LOAD_CONST              13 ('text')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L18)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L19)
        # |                NOT_TAKEN
        # |       L18:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L20)
        # |       L19:     LOAD_CONST              13 ('text')
        # |       L20:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format7)
        # |                LOAD_CONST              14 ('assert %(py8)s')
        # |                LOAD_CONST              15 ('py8')
        # |                LOAD_FAST_BORROW         7 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format9)
        # |                LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               30 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format9)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L21:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert3, @py_assert5)
        # |  78            LOAD_FAST_BORROW         2 (cfg)
        # |                LOAD_CONST               6 ('length')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              18 ('dialogue_ratio_min')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              19 ('.0%')
        # |                FORMAT_WITH_SPEC
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       177 (to L25)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              25 (('in',))
        # |                LOAD_FAST_BORROW        10 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              27 (('%(py1)s in %(py3)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (@py_assert0, text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              20 ('py1')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              21 ('py3')
        # |                LOAD_CONST              13 ('text')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L22)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L23)
        # |                NOT_TAKEN
        # |       L22:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L24)
        # |       L23:     LOAD_CONST              13 ('text')
        # |       L24:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format4)
        # |                LOAD_CONST              22 ('assert %(py5)s')
        # |                LOAD_CONST              23 ('py5')
        # |                LOAD_FAST_BORROW        11 (@py_format4)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format6)
        # |                LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               30 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format6)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L25:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  154 (@py_assert0, @py_assert2)
        # |  79            LOAD_FAST_BORROW         2 (cfg)
        # |                LOAD_CONST               6 ('length')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              24 ('dialogue_ratio_max')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              19 ('.0%')
        # |                FORMAT_WITH_SPEC
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert0, @py_assert0)
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       177 (to L29)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              25 (('in',))
        # |                LOAD_FAST_BORROW        10 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              27 (('%(py1)s in %(py3)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 147 (@py_assert0, text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              20 ('py1')
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              21 ('py3')
        # |                LOAD_CONST              13 ('text')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L26)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L27)
        # |                NOT_TAKEN
        # |       L26:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L28)
        # |       L27:     LOAD_CONST              13 ('text')
        # |       L28:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format4)
        # |                LOAD_CONST              22 ('assert %(py5)s')
        # |                LOAD_CONST              23 ('py5')
        # |                LOAD_FAST_BORROW        11 (@py_format4)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format6)
        # |                LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               30 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_format6)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L29:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  154 (@py_assert0, @py_assert2)
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE

    def test_intimacy_levels_covers_all_configured_levels(self):
        'intimacy_levels'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  81           RESUME                   0
        # |  82           LOAD_GLOBAL              1 (SkillLibrary + NULL)
        # |               LOAD_GLOBAL              2 (REAL_SKILLS)
        # |               CALL                     1
        # |               LOAD_ATTR                5 (load + NULL|self)
        # |               LOAD_CONST               0 ('intimacy_levels')
        # |               CALL                     1
        # |               STORE_FAST               1 (text)
        # |  83           LOAD_CONST               8 (('L0', 'L1', 'L2'))
        # |               GET_ITER
        # |       L1:     FOR_ITER               248 (to L9)
        # |               STORE_FAST               2 (level)
        # |  84           LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (level, text)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       233 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 (('in',))
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              10 (('%(py0)s in %(py2)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (level, text)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('level')
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
        # |               LOAD_FAST_BORROW         2 (level)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (level)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               2 ('level')
        # |       L4:     LOAD_CONST               3 ('py2')
        # |               LOAD_CONST               4 ('text')
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
        # |               LOAD_FAST_BORROW         1 (text)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (text)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               4 ('text')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               4 (@py_format3)
        # |               LOAD_CONST               5 ('assert %(py4)s')
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_FAST_BORROW         4 (@py_format3)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               7 (None)
        # |               STORE_FAST               3 (@py_assert1)
        # |               JUMP_BACKWARD          250 (to L1)
        # |  83   L9:     END_FOR
        # |               POP_ITER
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_every_referenced_skill_exists_somewhere(self):
        '引用的 skill 要么已在 skills/，要么还在 _drafts/ 待审。\n出现第三种情况就是名字拼错了。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   86           RESUME                   0
        # |   89           LOAD_GLOBAL              1 (SkillLibrary + NULL)
        # |                LOAD_GLOBAL              2 (REAL_SKILLS)
        # |                CALL                     1
        # |                STORE_FAST               1 (lib)
        # |   90           LOAD_GLOBAL              2 (REAL_SKILLS)
        # |                LOAD_CONST               1 ('_drafts')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR                5 (glob + NULL|self)
        # |                LOAD_CONST               2 ('*.md')
        # |                CALL                     1
        # |                GET_ITER
        # |                LOAD_FAST_AND_CLEAR      2 (p)
        # |                SWAP                     2
        # |        L1:     BUILD_SET                0
        # |                SWAP                     2
        # |        L2:     FOR_ITER                14 (to L3)
        # |                STORE_FAST_LOAD_FAST    34 (p, p)
        # |                LOAD_ATTR                6 (stem)
        # |                SET_ADD                  2
        # |                JUMP_BACKWARD           16 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |        L4:     STORE_FAST               3 (drafts)
        # |                STORE_FAST               2 (p)
        # |   91           LOAD_GLOBAL              9 (set + NULL)
        # |                LOAD_FAST_BORROW         1 (lib)
        # |                LOAD_ATTR               11 (available + NULL|self)
        # |                CALL                     0
        # |                CALL                     1
        # |                LOAD_FAST_BORROW         3 (drafts)
        # |                BINARY_OP                7 (|)
        # |                STORE_FAST               4 (have)
        # |   92           LOAD_GLOBAL              9 (set + NULL)
        # |                LOAD_GLOBAL             12 (WRITER_SKILLS)
        # |                CALL                     1
        # |                LOAD_GLOBAL              9 (set + NULL)
        # |                LOAD_GLOBAL             14 (ARCHITECT_SKILLS)
        # |                CALL                     1
        # |                BINARY_OP                7 (|)
        # |                LOAD_FAST_BORROW         4 (have)
        # |                BINARY_OP               10 (-)
        # |                STORE_FAST               5 (missing)
        # |   93           LOAD_FAST_BORROW         5 (missing)
        # |                TO_BOOL
        # |                UNARY_NOT
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       149 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST               3 ('引用了不存在的 skill：')
        # |                LOAD_FAST_BORROW         5 (missing)
        # |                FORMAT_SIMPLE
        # |                BUILD_STRING             2
        # |                CALL                     1
        # |                LOAD_CONST               4 ('\n>assert not %(py0)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('missing')
        # |                LOAD_GLOBAL             20 (@py_builtins)
        # |                LOAD_ATTR               22 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (missing)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (missing)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               6 ('missing')
        # |        L7:     BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format2)
        # |                LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                LOAD_GLOBAL             16 (@pytest_ar)
        # |                LOAD_ATTR               30 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format2)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST               7 (None)
        # |                STORE_FAST               6 (@py_assert1)
        # |                LOAD_CONST               7 (None)
        # |                RETURN_VALUE
        # |   --   L9:     SWAP                     2
        # |                POP_TOP
        # |   90           SWAP                     2
        # |                STORE_FAST               2 (p)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L9 [2]

    def test_lenient_compose_works_today(self):
        '语料没到位也要能拼出可用的 system_core。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  95           RESUME                   0
        # |  97           LOAD_GLOBAL              1 (SkillLibrary + NULL)
        # |               LOAD_GLOBAL              2 (REAL_SKILLS)
        # |               CALL                     1
        # |               LOAD_ATTR                5 (compose + NULL|self)
        # |               LOAD_GLOBAL              6 (WRITER_SKILLS)
        # |               LOAD_CONST               1 (False)
        # |               LOAD_CONST               2 (('strict',))
        # |               CALL_KW                  2
        # |               STORE_FAST               1 (out)
        # |  98           BUILD_LIST               0
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               3 ('格式硬规范')
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
        # |               LOAD_FAST_BORROW         1 (out)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert0, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE        8 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_CONST               4 ('亲密尺度分档')
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert9, @py_assert9)
        # |               LOAD_FAST_BORROW         1 (out)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert11, @py_assert11)
        # |               STORE_FAST               5 (@py_assert0)
        # |       L1:     LOAD_FAST_BORROW         5 (@py_assert0)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       404 (to L9)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('in',))
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py3)s in %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (@py_assert2, out)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               5 ('py3')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py5')
        # |               LOAD_CONST               7 ('out')
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
        # |               LOAD_FAST_BORROW         1 (out)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (out)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               7 ('out')
        # |       L4:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format6)
        # |               LOAD_CONST               8 ('%(py7)s')
        # |               LOAD_CONST               9 ('py7')
        # |               LOAD_FAST_BORROW         8 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   146 (@py_format8, @py_assert1)
        # |               LOAD_ATTR               21 (append + NULL|self)
        # |               LOAD_FAST_BORROW         9 (@py_format8)
        # |               CALL                     1
        # |               POP_TOP
        # |               LOAD_FAST_BORROW         4 (@py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE      163 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('in',))
        # |               LOAD_FAST_CHECK          7 (@py_assert11)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              19 (('%(py10)s in %(py12)s',))
        # |               LOAD_FAST_CHECK          6 (@py_assert9)
        # |               LOAD_FAST_BORROW         1 (out)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              10 ('py10')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert9)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py12')
        # |               LOAD_CONST               7 ('out')
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
        # |               LOAD_FAST_BORROW         1 (out)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (out)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               7 ('out')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format13)
        # |               LOAD_CONST              12 ('%(py14)s')
        # |               LOAD_CONST              13 ('py14')
        # |               LOAD_FAST_BORROW        10 (@py_format13)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   178 (@py_format15, @py_assert1)
        # |               LOAD_ATTR               21 (append + NULL|self)
        # |               LOAD_FAST_BORROW        11 (@py_format15)
        # |               CALL                     1
        # |               POP_TOP
        # |       L8:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_boolop)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BUILD_MAP                0
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format16)
        # |               LOAD_CONST              14 ('assert %(py17)s')
        # |               LOAD_CONST              15 ('py17')
        # |               LOAD_FAST_BORROW        12 (@py_format16)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format18)
        # |               LOAD_GLOBAL             25 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               26 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        13 (@py_format18)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L9:     LOAD_CONST              16 (None)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  103 (@py_assert9, @py_assert11)
        # |               LOAD_CONST              16 (None)
        # |               RETURN_VALUE

    def test_design_time_skills_kept_out_of_writer(self):
        'writer 一次只写一个 scene，拿到的是设计的**产物**（人物卡来自\nstory_state、节拍类型在 scene spec 里），不需要知道它们怎么被设计。\n\n把设计期技能塞给 writer 会让它的 system_core 从 22K 涨到 41K tokens，\n多出来的规则只会争夺注意力。这条断言防止它们被顺手加回去。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 100            RESUME                   0
        # | 106            BUILD_SET                0
        # |                LOAD_CONST              17 (frozenset({'romance_beats', 'character_design', 'campus_to_career'}))
        # |                SET_UPDATE               1
        # |                STORE_FAST               1 (design_time)
        # | 107            LOAD_GLOBAL              1 (set + NULL)
        # |                LOAD_GLOBAL              2 (WRITER_SKILLS)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    33 (@py_assert3, design_time)
        # |                LOAD_FAST_BORROW         2 (@py_assert3)
        # |                BINARY_OP                1 (&)
        # |                STORE_FAST               3 (@py_assert5)
        # |                LOAD_GLOBAL              1 (set + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert8, @py_assert5)
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       457 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              18 (('==',))
        # |                LOAD_FAST_BORROW         5 (@py_assert6)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('(%(py0)s & %(py4)s\n{%(py4)s = %(py1)s(%(py2)s)\n}) == %(py9)s\n{%(py9)s = %(py7)s()\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert5, @py_assert8)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('design_time')
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
        # |                LOAD_FAST_BORROW         1 (design_time)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (design_time)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               2 ('design_time')
        # |        L3:     LOAD_CONST               3 ('py1')
        # |                LOAD_CONST               4 ('set')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (set)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (set)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               4 ('set')
        # |        L6:     LOAD_CONST               5 ('py2')
        # |                LOAD_CONST               6 ('WRITER_SKILLS')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (WRITER_SKILLS)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (WRITER_SKILLS)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               6 ('WRITER_SKILLS')
        # |        L9:     LOAD_CONST               7 ('py4')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_CONST               4 ('set')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (set)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (set)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST               4 ('set')
        # |       L12:     LOAD_CONST               9 ('py9')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                CALL                     1
        # |                BUILD_MAP                6
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format10)
        # |                LOAD_CONST              10 ('assert %(py11)s')
        # |                LOAD_CONST              11 ('py11')
        # |                LOAD_FAST_BORROW         6 (@py_format10)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format12)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format12)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L13:     LOAD_CONST              12 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   84 (@py_assert6, @py_assert8)
        # | 108            LOAD_GLOBAL              1 (set + NULL)
        # |                LOAD_GLOBAL             20 (ARCHITECT_SKILLS)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   129 (@py_assert4, design_time)
        # |                LOAD_FAST_BORROW         8 (@py_assert4)
        # |                COMPARE_OP              42 (<=)
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       349 (to L23)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              20 (('<=',))
        # |                LOAD_FAST_BORROW         9 (@py_assert1)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              21 (('%(py0)s <= %(py5)s\n{%(py5)s = %(py2)s(%(py3)s)\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 24 (design_time, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('design_time')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (design_time)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L15)
        # |                NOT_TAKEN
        # |       L14:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (design_time)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L16)
        # |       L15:     LOAD_CONST               2 ('design_time')
        # |       L16:     LOAD_CONST               5 ('py2')
        # |                LOAD_CONST               4 ('set')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L17)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (set)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L18)
        # |                NOT_TAKEN
        # |       L17:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (set)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L19)
        # |       L18:     LOAD_CONST               4 ('set')
        # |       L19:     LOAD_CONST              13 ('py3')
        # |                LOAD_CONST              14 ('ARCHITECT_SKILLS')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L20)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             20 (ARCHITECT_SKILLS)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L21)
        # |                NOT_TAKEN
        # |       L20:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             20 (ARCHITECT_SKILLS)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L22)
        # |       L21:     LOAD_CONST              14 ('ARCHITECT_SKILLS')
        # |       L22:     LOAD_CONST              15 ('py5')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format6)
        # |                LOAD_CONST              16 ('assert %(py7)s')
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_FAST_BORROW        10 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format8)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L23:     LOAD_CONST              12 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  152 (@py_assert1, @py_assert4)
        # |                LOAD_CONST              12 (None)
        # |                RETURN_VALUE

    def test_writer_keeps_the_craft_skills(self):
        '反过来，落笔相关的必须在 writer 手里。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 110           RESUME                   0
        # | 112           BUILD_SET                0
        # |               LOAD_CONST              10 (frozenset({'dialogue', 'style_voice', 'format_spec'}))
        # |               SET_UPDATE               1
        # |               STORE_FAST               1 (@py_assert0)
        # |               LOAD_GLOBAL              1 (set + NULL)
        # |               LOAD_GLOBAL              2 (WRITER_SKILLS)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    33 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         2 (@py_assert5)
        # |               COMPARE_OP              42 (<=)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       293 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('<=',))
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py1)s <= %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               2 ('py3')
        # |               LOAD_CONST               3 ('set')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (set)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (set)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('set')
        # |       L3:     LOAD_CONST               4 ('py4')
        # |               LOAD_CONST               5 ('WRITER_SKILLS')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              2 (WRITER_SKILLS)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              2 (WRITER_SKILLS)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               5 ('WRITER_SKILLS')
        # |       L6:     LOAD_CONST               6 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               4 (@py_format7)
        # |               LOAD_CONST               7 ('assert %(py8)s')
        # |               LOAD_CONST               8 ('py8')
        # |               LOAD_FAST_BORROW         4 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format9)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   50 (@py_assert2, @py_assert5)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_format_spec_is_last(self):
        '格式规范放最后，最靠近指令 —— 模型对结尾要求服从度更高。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 114           RESUME                   0
        # | 116           LOAD_GLOBAL              0 (WRITER_SKILLS)
        # |               LOAD_CONST               7 (-1)
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               1 (@py_assert0)
        # |               LOAD_CONST               1 ('format_spec')
        # |               STORE_FAST_LOAD_FAST    33 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         2 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 (('==',))
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               9 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               4 (@py_format5)
        # |               LOAD_CONST               4 ('assert %(py6)s')
        # |               LOAD_CONST               5 ('py6')
        # |               LOAD_FAST_BORROW         4 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format7)
        # |               LOAD_GLOBAL              9 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   50 (@py_assert2, @py_assert3)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE

