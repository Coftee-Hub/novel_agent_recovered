# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py
# 来源   : test_cli_graph.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = 'CLI 走图这条路的接线。\n\n`build_graph` + SqliteSaver 早就写好了，但 CLI 一直直调 pipeline —— 结果\ncheckpoint 形同虚设，第 3 章两次崩在缝合都得从出细纲重来。所以这里测的不是\n图本身（那是 test_graph.py 的事），而是**CLI 有没有真的走上去**。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'CLI 走图这条路的接线。\n\n`build_graph` + SqliteSaver 早就写好了，但 CLI 一直直调 pipeline —— 结果\ncheckpoint 形同虚设，第 3 章两次崩在缝合都得从出细纲重来。所以这里测的不是\n图本身（那是 test_graph.py 的事），而是**CLI 有没有真的走上去**。\n',
    9: 'config',
    10: 'project.yaml',
    14: 'TestGraphPath',
    16: 'TestStaleOutlineGuard',
    18: 'TestThreadHygiene',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('pipeline', 0): '场景一',
    ('pipeline', 1): '场景二',
    ('TestGraphPath', 0): 'TestGraphPath',
    ('test_returns_a_result_the_cli_can_use', 0): 'write 命令拿到手就要能落盘、能归档、能报错 —— 字段必须齐。',
    ('test_returns_a_result_the_cli_can_use', 2): 'cp.sqlite',
    ('test_returns_a_result_the_cli_can_use', 4): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_returns_a_result_the_cli_can_use', 5): 'py0',
    ('test_returns_a_result_the_cli_can_use', 6): 'r',
    ('test_returns_a_result_the_cli_can_use', 7): 'py2',
    ('test_returns_a_result_the_cli_can_use', 9): 'py4',
    ('test_returns_a_result_the_cli_can_use', 10): 'GOOD',
    ('test_returns_a_result_the_cli_can_use', 11): 'assert %(py6)s',
    ('test_returns_a_result_the_cli_can_use', 12): 'py6',
    ('test_returns_a_result_the_cli_can_use', 13): 'py5',
    ('test_returns_a_result_the_cli_can_use', 14): 'assert %(py7)s',
    ('test_returns_a_result_the_cli_can_use', 15): 'py7',
    ('test_returns_a_result_the_cli_can_use', 17): '%(py9)s',
    ('test_returns_a_result_the_cli_can_use', 18): 'py9',
    ('test_returns_a_result_the_cli_can_use', 19): '%(py15)s\n{%(py15)s = %(py11)s(%(py13)s)\n}',
    ('test_returns_a_result_the_cli_can_use', 20): 'py11',
    ('test_returns_a_result_the_cli_can_use', 21): 'any',
    ('test_returns_a_result_the_cli_can_use', 22): 'py13',
    ('test_returns_a_result_the_cli_can_use', 23): 'py15',
    ('test_returns_a_result_the_cli_can_use', 24): 'assert %(py18)s',
    ('test_returns_a_result_the_cli_can_use', 25): 'py18',
    ('test_returns_a_result_the_cli_can_use', 26): 'assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}',
    ('test_crash_then_rerun_resumes', 0): '第 3 章的真实剧本：三场写完，缝合崩掉，重跑一次。',
    ('test_crash_then_rerun_resumes', 2): 'Flaky',
    ('test_crash_then_rerun_resumes', 3): 'cp.sqlite',
    ('test_crash_then_rerun_resumes', 7): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_crash_then_rerun_resumes', 8): 'py0',
    ('test_crash_then_rerun_resumes', 9): 'r',
    ('test_crash_then_rerun_resumes', 10): 'py2',
    ('test_crash_then_rerun_resumes', 11): 'p',
    ('test_crash_then_rerun_resumes', 12): 'py4',
    ('test_crash_then_rerun_resumes', 13): 'py7',
    ('test_crash_then_rerun_resumes', 14): '重跑不该重出细纲',
    ('test_crash_then_rerun_resumes', 15): '\n>assert %(py9)s',
    ('test_crash_then_rerun_resumes', 16): 'py9',
    ('test_crash_then_rerun_resumes', 17): '重跑不该重写场景',
    ('Flaky', 0): 'TestGraphPath.test_crash_then_rerun_resumes.<locals>.Flaky',
    ('stitch', 1): '上游 403',
    ('test_confirmed_outline_is_not_replanned', 3): 'cp.sqlite',
    ('test_confirmed_outline_is_not_replanned', 5): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_confirmed_outline_is_not_replanned', 6): 'py0',
    ('test_confirmed_outline_is_not_replanned', 7): 'r',
    ('test_confirmed_outline_is_not_replanned', 8): 'py2',
    ('test_confirmed_outline_is_not_replanned', 10): 'p',
    ('test_confirmed_outline_is_not_replanned', 11): 'py4',
    ('test_confirmed_outline_is_not_replanned', 12): 'py7',
    ('test_confirmed_outline_is_not_replanned', 13): '人确认过的细纲不该被重出一份盖掉',
    ('test_confirmed_outline_is_not_replanned', 14): '\n>assert %(py9)s',
    ('test_confirmed_outline_is_not_replanned', 15): 'py9',
    ('test_drafts_seed_the_scenes', 2): '草稿一',
    ('test_drafts_seed_the_scenes', 3): '草稿二',
    ('test_drafts_seed_the_scenes', 4): 'cp.sqlite',
    ('test_drafts_seed_the_scenes', 6): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_drafts_seed_the_scenes', 7): 'py0',
    ('test_drafts_seed_the_scenes', 8): 'r',
    ('test_drafts_seed_the_scenes', 9): 'py2',
    ('test_drafts_seed_the_scenes', 11): 'p',
    ('test_drafts_seed_the_scenes', 12): 'py4',
    ('test_drafts_seed_the_scenes', 13): 'py7',
    ('test_drafts_seed_the_scenes', 14): '草稿齐了就不该再调 writer',
    ('test_drafts_seed_the_scenes', 15): '\n>assert %(py9)s',
    ('test_drafts_seed_the_scenes', 16): 'py9',
    ('test_chapters_do_not_share_a_thread', 0): '第 4 章不能捡起第 3 章的残局。',
    ('test_chapters_do_not_share_a_thread', 1): 'cp.sqlite',
    ('test_chapters_do_not_share_a_thread', 4): 'py0',
    ('test_chapters_do_not_share_a_thread', 5): 'r',
    ('test_chapters_do_not_share_a_thread', 6): 'py2',
    ('test_chapters_do_not_share_a_thread', 7): 'py5',
    ('test_chapters_do_not_share_a_thread', 8): 'assert %(py7)s',
    ('test_chapters_do_not_share_a_thread', 9): 'py7',
    ('test_chapters_do_not_share_a_thread', 11): 'p2',
    ('test_chapters_do_not_share_a_thread', 12): 'py4',
    ('test_chapters_do_not_share_a_thread', 13): '另一章要自己出细纲',
    ('test_chapters_do_not_share_a_thread', 14): '\n>assert %(py9)s',
    ('test_chapters_do_not_share_a_thread', 15): 'py9',
    ('TestStaleOutlineGuard', 0): 'TestStaleOutlineGuard',
    ('TestStaleOutlineGuard', 1): '细纲被人改过之后再跑，绝不能默默续上照着旧细纲写的那份存档 ——\n第 3 章正是「细纲把心理描写禁掉了」才要改，续旧档等于修改白做。',
    ('_crash_then', 3): 'Flaky',
    ('_crash_then', 4): 'cp.sqlite',
    ('Flaky', 0): 'TestStaleOutlineGuard._crash_then.<locals>.Flaky',
    ('stitch', 1): '上游 403',
    ('test_changed_outline_starts_over', 2): '这一场要写足心理活动',
    ('test_changed_outline_starts_over', 3): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_changed_outline_starts_over', 4): 'py0',
    ('test_changed_outline_starts_over', 5): 'r',
    ('test_changed_outline_starts_over', 6): 'py2',
    ('test_changed_outline_starts_over', 8): 'p2',
    ('test_changed_outline_starts_over', 9): 'py4',
    ('test_changed_outline_starts_over', 10): 'py7',
    ('test_changed_outline_starts_over', 11): '按新细纲重写，而不是捡旧场景续跑',
    ('test_changed_outline_starts_over', 12): '\n>assert %(py9)s',
    ('test_changed_outline_starts_over', 13): 'py9',
    ('test_changed_outline_starts_over', 14): 'ch001_s1',
    ('test_changed_outline_starts_over', 15): 'ch001_s2',
    ('test_changed_outline_starts_over', 16): 'assert %(py9)s',
    ('test_unchanged_outline_still_resumes', 0): '没改就该续 —— 否则 checkpoint 白建了。',
    ('test_unchanged_outline_still_resumes', 2): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_unchanged_outline_still_resumes', 3): 'py0',
    ('test_unchanged_outline_still_resumes', 4): 'r',
    ('test_unchanged_outline_still_resumes', 5): 'py2',
    ('test_unchanged_outline_still_resumes', 7): 'p2',
    ('test_unchanged_outline_still_resumes', 8): 'py4',
    ('test_unchanged_outline_still_resumes', 9): 'py6',
    ('test_unchanged_outline_still_resumes', 10): 'py9',
    ('test_unchanged_outline_still_resumes', 11): '%(py11)s',
    ('test_unchanged_outline_still_resumes', 12): 'py11',
    ('test_unchanged_outline_still_resumes', 13): 'py13',
    ('test_unchanged_outline_still_resumes', 14): 'py15',
    ('test_unchanged_outline_still_resumes', 15): 'py17',
    ('test_unchanged_outline_still_resumes', 16): 'py20',
    ('test_unchanged_outline_still_resumes', 17): '%(py22)s',
    ('test_unchanged_outline_still_resumes', 18): 'py22',
    ('test_unchanged_outline_still_resumes', 19): 'assert %(py25)s',
    ('test_unchanged_outline_still_resumes', 20): 'py25',
    ('TestThreadHygiene', 0): 'TestThreadHygiene',
    ('TestThreadHygiene', 1): 'LangGraph 的线程状态是累积的：往一条**已经跑完**的线程再 invoke，\nseed 只是合并进旧状态，`revisions` 还停在上次的 2 —— 新一轮缝合完、\ngate 一失败就直接判"修订 2 轮后仍未通过"，一轮修订都不做。\n实测连着两次跑各花 $0.05，什么都没修。',
    ('test_a_finished_run_does_not_poison_the_next_one', 2): 'cp.sqlite',
    ('test_a_finished_run_does_not_poison_the_next_one', 7): 'not %(py4)s\n{%(py4)s = %(py2)s.passed\n}',
    ('test_a_finished_run_does_not_poison_the_next_one', 8): 'py2',
    ('test_a_finished_run_does_not_poison_the_next_one', 9): 'r1',
    ('test_a_finished_run_does_not_poison_the_next_one', 10): 'py4',
    ('test_a_finished_run_does_not_poison_the_next_one', 11): 'py7',
    ('test_a_finished_run_does_not_poison_the_next_one', 12): 'py9',
    ('test_a_finished_run_does_not_poison_the_next_one', 13): 'py12',
    ('test_a_finished_run_does_not_poison_the_next_one', 14): '%(py14)s',
    ('test_a_finished_run_does_not_poison_the_next_one', 15): 'py14',
    ('test_a_finished_run_does_not_poison_the_next_one', 16): 'assert %(py17)s',
    ('test_a_finished_run_does_not_poison_the_next_one', 17): 'py17',
    ('test_a_finished_run_does_not_poison_the_next_one', 20): '新一轮不该继承上一轮用完的修订次数',
    ('test_a_finished_run_does_not_poison_the_next_one', 21): '\n>assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_a_finished_run_does_not_poison_the_next_one', 22): 'py0',
    ('test_a_finished_run_does_not_poison_the_next_one', 23): 'r2',
    ('test_a_finished_run_does_not_poison_the_next_one', 24): '该真的修订过',
    ('test_a_finished_run_does_not_poison_the_next_one', 25): '\n>assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.revised\n}',
    ('test_a_finished_run_does_not_poison_the_next_one', 26): 'p2',
    ('test_an_unfinished_run_is_still_resumed', 0): '别把澡盆里的孩子一起倒掉：没跑完的存档仍然要续。',
    ('test_an_unfinished_run_is_still_resumed', 3): 'Flaky',
    ('test_an_unfinished_run_is_still_resumed', 4): 'cp.sqlite',
    ('test_an_unfinished_run_is_still_resumed', 8): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_an_unfinished_run_is_still_resumed', 9): 'py0',
    ('test_an_unfinished_run_is_still_resumed', 10): 'r',
    ('test_an_unfinished_run_is_still_resumed', 11): 'py2',
    ('test_an_unfinished_run_is_still_resumed', 12): 'p2',
    ('test_an_unfinished_run_is_still_resumed', 13): 'py4',
    ('test_an_unfinished_run_is_still_resumed', 14): 'py7',
    ('test_an_unfinished_run_is_still_resumed', 15): '续跑不该重写场景',
    ('test_an_unfinished_run_is_still_resumed', 16): '\n>assert %(py9)s',
    ('test_an_unfinished_run_is_still_resumed', 17): 'py9',
    ('Flaky', 0): 'TestThreadHygiene.test_an_unfinished_run_is_still_resumed.<locals>.Flaky',
    ('stitch', 1): '上游 403',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def pipeline(stitcher):
    '场景一'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  29           RESUME                   0
    # |  30           LOAD_GLOBAL              1 (ChapterPipeline + NULL)
    # |  31           LOAD_GLOBAL              3 (FakeArchitect + NULL)
    # |               CALL                     0
    # |               LOAD_GLOBAL              5 (FakeWriter + NULL)
    # |               LOAD_CONST               0 ('场景一')
    # |               LOAD_CONST               1 ('场景二')
    # |               BUILD_LIST               2
    # |               CALL                     1
    # |  32           LOAD_FAST                0 (stitcher)
    # |               COPY                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE        17 (to L1)
    # |               NOT_TAKEN
    # |               POP_TOP
    # |               LOAD_GLOBAL              7 (FakeStitcher + NULL)
    # |               LOAD_GLOBAL              8 (GOOD)
    # |               BUILD_LIST               1
    # |               CALL                     1
    # |       L1:     LOAD_GLOBAL             10 (Gate)
    # |               LOAD_ATTR               12 (from_config)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             14 (CONFIG)
    # |               CALL                     1
    # |  33           LOAD_GLOBAL             17 (FakeJudge + NULL)
    # |               LOAD_GLOBAL             18 (PASS)
    # |               BUILD_LIST               1
    # |               CALL                     1
    # |               LOAD_GLOBAL             21 (FakeArchivist + NULL)
    # |               CALL                     0
    # |  34           LOAD_SMALL_INT           2
    # |               LOAD_CONST               2 (<code object <lambda> at 0x1062bddf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 34>)
    # |               MAKE_FUNCTION
    # |  30           LOAD_CONST               3 (('architect', 'writer', 'stitcher', 'gate', 'judge', 'archivist', 'max_revisions', 'log'))
    # |               CALL_KW                  8
    # |               RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x1062bddf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 34>:
    # |  34           RESUME                   0
    # |               LOAD_CONST               0 (None)
    # |               RETURN_VALUE

