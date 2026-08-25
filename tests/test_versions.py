# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py
# 来源   : test_versions.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '覆盖前留旧版。\n\n大纲和成稿都是"重跑一次就原地覆盖"的文件：卷大纲是唯一经人确认的产物，\n章细纲决定一章能不能写好，成稿是几十分钟加真金白银换来的。新版未必更好，\n旧版没地方找回来就是纯损失。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '覆盖前留旧版。\n\n大纲和成稿都是"重跑一次就原地覆盖"的文件：卷大纲是唯一经人确认的产物，\n章细纲决定一章能不能写好，成稿是几十分钟加真金白银换来的。新版未必更好，\n旧版没地方找回来就是纯损失。\n',
    11: 'TestRetireDrafts',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('test_first_write_leaves_no_version', 0): 'ch_003.json',
    ('test_first_write_leaves_no_version', 2): 'py0',
    ('test_first_write_leaves_no_version', 3): 'archive_previous',
    ('test_first_write_leaves_no_version', 4): 'py1',
    ('test_first_write_leaves_no_version', 5): 'f',
    ('test_first_write_leaves_no_version', 6): 'py3',
    ('test_first_write_leaves_no_version', 7): 'py6',
    ('test_first_write_leaves_no_version', 8): '文件还不存在，没有旧版可留',
    ('test_first_write_leaves_no_version', 9): '\n>assert %(py8)s',
    ('test_first_write_leaves_no_version', 10): 'py8',
    ('test_first_write_leaves_no_version', 11): '_versions',
    ('test_first_write_leaves_no_version', 12): 'assert not %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = (%(py0)s / %(py2)s).exists\n}()\n}',
    ('test_first_write_leaves_no_version', 13): 'tmp_path',
    ('test_first_write_leaves_no_version', 14): 'py2',
    ('test_first_write_leaves_no_version', 15): 'py5',
    ('test_first_write_leaves_no_version', 16): 'py7',
    ('test_old_content_is_what_gets_kept', 0): 'v01 存的是**被覆盖掉的那一版**，不是新写进去的那版。',
    ('test_old_content_is_what_gets_kept', 1): 'ch_003.json',
    ('test_old_content_is_what_gets_kept', 2): '第一版',
    ('test_old_content_is_what_gets_kept', 3): 'utf-8',
    ('test_old_content_is_what_gets_kept', 4): '第二版',
    ('test_old_content_is_what_gets_kept', 5): 'ch_003.v01.json',
    ('test_old_content_is_what_gets_kept', 6): 'py0',
    ('test_old_content_is_what_gets_kept', 7): 'kept',
    ('test_old_content_is_what_gets_kept', 8): 'py2',
    ('test_old_content_is_what_gets_kept', 9): 'py5',
    ('test_old_content_is_what_gets_kept', 10): 'assert %(py7)s',
    ('test_old_content_is_what_gets_kept', 11): 'py7',
    ('test_old_content_is_what_gets_kept', 13): 'py4',
    ('test_old_content_is_what_gets_kept', 14): 'py6',
    ('test_old_content_is_what_gets_kept', 15): 'py9',
    ('test_old_content_is_what_gets_kept', 16): 'assert %(py11)s',
    ('test_old_content_is_what_gets_kept', 17): 'py11',
    ('test_old_content_is_what_gets_kept', 18): 'f',
    ('test_versions_accumulate_in_order', 0): 'ch_003.json',
    ('test_versions_accumulate_in_order', 1): '三',
    ('test_versions_accumulate_in_order', 2): 'utf-8',
    ('test_versions_accumulate_in_order', 4): '_versions',
    ('test_versions_accumulate_in_order', 5): 'ch_003.v03.json',
    ('test_versions_accumulate_in_order', 6): 'py0',
    ('test_versions_accumulate_in_order', 7): 'names',
    ('test_versions_accumulate_in_order', 8): 'py3',
    ('test_versions_accumulate_in_order', 9): 'assert %(py5)s',
    ('test_versions_accumulate_in_order', 10): 'py5',
    ('test_versions_accumulate_in_order', 12): 'tmp_path',
    ('test_versions_accumulate_in_order', 13): 'py2',
    ('test_versions_accumulate_in_order', 14): 'py8',
    ('test_versions_accumulate_in_order', 15): 'py10',
    ('test_versions_accumulate_in_order', 16): 'py12',
    ('test_versions_accumulate_in_order', 17): 'py15',
    ('test_versions_accumulate_in_order', 18): 'assert %(py17)s',
    ('test_versions_accumulate_in_order', 19): 'py17',
    ('test_identical_content_does_not_pile_up', 0): '重跑出一模一样的细纲很常见，不该攒出一堆无差别副本。',
    ('test_identical_content_does_not_pile_up', 1): 'ch_003.json',
    ('test_identical_content_does_not_pile_up', 2): '同样的内容',
    ('test_identical_content_does_not_pile_up', 3): 'utf-8',
    ('test_identical_content_does_not_pile_up', 4): '_versions',
    ('test_identical_content_does_not_pile_up', 5): 'py0',
    ('test_identical_content_does_not_pile_up', 6): 'len',
    ('test_identical_content_does_not_pile_up', 7): 'py1',
    ('test_identical_content_does_not_pile_up', 8): 'list',
    ('test_identical_content_does_not_pile_up', 9): 'py2',
    ('test_identical_content_does_not_pile_up', 10): 'tmp_path',
    ('test_identical_content_does_not_pile_up', 11): 'py4',
    ('test_identical_content_does_not_pile_up', 12): 'py7',
    ('test_identical_content_does_not_pile_up', 13): 'py9',
    ('test_identical_content_does_not_pile_up', 14): 'py11',
    ('test_identical_content_does_not_pile_up', 15): 'py13',
    ('test_identical_content_does_not_pile_up', 16): 'py16',
    ('test_identical_content_does_not_pile_up', 17): 'assert %(py18)s',
    ('test_identical_content_does_not_pile_up', 18): 'py18',
    ('test_each_artifact_has_its_own_series', 0): '章细纲、卷大纲、成稿存在同一个 _versions/ 里，版本号不能互相串。',
    ('test_each_artifact_has_its_own_series', 1): '旧',
    ('test_each_artifact_has_its_own_series', 2): 'utf-8',
    ('test_each_artifact_has_its_own_series', 4): '_versions',
    ('test_each_artifact_has_its_own_series', 5): 'ch_003.v01.json',
    ('test_each_artifact_has_its_own_series', 6): 'vol_01.v01.json',
    ('test_each_artifact_has_its_own_series', 7): 'py0',
    ('test_each_artifact_has_its_own_series', 8): 'names',
    ('test_each_artifact_has_its_own_series', 9): 'py3',
    ('test_each_artifact_has_its_own_series', 10): 'assert %(py5)s',
    ('test_each_artifact_has_its_own_series', 11): 'py5',
    ('test_json_and_markdown_are_versioned_separately', 0): 'ch_003.json',
    ('test_json_and_markdown_are_versioned_separately', 1): '旧',
    ('test_json_and_markdown_are_versioned_separately', 2): 'utf-8',
    ('test_json_and_markdown_are_versioned_separately', 4): '_versions',
    ('test_json_and_markdown_are_versioned_separately', 5): 'ch_003.v01.json',
    ('test_json_and_markdown_are_versioned_separately', 6): 'ch_003.v01.md',
    ('test_json_and_markdown_are_versioned_separately', 7): 'py0',
    ('test_json_and_markdown_are_versioned_separately', 8): 'names',
    ('test_json_and_markdown_are_versioned_separately', 9): 'py3',
    ('test_json_and_markdown_are_versioned_separately', 10): 'assert %(py5)s',
    ('test_json_and_markdown_are_versioned_separately', 11): 'py5',
    ('TestRetireDrafts', 0): 'TestRetireDrafts',
    ('TestRetireDrafts', 1): '草稿是**某一版细纲**的产物。细纲改了还把旧草稿捡回去，等于修改白做 ——\n第 3 章正是改细纲的场景（旧版把心理描写禁掉了）。',
    ('test_drafts_move_aside_not_away', 2): 'BOOK',
    ('test_drafts_move_aside_not_away', 3): 'drafts',
    ('test_drafts_move_aside_not_away', 4): 'ch_003',
    ('test_drafts_move_aside_not_away', 7): 'ch003_s1.md',
    ('test_drafts_move_aside_not_away', 8): '旧草稿',
    ('test_drafts_move_aside_not_away', 9): 'utf-8',
    ('test_drafts_move_aside_not_away', 10): 'ch_003.v01',
    ('test_drafts_move_aside_not_away', 11): 'py0',
    ('test_drafts_move_aside_not_away', 12): 'dest',
    ('test_drafts_move_aside_not_away', 13): 'py2',
    ('test_drafts_move_aside_not_away', 14): 'py5',
    ('test_drafts_move_aside_not_away', 15): 'assert %(py7)s',
    ('test_drafts_move_aside_not_away', 16): 'py7',
    ('test_drafts_move_aside_not_away', 17): 'py9',
    ('test_drafts_move_aside_not_away', 18): 'py12',
    ('test_drafts_move_aside_not_away', 19): '挪开，不是删掉',
    ('test_drafts_move_aside_not_away', 20): '\n>assert %(py14)s',
    ('test_drafts_move_aside_not_away', 21): 'py14',
    ('test_drafts_move_aside_not_away', 22): '原位置要空出来，否则 --resume-drafts 还会捡到',
    ('test_drafts_move_aside_not_away', 23): '\n>assert not %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.exists\n}()\n}',
    ('test_drafts_move_aside_not_away', 24): 'd',
    ('test_drafts_move_aside_not_away', 25): 'py4',
    ('test_nothing_to_retire_is_fine', 2): 'BOOK',
    ('test_nothing_to_retire_is_fine', 3): 'py0',
    ('test_nothing_to_retire_is_fine', 4): 'cli',
    ('test_nothing_to_retire_is_fine', 5): 'py2',
    ('test_nothing_to_retire_is_fine', 6): 'py4',
    ('test_nothing_to_retire_is_fine', 7): 'py6',
    ('test_nothing_to_retire_is_fine', 8): 'py9',
    ('test_nothing_to_retire_is_fine', 9): 'assert %(py11)s',
    ('test_nothing_to_retire_is_fine', 10): 'py11',
    ('test_successive_retirements_get_their_own_slot', 2): 'BOOK',
    ('test_successive_retirements_get_their_own_slot', 3): 'drafts',
    ('test_successive_retirements_get_their_own_slot', 4): 'ch_003',
    ('test_successive_retirements_get_their_own_slot', 7): 'ch003_s1.md',
    ('test_successive_retirements_get_their_own_slot', 8): 'x',
    ('test_successive_retirements_get_their_own_slot', 9): 'utf-8',
    ('test_successive_retirements_get_their_own_slot', 10): 'ch_003.v01',
    ('test_successive_retirements_get_their_own_slot', 11): 'ch_003.v02',
    ('test_successive_retirements_get_their_own_slot', 12): 'py1',
    ('test_successive_retirements_get_their_own_slot', 13): 'py4',
    ('test_successive_retirements_get_their_own_slot', 14): 'assert %(py6)s',
    ('test_successive_retirements_get_their_own_slot', 15): 'py6',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def test_first_write_leaves_no_version(tmp_path):
    'ch_003.json'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  13            RESUME                   0
    # |  14            LOAD_FAST_BORROW         0 (tmp_path)
    # |                LOAD_CONST               0 ('ch_003.json')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               1 (f)
    # |  15            LOAD_GLOBAL              1 (archive_previous + NULL)
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                STORE_FAST               2 (@py_assert2)
    # |                LOAD_CONST               1 (None)
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert5, @py_assert2)
    # |                LOAD_FAST_BORROW         3 (@py_assert5)
    # |                IS_OP                    0 (is)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       312 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('is',))
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} is %(py6)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert2, @py_assert5)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('archive_previous')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (archive_previous)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (archive_previous)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               3 ('archive_previous')
    # |        L3:     LOAD_CONST               4 ('py1')
    # |                LOAD_CONST               5 ('f')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               5 ('f')
    # |        L6:     LOAD_CONST               6 ('py3')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py6')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format7)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               14 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST               8 ('文件还不存在，没有旧版可留')
    # |                CALL                     1
    # |                LOAD_CONST               9 ('\n>assert %(py8)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              10 ('py8')
    # |                LOAD_FAST_BORROW         5 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format9)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   67 (@py_assert4, @py_assert5)
    # |  16            LOAD_CONST              11 ('_versions')
    # |                STORE_FAST_LOAD_FAST   112 (@py_assert1, tmp_path)
    # |                LOAD_FAST_BORROW         7 (@py_assert1)
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
    # |                LOAD_ATTR               20 (exists)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert6, @py_assert6)
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert8, @py_assert8)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       185 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_CONST              12 ('assert not %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = (%(py0)s / %(py2)s).exists\n}()\n}')
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST              13 ('tmp_path')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (tmp_path)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (tmp_path)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST              13 ('tmp_path')
    # |       L10:     LOAD_CONST              14 ('py2')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py5')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py7')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert6)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format9)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L11:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  154 (@py_assert6, @py_assert8)
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE

