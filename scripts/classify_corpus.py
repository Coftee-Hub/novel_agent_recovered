# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py
# 来源   : classify_corpus.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '按题材给语料分类，用于挑选范本。\n\n不靠书名和印象，读实际文本统计特征词密度。输出每本书的时代（古言/现言）、\n场景（校园/职场）与特殊题材标签，供人工决策。\n\n    .venv/bin/python scripts/classify_corpus.py <目录> [--csv out.csv]\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '按题材给语料分类，用于挑选范本。\n\n不靠书名和印象，读实际文本统计特征词密度。输出每本书的时代（古言/现言）、\n场景（校园/职场）与特殊题材标签，供人工决策。\n\n    .venv/bin/python scripts/classify_corpus.py <目录> [--csv out.csv]\n',
    5: 'src',
    7: '古代',
    8: '高中',
    9: '大学',
    10: '职场',
    11: '电竞',
    12: '军旅',
    13: '医疗',
    14: '娱乐圈',
    15: 'dict[str, tuple[str, ...]]',
    16: 'SIGNALS',
    17: '[一-鿿]',
    19: 'BookProfile',
    24: '__main__',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('BookProfile', 0): 'BookProfile',
    ('BookProfile', 1): 'str',
    ('BookProfile', 2): 'name',
    ('BookProfile', 3): 'author',
    ('BookProfile', 4): 'int',
    ('BookProfile', 5): 'chars',
    ('BookProfile', 6): 'chapters',
    ('BookProfile', 7): 'encoding',
    ('BookProfile', 9): 'dict[str, float]',
    ('BookProfile', 10): 'density',
    ('BookProfile', 11): 'head',
    ('BookProfile', 12): 'tail',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('era', 0): '古代',
    ('era', 1): '古言',
    ('era', 2): '现言',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'bool',
    ('campus_to_work', 0): '校园在前、职场在后 —— 正是目标作品的结构。',
    ('campus_to_work', 1): '大学',
    ('campus_to_work', 2): '高中',
    ('campus_to_work', 3): '职场',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('setting', 0): '古言',
    ('setting', 1): '古代',
    ('setting', 2): '★跨阶段',
    ('setting', 5): '都市(泛)',
    ('setting', 7): '/混',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[str]',
    ('special', 0): '电竞',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'BookProfile | None',
    ('profile', 3): '(',
    ('profile', 4): ')',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict[str, float]',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('main', 3): '*.txt',
    ('main', 6): '书名',
    ('main', 7): '26',
    ('main', 9): '作者',
    ('main', 10): '12',
    ('main', 11): '万字',
    ('main', 12): '>5',
    ('main', 13): '章',
    ('main', 14): '>4',
    ('main', 15): '时代',
    ('main', 16): '4',
    ('main', 17): '场景',
    ('main', 18): '10',
    ('main', 19): ' 特殊题材',
    ('main', 23): '5.1f',
    ('main', 24): '、',
    ('main', 25): '\n共 ',
    ('main', 26): ' 本',
    ('main', 32): ': ',
    ('main', 33): '--csv',
    ('main', 35): 'w',
    ('main', 37): 'utf-8-sig',
    ('main', 39): '.1f',
    ('main', 40): '\n已写出 ',
    ('main', 41): '--------------------------------------------------------------------------------------------',
    ('<lambda>', 0): '★跨阶段',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
