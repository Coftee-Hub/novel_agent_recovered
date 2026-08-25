# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py
# 来源   : test_stitch_fallback.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '缝合失败时的机械兜底。\n\n第 3 章连着四次尝试，三次死在缝合，每次都是三场写好的正文（$0.07、十几分钟）\n换来零产出 —— 连"内容到底行不行"都无从判断。兜底让人至少能看到正文。\n\n但兜底稿**不是成稿**：接缝没打磨、重复没删、章末钩子没处理。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '缝合失败时的机械兜底。\n\n第 3 章连着四次尝试，三次死在缝合，每次都是三场写好的正文（$0.07、十几分钟）\n换来零产出 —— 连"内容到底行不行"都无从判断。兜底让人至少能看到正文。\n\n但兜底稿**不是成稿**：接缝没打磨、重复没删、章末钩子没处理。\n',
    8: 'config',
    9: 'project.yaml',
    10: 'skills',
    12: 'Client',
    15: 'TestMechanicalFallback',
    17: 'TestPipelineTreatsItAsNotPassed',
    18: '第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。第一场的正文。',
    19: '第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。第二场的正文。',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Client', 0): 'Client',
    ('Client', 1): '按脚本行事的假 LLM：可以抛异常，也可以吐残缺内容。',
    ('complete', 2): 'R',
    ('R', 0): 'Client.complete.<locals>.R',
    ('<lambda>', 0): '角色',
    ('TestMechanicalFallback', 0): 'TestMechanicalFallback',
    ('test_api_failure_still_yields_the_prose', 0): '上游 403 是实测最常见的失败方式。正文不能跟着一起没。',
    ('test_api_failure_still_yields_the_prose', 1): '上游 403',
    ('test_api_failure_still_yields_the_prose', 3): '第一场的正文',
    ('test_api_failure_still_yields_the_prose', 4): 'py1',
    ('test_api_failure_still_yields_the_prose', 5): 'py3',
    ('test_api_failure_still_yields_the_prose', 6): 'e',
    ('test_api_failure_still_yields_the_prose', 7): 'py5',
    ('test_api_failure_still_yields_the_prose', 8): 'py7',
    ('test_api_failure_still_yields_the_prose', 9): 'assert %(py9)s',
    ('test_api_failure_still_yields_the_prose', 10): 'py9',
    ('test_api_failure_still_yields_the_prose', 11): '第二场的正文',
    ('test_truncated_output_also_falls_back', 0): '实测过一次只吐 87 字就 end_turn 收工。',
    ('test_truncated_output_also_falls_back', 1): '太短了。',
    ('test_truncated_output_also_falls_back', 3): '第一场的正文',
    ('test_truncated_output_also_falls_back', 4): 'py1',
    ('test_truncated_output_also_falls_back', 5): 'py3',
    ('test_truncated_output_also_falls_back', 6): 'e',
    ('test_truncated_output_also_falls_back', 7): 'py5',
    ('test_truncated_output_also_falls_back', 8): 'py7',
    ('test_truncated_output_also_falls_back', 9): 'assert %(py9)s',
    ('test_truncated_output_also_falls_back', 10): 'py9',
    ('test_fallback_carries_a_title_the_gate_accepts', 0): '没有标题的话，gate 会先报标题错，掩盖掉真正的原因。',
    ('test_fallback_carries_a_title_the_gate_accepts', 1): '## 第1章 值班',
    ('test_fallback_carries_a_title_the_gate_accepts', 2): 'assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.startswith\n}(%(py4)s)\n}',
    ('test_fallback_carries_a_title_the_gate_accepts', 3): 'py0',
    ('test_fallback_carries_a_title_the_gate_accepts', 4): 'text',
    ('test_fallback_carries_a_title_the_gate_accepts', 5): 'py2',
    ('test_fallback_carries_a_title_the_gate_accepts', 6): 'py4',
    ('test_fallback_carries_a_title_the_gate_accepts', 7): 'py6',
    ('test_fallback_carries_a_title_the_gate_accepts', 11): 'assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_fallback_carries_a_title_the_gate_accepts', 12): 'any',
    ('<genexpr>', 0): 'title',
    ('test_retries_once_before_giving_up', 0): '第一次失败可能只是抖动；但不能无限试 —— 这是最贵的一次调用。',
    ('test_retries_once_before_giving_up', 1): '403',
    ('test_retries_once_before_giving_up', 3): '## 第1章',
    ('test_retries_once_before_giving_up', 4): 'assert %(py14)s\n{%(py14)s = %(py10)s\n{%(py10)s = %(py8)s\n{%(py8)s = %(py2)s\n{%(py2)s = %(py0)s.stitch\n}(%(py5)s\n{%(py5)s = %(py3)s()\n}, %(py6)s)\n}.startswith\n}(%(py12)s)\n}',
    ('test_retries_once_before_giving_up', 5): 'py0',
    ('test_retries_once_before_giving_up', 6): 'c',
    ('test_retries_once_before_giving_up', 7): 'py2',
    ('test_retries_once_before_giving_up', 8): 'py3',
    ('test_retries_once_before_giving_up', 9): 'outline',
    ('test_retries_once_before_giving_up', 10): 'py5',
    ('test_retries_once_before_giving_up', 11): 'py6',
    ('test_retries_once_before_giving_up', 12): 'SCENES',
    ('test_retries_once_before_giving_up', 13): 'py8',
    ('test_retries_once_before_giving_up', 14): 'py10',
    ('test_retries_once_before_giving_up', 15): 'py12',
    ('test_retries_once_before_giving_up', 16): 'py14',
    ('test_retries_once_before_giving_up', 18): 'py4',
    ('test_retries_once_before_giving_up', 19): 'py7',
    ('test_retries_once_before_giving_up', 20): 'assert %(py9)s',
    ('test_retries_once_before_giving_up', 21): 'py9',
    ('test_empty_scenes_do_not_crash_the_fallback', 2): '值班',
    ('test_empty_scenes_do_not_crash_the_fallback', 3): 'assert %(py17)s\n{%(py17)s = %(py13)s\n{%(py13)s = %(py11)s\n{%(py11)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}.mechanical\n}(%(py7)s\n{%(py7)s = %(py5)s()\n}, %(py9)s)\n}.endswith\n}(%(py15)s)\n}',
    ('test_empty_scenes_do_not_crash_the_fallback', 4): 'py0',
    ('test_empty_scenes_do_not_crash_the_fallback', 5): 'stitcher',
    ('test_empty_scenes_do_not_crash_the_fallback', 6): 'py2',
    ('test_empty_scenes_do_not_crash_the_fallback', 7): 'py4',
    ('test_empty_scenes_do_not_crash_the_fallback', 8): 'py5',
    ('test_empty_scenes_do_not_crash_the_fallback', 9): 'outline',
    ('test_empty_scenes_do_not_crash_the_fallback', 10): 'py7',
    ('test_empty_scenes_do_not_crash_the_fallback', 11): 'py9',
    ('test_empty_scenes_do_not_crash_the_fallback', 12): 'py11',
    ('test_empty_scenes_do_not_crash_the_fallback', 13): 'py13',
    ('test_empty_scenes_do_not_crash_the_fallback', 14): 'py15',
    ('test_empty_scenes_do_not_crash_the_fallback', 15): 'py17',
    ('TestPipelineTreatsItAsNotPassed', 0): 'TestPipelineTreatsItAsNotPassed',
    ('TestPipelineTreatsItAsNotPassed', 1): '降级稿绝不能当成稿落进 book/chapters/ —— 那是"不合格产出不覆盖"那条\n防线的同一个道理。',
    ('_run', 2): '上游 403',
    ('test_chapter_is_not_passed', 1): 'assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_chapter_is_not_passed', 2): 'py0',
    ('test_chapter_is_not_passed', 3): 'r',
    ('test_chapter_is_not_passed', 4): 'py2',
    ('test_chapter_is_not_passed', 6): 'assert %(py2)s\n{%(py2)s = %(py0)s.stitch_degraded\n}',
    ('test_chapter_is_not_passed', 7): 'archivist',
    ('test_chapter_is_not_passed', 8): 'py5',
    ('test_chapter_is_not_passed', 9): '没通过就不该归档',
    ('test_chapter_is_not_passed', 10): '\n>assert %(py7)s',
    ('test_chapter_is_not_passed', 11): 'py7',
    ('test_prose_is_still_there_to_look_at', 0): '场景一',
    ('test_prose_is_still_there_to_look_at', 1): '场景二',
    ('test_prose_is_still_there_to_look_at', 2): 'py3',
    ('test_prose_is_still_there_to_look_at', 3): 'py5',
    ('test_prose_is_still_there_to_look_at', 4): 'r',
    ('test_prose_is_still_there_to_look_at', 5): 'py7',
    ('test_prose_is_still_there_to_look_at', 6): '%(py9)s',
    ('test_prose_is_still_there_to_look_at', 7): 'py9',
    ('test_prose_is_still_there_to_look_at', 8): 'py12',
    ('test_prose_is_still_there_to_look_at', 9): 'py14',
    ('test_prose_is_still_there_to_look_at', 10): 'py16',
    ('test_prose_is_still_there_to_look_at', 11): '%(py18)s',
    ('test_prose_is_still_there_to_look_at', 12): 'py18',
    ('test_prose_is_still_there_to_look_at', 13): 'assert %(py21)s',
    ('test_prose_is_still_there_to_look_at', 14): 'py21',
    ('test_note_explains_what_to_do', 1): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_note_explains_what_to_do', 2): 'py0',
    ('test_note_explains_what_to_do', 3): 'any',
    ('test_note_explains_what_to_do', 4): 'py2',
    ('test_note_explains_what_to_do', 5): 'py4',
    ('<genexpr>', 0): '机械拼接',
    ('<genexpr>', 0): '重跑',
    ('test_no_revision_rounds_are_wasted', 0): '问题在缝合，重写场景救不了它 —— 别再烧两轮修订。',
    ('test_no_revision_rounds_are_wasted', 1): 'py0',
    ('test_no_revision_rounds_are_wasted', 2): 'r',
    ('test_no_revision_rounds_are_wasted', 3): 'py2',
    ('test_no_revision_rounds_are_wasted', 4): 'py5',
    ('test_no_revision_rounds_are_wasted', 5): 'assert %(py7)s',
    ('test_no_revision_rounds_are_wasted', 6): 'py7',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