class TestGraphPath:
    'TestGraphPath'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  37           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestGraphPath')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          37
    # |               STORE_NAME               3 (__firstlineno__)
    # |  38           LOAD_CONST               1 (<code object test_returns_a_result_the_cli_can_use at 0x78f12c5c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 38>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_returns_a_result_the_cli_can_use)
    # |  49           LOAD_CONST               2 (<code object test_crash_then_rerun_resumes at 0x78f1097000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 49>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_crash_then_rerun_resumes)
    # |  68           LOAD_CONST               3 (<code object test_confirmed_outline_is_not_replanned at 0x78f0d8e300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 68>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_confirmed_outline_is_not_replanned)
    # |  77           LOAD_CONST               4 (<code object test_drafts_seed_the_scenes at 0x78f0d8ed00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 77>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_drafts_seed_the_scenes)
    # |  85           LOAD_CONST               5 (<code object test_chapters_do_not_share_a_thread at 0x78f12c1200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 85>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_chapters_do_not_share_a_thread)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_returns_a_result_the_cli_can_use at 0x78f12c5c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 38>:
    # |  38            RESUME                   0
    # |  40            LOAD_GLOBAL              1 (run_via_graph + NULL)
    # |                LOAD_GLOBAL              3 (pipeline + NULL)
    # |                CALL                     0
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                LOAD_GLOBAL              5 (volume + NULL)
    # |                CALL                     0
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               1 ('')
    # |  41            LOAD_FAST_BORROW         2 (tmp_path)
    # |                LOAD_CONST               2 ('cp.sqlite')
    # |                BINARY_OP               11 (/)
    # |  40            LOAD_CONST               3 (('note', 'checkpoint_db'))
    # |                CALL_KW                  6
    # |                STORE_FAST               3 (r)
    # |  42            LOAD_FAST_BORROW         3 (r)
    # |                LOAD_ATTR                6 (passed)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       141 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_CONST               4 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('r')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               6 ('r')
    # |        L3:     LOAD_CONST               7 ('py2')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format3)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_format3)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               8 (None)
    # |                STORE_FAST               4 (@py_assert1)
    # |  43            LOAD_FAST_BORROW         3 (r)
    # |                LOAD_ATTR               22 (text)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |                LOAD_GLOBAL             24 (GOOD)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       268 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               26 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              27 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              28 (('%(py2)s\n{%(py2)s = %(py0)s.text\n} == %(py4)s',))
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                LOAD_GLOBAL             24 (GOOD)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('r')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               6 ('r')
    # |        L7:     LOAD_CONST               7 ('py2')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py4')
    # |                LOAD_CONST              10 ('GOOD')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             24 (GOOD)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             24 (GOOD)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST              10 ('GOOD')
    # |       L10:     BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format5)
    # |                LOAD_CONST              11 ('assert %(py6)s')
    # |                LOAD_CONST              12 ('py6')
    # |                LOAD_FAST_BORROW         7 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format7)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L11:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   70 (@py_assert1, @py_assert3)
    # |  44            LOAD_FAST_BORROW         3 (r)
    # |                LOAD_ATTR               28 (revisions)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                STORE_FAST_LOAD_FAST   148 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L15)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               26 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              27 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              29 (('%(py2)s\n{%(py2)s = %(py0)s.revisions\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('r')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L13)
    # |                NOT_TAKEN
    # |       L12:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L14)
    # |       L13:     LOAD_CONST               6 ('r')
    # |       L14:     LOAD_CONST               7 ('py2')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py5')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format6)
    # |                LOAD_CONST              14 ('assert %(py7)s')
    # |                LOAD_CONST              15 ('py7')
    # |                LOAD_FAST_BORROW        10 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format8)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L15:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  105 (@py_assert3, @py_assert4)
    # |  45            BUILD_LIST               0
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert1, r)
    # |                LOAD_ATTR               30 (state)
    # |                STORE_FAST               6 (@py_assert3)
    # |                LOAD_CONST               8 (None)
    # |                STORE_FAST_LOAD_FAST   198 (@py_assert6, @py_assert3)
    # |                LOAD_FAST_BORROW        12 (@py_assert6)
    # |                IS_OP                    1 (is not)
    # |                STORE_FAST_LOAD_FAST   221 (@py_assert5, @py_assert5)
    # |                STORE_FAST_LOAD_FAST   237 (@py_assert0, @py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       43 (to L16)
    # |                NOT_TAKEN
    # |                LOAD_CONST              16 (<code object <genexpr> at 0x10626bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 45>)
    # |                MAKE_FUNCTION
    # |  46            LOAD_FAST_BORROW         3 (r)
    # |                LOAD_ATTR               30 (state)
    # |                LOAD_ATTR               32 (chapter_summaries)
    # |                GET_ITER
    # |  45            CALL                     0
    # |                STORE_FAST              15 (@py_assert12)
    # |                LOAD_GLOBAL             35 (any + NULL)
    # |                LOAD_FAST_BORROW        15 (@py_assert12)
    # |                CALL                     1
    # |                STORE_FAST              16 (@py_assert14)
    # |                LOAD_FAST               16 (@py_assert14)
    # |                STORE_FAST              14 (@py_assert0)
    # |       L16:     LOAD_FAST_BORROW        14 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       421 (to L24)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               26 (_call_reprcompare)
    # |  45            PUSH_NULL
    # |                LOAD_CONST              30 (('is not',))
    # |                LOAD_FAST_BORROW        13 (@py_assert5)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              31 (('%(py4)s\n{%(py4)s = %(py2)s.state\n} is not %(py7)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 108 (@py_assert3, @py_assert6)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               7 ('py2')
    # |                LOAD_CONST               6 ('r')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |  46            LOAD_ATTR               10 (locals)
    # |  45            PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L17)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               14 (_should_repr_global_name)
    # |  45            PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L18)
    # |                NOT_TAKEN
    # |       L17:     LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               16 (_saferepr)
    # |  45            PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L19)
    # |       L18:     LOAD_CONST               6 ('r')
    # |       L19:     LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               16 (_saferepr)
    # |  45            PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py7')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               16 (_saferepr)
    # |  45            PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert6)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format8)
    # |                LOAD_CONST              17 ('%(py9)s')
    # |                LOAD_CONST              18 ('py9')
    # |                LOAD_FAST_BORROW        11 (@py_format8)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format10)
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |  46            LOAD_ATTR               37 (append + NULL|self)
    # |  45            LOAD_FAST_BORROW        17 (@py_format10)
    # |  46            CALL                     1
    # |                POP_TOP
    # |  45            LOAD_FAST_BORROW        13 (@py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      157 (to L23)
    # |                NOT_TAKEN
    # |                LOAD_CONST              19 ('%(py15)s\n{%(py15)s = %(py11)s(%(py13)s)\n}')
    # |                LOAD_CONST              20 ('py11')
    # |                LOAD_CONST              21 ('any')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |  46            LOAD_ATTR               10 (locals)
    # |  45            PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L20)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               14 (_should_repr_global_name)
    # |  45            PUSH_NULL
    # |                LOAD_GLOBAL             34 (any)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L21)
    # |                NOT_TAKEN
    # |       L20:     LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               16 (_saferepr)
    # |  45            PUSH_NULL
    # |                LOAD_GLOBAL             34 (any)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L22)
    # |       L21:     LOAD_CONST              21 ('any')
    # |       L22:     LOAD_CONST              22 ('py13')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               16 (_saferepr)
    # |  45            PUSH_NULL
    # |                LOAD_FAST_CHECK         15 (@py_assert12)
    # |                CALL                     1
    # |                LOAD_CONST              23 ('py15')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               16 (_saferepr)
    # |  45            PUSH_NULL
    # |                LOAD_FAST_CHECK         16 (@py_assert14)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format16)
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |  46            LOAD_ATTR               37 (append + NULL|self)
    # |  45            LOAD_FAST_BORROW        18 (@py_format16)
    # |  46            CALL                     1
    # |                POP_TOP
    # |  45   L23:     LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               38 (_format_boolop)
    # |  45            PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              19 (@py_format17)
    # |                LOAD_CONST              24 ('assert %(py18)s')
    # |                LOAD_CONST              25 ('py18')
    # |                LOAD_FAST_BORROW        19 (@py_format17)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              20 (@py_format19)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |  46            LOAD_ATTR               20 (_format_explanation)
    # |  45            PUSH_NULL
    # |                LOAD_FAST_BORROW        20 (@py_format19)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L24:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST              14 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST              12 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST              15 (@py_assert12)
    # |                STORE_FAST              16 (@py_assert14)
    # |  47            LOAD_FAST_BORROW         3 (r)
    # |                LOAD_ATTR               40 (gate)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |                LOAD_ATTR                6 (passed)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       163 (to L28)
    # |                NOT_TAKEN
    # |                LOAD_CONST              26 ('assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}')
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('r')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L25)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L26)
    # |                NOT_TAKEN
    # |       L25:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L27)
    # |       L26:     LOAD_CONST               6 ('r')
    # |       L27:     LOAD_CONST               7 ('py2')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format5)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format5)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L28:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   70 (@py_assert1, @py_assert3)
    # |                LOAD_CONST               8 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10626bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 45>:
    # |   45           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |   46   L2:     FOR_ITER                19 (to L3)
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
    # | Disassembly of <code object test_crash_then_rerun_resumes at 0x78f1097000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 49>:
    # |   49            RESUME                   0
    # |   51            LOAD_BUILD_CLASS
    # |                 PUSH_NULL
    # |                 LOAD_CONST               1 (<code object Flaky at 0x1061e7430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 51>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_CONST               2 ('Flaky')
    # |                 CALL                     2
    # |                 STORE_FAST               3 (Flaky)
    # |   59            LOAD_GLOBAL              1 (pipeline + NULL)
    # |                 LOAD_FAST_BORROW         3 (Flaky)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 LOAD_FAST_BORROW         2 (tmp_path)
    # |                 LOAD_CONST               3 ('cp.sqlite')
    # |                 BINARY_OP               11 (/)
    # |                 STORE_FAST_STORE_FAST   84 (db, p)
    # |   60            LOAD_GLOBAL              2 (pytest)
    # |                 LOAD_ATTR                4 (raises)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              6 (RuntimeError)
    # |                 CALL                     1
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     POP_TOP
    # |   61            LOAD_GLOBAL              9 (run_via_graph + NULL)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (p, sample_state)
    # |                 LOAD_GLOBAL             11 (volume + NULL)
    # |                 CALL                     0
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_CONST               4 ('')
    # |                 LOAD_FAST_BORROW         5 (db)
    # |                 LOAD_CONST               5 (('note', 'checkpoint_db'))
    # |                 CALL_KW                  6
    # |                 POP_TOP
    # |   60    L2:     LOAD_CONST               6 (None)
    # |                 LOAD_CONST               6 (None)
    # |                 LOAD_CONST               6 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |   63    L3:     LOAD_GLOBAL              9 (run_via_graph + NULL)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (p, sample_state)
    # |                 LOAD_GLOBAL             11 (volume + NULL)
    # |                 CALL                     0
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_CONST               4 ('')
    # |                 LOAD_FAST_BORROW         5 (db)
    # |                 LOAD_CONST               5 (('note', 'checkpoint_db'))
    # |                 CALL_KW                  6
    # |                 STORE_FAST               6 (r)
    # |   64            LOAD_FAST_BORROW         6 (r)
    # |                 LOAD_ATTR               12 (passed)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       141 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_CONST               7 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |                 LOAD_CONST               8 ('py0')
    # |                 LOAD_CONST               9 ('r')
    # |                 LOAD_GLOBAL             14 (@py_builtins)
    # |                 LOAD_ATTR               16 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (r)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (r)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               9 ('r')
    # |         L6:     LOAD_CONST              10 ('py2')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert1)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format3)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_format3)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST               6 (None)
    # |                 STORE_FAST               7 (@py_assert1)
    # |   65            LOAD_FAST_BORROW         4 (p)
    # |                 LOAD_ATTR               28 (architect)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
    # |                 LOAD_ATTR               30 (calls)
    # |                 STORE_FAST               9 (@py_assert3)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST_LOAD_FAST   169 (@py_assert6, @py_assert3)
    # |                 LOAD_FAST_BORROW        10 (@py_assert6)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   187 (@py_assert5, @py_assert5)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       248 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              18 (('==',))
    # |                 LOAD_FAST_BORROW        11 (@py_assert5)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              19 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.architect\n}.calls\n} == %(py7)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert3, @py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               8 ('py0')
    # |                 LOAD_CONST              11 ('p')
    # |                 LOAD_GLOBAL             14 (@py_builtins)
    # |                 LOAD_ATTR               16 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (p)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (p)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST              11 ('p')
    # |        L10:     LOAD_CONST              10 ('py2')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py4')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST              13 ('py7')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format8)
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               34 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              14 ('重跑不该重出细纲')
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('\n>assert %(py9)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              16 ('py9')
    # |                 LOAD_FAST_BORROW        12 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format10)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST               6 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               7 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST               9 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  186 (@py_assert5, @py_assert6)
    # |   66            LOAD_FAST_BORROW         4 (p)
    # |                 LOAD_ATTR               36 (writer)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
    # |                 LOAD_ATTR               30 (calls)
    # |                 STORE_FAST               9 (@py_assert3)
    # |                 LOAD_SMALL_INT           1
    # |                 STORE_FAST_LOAD_FAST   169 (@py_assert6, @py_assert3)
    # |                 LOAD_FAST_BORROW        10 (@py_assert6)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   187 (@py_assert5, @py_assert5)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       248 (to L15)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              18 (('==',))
    # |                 LOAD_FAST_BORROW        11 (@py_assert5)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              20 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.calls\n} == %(py7)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert3, @py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               8 ('py0')
    # |                 LOAD_CONST              11 ('p')
    # |                 LOAD_GLOBAL             14 (@py_builtins)
    # |                 LOAD_ATTR               16 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L12)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (p)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L13)
    # |                 NOT_TAKEN
    # |        L12:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (p)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L14)
    # |        L13:     LOAD_CONST              11 ('p')
    # |        L14:     LOAD_CONST              10 ('py2')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py4')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST              13 ('py7')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format8)
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               34 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              17 ('重跑不该重写场景')
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('\n>assert %(py9)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              16 ('py9')
    # |                 LOAD_FAST_BORROW        12 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format10)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L15:     LOAD_CONST               6 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               7 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST               9 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  186 (@py_assert5, @py_assert6)
    # |                 LOAD_CONST               6 (None)
    # |                 RETURN_VALUE
    # |   60   L16:     PUSH_EXC_INFO
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
    # |                 EXTENDED_ARG             3
    # |                 JUMP_BACKWARD_NO_INTERRUPT 784 (to L3)
    # |   --   L19:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L16 [2] lasti
    # |   L16 to L18 -> L19 [4] lasti
    # | Disassembly of <code object Flaky at 0x1061e7430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 51>:
    # |  51           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestGraphPath.test_crash_then_rerun_resumes.<locals>.Flaky')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          51
    # |               STORE_NAME               3 (__firstlineno__)
    # |  52           LOAD_CONST               1 (<code object __init__ at 0x1062065b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 52>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (__init__)
    # |  53           LOAD_CONST               2 (<code object stitch at 0x10622f360, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 53>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (stitch)
    # |               LOAD_CONST               3 (('calls',))
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x1062065b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 52>:
    # |  52           RESUME                   0
    # |               LOAD_SMALL_INT           0
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               0 (calls)
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object stitch at 0x10622f360, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 53>:
    # |  53           RESUME                   0
    # |  54           LOAD_FAST_BORROW         0 (self)
    # |               COPY                     1
    # |               LOAD_ATTR                0 (calls)
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               13 (+=)
    # |               SWAP                     2
    # |               STORE_ATTR               0 (calls)
    # |  55           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (calls)
    # |               LOAD_SMALL_INT           1
    # |               COMPARE_OP              88 (bool(==))
    # |               POP_JUMP_IF_FALSE       12 (to L1)
    # |               NOT_TAKEN
    # |  56           LOAD_GLOBAL              3 (RuntimeError + NULL)
    # |               LOAD_CONST               1 ('上游 403')
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |  57   L1:     LOAD_GLOBAL              4 (GOOD)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_confirmed_outline_is_not_replanned at 0x78f0d8e300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 68>:
    # |  68           RESUME                   0
    # |  69           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('outline',))
    # |               IMPORT_NAME              0 (test_pipeline)
    # |               IMPORT_FROM              1 (outline)
    # |               STORE_FAST               3 (outline)
    # |               POP_TOP
    # |  71           LOAD_GLOBAL              5 (pipeline + NULL)
    # |               CALL                     0
    # |               STORE_FAST               4 (p)
    # |  72           LOAD_GLOBAL              7 (run_via_graph + NULL)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (p, sample_state)
    # |               LOAD_GLOBAL              9 (volume + NULL)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               2 ('')
    # |  73           LOAD_FAST_BORROW         3 (outline)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               LOAD_FAST_BORROW         2 (tmp_path)
    # |               LOAD_CONST               3 ('cp.sqlite')
    # |               BINARY_OP               11 (/)
    # |  72           LOAD_CONST               4 (('note', 'outline', 'checkpoint_db'))
    # |               CALL_KW                  7
    # |               STORE_FAST               5 (r)
    # |  74           LOAD_FAST_BORROW         5 (r)
    # |               LOAD_ATTR               10 (passed)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       141 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               5 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |               LOAD_CONST               6 ('py0')
    # |               LOAD_CONST               7 ('r')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               7 ('r')
    # |       L3:     LOAD_CONST               8 ('py2')
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format3)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format3)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               STORE_FAST               6 (@py_assert1)
    # |  75           LOAD_FAST_BORROW         4 (p)
    # |               LOAD_ATTR               26 (architect)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
    # |               LOAD_ATTR               28 (calls)
    # |               STORE_FAST               8 (@py_assert3)
    # |               LOAD_SMALL_INT           0
    # |               STORE_FAST_LOAD_FAST   152 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         9 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       248 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               30 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW        10 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.architect\n}.calls\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               6 ('py0')
    # |               LOAD_CONST              10 ('p')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (p)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (p)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST              10 ('p')
    # |       L7:     LOAD_CONST               8 ('py2')
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py4')
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py7')
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format8)
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               32 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 ('人确认过的细纲不该被重出一份盖掉')
    # |               CALL                     1
    # |               LOAD_CONST              14 ('\n>assert %(py9)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST              15 ('py9')
    # |               LOAD_FAST_BORROW        11 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format10)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        12 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  169 (@py_assert5, @py_assert6)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_drafts_seed_the_scenes at 0x78f0d8ed00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 77>:
    # |  77           RESUME                   0
    # |  78           LOAD_GLOBAL              1 (pipeline + NULL)
    # |               CALL                     0
    # |               STORE_FAST               3 (p)
    # |  79           LOAD_GLOBAL              3 (run_via_graph + NULL)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (p, sample_state)
    # |               LOAD_GLOBAL              5 (volume + NULL)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               1 ('')
    # |  80           LOAD_CONST               2 ('草稿一')
    # |               LOAD_CONST               3 ('草稿二')
    # |               BUILD_LIST               2
    # |  81           LOAD_FAST_BORROW         2 (tmp_path)
    # |               LOAD_CONST               4 ('cp.sqlite')
    # |               BINARY_OP               11 (/)
    # |  79           LOAD_CONST               5 (('note', 'drafts', 'checkpoint_db'))
    # |               CALL_KW                  7
    # |               STORE_FAST               4 (r)
    # |  82           LOAD_FAST_BORROW         4 (r)
    # |               LOAD_ATTR                6 (passed)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       141 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               6 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |               LOAD_CONST               7 ('py0')
    # |               LOAD_CONST               8 ('r')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               8 ('r')
    # |       L3:     LOAD_CONST               9 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert1)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format3)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format3)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              10 (None)
    # |               STORE_FAST               5 (@py_assert1)
    # |  83           LOAD_FAST_BORROW         3 (p)
    # |               LOAD_ATTR               22 (writer)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
    # |               LOAD_ATTR               24 (wrote)
    # |               STORE_FAST               7 (@py_assert3)
    # |               BUILD_LIST               0
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         8 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       248 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               26 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              17 (('==',))
    # |               LOAD_FAST_BORROW         9 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.wrote\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py0')
    # |               LOAD_CONST              11 ('p')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (p)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (p)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST              11 ('p')
    # |       L7:     LOAD_CONST               9 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST              13 ('py7')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format8)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               28 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 ('草稿齐了就不该再调 writer')
    # |               CALL                     1
    # |               LOAD_CONST              15 ('\n>assert %(py9)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST              16 ('py9')
    # |               LOAD_FAST_BORROW        10 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format10)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  152 (@py_assert5, @py_assert6)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_chapters_do_not_share_a_thread at 0x78f12c1200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 85>:
    # |  85           RESUME                   0
    # |  87           LOAD_FAST_BORROW         2 (tmp_path)
    # |               LOAD_CONST               1 ('cp.sqlite')
    # |               BINARY_OP               11 (/)
    # |               STORE_FAST               3 (db)
    # |  88           LOAD_GLOBAL              1 (pipeline + NULL)
    # |               CALL                     0
    # |               STORE_FAST               4 (p)
    # |  89           LOAD_GLOBAL              3 (run_via_graph + NULL)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (p, sample_state)
    # |               LOAD_GLOBAL              5 (volume + NULL)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               2 ('')
    # |               LOAD_FAST_BORROW         3 (db)
    # |               LOAD_CONST               3 (('note', 'checkpoint_db'))
    # |               CALL_KW                  6
    # |               POP_TOP
    # |  90           LOAD_GLOBAL              1 (pipeline + NULL)
    # |               CALL                     0
    # |               STORE_FAST               5 (p2)
    # |  91           LOAD_GLOBAL              3 (run_via_graph + NULL)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 81 (p2, sample_state)
    # |               LOAD_GLOBAL              5 (volume + NULL)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           2
    # |               LOAD_CONST               2 ('')
    # |               LOAD_FAST_BORROW         3 (db)
    # |               LOAD_CONST               3 (('note', 'checkpoint_db'))
    # |               CALL_KW                  6
    # |               STORE_FAST               6 (r)
    # |  92           LOAD_FAST_BORROW         6 (r)
    # |               LOAD_ATTR                6 (ch)
    # |               STORE_FAST               7 (@py_assert1)
    # |               LOAD_SMALL_INT           2
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         8 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW         9 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.ch\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST               5 ('r')
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
    # |               LOAD_FAST_BORROW         6 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('r')
    # |       L3:     LOAD_CONST               6 ('py2')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py5')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format6)
    # |               LOAD_CONST               8 ('assert %(py7)s')
    # |               LOAD_CONST               9 ('py7')
    # |               LOAD_FAST_BORROW        10 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format8)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  152 (@py_assert3, @py_assert4)
    # |  93           LOAD_FAST_BORROW         5 (p2)
    # |               LOAD_ATTR               24 (architect)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
    # |               LOAD_ATTR               26 (calls)
    # |               STORE_FAST               9 (@py_assert3)
    # |               LOAD_SMALL_INT           1
    # |               STORE_FAST_LOAD_FAST   201 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW        12 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   221 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       248 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW        13 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.architect\n}.calls\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST              11 ('p2')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (p2)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (p2)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST              11 ('p2')
    # |       L7:     LOAD_CONST               6 ('py2')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py7')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        12 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format8)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               28 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 ('另一章要自己出细纲')
    # |               CALL                     1
    # |               LOAD_CONST              14 ('\n>assert %(py9)s')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST              15 ('py9')
    # |               LOAD_FAST_BORROW        11 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              14 (@py_format10)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        14 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  220 (@py_assert5, @py_assert6)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE

    def test_returns_a_result_the_cli_can_use(self, sample_state, tmp_path):
        'write 命令拿到手就要能落盘、能归档、能报错 —— 字段必须齐。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  38            RESUME                   0
        # |  40            LOAD_GLOBAL              1 (run_via_graph + NULL)
        # |                LOAD_GLOBAL              3 (pipeline + NULL)
        # |                CALL                     0
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                LOAD_GLOBAL              5 (volume + NULL)
        # |                CALL                     0
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               1 ('')
        # |  41            LOAD_FAST_BORROW         2 (tmp_path)
        # |                LOAD_CONST               2 ('cp.sqlite')
        # |                BINARY_OP               11 (/)
        # |  40            LOAD_CONST               3 (('note', 'checkpoint_db'))
        # |                CALL_KW                  6
        # |                STORE_FAST               3 (r)
        # |  42            LOAD_FAST_BORROW         3 (r)
        # |                LOAD_ATTR                6 (passed)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       141 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_CONST               4 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('r')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               6 ('r')
        # |        L3:     LOAD_CONST               7 ('py2')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format3)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_format3)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               8 (None)
        # |                STORE_FAST               4 (@py_assert1)
        # |  43            LOAD_FAST_BORROW         3 (r)
        # |                LOAD_ATTR               22 (text)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |                LOAD_GLOBAL             24 (GOOD)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       268 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               26 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              27 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              28 (('%(py2)s\n{%(py2)s = %(py0)s.text\n} == %(py4)s',))
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                LOAD_GLOBAL             24 (GOOD)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('r')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               6 ('r')
        # |        L7:     LOAD_CONST               7 ('py2')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py4')
        # |                LOAD_CONST              10 ('GOOD')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             24 (GOOD)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             24 (GOOD)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST              10 ('GOOD')
        # |       L10:     BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format5)
        # |                LOAD_CONST              11 ('assert %(py6)s')
        # |                LOAD_CONST              12 ('py6')
        # |                LOAD_FAST_BORROW         7 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format7)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L11:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   70 (@py_assert1, @py_assert3)
        # |  44            LOAD_FAST_BORROW         3 (r)
        # |                LOAD_ATTR               28 (revisions)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                STORE_FAST_LOAD_FAST   148 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L15)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               26 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              27 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              29 (('%(py2)s\n{%(py2)s = %(py0)s.revisions\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('r')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L13)
        # |                NOT_TAKEN
        # |       L12:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L14)
        # |       L13:     LOAD_CONST               6 ('r')
        # |       L14:     LOAD_CONST               7 ('py2')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py5')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format6)
        # |                LOAD_CONST              14 ('assert %(py7)s')
        # |                LOAD_CONST              15 ('py7')
        # |                LOAD_FAST_BORROW        10 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format8)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L15:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  105 (@py_assert3, @py_assert4)
        # |  45            BUILD_LIST               0
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert1, r)
        # |                LOAD_ATTR               30 (state)
        # |                STORE_FAST               6 (@py_assert3)
        # |                LOAD_CONST               8 (None)
        # |                STORE_FAST_LOAD_FAST   198 (@py_assert6, @py_assert3)
        # |                LOAD_FAST_BORROW        12 (@py_assert6)
        # |                IS_OP                    1 (is not)
        # |                STORE_FAST_LOAD_FAST   221 (@py_assert5, @py_assert5)
        # |                STORE_FAST_LOAD_FAST   237 (@py_assert0, @py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       43 (to L16)
        # |                NOT_TAKEN
        # |                LOAD_CONST              16 (<code object <genexpr> at 0x10626bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 45>)
        # |                MAKE_FUNCTION
        # |  46            LOAD_FAST_BORROW         3 (r)
        # |                LOAD_ATTR               30 (state)
        # |                LOAD_ATTR               32 (chapter_summaries)
        # |                GET_ITER
        # |  45            CALL                     0
        # |                STORE_FAST              15 (@py_assert12)
        # |                LOAD_GLOBAL             35 (any + NULL)
        # |                LOAD_FAST_BORROW        15 (@py_assert12)
        # |                CALL                     1
        # |                STORE_FAST              16 (@py_assert14)
        # |                LOAD_FAST               16 (@py_assert14)
        # |                STORE_FAST              14 (@py_assert0)
        # |       L16:     LOAD_FAST_BORROW        14 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       421 (to L24)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               26 (_call_reprcompare)
        # |  45            PUSH_NULL
        # |                LOAD_CONST              30 (('is not',))
        # |                LOAD_FAST_BORROW        13 (@py_assert5)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              31 (('%(py4)s\n{%(py4)s = %(py2)s.state\n} is not %(py7)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 108 (@py_assert3, @py_assert6)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               7 ('py2')
        # |                LOAD_CONST               6 ('r')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |  46            LOAD_ATTR               10 (locals)
        # |  45            PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L17)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               14 (_should_repr_global_name)
        # |  45            PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L18)
        # |                NOT_TAKEN
        # |       L17:     LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               16 (_saferepr)
        # |  45            PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L19)
        # |       L18:     LOAD_CONST               6 ('r')
        # |       L19:     LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               16 (_saferepr)
        # |  45            PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py7')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               16 (_saferepr)
        # |  45            PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert6)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format8)
        # |                LOAD_CONST              17 ('%(py9)s')
        # |                LOAD_CONST              18 ('py9')
        # |                LOAD_FAST_BORROW        11 (@py_format8)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format10)
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |  46            LOAD_ATTR               37 (append + NULL|self)
        # |  45            LOAD_FAST_BORROW        17 (@py_format10)
        # |  46            CALL                     1
        # |                POP_TOP
        # |  45            LOAD_FAST_BORROW        13 (@py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      157 (to L23)
        # |                NOT_TAKEN
        # |                LOAD_CONST              19 ('%(py15)s\n{%(py15)s = %(py11)s(%(py13)s)\n}')
        # |                LOAD_CONST              20 ('py11')
        # |                LOAD_CONST              21 ('any')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |  46            LOAD_ATTR               10 (locals)
        # |  45            PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L20)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               14 (_should_repr_global_name)
        # |  45            PUSH_NULL
        # |                LOAD_GLOBAL             34 (any)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L21)
        # |                NOT_TAKEN
        # |       L20:     LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               16 (_saferepr)
        # |  45            PUSH_NULL
        # |                LOAD_GLOBAL             34 (any)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L22)
        # |       L21:     LOAD_CONST              21 ('any')
        # |       L22:     LOAD_CONST              22 ('py13')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               16 (_saferepr)
        # |  45            PUSH_NULL
        # |                LOAD_FAST_CHECK         15 (@py_assert12)
        # |                CALL                     1
        # |                LOAD_CONST              23 ('py15')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               16 (_saferepr)
        # |  45            PUSH_NULL
        # |                LOAD_FAST_CHECK         16 (@py_assert14)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format16)
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |  46            LOAD_ATTR               37 (append + NULL|self)
        # |  45            LOAD_FAST_BORROW        18 (@py_format16)
        # |  46            CALL                     1
        # |                POP_TOP
        # |  45   L23:     LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               38 (_format_boolop)
        # |  45            PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              19 (@py_format17)
        # |                LOAD_CONST              24 ('assert %(py18)s')
        # |                LOAD_CONST              25 ('py18')
        # |                LOAD_FAST_BORROW        19 (@py_format17)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              20 (@py_format19)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |  46            LOAD_ATTR               20 (_format_explanation)
        # |  45            PUSH_NULL
        # |                LOAD_FAST_BORROW        20 (@py_format19)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L24:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST              14 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST              13 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST              12 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST              15 (@py_assert12)
        # |                STORE_FAST              16 (@py_assert14)
        # |  47            LOAD_FAST_BORROW         3 (r)
        # |                LOAD_ATTR               40 (gate)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |                LOAD_ATTR                6 (passed)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       163 (to L28)
        # |                NOT_TAKEN
        # |                LOAD_CONST              26 ('assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.gate\n}.passed\n}')
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('r')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L25)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L26)
        # |                NOT_TAKEN
        # |       L25:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L27)
        # |       L26:     LOAD_CONST               6 ('r')
        # |       L27:     LOAD_CONST               7 ('py2')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format5)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format5)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L28:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   70 (@py_assert1, @py_assert3)
        # |                LOAD_CONST               8 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x10626bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 45>:
        # |   45           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |   46   L2:     FOR_ITER                19 (to L3)
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

    def test_crash_then_rerun_resumes(self, sample_state, tmp_path):
        '第 3 章的真实剧本：三场写完，缝合崩掉，重跑一次。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   49            RESUME                   0
        # |   51            LOAD_BUILD_CLASS
        # |                 PUSH_NULL
        # |                 LOAD_CONST               1 (<code object Flaky at 0x1061e7430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 51>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_CONST               2 ('Flaky')
        # |                 CALL                     2
        # |                 STORE_FAST               3 (Flaky)
        # |   59            LOAD_GLOBAL              1 (pipeline + NULL)
        # |                 LOAD_FAST_BORROW         3 (Flaky)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CALL                     1
        # |                 LOAD_FAST_BORROW         2 (tmp_path)
        # |                 LOAD_CONST               3 ('cp.sqlite')
        # |                 BINARY_OP               11 (/)
        # |                 STORE_FAST_STORE_FAST   84 (db, p)
        # |   60            LOAD_GLOBAL              2 (pytest)
        # |                 LOAD_ATTR                4 (raises)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              6 (RuntimeError)
        # |                 CALL                     1
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     POP_TOP
        # |   61            LOAD_GLOBAL              9 (run_via_graph + NULL)
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (p, sample_state)
        # |                 LOAD_GLOBAL             11 (volume + NULL)
        # |                 CALL                     0
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_CONST               4 ('')
        # |                 LOAD_FAST_BORROW         5 (db)
        # |                 LOAD_CONST               5 (('note', 'checkpoint_db'))
        # |                 CALL_KW                  6
        # |                 POP_TOP
        # |   60    L2:     LOAD_CONST               6 (None)
        # |                 LOAD_CONST               6 (None)
        # |                 LOAD_CONST               6 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |   63    L3:     LOAD_GLOBAL              9 (run_via_graph + NULL)
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (p, sample_state)
        # |                 LOAD_GLOBAL             11 (volume + NULL)
        # |                 CALL                     0
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_CONST               4 ('')
        # |                 LOAD_FAST_BORROW         5 (db)
        # |                 LOAD_CONST               5 (('note', 'checkpoint_db'))
        # |                 CALL_KW                  6
        # |                 STORE_FAST               6 (r)
        # |   64            LOAD_FAST_BORROW         6 (r)
        # |                 LOAD_ATTR               12 (passed)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       141 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_CONST               7 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |                 LOAD_CONST               8 ('py0')
        # |                 LOAD_CONST               9 ('r')
        # |                 LOAD_GLOBAL             14 (@py_builtins)
        # |                 LOAD_ATTR               16 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (r)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (r)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               9 ('r')
        # |         L6:     LOAD_CONST              10 ('py2')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert1)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format3)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_format3)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST               6 (None)
        # |                 STORE_FAST               7 (@py_assert1)
        # |   65            LOAD_FAST_BORROW         4 (p)
        # |                 LOAD_ATTR               28 (architect)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
        # |                 LOAD_ATTR               30 (calls)
        # |                 STORE_FAST               9 (@py_assert3)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST_LOAD_FAST   169 (@py_assert6, @py_assert3)
        # |                 LOAD_FAST_BORROW        10 (@py_assert6)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   187 (@py_assert5, @py_assert5)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       248 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              18 (('==',))
        # |                 LOAD_FAST_BORROW        11 (@py_assert5)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              19 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.architect\n}.calls\n} == %(py7)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert3, @py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               8 ('py0')
        # |                 LOAD_CONST              11 ('p')
        # |                 LOAD_GLOBAL             14 (@py_builtins)
        # |                 LOAD_ATTR               16 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (p)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (p)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST              11 ('p')
        # |        L10:     LOAD_CONST              10 ('py2')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py4')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST              13 ('py7')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format8)
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               34 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              14 ('重跑不该重出细纲')
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('\n>assert %(py9)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              16 ('py9')
        # |                 LOAD_FAST_BORROW        12 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format10)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST               6 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               7 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST               9 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  186 (@py_assert5, @py_assert6)
        # |   66            LOAD_FAST_BORROW         4 (p)
        # |                 LOAD_ATTR               36 (writer)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
        # |                 LOAD_ATTR               30 (calls)
        # |                 STORE_FAST               9 (@py_assert3)
        # |                 LOAD_SMALL_INT           1
        # |                 STORE_FAST_LOAD_FAST   169 (@py_assert6, @py_assert3)
        # |                 LOAD_FAST_BORROW        10 (@py_assert6)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   187 (@py_assert5, @py_assert5)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       248 (to L15)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              18 (('==',))
        # |                 LOAD_FAST_BORROW        11 (@py_assert5)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              20 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.calls\n} == %(py7)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert3, @py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               8 ('py0')
        # |                 LOAD_CONST              11 ('p')
        # |                 LOAD_GLOBAL             14 (@py_builtins)
        # |                 LOAD_ATTR               16 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L12)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (p)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L13)
        # |                 NOT_TAKEN
        # |        L12:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (p)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L14)
        # |        L13:     LOAD_CONST              11 ('p')
        # |        L14:     LOAD_CONST              10 ('py2')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py4')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST              13 ('py7')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format8)
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               34 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              17 ('重跑不该重写场景')
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('\n>assert %(py9)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              16 ('py9')
        # |                 LOAD_FAST_BORROW        12 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format10)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L15:     LOAD_CONST               6 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               7 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST               9 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  186 (@py_assert5, @py_assert6)
        # |                 LOAD_CONST               6 (None)
        # |                 RETURN_VALUE
        # |   60   L16:     PUSH_EXC_INFO
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
        # |                 EXTENDED_ARG             3
        # |                 JUMP_BACKWARD_NO_INTERRUPT 784 (to L3)
        # |   --   L19:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L16 [2] lasti
        # |   L16 to L18 -> L19 [4] lasti
        # | Disassembly of <code object Flaky at 0x1061e7430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 51>:
        # |  51           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestGraphPath.test_crash_then_rerun_resumes.<locals>.Flaky')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT          51
        # |               STORE_NAME               3 (__firstlineno__)
        # |  52           LOAD_CONST               1 (<code object __init__ at 0x1062065b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 52>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               4 (__init__)
        # |  53           LOAD_CONST               2 (<code object stitch at 0x10622f360, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 53>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               5 (stitch)
        # |               LOAD_CONST               3 (('calls',))
        # |               STORE_NAME               6 (__static_attributes__)
        # |               LOAD_CONST               4 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object __init__ at 0x1062065b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 52>:
        # |  52           RESUME                   0
        # |               LOAD_SMALL_INT           0
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               0 (calls)
        # |               LOAD_CONST               1 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object stitch at 0x10622f360, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 53>:
        # |  53           RESUME                   0
        # |  54           LOAD_FAST_BORROW         0 (self)
        # |               COPY                     1
        # |               LOAD_ATTR                0 (calls)
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               13 (+=)
        # |               SWAP                     2
        # |               STORE_ATTR               0 (calls)
        # |  55           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (calls)
        # |               LOAD_SMALL_INT           1
        # |               COMPARE_OP              88 (bool(==))
        # |               POP_JUMP_IF_FALSE       12 (to L1)
        # |               NOT_TAKEN
        # |  56           LOAD_GLOBAL              3 (RuntimeError + NULL)
        # |               LOAD_CONST               1 ('上游 403')
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |  57   L1:     LOAD_GLOBAL              4 (GOOD)
        # |               RETURN_VALUE

        class Flaky:
            'TestGraphPath.test_crash_then_rerun_resumes.<locals>.Flaky'
            # ── 函数体（字节码重建见 BODY 段）──
            # |  51           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestGraphPath.test_crash_then_rerun_resumes.<locals>.Flaky')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT          51
            # |               STORE_NAME               3 (__firstlineno__)
            # |  52           LOAD_CONST               1 (<code object __init__ at 0x1062065b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 52>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               4 (__init__)
            # |  53           LOAD_CONST               2 (<code object stitch at 0x10622f360, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 53>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               5 (stitch)
            # |               LOAD_CONST               3 (('calls',))
            # |               STORE_NAME               6 (__static_attributes__)
            # |               LOAD_CONST               4 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object __init__ at 0x1062065b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 52>:
            # |  52           RESUME                   0
            # |               LOAD_SMALL_INT           0
            # |               LOAD_FAST_BORROW         0 (self)
            # |               STORE_ATTR               0 (calls)
            # |               LOAD_CONST               1 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object stitch at 0x10622f360, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 53>:
            # |  53           RESUME                   0
            # |  54           LOAD_FAST_BORROW         0 (self)
            # |               COPY                     1
            # |               LOAD_ATTR                0 (calls)
            # |               LOAD_SMALL_INT           1
            # |               BINARY_OP               13 (+=)
            # |               SWAP                     2
            # |               STORE_ATTR               0 (calls)
            # |  55           LOAD_FAST_BORROW         0 (self)
            # |               LOAD_ATTR                0 (calls)
            # |               LOAD_SMALL_INT           1
            # |               COMPARE_OP              88 (bool(==))
            # |               POP_JUMP_IF_FALSE       12 (to L1)
            # |               NOT_TAKEN
            # |  56           LOAD_GLOBAL              3 (RuntimeError + NULL)
            # |               LOAD_CONST               1 ('上游 403')
            # |               CALL                     1
            # |               RAISE_VARARGS            1
            # |  57   L1:     LOAD_GLOBAL              4 (GOOD)
            # |               RETURN_VALUE

            def __init__(self):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # |  52           RESUME                   0
                # |               LOAD_SMALL_INT           0
                # |               LOAD_FAST_BORROW         0 (self)
                # |               STORE_ATTR               0 (calls)
                # |               LOAD_CONST               1 (None)
                # |               RETURN_VALUE

            def stitch(self, o, scenes, **kw):
                '上游 403'
                # ── 函数体（字节码重建见 BODY 段）──
                # |  53           RESUME                   0
                # |  54           LOAD_FAST_BORROW         0 (self)
                # |               COPY                     1
                # |               LOAD_ATTR                0 (calls)
                # |               LOAD_SMALL_INT           1
                # |               BINARY_OP               13 (+=)
                # |               SWAP                     2
                # |               STORE_ATTR               0 (calls)
                # |  55           LOAD_FAST_BORROW         0 (self)
                # |               LOAD_ATTR                0 (calls)
                # |               LOAD_SMALL_INT           1
                # |               COMPARE_OP              88 (bool(==))
                # |               POP_JUMP_IF_FALSE       12 (to L1)
                # |               NOT_TAKEN
                # |  56           LOAD_GLOBAL              3 (RuntimeError + NULL)
                # |               LOAD_CONST               1 ('上游 403')
                # |               CALL                     1
                # |               RAISE_VARARGS            1
                # |  57   L1:     LOAD_GLOBAL              4 (GOOD)
                # |               RETURN_VALUE



    def test_confirmed_outline_is_not_replanned(self, sample_state, tmp_path):
        'cp.sqlite'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  68           RESUME                   0
        # |  69           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('outline',))
        # |               IMPORT_NAME              0 (test_pipeline)
        # |               IMPORT_FROM              1 (outline)
        # |               STORE_FAST               3 (outline)
        # |               POP_TOP
        # |  71           LOAD_GLOBAL              5 (pipeline + NULL)
        # |               CALL                     0
        # |               STORE_FAST               4 (p)
        # |  72           LOAD_GLOBAL              7 (run_via_graph + NULL)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (p, sample_state)
        # |               LOAD_GLOBAL              9 (volume + NULL)
        # |               CALL                     0
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               2 ('')
        # |  73           LOAD_FAST_BORROW         3 (outline)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               LOAD_FAST_BORROW         2 (tmp_path)
        # |               LOAD_CONST               3 ('cp.sqlite')
        # |               BINARY_OP               11 (/)
        # |  72           LOAD_CONST               4 (('note', 'outline', 'checkpoint_db'))
        # |               CALL_KW                  7
        # |               STORE_FAST               5 (r)
        # |  74           LOAD_FAST_BORROW         5 (r)
        # |               LOAD_ATTR               10 (passed)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       141 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               5 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |               LOAD_CONST               6 ('py0')
        # |               LOAD_CONST               7 ('r')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               7 ('r')
        # |       L3:     LOAD_CONST               8 ('py2')
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format3)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format3)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               STORE_FAST               6 (@py_assert1)
        # |  75           LOAD_FAST_BORROW         4 (p)
        # |               LOAD_ATTR               26 (architect)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
        # |               LOAD_ATTR               28 (calls)
        # |               STORE_FAST               8 (@py_assert3)
        # |               LOAD_SMALL_INT           0
        # |               STORE_FAST_LOAD_FAST   152 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         9 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       248 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               30 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW        10 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.architect\n}.calls\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               6 ('py0')
        # |               LOAD_CONST              10 ('p')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (p)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (p)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST              10 ('p')
        # |       L7:     LOAD_CONST               8 ('py2')
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py4')
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py7')
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format8)
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               32 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 ('人确认过的细纲不该被重出一份盖掉')
        # |               CALL                     1
        # |               LOAD_CONST              14 ('\n>assert %(py9)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST              15 ('py9')
        # |               LOAD_FAST_BORROW        11 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format10)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        12 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  169 (@py_assert5, @py_assert6)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_drafts_seed_the_scenes(self, sample_state, tmp_path):
        '草稿一'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  77           RESUME                   0
        # |  78           LOAD_GLOBAL              1 (pipeline + NULL)
        # |               CALL                     0
        # |               STORE_FAST               3 (p)
        # |  79           LOAD_GLOBAL              3 (run_via_graph + NULL)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 49 (p, sample_state)
        # |               LOAD_GLOBAL              5 (volume + NULL)
        # |               CALL                     0
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               1 ('')
        # |  80           LOAD_CONST               2 ('草稿一')
        # |               LOAD_CONST               3 ('草稿二')
        # |               BUILD_LIST               2
        # |  81           LOAD_FAST_BORROW         2 (tmp_path)
        # |               LOAD_CONST               4 ('cp.sqlite')
        # |               BINARY_OP               11 (/)
        # |  79           LOAD_CONST               5 (('note', 'drafts', 'checkpoint_db'))
        # |               CALL_KW                  7
        # |               STORE_FAST               4 (r)
        # |  82           LOAD_FAST_BORROW         4 (r)
        # |               LOAD_ATTR                6 (passed)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       141 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               6 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |               LOAD_CONST               7 ('py0')
        # |               LOAD_CONST               8 ('r')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               8 ('r')
        # |       L3:     LOAD_CONST               9 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert1)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format3)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format3)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              10 (None)
        # |               STORE_FAST               5 (@py_assert1)
        # |  83           LOAD_FAST_BORROW         3 (p)
        # |               LOAD_ATTR               22 (writer)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert1, @py_assert1)
        # |               LOAD_ATTR               24 (wrote)
        # |               STORE_FAST               7 (@py_assert3)
        # |               BUILD_LIST               0
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         8 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       248 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               26 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              17 (('==',))
        # |               LOAD_FAST_BORROW         9 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.wrote\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py0')
        # |               LOAD_CONST              11 ('p')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (p)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (p)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST              11 ('p')
        # |       L7:     LOAD_CONST               9 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST              13 ('py7')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format8)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               28 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 ('草稿齐了就不该再调 writer')
        # |               CALL                     1
        # |               LOAD_CONST              15 ('\n>assert %(py9)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST              16 ('py9')
        # |               LOAD_FAST_BORROW        10 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format10)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  152 (@py_assert5, @py_assert6)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE

    def test_chapters_do_not_share_a_thread(self, sample_state, tmp_path):
        '第 4 章不能捡起第 3 章的残局。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  85           RESUME                   0
        # |  87           LOAD_FAST_BORROW         2 (tmp_path)
        # |               LOAD_CONST               1 ('cp.sqlite')
        # |               BINARY_OP               11 (/)
        # |               STORE_FAST               3 (db)
        # |  88           LOAD_GLOBAL              1 (pipeline + NULL)
        # |               CALL                     0
        # |               STORE_FAST               4 (p)
        # |  89           LOAD_GLOBAL              3 (run_via_graph + NULL)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 65 (p, sample_state)
        # |               LOAD_GLOBAL              5 (volume + NULL)
        # |               CALL                     0
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               2 ('')
        # |               LOAD_FAST_BORROW         3 (db)
        # |               LOAD_CONST               3 (('note', 'checkpoint_db'))
        # |               CALL_KW                  6
        # |               POP_TOP
        # |  90           LOAD_GLOBAL              1 (pipeline + NULL)
        # |               CALL                     0
        # |               STORE_FAST               5 (p2)
        # |  91           LOAD_GLOBAL              3 (run_via_graph + NULL)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 81 (p2, sample_state)
        # |               LOAD_GLOBAL              5 (volume + NULL)
        # |               CALL                     0
        # |               LOAD_SMALL_INT           2
        # |               LOAD_CONST               2 ('')
        # |               LOAD_FAST_BORROW         3 (db)
        # |               LOAD_CONST               3 (('note', 'checkpoint_db'))
        # |               CALL_KW                  6
        # |               STORE_FAST               6 (r)
        # |  92           LOAD_FAST_BORROW         6 (r)
        # |               LOAD_ATTR                6 (ch)
        # |               STORE_FAST               7 (@py_assert1)
        # |               LOAD_SMALL_INT           2
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         8 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW         9 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.ch\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST               5 ('r')
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
        # |               LOAD_FAST_BORROW         6 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('r')
        # |       L3:     LOAD_CONST               6 ('py2')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py5')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format6)
        # |               LOAD_CONST               8 ('assert %(py7)s')
        # |               LOAD_CONST               9 ('py7')
        # |               LOAD_FAST_BORROW        10 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format8)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  152 (@py_assert3, @py_assert4)
        # |  93           LOAD_FAST_BORROW         5 (p2)
        # |               LOAD_ATTR               24 (architect)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
        # |               LOAD_ATTR               26 (calls)
        # |               STORE_FAST               9 (@py_assert3)
        # |               LOAD_SMALL_INT           1
        # |               STORE_FAST_LOAD_FAST   201 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW        12 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   221 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       248 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW        13 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.architect\n}.calls\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 156 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST              11 ('p2')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (p2)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (p2)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST              11 ('p2')
        # |       L7:     LOAD_CONST               6 ('py2')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py7')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        12 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format8)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               28 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 ('另一章要自己出细纲')
        # |               CALL                     1
        # |               LOAD_CONST              14 ('\n>assert %(py9)s')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST              15 ('py9')
        # |               LOAD_FAST_BORROW        11 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              14 (@py_format10)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        14 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  220 (@py_assert5, @py_assert6)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE


class TestStaleOutlineGuard:
    'TestStaleOutlineGuard'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  96           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestStaleOutlineGuard')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          96
    # |               STORE_NAME               3 (__firstlineno__)
    # |  97           LOAD_CONST               1 ('细纲被人改过之后再跑，绝不能默默续上照着旧细纲写的那份存档 ——\n第 3 章正是「细纲把心理描写禁掉了」才要改，续旧档等于修改白做。')
    # |               STORE_NAME               4 (__doc__)
    # | 100           LOAD_CONST               2 (<code object _crash_then at 0x78f0d76a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 100>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (_crash_then)
    # | 120           LOAD_CONST               3 (<code object test_changed_outline_starts_over at 0x78f0c9b100, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 120>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_changed_outline_starts_over)
    # | 130           LOAD_CONST               4 (<code object test_unchanged_outline_still_resumes at 0x78f0d9c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 130>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_unchanged_outline_still_resumes)
    # |               LOAD_CONST               5 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object _crash_then at 0x78f0d76a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 100>:
    # |  100           RESUME                   0
    # |  101           LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('outline',))
    # |                IMPORT_NAME              0 (test_pipeline)
    # |                IMPORT_FROM              1 (outline)
    # |                STORE_FAST               4 (outline)
    # |                POP_TOP
    # |  103           LOAD_BUILD_CLASS
    # |                PUSH_NULL
    # |                LOAD_CONST               2 (<code object Flaky at 0x1061e7030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 103>)
    # |                MAKE_FUNCTION
    # |                LOAD_CONST               3 ('Flaky')
    # |                CALL                     2
    # |                STORE_FAST               5 (Flaky)
    # |  111           LOAD_GLOBAL              5 (pipeline + NULL)
    # |                LOAD_FAST_BORROW         5 (Flaky)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CALL                     1
    # |                LOAD_FAST_BORROW         2 (tmp_path)
    # |                LOAD_CONST               4 ('cp.sqlite')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST_STORE_FAST  118 (db, p)
    # |  112           LOAD_GLOBAL              6 (pytest)
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
    # |  113           LOAD_GLOBAL             13 (run_via_graph + NULL)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (p, sample_state)
    # |                LOAD_GLOBAL             15 (volume + NULL)
    # |                CALL                     0
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               5 ('')
    # |  114           LOAD_FAST_BORROW         4 (outline)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                LOAD_FAST_BORROW         7 (db)
    # |  113           LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
    # |                CALL_KW                  7
    # |                POP_TOP
    # |  112   L2:     LOAD_CONST               7 (None)
    # |                LOAD_CONST               7 (None)
    # |                LOAD_CONST               7 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |  115   L3:     LOAD_GLOBAL              5 (pipeline + NULL)
    # |                CALL                     0
    # |                STORE_FAST               8 (p2)
    # |  116           LOAD_GLOBAL             13 (run_via_graph + NULL)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 129 (p2, sample_state)
    # |                LOAD_GLOBAL             15 (volume + NULL)
    # |                CALL                     0
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               5 ('')
    # |  117           LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (second_outline, db)
    # |  116           LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
    # |                CALL_KW                  7
    # |                STORE_FAST               9 (r)
    # |  118           LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (p2, r)
    # |                BUILD_TUPLE              2
    # |                RETURN_VALUE
    # |  112   L4:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L5)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L5:     POP_TOP
    # |        L6:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                JUMP_BACKWARD_NO_INTERRUPT 53 (to L3)
    # |   --   L7:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L4 [2] lasti
    # |   L4 to L6 -> L7 [4] lasti
    # | Disassembly of <code object Flaky at 0x1061e7030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 103>:
    # | 103           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestStaleOutlineGuard._crash_then.<locals>.Flaky')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         103
    # |               STORE_NAME               3 (__firstlineno__)
    # | 104           LOAD_CONST               1 (<code object __init__ at 0x1062066a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 104>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (__init__)
    # | 105           LOAD_CONST               2 (<code object stitch at 0x10622c960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 105>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (stitch)
    # |               LOAD_CONST               3 (('calls',))
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x1062066a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 104>:
    # | 104           RESUME                   0
    # |               LOAD_SMALL_INT           0
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               0 (calls)
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object stitch at 0x10622c960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 105>:
    # | 105           RESUME                   0
    # | 106           LOAD_FAST_BORROW         0 (self)
    # |               COPY                     1
    # |               LOAD_ATTR                0 (calls)
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               13 (+=)
    # |               SWAP                     2
    # |               STORE_ATTR               0 (calls)
    # | 107           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (calls)
    # |               LOAD_SMALL_INT           1
    # |               COMPARE_OP              88 (bool(==))
    # |               POP_JUMP_IF_FALSE       12 (to L1)
    # |               NOT_TAKEN
    # | 108           LOAD_GLOBAL              3 (RuntimeError + NULL)
    # |               LOAD_CONST               1 ('上游 403')
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # | 109   L1:     LOAD_GLOBAL              4 (GOOD)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_changed_outline_starts_over at 0x78f0c9b100, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 120>:
    # | 120            RESUME                   0
    # | 121            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('outline', 'scene'))
    # |                IMPORT_NAME              0 (test_pipeline)
    # |                IMPORT_FROM              1 (outline)
    # |                STORE_FAST               3 (outline)
    # |                IMPORT_FROM              2 (scene)
    # |                STORE_FAST               4 (scene)
    # |                POP_TOP
    # | 123            LOAD_FAST_BORROW         3 (outline)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                STORE_FAST               5 (changed)
    # | 124            LOAD_CONST               2 ('这一场要写足心理活动')
    # |                BUILD_LIST               1
    # |                LOAD_FAST_BORROW         5 (changed)
    # |                LOAD_ATTR                6 (scenes)
    # |                LOAD_SMALL_INT           0
    # |                BINARY_OP               26 ([])
    # |                STORE_ATTR               4 (must_include)
    # | 125            LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR               11 (_crash_then + NULL|self)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (sample_state, tmp_path)
    # |                LOAD_FAST_BORROW         5 (changed)
    # |                CALL                     3
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST  103 (p2, r)
    # | 126            LOAD_FAST_BORROW         7 (r)
    # |                LOAD_ATTR               12 (passed)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       141 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_CONST               3 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |                LOAD_CONST               4 ('py0')
    # |                LOAD_CONST               5 ('r')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('r')
    # |        L3:     LOAD_CONST               6 ('py2')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert1)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format3)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               26 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format3)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               7 (None)
    # |                STORE_FAST               8 (@py_assert1)
    # | 127            LOAD_FAST_BORROW         6 (p2)
    # |                LOAD_ATTR               28 (writer)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
    # |                LOAD_ATTR               30 (calls)
    # |                STORE_FAST              10 (@py_assert3)
    # |                LOAD_SMALL_INT           1
    # |                STORE_FAST_LOAD_FAST   186 (@py_assert6, @py_assert3)
    # |                LOAD_FAST_BORROW        11 (@py_assert6)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   204 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       248 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               32 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW        12 (@py_assert5)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.calls\n} == %(py7)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert3, @py_assert6)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py0')
    # |                LOAD_CONST               8 ('p2')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (p2)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (p2)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               8 ('p2')
    # |        L7:     LOAD_CONST               6 ('py2')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert6)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format8)
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               34 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              11 ('按新细纲重写，而不是捡旧场景续跑')
    # |                CALL                     1
    # |                LOAD_CONST              12 ('\n>assert %(py9)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              13 ('py9')
    # |                LOAD_FAST_BORROW        13 (@py_format8)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format10)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               26 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        14 (@py_format10)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST               7 (None)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  203 (@py_assert5, @py_assert6)
    # | 128            LOAD_FAST_BORROW         6 (p2)
    # |                LOAD_ATTR               28 (writer)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
    # |                LOAD_ATTR               36 (wrote)
    # |                STORE_FAST              10 (@py_assert3)
    # |                LOAD_CONST              14 ('ch001_s1')
    # |                LOAD_CONST              15 ('ch001_s2')
    # |                BUILD_LIST               2
    # |                STORE_FAST_LOAD_FAST   186 (@py_assert6, @py_assert3)
    # |                LOAD_FAST_BORROW        11 (@py_assert6)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   204 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       221 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               32 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW        12 (@py_assert5)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.wrote\n} == %(py7)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert3, @py_assert6)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py0')
    # |                LOAD_CONST               8 ('p2')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (p2)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L10)
    # |                NOT_TAKEN
    # |        L9:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (p2)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L11)
    # |       L10:     LOAD_CONST               8 ('p2')
    # |       L11:     LOAD_CONST               6 ('py2')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert6)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format8)
    # |                LOAD_CONST              16 ('assert %(py9)s')
    # |                LOAD_CONST              13 ('py9')
    # |                LOAD_FAST_BORROW        13 (@py_format8)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format10)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               26 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        14 (@py_format10)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L12:     LOAD_CONST               7 (None)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  203 (@py_assert5, @py_assert6)
    # |                LOAD_CONST               7 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_unchanged_outline_still_resumes at 0x78f0d9c000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 130>:
    # | 130            RESUME                   0
    # | 132            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('outline',))
    # |                IMPORT_NAME              0 (test_pipeline)
    # |                IMPORT_FROM              1 (outline)
    # |                STORE_FAST               3 (outline)
    # |                POP_TOP
    # | 134            LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                5 (_crash_then + NULL|self)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (sample_state, tmp_path)
    # |                LOAD_FAST_BORROW         3 (outline)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CALL                     3
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   69 (p2, r)
    # | 135            LOAD_FAST_BORROW         5 (r)
    # |                LOAD_ATTR                6 (passed)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       141 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_CONST               2 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('r')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('r')
    # |        L3:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format3)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format3)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               6 (None)
    # |                STORE_FAST               6 (@py_assert1)
    # | 136            BUILD_LIST               0
    # |                STORE_FAST_LOAD_FAST   100 (@py_assert1, p2)
    # |                LOAD_ATTR               22 (writer)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
    # |                LOAD_ATTR               24 (calls)
    # |                STORE_FAST               9 (@py_assert5)
    # |                LOAD_SMALL_INT           0
    # |                STORE_FAST_LOAD_FAST   169 (@py_assert8, @py_assert5)
    # |                LOAD_FAST_BORROW        10 (@py_assert8)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert7, @py_assert7)
    # |                STORE_FAST_LOAD_FAST   203 (@py_assert0, @py_assert7)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       32 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         4 (p2)
    # |                LOAD_ATTR               26 (architect)
    # |                STORE_FAST_LOAD_FAST   221 (@py_assert14, @py_assert14)
    # |                LOAD_ATTR               24 (calls)
    # |                STORE_FAST              14 (@py_assert16)
    # |                LOAD_SMALL_INT           0
    # |                STORE_FAST_LOAD_FAST   254 (@py_assert19, @py_assert16)
    # |                LOAD_FAST_BORROW        15 (@py_assert19)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST              16 (@py_assert18)
    # |                LOAD_FAST               16 (@py_assert18)
    # |                STORE_FAST              12 (@py_assert0)
    # |        L5:     LOAD_FAST_BORROW        12 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       494 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               28 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              21 (('==',))
    # |                LOAD_FAST_BORROW        11 (@py_assert7)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              22 (('%(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py2)s.writer\n}.calls\n} == %(py9)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert5, @py_assert8)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py2')
    # |                LOAD_CONST               7 ('p2')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L6)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (p2)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L7)
    # |                NOT_TAKEN
    # |        L6:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (p2)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L8)
    # |        L7:     LOAD_CONST               7 ('p2')
    # |        L8:     LOAD_CONST               8 ('py4')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py6')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py9')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert8)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format10)
    # |                LOAD_CONST              11 ('%(py11)s')
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_FAST_BORROW        17 (@py_format10)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format12)
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                LOAD_ATTR               31 (append + NULL|self)
    # |                LOAD_FAST_BORROW        18 (@py_format12)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW        11 (@py_assert7)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      208 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               28 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              21 (('==',))
    # |                LOAD_FAST_CHECK         16 (@py_assert18)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              23 (('%(py17)s\n{%(py17)s = %(py15)s\n{%(py15)s = %(py13)s.architect\n}.calls\n} == %(py20)s',))
    # |                LOAD_FAST_CHECK         14 (@py_assert16)
    # |                LOAD_FAST_CHECK         15 (@py_assert19)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              13 ('py13')
    # |                LOAD_CONST               7 ('p2')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (p2)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L10)
    # |                NOT_TAKEN
    # |        L9:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (p2)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L11)
    # |       L10:     LOAD_CONST               7 ('p2')
    # |       L11:     LOAD_CONST              14 ('py15')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_CHECK         13 (@py_assert14)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py17')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        14 (@py_assert16)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py20')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        15 (@py_assert19)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              19 (@py_format21)
    # |                LOAD_CONST              17 ('%(py22)s')
    # |                LOAD_CONST              18 ('py22')
    # |                LOAD_FAST_BORROW        19 (@py_format21)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              20 (@py_format23)
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                LOAD_ATTR               31 (append + NULL|self)
    # |                LOAD_FAST_BORROW        20 (@py_format23)
    # |                CALL                     1
    # |                POP_TOP
    # |       L12:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               32 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              21 (@py_format24)
    # |                LOAD_CONST              19 ('assert %(py25)s')
    # |                LOAD_CONST              20 ('py25')
    # |                LOAD_FAST_BORROW        21 (@py_format24)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              22 (@py_format26)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        22 (@py_format26)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L13:     LOAD_CONST               6 (None)
    # |                COPY                     1
    # |                STORE_FAST              12 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST              11 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert14)
    # |                COPY                     1
    # |                STORE_FAST              14 (@py_assert16)
    # |                COPY                     1
    # |                STORE_FAST              16 (@py_assert18)
    # |                STORE_FAST              15 (@py_assert19)
    # |                LOAD_CONST               6 (None)
    # |                RETURN_VALUE

    def _crash_then(self, sample_state, tmp_path, second_outline):
        'Flaky'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  100           RESUME                   0
        # |  101           LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('outline',))
        # |                IMPORT_NAME              0 (test_pipeline)
        # |                IMPORT_FROM              1 (outline)
        # |                STORE_FAST               4 (outline)
        # |                POP_TOP
        # |  103           LOAD_BUILD_CLASS
        # |                PUSH_NULL
        # |                LOAD_CONST               2 (<code object Flaky at 0x1061e7030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 103>)
        # |                MAKE_FUNCTION
        # |                LOAD_CONST               3 ('Flaky')
        # |                CALL                     2
        # |                STORE_FAST               5 (Flaky)
        # |  111           LOAD_GLOBAL              5 (pipeline + NULL)
        # |                LOAD_FAST_BORROW         5 (Flaky)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CALL                     1
        # |                LOAD_FAST_BORROW         2 (tmp_path)
        # |                LOAD_CONST               4 ('cp.sqlite')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST_STORE_FAST  118 (db, p)
        # |  112           LOAD_GLOBAL              6 (pytest)
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
        # |  113           LOAD_GLOBAL             13 (run_via_graph + NULL)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (p, sample_state)
        # |                LOAD_GLOBAL             15 (volume + NULL)
        # |                CALL                     0
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               5 ('')
        # |  114           LOAD_FAST_BORROW         4 (outline)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                LOAD_FAST_BORROW         7 (db)
        # |  113           LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
        # |                CALL_KW                  7
        # |                POP_TOP
        # |  112   L2:     LOAD_CONST               7 (None)
        # |                LOAD_CONST               7 (None)
        # |                LOAD_CONST               7 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |  115   L3:     LOAD_GLOBAL              5 (pipeline + NULL)
        # |                CALL                     0
        # |                STORE_FAST               8 (p2)
        # |  116           LOAD_GLOBAL             13 (run_via_graph + NULL)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 129 (p2, sample_state)
        # |                LOAD_GLOBAL             15 (volume + NULL)
        # |                CALL                     0
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               5 ('')
        # |  117           LOAD_FAST_BORROW_LOAD_FAST_BORROW 55 (second_outline, db)
        # |  116           LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
        # |                CALL_KW                  7
        # |                STORE_FAST               9 (r)
        # |  118           LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (p2, r)
        # |                BUILD_TUPLE              2
        # |                RETURN_VALUE
        # |  112   L4:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L5)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L5:     POP_TOP
        # |        L6:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                JUMP_BACKWARD_NO_INTERRUPT 53 (to L3)
        # |   --   L7:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L4 [2] lasti
        # |   L4 to L6 -> L7 [4] lasti
        # | Disassembly of <code object Flaky at 0x1061e7030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 103>:
        # | 103           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestStaleOutlineGuard._crash_then.<locals>.Flaky')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         103
        # |               STORE_NAME               3 (__firstlineno__)
        # | 104           LOAD_CONST               1 (<code object __init__ at 0x1062066a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 104>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               4 (__init__)
        # | 105           LOAD_CONST               2 (<code object stitch at 0x10622c960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 105>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               5 (stitch)
        # |               LOAD_CONST               3 (('calls',))
        # |               STORE_NAME               6 (__static_attributes__)
        # |               LOAD_CONST               4 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object __init__ at 0x1062066a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 104>:
        # | 104           RESUME                   0
        # |               LOAD_SMALL_INT           0
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               0 (calls)
        # |               LOAD_CONST               1 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object stitch at 0x10622c960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 105>:
        # | 105           RESUME                   0
        # | 106           LOAD_FAST_BORROW         0 (self)
        # |               COPY                     1
        # |               LOAD_ATTR                0 (calls)
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               13 (+=)
        # |               SWAP                     2
        # |               STORE_ATTR               0 (calls)
        # | 107           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (calls)
        # |               LOAD_SMALL_INT           1
        # |               COMPARE_OP              88 (bool(==))
        # |               POP_JUMP_IF_FALSE       12 (to L1)
        # |               NOT_TAKEN
        # | 108           LOAD_GLOBAL              3 (RuntimeError + NULL)
        # |               LOAD_CONST               1 ('上游 403')
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # | 109   L1:     LOAD_GLOBAL              4 (GOOD)
        # |               RETURN_VALUE

        class Flaky:
            'TestStaleOutlineGuard._crash_then.<locals>.Flaky'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 103           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestStaleOutlineGuard._crash_then.<locals>.Flaky')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         103
            # |               STORE_NAME               3 (__firstlineno__)
            # | 104           LOAD_CONST               1 (<code object __init__ at 0x1062066a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 104>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               4 (__init__)
            # | 105           LOAD_CONST               2 (<code object stitch at 0x10622c960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 105>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               5 (stitch)
            # |               LOAD_CONST               3 (('calls',))
            # |               STORE_NAME               6 (__static_attributes__)
            # |               LOAD_CONST               4 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object __init__ at 0x1062066a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 104>:
            # | 104           RESUME                   0
            # |               LOAD_SMALL_INT           0
            # |               LOAD_FAST_BORROW         0 (self)
            # |               STORE_ATTR               0 (calls)
            # |               LOAD_CONST               1 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object stitch at 0x10622c960, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 105>:
            # | 105           RESUME                   0
            # | 106           LOAD_FAST_BORROW         0 (self)
            # |               COPY                     1
            # |               LOAD_ATTR                0 (calls)
            # |               LOAD_SMALL_INT           1
            # |               BINARY_OP               13 (+=)
            # |               SWAP                     2
            # |               STORE_ATTR               0 (calls)
            # | 107           LOAD_FAST_BORROW         0 (self)
            # |               LOAD_ATTR                0 (calls)
            # |               LOAD_SMALL_INT           1
            # |               COMPARE_OP              88 (bool(==))
            # |               POP_JUMP_IF_FALSE       12 (to L1)
            # |               NOT_TAKEN
            # | 108           LOAD_GLOBAL              3 (RuntimeError + NULL)
            # |               LOAD_CONST               1 ('上游 403')
            # |               CALL                     1
            # |               RAISE_VARARGS            1
            # | 109   L1:     LOAD_GLOBAL              4 (GOOD)
            # |               RETURN_VALUE

            def __init__(self):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # | 104           RESUME                   0
                # |               LOAD_SMALL_INT           0
                # |               LOAD_FAST_BORROW         0 (self)
                # |               STORE_ATTR               0 (calls)
                # |               LOAD_CONST               1 (None)
                # |               RETURN_VALUE

            def stitch(self, o, scenes, **kw):
                '上游 403'
                # ── 函数体（字节码重建见 BODY 段）──
                # | 105           RESUME                   0
                # | 106           LOAD_FAST_BORROW         0 (self)
                # |               COPY                     1
                # |               LOAD_ATTR                0 (calls)
                # |               LOAD_SMALL_INT           1
                # |               BINARY_OP               13 (+=)
                # |               SWAP                     2
                # |               STORE_ATTR               0 (calls)
                # | 107           LOAD_FAST_BORROW         0 (self)
                # |               LOAD_ATTR                0 (calls)
                # |               LOAD_SMALL_INT           1
                # |               COMPARE_OP              88 (bool(==))
                # |               POP_JUMP_IF_FALSE       12 (to L1)
                # |               NOT_TAKEN
                # | 108           LOAD_GLOBAL              3 (RuntimeError + NULL)
                # |               LOAD_CONST               1 ('上游 403')
                # |               CALL                     1
                # |               RAISE_VARARGS            1
                # | 109   L1:     LOAD_GLOBAL              4 (GOOD)
                # |               RETURN_VALUE



    def test_changed_outline_starts_over(self, sample_state, tmp_path):
        '这一场要写足心理活动'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 120            RESUME                   0
        # | 121            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('outline', 'scene'))
        # |                IMPORT_NAME              0 (test_pipeline)
        # |                IMPORT_FROM              1 (outline)
        # |                STORE_FAST               3 (outline)
        # |                IMPORT_FROM              2 (scene)
        # |                STORE_FAST               4 (scene)
        # |                POP_TOP
        # | 123            LOAD_FAST_BORROW         3 (outline)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                STORE_FAST               5 (changed)
        # | 124            LOAD_CONST               2 ('这一场要写足心理活动')
        # |                BUILD_LIST               1
        # |                LOAD_FAST_BORROW         5 (changed)
        # |                LOAD_ATTR                6 (scenes)
        # |                LOAD_SMALL_INT           0
        # |                BINARY_OP               26 ([])
        # |                STORE_ATTR               4 (must_include)
        # | 125            LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR               11 (_crash_then + NULL|self)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (sample_state, tmp_path)
        # |                LOAD_FAST_BORROW         5 (changed)
        # |                CALL                     3
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST  103 (p2, r)
        # | 126            LOAD_FAST_BORROW         7 (r)
        # |                LOAD_ATTR               12 (passed)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       141 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_CONST               3 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |                LOAD_CONST               4 ('py0')
        # |                LOAD_CONST               5 ('r')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('r')
        # |        L3:     LOAD_CONST               6 ('py2')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert1)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format3)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               26 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format3)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               7 (None)
        # |                STORE_FAST               8 (@py_assert1)
        # | 127            LOAD_FAST_BORROW         6 (p2)
        # |                LOAD_ATTR               28 (writer)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
        # |                LOAD_ATTR               30 (calls)
        # |                STORE_FAST              10 (@py_assert3)
        # |                LOAD_SMALL_INT           1
        # |                STORE_FAST_LOAD_FAST   186 (@py_assert6, @py_assert3)
        # |                LOAD_FAST_BORROW        11 (@py_assert6)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   204 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       248 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               32 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW        12 (@py_assert5)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.calls\n} == %(py7)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert3, @py_assert6)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py0')
        # |                LOAD_CONST               8 ('p2')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (p2)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (p2)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               8 ('p2')
        # |        L7:     LOAD_CONST               6 ('py2')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert6)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format8)
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               34 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              11 ('按新细纲重写，而不是捡旧场景续跑')
        # |                CALL                     1
        # |                LOAD_CONST              12 ('\n>assert %(py9)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              13 ('py9')
        # |                LOAD_FAST_BORROW        13 (@py_format8)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format10)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               26 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        14 (@py_format10)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST               7 (None)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  203 (@py_assert5, @py_assert6)
        # | 128            LOAD_FAST_BORROW         6 (p2)
        # |                LOAD_ATTR               28 (writer)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert1, @py_assert1)
        # |                LOAD_ATTR               36 (wrote)
        # |                STORE_FAST              10 (@py_assert3)
        # |                LOAD_CONST              14 ('ch001_s1')
        # |                LOAD_CONST              15 ('ch001_s2')
        # |                BUILD_LIST               2
        # |                STORE_FAST_LOAD_FAST   186 (@py_assert6, @py_assert3)
        # |                LOAD_FAST_BORROW        11 (@py_assert6)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   204 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       221 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               32 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW        12 (@py_assert5)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.wrote\n} == %(py7)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert3, @py_assert6)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py0')
        # |                LOAD_CONST               8 ('p2')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (p2)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L10)
        # |                NOT_TAKEN
        # |        L9:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (p2)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L11)
        # |       L10:     LOAD_CONST               8 ('p2')
        # |       L11:     LOAD_CONST               6 ('py2')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert6)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format8)
        # |                LOAD_CONST              16 ('assert %(py9)s')
        # |                LOAD_CONST              13 ('py9')
        # |                LOAD_FAST_BORROW        13 (@py_format8)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format10)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               26 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        14 (@py_format10)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L12:     LOAD_CONST               7 (None)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  203 (@py_assert5, @py_assert6)
        # |                LOAD_CONST               7 (None)
        # |                RETURN_VALUE

    def test_unchanged_outline_still_resumes(self, sample_state, tmp_path):
        '没改就该续 —— 否则 checkpoint 白建了。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 130            RESUME                   0
        # | 132            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('outline',))
        # |                IMPORT_NAME              0 (test_pipeline)
        # |                IMPORT_FROM              1 (outline)
        # |                STORE_FAST               3 (outline)
        # |                POP_TOP
        # | 134            LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                5 (_crash_then + NULL|self)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (sample_state, tmp_path)
        # |                LOAD_FAST_BORROW         3 (outline)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CALL                     3
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   69 (p2, r)
        # | 135            LOAD_FAST_BORROW         5 (r)
        # |                LOAD_ATTR                6 (passed)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       141 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_CONST               2 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('r')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('r')
        # |        L3:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format3)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format3)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               6 (None)
        # |                STORE_FAST               6 (@py_assert1)
        # | 136            BUILD_LIST               0
        # |                STORE_FAST_LOAD_FAST   100 (@py_assert1, p2)
        # |                LOAD_ATTR               22 (writer)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
        # |                LOAD_ATTR               24 (calls)
        # |                STORE_FAST               9 (@py_assert5)
        # |                LOAD_SMALL_INT           0
        # |                STORE_FAST_LOAD_FAST   169 (@py_assert8, @py_assert5)
        # |                LOAD_FAST_BORROW        10 (@py_assert8)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert7, @py_assert7)
        # |                STORE_FAST_LOAD_FAST   203 (@py_assert0, @py_assert7)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       32 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_FAST_BORROW         4 (p2)
        # |                LOAD_ATTR               26 (architect)
        # |                STORE_FAST_LOAD_FAST   221 (@py_assert14, @py_assert14)
        # |                LOAD_ATTR               24 (calls)
        # |                STORE_FAST              14 (@py_assert16)
        # |                LOAD_SMALL_INT           0
        # |                STORE_FAST_LOAD_FAST   254 (@py_assert19, @py_assert16)
        # |                LOAD_FAST_BORROW        15 (@py_assert19)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST              16 (@py_assert18)
        # |                LOAD_FAST               16 (@py_assert18)
        # |                STORE_FAST              12 (@py_assert0)
        # |        L5:     LOAD_FAST_BORROW        12 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       494 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               28 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              21 (('==',))
        # |                LOAD_FAST_BORROW        11 (@py_assert7)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              22 (('%(py6)s\n{%(py6)s = %(py4)s\n{%(py4)s = %(py2)s.writer\n}.calls\n} == %(py9)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert5, @py_assert8)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py2')
        # |                LOAD_CONST               7 ('p2')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L6)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (p2)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L7)
        # |                NOT_TAKEN
        # |        L6:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (p2)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L8)
        # |        L7:     LOAD_CONST               7 ('p2')
        # |        L8:     LOAD_CONST               8 ('py4')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py6')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py9')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert8)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format10)
        # |                LOAD_CONST              11 ('%(py11)s')
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_FAST_BORROW        17 (@py_format10)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format12)
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                LOAD_ATTR               31 (append + NULL|self)
        # |                LOAD_FAST_BORROW        18 (@py_format12)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW        11 (@py_assert7)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      208 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               28 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              21 (('==',))
        # |                LOAD_FAST_CHECK         16 (@py_assert18)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              23 (('%(py17)s\n{%(py17)s = %(py15)s\n{%(py15)s = %(py13)s.architect\n}.calls\n} == %(py20)s',))
        # |                LOAD_FAST_CHECK         14 (@py_assert16)
        # |                LOAD_FAST_CHECK         15 (@py_assert19)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              13 ('py13')
        # |                LOAD_CONST               7 ('p2')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (p2)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L10)
        # |                NOT_TAKEN
        # |        L9:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (p2)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L11)
        # |       L10:     LOAD_CONST               7 ('p2')
        # |       L11:     LOAD_CONST              14 ('py15')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_CHECK         13 (@py_assert14)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py17')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        14 (@py_assert16)
        # |                CALL                     1
        # |                LOAD_CONST              16 ('py20')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        15 (@py_assert19)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              19 (@py_format21)
        # |                LOAD_CONST              17 ('%(py22)s')
        # |                LOAD_CONST              18 ('py22')
        # |                LOAD_FAST_BORROW        19 (@py_format21)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              20 (@py_format23)
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                LOAD_ATTR               31 (append + NULL|self)
        # |                LOAD_FAST_BORROW        20 (@py_format23)
        # |                CALL                     1
        # |                POP_TOP
        # |       L12:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               32 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              21 (@py_format24)
        # |                LOAD_CONST              19 ('assert %(py25)s')
        # |                LOAD_CONST              20 ('py25')
        # |                LOAD_FAST_BORROW        21 (@py_format24)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              22 (@py_format26)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        22 (@py_format26)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L13:     LOAD_CONST               6 (None)
        # |                COPY                     1
        # |                STORE_FAST              12 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST              11 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST              13 (@py_assert14)
        # |                COPY                     1
        # |                STORE_FAST              14 (@py_assert16)
        # |                COPY                     1
        # |                STORE_FAST              16 (@py_assert18)
        # |                STORE_FAST              15 (@py_assert19)
        # |                LOAD_CONST               6 (None)
        # |                RETURN_VALUE