def test_old_content_is_what_gets_kept(tmp_path):
    'v01 存的是**被覆盖掉的那一版**，不是新写进去的那版。'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  19            RESUME                   0
    # |  21            LOAD_FAST_BORROW         0 (tmp_path)
    # |                LOAD_CONST               1 ('ch_003.json')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               1 (f)
    # |  22            LOAD_FAST_BORROW         1 (f)
    # |                LOAD_ATTR                1 (write_text + NULL|self)
    # |                LOAD_CONST               2 ('第一版')
    # |                LOAD_CONST               3 ('utf-8')
    # |                CALL                     2
    # |                POP_TOP
    # |  23            LOAD_GLOBAL              3 (archive_previous + NULL)
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                STORE_FAST               2 (kept)
    # |  24            LOAD_FAST_BORROW         1 (f)
    # |                LOAD_ATTR                1 (write_text + NULL|self)
    # |                LOAD_CONST               4 ('第二版')
    # |                LOAD_CONST               3 ('utf-8')
    # |                CALL                     2
    # |                POP_TOP
    # |  25            LOAD_FAST_BORROW         2 (kept)
    # |                LOAD_ATTR                4 (name)
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_CONST               5 ('ch_003.v01.json')
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('==',))
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py2)s\n{%(py2)s = %(py0)s.name\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               6 ('py0')
    # |                LOAD_CONST               7 ('kept')
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
    # |                LOAD_FAST_BORROW         2 (kept)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (kept)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               7 ('kept')
    # |        L3:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py5')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format6)
    # |                LOAD_CONST              10 ('assert %(py7)s')
    # |                LOAD_CONST              11 ('py7')
    # |                LOAD_FAST_BORROW         6 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format8)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   84 (@py_assert3, @py_assert4)
    # |  26            LOAD_FAST_BORROW         2 (kept)
    # |                LOAD_ATTR               22 (read_text)
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_CONST               3 ('utf-8')
    # |                STORE_FAST_LOAD_FAST    83 (@py_assert3, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                STORE_FAST               8 (@py_assert5)
    # |                LOAD_CONST               2 ('第一版')
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert8, @py_assert5)
    # |                LOAD_FAST_BORROW         9 (@py_assert8)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert7, @py_assert7)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       243 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert7)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              21 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.read_text\n}(%(py4)s)\n} == %(py9)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert5, @py_assert8)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               6 ('py0')
    # |                LOAD_CONST               7 ('kept')
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
    # |                LOAD_FAST_BORROW         2 (kept)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (kept)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               7 ('kept')
    # |        L7:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py4')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert8)
    # |                CALL                     1
    # |                BUILD_MAP                5
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format10)
    # |                LOAD_CONST              16 ('assert %(py11)s')
    # |                LOAD_CONST              17 ('py11')
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
    # |        L8:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  169 (@py_assert7, @py_assert8)
    # |  27            LOAD_FAST_BORROW         1 (f)
    # |                LOAD_ATTR               22 (read_text)
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_CONST               3 ('utf-8')
    # |                STORE_FAST_LOAD_FAST    83 (@py_assert3, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                STORE_FAST               8 (@py_assert5)
    # |                LOAD_CONST               4 ('第二版')
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert8, @py_assert5)
    # |                LOAD_FAST_BORROW         9 (@py_assert8)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert7, @py_assert7)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       243 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('==',))
    # |                LOAD_FAST_BORROW        10 (@py_assert7)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              21 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.read_text\n}(%(py4)s)\n} == %(py9)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert5, @py_assert8)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               6 ('py0')
    # |                LOAD_CONST              18 ('f')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L10)
    # |                NOT_TAKEN
    # |        L9:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L11)
    # |       L10:     LOAD_CONST              18 ('f')
    # |       L11:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py4')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert8)
    # |                CALL                     1
    # |                BUILD_MAP                5
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format10)
    # |                LOAD_CONST              16 ('assert %(py11)s')
    # |                LOAD_CONST              17 ('py11')
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
    # |       L12:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  169 (@py_assert7, @py_assert8)
    # |                LOAD_CONST              12 (None)
    # |                RETURN_VALUE