class Client:
    'Client'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  25           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('Client')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          25
    # |               STORE_NAME               3 (__firstlineno__)
    # |  26           LOAD_CONST               1 ('按脚本行事的假 LLM：可以抛异常，也可以吐残缺内容。')
    # |               STORE_NAME               4 (__doc__)
    # |  28           LOAD_CONST               2 (<code object __init__ at 0x101657bb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 28>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (__init__)
    # |  31           LOAD_CONST               3 (<code object complete at 0x101513870, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 31>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (complete)
    # |               LOAD_CONST               4 (('n', 'outcomes'))
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __init__ at 0x101657bb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 28>:
    # |  28           RESUME                   0
    # |  29           LOAD_GLOBAL              1 (list + NULL)
    # |               LOAD_FAST_BORROW         1 (outcomes)
    # |               CALL                     1
    # |               LOAD_SMALL_INT           0
    # |               SWAP                     2
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               1 (outcomes)
    # |               LOAD_FAST_BORROW         0 (self)
    # |               STORE_ATTR               2 (n)
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object complete at 0x101513870, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 31>:
    # |   --           MAKE_CELL                5 (out)
    # |   31           RESUME                   0
    # |   32           LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                0 (outcomes)
    # |                LOAD_GLOBAL              3 (min + NULL)
    # |                LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                4 (n)
    # |                LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                0 (outcomes)
    # |                CALL                     1
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               10 (-)
    # |                CALL                     2
    # |                BINARY_OP               26 ([])
    # |                STORE_DEREF              5 (out)
    # |   33           LOAD_FAST_BORROW         0 (self)
    # |                COPY                     1
    # |                LOAD_ATTR                4 (n)
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                SWAP                     2
    # |                STORE_ATTR               2 (n)
    # |   34           LOAD_GLOBAL              9 (isinstance + NULL)
    # |                LOAD_DEREF               5 (out)
    # |                LOAD_GLOBAL             10 (Exception)
    # |                CALL                     2
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        3 (to L1)
    # |                NOT_TAKEN
    # |   35           LOAD_DEREF               5 (out)
    # |                RAISE_VARARGS            1
    # |   36   L1:     LOAD_BUILD_CLASS
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (out)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object R at 0x1015f65b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 36>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_CONST               2 ('R')
    # |                CALL                     2
    # |                STORE_FAST               4 (R)
    # |   37           LOAD_FAST_BORROW         4 (R)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                RETURN_VALUE
    # | Disassembly of <code object R at 0x1015f65b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 36>:
    # |   --           COPY_FREE_VARS           1
    # |   36           RESUME                   0
    # |                LOAD_NAME                0 (__name__)
    # |                STORE_NAME               1 (__module__)
    # |                LOAD_CONST               0 ('Client.complete.<locals>.R')
    # |                STORE_NAME               2 (__qualname__)
    # |                LOAD_SMALL_INT          36
    # |                STORE_NAME               3 (__firstlineno__)
    # |                LOAD_LOCALS
    # |                LOAD_FROM_DICT_OR_DEREF  0 (out)
    # |                STORE_NAME               4 (text)
    # |                LOAD_CONST               1 (())
    # |                STORE_NAME               5 (__static_attributes__)
    # |                LOAD_CONST               2 (None)
    # |                RETURN_VALUE

    def __init__(self, *outcomes):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |  28           RESUME                   0
        # |  29           LOAD_GLOBAL              1 (list + NULL)
        # |               LOAD_FAST_BORROW         1 (outcomes)
        # |               CALL                     1
        # |               LOAD_SMALL_INT           0
        # |               SWAP                     2
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               1 (outcomes)
        # |               LOAD_FAST_BORROW         0 (self)
        # |               STORE_ATTR               2 (n)
        # |               LOAD_CONST               1 (None)
        # |               RETURN_VALUE

    def complete(self, role, prompt, **kw):
        'R'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                5 (out)
        # |   31           RESUME                   0
        # |   32           LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                0 (outcomes)
        # |                LOAD_GLOBAL              3 (min + NULL)
        # |                LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                4 (n)
        # |                LOAD_GLOBAL              7 (len + NULL)
        # |                LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                0 (outcomes)
        # |                CALL                     1
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               10 (-)
        # |                CALL                     2
        # |                BINARY_OP               26 ([])
        # |                STORE_DEREF              5 (out)
        # |   33           LOAD_FAST_BORROW         0 (self)
        # |                COPY                     1
        # |                LOAD_ATTR                4 (n)
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               13 (+=)
        # |                SWAP                     2
        # |                STORE_ATTR               2 (n)
        # |   34           LOAD_GLOBAL              9 (isinstance + NULL)
        # |                LOAD_DEREF               5 (out)
        # |                LOAD_GLOBAL             10 (Exception)
        # |                CALL                     2
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE        3 (to L1)
        # |                NOT_TAKEN
        # |   35           LOAD_DEREF               5 (out)
        # |                RAISE_VARARGS            1
        # |   36   L1:     LOAD_BUILD_CLASS
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (out)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object R at 0x1015f65b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 36>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_CONST               2 ('R')
        # |                CALL                     2
        # |                STORE_FAST               4 (R)
        # |   37           LOAD_FAST_BORROW         4 (R)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                RETURN_VALUE
        # | Disassembly of <code object R at 0x1015f65b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 36>:
        # |   --           COPY_FREE_VARS           1
        # |   36           RESUME                   0
        # |                LOAD_NAME                0 (__name__)
        # |                STORE_NAME               1 (__module__)
        # |                LOAD_CONST               0 ('Client.complete.<locals>.R')
        # |                STORE_NAME               2 (__qualname__)
        # |                LOAD_SMALL_INT          36
        # |                STORE_NAME               3 (__firstlineno__)
        # |                LOAD_LOCALS
        # |                LOAD_FROM_DICT_OR_DEREF  0 (out)
        # |                STORE_NAME               4 (text)
        # |                LOAD_CONST               1 (())
        # |                STORE_NAME               5 (__static_attributes__)
        # |                LOAD_CONST               2 (None)
        # |                RETURN_VALUE

        class R:
            'Client.complete.<locals>.R'
            # ── 函数体（字节码重建见 BODY 段）──
            # |   --           COPY_FREE_VARS           1
            # |   36           RESUME                   0
            # |                LOAD_NAME                0 (__name__)
            # |                STORE_NAME               1 (__module__)
            # |                LOAD_CONST               0 ('Client.complete.<locals>.R')
            # |                STORE_NAME               2 (__qualname__)
            # |                LOAD_SMALL_INT          36
            # |                STORE_NAME               3 (__firstlineno__)
            # |                LOAD_LOCALS
            # |                LOAD_FROM_DICT_OR_DEREF  0 (out)
            # |                STORE_NAME               4 (text)
            # |                LOAD_CONST               1 (())
            # |                STORE_NAME               5 (__static_attributes__)
            # |                LOAD_CONST               2 (None)
            # |                RETURN_VALUE