class BookProfile:
    'BookProfile'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  48           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('BookProfile')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          48
    # |               STORE_NAME               3 (__firstlineno__)
    # |               SETUP_ANNOTATIONS
    # |  50           LOAD_CONST               1 ('str')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST               2 ('name')
    # |               STORE_SUBSCR
    # |  51           LOAD_CONST               1 ('str')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST               3 ('author')
    # |               STORE_SUBSCR
    # |  52           LOAD_CONST               4 ('int')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST               5 ('chars')
    # |               STORE_SUBSCR
    # |  53           LOAD_CONST               4 ('int')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST               6 ('chapters')
    # |               STORE_SUBSCR
    # |  54           LOAD_CONST               1 ('str')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST               7 ('encoding')
    # |               STORE_SUBSCR
    # |  55           LOAD_NAME                5 (field)
    # |               PUSH_NULL
    # |               LOAD_NAME                6 (dict)
    # |               LOAD_CONST               8 (('default_factory',))
    # |               CALL_KW                  1
    # |               STORE_NAME               7 (density)
    # |               LOAD_CONST               9 ('dict[str, float]')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST              10 ('density')
    # |               STORE_SUBSCR
    # |  56           LOAD_NAME                5 (field)
    # |               PUSH_NULL
    # |               LOAD_NAME                6 (dict)
    # |               LOAD_CONST               8 (('default_factory',))
    # |               CALL_KW                  1
    # |               STORE_NAME               8 (head)
    # |               LOAD_CONST               9 ('dict[str, float]')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST              11 ('head')
    # |               STORE_SUBSCR
    # |  57           LOAD_NAME                5 (field)
    # |               PUSH_NULL
    # |               LOAD_NAME                6 (dict)
    # |               LOAD_CONST               8 (('default_factory',))
    # |               CALL_KW                  1
    # |               STORE_NAME               9 (tail)
    # |               LOAD_CONST               9 ('dict[str, float]')
    # |               LOAD_NAME                4 (__annotations__)
    # |               LOAD_CONST              12 ('tail')
    # |               STORE_SUBSCR
    # |  59           LOAD_NAME               10 (property)
    # |  60           LOAD_CONST              13 (<code object __annotate__ at 0x103fa66a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 60>)
    # |               MAKE_FUNCTION
    # |               LOAD_CONST              14 (<code object era at 0x103faaaf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 59>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE  16 (annotate)
    # |  59           CALL                     0
    # |  60           STORE_NAME              11 (era)
    # |  63           LOAD_NAME               10 (property)
    # |  64           LOAD_CONST              15 (<code object __annotate__ at 0x103fa52f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 64>)
    # |               MAKE_FUNCTION
    # |               LOAD_CONST              16 (<code object campus_to_work at 0x78172f3300, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 63>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE  16 (annotate)
    # |  63           CALL                     0
    # |  64           STORE_NAME              12 (campus_to_work)
    # |  76           LOAD_NAME               10 (property)
    # |  77           LOAD_CONST              17 (<code object __annotate__ at 0x103fa64c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 77>)
    # |               MAKE_FUNCTION
    # |               LOAD_CONST              18 (<code object setting at 0x7816d76a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 76>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE  16 (annotate)
    # |  76           CALL                     0
    # |  77           STORE_NAME              13 (setting)
    # |  89           LOAD_NAME               10 (property)
    # |  90           LOAD_CONST              19 (<code object __annotate__ at 0x103fa6880, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 90>)
    # |               MAKE_FUNCTION
    # |               LOAD_CONST              20 (<code object special at 0x103fcf360, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 89>)
    # |               MAKE_FUNCTION
    # |               SET_FUNCTION_ATTRIBUTE  16 (annotate)
    # |  89           CALL                     0
    # |  90           STORE_NAME              14 (special)
    # |               LOAD_CONST              21 (())
    # |               STORE_NAME              15 (__static_attributes__)
    # |               LOAD_CONST              22 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object __annotate__ at 0x103fa66a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 60>:
    # |  60           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (format)
    # |               LOAD_SMALL_INT           2
    # |               COMPARE_OP             132 (>)
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               1 ('return')
    # |               LOAD_CONST               2 ('str')
    # |               BUILD_MAP                1
    # |               RETURN_VALUE
    # | Disassembly of <code object era at 0x103faaaf0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 59>:
    # |  59           RESUME                   0
    # |  61           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (density)
    # |               LOAD_ATTR                3 (get + NULL|self)
    # |               LOAD_CONST               0 ('古代')
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               LOAD_SMALL_INT           3
    # |               COMPARE_OP             148 (bool(>))
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('古言')
    # |               RETURN_VALUE
    # |       L1:     LOAD_CONST               2 ('现言')
    # |               RETURN_VALUE
    # | Disassembly of <code object __annotate__ at 0x103fa52f0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 64>:
    # |  64           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (format)
    # |               LOAD_SMALL_INT           2
    # |               COMPARE_OP             132 (>)
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               1 ('return')
    # |               LOAD_CONST               2 ('bool')
    # |               BUILD_MAP                1
    # |               RETURN_VALUE
    # | Disassembly of <code object campus_to_work at 0x78172f3300, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 63>:
    # |  63           RESUME                   0
    # |  66           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (head)
    # |               LOAD_ATTR                3 (get + NULL|self)
    # |               LOAD_CONST               1 ('大学')
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (head)
    # |               LOAD_ATTR                3 (get + NULL|self)
    # |               LOAD_CONST               2 ('高中')
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BINARY_OP                0 (+)
    # |               STORE_FAST               1 (campus_head)
    # |  67           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                4 (tail)
    # |               LOAD_ATTR                3 (get + NULL|self)
    # |               LOAD_CONST               1 ('大学')
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                4 (tail)
    # |               LOAD_ATTR                3 (get + NULL|self)
    # |               LOAD_CONST               2 ('高中')
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BINARY_OP                0 (+)
    # |               STORE_FAST               2 (campus_tail)
    # |  68           LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                0 (head)
    # |               LOAD_ATTR                3 (get + NULL|self)
    # |               LOAD_CONST               3 ('职场')
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               LOAD_FAST_BORROW         0 (self)
    # |               LOAD_ATTR                4 (tail)
    # |               LOAD_ATTR                3 (get + NULL|self)
    # |               LOAD_CONST               3 ('职场')
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               STORE_FAST_STORE_FAST   67 (work_tail, work_head)
    # |  70           LOAD_FAST_BORROW         1 (campus_head)
    # |               LOAD_CONST               4 (3.0)
    # |               COMPARE_OP             172 (>=)
    # |               COPY                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       44 (to L1)
    # |               NOT_TAKEN
    # |               POP_TOP
    # |  71           LOAD_FAST_BORROW         4 (work_tail)
    # |               LOAD_CONST               5 (2.0)
    # |               COMPARE_OP             172 (>=)
    # |  70           COPY                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       31 (to L1)
    # |               NOT_TAKEN
    # |               POP_TOP
    # |  72           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (work_tail, work_head)
    # |               LOAD_CONST               6 (1.6)
    # |               BINARY_OP                5 (*)
    # |               COMPARE_OP             132 (>)
    # |  70           COPY                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       12 (to L1)
    # |               NOT_TAKEN
    # |               POP_TOP
    # |  73           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (campus_head, campus_tail)
    # |               LOAD_CONST               7 (1.3)
    # |               BINARY_OP                5 (*)
    # |               COMPARE_OP             132 (>)
    # |  69   L1:     RETURN_VALUE
    # | Disassembly of <code object __annotate__ at 0x103fa64c0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 77>:
    # |  77           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (format)
    # |               LOAD_SMALL_INT           2
    # |               COMPARE_OP             132 (>)
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               1 ('return')
    # |               LOAD_CONST               2 ('str')
    # |               BUILD_MAP                1
    # |               RETURN_VALUE
    # | Disassembly of <code object setting at 0x7816d76a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 76>:
    # |   76           RESUME                   0
    # |   78           LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                0 (era)
    # |                LOAD_CONST               0 ('古言')
    # |                COMPARE_OP              88 (bool(==))
    # |                POP_JUMP_IF_FALSE        3 (to L1)
    # |                NOT_TAKEN
    # |   79           LOAD_CONST               1 ('古代')
    # |                RETURN_VALUE
    # |   80   L1:     LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                2 (campus_to_work)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        3 (to L2)
    # |                NOT_TAKEN
    # |   81           LOAD_CONST               2 ('★跨阶段')
    # |                RETURN_VALUE
    # |   82   L2:     LOAD_CONST               8 (('高中', '大学', '职场'))
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      1 (k)
    # |                SWAP                     2
    # |        L3:     BUILD_MAP                0
    # |                SWAP                     2
    # |        L4:     FOR_ITER                31 (to L5)
    # |                STORE_FAST_LOAD_FAST    17 (k, k)
    # |                LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                4 (density)
    # |                LOAD_ATTR                7 (get + NULL|self)
    # |                LOAD_FAST_BORROW         1 (k)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                MAP_ADD                  2
    # |                JUMP_BACKWARD           33 (to L4)
    # |        L5:     END_FOR
    # |                POP_ITER
    # |        L6:     STORE_FAST               2 (scores)
    # |                STORE_FAST               1 (k)
    # |   83           LOAD_GLOBAL              9 (max + NULL)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 34 (scores, scores)
    # |                LOAD_ATTR               10 (__getitem__)
    # |                LOAD_CONST               3 (('key',))
    # |                CALL_KW                  2
    # |                STORE_FAST               3 (top)
    # |   84           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (scores, top)
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST               4 (2.0)
    # |                COMPARE_OP              18 (bool(<))
    # |                POP_JUMP_IF_FALSE        3 (to L7)
    # |                NOT_TAKEN
    # |   85           LOAD_CONST               5 ('都市(泛)')
    # |                RETURN_VALUE
    # |   86   L7:     LOAD_GLOBAL             13 (sorted + NULL)
    # |                LOAD_FAST_BORROW         2 (scores)
    # |                LOAD_ATTR               15 (values + NULL|self)
    # |                CALL                     0
    # |                CALL                     1
    # |                LOAD_CONST               9 (-2)
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               4 (runner)
    # |   87           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (scores, top)
    # |                BINARY_OP               26 ([])
    # |                LOAD_FAST_BORROW         4 (runner)
    # |                LOAD_CONST               6 (1.6)
    # |                BINARY_OP                5 (*)
    # |                COMPARE_OP             148 (bool(>))
    # |                POP_JUMP_IF_FALSE        3 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         3 (top)
    # |                RETURN_VALUE
    # |        L8:     LOAD_FAST_BORROW         3 (top)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               7 ('/混')
    # |                BUILD_STRING             2
    # |                RETURN_VALUE
    # |   --   L9:     SWAP                     2
    # |                POP_TOP
    # |   82           SWAP                     2
    # |                STORE_FAST               1 (k)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L3 to L6 -> L9 [2]
    # | Disassembly of <code object __annotate__ at 0x103fa6880, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 90>:
    # |  90           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (format)
    # |               LOAD_SMALL_INT           2
    # |               COMPARE_OP             132 (>)
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               1 ('return')
    # |               LOAD_CONST               2 ('list[str]')
    # |               BUILD_MAP                1
    # |               RETURN_VALUE
    # | Disassembly of <code object special at 0x103fcf360, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 89>:
    # |   89           RESUME                   0
    # |   91           LOAD_CONST               2 (('电竞', '军旅', '医疗', '娱乐圈'))
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      1 (k)
    # |                SWAP                     2
    # |        L1:     BUILD_LIST               0
    # |                SWAP                     2
    # |        L2:     FOR_ITER                40 (to L5)
    # |                STORE_FAST               1 (k)
    # |   92           LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                0 (density)
    # |                LOAD_ATTR                3 (get + NULL|self)
    # |                LOAD_FAST_BORROW         1 (k)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                LOAD_CONST               1 (2.5)
    # |                COMPARE_OP             188 (bool(>=))
    # |   91   L3:     POP_JUMP_IF_TRUE         3 (to L4)
    # |                NOT_TAKEN
    # |                JUMP_BACKWARD           38 (to L2)
    # |        L4:     LOAD_FAST_BORROW         1 (k)
    # |                LIST_APPEND              2
    # |                JUMP_BACKWARD           42 (to L2)
    # |        L5:     END_FOR
    # |                POP_ITER
    # |        L6:     SWAP                     2
    # |                STORE_FAST               1 (k)
    # |                RETURN_VALUE
    # |   --   L7:     SWAP                     2
    # |                POP_TOP
    # |   91           SWAP                     2
    # |                STORE_FAST               1 (k)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L3 -> L7 [2]
    # |   L4 to L6 -> L7 [2]

    def era(self):
        '古代'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  59           RESUME                   0
        # |  61           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (density)
        # |               LOAD_ATTR                3 (get + NULL|self)
        # |               LOAD_CONST               0 ('古代')
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               LOAD_SMALL_INT           3
        # |               COMPARE_OP             148 (bool(>))
        # |               POP_JUMP_IF_FALSE        3 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('古言')
        # |               RETURN_VALUE
        # |       L1:     LOAD_CONST               2 ('现言')
        # |               RETURN_VALUE

    def campus_to_work(self):
        '校园在前、职场在后 —— 正是目标作品的结构。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  63           RESUME                   0
        # |  66           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (head)
        # |               LOAD_ATTR                3 (get + NULL|self)
        # |               LOAD_CONST               1 ('大学')
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (head)
        # |               LOAD_ATTR                3 (get + NULL|self)
        # |               LOAD_CONST               2 ('高中')
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BINARY_OP                0 (+)
        # |               STORE_FAST               1 (campus_head)
        # |  67           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                4 (tail)
        # |               LOAD_ATTR                3 (get + NULL|self)
        # |               LOAD_CONST               1 ('大学')
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                4 (tail)
        # |               LOAD_ATTR                3 (get + NULL|self)
        # |               LOAD_CONST               2 ('高中')
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BINARY_OP                0 (+)
        # |               STORE_FAST               2 (campus_tail)
        # |  68           LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                0 (head)
        # |               LOAD_ATTR                3 (get + NULL|self)
        # |               LOAD_CONST               3 ('职场')
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               LOAD_FAST_BORROW         0 (self)
        # |               LOAD_ATTR                4 (tail)
        # |               LOAD_ATTR                3 (get + NULL|self)
        # |               LOAD_CONST               3 ('职场')
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               STORE_FAST_STORE_FAST   67 (work_tail, work_head)
        # |  70           LOAD_FAST_BORROW         1 (campus_head)
        # |               LOAD_CONST               4 (3.0)
        # |               COMPARE_OP             172 (>=)
        # |               COPY                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       44 (to L1)
        # |               NOT_TAKEN
        # |               POP_TOP
        # |  71           LOAD_FAST_BORROW         4 (work_tail)
        # |               LOAD_CONST               5 (2.0)
        # |               COMPARE_OP             172 (>=)
        # |  70           COPY                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       31 (to L1)
        # |               NOT_TAKEN
        # |               POP_TOP
        # |  72           LOAD_FAST_BORROW_LOAD_FAST_BORROW 67 (work_tail, work_head)
        # |               LOAD_CONST               6 (1.6)
        # |               BINARY_OP                5 (*)
        # |               COMPARE_OP             132 (>)
        # |  70           COPY                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       12 (to L1)
        # |               NOT_TAKEN
        # |               POP_TOP
        # |  73           LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (campus_head, campus_tail)
        # |               LOAD_CONST               7 (1.3)
        # |               BINARY_OP                5 (*)
        # |               COMPARE_OP             132 (>)
        # |  69   L1:     RETURN_VALUE

    def setting(self):
        '古言'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   76           RESUME                   0
        # |   78           LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                0 (era)
        # |                LOAD_CONST               0 ('古言')
        # |                COMPARE_OP              88 (bool(==))
        # |                POP_JUMP_IF_FALSE        3 (to L1)
        # |                NOT_TAKEN
        # |   79           LOAD_CONST               1 ('古代')
        # |                RETURN_VALUE
        # |   80   L1:     LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                2 (campus_to_work)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE        3 (to L2)
        # |                NOT_TAKEN
        # |   81           LOAD_CONST               2 ('★跨阶段')
        # |                RETURN_VALUE
        # |   82   L2:     LOAD_CONST               8 (('高中', '大学', '职场'))
        # |                GET_ITER
        # |                LOAD_FAST_AND_CLEAR      1 (k)
        # |                SWAP                     2
        # |        L3:     BUILD_MAP                0
        # |                SWAP                     2
        # |        L4:     FOR_ITER                31 (to L5)
        # |                STORE_FAST_LOAD_FAST    17 (k, k)
        # |                LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                4 (density)
        # |                LOAD_ATTR                7 (get + NULL|self)
        # |                LOAD_FAST_BORROW         1 (k)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                MAP_ADD                  2
        # |                JUMP_BACKWARD           33 (to L4)
        # |        L5:     END_FOR
        # |                POP_ITER
        # |        L6:     STORE_FAST               2 (scores)
        # |                STORE_FAST               1 (k)
        # |   83           LOAD_GLOBAL              9 (max + NULL)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 34 (scores, scores)
        # |                LOAD_ATTR               10 (__getitem__)
        # |                LOAD_CONST               3 (('key',))
        # |                CALL_KW                  2
        # |                STORE_FAST               3 (top)
        # |   84           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (scores, top)
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST               4 (2.0)
        # |                COMPARE_OP              18 (bool(<))
        # |                POP_JUMP_IF_FALSE        3 (to L7)
        # |                NOT_TAKEN
        # |   85           LOAD_CONST               5 ('都市(泛)')
        # |                RETURN_VALUE
        # |   86   L7:     LOAD_GLOBAL             13 (sorted + NULL)
        # |                LOAD_FAST_BORROW         2 (scores)
        # |                LOAD_ATTR               15 (values + NULL|self)
        # |                CALL                     0
        # |                CALL                     1
        # |                LOAD_CONST               9 (-2)
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               4 (runner)
        # |   87           LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (scores, top)
        # |                BINARY_OP               26 ([])
        # |                LOAD_FAST_BORROW         4 (runner)
        # |                LOAD_CONST               6 (1.6)
        # |                BINARY_OP                5 (*)
        # |                COMPARE_OP             148 (bool(>))
        # |                POP_JUMP_IF_FALSE        3 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_FAST_BORROW         3 (top)
        # |                RETURN_VALUE
        # |        L8:     LOAD_FAST_BORROW         3 (top)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST               7 ('/混')
        # |                BUILD_STRING             2
        # |                RETURN_VALUE
        # |   --   L9:     SWAP                     2
        # |                POP_TOP
        # |   82           SWAP                     2
        # |                STORE_FAST               1 (k)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L3 to L6 -> L9 [2]

    def special(self):
        '电竞'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   89           RESUME                   0
        # |   91           LOAD_CONST               2 (('电竞', '军旅', '医疗', '娱乐圈'))
        # |                GET_ITER
        # |                LOAD_FAST_AND_CLEAR      1 (k)
        # |                SWAP                     2
        # |        L1:     BUILD_LIST               0
        # |                SWAP                     2
        # |        L2:     FOR_ITER                40 (to L5)
        # |                STORE_FAST               1 (k)
        # |   92           LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                0 (density)
        # |                LOAD_ATTR                3 (get + NULL|self)
        # |                LOAD_FAST_BORROW         1 (k)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                LOAD_CONST               1 (2.5)
        # |                COMPARE_OP             188 (bool(>=))
        # |   91   L3:     POP_JUMP_IF_TRUE         3 (to L4)
        # |                NOT_TAKEN
        # |                JUMP_BACKWARD           38 (to L2)
        # |        L4:     LOAD_FAST_BORROW         1 (k)
        # |                LIST_APPEND              2
        # |                JUMP_BACKWARD           42 (to L2)
        # |        L5:     END_FOR
        # |                POP_ITER
        # |        L6:     SWAP                     2
        # |                STORE_FAST               1 (k)
        # |                RETURN_VALUE
        # |   --   L7:     SWAP                     2
        # |                POP_TOP
        # |   91           SWAP                     2
        # |                STORE_FAST               1 (k)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L3 -> L7 [2]
        # |   L4 to L6 -> L7 [2]