def test_versions_accumulate_in_order(tmp_path):
    'ch_003.json'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  30            RESUME                   0
    # |  31            LOAD_FAST_BORROW         0 (tmp_path)
    # |                LOAD_CONST               0 ('ch_003.json')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               1 (f)
    # |  32            LOAD_CONST              20 (('一', '二', '三'))
    # |                GET_ITER
    # |        L1:     FOR_ITER                32 (to L2)
    # |                STORE_FAST               2 (text)
    # |  33            LOAD_FAST_BORROW         1 (f)
    # |                LOAD_ATTR                1 (write_text + NULL|self)
    # |                LOAD_FAST_BORROW         2 (text)
    # |                LOAD_CONST               2 ('utf-8')
    # |                CALL                     2
    # |                POP_TOP
    # |  34            LOAD_GLOBAL              3 (archive_previous + NULL)
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                POP_TOP
    # |                JUMP_BACKWARD           34 (to L1)
    # |  32    L2:     END_FOR
    # |                POP_ITER
    # |  35            LOAD_GLOBAL              5 (sorted + NULL)
    # |                LOAD_CONST               3 (<code object <genexpr> at 0x10ac97dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 35>)
    # |                MAKE_FUNCTION
    # |                LOAD_FAST_BORROW         0 (tmp_path)
    # |                LOAD_CONST               4 ('_versions')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR                7 (iterdir + NULL|self)
    # |                CALL                     0
    # |                GET_ITER
    # |                CALL                     0
    # |                CALL                     1
    # |                STORE_FAST               3 (names)
    # |  36            BUILD_LIST               0
    # |                LOAD_CONST              21 (('ch_003.v01.json', 'ch_003.v02.json', 'ch_003.v03.json'))
    # |                LIST_EXTEND              1
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert2, names)
    # |                LOAD_FAST_BORROW         4 (@py_assert2)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       177 (to L6)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 (('==',))
    # |                LOAD_FAST_BORROW         5 (@py_assert1)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              23 (('%(py0)s == %(py3)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (names, @py_assert2)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               6 ('py0')
    # |                LOAD_CONST               7 ('names')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L3)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (names)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L4)
    # |                NOT_TAKEN
    # |        L3:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (names)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L5)
    # |        L4:     LOAD_CONST               7 ('names')
    # |        L5:     LOAD_CONST               8 ('py3')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert2)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format4)
    # |                LOAD_CONST               9 ('assert %(py5)s')
    # |                LOAD_CONST              10 ('py5')
    # |                LOAD_FAST_BORROW         6 (@py_format4)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format6)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format6)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L6:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   84 (@py_assert1, @py_assert2)
    # |  37            LOAD_CONST               4 ('_versions')
    # |                STORE_FAST_LOAD_FAST    80 (@py_assert1, tmp_path)
    # |                LOAD_FAST_BORROW         5 (@py_assert1)
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               8 (@py_assert3)
    # |                LOAD_CONST               5 ('ch_003.v03.json')
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert4, @py_assert3)
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert6, @py_assert6)
    # |                LOAD_ATTR               24 (read_text)
    # |                STORE_FAST              11 (@py_assert7)
    # |                LOAD_CONST               2 ('utf-8')
    # |                STORE_FAST_LOAD_FAST   203 (@py_assert9, @py_assert7)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert9)
    # |                CALL                     1
    # |                STORE_FAST              13 (@py_assert11)
    # |                LOAD_CONST               1 ('三')
    # |                STORE_FAST_LOAD_FAST   237 (@py_assert14, @py_assert11)
    # |                LOAD_FAST_BORROW        14 (@py_assert14)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   255 (@py_assert13, @py_assert13)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       287 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 (('==',))
    # |                LOAD_FAST_BORROW        15 (@py_assert13)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              24 (('%(py12)s\n{%(py12)s = %(py8)s\n{%(py8)s = ((%(py0)s / %(py2)s) / %(py5)s).read_text\n}(%(py10)s)\n} == %(py15)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 222 (@py_assert11, @py_assert14)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               6 ('py0')
    # |                LOAD_CONST              12 ('tmp_path')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (tmp_path)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (tmp_path)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              12 ('tmp_path')
    # |        L9:     LOAD_CONST              13 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py8')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert7)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py10')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py12')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_assert11)
    # |                CALL                     1
    # |                LOAD_CONST              17 ('py15')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        14 (@py_assert14)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format16)
    # |                LOAD_CONST              18 ('assert %(py17)s')
    # |                LOAD_CONST              19 ('py17')
    # |                LOAD_FAST_BORROW        16 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format18)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        17 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST              11 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST              12 (@py_assert9)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert11)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  254 (@py_assert13, @py_assert14)
    # |                LOAD_CONST              11 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10ac97dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 35>:
    # |   35           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (p, p)
    # |                LOAD_ATTR                0 (name)
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