def stitcher(*outcomes):
    pass  # 无 docstring
    # ── 函数体（字节码重建见 BODY 段）──
    # |  40           RESUME                   0
    # |  41           LOAD_GLOBAL              0 (Stitcher)
    # |               LOAD_ATTR                2 (__new__)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (Stitcher)
    # |               CALL                     1
    # |               STORE_FAST               1 (s)
    # |  42           LOAD_GLOBAL              5 (Client + NULL)
    # |               LOAD_FAST_BORROW         0 (outcomes)
    # |               PUSH_NULL
    # |               CALL_FUNCTION_EX
    # |               LOAD_FAST_BORROW         1 (s)
    # |               STORE_ATTR               3 (client)
    # |  43           LOAD_CONST               0 (None)
    # |               LOAD_FAST_BORROW         1 (s)
    # |               STORE_ATTR               4 (skills)
    # |  44           LOAD_CONST               1 (<code object <lambda> at 0x1060b5df0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 44>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         1 (s)
    # |               STORE_ATTR               5 (system_core)
    # |  45           LOAD_FAST_BORROW         1 (s)
    # |               RETURN_VALUE
    # | Disassembly of <code object <lambda> at 0x1060b5df0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 44>:
    # |  44           RESUME                   0
    # |               LOAD_CONST               0 ('角色')
    # |               RETURN_VALUE