def profile(path):
    '('
    # ── 函数体（字节码重建见 BODY 段）──
    # |   95           RESUME                   0
    # |   96           NOP
    # |   97   L1:     LOAD_GLOBAL              1 (read_text + NULL)
    # |                LOAD_FAST_BORROW         0 (path)
    # |                CALL                     1
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   18 (raw, encoding)
    # |  100   L2:     LOAD_GLOBAL              5 (clean + NULL)
    # |                LOAD_FAST                1 (raw)
    # |                CALL                     1
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   52 (body, _)
    # |  101           LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_GLOBAL              8 (_CJK)
    # |                LOAD_ATTR               11 (findall + NULL|self)
    # |                LOAD_FAST                3 (body)
    # |                CALL                     1
    # |                CALL                     1
    # |                STORE_FAST               5 (chars)
    # |  102           LOAD_FAST                5 (chars)
    # |                LOAD_CONST               1 (5000)
    # |                COMPARE_OP              18 (bool(<))
    # |                POP_JUMP_IF_FALSE        3 (to L3)
    # |                NOT_TAKEN
    # |  103           LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |  105   L3:     LOAD_FAST                0 (path)
    # |                LOAD_ATTR               12 (stem)
    # |                STORE_FAST               6 (stem)
    # |  106           LOAD_CONST               2 ('')
    # |                STORE_FAST               7 (author)
    # |  107           LOAD_CONST               3 ('(')
    # |                LOAD_FAST                6 (stem)
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_FALSE       69 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_FAST                6 (stem)
    # |                LOAD_ATTR               15 (endswith + NULL|self)
    # |                LOAD_CONST               4 (')')
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       46 (to L4)
    # |                NOT_TAKEN
    # |  108           LOAD_FAST                6 (stem)
    # |                LOAD_CONST               0 (None)
    # |                LOAD_FAST                6 (stem)
    # |                LOAD_ATTR               17 (rindex + NULL|self)
    # |                LOAD_CONST               3 ('(')
    # |                CALL                     1
    # |                BINARY_SLICE
    # |                LOAD_FAST_LOAD_FAST    102 (stem, stem)
    # |                LOAD_ATTR               17 (rindex + NULL|self)
    # |                LOAD_CONST               3 ('(')
    # |                CALL                     1
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               8 (-1)
    # |                BINARY_SLICE
    # |                STORE_FAST_STORE_FAST  118 (author, stem)
    # |  110   L4:     LOAD_CONST               5 (<code object __annotate__ at 0x103fa72d0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 110>)
    # |                MAKE_FUNCTION
    # |                LOAD_CONST               6 (<code object density_of at 0x103e522a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 110>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE  16 (annotate)
    # |                STORE_FAST               8 (density_of)
    # |  115           LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_FAST                3 (body)
    # |                CALL                     1
    # |                LOAD_GLOBAL             18 (SEGMENTS)
    # |                BINARY_OP                2 (//)
    # |                STORE_FAST               9 (seg)
    # |  116           LOAD_GLOBAL             21 (BookProfile + NULL)
    # |  117           LOAD_FAST                6 (stem)
    # |                LOAD_ATTR               23 (strip + NULL|self)
    # |                CALL                     0
    # |                LOAD_FAST_LOAD_FAST    117 (author, chars)
    # |  118           LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_GLOBAL             25 (split_chapters + NULL)
    # |                LOAD_FAST                3 (body)
    # |                CALL                     1
    # |                CALL                     1
    # |                LOAD_FAST                2 (encoding)
    # |  119           LOAD_FAST                8 (density_of)
    # |                PUSH_NULL
    # |                LOAD_FAST                3 (body)
    # |                CALL                     1
    # |  120           LOAD_FAST                8 (density_of)
    # |                PUSH_NULL
    # |                LOAD_FAST                3 (body)
    # |                LOAD_CONST               0 (None)
    # |                LOAD_FAST                9 (seg)
    # |                BINARY_SLICE
    # |                CALL                     1
    # |  121           LOAD_FAST                8 (density_of)
    # |                PUSH_NULL
    # |                LOAD_FAST_LOAD_FAST     57 (body, seg)
    # |                UNARY_NEGATIVE
    # |                LOAD_CONST               0 (None)
    # |                BINARY_SLICE
    # |                CALL                     1
    # |  116           LOAD_CONST               7 (('name', 'author', 'chars', 'chapters', 'encoding', 'density', 'head', 'tail'))
    # |                CALL_KW                  8
    # |                RETURN_VALUE
    # |   --   L5:     PUSH_EXC_INFO
    # |   98           LOAD_GLOBAL              2 (OSError)
    # |                CHECK_EXC_MATCH
    # |                POP_JUMP_IF_FALSE        5 (to L7)
    # |                NOT_TAKEN
    # |                POP_TOP
    # |   99   L6:     POP_EXCEPT
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |   98   L7:     RERAISE                  0
    # |   --   L8:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L2 -> L5 [0]
    # |   L5 to L6 -> L8 [1] lasti
    # |   L7 to L8 -> L8 [1] lasti
    # | Disassembly of <code object __annotate__ at 0x103fa72d0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 110>:
    # | 110           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (format)
    # |               LOAD_SMALL_INT           2
    # |               COMPARE_OP             132 (>)
    # |               POP_JUMP_IF_FALSE        3 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_COMMON_CONSTANT     1 (NotImplementedError)
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               1 ('text')
    # |               LOAD_CONST               2 ('str')
    # |               LOAD_CONST               3 ('return')
    # |               LOAD_CONST               4 ('dict[str, float]')
    # |               BUILD_MAP                2
    # |               RETURN_VALUE
    # | Disassembly of <code object density_of at 0x103e522a0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 110>:
    # |   --           MAKE_CELL                0 (text)
    # |  110           RESUME                   0
    # |  111           LOAD_GLOBAL              1 (len + NULL)
    # |                LOAD_GLOBAL              2 (_CJK)
    # |                LOAD_ATTR                5 (findall + NULL|self)
    # |                LOAD_DEREF               0 (text)
    # |                CALL                     1
    # |                CALL                     1
    # |                COPY                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         3 (to L1)
    # |                NOT_TAKEN
    # |                POP_TOP
    # |                LOAD_SMALL_INT           1
    # |        L1:     STORE_FAST               1 (n)
    # |  113           LOAD_GLOBAL              6 (SIGNALS)
    # |                LOAD_ATTR                9 (items + NULL|self)
    # |                CALL                     0
    # |                GET_ITER
    # |  112           LOAD_FAST_AND_CLEAR      2 (k)
    # |                LOAD_FAST_AND_CLEAR      3 (words)
    # |                SWAP                     3
    # |        L2:     BUILD_MAP                0
    # |                SWAP                     2
    # |  113   L3:     FOR_ITER                41 (to L4)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   35 (k, words)
    # |  112           LOAD_FAST_BORROW         2 (k)
    # |                LOAD_GLOBAL             11 (sum + NULL)
    # |                LOAD_FAST_BORROW         0 (text)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               1 (<code object <genexpr> at 0x103faad30, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 112>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_FAST_BORROW         3 (words)
    # |                GET_ITER
    # |                CALL                     0
    # |                CALL                     1
    # |                LOAD_CONST               2 (10000)
    # |                BINARY_OP                5 (*)
    # |                LOAD_FAST_BORROW         1 (n)
    # |                BINARY_OP               11 (/)
    # |                MAP_ADD                  2
    # |                JUMP_BACKWARD           43 (to L3)
    # |  113   L4:     END_FOR
    # |                POP_ITER
    # |  112   L5:     SWAP                     3
    # |                STORE_FAST               3 (words)
    # |                STORE_FAST               2 (k)
    # |                RETURN_VALUE
    # |   --   L6:     SWAP                     2
    # |                POP_TOP
    # |  112           SWAP                     3
    # |                STORE_FAST               3 (words)
    # |                STORE_FAST               2 (k)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L2 to L5 -> L6 [3]
    # | Disassembly of <code object <genexpr> at 0x103faad30, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 112>:
    # |   --           COPY_FREE_VARS           1
    # |  112           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                22 (to L3)
    # |                STORE_FAST               1 (w)
    # |                LOAD_DEREF               2 (text)
    # |                LOAD_ATTR                1 (count + NULL|self)
    # |                LOAD_FAST_BORROW         1 (w)
    # |                CALL                     1
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           24 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti

    def density_of(text):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL                0 (text)
        # |  110           RESUME                   0
        # |  111           LOAD_GLOBAL              1 (len + NULL)
        # |                LOAD_GLOBAL              2 (_CJK)
        # |                LOAD_ATTR                5 (findall + NULL|self)
        # |                LOAD_DEREF               0 (text)
        # |                CALL                     1
        # |                CALL                     1
        # |                COPY                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         3 (to L1)
        # |                NOT_TAKEN
        # |                POP_TOP
        # |                LOAD_SMALL_INT           1
        # |        L1:     STORE_FAST               1 (n)
        # |  113           LOAD_GLOBAL              6 (SIGNALS)
        # |                LOAD_ATTR                9 (items + NULL|self)
        # |                CALL                     0
        # |                GET_ITER
        # |  112           LOAD_FAST_AND_CLEAR      2 (k)
        # |                LOAD_FAST_AND_CLEAR      3 (words)
        # |                SWAP                     3
        # |        L2:     BUILD_MAP                0
        # |                SWAP                     2
        # |  113   L3:     FOR_ITER                41 (to L4)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   35 (k, words)
        # |  112           LOAD_FAST_BORROW         2 (k)
        # |                LOAD_GLOBAL             11 (sum + NULL)
        # |                LOAD_FAST_BORROW         0 (text)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               1 (<code object <genexpr> at 0x103faad30, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 112>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_FAST_BORROW         3 (words)
        # |                GET_ITER
        # |                CALL                     0
        # |                CALL                     1
        # |                LOAD_CONST               2 (10000)
        # |                BINARY_OP                5 (*)
        # |                LOAD_FAST_BORROW         1 (n)
        # |                BINARY_OP               11 (/)
        # |                MAP_ADD                  2
        # |                JUMP_BACKWARD           43 (to L3)
        # |  113   L4:     END_FOR
        # |                POP_ITER
        # |  112   L5:     SWAP                     3
        # |                STORE_FAST               3 (words)
        # |                STORE_FAST               2 (k)
        # |                RETURN_VALUE
        # |   --   L6:     SWAP                     2
        # |                POP_TOP
        # |  112           SWAP                     3
        # |                STORE_FAST               3 (words)
        # |                STORE_FAST               2 (k)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L2 to L5 -> L6 [3]
        # | Disassembly of <code object <genexpr> at 0x103faad30, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 112>:
        # |   --           COPY_FREE_VARS           1
        # |  112           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                22 (to L3)
        # |                STORE_FAST               1 (w)
        # |                LOAD_DEREF               2 (text)
        # |                LOAD_ATTR                1 (count + NULL|self)
        # |                LOAD_FAST_BORROW         1 (w)
        # |                CALL                     1
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           24 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               0 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti


def main():
    '*.txt'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  125            RESUME                   0
    # |  126            LOAD_GLOBAL              1 (len + NULL)
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 CALL                     1
    # |                 LOAD_SMALL_INT           2
    # |                 COMPARE_OP              18 (bool(<))
    # |                 POP_JUMP_IF_FALSE       18 (to L1)
    # |                 NOT_TAKEN
    # |  127            LOAD_GLOBAL              7 (print + NULL)
    # |                 LOAD_GLOBAL              8 (__doc__)
    # |                 CALL                     1
    # |                 POP_TOP
    # |  128            LOAD_SMALL_INT           2
    # |                 RETURN_VALUE
    # |  129    L1:     LOAD_GLOBAL             11 (Path + NULL)
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 LOAD_SMALL_INT           1
    # |                 BINARY_OP               26 ([])
    # |                 CALL                     1
    # |                 STORE_FAST               0 (src)
    # |  130            LOAD_GLOBAL             13 (sorted + NULL)
    # |  131            LOAD_CONST               1 (<code object <genexpr> at 0x10400bbb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 131>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_CONST               2 (<code object <genexpr> at 0x10400bcc0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 131>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_GLOBAL             13 (sorted + NULL)
    # |                 LOAD_FAST_BORROW         0 (src)
    # |                 LOAD_ATTR               15 (rglob + NULL|self)
    # |                 LOAD_CONST               3 ('*.txt')
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 GET_ITER
    # |                 CALL                     0
    # |  132            LOAD_CONST               4 (<code object <lambda> at 0x103faaf70, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 132>)
    # |                 MAKE_FUNCTION
    # |  130            LOAD_CONST               5 (('key',))
    # |                 CALL_KW                  2
    # |                 STORE_FAST               1 (books)
    # |  135            LOAD_GLOBAL              7 (print + NULL)
    # |                 LOAD_CONST               6 ('书名')
    # |                 LOAD_CONST               7 ('26')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_CONST               9 ('作者')
    # |                 LOAD_CONST              10 ('12')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_CONST              11 ('万字')
    # |                 LOAD_CONST              12 ('>5')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_CONST              13 ('章')
    # |                 LOAD_CONST              14 ('>4')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_CONST              15 ('时代')
    # |                 LOAD_CONST              16 ('4')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_CONST              17 ('场景')
    # |                 LOAD_CONST              18 ('10')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST              19 (' 特殊题材')
    # |                 BUILD_STRING            12
    # |                 CALL                     1
    # |                 POP_TOP
    # |  136            LOAD_GLOBAL              7 (print + NULL)
    # |                 LOAD_CONST              41 ('--------------------------------------------------------------------------------------------')
    # |                 CALL                     1
    # |                 POP_TOP
    # |  137            LOAD_FAST_BORROW         1 (books)
    # |                 GET_ITER
    # |         L2:     FOR_ITER               146 (to L3)
    # |                 STORE_FAST               2 (b)
    # |  138            LOAD_GLOBAL              7 (print + NULL)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               16 (name)
    # |                 LOAD_CONST              20 (slice(None, 25, None))
    # |                 BINARY_OP               26 ([])
    # |                 LOAD_CONST               7 ('26')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               18 (author)
    # |                 LOAD_CONST              21 (slice(None, 11, None))
    # |                 BINARY_OP               26 ([])
    # |                 LOAD_CONST              10 ('12')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               20 (chars)
    # |                 LOAD_CONST              22 (10000)
    # |                 BINARY_OP               11 (/)
    # |                 LOAD_CONST              23 ('5.1f')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |  139            LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               22 (chapters)
    # |                 LOAD_CONST              16 ('4')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               24 (era)
    # |                 LOAD_CONST              16 ('4')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               26 (setting)
    # |                 LOAD_CONST              18 ('10')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST               8 (' ')
    # |                 LOAD_CONST              24 ('、')
    # |                 LOAD_ATTR               29 (join + NULL|self)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               30 (special)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |  138            BUILD_STRING            13
    # |                 CALL                     1
    # |                 POP_TOP
    # |                 JUMP_BACKWARD          148 (to L2)
    # |  137    L3:     END_FOR
    # |                 POP_ITER
    # |  141            LOAD_GLOBAL              7 (print + NULL)
    # |                 LOAD_CONST              25 ('\n共 ')
    # |                 LOAD_GLOBAL              1 (len + NULL)
    # |                 LOAD_FAST_BORROW         1 (books)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              26 (' 本')
    # |                 BUILD_STRING             3
    # |                 CALL                     1
    # |                 POP_TOP
    # |  142            LOAD_SMALL_INT           0
    # |                 LOAD_CONST              27 (('Counter',))
    # |                 IMPORT_NAME             16 (collections)
    # |                 IMPORT_FROM             17 (Counter)
    # |                 STORE_FAST               3 (Counter)
    # |                 POP_TOP
    # |  143            LOAD_CONST              15 ('时代')
    # |                 LOAD_FAST_BORROW         3 (Counter)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              28 (<code object <genexpr> at 0x10400bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 143>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_FAST_BORROW         1 (books)
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 BUILD_TUPLE              2
    # |  144            LOAD_CONST              17 ('场景')
    # |                 LOAD_FAST_BORROW         3 (Counter)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              29 (<code object <genexpr> at 0x10400bee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 144>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_FAST_BORROW         1 (books)
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 BUILD_TUPLE              2
    # |  143            BUILD_TUPLE              2
    # |                 GET_ITER
    # |         L4:     FOR_ITER                60 (to L5)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST   69 (label, counter)
    # |  145            LOAD_CONST              30 ('  ')
    # |                 LOAD_ATTR               29 (join + NULL|self)
    # |                 LOAD_CONST              31 (<code object <genexpr> at 0x104060250, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 145>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_FAST_BORROW         5 (counter)
    # |                 LOAD_ATTR               37 (most_common + NULL|self)
    # |                 CALL                     0
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 STORE_FAST               6 (rows)
    # |  146            LOAD_GLOBAL              7 (print + NULL)
    # |                 LOAD_CONST              30 ('  ')
    # |                 LOAD_FAST_BORROW         4 (label)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              32 (': ')
    # |                 LOAD_FAST_BORROW         6 (rows)
    # |                 FORMAT_SIMPLE
    # |                 BUILD_STRING             4
    # |                 CALL                     1
    # |                 POP_TOP
    # |                 JUMP_BACKWARD           62 (to L4)
    # |  143    L5:     END_FOR
    # |                 POP_ITER
    # |  148            LOAD_CONST              33 ('--csv')
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 CONTAINS_OP              0 (in)
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_FALSE      352 (to L15)
    # |                 NOT_TAKEN
    # |  149            LOAD_GLOBAL             11 (Path + NULL)
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 LOAD_ATTR               39 (index + NULL|self)
    # |                 LOAD_CONST              33 ('--csv')
    # |                 CALL                     1
    # |                 LOAD_SMALL_INT           1
    # |                 BINARY_OP                0 (+)
    # |                 BINARY_OP               26 ([])
    # |                 CALL                     1
    # |                 STORE_FAST               7 (out)
    # |  150            LOAD_SMALL_INT           0
    # |                 LOAD_CONST              34 (None)
    # |                 IMPORT_NAME             20 (csv)
    # |                 STORE_FAST               8 (csv)
    # |  151            LOAD_FAST_BORROW         7 (out)
    # |                 LOAD_ATTR               43 (open + NULL|self)
    # |                 LOAD_CONST              35 ('w')
    # |                 LOAD_CONST              36 ('')
    # |                 LOAD_CONST              37 ('utf-8-sig')
    # |                 LOAD_CONST              38 (('newline', 'encoding'))
    # |                 CALL_KW                  3
    # |                 COPY                     1
    # |                 LOAD_SPECIAL             1 (__exit__)
    # |                 SWAP                     2
    # |                 SWAP                     3
    # |                 LOAD_SPECIAL             0 (__enter__)
    # |                 CALL                     0
    # |         L6:     STORE_FAST               9 (fh)
    # |  152            LOAD_FAST_BORROW         8 (csv)
    # |                 LOAD_ATTR               45 (writer + NULL|self)
    # |                 LOAD_FAST_BORROW         9 (fh)
    # |                 CALL                     1
    # |                 STORE_FAST              10 (w)
    # |  153            LOAD_FAST_BORROW        10 (w)
    # |                 LOAD_ATTR               47 (writerow + NULL|self)
    # |                 BUILD_LIST               0
    # |                 LOAD_CONST              42 (('书名', '作者', '字数', '章数', '时代', '场景', '特殊题材'))
    # |                 LIST_EXTEND              1
    # |  154            LOAD_GLOBAL             49 (list + NULL)
    # |                 LOAD_GLOBAL             50 (SIGNALS)
    # |                 CALL                     1
    # |  153            BINARY_OP                0 (+)
    # |                 CALL                     1
    # |                 POP_TOP
    # |  155            LOAD_FAST_BORROW         1 (books)
    # |                 GET_ITER
    # |         L7:     FOR_ITER               166 (to L12)
    # |                 STORE_FAST               2 (b)
    # |  156            LOAD_FAST               10 (w)
    # |                 LOAD_ATTR               47 (writerow + NULL|self)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               16 (name)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               18 (author)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               20 (chars)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               22 (chapters)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               24 (era)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               26 (setting)
    # |  157            LOAD_CONST              24 ('、')
    # |                 LOAD_ATTR               29 (join + NULL|self)
    # |                 LOAD_FAST_BORROW         2 (b)
    # |                 LOAD_ATTR               30 (special)
    # |                 CALL                     1
    # |  156            BUILD_LIST               7
    # |  158            LOAD_GLOBAL             50 (SIGNALS)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR     11 (k)
    # |                 SWAP                     2
    # |         L8:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L9:     FOR_ITER                32 (to L10)
    # |                 STORE_FAST_LOAD_FAST   178 (k, b)
    # |                 LOAD_ATTR               52 (density)
    # |                 LOAD_ATTR               55 (get + NULL|self)
    # |                 LOAD_FAST_BORROW        11 (k)
    # |                 LOAD_SMALL_INT           0
    # |                 CALL                     2
    # |                 LOAD_CONST              39 ('.1f')
    # |                 FORMAT_WITH_SPEC
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           34 (to L9)
    # |        L10:     END_FOR
    # |                 POP_ITER
    # |        L11:     SWAP                     2
    # |                 STORE_FAST              11 (k)
    # |  156            BINARY_OP                0 (+)
    # |                 CALL                     1
    # |                 POP_TOP
    # |                 JUMP_BACKWARD          168 (to L7)
    # |  155   L12:     END_FOR
    # |                 POP_ITER
    # |  151   L13:     LOAD_CONST              34 (None)
    # |                 LOAD_CONST              34 (None)
    # |                 LOAD_CONST              34 (None)
    # |                 CALL                     3
    # |                 POP_TOP
    # |  159   L14:     LOAD_GLOBAL              7 (print + NULL)
    # |                 LOAD_CONST              40 ('\n已写出 ')
    # |                 LOAD_FAST_BORROW         7 (out)
    # |                 FORMAT_SIMPLE
    # |                 BUILD_STRING             2
    # |                 CALL                     1
    # |                 POP_TOP
    # |  160   L15:     LOAD_SMALL_INT           0
    # |                 RETURN_VALUE
    # |   --   L16:     SWAP                     2
    # |                 POP_TOP
    # |  158            SWAP                     2
    # |                 STORE_FAST              11 (k)
    # |                 RERAISE                  0
    # |  151   L17:     PUSH_EXC_INFO
    # |                 WITH_EXCEPT_START
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         2 (to L18)
    # |                 NOT_TAKEN
    # |                 RERAISE                  2
    # |        L18:     POP_TOP
    # |        L19:     POP_EXCEPT
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 POP_TOP
    # |                 JUMP_BACKWARD_NO_INTERRUPT 37 (to L14)
    # |   --   L20:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L6 to L8 -> L17 [2] lasti
    # |   L8 to L11 -> L16 [8]
    # |   L11 to L13 -> L17 [2] lasti
    # |   L16 to L17 -> L17 [2] lasti
    # |   L17 to L19 -> L20 [4] lasti
    # | Disassembly of <code object <genexpr> at 0x10400bbb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 131>:
    # |  131           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L5)
    # |                STORE_FAST_LOAD_FAST    17 (b, b)
    # |                TO_BOOL
    # |        L3:     POP_JUMP_IF_TRUE         3 (to L4)
    # |                NOT_TAKEN
    # |                JUMP_BACKWARD           12 (to L2)
    # |        L4:     LOAD_FAST_BORROW         1 (b)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           18 (to L2)
    # |        L5:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |   --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L3 -> L6 [0] lasti
    # |   L4 to L6 -> L6 [0] lasti
    # | Disassembly of <code object <genexpr> at 0x10400bcc0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 131>:
    # |  131           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST               1 (p)
    # |                LOAD_GLOBAL              1 (profile + NULL)
    # |                LOAD_FAST_BORROW         1 (p)
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
    # | Disassembly of <code object <lambda> at 0x103faaf70, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 132>:
    # | 132           RESUME                   0
    # |               LOAD_FAST_BORROW         0 (b)
    # |               LOAD_ATTR                0 (setting)
    # |               LOAD_CONST               0 ('★跨阶段')
    # |               COMPARE_OP             103 (!=)
    # |               LOAD_FAST_BORROW         0 (b)
    # |               LOAD_ATTR                0 (setting)
    # |               LOAD_FAST_BORROW         0 (b)
    # |               LOAD_ATTR                2 (chars)
    # |               UNARY_NEGATIVE
    # |               BUILD_TUPLE              3
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10400bdd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 143>:
    # |  143           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (b, b)
    # |                LOAD_ATTR                0 (era)
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
    # | Disassembly of <code object <genexpr> at 0x10400bee0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 144>:
    # |  144           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (b, b)
    # |                LOAD_ATTR                0 (setting)
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
    # | Disassembly of <code object <genexpr> at 0x104060250, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/classify_corpus.py", line 145>:
    # |  145           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                14 (to L3)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   18 (k, v)
    # |                LOAD_FAST_BORROW         1 (k)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               0 (' ')
    # |                LOAD_FAST_BORROW         2 (v)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             3
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           16 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