def test_identical_content_does_not_pile_up(tmp_path):
    '重跑出一模一样的细纲很常见，不该攒出一堆无差别副本。'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  40            RESUME                   0
    # |  42            LOAD_FAST_BORROW         0 (tmp_path)
    # |                LOAD_CONST               1 ('ch_003.json')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               1 (f)
    # |  43            LOAD_FAST_BORROW         1 (f)
    # |                LOAD_ATTR                1 (write_text + NULL|self)
    # |                LOAD_CONST               2 ('同样的内容')
    # |                LOAD_CONST               3 ('utf-8')
    # |                CALL                     2
    # |                POP_TOP
    # |  44            LOAD_GLOBAL              3 (archive_previous + NULL)
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                POP_TOP
    # |  45            LOAD_GLOBAL              3 (archive_previous + NULL)
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                POP_TOP
    # |  46            LOAD_GLOBAL              3 (archive_previous + NULL)
    # |                LOAD_FAST_BORROW         1 (f)
    # |                CALL                     1
    # |                POP_TOP
    # |  47            LOAD_CONST               4 ('_versions')
    # |                STORE_FAST_LOAD_FAST    32 (@py_assert3, tmp_path)
    # |                LOAD_FAST_BORROW         2 (@py_assert3)
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert5, @py_assert5)
    # |                LOAD_ATTR                4 (iterdir)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert6, @py_assert6)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_GLOBAL              7 (list + NULL)
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST               6 (@py_assert10)
    # |                LOAD_GLOBAL              9 (len + NULL)
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                STORE_FAST               7 (@py_assert12)
    # |                LOAD_SMALL_INT           1
    # |                STORE_FAST_LOAD_FAST   135 (@py_assert15, @py_assert12)
    # |                LOAD_FAST_BORROW         8 (@py_assert15)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert14, @py_assert14)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       459 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              20 (('==',))
    # |                LOAD_FAST_BORROW         9 (@py_assert14)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              21 (('%(py13)s\n{%(py13)s = %(py0)s(%(py11)s\n{%(py11)s = %(py1)s(%(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = (%(py2)s / %(py4)s).iterdir\n}()\n})\n})\n} == %(py16)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert12, @py_assert15)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('len')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (len)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (len)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               6 ('len')
    # |        L3:     LOAD_CONST               7 ('py1')
    # |                LOAD_CONST               8 ('list')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (list)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (list)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               8 ('list')
    # |        L6:     LOAD_CONST               9 ('py2')
    # |                LOAD_CONST              10 ('tmp_path')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (tmp_path)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (tmp_path)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('tmp_path')
    # |        L9:     LOAD_CONST              11 ('py4')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py7')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py9')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py11')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py13')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert12)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py16')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert15)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format17)
    # |                LOAD_CONST              17 ('assert %(py18)s')
    # |                LOAD_CONST              18 ('py18')
    # |                LOAD_FAST_BORROW        10 (@py_format17)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format19)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_format19)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              19 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert10)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert12)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  152 (@py_assert14, @py_assert15)
    # |                LOAD_CONST              19 (None)
    # |                RETURN_VALUE

def test_each_artifact_has_its_own_series(tmp_path):
    '章细纲、卷大纲、成稿存在同一个 _versions/ 里，版本号不能互相串。'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  50           RESUME                   0
    # |  52           LOAD_CONST              13 (('ch_003.json', 'vol_01.json'))
    # |               GET_ITER
    # |       L1:     FOR_ITER                40 (to L2)
    # |               STORE_FAST               1 (name)
    # |  53           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (tmp_path, name)
    # |               BINARY_OP               11 (/)
    # |               STORE_FAST               2 (f)
    # |  54           LOAD_FAST_BORROW         2 (f)
    # |               LOAD_ATTR                1 (write_text + NULL|self)
    # |               LOAD_CONST               1 ('旧')
    # |               LOAD_CONST               2 ('utf-8')
    # |               CALL                     2
    # |               POP_TOP
    # |  55           LOAD_GLOBAL              3 (archive_previous + NULL)
    # |               LOAD_FAST_BORROW         2 (f)
    # |               CALL                     1
    # |               POP_TOP
    # |               JUMP_BACKWARD           42 (to L1)
    # |  52   L2:     END_FOR
    # |               POP_ITER
    # |  56           LOAD_GLOBAL              5 (sorted + NULL)
    # |               LOAD_CONST               3 (<code object <genexpr> at 0x10ac97ee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 56>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         0 (tmp_path)
    # |               LOAD_CONST               4 ('_versions')
    # |               BINARY_OP               11 (/)
    # |               LOAD_ATTR                7 (iterdir + NULL|self)
    # |               CALL                     0
    # |               GET_ITER
    # |               CALL                     0
    # |               CALL                     1
    # |               STORE_FAST               3 (names)
    # |  57           LOAD_CONST               5 ('ch_003.v01.json')
    # |               LOAD_CONST               6 ('vol_01.v01.json')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert2, names)
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L6)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert1)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py0)s == %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (names, @py_assert2)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py0')
    # |               LOAD_CONST               8 ('names')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (names)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L4)
    # |               NOT_TAKEN
    # |       L3:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (names)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L5)
    # |       L4:     LOAD_CONST               8 ('names')
    # |       L5:     LOAD_CONST               9 ('py3')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format4)
    # |               LOAD_CONST              10 ('assert %(py5)s')
    # |               LOAD_CONST              11 ('py5')
    # |               LOAD_FAST_BORROW         6 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format6)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L6:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert1, @py_assert2)
    # |               LOAD_CONST              12 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10ac97ee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 56>:
    # |   56           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (p, p)
    # |                LOAD_ATTR                0 (name)
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