class TestMechanicalFallback:
    'TestMechanicalFallback'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  51           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestMechanicalFallback')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          51
    # |               STORE_NAME               3 (__firstlineno__)
    # |  52           LOAD_CONST               1 (<code object test_api_failure_still_yields_the_prose at 0x7bc729d800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 52>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_api_failure_still_yields_the_prose)
    # |  59           LOAD_CONST               2 (<code object test_truncated_output_also_falls_back at 0x7bc6dadc00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 59>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_truncated_output_also_falls_back)
    # |  65           LOAD_CONST               3 (<code object test_fallback_carries_a_title_the_gate_accepts at 0x7bc6da2300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 65>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_fallback_carries_a_title_the_gate_accepts)
    # |  73           LOAD_CONST               4 (<code object test_retries_once_before_giving_up at 0x7bc6cb3100, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 73>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_retries_once_before_giving_up)
    # |  79           LOAD_CONST               5 (<code object test_empty_scenes_do_not_crash_the_fallback at 0x7bc6da2800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 79>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_empty_scenes_do_not_crash_the_fallback)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_api_failure_still_yields_the_prose at 0x7bc729d800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 52>:
    # |   52            RESUME                   0
    # |   54            LOAD_GLOBAL              0 (pytest)
    # |                 LOAD_ATTR                2 (raises)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              4 (StitchFailed)
    # |                 CALL                     1
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     STORE_FAST               1 (e)
    # |   55            LOAD_GLOBAL              7 (stitcher + NULL)
    # |                 LOAD_GLOBAL              9 (RuntimeError + NULL)
    # |                 LOAD_CONST               1 ('上游 403')
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 LOAD_ATTR               11 (stitch + NULL|self)
    # |                 LOAD_GLOBAL             13 (outline + NULL)
    # |                 CALL                     0
    # |                 LOAD_GLOBAL             14 (SCENES)
    # |                 CALL                     2
    # |                 POP_TOP
    # |   54    L2:     LOAD_CONST               2 (None)
    # |                 LOAD_CONST               2 (None)
    # |                 LOAD_CONST               2 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |   56    L3:     LOAD_CONST               3 ('第一场的正文')
    # |                 STORE_FAST               2 (@py_assert0)
    # |                 LOAD_FAST_CHECK          1 (e)
    # |                 LOAD_ATTR               16 (value)
    # |                 STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |                 LOAD_ATTR               18 (fallback)
    # |                 STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
    # |                 LOAD_FAST_BORROW         4 (@py_assert6)
    # |                 CONTAINS_OP              0 (in)
    # |                 STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       221 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              12 (('in',))
    # |                 LOAD_FAST_BORROW         5 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              13 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.value\n}.fallback\n}',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               4 ('py1')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               5 ('py3')
    # |                 LOAD_CONST               6 ('e')
    # |                 LOAD_GLOBAL             26 (@py_builtins)
    # |                 LOAD_ATTR               28 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (e)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (e)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               6 ('e')
    # |         L6:     LOAD_CONST               7 ('py5')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST               8 ('py7')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               6 (@py_format8)
    # |                 LOAD_CONST               9 ('assert %(py9)s')
    # |                 LOAD_CONST              10 ('py9')
    # |                 LOAD_FAST_BORROW         6 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format10)
    # |                 LOAD_GLOBAL             33 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               34 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST               2 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               2 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
    # |   57            LOAD_CONST              11 ('第二场的正文')
    # |                 STORE_FAST_LOAD_FAST    33 (@py_assert0, e)
    # |                 LOAD_ATTR               16 (value)
    # |                 STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |                 LOAD_ATTR               18 (fallback)
    # |                 STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
    # |                 LOAD_FAST_BORROW         4 (@py_assert6)
    # |                 CONTAINS_OP              0 (in)
    # |                 STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       221 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              12 (('in',))
    # |                 LOAD_FAST_BORROW         5 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              13 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.value\n}.fallback\n}',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               4 ('py1')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               5 ('py3')
    # |                 LOAD_CONST               6 ('e')
    # |                 LOAD_GLOBAL             26 (@py_builtins)
    # |                 LOAD_ATTR               28 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               30 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (e)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (e)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST               6 ('e')
    # |        L10:     LOAD_CONST               7 ('py5')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST               8 ('py7')
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               6 (@py_format8)
    # |                 LOAD_CONST               9 ('assert %(py9)s')
    # |                 LOAD_CONST              10 ('py9')
    # |                 LOAD_FAST_BORROW         6 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format10)
    # |                 LOAD_GLOBAL             33 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             20 (@pytest_ar)
    # |                 LOAD_ATTR               34 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST               2 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               2 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
    # |                 LOAD_CONST               2 (None)
    # |                 RETURN_VALUE
    # |   54   L12:     PUSH_EXC_INFO
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
    # |                 EXTENDED_ARG             2
    # |                 JUMP_BACKWARD_NO_INTERRUPT 544 (to L3)
    # |   --   L15:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L12 [2] lasti
    # |   L12 to L14 -> L15 [4] lasti
    # | Disassembly of <code object test_truncated_output_also_falls_back at 0x7bc6dadc00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 59>:
    # |   59            RESUME                   0
    # |   61            LOAD_GLOBAL              0 (pytest)
    # |                 LOAD_ATTR                2 (raises)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              4 (StitchFailed)
    # |                 CALL                     1
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L1:     STORE_FAST               1 (e)
    # |   62            LOAD_GLOBAL              7 (stitcher + NULL)
    # |                 LOAD_CONST               1 ('太短了。')
    # |                 CALL                     1
    # |                 LOAD_ATTR                9 (stitch + NULL|self)
    # |                 LOAD_GLOBAL             11 (outline + NULL)
    # |                 CALL                     0
    # |                 LOAD_GLOBAL             12 (SCENES)
    # |                 CALL                     2
    # |                 POP_TOP
    # |   61    L2:     LOAD_CONST               2 (None)
    # |                 LOAD_CONST               2 (None)
    # |                 LOAD_CONST               2 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |   63    L3:     LOAD_CONST               3 ('第一场的正文')
    # |                 STORE_FAST               2 (@py_assert0)
    # |                 LOAD_FAST_CHECK          1 (e)
    # |                 LOAD_ATTR               14 (value)
    # |                 STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |                 LOAD_ATTR               16 (fallback)
    # |                 STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
    # |                 LOAD_FAST_BORROW         4 (@py_assert6)
    # |                 CONTAINS_OP              0 (in)
    # |                 STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       221 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              11 (('in',))
    # |                 LOAD_FAST_BORROW         5 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              12 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.value\n}.fallback\n}',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               4 ('py1')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST               5 ('py3')
    # |                 LOAD_CONST               6 ('e')
    # |                 LOAD_GLOBAL             24 (@py_builtins)
    # |                 LOAD_ATTR               26 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (e)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         1 (e)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               6 ('e')
    # |         L6:     LOAD_CONST               7 ('py5')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST               8 ('py7')
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert6)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               6 (@py_format8)
    # |                 LOAD_CONST               9 ('assert %(py9)s')
    # |                 LOAD_CONST              10 ('py9')
    # |                 LOAD_FAST_BORROW         6 (@py_format8)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format10)
    # |                 LOAD_GLOBAL             31 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             18 (@pytest_ar)
    # |                 LOAD_ATTR               32 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_format10)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST               2 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               2 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
    # |                 LOAD_CONST               2 (None)
    # |                 RETURN_VALUE
    # |   61    L8:     PUSH_EXC_INFO
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
    # |                 EXTENDED_ARG             1
    # |                 JUMP_BACKWARD_NO_INTERRUPT 282 (to L3)
    # |   --   L11:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L8 [2] lasti
    # |   L8 to L10 -> L11 [4] lasti
    # | Disassembly of <code object test_fallback_carries_a_title_the_gate_accepts at 0x7bc6da2300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 65>:
    # |  65           RESUME                   0
    # |  67           LOAD_GLOBAL              1 (stitcher + NULL)
    # |               CALL                     0
    # |               STORE_FAST               1 (s)
    # |  68           LOAD_FAST_BORROW         1 (s)
    # |               LOAD_ATTR                3 (mechanical + NULL|self)
    # |               LOAD_GLOBAL              5 (outline + NULL)
    # |               CALL                     0
    # |               LOAD_GLOBAL              6 (SCENES)
    # |               CALL                     2
    # |               STORE_FAST               2 (text)
    # |  69           LOAD_FAST_BORROW         2 (text)
    # |               LOAD_ATTR                8 (startswith)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               1 ('## 第1章 值班')
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       185 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               2 ('assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.startswith\n}(%(py4)s)\n}')
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('text')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (text)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (text)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('text')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
    # |  70           LOAD_GLOBAL             24 (Gate)
    # |               LOAD_ATTR               26 (from_config)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             28 (CONFIG)
    # |               CALL                     1
    # |               LOAD_ATTR               31 (check + NULL|self)
    # |               LOAD_FAST_BORROW         2 (text)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               9 (('expected_ch',))
    # |               CALL_KW                  2
    # |               STORE_FAST               7 (report)
    # |  71           LOAD_CONST              10 (<code object <genexpr> at 0x101657cc0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 71>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         7 (report)
    # |               LOAD_ATTR               32 (errors)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_GLOBAL             35 (any + NULL)
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_CONST              11 ('assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST              12 ('any')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             34 (any)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             34 (any)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST              12 ('any')
    # |       L7:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format6)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL             14 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x101657cc0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 71>:
    # |   71           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                19 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (f, f)
    # |                LOAD_ATTR                0 (rule)
    # |                LOAD_CONST               0 ('title')
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
    # | Disassembly of <code object test_retries_once_before_giving_up at 0x7bc6cb3100, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 73>:
    # |  73            RESUME                   0
    # |  75            LOAD_GLOBAL              1 (stitcher + NULL)
    # |                LOAD_GLOBAL              3 (RuntimeError + NULL)
    # |                LOAD_CONST               1 ('403')
    # |                CALL                     1
    # |                LOAD_GLOBAL              5 (make_chapter + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST               2 (('ch',))
    # |                CALL_KW                  1
    # |                CALL                     2
    # |                STORE_FAST               1 (c)
    # |  76            LOAD_FAST_BORROW         1 (c)
    # |                LOAD_ATTR                6 (stitch)
    # |                STORE_FAST               2 (@py_assert1)
    # |                LOAD_GLOBAL              9 (outline + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                LOAD_GLOBAL             10 (SCENES)
    # |                CALL                     2
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert7, @py_assert7)
    # |                LOAD_ATTR               12 (startswith)
    # |                STORE_FAST               5 (@py_assert9)
    # |                LOAD_CONST               3 ('## 第1章')
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert9)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert13, @py_assert13)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       423 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_CONST               4 ('assert %(py14)s\n{%(py14)s = %(py10)s\n{%(py10)s = %(py8)s\n{%(py8)s = %(py2)s\n{%(py2)s = %(py0)s.stitch\n}(%(py5)s\n{%(py5)s = %(py3)s()\n}, %(py6)s)\n}.startswith\n}(%(py12)s)\n}')
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('c')
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
    # |                LOAD_FAST_BORROW         1 (c)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (c)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               6 ('c')
    # |        L3:     LOAD_CONST               7 ('py2')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py3')
    # |                LOAD_CONST               9 ('outline')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (outline)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (outline)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               9 ('outline')
    # |        L6:     LOAD_CONST              10 ('py5')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py6')
    # |                LOAD_CONST              12 ('SCENES')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (SCENES)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (SCENES)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              12 ('SCENES')
    # |        L9:     LOAD_CONST              13 ('py8')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert7)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py10')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py12')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py14')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert13)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format15)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               26 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format15)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              17 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert9)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert11, @py_assert13)
    # |  77            LOAD_FAST_BORROW         1 (c)
    # |                LOAD_ATTR               28 (client)
    # |                STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
    # |                LOAD_ATTR               30 (n)
    # |                STORE_FAST               9 (@py_assert3)
    # |                LOAD_SMALL_INT           2
    # |                STORE_FAST_LOAD_FAST   169 (@py_assert6, @py_assert3)
    # |                LOAD_FAST_BORROW        10 (@py_assert6)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       221 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               32 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              22 (('==',))
    # |                LOAD_FAST_BORROW        11 (@py_assert5)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              23 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.client\n}.n\n} == %(py7)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert3, @py_assert6)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('c')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (c)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L12)
    # |                NOT_TAKEN
    # |       L11:     LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (c)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L13)
    # |       L12:     LOAD_CONST               6 ('c')
    # |       L13:     LOAD_CONST               7 ('py2')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              18 ('py4')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              19 ('py7')
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert6)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format8)
    # |                LOAD_CONST              20 ('assert %(py9)s')
    # |                LOAD_CONST              21 ('py9')
    # |                LOAD_FAST_BORROW        12 (@py_format8)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format10)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             18 (@pytest_ar)
    # |                LOAD_ATTR               26 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_format10)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L14:     LOAD_CONST              17 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  186 (@py_assert5, @py_assert6)
    # |                LOAD_CONST              17 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_empty_scenes_do_not_crash_the_fallback at 0x7bc6da2800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 79>:
    # |  79           RESUME                   0
    # |  80           LOAD_GLOBAL              1 (stitcher + NULL)
    # |               CALL                     0
    # |               STORE_FAST_LOAD_FAST    17 (@py_assert1, @py_assert1)
    # |               LOAD_ATTR                2 (mechanical)
    # |               STORE_FAST               2 (@py_assert3)
    # |               LOAD_GLOBAL              5 (outline + NULL)
    # |               CALL                     0
    # |               STORE_FAST               3 (@py_assert6)
    # |               LOAD_CONST               0 ('')
    # |               LOAD_CONST               1 ('  ')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST    66 (@py_assert8, @py_assert3)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert6, @py_assert8)
    # |               CALL                     2
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert10, @py_assert10)
    # |               LOAD_ATTR                6 (endswith)
    # |               STORE_FAST               6 (@py_assert12)
    # |               LOAD_CONST               2 ('值班')
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert14, @py_assert12)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert14)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert16, @py_assert16)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       389 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_CONST               3 ('assert %(py17)s\n{%(py17)s = %(py13)s\n{%(py13)s = %(py11)s\n{%(py11)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}.mechanical\n}(%(py7)s\n{%(py7)s = %(py5)s()\n}, %(py9)s)\n}.endswith\n}(%(py15)s)\n}')
    # |               LOAD_CONST               4 ('py0')
    # |               LOAD_CONST               5 ('stitcher')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (stitcher)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (stitcher)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('stitcher')
    # |       L3:     LOAD_CONST               6 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py5')
    # |               LOAD_CONST               9 ('outline')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (outline)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (outline)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               9 ('outline')
    # |       L6:     LOAD_CONST              10 ('py7')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py9')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert8)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py11')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert10)
    # |               CALL                     1
    # |               LOAD_CONST              13 ('py13')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert12)
    # |               CALL                     1
    # |               LOAD_CONST              14 ('py15')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert14)
    # |               CALL                     1
    # |               LOAD_CONST              15 ('py17')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert16)
    # |               CALL                     1
    # |               BUILD_MAP               10
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format18)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format18)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              16 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert6)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert8)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert10)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert12)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert14, @py_assert16)
    # |               LOAD_CONST              16 (None)
    # |               RETURN_VALUE

    def test_api_failure_still_yields_the_prose(self):
        '上游 403 是实测最常见的失败方式。正文不能跟着一起没。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   52            RESUME                   0
        # |   54            LOAD_GLOBAL              0 (pytest)
        # |                 LOAD_ATTR                2 (raises)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              4 (StitchFailed)
        # |                 CALL                     1
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     STORE_FAST               1 (e)
        # |   55            LOAD_GLOBAL              7 (stitcher + NULL)
        # |                 LOAD_GLOBAL              9 (RuntimeError + NULL)
        # |                 LOAD_CONST               1 ('上游 403')
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 LOAD_ATTR               11 (stitch + NULL|self)
        # |                 LOAD_GLOBAL             13 (outline + NULL)
        # |                 CALL                     0
        # |                 LOAD_GLOBAL             14 (SCENES)
        # |                 CALL                     2
        # |                 POP_TOP
        # |   54    L2:     LOAD_CONST               2 (None)
        # |                 LOAD_CONST               2 (None)
        # |                 LOAD_CONST               2 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |   56    L3:     LOAD_CONST               3 ('第一场的正文')
        # |                 STORE_FAST               2 (@py_assert0)
        # |                 LOAD_FAST_CHECK          1 (e)
        # |                 LOAD_ATTR               16 (value)
        # |                 STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |                 LOAD_ATTR               18 (fallback)
        # |                 STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
        # |                 LOAD_FAST_BORROW         4 (@py_assert6)
        # |                 CONTAINS_OP              0 (in)
        # |                 STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       221 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              12 (('in',))
        # |                 LOAD_FAST_BORROW         5 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              13 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.value\n}.fallback\n}',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               4 ('py1')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               5 ('py3')
        # |                 LOAD_CONST               6 ('e')
        # |                 LOAD_GLOBAL             26 (@py_builtins)
        # |                 LOAD_ATTR               28 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (e)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (e)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               6 ('e')
        # |         L6:     LOAD_CONST               7 ('py5')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST               8 ('py7')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               6 (@py_format8)
        # |                 LOAD_CONST               9 ('assert %(py9)s')
        # |                 LOAD_CONST              10 ('py9')
        # |                 LOAD_FAST_BORROW         6 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format10)
        # |                 LOAD_GLOBAL             33 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               34 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST               2 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               2 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
        # |   57            LOAD_CONST              11 ('第二场的正文')
        # |                 STORE_FAST_LOAD_FAST    33 (@py_assert0, e)
        # |                 LOAD_ATTR               16 (value)
        # |                 STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |                 LOAD_ATTR               18 (fallback)
        # |                 STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
        # |                 LOAD_FAST_BORROW         4 (@py_assert6)
        # |                 CONTAINS_OP              0 (in)
        # |                 STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       221 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              12 (('in',))
        # |                 LOAD_FAST_BORROW         5 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              13 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.value\n}.fallback\n}',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               4 ('py1')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               5 ('py3')
        # |                 LOAD_CONST               6 ('e')
        # |                 LOAD_GLOBAL             26 (@py_builtins)
        # |                 LOAD_ATTR               28 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               30 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (e)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (e)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST               6 ('e')
        # |        L10:     LOAD_CONST               7 ('py5')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST               8 ('py7')
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               6 (@py_format8)
        # |                 LOAD_CONST               9 ('assert %(py9)s')
        # |                 LOAD_CONST              10 ('py9')
        # |                 LOAD_FAST_BORROW         6 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format10)
        # |                 LOAD_GLOBAL             33 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             20 (@pytest_ar)
        # |                 LOAD_ATTR               34 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST               2 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               2 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
        # |                 LOAD_CONST               2 (None)
        # |                 RETURN_VALUE
        # |   54   L12:     PUSH_EXC_INFO
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
        # |                 EXTENDED_ARG             2
        # |                 JUMP_BACKWARD_NO_INTERRUPT 544 (to L3)
        # |   --   L15:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L12 [2] lasti
        # |   L12 to L14 -> L15 [4] lasti

    def test_truncated_output_also_falls_back(self):
        '实测过一次只吐 87 字就 end_turn 收工。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   59            RESUME                   0
        # |   61            LOAD_GLOBAL              0 (pytest)
        # |                 LOAD_ATTR                2 (raises)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              4 (StitchFailed)
        # |                 CALL                     1
        # |                 COPY                     1
        # |                 LOAD_SPECIAL             1 (__exit__)
        # |                 SWAP                     2
        # |                 SWAP                     3
        # |                 LOAD_SPECIAL             0 (__enter__)
        # |                 CALL                     0
        # |         L1:     STORE_FAST               1 (e)
        # |   62            LOAD_GLOBAL              7 (stitcher + NULL)
        # |                 LOAD_CONST               1 ('太短了。')
        # |                 CALL                     1
        # |                 LOAD_ATTR                9 (stitch + NULL|self)
        # |                 LOAD_GLOBAL             11 (outline + NULL)
        # |                 CALL                     0
        # |                 LOAD_GLOBAL             12 (SCENES)
        # |                 CALL                     2
        # |                 POP_TOP
        # |   61    L2:     LOAD_CONST               2 (None)
        # |                 LOAD_CONST               2 (None)
        # |                 LOAD_CONST               2 (None)
        # |                 CALL                     3
        # |                 POP_TOP
        # |   63    L3:     LOAD_CONST               3 ('第一场的正文')
        # |                 STORE_FAST               2 (@py_assert0)
        # |                 LOAD_FAST_CHECK          1 (e)
        # |                 LOAD_ATTR               14 (value)
        # |                 STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |                 LOAD_ATTR               16 (fallback)
        # |                 STORE_FAST_LOAD_FAST    66 (@py_assert6, @py_assert0)
        # |                 LOAD_FAST_BORROW         4 (@py_assert6)
        # |                 CONTAINS_OP              0 (in)
        # |                 STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       221 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              11 (('in',))
        # |                 LOAD_FAST_BORROW         5 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              12 (('%(py1)s in %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py3)s.value\n}.fallback\n}',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 36 (@py_assert0, @py_assert6)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               4 ('py1')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST               5 ('py3')
        # |                 LOAD_CONST               6 ('e')
        # |                 LOAD_GLOBAL             24 (@py_builtins)
        # |                 LOAD_ATTR               26 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (e)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         1 (e)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               6 ('e')
        # |         L6:     LOAD_CONST               7 ('py5')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST               8 ('py7')
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert6)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               6 (@py_format8)
        # |                 LOAD_CONST               9 ('assert %(py9)s')
        # |                 LOAD_CONST              10 ('py9')
        # |                 LOAD_FAST_BORROW         6 (@py_format8)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format10)
        # |                 LOAD_GLOBAL             31 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             18 (@pytest_ar)
        # |                 LOAD_ATTR               32 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_format10)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST               2 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               2 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   52 (@py_assert4, @py_assert6)
        # |                 LOAD_CONST               2 (None)
        # |                 RETURN_VALUE
        # |   61    L8:     PUSH_EXC_INFO
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
        # |                 EXTENDED_ARG             1
        # |                 JUMP_BACKWARD_NO_INTERRUPT 282 (to L3)
        # |   --   L11:     COPY                     3
        # |                 POP_EXCEPT
        # |                 RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L2 -> L8 [2] lasti
        # |   L8 to L10 -> L11 [4] lasti

    def test_fallback_carries_a_title_the_gate_accepts(self):
        '没有标题的话，gate 会先报标题错，掩盖掉真正的原因。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  65           RESUME                   0
        # |  67           LOAD_GLOBAL              1 (stitcher + NULL)
        # |               CALL                     0
        # |               STORE_FAST               1 (s)
        # |  68           LOAD_FAST_BORROW         1 (s)
        # |               LOAD_ATTR                3 (mechanical + NULL|self)
        # |               LOAD_GLOBAL              5 (outline + NULL)
        # |               CALL                     0
        # |               LOAD_GLOBAL              6 (SCENES)
        # |               CALL                     2
        # |               STORE_FAST               2 (text)
        # |  69           LOAD_FAST_BORROW         2 (text)
        # |               LOAD_ATTR                8 (startswith)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               1 ('## 第1章 值班')
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       185 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               2 ('assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.startswith\n}(%(py4)s)\n}')
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('text')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (text)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (text)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('text')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
        # |  70           LOAD_GLOBAL             24 (Gate)
        # |               LOAD_ATTR               26 (from_config)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             28 (CONFIG)
        # |               CALL                     1
        # |               LOAD_ATTR               31 (check + NULL|self)
        # |               LOAD_FAST_BORROW         2 (text)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               9 (('expected_ch',))
        # |               CALL_KW                  2
        # |               STORE_FAST               7 (report)
        # |  71           LOAD_CONST              10 (<code object <genexpr> at 0x101657cc0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 71>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         7 (report)
        # |               LOAD_ATTR               32 (errors)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_GLOBAL             35 (any + NULL)
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_CONST              11 ('assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST              12 ('any')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             34 (any)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             34 (any)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST              12 ('any')
        # |       L7:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format6)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL             14 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x101657cc0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 71>:
        # |   71           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                19 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (f, f)
        # |                LOAD_ATTR                0 (rule)
        # |                LOAD_CONST               0 ('title')
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

    def test_retries_once_before_giving_up(self):
        '第一次失败可能只是抖动；但不能无限试 —— 这是最贵的一次调用。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  73            RESUME                   0
        # |  75            LOAD_GLOBAL              1 (stitcher + NULL)
        # |                LOAD_GLOBAL              3 (RuntimeError + NULL)
        # |                LOAD_CONST               1 ('403')
        # |                CALL                     1
        # |                LOAD_GLOBAL              5 (make_chapter + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST               2 (('ch',))
        # |                CALL_KW                  1
        # |                CALL                     2
        # |                STORE_FAST               1 (c)
        # |  76            LOAD_FAST_BORROW         1 (c)
        # |                LOAD_ATTR                6 (stitch)
        # |                STORE_FAST               2 (@py_assert1)
        # |                LOAD_GLOBAL              9 (outline + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                LOAD_GLOBAL             10 (SCENES)
        # |                CALL                     2
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert7, @py_assert7)
        # |                LOAD_ATTR               12 (startswith)
        # |                STORE_FAST               5 (@py_assert9)
        # |                LOAD_CONST               3 ('## 第1章')
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert11, @py_assert9)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert13, @py_assert13)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       423 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_CONST               4 ('assert %(py14)s\n{%(py14)s = %(py10)s\n{%(py10)s = %(py8)s\n{%(py8)s = %(py2)s\n{%(py2)s = %(py0)s.stitch\n}(%(py5)s\n{%(py5)s = %(py3)s()\n}, %(py6)s)\n}.startswith\n}(%(py12)s)\n}')
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('c')
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
        # |                LOAD_FAST_BORROW         1 (c)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (c)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               6 ('c')
        # |        L3:     LOAD_CONST               7 ('py2')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py3')
        # |                LOAD_CONST               9 ('outline')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (outline)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (outline)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               9 ('outline')
        # |        L6:     LOAD_CONST              10 ('py5')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py6')
        # |                LOAD_CONST              12 ('SCENES')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (SCENES)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (SCENES)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              12 ('SCENES')
        # |        L9:     LOAD_CONST              13 ('py8')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert7)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py10')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert9)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py12')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                LOAD_CONST              16 ('py14')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert13)
        # |                CALL                     1
        # |                BUILD_MAP                9
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format15)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               26 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format15)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              17 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert9)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert11, @py_assert13)
        # |  77            LOAD_FAST_BORROW         1 (c)
        # |                LOAD_ATTR               28 (client)
        # |                STORE_FAST_LOAD_FAST    34 (@py_assert1, @py_assert1)
        # |                LOAD_ATTR               30 (n)
        # |                STORE_FAST               9 (@py_assert3)
        # |                LOAD_SMALL_INT           2
        # |                STORE_FAST_LOAD_FAST   169 (@py_assert6, @py_assert3)
        # |                LOAD_FAST_BORROW        10 (@py_assert6)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       221 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               32 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              22 (('==',))
        # |                LOAD_FAST_BORROW        11 (@py_assert5)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              23 (('%(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s.client\n}.n\n} == %(py7)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 154 (@py_assert3, @py_assert6)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('c')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (c)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L12)
        # |                NOT_TAKEN
        # |       L11:     LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (c)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L13)
        # |       L12:     LOAD_CONST               6 ('c')
        # |       L13:     LOAD_CONST               7 ('py2')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              18 ('py4')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              19 ('py7')
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert6)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format8)
        # |                LOAD_CONST              20 ('assert %(py9)s')
        # |                LOAD_CONST              21 ('py9')
        # |                LOAD_FAST_BORROW        12 (@py_format8)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format10)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             18 (@pytest_ar)
        # |                LOAD_ATTR               26 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_format10)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L14:     LOAD_CONST              17 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  186 (@py_assert5, @py_assert6)
        # |                LOAD_CONST              17 (None)
        # |                RETURN_VALUE

    def test_empty_scenes_do_not_crash_the_fallback(self):
        '值班'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  79           RESUME                   0
        # |  80           LOAD_GLOBAL              1 (stitcher + NULL)
        # |               CALL                     0
        # |               STORE_FAST_LOAD_FAST    17 (@py_assert1, @py_assert1)
        # |               LOAD_ATTR                2 (mechanical)
        # |               STORE_FAST               2 (@py_assert3)
        # |               LOAD_GLOBAL              5 (outline + NULL)
        # |               CALL                     0
        # |               STORE_FAST               3 (@py_assert6)
        # |               LOAD_CONST               0 ('')
        # |               LOAD_CONST               1 ('  ')
        # |               BUILD_LIST               2
        # |               STORE_FAST_LOAD_FAST    66 (@py_assert8, @py_assert3)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert6, @py_assert8)
        # |               CALL                     2
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert10, @py_assert10)
        # |               LOAD_ATTR                6 (endswith)
        # |               STORE_FAST               6 (@py_assert12)
        # |               LOAD_CONST               2 ('值班')
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert14, @py_assert12)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert14)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert16, @py_assert16)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       389 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_CONST               3 ('assert %(py17)s\n{%(py17)s = %(py13)s\n{%(py13)s = %(py11)s\n{%(py11)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}.mechanical\n}(%(py7)s\n{%(py7)s = %(py5)s()\n}, %(py9)s)\n}.endswith\n}(%(py15)s)\n}')
        # |               LOAD_CONST               4 ('py0')
        # |               LOAD_CONST               5 ('stitcher')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (stitcher)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (stitcher)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('stitcher')
        # |       L3:     LOAD_CONST               6 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py5')
        # |               LOAD_CONST               9 ('outline')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (outline)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (outline)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               9 ('outline')
        # |       L6:     LOAD_CONST              10 ('py7')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py9')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert8)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py11')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert10)
        # |               CALL                     1
        # |               LOAD_CONST              13 ('py13')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert12)
        # |               CALL                     1
        # |               LOAD_CONST              14 ('py15')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert14)
        # |               CALL                     1
        # |               LOAD_CONST              15 ('py17')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert16)
        # |               CALL                     1
        # |               BUILD_MAP               10
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format18)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format18)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              16 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert6)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert8)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert10)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert12)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert14, @py_assert16)
        # |               LOAD_CONST              16 (None)
        # |               RETURN_VALUE