class TestThreadHygiene:
    'TestThreadHygiene'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 139           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestThreadHygiene')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         139
    # |               STORE_NAME               3 (__firstlineno__)
    # | 140           LOAD_CONST               1 ('LangGraph 的线程状态是累积的：往一条**已经跑完**的线程再 invoke，\nseed 只是合并进旧状态，`revisions` 还停在上次的 2 —— 新一轮缝合完、\ngate 一失败就直接判"修订 2 轮后仍未通过"，一轮修订都不做。\n实测连着两次跑各花 $0.05，什么都没修。')
    # |               STORE_NAME               4 (__doc__)
    # | 145           LOAD_CONST               2 (<code object test_a_finished_run_does_not_poison_the_next_one at 0x78f12ad400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 145>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_a_finished_run_does_not_poison_the_next_one)
    # | 163           LOAD_CONST               3 (<code object test_an_unfinished_run_is_still_resumed at 0x78f12c1e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 163>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_an_unfinished_run_is_still_resumed)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_a_finished_run_does_not_poison_the_next_one at 0x78f12ad400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 145>:
    # | 145            RESUME                   0
    # | 146            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('outline',))
    # |                IMPORT_NAME              0 (test_pipeline)
    # |                IMPORT_FROM              1 (outline)
    # |                STORE_FAST               3 (outline)
    # |                POP_TOP
    # | 148            LOAD_FAST_BORROW         2 (tmp_path)
    # |                LOAD_CONST               2 ('cp.sqlite')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               4 (db)
    # | 150            LOAD_GLOBAL              5 (pipeline + NULL)
    # |                LOAD_GLOBAL              7 (FakeStitcher + NULL)
    # |                LOAD_GLOBAL              9 (make_chapter + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               3 (500)
    # |                LOAD_CONST               4 (('ch', 'target_words'))
    # |                CALL_KW                  2
    # |                BUILD_LIST               1
    # |                CALL                     1
    # |                CALL                     1
    # |                STORE_FAST               5 (p1)
    # | 151            LOAD_GLOBAL             11 (run_via_graph + NULL)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 81 (p1, sample_state)
    # |                LOAD_GLOBAL             13 (volume + NULL)
    # |                CALL                     0
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               5 ('')
    # | 152            LOAD_FAST_BORROW         3 (outline)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                LOAD_FAST_BORROW         4 (db)
    # | 151            LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
    # |                CALL_KW                  7
    # |                STORE_FAST               6 (r1)
    # | 153            BUILD_LIST               0
    # |                STORE_FAST_LOAD_FAST   118 (@py_assert1, r1)
    # |                LOAD_ATTR               14 (passed)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert5, @py_assert5)
    # |                STORE_FAST_LOAD_FAST   169 (@py_assert0, @py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       20 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         6 (r1)
    # |                LOAD_ATTR               16 (revisions)
    # |                STORE_FAST              11 (@py_assert8)
    # |                LOAD_SMALL_INT           2
    # |                STORE_FAST_LOAD_FAST   203 (@py_assert11, @py_assert8)
    # |                LOAD_FAST_BORROW        12 (@py_assert11)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   221 (@py_assert10, @py_assert10)
    # |                STORE_FAST              10 (@py_assert0)
    # |        L1:     LOAD_FAST_BORROW        10 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       391 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_CONST               7 ('not %(py4)s\n{%(py4)s = %(py2)s.passed\n}')
    # |                LOAD_CONST               8 ('py2')
    # |                LOAD_CONST               9 ('r1')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (r1)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (r1)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST               9 ('r1')
    # |        L4:     LOAD_CONST              10 ('py4')
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   231 (@py_format6, @py_assert1)
    # |                LOAD_ATTR               29 (append + NULL|self)
    # |                LOAD_FAST_BORROW        14 (@py_format6)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW         9 (@py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      186 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               30 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              27 (('==',))
    # |                LOAD_FAST_CHECK         13 (@py_assert10)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              28 (('%(py9)s\n{%(py9)s = %(py7)s.revisions\n} == %(py12)s',))
    # |                LOAD_FAST_CHECK         11 (@py_assert8)
    # |                LOAD_FAST_CHECK         12 (@py_assert11)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              11 ('py7')
    # |                LOAD_CONST               9 ('r1')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (r1)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (r1)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               9 ('r1')
    # |        L7:     LOAD_CONST              12 ('py9')
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py12')
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format13)
    # |                LOAD_CONST              14 ('%(py14)s')
    # |                LOAD_CONST              15 ('py14')
    # |                LOAD_FAST_BORROW        15 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format15)
    # |                LOAD_FAST_BORROW         7 (@py_assert1)
    # |                LOAD_ATTR               29 (append + NULL|self)
    # |                LOAD_FAST_BORROW        16 (@py_format15)
    # |                CALL                     1
    # |                POP_TOP
    # |        L8:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               32 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format16)
    # |                LOAD_CONST              16 ('assert %(py17)s')
    # |                LOAD_CONST              17 ('py17')
    # |                LOAD_FAST_BORROW        17 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format18)
    # |                LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               36 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        18 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L9:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST              11 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  220 (@py_assert10, @py_assert11)
    # | 156            LOAD_GLOBAL              5 (pipeline + NULL)
    # |                LOAD_GLOBAL              7 (FakeStitcher + NULL)
    # |                LOAD_GLOBAL              9 (make_chapter + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               3 (500)
    # |                LOAD_CONST               4 (('ch', 'target_words'))
    # |                CALL_KW                  2
    # | 157            LOAD_GLOBAL              9 (make_chapter + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST              19 (('ch',))
    # |                CALL_KW                  1
    # | 156            BUILD_LIST               2
    # |                CALL                     1
    # |                CALL                     1
    # |                STORE_FAST              19 (p2)
    # | 158            LOAD_GLOBAL             11 (run_via_graph + NULL)
    # |                LOAD_FAST_BORROW        19 (p2)
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                LOAD_GLOBAL             13 (volume + NULL)
    # |                CALL                     0
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               5 ('')
    # | 159            LOAD_FAST_BORROW         3 (outline)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                LOAD_FAST_BORROW         4 (db)
    # | 158            LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
    # |                CALL_KW                  7
    # |                STORE_FAST              20 (r2)
    # | 160            LOAD_FAST_BORROW        20 (r2)
    # |                LOAD_ATTR               14 (passed)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       168 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               38 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              20 ('新一轮不该继承上一轮用完的修订次数')
    # |                CALL                     1
    # |                LOAD_CONST              21 ('\n>assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              22 ('py0')
    # |                LOAD_CONST              23 ('r2')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        20 (r2)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        20 (r2)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST              23 ('r2')
    # |       L12:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert1)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              21 (@py_format3)
    # |                LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               36 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        21 (@py_format3)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L13:     LOAD_CONST              18 (None)
    # |                STORE_FAST               7 (@py_assert1)
    # | 161            LOAD_FAST_BORROW        19 (p2)
    # |                LOAD_ATTR               40 (writer)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
    # |                LOAD_ATTR               42 (revised)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       190 (to L17)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               38 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              24 ('该真的修订过')
    # |                CALL                     1
    # |                LOAD_CONST              25 ('\n>assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.revised\n}')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              22 ('py0')
    # |                LOAD_CONST              26 ('p2')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               24 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        19 (p2)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L15)
    # |                NOT_TAKEN
    # |       L14:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        19 (p2)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L16)
    # |       L15:     LOAD_CONST              26 ('p2')
    # |       L16:     LOAD_CONST               8 ('py2')
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py4')
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               26 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              22 (@py_format5)
    # |                LOAD_GLOBAL             35 (AssertionError + NULL)
    # |                LOAD_GLOBAL             22 (@pytest_ar)
    # |                LOAD_ATTR               36 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        22 (@py_format5)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L17:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  120 (@py_assert1, @py_assert3)
    # |                LOAD_CONST              18 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_an_unfinished_run_is_still_resumed at 0x78f12c1e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 163>:
    # |  163            RESUME                   0
    # |  165            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               1 (('outline',))
    # |                 IMPORT_NAME              0 (test_pipeline)
    # |                 IMPORT_FROM              1 (outline)
    # |                 STORE_FAST               3 (outline)
    # |                 POP_TOP
    # |  167            LOAD_BUILD_CLASS
    # |                 PUSH_NULL
    # |                 LOAD_CONST               2 (<code object Flaky at 0x1061e6730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 167>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_CONST               3 ('Flaky')
    # |                 CALL                     2
    # |                 STORE_FAST               4 (Flaky)
    # |  175            LOAD_FAST_BORROW         2 (tmp_path)
    # |                 LOAD_CONST               4 ('cp.sqlite')
    # |                 BINARY_OP               11 (/)
    # |                 STORE_FAST               5 (db)
    # |  176            LOAD_GLOBAL              5 (pipeline + NULL)
    # |                 LOAD_FAST_BORROW         4 (Flaky)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 STORE_FAST               6 (p1)
    # |  177            LOAD_GLOBAL              6 (pytest)
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
    # |  178            LOAD_GLOBAL             13 (run_via_graph + NULL)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (p1, sample_state)
    # |                 LOAD_GLOBAL             15 (volume + NULL)
    # |                 CALL                     0
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_CONST               5 ('')
    # |  179            LOAD_FAST_BORROW         3 (outline)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 LOAD_FAST_BORROW         5 (db)
    # |  178            LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
    # |                 CALL_KW                  7
    # |                 POP_TOP
    # |  177    L2:     LOAD_CONST               7 (None)
    # |                 LOAD_CONST               7 (None)
    # |                 LOAD_CONST               7 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  180    L3:     LOAD_GLOBAL              5 (pipeline + NULL)
    # |                 CALL                     0
    # |                 STORE_FAST               7 (p2)
    # |  181            LOAD_GLOBAL             13 (run_via_graph + NULL)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 113 (p2, sample_state)
    # |                 LOAD_GLOBAL             15 (volume + NULL)
    # |                 CALL                     0
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_CONST               5 ('')
    # |  182            LOAD_FAST_BORROW         3 (outline)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 LOAD_FAST_BORROW         5 (db)
    # |  181            LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
    # |                 CALL_KW                  7
    # |                 STORE_FAST               8 (r)
    # |  183            LOAD_FAST_BORROW         8 (r)
    # |                 LOAD_ATTR               16 (passed)
    # |                 STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       141 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_CONST               8 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |                 LOAD_CONST               9 ('py0')
    # |                 LOAD_CONST              10 ('r')
    # |                 LOAD_GLOBAL             18 (@py_builtins)
    # |                 LOAD_ATTR               20 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (r)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (r)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST              10 ('r')
    # |         L6:     LOAD_CONST              11 ('py2')
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert1)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              10 (@py_format3)
    # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_format3)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST               7 (None)
    # |                 STORE_FAST               9 (@py_assert1)
    # |  184            LOAD_FAST_BORROW         7 (p2)
    # |                 LOAD_ATTR               32 (writer)
    # |                 STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
    # |                 LOAD_ATTR               34 (calls)
    # |                 STORE_FAST              11 (@py_assert3)
    # |                 LOAD_SMALL_INT           0
    # |                 STORE_FAST_LOAD_FAST   203 (@py_assert6, @py_assert3)
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   221 (@py_assert5, @py_assert5)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       248 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               36 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              18 (('==',))
    # |                 LOAD_FAST_BORROW        13 (@py_assert5)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              19 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.calls\n} == %(py7)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert3, @py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               9 ('py0')
    # |                 LOAD_CONST              12 ('p2')
    # |                 LOAD_GLOBAL             18 (@py_builtins)
    # |                 LOAD_ATTR               20 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (p2)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (p2)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST              12 ('p2')
    # |        L10:     LOAD_CONST              11 ('py2')
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              13 ('py4')
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST              14 ('py7')
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              14 (@py_format8)
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               38 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              15 ('续跑不该重写场景')
    # |                 CALL                     1
    # |                 LOAD_CONST              16 ('\n>assert %(py9)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              17 ('py9')
    # |                 LOAD_FAST_BORROW        14 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              15 (@py_format10)
    # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             22 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        15 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST               7 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               9 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST              11 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  220 (@py_assert5, @py_assert6)
    # |                 LOAD_CONST               7 (None)
    # |                 RETURN_VALUE
    # |  177   L12:     PUSH_EXC_INFO
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
    # |                 JUMP_BACKWARD_NO_INTERRUPT 510 (to L3)
    # |   --   L15:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L12 [2] lasti
    # |   L12 to L14 -> L15 [4] lasti
    # | Disassembly of <code object Flaky at 0x1061e6730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 167>:
    # | 167           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestThreadHygiene.test_an_unfinished_run_is_still_resumed.<locals>.Flaky')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         167
    # |               STORE_NAME               3 (__firstlineno__)
    # | 168           LOAD_CONST               1 (<code object __init__ at 0x106206880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 168>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (__init__)
    # | 169           LOAD_CONST               2 (<code object stitch at 0x10622ef70, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 169>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (stitch)
    # |               LOAD_CONST               3 (('calls',))
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x106206880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 168>:
    # | 168           RESUME                   0
    # |               LOAD_SMALL_INT           0
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               0 (calls)
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object stitch at 0x10622ef70, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 169>:
    # | 169           RESUME                   0
    # | 170           LOAD_FAST_BORROW         0 (self)
    # |               COPY                     1
    # |               LOAD_ATTR                0 (calls)
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               13 (+=)
    # |               SWAP                     2
    # |               STORE_ATTR               0 (calls)
    # | 171           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (calls)
    # |               LOAD_SMALL_INT           1
    # |               COMPARE_OP              88 (bool(==))
    # |               POP_JUMP_IF_FALSE       12 (to L1)
    # |               NOT_TAKEN
    # | 172           LOAD_GLOBAL              3 (RuntimeError + NULL)
    # |               LOAD_CONST               1 ('上游 403')
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # | 173   L1:     LOAD_GLOBAL              4 (GOOD)
    # |               RETURN_VALUE

    def test_a_finished_run_does_not_poison_the_next_one(self, sample_state, tmp_path):
        'cp.sqlite'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 145            RESUME                   0
        # | 146            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('outline',))
        # |                IMPORT_NAME              0 (test_pipeline)
        # |                IMPORT_FROM              1 (outline)
        # |                STORE_FAST               3 (outline)
        # |                POP_TOP
        # | 148            LOAD_FAST_BORROW         2 (tmp_path)
        # |                LOAD_CONST               2 ('cp.sqlite')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               4 (db)
        # | 150            LOAD_GLOBAL              5 (pipeline + NULL)
        # |                LOAD_GLOBAL              7 (FakeStitcher + NULL)
        # |                LOAD_GLOBAL              9 (make_chapter + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               3 (500)
        # |                LOAD_CONST               4 (('ch', 'target_words'))
        # |                CALL_KW                  2
        # |                BUILD_LIST               1
        # |                CALL                     1
        # |                CALL                     1
        # |                STORE_FAST               5 (p1)
        # | 151            LOAD_GLOBAL             11 (run_via_graph + NULL)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 81 (p1, sample_state)
        # |                LOAD_GLOBAL             13 (volume + NULL)
        # |                CALL                     0
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               5 ('')
        # | 152            LOAD_FAST_BORROW         3 (outline)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                LOAD_FAST_BORROW         4 (db)
        # | 151            LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
        # |                CALL_KW                  7
        # |                STORE_FAST               6 (r1)
        # | 153            BUILD_LIST               0
        # |                STORE_FAST_LOAD_FAST   118 (@py_assert1, r1)
        # |                LOAD_ATTR               14 (passed)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                UNARY_NOT
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert5, @py_assert5)
        # |                STORE_FAST_LOAD_FAST   169 (@py_assert0, @py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       20 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_FAST_BORROW         6 (r1)
        # |                LOAD_ATTR               16 (revisions)
        # |                STORE_FAST              11 (@py_assert8)
        # |                LOAD_SMALL_INT           2
        # |                STORE_FAST_LOAD_FAST   203 (@py_assert11, @py_assert8)
        # |                LOAD_FAST_BORROW        12 (@py_assert11)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   221 (@py_assert10, @py_assert10)
        # |                STORE_FAST              10 (@py_assert0)
        # |        L1:     LOAD_FAST_BORROW        10 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       391 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_CONST               7 ('not %(py4)s\n{%(py4)s = %(py2)s.passed\n}')
        # |                LOAD_CONST               8 ('py2')
        # |                LOAD_CONST               9 ('r1')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (r1)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (r1)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST               9 ('r1')
        # |        L4:     LOAD_CONST              10 ('py4')
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   231 (@py_format6, @py_assert1)
        # |                LOAD_ATTR               29 (append + NULL|self)
        # |                LOAD_FAST_BORROW        14 (@py_format6)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW         9 (@py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      186 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               30 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              27 (('==',))
        # |                LOAD_FAST_CHECK         13 (@py_assert10)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              28 (('%(py9)s\n{%(py9)s = %(py7)s.revisions\n} == %(py12)s',))
        # |                LOAD_FAST_CHECK         11 (@py_assert8)
        # |                LOAD_FAST_CHECK         12 (@py_assert11)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              11 ('py7')
        # |                LOAD_CONST               9 ('r1')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (r1)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (r1)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               9 ('r1')
        # |        L7:     LOAD_CONST              12 ('py9')
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py12')
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format13)
        # |                LOAD_CONST              14 ('%(py14)s')
        # |                LOAD_CONST              15 ('py14')
        # |                LOAD_FAST_BORROW        15 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format15)
        # |                LOAD_FAST_BORROW         7 (@py_assert1)
        # |                LOAD_ATTR               29 (append + NULL|self)
        # |                LOAD_FAST_BORROW        16 (@py_format15)
        # |                CALL                     1
        # |                POP_TOP
        # |        L8:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               32 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format16)
        # |                LOAD_CONST              16 ('assert %(py17)s')
        # |                LOAD_CONST              17 ('py17')
        # |                LOAD_FAST_BORROW        17 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format18)
        # |                LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               36 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        18 (@py_format18)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L9:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST              11 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  220 (@py_assert10, @py_assert11)
        # | 156            LOAD_GLOBAL              5 (pipeline + NULL)
        # |                LOAD_GLOBAL              7 (FakeStitcher + NULL)
        # |                LOAD_GLOBAL              9 (make_chapter + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               3 (500)
        # |                LOAD_CONST               4 (('ch', 'target_words'))
        # |                CALL_KW                  2
        # | 157            LOAD_GLOBAL              9 (make_chapter + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST              19 (('ch',))
        # |                CALL_KW                  1
        # | 156            BUILD_LIST               2
        # |                CALL                     1
        # |                CALL                     1
        # |                STORE_FAST              19 (p2)
        # | 158            LOAD_GLOBAL             11 (run_via_graph + NULL)
        # |                LOAD_FAST_BORROW        19 (p2)
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                LOAD_GLOBAL             13 (volume + NULL)
        # |                CALL                     0
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               5 ('')
        # | 159            LOAD_FAST_BORROW         3 (outline)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                LOAD_FAST_BORROW         4 (db)
        # | 158            LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
        # |                CALL_KW                  7
        # |                STORE_FAST              20 (r2)
        # | 160            LOAD_FAST_BORROW        20 (r2)
        # |                LOAD_ATTR               14 (passed)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       168 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               38 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              20 ('新一轮不该继承上一轮用完的修订次数')
        # |                CALL                     1
        # |                LOAD_CONST              21 ('\n>assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              22 ('py0')
        # |                LOAD_CONST              23 ('r2')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        20 (r2)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        20 (r2)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST              23 ('r2')
        # |       L12:     LOAD_CONST               8 ('py2')
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert1)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              21 (@py_format3)
        # |                LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               36 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        21 (@py_format3)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L13:     LOAD_CONST              18 (None)
        # |                STORE_FAST               7 (@py_assert1)
        # | 161            LOAD_FAST_BORROW        19 (p2)
        # |                LOAD_ATTR               40 (writer)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert1, @py_assert1)
        # |                LOAD_ATTR               42 (revised)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       190 (to L17)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               38 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              24 ('该真的修订过')
        # |                CALL                     1
        # |                LOAD_CONST              25 ('\n>assert %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.revised\n}')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              22 ('py0')
        # |                LOAD_CONST              26 ('p2')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               24 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        19 (p2)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L15)
        # |                NOT_TAKEN
        # |       L14:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        19 (p2)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L16)
        # |       L15:     LOAD_CONST              26 ('p2')
        # |       L16:     LOAD_CONST               8 ('py2')
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py4')
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               26 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              22 (@py_format5)
        # |                LOAD_GLOBAL             35 (AssertionError + NULL)
        # |                LOAD_GLOBAL             22 (@pytest_ar)
        # |                LOAD_ATTR               36 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        22 (@py_format5)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L17:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  120 (@py_assert1, @py_assert3)
        # |                LOAD_CONST              18 (None)
        # |                RETURN_VALUE

    def test_an_unfinished_run_is_still_resumed(self, sample_state, tmp_path):
        '别把澡盆里的孩子一起倒掉：没跑完的存档仍然要续。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  163            RESUME                   0
        # |  165            LOAD_SMALL_INT           0
        # |                 LOAD_CONST               1 (('outline',))
        # |                 IMPORT_NAME              0 (test_pipeline)
        # |                 IMPORT_FROM              1 (outline)
        # |                 STORE_FAST               3 (outline)
        # |                 POP_TOP
        # |  167            LOAD_BUILD_CLASS
        # |                 PUSH_NULL
        # |                 LOAD_CONST               2 (<code object Flaky at 0x1061e6730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 167>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_CONST               3 ('Flaky')
        # |                 CALL                     2
        # |                 STORE_FAST               4 (Flaky)
        # |  175            LOAD_FAST_BORROW         2 (tmp_path)
        # |                 LOAD_CONST               4 ('cp.sqlite')
        # |                 BINARY_OP               11 (/)
        # |                 STORE_FAST               5 (db)
        # |  176            LOAD_GLOBAL              5 (pipeline + NULL)
        # |                 LOAD_FAST_BORROW         4 (Flaky)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CALL                     1
        # |                 STORE_FAST               6 (p1)
        # |  177            LOAD_GLOBAL              6 (pytest)
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
        # |  178            LOAD_GLOBAL             13 (run_via_graph + NULL)
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 97 (p1, sample_state)
        # |                 LOAD_GLOBAL             15 (volume + NULL)
        # |                 CALL                     0
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_CONST               5 ('')
        # |  179            LOAD_FAST_BORROW         3 (outline)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 LOAD_FAST_BORROW         5 (db)
        # |  178            LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
        # |                 CALL_KW                  7
        # |                 POP_TOP
        # |  177    L2:     LOAD_CONST               7 (None)
        # |                 LOAD_CONST               7 (None)
        # |                 LOAD_CONST               7 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |  180    L3:     LOAD_GLOBAL              5 (pipeline + NULL)
        # |                 CALL                     0
        # |                 STORE_FAST               7 (p2)
        # |  181            LOAD_GLOBAL             13 (run_via_graph + NULL)
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 113 (p2, sample_state)
        # |                 LOAD_GLOBAL             15 (volume + NULL)
        # |                 CALL                     0
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_CONST               5 ('')
        # |  182            LOAD_FAST_BORROW         3 (outline)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 LOAD_FAST_BORROW         5 (db)
        # |  181            LOAD_CONST               6 (('note', 'outline', 'checkpoint_db'))
        # |                 CALL_KW                  7
        # |                 STORE_FAST               8 (r)
        # |  183            LOAD_FAST_BORROW         8 (r)
        # |                 LOAD_ATTR               16 (passed)
        # |                 STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       141 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_CONST               8 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |                 LOAD_CONST               9 ('py0')
        # |                 LOAD_CONST              10 ('r')
        # |                 LOAD_GLOBAL             18 (@py_builtins)
        # |                 LOAD_ATTR               20 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (r)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (r)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST              10 ('r')
        # |         L6:     LOAD_CONST              11 ('py2')
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert1)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              10 (@py_format3)
        # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_format3)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST               7 (None)
        # |                 STORE_FAST               9 (@py_assert1)
        # |  184            LOAD_FAST_BORROW         7 (p2)
        # |                 LOAD_ATTR               32 (writer)
        # |                 STORE_FAST_LOAD_FAST   153 (@py_assert1, @py_assert1)
        # |                 LOAD_ATTR               34 (calls)
        # |                 STORE_FAST              11 (@py_assert3)
        # |                 LOAD_SMALL_INT           0
        # |                 STORE_FAST_LOAD_FAST   203 (@py_assert6, @py_assert3)
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   221 (@py_assert5, @py_assert5)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       248 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               36 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              18 (('==',))
        # |                 LOAD_FAST_BORROW        13 (@py_assert5)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              19 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.writer\n}.calls\n} == %(py7)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 188 (@py_assert3, @py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               9 ('py0')
        # |                 LOAD_CONST              12 ('p2')
        # |                 LOAD_GLOBAL             18 (@py_builtins)
        # |                 LOAD_ATTR               20 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (p2)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (p2)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST              12 ('p2')
        # |        L10:     LOAD_CONST              11 ('py2')
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              13 ('py4')
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST              14 ('py7')
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              14 (@py_format8)
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               38 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              15 ('续跑不该重写场景')
        # |                 CALL                     1
        # |                 LOAD_CONST              16 ('\n>assert %(py9)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              17 ('py9')
        # |                 LOAD_FAST_BORROW        14 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              15 (@py_format10)
        # |                 LOAD_GLOBAL             29 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             22 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        15 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST               7 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               9 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST              11 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  220 (@py_assert5, @py_assert6)
        # |                 LOAD_CONST               7 (None)
        # |                 RETURN_VALUE
        # |  177   L12:     PUSH_EXC_INFO
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
        # |                 JUMP_BACKWARD_NO_INTERRUPT 510 (to L3)
        # |   --   L15:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L12 [2] lasti
        # |   L12 to L14 -> L15 [4] lasti
        # | Disassembly of <code object Flaky at 0x1061e6730, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 167>:
        # | 167           RESUME                   0
        # |               LOAD_NAME                0 (__name__)
        # |               STORE_NAME               1 (__module__)
        # |               LOAD_CONST               0 ('TestThreadHygiene.test_an_unfinished_run_is_still_resumed.<locals>.Flaky')
        # |               STORE_NAME               2 (__qualname__)
        # |               LOAD_SMALL_INT         167
        # |               STORE_NAME               3 (__firstlineno__)
        # | 168           LOAD_CONST               1 (<code object __init__ at 0x106206880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 168>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               4 (__init__)
        # | 169           LOAD_CONST               2 (<code object stitch at 0x10622ef70, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 169>)
        # |               MAKE_FUNCTION
        # |               STORE_NAME               5 (stitch)
        # |               LOAD_CONST               3 (('calls',))
        # |               STORE_NAME               6 (__static_attributes__)
        # |               LOAD_CONST               4 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object __init__ at 0x106206880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 168>:
        # | 168           RESUME                   0
        # |               LOAD_SMALL_INT           0
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               0 (calls)
        # |               LOAD_CONST               1 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object stitch at 0x10622ef70, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 169>:
        # | 169           RESUME                   0
        # | 170           LOAD_FAST_BORROW         0 (self)
        # |               COPY                     1
        # |               LOAD_ATTR                0 (calls)
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               13 (+=)
        # |               SWAP                     2
        # |               STORE_ATTR               0 (calls)
        # | 171           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (calls)
        # |               LOAD_SMALL_INT           1
        # |               COMPARE_OP              88 (bool(==))
        # |               POP_JUMP_IF_FALSE       12 (to L1)
        # |               NOT_TAKEN
        # | 172           LOAD_GLOBAL              3 (RuntimeError + NULL)
        # |               LOAD_CONST               1 ('上游 403')
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # | 173   L1:     LOAD_GLOBAL              4 (GOOD)
        # |               RETURN_VALUE

        class Flaky:
            'TestThreadHygiene.test_an_unfinished_run_is_still_resumed.<locals>.Flaky'
            # ── 函数体（字节码重建见 BODY 段）──
            # | 167           RESUME                   0
            # |               LOAD_NAME                0 (__name__)
            # |               STORE_NAME               1 (__module__)
            # |               LOAD_CONST               0 ('TestThreadHygiene.test_an_unfinished_run_is_still_resumed.<locals>.Flaky')
            # |               STORE_NAME               2 (__qualname__)
            # |               LOAD_SMALL_INT         167
            # |               STORE_NAME               3 (__firstlineno__)
            # | 168           LOAD_CONST               1 (<code object __init__ at 0x106206880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 168>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               4 (__init__)
            # | 169           LOAD_CONST               2 (<code object stitch at 0x10622ef70, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 169>)
            # |               MAKE_FUNCTION
            # |               STORE_NAME               5 (stitch)
            # |               LOAD_CONST               3 (('calls',))
            # |               STORE_NAME               6 (__static_attributes__)
            # |               LOAD_CONST               4 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object __init__ at 0x106206880, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 168>:
            # | 168           RESUME                   0
            # |               LOAD_SMALL_INT           0
            # |               LOAD_FAST_BORROW         0 (self)
            # |               STORE_ATTR               0 (calls)
            # |               LOAD_CONST               1 (None)
            # |               RETURN_VALUE
            # | Disassembly of <code object stitch at 0x10622ef70, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_cli_graph.py", line 169>:
            # | 169           RESUME                   0
            # | 170           LOAD_FAST_BORROW         0 (self)
            # |               COPY                     1
            # |               LOAD_ATTR                0 (calls)
            # |               LOAD_SMALL_INT           1
            # |               BINARY_OP               13 (+=)
            # |               SWAP                     2
            # |               STORE_ATTR               0 (calls)
            # | 171           LOAD_FAST_BORROW         0 (self)
            # |               LOAD_ATTR                0 (calls)
            # |               LOAD_SMALL_INT           1
            # |               COMPARE_OP              88 (bool(==))
            # |               POP_JUMP_IF_FALSE       12 (to L1)
            # |               NOT_TAKEN
            # | 172           LOAD_GLOBAL              3 (RuntimeError + NULL)
            # |               LOAD_CONST               1 ('上游 403')
            # |               CALL                     1
            # |               RAISE_VARARGS            1
            # | 173   L1:     LOAD_GLOBAL              4 (GOOD)
            # |               RETURN_VALUE

            def __init__(self):
                pass  # 无 docstring
                # ── 函数体（字节码重建见 BODY 段）──
                # | 168           RESUME                   0
                # |               LOAD_SMALL_INT           0
                # |               LOAD_FAST_BORROW         0 (self)
                # |               STORE_ATTR               0 (calls)
                # |               LOAD_CONST               1 (None)
                # |               RETURN_VALUE

            def stitch(self, o, scenes, **kw):
                '上游 403'
                # ── 函数体（字节码重建见 BODY 段）──
                # | 169           RESUME                   0
                # | 170           LOAD_FAST_BORROW         0 (self)
                # |               COPY                     1
                # |               LOAD_ATTR                0 (calls)
                # |               LOAD_SMALL_INT           1
                # |               BINARY_OP               13 (+=)
                # |               SWAP                     2
                # |               STORE_ATTR               0 (calls)
                # | 171           LOAD_FAST_BORROW         0 (self)
                # |               LOAD_ATTR                0 (calls)
                # |               LOAD_SMALL_INT           1
                # |               COMPARE_OP              88 (bool(==))
                # |               POP_JUMP_IF_FALSE       12 (to L1)
                # |               NOT_TAKEN
                # | 172           LOAD_GLOBAL              3 (RuntimeError + NULL)
                # |               LOAD_CONST               1 ('上游 403')
                # |               CALL                     1
                # |               RAISE_VARARGS            1
                # | 173   L1:     LOAD_GLOBAL              4 (GOOD)
                # |               RETURN_VALUE