def test_json_and_markdown_are_versioned_separately(tmp_path):
    'ch_003.json'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  60           RESUME                   0
    # |  61           LOAD_CONST              13 (('ch_003.json', 'ch_003.md'))
    # |               GET_ITER
    # |       L1:     FOR_ITER                40 (to L2)
    # |               STORE_FAST               1 (name)
    # |  62           LOAD_FAST_BORROW_LOAD_FAST_BORROW 1 (tmp_path, name)
    # |               BINARY_OP               11 (/)
    # |               STORE_FAST               2 (f)
    # |  63           LOAD_FAST_BORROW         2 (f)
    # |               LOAD_ATTR                1 (write_text + NULL|self)
    # |               LOAD_CONST               1 ('旧')
    # |               LOAD_CONST               2 ('utf-8')
    # |               CALL                     2
    # |               POP_TOP
    # |  64           LOAD_GLOBAL              3 (archive_previous + NULL)
    # |               LOAD_FAST_BORROW         2 (f)
    # |               CALL                     1
    # |               POP_TOP
    # |               JUMP_BACKWARD           42 (to L1)
    # |  61   L2:     END_FOR
    # |               POP_ITER
    # |  65           LOAD_GLOBAL              5 (sorted + NULL)
    # |               LOAD_CONST               3 (<code object <genexpr> at 0x10ace8030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 65>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         0 (tmp_path)
    # |               LOAD_CONST               4 ('_versions')
    # |               BINARY_OP               11 (/)
    # |               LOAD_ATTR                7 (iterdir + NULL|self)
    # |               CALL                     0
    # |               GET_ITER
    # |               CALL                     0
    # |               CALL                     1
    # |               STORE_FAST               3 (names)
    # |  66           LOAD_CONST               5 ('ch_003.v01.json')
    # |               LOAD_CONST               6 ('ch_003.v01.md')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert2, names)
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L6)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert1)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py0)s == %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (names, @py_assert2)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py0')
    # |               LOAD_CONST               8 ('names')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (names)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L4)
    # |               NOT_TAKEN
    # |       L3:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (names)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L5)
    # |       L4:     LOAD_CONST               8 ('names')
    # |       L5:     LOAD_CONST               9 ('py3')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format4)
    # |               LOAD_CONST              10 ('assert %(py5)s')
    # |               LOAD_CONST              11 ('py5')
    # |               LOAD_FAST_BORROW         6 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format6)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L6:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert1, @py_assert2)
    # |               LOAD_CONST              12 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10ace8030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 65>:
    # |   65           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (p, p)
    # |                LOAD_ATTR                0 (name)
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