class TestPipelineTreatsItAsNotPassed:
    'TestPipelineTreatsItAsNotPassed'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  83           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestPipelineTreatsItAsNotPassed')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          83
    # |               STORE_NAME               3 (__firstlineno__)
    # |  84           LOAD_CONST               1 ('降级稿绝不能当成稿落进 book/chapters/ —— 那是"不合格产出不覆盖"那条\n防线的同一个道理。')
    # |               STORE_NAME               4 (__doc__)
    # |  87           LOAD_CONST               2 (<code object _run at 0x1014be0b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 87>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (_run)
    # |  92           LOAD_CONST               3 (<code object test_chapter_is_not_passed at 0x7bc729de00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 92>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_chapter_is_not_passed)
    # |  98           LOAD_CONST               4 (<code object test_prose_is_still_there_to_look_at at 0x7bc729e400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 98>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_prose_is_still_there_to_look_at)
    # | 102           LOAD_CONST               5 (<code object test_note_explains_what_to_do at 0x7bc6da3700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 102>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_note_explains_what_to_do)
    # | 107           LOAD_CONST               6 (<code object test_no_revision_rounds_are_wasted at 0x7bc72d3900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 107>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_no_revision_rounds_are_wasted)
    # |               LOAD_CONST               7 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object _run at 0x1014be0b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 87>:
    # |  87           RESUME                   0
    # |  88           LOAD_GLOBAL              1 (build + NULL)
    # |               LOAD_GLOBAL              3 (make_chapter + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               1 (('ch',))
    # |               CALL_KW                  1
    # |               BUILD_LIST               1
    # |               LOAD_GLOBAL              4 (PASS)
    # |               BUILD_LIST               1
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     3
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST_STORE_FAST   35 (p, _)
    # |               STORE_FAST               4 (a)
    # |  89           LOAD_GLOBAL              7 (stitcher + NULL)
    # |               LOAD_GLOBAL              9 (RuntimeError + NULL)
    # |               LOAD_CONST               2 ('上游 403')
    # |               CALL                     1
    # |               LOAD_GLOBAL              9 (RuntimeError + NULL)
    # |               LOAD_CONST               2 ('上游 403')
    # |               CALL                     1
    # |               CALL                     2
    # |               LOAD_FAST_BORROW         2 (p)
    # |               STORE_ATTR               3 (stitcher)
    # |  90           LOAD_FAST_BORROW         2 (p)
    # |               LOAD_ATTR               11 (run + NULL|self)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               LOAD_GLOBAL             13 (volume + NULL)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           1
    # |               CALL                     3
    # |               LOAD_FAST_BORROW         4 (a)
    # |               BUILD_TUPLE              2
    # |               RETURN_VALUE
    # | Disassembly of <code object test_chapter_is_not_passed at 0x7bc729de00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 92>:
    # |  92            RESUME                   0
    # |  93            LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                1 (_run + NULL|self)
    # |                LOAD_FAST_BORROW         1 (sample_state)
    # |                CALL                     1
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   35 (r, archivist)
    # |  94            LOAD_FAST_BORROW         2 (r)
    # |                LOAD_ATTR                2 (passed)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       141 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_CONST               1 ('assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('r')
    # |                LOAD_GLOBAL              4 (@py_builtins)
    # |                LOAD_ATTR                6 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               3 ('r')
    # |        L3:     LOAD_CONST               4 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format4)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format4)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               5 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
    # |  95            LOAD_FAST_BORROW         2 (r)
    # |                LOAD_ATTR               18 (stitch_degraded)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       141 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_CONST               6 ('assert %(py2)s\n{%(py2)s = %(py0)s.stitch_degraded\n}')
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('r')
    # |                LOAD_GLOBAL              4 (@py_builtins)
    # |                LOAD_ATTR                6 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (r)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (r)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               3 ('r')
    # |        L7:     LOAD_CONST               4 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format3)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format3)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST               5 (None)
    # |                STORE_FAST               4 (@py_assert1)
    # |  96            LOAD_FAST_BORROW         3 (archivist)
    # |                LOAD_ATTR               20 (called)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                STORE_FAST_LOAD_FAST   132 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         8 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       226 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              12 (('==',))
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              13 (('%(py2)s\n{%(py2)s = %(py0)s.called\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               7 ('archivist')
    # |                LOAD_GLOBAL              4 (@py_builtins)
    # |                LOAD_ATTR                6 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (archivist)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L10)
    # |                NOT_TAKEN
    # |        L9:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (archivist)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L11)
    # |       L10:     LOAD_CONST               7 ('archivist')
    # |       L11:     LOAD_CONST               4 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format6)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST               9 ('没通过就不该归档')
    # |                CALL                     1
    # |                LOAD_CONST              10 ('\n>assert %(py7)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              11 ('py7')
    # |                LOAD_FAST_BORROW         9 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format8)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L12:     LOAD_CONST               5 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   88 (@py_assert3, @py_assert4)
    # |                LOAD_CONST               5 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_prose_is_still_there_to_look_at at 0x7bc729e400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 98>:
    # |  98           RESUME                   0
    # |  99           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                1 (_run + NULL|self)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   35 (r, _)
    # | 100           BUILD_LIST               0
    # |               STORE_FAST               4 (@py_assert1)
    # |               LOAD_CONST               0 ('场景一')
    # |               STORE_FAST_LOAD_FAST    82 (@py_assert2, r)
    # |               LOAD_ATTR                2 (text)
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert6, @py_assert2)
    # |               LOAD_FAST_BORROW         6 (@py_assert6)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |               STORE_FAST_LOAD_FAST   135 (@py_assert0, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       19 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('场景二')
    # |               STORE_FAST_LOAD_FAST   146 (@py_assert11, r)
    # |               LOAD_ATTR                2 (text)
    # |               STORE_FAST_LOAD_FAST   169 (@py_assert15, @py_assert11)
    # |               LOAD_FAST_BORROW        10 (@py_assert15)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   187 (@py_assert13, @py_assert13)
    # |               STORE_FAST               8 (@py_assert0)
    # |       L1:     LOAD_FAST_BORROW         8 (@py_assert0)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       448 (to L9)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('in',))
    # |               LOAD_FAST_BORROW         7 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py3)s in %(py7)s\n{%(py7)s = %(py5)s.text\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py3')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py5')
    # |               LOAD_CONST               4 ('r')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               4 ('r')
    # |       L4:     LOAD_CONST               5 ('py7')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format8)
    # |               LOAD_CONST               6 ('%(py9)s')
    # |               LOAD_CONST               7 ('py9')
    # |               LOAD_FAST_BORROW        12 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   212 (@py_format10, @py_assert1)
    # |               LOAD_ATTR               17 (append + NULL|self)
    # |               LOAD_FAST_BORROW        13 (@py_format10)
    # |               CALL                     1
    # |               POP_TOP
    # |               LOAD_FAST_BORROW         7 (@py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE      185 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('in',))
    # |               LOAD_FAST_CHECK         11 (@py_assert13)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              18 (('%(py12)s in %(py16)s\n{%(py16)s = %(py14)s.text\n}',))
    # |               LOAD_FAST_CHECK          9 (@py_assert11)
    # |               LOAD_FAST_CHECK         10 (@py_assert15)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               8 ('py12')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert11)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py14')
    # |               LOAD_CONST               4 ('r')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               4 ('r')
    # |       L7:     LOAD_CONST              10 ('py16')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_assert15)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              14 (@py_format17)
    # |               LOAD_CONST              11 ('%(py18)s')
    # |               LOAD_CONST              12 ('py18')
    # |               LOAD_FAST_BORROW        14 (@py_format17)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   244 (@py_format19, @py_assert1)
    # |               LOAD_ATTR               17 (append + NULL|self)
    # |               LOAD_FAST_BORROW        15 (@py_format19)
    # |               CALL                     1
    # |               POP_TOP
    # |       L8:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_boolop)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BUILD_MAP                0
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              16 (@py_format20)
    # |               LOAD_CONST              13 ('assert %(py21)s')
    # |               LOAD_CONST              14 ('py21')
    # |               LOAD_FAST_BORROW        16 (@py_format20)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              17 (@py_format22)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        17 (@py_format22)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L9:     LOAD_CONST              15 (None)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert6)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert11)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  186 (@py_assert13, @py_assert15)
    # |               LOAD_CONST              15 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_note_explains_what_to_do at 0x7bc6da3700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 102>:
    # | 102           RESUME                   0
    # | 103           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                1 (_run + NULL|self)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   35 (r, _)
    # | 104           LOAD_CONST               0 (<code object <genexpr> at 0x1015d3430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 104>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         2 (r)
    # |               LOAD_ATTR                2 (notes)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               4 (@py_assert1)
    # |               LOAD_GLOBAL              5 (any + NULL)
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('any')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (any)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (any)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('any')
    # |       L3:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
    # | 105           LOAD_CONST               7 (<code object <genexpr> at 0x1015d3030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 105>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         2 (r)
    # |               LOAD_ATTR                2 (notes)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               4 (@py_assert1)
    # |               LOAD_GLOBAL              5 (any + NULL)
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('any')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (any)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (any)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               3 ('any')
    # |       L7:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x1015d3430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 104>:
    # |  104           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                10 (to L3)
    # |                STORE_FAST               1 (n)
    # |                LOAD_CONST               0 ('机械拼接')
    # |                LOAD_FAST_BORROW         1 (n)
    # |                CONTAINS_OP              0 (in)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           12 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
    # | Disassembly of <code object <genexpr> at 0x1015d3030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 105>:
    # |  105           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                10 (to L3)
    # |                STORE_FAST               1 (n)
    # |                LOAD_CONST               0 ('重跑')
    # |                LOAD_FAST_BORROW         1 (n)
    # |                CONTAINS_OP              0 (in)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           12 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
    # | Disassembly of <code object test_no_revision_rounds_are_wasted at 0x7bc72d3900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 107>:
    # | 107           RESUME                   0
    # | 109           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                1 (_run + NULL|self)
    # |               LOAD_FAST_BORROW         1 (sample_state)
    # |               CALL                     1
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   35 (r, _)
    # | 110           LOAD_FAST_BORROW         2 (r)
    # |               LOAD_ATTR                2 (revisions)
    # |               STORE_FAST               4 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               8 (('==',))
    # |               LOAD_FAST_BORROW         6 (@py_assert3)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               9 (('%(py2)s\n{%(py2)s = %(py0)s.revisions\n} == %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('r')
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
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (r)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('r')
    # |       L3:     LOAD_CONST               3 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py5')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format6)
    # |               LOAD_CONST               5 ('assert %(py7)s')
    # |               LOAD_CONST               6 ('py7')
    # |               LOAD_FAST_BORROW         7 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format8)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE

    def _run(self, sample_state):
        '上游 403'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  87           RESUME                   0
        # |  88           LOAD_GLOBAL              1 (build + NULL)
        # |               LOAD_GLOBAL              3 (make_chapter + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               1 (('ch',))
        # |               CALL_KW                  1
        # |               BUILD_LIST               1
        # |               LOAD_GLOBAL              4 (PASS)
        # |               BUILD_LIST               1
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     3
        # |               UNPACK_SEQUENCE          3
        # |               STORE_FAST_STORE_FAST   35 (p, _)
        # |               STORE_FAST               4 (a)
        # |  89           LOAD_GLOBAL              7 (stitcher + NULL)
        # |               LOAD_GLOBAL              9 (RuntimeError + NULL)
        # |               LOAD_CONST               2 ('上游 403')
        # |               CALL                     1
        # |               LOAD_GLOBAL              9 (RuntimeError + NULL)
        # |               LOAD_CONST               2 ('上游 403')
        # |               CALL                     1
        # |               CALL                     2
        # |               LOAD_FAST_BORROW         2 (p)
        # |               STORE_ATTR               3 (stitcher)
        # |  90           LOAD_FAST_BORROW         2 (p)
        # |               LOAD_ATTR               11 (run + NULL|self)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               LOAD_GLOBAL             13 (volume + NULL)
        # |               CALL                     0
        # |               LOAD_SMALL_INT           1
        # |               CALL                     3
        # |               LOAD_FAST_BORROW         4 (a)
        # |               BUILD_TUPLE              2
        # |               RETURN_VALUE

    def test_chapter_is_not_passed(self, sample_state):
        'assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  92            RESUME                   0
        # |  93            LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                1 (_run + NULL|self)
        # |                LOAD_FAST_BORROW         1 (sample_state)
        # |                CALL                     1
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   35 (r, archivist)
        # |  94            LOAD_FAST_BORROW         2 (r)
        # |                LOAD_ATTR                2 (passed)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                UNARY_NOT
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       141 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_CONST               1 ('assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               3 ('r')
        # |                LOAD_GLOBAL              4 (@py_builtins)
        # |                LOAD_ATTR                6 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               3 ('r')
        # |        L3:     LOAD_CONST               4 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format4)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format4)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               5 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
        # |  95            LOAD_FAST_BORROW         2 (r)
        # |                LOAD_ATTR               18 (stitch_degraded)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       141 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_CONST               6 ('assert %(py2)s\n{%(py2)s = %(py0)s.stitch_degraded\n}')
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               3 ('r')
        # |                LOAD_GLOBAL              4 (@py_builtins)
        # |                LOAD_ATTR                6 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (r)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (r)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               3 ('r')
        # |        L7:     LOAD_CONST               4 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format3)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format3)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST               5 (None)
        # |                STORE_FAST               4 (@py_assert1)
        # |  96            LOAD_FAST_BORROW         3 (archivist)
        # |                LOAD_ATTR               20 (called)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                STORE_FAST_LOAD_FAST   132 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         8 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       226 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              12 (('==',))
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              13 (('%(py2)s\n{%(py2)s = %(py0)s.called\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               7 ('archivist')
        # |                LOAD_GLOBAL              4 (@py_builtins)
        # |                LOAD_ATTR                6 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (archivist)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L10)
        # |                NOT_TAKEN
        # |        L9:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (archivist)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L11)
        # |       L10:     LOAD_CONST               7 ('archivist')
        # |       L11:     LOAD_CONST               4 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format6)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST               9 ('没通过就不该归档')
        # |                CALL                     1
        # |                LOAD_CONST              10 ('\n>assert %(py7)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              11 ('py7')
        # |                LOAD_FAST_BORROW         9 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format8)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L12:     LOAD_CONST               5 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   88 (@py_assert3, @py_assert4)
        # |                LOAD_CONST               5 (None)
        # |                RETURN_VALUE

    def test_prose_is_still_there_to_look_at(self, sample_state):
        '场景一'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  98           RESUME                   0
        # |  99           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                1 (_run + NULL|self)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   35 (r, _)
        # | 100           BUILD_LIST               0
        # |               STORE_FAST               4 (@py_assert1)
        # |               LOAD_CONST               0 ('场景一')
        # |               STORE_FAST_LOAD_FAST    82 (@py_assert2, r)
        # |               LOAD_ATTR                2 (text)
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert6, @py_assert2)
        # |               LOAD_FAST_BORROW         6 (@py_assert6)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |               STORE_FAST_LOAD_FAST   135 (@py_assert0, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       19 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('场景二')
        # |               STORE_FAST_LOAD_FAST   146 (@py_assert11, r)
        # |               LOAD_ATTR                2 (text)
        # |               STORE_FAST_LOAD_FAST   169 (@py_assert15, @py_assert11)
        # |               LOAD_FAST_BORROW        10 (@py_assert15)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   187 (@py_assert13, @py_assert13)
        # |               STORE_FAST               8 (@py_assert0)
        # |       L1:     LOAD_FAST_BORROW         8 (@py_assert0)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       448 (to L9)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('in',))
        # |               LOAD_FAST_BORROW         7 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py3)s in %(py7)s\n{%(py7)s = %(py5)s.text\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py3')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py5')
        # |               LOAD_CONST               4 ('r')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               4 ('r')
        # |       L4:     LOAD_CONST               5 ('py7')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format8)
        # |               LOAD_CONST               6 ('%(py9)s')
        # |               LOAD_CONST               7 ('py9')
        # |               LOAD_FAST_BORROW        12 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   212 (@py_format10, @py_assert1)
        # |               LOAD_ATTR               17 (append + NULL|self)
        # |               LOAD_FAST_BORROW        13 (@py_format10)
        # |               CALL                     1
        # |               POP_TOP
        # |               LOAD_FAST_BORROW         7 (@py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE      185 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('in',))
        # |               LOAD_FAST_CHECK         11 (@py_assert13)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              18 (('%(py12)s in %(py16)s\n{%(py16)s = %(py14)s.text\n}',))
        # |               LOAD_FAST_CHECK          9 (@py_assert11)
        # |               LOAD_FAST_CHECK         10 (@py_assert15)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               8 ('py12')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert11)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py14')
        # |               LOAD_CONST               4 ('r')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               4 ('r')
        # |       L7:     LOAD_CONST              10 ('py16')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_assert15)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              14 (@py_format17)
        # |               LOAD_CONST              11 ('%(py18)s')
        # |               LOAD_CONST              12 ('py18')
        # |               LOAD_FAST_BORROW        14 (@py_format17)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   244 (@py_format19, @py_assert1)
        # |               LOAD_ATTR               17 (append + NULL|self)
        # |               LOAD_FAST_BORROW        15 (@py_format19)
        # |               CALL                     1
        # |               POP_TOP
        # |       L8:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_boolop)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BUILD_MAP                0
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              16 (@py_format20)
        # |               LOAD_CONST              13 ('assert %(py21)s')
        # |               LOAD_CONST              14 ('py21')
        # |               LOAD_FAST_BORROW        16 (@py_format20)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              17 (@py_format22)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        17 (@py_format22)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L9:     LOAD_CONST              15 (None)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert6)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert11)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  186 (@py_assert13, @py_assert15)
        # |               LOAD_CONST              15 (None)
        # |               RETURN_VALUE

    def test_note_explains_what_to_do(self, sample_state):
        'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 102           RESUME                   0
        # | 103           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                1 (_run + NULL|self)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   35 (r, _)
        # | 104           LOAD_CONST               0 (<code object <genexpr> at 0x1015d3430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 104>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         2 (r)
        # |               LOAD_ATTR                2 (notes)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               4 (@py_assert1)
        # |               LOAD_GLOBAL              5 (any + NULL)
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('any')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (any)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (any)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('any')
        # |       L3:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
        # | 105           LOAD_CONST               7 (<code object <genexpr> at 0x1015d3030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 105>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         2 (r)
        # |               LOAD_ATTR                2 (notes)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               4 (@py_assert1)
        # |               LOAD_GLOBAL              5 (any + NULL)
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('any')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (any)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (any)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               3 ('any')
        # |       L7:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x1015d3430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 104>:
        # |  104           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                10 (to L3)
        # |                STORE_FAST               1 (n)
        # |                LOAD_CONST               0 ('机械拼接')
        # |                LOAD_FAST_BORROW         1 (n)
        # |                CONTAINS_OP              0 (in)
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           12 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti
        # | Disassembly of <code object <genexpr> at 0x1015d3030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_stitch_fallback.py", line 105>:
        # |  105           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                10 (to L3)
        # |                STORE_FAST               1 (n)
        # |                LOAD_CONST               0 ('重跑')
        # |                LOAD_FAST_BORROW         1 (n)
        # |                CONTAINS_OP              0 (in)
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           12 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti

    def test_no_revision_rounds_are_wasted(self, sample_state):
        '问题在缝合，重写场景救不了它 —— 别再烧两轮修订。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 107           RESUME                   0
        # | 109           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                1 (_run + NULL|self)
        # |               LOAD_FAST_BORROW         1 (sample_state)
        # |               CALL                     1
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   35 (r, _)
        # | 110           LOAD_FAST_BORROW         2 (r)
        # |               LOAD_ATTR                2 (revisions)
        # |               STORE_FAST               4 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               8 (('==',))
        # |               LOAD_FAST_BORROW         6 (@py_assert3)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               9 (('%(py2)s\n{%(py2)s = %(py0)s.revisions\n} == %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('r')
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
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (r)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('r')
        # |       L3:     LOAD_CONST               3 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py5')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format6)
        # |               LOAD_CONST               5 ('assert %(py7)s')
        # |               LOAD_CONST               6 ('py7')
        # |               LOAD_FAST_BORROW         7 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format8)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