class TestRetireDrafts:
    'TestRetireDrafts'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  69           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestRetireDrafts')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          69
    # |               STORE_NAME               3 (__firstlineno__)
    # |  70           LOAD_CONST               1 ('草稿是**某一版细纲**的产物。细纲改了还把旧草稿捡回去，等于修改白做 ——\n第 3 章正是改细纲的场景（旧版把心理描写禁掉了）。')
    # |               STORE_NAME               4 (__doc__)
    # |  73           LOAD_CONST               2 (<code object test_drafts_move_aside_not_away at 0x7ce92a4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 73>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_drafts_move_aside_not_away)
    # |  86           LOAD_CONST               3 (<code object test_nothing_to_retire_is_fine at 0x7ce9294a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 86>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_nothing_to_retire_is_fine)
    # |  92           LOAD_CONST               4 (<code object test_successive_retirements_get_their_own_slot at 0x7ce9294e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 92>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_successive_retirements_get_their_own_slot)
    # |               LOAD_CONST               5 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_drafts_move_aside_not_away at 0x7ce92a4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 73>:
    # |  73            RESUME                   0
    # |  74            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (None)
    # |                IMPORT_NAME              0 (novel_agent.cli)
    # |                IMPORT_FROM              1 (cli)
    # |                STORE_FAST               3 (cli)
    # |                POP_TOP
    # |  76            LOAD_FAST_BORROW         2 (monkeypatch)
    # |                LOAD_ATTR                5 (setattr + NULL|self)
    # |                LOAD_FAST_BORROW         3 (cli)
    # |                LOAD_CONST               2 ('BOOK')
    # |                LOAD_FAST_BORROW         1 (tmp_path)
    # |                CALL                     3
    # |                POP_TOP
    # |  77            LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               3 ('drafts')
    # |                BINARY_OP               11 (/)
    # |                LOAD_CONST               4 ('ch_003')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               4 (d)
    # |  78            LOAD_FAST_BORROW         4 (d)
    # |                LOAD_ATTR                7 (mkdir + NULL|self)
    # |                LOAD_CONST               5 (True)
    # |                LOAD_CONST               6 (('parents',))
    # |                CALL_KW                  1
    # |                POP_TOP
    # |  79            LOAD_FAST_BORROW         4 (d)
    # |                LOAD_CONST               7 ('ch003_s1.md')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR                9 (write_text + NULL|self)
    # |                LOAD_CONST               8 ('旧草稿')
    # |                LOAD_CONST               9 ('utf-8')
    # |                CALL                     2
    # |                POP_TOP
    # |  81            LOAD_FAST_BORROW         3 (cli)
    # |                LOAD_ATTR               11 (retire_drafts + NULL|self)
    # |                LOAD_SMALL_INT           3
    # |                CALL                     1
    # |                STORE_FAST               5 (dest)
    # |  82            LOAD_FAST_BORROW         5 (dest)
    # |                LOAD_ATTR               12 (name)
    # |                STORE_FAST               6 (@py_assert1)
    # |                LOAD_CONST              10 ('ch_003.v01')
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              26 (('==',))
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              27 (('%(py2)s\n{%(py2)s = %(py0)s.name\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              11 ('py0')
    # |                LOAD_CONST              12 ('dest')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (dest)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (dest)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST              12 ('dest')
    # |        L3:     LOAD_CONST              13 ('py2')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py5')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format6)
    # |                LOAD_CONST              15 ('assert %(py7)s')
    # |                LOAD_CONST              16 ('py7')
    # |                LOAD_FAST_BORROW         9 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format8)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  135 (@py_assert3, @py_assert4)
    # |  83            LOAD_CONST               7 ('ch003_s1.md')
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert1, dest)
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
    # |                LOAD_ATTR               30 (read_text)
    # |                STORE_FAST               7 (@py_assert4)
    # |                LOAD_CONST               9 ('utf-8')
    # |                STORE_FAST_LOAD_FAST   183 (@py_assert6, @py_assert4)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert6)
    # |                CALL                     1
    # |                STORE_FAST              12 (@py_assert8)
    # |                LOAD_CONST               8 ('旧草稿')
    # |                STORE_FAST_LOAD_FAST   220 (@py_assert11, @py_assert8)
    # |                LOAD_FAST_BORROW        13 (@py_assert11)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   238 (@py_assert10, @py_assert10)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       292 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              26 (('==',))
    # |                LOAD_FAST_BORROW        14 (@py_assert10)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              28 (('%(py9)s\n{%(py9)s = %(py5)s\n{%(py5)s = (%(py0)s / %(py2)s).read_text\n}(%(py7)s)\n} == %(py12)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 205 (@py_assert8, @py_assert11)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              11 ('py0')
    # |                LOAD_CONST              12 ('dest')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (dest)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (dest)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST              12 ('dest')
    # |        L7:     LOAD_CONST              13 ('py2')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py5')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py7')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST              17 ('py9')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              18 ('py12')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                6
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format13)
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               32 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 ('挪开，不是删掉')
    # |                CALL                     1
    # |                LOAD_CONST              20 ('\n>assert %(py14)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              21 ('py14')
    # |                LOAD_FAST_BORROW        15 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format15)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        16 (@py_format15)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST              11 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST              12 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  237 (@py_assert10, @py_assert11)
    # |  84            LOAD_FAST_BORROW         4 (d)
    # |                LOAD_ATTR               34 (exists)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                STORE_FAST              17 (@py_assert5)
    # |                LOAD_FAST_BORROW        17 (@py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       190 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               32 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 ('原位置要空出来，否则 --resume-drafts 还会捡到')
    # |                CALL                     1
    # |                LOAD_CONST              23 ('\n>assert not %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.exists\n}()\n}')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              11 ('py0')
    # |                LOAD_CONST              24 ('d')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (d)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L10)
    # |                NOT_TAKEN
    # |        L9:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (d)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L11)
    # |       L10:     LOAD_CONST              24 ('d')
    # |       L11:     LOAD_CONST              13 ('py2')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              25 ('py4')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               24 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format6)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format6)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L12:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert3)
    # |                STORE_FAST              17 (@py_assert5)
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_nothing_to_retire_is_fine at 0x7ce9294a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 86>:
    # |  86           RESUME                   0
    # |  87           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (None)
    # |               IMPORT_NAME              0 (novel_agent.cli)
    # |               IMPORT_FROM              1 (cli)
    # |               STORE_FAST               3 (cli)
    # |               POP_TOP
    # |  89           LOAD_FAST_BORROW         2 (monkeypatch)
    # |               LOAD_ATTR                5 (setattr + NULL|self)
    # |               LOAD_FAST_BORROW         3 (cli)
    # |               LOAD_CONST               2 ('BOOK')
    # |               LOAD_FAST_BORROW         1 (tmp_path)
    # |               CALL                     3
    # |               POP_TOP
    # |  90           LOAD_FAST_BORROW         3 (cli)
    # |               LOAD_ATTR                6 (retire_drafts)
    # |               STORE_FAST               4 (@py_assert1)
    # |               LOAD_SMALL_INT           3
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST               6 (@py_assert5)
    # |               LOAD_CONST               1 (None)
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert8, @py_assert5)
    # |               LOAD_FAST_BORROW         7 (@py_assert8)
    # |               IS_OP                    0 (is)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       243 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('is',))
    # |               LOAD_FAST_BORROW         8 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.retire_drafts\n}(%(py4)s)\n} is %(py9)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert5, @py_assert8)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('cli')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (cli)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (cli)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('cli')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py9')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format10)
    # |               LOAD_CONST               9 ('assert %(py11)s')
    # |               LOAD_CONST              10 ('py11')
    # |               LOAD_FAST_BORROW         9 (@py_format10)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format12)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format12)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               1 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert7, @py_assert8)
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_successive_retirements_get_their_own_slot at 0x7ce9294e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_versions.py", line 92>:
    # |   92           RESUME                   0
    # |   93           LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (None)
    # |                IMPORT_NAME              0 (novel_agent.cli)
    # |                IMPORT_FROM              1 (cli)
    # |                STORE_FAST               3 (cli)
    # |                POP_TOP
    # |   95           LOAD_FAST_BORROW         2 (monkeypatch)
    # |                LOAD_ATTR                5 (setattr + NULL|self)
    # |                LOAD_FAST_BORROW         3 (cli)
    # |                LOAD_CONST               2 ('BOOK')
    # |                LOAD_FAST_BORROW         1 (tmp_path)
    # |                CALL                     3
    # |                POP_TOP
    # |   96           LOAD_GLOBAL              7 (range + NULL)
    # |                LOAD_SMALL_INT           2
    # |                CALL                     1
    # |                GET_ITER
    # |        L1:     FOR_ITER                79 (to L2)
    # |                STORE_FAST               4 (_)
    # |   97           LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               3 ('drafts')
    # |                BINARY_OP               11 (/)
    # |                LOAD_CONST               4 ('ch_003')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               5 (d)
    # |   98           LOAD_FAST_BORROW         5 (d)
    # |                LOAD_ATTR                9 (mkdir + NULL|self)
    # |                LOAD_CONST               5 (True)
    # |                LOAD_CONST               6 (('parents',))
    # |                CALL_KW                  1
    # |                POP_TOP
    # |   99           LOAD_FAST_BORROW         5 (d)
    # |                LOAD_CONST               7 ('ch003_s1.md')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR               11 (write_text + NULL|self)
    # |                LOAD_CONST               8 ('x')
    # |                LOAD_CONST               9 ('utf-8')
    # |                CALL                     2
    # |                POP_TOP
    # |  100           LOAD_FAST_BORROW         3 (cli)
    # |                LOAD_ATTR               13 (retire_drafts + NULL|self)
    # |                LOAD_SMALL_INT           3
    # |                CALL                     1
    # |                POP_TOP
    # |                JUMP_BACKWARD           81 (to L1)
    # |   96   L2:     END_FOR
    # |                POP_ITER
    # |  101           LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               3 ('drafts')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR               15 (iterdir + NULL|self)
    # |                CALL                     0
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      6 (p)
    # |                SWAP                     2
    # |        L3:     BUILD_SET                0
    # |                SWAP                     2
    # |        L4:     FOR_ITER                14 (to L5)
    # |                STORE_FAST_LOAD_FAST   102 (p, p)
    # |                LOAD_ATTR               16 (name)
    # |                SET_ADD                  2
    # |                JUMP_BACKWARD           16 (to L4)
    # |        L5:     END_FOR
    # |                POP_ITER
    # |        L6:     STORE_FAST               7 (@py_assert0)
    # |                STORE_FAST               6 (p)
    # |  102           LOAD_CONST              10 ('ch_003.v01')
    # |                LOAD_CONST              11 ('ch_003.v02')
    # |  101           BUILD_SET                2
    # |                STORE_FAST_LOAD_FAST   135 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |  102           LOAD_ATTR               20 (_call_reprcompare)
    # |  101           PUSH_NULL
    # |                LOAD_CONST              16 (('==',))
    # |                LOAD_FAST_BORROW         9 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              12 ('py1')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |  102           LOAD_ATTR               22 (_saferepr)
    # |  101           PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py4')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |  102           LOAD_ATTR               22 (_saferepr)
    # |  101           PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format5)
    # |                LOAD_CONST              14 ('assert %(py6)s')
    # |                LOAD_CONST              15 ('py6')
    # |                LOAD_FAST_BORROW        10 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format7)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |  102           LOAD_ATTR               26 (_format_explanation)
    # |  101           PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST               1 (None)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  152 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L8:     SWAP                     2
    # |                POP_TOP
    # |  101           SWAP                     2
    # |                STORE_FAST               6 (p)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L3 to L6 -> L8 [2]

    def test_drafts_move_aside_not_away(self, tmp_path, monkeypatch):
        'BOOK'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  73            RESUME                   0
        # |  74            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (None)
        # |                IMPORT_NAME              0 (novel_agent.cli)
        # |                IMPORT_FROM              1 (cli)
        # |                STORE_FAST               3 (cli)
        # |                POP_TOP
        # |  76            LOAD_FAST_BORROW         2 (monkeypatch)
        # |                LOAD_ATTR                5 (setattr + NULL|self)
        # |                LOAD_FAST_BORROW         3 (cli)
        # |                LOAD_CONST               2 ('BOOK')
        # |                LOAD_FAST_BORROW         1 (tmp_path)
        # |                CALL                     3
        # |                POP_TOP
        # |  77            LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               3 ('drafts')
        # |                BINARY_OP               11 (/)
        # |                LOAD_CONST               4 ('ch_003')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               4 (d)
        # |  78            LOAD_FAST_BORROW         4 (d)
        # |                LOAD_ATTR                7 (mkdir + NULL|self)
        # |                LOAD_CONST               5 (True)
        # |                LOAD_CONST               6 (('parents',))
        # |                CALL_KW                  1
        # |                POP_TOP
        # |  79            LOAD_FAST_BORROW         4 (d)
        # |                LOAD_CONST               7 ('ch003_s1.md')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR                9 (write_text + NULL|self)
        # |                LOAD_CONST               8 ('旧草稿')
        # |                LOAD_CONST               9 ('utf-8')
        # |                CALL                     2
        # |                POP_TOP
        # |  81            LOAD_FAST_BORROW         3 (cli)
        # |                LOAD_ATTR               11 (retire_drafts + NULL|self)
        # |                LOAD_SMALL_INT           3
        # |                CALL                     1
        # |                STORE_FAST               5 (dest)
        # |  82            LOAD_FAST_BORROW         5 (dest)
        # |                LOAD_ATTR               12 (name)
        # |                STORE_FAST               6 (@py_assert1)
        # |                LOAD_CONST              10 ('ch_003.v01')
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              26 (('==',))
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              27 (('%(py2)s\n{%(py2)s = %(py0)s.name\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              11 ('py0')
        # |                LOAD_CONST              12 ('dest')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (dest)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (dest)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST              12 ('dest')
        # |        L3:     LOAD_CONST              13 ('py2')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py5')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format6)
        # |                LOAD_CONST              15 ('assert %(py7)s')
        # |                LOAD_CONST              16 ('py7')
        # |                LOAD_FAST_BORROW         9 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format8)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  135 (@py_assert3, @py_assert4)
        # |  83            LOAD_CONST               7 ('ch003_s1.md')
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert1, dest)
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
        # |                LOAD_ATTR               30 (read_text)
        # |                STORE_FAST               7 (@py_assert4)
        # |                LOAD_CONST               9 ('utf-8')
        # |                STORE_FAST_LOAD_FAST   183 (@py_assert6, @py_assert4)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert6)
        # |                CALL                     1
        # |                STORE_FAST              12 (@py_assert8)
        # |                LOAD_CONST               8 ('旧草稿')
        # |                STORE_FAST_LOAD_FAST   220 (@py_assert11, @py_assert8)
        # |                LOAD_FAST_BORROW        13 (@py_assert11)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   238 (@py_assert10, @py_assert10)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       292 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              26 (('==',))
        # |                LOAD_FAST_BORROW        14 (@py_assert10)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              28 (('%(py9)s\n{%(py9)s = %(py5)s\n{%(py5)s = (%(py0)s / %(py2)s).read_text\n}(%(py7)s)\n} == %(py12)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 205 (@py_assert8, @py_assert11)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              11 ('py0')
        # |                LOAD_CONST              12 ('dest')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (dest)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (dest)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST              12 ('dest')
        # |        L7:     LOAD_CONST              13 ('py2')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py5')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST              16 ('py7')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST              17 ('py9')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              18 ('py12')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                6
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format13)
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               32 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 ('挪开，不是删掉')
        # |                CALL                     1
        # |                LOAD_CONST              20 ('\n>assert %(py14)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              21 ('py14')
        # |                LOAD_FAST_BORROW        15 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format15)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        16 (@py_format15)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST              11 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST              12 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  237 (@py_assert10, @py_assert11)
        # |  84            LOAD_FAST_BORROW         4 (d)
        # |                LOAD_ATTR               34 (exists)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                UNARY_NOT
        # |                STORE_FAST              17 (@py_assert5)
        # |                LOAD_FAST_BORROW        17 (@py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       190 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               32 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              22 ('原位置要空出来，否则 --resume-drafts 还会捡到')
        # |                CALL                     1
        # |                LOAD_CONST              23 ('\n>assert not %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.exists\n}()\n}')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              11 ('py0')
        # |                LOAD_CONST              24 ('d')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (d)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L10)
        # |                NOT_TAKEN
        # |        L9:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (d)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L11)
        # |       L10:     LOAD_CONST              24 ('d')
        # |       L11:     LOAD_CONST              13 ('py2')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              25 ('py4')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               24 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format6)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format6)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L12:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert3)
        # |                STORE_FAST              17 (@py_assert5)
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE

    def test_nothing_to_retire_is_fine(self, tmp_path, monkeypatch):
        'BOOK'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  86           RESUME                   0
        # |  87           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (None)
        # |               IMPORT_NAME              0 (novel_agent.cli)
        # |               IMPORT_FROM              1 (cli)
        # |               STORE_FAST               3 (cli)
        # |               POP_TOP
        # |  89           LOAD_FAST_BORROW         2 (monkeypatch)
        # |               LOAD_ATTR                5 (setattr + NULL|self)
        # |               LOAD_FAST_BORROW         3 (cli)
        # |               LOAD_CONST               2 ('BOOK')
        # |               LOAD_FAST_BORROW         1 (tmp_path)
        # |               CALL                     3
        # |               POP_TOP
        # |  90           LOAD_FAST_BORROW         3 (cli)
        # |               LOAD_ATTR                6 (retire_drafts)
        # |               STORE_FAST               4 (@py_assert1)
        # |               LOAD_SMALL_INT           3
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST               6 (@py_assert5)
        # |               LOAD_CONST               1 (None)
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert8, @py_assert5)
        # |               LOAD_FAST_BORROW         7 (@py_assert8)
        # |               IS_OP                    0 (is)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       243 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('is',))
        # |               LOAD_FAST_BORROW         8 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.retire_drafts\n}(%(py4)s)\n} is %(py9)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert5, @py_assert8)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('cli')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (cli)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (cli)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('cli')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py9')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format10)
        # |               LOAD_CONST               9 ('assert %(py11)s')
        # |               LOAD_CONST              10 ('py11')
        # |               LOAD_FAST_BORROW         9 (@py_format10)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format12)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format12)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               1 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert7, @py_assert8)
        # |               LOAD_CONST               1 (None)
        # |               RETURN_VALUE

    def test_successive_retirements_get_their_own_slot(self, tmp_path, monkeypatch):
        'BOOK'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   92           RESUME                   0
        # |   93           LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (None)
        # |                IMPORT_NAME              0 (novel_agent.cli)
        # |                IMPORT_FROM              1 (cli)
        # |                STORE_FAST               3 (cli)
        # |                POP_TOP
        # |   95           LOAD_FAST_BORROW         2 (monkeypatch)
        # |                LOAD_ATTR                5 (setattr + NULL|self)
        # |                LOAD_FAST_BORROW         3 (cli)
        # |                LOAD_CONST               2 ('BOOK')
        # |                LOAD_FAST_BORROW         1 (tmp_path)
        # |                CALL                     3
        # |                POP_TOP
        # |   96           LOAD_GLOBAL              7 (range + NULL)
        # |                LOAD_SMALL_INT           2
        # |                CALL                     1
        # |                GET_ITER
        # |        L1:     FOR_ITER                79 (to L2)
        # |                STORE_FAST               4 (_)
        # |   97           LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               3 ('drafts')
        # |                BINARY_OP               11 (/)
        # |                LOAD_CONST               4 ('ch_003')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               5 (d)
        # |   98           LOAD_FAST_BORROW         5 (d)
        # |                LOAD_ATTR                9 (mkdir + NULL|self)
        # |                LOAD_CONST               5 (True)
        # |                LOAD_CONST               6 (('parents',))
        # |                CALL_KW                  1
        # |                POP_TOP
        # |   99           LOAD_FAST_BORROW         5 (d)
        # |                LOAD_CONST               7 ('ch003_s1.md')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR               11 (write_text + NULL|self)
        # |                LOAD_CONST               8 ('x')
        # |                LOAD_CONST               9 ('utf-8')
        # |                CALL                     2
        # |                POP_TOP
        # |  100           LOAD_FAST_BORROW         3 (cli)
        # |                LOAD_ATTR               13 (retire_drafts + NULL|self)
        # |                LOAD_SMALL_INT           3
        # |                CALL                     1
        # |                POP_TOP
        # |                JUMP_BACKWARD           81 (to L1)
        # |   96   L2:     END_FOR
        # |                POP_ITER
        # |  101           LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               3 ('drafts')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR               15 (iterdir + NULL|self)
        # |                CALL                     0
        # |                GET_ITER
        # |                LOAD_FAST_AND_CLEAR      6 (p)
        # |                SWAP                     2
        # |        L3:     BUILD_SET                0
        # |                SWAP                     2
        # |        L4:     FOR_ITER                14 (to L5)
        # |                STORE_FAST_LOAD_FAST   102 (p, p)
        # |                LOAD_ATTR               16 (name)
        # |                SET_ADD                  2
        # |                JUMP_BACKWARD           16 (to L4)
        # |        L5:     END_FOR
        # |                POP_ITER
        # |        L6:     STORE_FAST               7 (@py_assert0)
        # |                STORE_FAST               6 (p)
        # |  102           LOAD_CONST              10 ('ch_003.v01')
        # |                LOAD_CONST              11 ('ch_003.v02')
        # |  101           BUILD_SET                2
        # |                STORE_FAST_LOAD_FAST   135 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |  102           LOAD_ATTR               20 (_call_reprcompare)
        # |  101           PUSH_NULL
        # |                LOAD_CONST              16 (('==',))
        # |                LOAD_FAST_BORROW         9 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              12 ('py1')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |  102           LOAD_ATTR               22 (_saferepr)
        # |  101           PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py4')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |  102           LOAD_ATTR               22 (_saferepr)
        # |  101           PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format5)
        # |                LOAD_CONST              14 ('assert %(py6)s')
        # |                LOAD_CONST              15 ('py6')
        # |                LOAD_FAST_BORROW        10 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format7)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |  102           LOAD_ATTR               26 (_format_explanation)
        # |  101           PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST               1 (None)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  152 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L8:     SWAP                     2
        # |                POP_TOP
        # |  101           SWAP                     2
        # |                STORE_FAST               6 (p)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L3 to L6 -> L8 [2]

