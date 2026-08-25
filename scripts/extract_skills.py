# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/scripts/extract_skills.py
# 来源   : extract_skills.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '从范本萃取六个 skills 草稿。\n\n产出写到 skills/_drafts/，**不直接进 skills/** —— 按计划这些要你审阅后\n才算数。审完把文件移过去即可。\n\n    .venv/bin/python scripts/extract_skills.py [skill名...] [--per-book N]\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '从范本萃取六个 skills 草稿。\n\n产出写到 skills/_drafts/，**不直接进 skills/** —— 按计划这些要你审阅后\n才算数。审完把文件移过去即可。\n\n    .venv/bin/python scripts/extract_skills.py [skill名...] [--per-book N]\n',
    4: 'src',
    8: 'corpus',
    9: 'core',
    10: 'skills',
    11: '_drafts',
    12: '_observations',
    13: 'style_voice',
    14: '叙述语感',
    15: '本项目的目标文风是「短句心理型 + 感官比喻」的融合：句长中位 18-26、短句率不低于 14%、心理活动密度高、比喻中等偏多、触觉与温度描写要在。请围绕这个目标组织，冲突的观察按适用场景分开写。',
    16: 'romance_beats',
    17: 'dialogue',
    18: 'character_design',
    19: 'campus_to_career',
    20: '大学→毕业过渡→职场 的阶段跨越',
    21: '重点：时间跳跃怎么交代、人物在新阶段保留什么改变什么、毕业季这个过渡期特有的冲突来源。',
    22: 'cliche_blacklist',
    23: 'dict[str, tuple[list[str] | None, int, str, str]]',
    24: 'PLAN',
    31: '__main__',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'None',
    ('load_env', 0): '.env',
    ('load_env', 2): 'utf-8',
    ('load_env', 3): '#',
    ('load_env', 4): '=',
    ('load_env', 5): '"\'',
    ('__annotate__', 1): 'names',
    ('__annotate__', 2): 'list[str] | None',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[Path]',
    ('books_for', 0): '按书名解析到实际文件。扩展名不写死 —— 语料里 txt 和 epub 混着。',
    ('books_for', 4): 'corpus/core 里找不到《',
    ('books_for', 5): '》（试过 ',
    ('books_for', 6): '、',
    ('books_for', 7): '）',
    ('<genexpr>', 0): '*',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('main', 1): '--',
    ('main', 3): '--per-book',
    ('main', 4): '✗ 未知 skill：',
    ('main', 5): '\n  可选：',
    ('main', 6): 'config',
    ('main', 7): 'models.yaml',
    ('main', 8): 'book',
    ('main', 9): 'run_log.jsonl',
    ('main', 11): '建立抄袭反查索引（核心范本）…',
    ('main', 16): ',',
    ('main', 17): ' 个 n-gram',
    ('main', 20): '\n── ',
    ('main', 21): ' ── ',
    ('main', 22): ' 本 × ',
    ('main', 23): ' 章 = ',
    ('main', 24): ' 次调用',
    ('main', 25): '.json',
    ('main', 26): '--refresh',
    ('main', 28): 'utf-8',
    ('main', 29): 'chapters_read',
    ('main', 30): 'observations',
    ('main', 32): '   复用缓存的 ',
    ('main', 33): ' 条观察（加 --refresh 重新读书）',
    ('main', 35): '   读完 ',
    ('main', 36): '/',
    ('main', 37): ' 章，',
    ('main', 38): ' 条观察，',
    ('main', 39): '.0f',
    ('main', 40): 's',
    ('main', 43): '   ⚠ 观察里混入了原文片段 ',
    ('main', 44): ' 处：',
    ('main', 46): '      「',
    ('main', 47): '」',
    ('main', 48): '   ✗ 没有得到任何观察，跳过合成',
    ('main', 49): '   合成草稿…',
    ('main', 51): '\n   ✗ 合成失败：',
    ('main', 52): '     观察已缓存在 ',
    ('main', 53): '，修好后重跑不必重读书',
    ('main', 55): '.md',
    ('main', 56): '<!-- 草稿：由 scripts/extract_skills.py 从 ',
    ('main', 57): '、',
    ('main', 59): ' 萃取 -->\n<!-- 读了 ',
    ('main', 60): ' 章，得到 ',
    ('main', 61): ' 条观察 -->\n<!-- 审阅后移动到 skills/ 才会生效 -->\n\n',
    ('main', 62): '# ',
    ('main', 65): '→ ',
    ('main', 66): '（',
    ('main', 67): ' 字符）',
    ('main', 68): '   ⚠ 草稿中检出与原文雷同 ',
    ('main', 69): ' 处，需人工核对：',
    ('main', 71): '\n全部完成。草稿在 ',
    ('main', 72): '/，审阅后移到 skills/ 生效。',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def load_env():
    '.env'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  64           RESUME                   0
    # |  65           LOAD_GLOBAL              0 (ROOT)
    # |               LOAD_CONST               0 ('.env')
    # |               BINARY_OP               11 (/)
    # |               STORE_FAST               0 (env)
    # |  66           LOAD_FAST_BORROW         0 (env)
    # |               LOAD_ATTR                3 (exists + NULL|self)
    # |               CALL                     0
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE         3 (to L1)
    # |               NOT_TAKEN
    # |  67           LOAD_CONST               1 (None)
    # |               RETURN_VALUE
    # |  68   L1:     LOAD_FAST_BORROW         0 (env)
    # |               LOAD_ATTR                5 (read_text + NULL|self)
    # |               LOAD_CONST               2 ('utf-8')
    # |               CALL                     1
    # |               LOAD_ATTR                7 (splitlines + NULL|self)
    # |               CALL                     0
    # |               GET_ITER
    # |       L2:     FOR_ITER               158 (to L6)
    # |               STORE_FAST               1 (raw)
    # |  69           LOAD_FAST_BORROW         1 (raw)
    # |               LOAD_ATTR                9 (strip + NULL|self)
    # |               CALL                     0
    # |               STORE_FAST               2 (line)
    # |  70           LOAD_FAST_BORROW         2 (line)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE         3 (to L3)
    # |               NOT_TAKEN
    # |               JUMP_BACKWARD           29 (to L2)
    # |       L3:     LOAD_FAST_BORROW         2 (line)
    # |               LOAD_ATTR               11 (startswith + NULL|self)
    # |               LOAD_CONST               3 ('#')
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE        3 (to L4)
    # |               NOT_TAKEN
    # |               JUMP_BACKWARD           54 (to L2)
    # |       L4:     LOAD_CONST               4 ('=')
    # |               LOAD_FAST_BORROW         2 (line)
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE         3 (to L5)
    # |               NOT_TAKEN
    # |               JUMP_BACKWARD           63 (to L2)
    # |  71   L5:     LOAD_FAST_BORROW         2 (line)
    # |               LOAD_ATTR               13 (partition + NULL|self)
    # |               LOAD_CONST               4 ('=')
    # |               CALL                     1
    # |               UNPACK_SEQUENCE          3
    # |               STORE_FAST_STORE_FAST   52 (key, _)
    # |               STORE_FAST               5 (value)
    # |  72           LOAD_GLOBAL             14 (os)
    # |               LOAD_ATTR               16 (environ)
    # |               LOAD_ATTR               19 (setdefault + NULL|self)
    # |               LOAD_FAST_BORROW         3 (key)
    # |               LOAD_ATTR                9 (strip + NULL|self)
    # |               CALL                     0
    # |               LOAD_FAST_BORROW         5 (value)
    # |               LOAD_ATTR                9 (strip + NULL|self)
    # |               CALL                     0
    # |               LOAD_ATTR                9 (strip + NULL|self)
    # |               LOAD_CONST               5 ('"\'')
    # |               CALL                     1
    # |               CALL                     2
    # |               POP_TOP
    # |               JUMP_BACKWARD          160 (to L2)
    # |  68   L6:     END_FOR
    # |               POP_ITER
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE

def books_for(names):
    '按书名解析到实际文件。扩展名不写死 —— 语料里 txt 和 epub 混着。'
    # ── 函数体（字节码重建见 BODY 段）──
    # |   --           MAKE_CELL                3 (name)
    # |   78           RESUME                   0
    # |   80           LOAD_FAST_BORROW         0 (names)
    # |                POP_JUMP_IF_NOT_NONE    23 (to L1)
    # |                NOT_TAKEN
    # |   81           LOAD_GLOBAL              1 (sorted + NULL)
    # |                LOAD_CONST               2 (<code object <genexpr> at 0x10849e470, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/extract_skills.py", line 81>)
    # |                MAKE_FUNCTION
    # |                LOAD_GLOBAL              2 (SUFFIXES)
    # |                GET_ITER
    # |                CALL                     0
    # |                CALL                     1
    # |                RETURN_VALUE
    # |   82   L1:     BUILD_LIST               0
    # |                STORE_FAST               1 (out)
    # |   83           LOAD_FAST_BORROW         0 (names)
    # |                GET_ITER
    # |        L2:     FOR_ITER                87 (to L4)
    # |                STORE_DEREF              3 (name)
    # |   84           LOAD_GLOBAL              5 (next + NULL)
    # |                LOAD_FAST_BORROW         3 (name)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               3 (<code object <genexpr> at 0x108504a40, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/extract_skills.py", line 84>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_GLOBAL              2 (SUFFIXES)
    # |                GET_ITER
    # |                CALL                     0
    # |   85           LOAD_CONST               1 (None)
    # |   84           CALL                     2
    # |                STORE_FAST               2 (found)
    # |   86           LOAD_FAST_BORROW         2 (found)
    # |                POP_JUMP_IF_NOT_NONE    38 (to L3)
    # |                NOT_TAKEN
    # |   87           LOAD_GLOBAL              7 (FileNotFoundError + NULL)
    # |   88           LOAD_CONST               4 ('corpus/core 里找不到《')
    # |                LOAD_DEREF               3 (name)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               5 ('》（试过 ')
    # |   89           LOAD_CONST               6 ('、')
    # |                LOAD_ATTR                9 (join + NULL|self)
    # |                LOAD_GLOBAL              2 (SUFFIXES)
    # |                CALL                     1
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               7 ('）')
    # |   88           BUILD_STRING             5
    # |   87           CALL                     1
    # |                RAISE_VARARGS            1
    # |   91   L3:     LOAD_FAST_BORROW         1 (out)
    # |                LOAD_ATTR               11 (append + NULL|self)
    # |                LOAD_FAST_BORROW         2 (found)
    # |                CALL                     1
    # |                POP_TOP
    # |                JUMP_BACKWARD           89 (to L2)
    # |   83   L4:     END_FOR
    # |                POP_ITER
    # |   92           LOAD_FAST_BORROW         1 (out)
    # |                RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10849e470, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/extract_skills.py", line 81>:
    # |   81           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                37 (to L5)
    # |                STORE_FAST               1 (s)
    # |                LOAD_GLOBAL              0 (CORE)
    # |                LOAD_ATTR                3 (glob + NULL|self)
    # |                LOAD_CONST               0 ('*')
    # |                LOAD_FAST_BORROW         1 (s)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                GET_ITER
    # |        L3:     FOR_ITER                 6 (to L4)
    # |                STORE_FAST_LOAD_FAST    34 (f, f)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD            8 (to L3)
    # |        L4:     END_FOR
    # |                POP_ITER
    # |                JUMP_BACKWARD           39 (to L2)
    # |        L5:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L6 -> L6 [0] lasti
    # | Disassembly of <code object <genexpr> at 0x108504a40, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/extract_skills.py", line 84>:
    # |   --           COPY_FREE_VARS           1
    # |   84           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                61 (to L5)
    # |                STORE_FAST               1 (s)
    # |   85           LOAD_GLOBAL              0 (CORE)
    # |                LOAD_DEREF               2 (name)
    # |                FORMAT_SIMPLE
    # |                LOAD_FAST_BORROW         1 (s)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR                3 (exists + NULL|self)
    # |                CALL                     0
    # |                TO_BOOL
    # |   84   L3:     POP_JUMP_IF_TRUE         3 (to L4)
    # |                NOT_TAKEN
    # |                JUMP_BACKWARD           42 (to L2)
    # |        L4:     LOAD_GLOBAL              0 (CORE)
    # |                LOAD_DEREF               2 (name)
    # |                FORMAT_SIMPLE
    # |                LOAD_FAST_BORROW         1 (s)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                BINARY_OP               11 (/)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           63 (to L2)
    # |        L5:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               0 (None)
    # |                RETURN_VALUE
    # |   --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L3 -> L6 [0] lasti
    # |   L4 to L6 -> L6 [0] lasti

def main():
    '--'
    # ── 函数体（字节码重建见 BODY 段）──
    # |   95            RESUME                   0
    # |   96            LOAD_GLOBAL              1 (load_env + NULL)
    # |                 CALL                     0
    # |                 POP_TOP
    # |   97            LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 LOAD_CONST               0 (slice(1, None, None))
    # |                 BINARY_OP               26 ([])
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      0 (a)
    # |                 SWAP                     2
    # |         L1:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                29 (to L5)
    # |                 STORE_FAST_LOAD_FAST     0 (a, a)
    # |                 LOAD_ATTR                7 (startswith + NULL|self)
    # |                 LOAD_CONST               1 ('--')
    # |                 CALL                     1
    # |                 TO_BOOL
    # |         L3:     POP_JUMP_IF_FALSE        3 (to L4)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD           27 (to L2)
    # |         L4:     LOAD_FAST_BORROW         0 (a)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           31 (to L2)
    # |         L5:     END_FOR
    # |                 POP_ITER
    # |         L6:     STORE_FAST               1 (args)
    # |                 STORE_FAST               0 (a)
    # |   98            LOAD_FAST                1 (args)
    # |                 COPY                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE        16 (to L7)
    # |                 NOT_TAKEN
    # |                 POP_TOP
    # |                 LOAD_GLOBAL              9 (list + NULL)
    # |                 LOAD_GLOBAL             10 (PLAN)
    # |                 CALL                     1
    # |         L7:     STORE_FAST               2 (wanted)
    # |   99            LOAD_CONST               2 (None)
    # |                 STORE_FAST               3 (per_book_override)
    # |  100            LOAD_CONST               3 ('--per-book')
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_FALSE       69 (to L8)
    # |                 NOT_TAKEN
    # |  101            LOAD_GLOBAL             13 (int + NULL)
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 LOAD_ATTR               15 (index + NULL|self)
    # |                 LOAD_CONST               3 ('--per-book')
    # |                 CALL                     1
    # |                 LOAD_SMALL_INT           1
    # |                 BINARY_OP                0 (+)
    # |                 BINARY_OP               26 ([])
    # |                 CALL                     1
    # |                 STORE_FAST               3 (per_book_override)
    # |  103    L8:     LOAD_FAST_BORROW         2 (wanted)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      4 (w)
    # |                 SWAP                     2
    # |         L9:     BUILD_LIST               0
    # |                 SWAP                     2
    # |        L10:     FOR_ITER                17 (to L13)
    # |                 STORE_FAST_LOAD_FAST    68 (w, w)
    # |                 LOAD_GLOBAL             10 (PLAN)
    # |                 CONTAINS_OP              1 (not in)
    # |        L11:     POP_JUMP_IF_TRUE         3 (to L12)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD           15 (to L10)
    # |        L12:     LOAD_FAST_BORROW         4 (w)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           19 (to L10)
    # |        L13:     END_FOR
    # |                 POP_ITER
    # |        L14:     STORE_FAST               5 (unknown)
    # |                 STORE_FAST               4 (w)
    # |  104            LOAD_FAST_BORROW         5 (unknown)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       33 (to L15)
    # |                 NOT_TAKEN
    # |  105            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST               4 ('✗ 未知 skill：')
    # |                 LOAD_FAST_BORROW         5 (unknown)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST               5 ('\n  可选：')
    # |                 LOAD_GLOBAL              9 (list + NULL)
    # |                 LOAD_GLOBAL             10 (PLAN)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 BUILD_STRING             4
    # |                 CALL                     1
    # |                 POP_TOP
    # |  106            LOAD_SMALL_INT           2
    # |                 RETURN_VALUE
    # |  108   L15:     LOAD_GLOBAL             19 (Router + NULL)
    # |                 LOAD_GLOBAL             20 (ROOT)
    # |                 LOAD_CONST               6 ('config')
    # |                 BINARY_OP               11 (/)
    # |                 LOAD_CONST               7 ('models.yaml')
    # |                 BINARY_OP               11 (/)
    # |                 CALL                     1
    # |                 STORE_FAST               6 (router)
    # |  109            LOAD_GLOBAL             23 (LLMClient + NULL)
    # |                 LOAD_FAST_BORROW         6 (router)
    # |                 LOAD_GLOBAL             20 (ROOT)
    # |                 LOAD_CONST               8 ('book')
    # |                 BINARY_OP               11 (/)
    # |                 LOAD_CONST               9 ('run_log.jsonl')
    # |                 BINARY_OP               11 (/)
    # |                 LOAD_CONST              10 (('log_path',))
    # |                 CALL_KW                  2
    # |                 STORE_FAST               7 (client)
    # |  111            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              11 ('建立抄袭反查索引（核心范本）…')
    # |                 LOAD_CONST              12 (' ')
    # |                 LOAD_CONST              13 (True)
    # |                 LOAD_CONST              14 (('end', 'flush'))
    # |                 CALL_KW                  3
    # |                 POP_TOP
    # |  112            LOAD_GLOBAL             25 (NGramIndex + NULL)
    # |                 LOAD_SMALL_INT          13
    # |                 LOAD_CONST              15 (('n',))
    # |                 CALL_KW                  1
    # |                 STORE_FAST               8 (index)
    # |  113            LOAD_FAST_BORROW         8 (index)
    # |                 LOAD_ATTR               27 (add_path + NULL|self)
    # |                 LOAD_GLOBAL             28 (CORE)
    # |                 CALL                     1
    # |                 POP_TOP
    # |  114            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST_BORROW         8 (index)
    # |                 CALL                     1
    # |                 LOAD_CONST              16 (',')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST              17 (' 个 n-gram')
    # |                 BUILD_STRING             2
    # |                 CALL                     1
    # |                 POP_TOP
    # |  116            LOAD_GLOBAL             33 (Extractor + NULL)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 120 (client, index)
    # |                 LOAD_CONST              18 (('corpus_index',))
    # |                 CALL_KW                  2
    # |                 STORE_FAST               9 (extractor)
    # |  117            LOAD_GLOBAL             34 (DRAFTS)
    # |                 LOAD_ATTR               37 (mkdir + NULL|self)
    # |                 LOAD_CONST              13 (True)
    # |                 LOAD_CONST              13 (True)
    # |                 LOAD_CONST              19 (('parents', 'exist_ok'))
    # |                 CALL_KW                  2
    # |                 POP_TOP
    # |  119            LOAD_FAST_BORROW         2 (wanted)
    # |                 GET_ITER
    # |        L16:     EXTENDED_ARG             3
    # |                 FOR_ITER               917 (to L35)
    # |                 STORE_FAST              10 (skill)
    # |  120            LOAD_GLOBAL             10 (PLAN)
    # |                 LOAD_FAST_BORROW        10 (skill)
    # |                 BINARY_OP               26 ([])
    # |                 UNPACK_SEQUENCE          4
    # |                 STORE_FAST_STORE_FAST  188 (names, per_book)
    # |                 STORE_FAST_STORE_FAST  222 (title, guidance)
    # |  121            LOAD_FAST                3 (per_book_override)
    # |                 COPY                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         3 (to L17)
    # |                 NOT_TAKEN
    # |                 POP_TOP
    # |                 LOAD_FAST               12 (per_book)
    # |        L17:     STORE_FAST              12 (per_book)
    # |  122            LOAD_GLOBAL             39 (books_for + NULL)
    # |                 LOAD_FAST_BORROW        11 (names)
    # |                 CALL                     1
    # |                 STORE_FAST              15 (sources)
    # |  123            LOAD_FAST_BORROW        12 (per_book)
    # |                 LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST_BORROW        15 (sources)
    # |                 CALL                     1
    # |                 BINARY_OP                5 (*)
    # |                 STORE_FAST              16 (total)
    # |  124            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              20 ('\n── ')
    # |                 LOAD_FAST_BORROW        10 (skill)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              21 (' ── ')
    # |                 LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST_BORROW        15 (sources)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              22 (' 本 × ')
    # |                 LOAD_FAST_BORROW        12 (per_book)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              23 (' 章 = ')
    # |                 LOAD_FAST_BORROW        16 (total)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              24 (' 次调用')
    # |                 BUILD_STRING             9
    # |                 CALL                     1
    # |                 POP_TOP
    # |  126            LOAD_GLOBAL             40 (CACHE)
    # |                 LOAD_FAST_BORROW        10 (skill)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              25 ('.json')
    # |                 BUILD_STRING             2
    # |                 BINARY_OP               11 (/)
    # |                 STORE_FAST              17 (cache_file)
    # |  127            LOAD_GLOBAL             42 (time)
    # |                 LOAD_ATTR               42 (time)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 STORE_FAST              18 (started)
    # |  128            LOAD_FAST_BORROW        17 (cache_file)
    # |                 LOAD_ATTR               45 (exists + NULL|self)
    # |                 CALL                     0
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE      148 (to L22)
    # |                 NOT_TAKEN
    # |                 LOAD_CONST              26 ('--refresh')
    # |                 LOAD_GLOBAL              2 (sys)
    # |                 LOAD_ATTR                4 (argv)
    # |                 CONTAINS_OP              1 (not in)
    # |                 POP_JUMP_IF_FALSE      127 (to L22)
    # |                 NOT_TAKEN
    # |  129            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               2 (None)
    # |                 IMPORT_NAME             23 (json)
    # |                 STORE_FAST              19 (json)
    # |  131            LOAD_SMALL_INT           0
    # |                 LOAD_CONST              27 (('ExtractionRun', 'Observation'))
    # |                 IMPORT_NAME             24 (novel_agent.corpus.extract)
    # |                 IMPORT_FROM             25 (ExtractionRun)
    # |                 STORE_FAST              20 (ExtractionRun)
    # |                 IMPORT_FROM             26 (Observation)
    # |                 STORE_FAST              21 (Observation)
    # |                 POP_TOP
    # |  133            LOAD_FAST_BORROW        19 (json)
    # |                 LOAD_ATTR               55 (loads + NULL|self)
    # |                 LOAD_FAST_BORROW        17 (cache_file)
    # |                 LOAD_ATTR               57 (read_text + NULL|self)
    # |                 LOAD_CONST              28 ('utf-8')
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 STORE_FAST              22 (data)
    # |  134            LOAD_FAST               20 (ExtractionRun)
    # |                 PUSH_NULL
    # |                 LOAD_FAST               10 (skill)
    # |                 LOAD_FAST_BORROW        22 (data)
    # |                 LOAD_CONST              29 ('chapters_read')
    # |                 BINARY_OP               26 ([])
    # |  135            LOAD_FAST_BORROW        22 (data)
    # |                 LOAD_CONST              30 ('observations')
    # |                 BINARY_OP               26 ([])
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR     23 (o)
    # |                 SWAP                     2
    # |        L18:     BUILD_LIST               0
    # |                 SWAP                     2
    # |        L19:     FOR_ITER                11 (to L20)
    # |                 STORE_FAST              23 (o)
    # |                 LOAD_FAST_BORROW        21 (Observation)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              73 (())
    # |                 BUILD_MAP                0
    # |                 LOAD_FAST_BORROW        23 (o)
    # |                 DICT_MERGE               1
    # |                 CALL_FUNCTION_EX
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           13 (to L19)
    # |        L20:     END_FOR
    # |                 POP_ITER
    # |        L21:     SWAP                     2
    # |                 STORE_FAST              23 (o)
    # |  134            LOAD_CONST              31 (('skill', 'chapters_read', 'observations'))
    # |                 CALL_KW                  3
    # |                 STORE_FAST              24 (run)
    # |  136            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              32 ('   复用缓存的 ')
    # |                 LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               58 (observations)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              33 (' 条观察（加 --refresh 重新读书）')
    # |                 BUILD_STRING             3
    # |                 CALL                     1
    # |                 POP_TOP
    # |                 JUMP_FORWARD           217 (to L27)
    # |  139   L22:     LOAD_FAST_BORROW         9 (extractor)
    # |                 LOAD_ATTR               61 (run + NULL|self)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 175 (skill, sources)
    # |                 LOAD_FAST_BORROW        12 (per_book)
    # |                 LOAD_SMALL_INT           4
    # |                 LOAD_CONST              34 (('per_book', 'workers'))
    # |                 CALL_KW                  4
    # |                 STORE_FAST              24 (run)
    # |  140            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              35 ('   读完 ')
    # |                 LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               62 (chapters_read)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              36 ('/')
    # |                 LOAD_FAST_BORROW        16 (total)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              37 (' 章，')
    # |  141            LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               58 (observations)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              38 (' 条观察，')
    # |                 LOAD_GLOBAL             42 (time)
    # |                 LOAD_ATTR               42 (time)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 LOAD_FAST_BORROW        18 (started)
    # |                 BINARY_OP               10 (-)
    # |                 LOAD_CONST              39 ('.0f')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST              40 ('s')
    # |  140            BUILD_STRING             9
    # |                 CALL                     1
    # |                 POP_TOP
    # |  142            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               2 (None)
    # |                 IMPORT_NAME             23 (json)
    # |                 STORE_FAST              19 (json)
    # |  144            LOAD_GLOBAL             40 (CACHE)
    # |                 LOAD_ATTR               37 (mkdir + NULL|self)
    # |                 LOAD_CONST              13 (True)
    # |                 LOAD_CONST              13 (True)
    # |                 LOAD_CONST              19 (('parents', 'exist_ok'))
    # |                 CALL_KW                  2
    # |                 POP_TOP
    # |  145            LOAD_FAST               17 (cache_file)
    # |                 LOAD_ATTR               65 (write_text + NULL|self)
    # |                 LOAD_FAST               19 (json)
    # |                 LOAD_ATTR               67 (dumps + NULL|self)
    # |  146            LOAD_CONST              29 ('chapters_read')
    # |                 LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               62 (chapters_read)
    # |  147            LOAD_CONST              30 ('observations')
    # |                 LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               58 (observations)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR     23 (o)
    # |                 SWAP                     2
    # |        L23:     BUILD_LIST               0
    # |                 SWAP                     2
    # |        L24:     FOR_ITER                19 (to L25)
    # |                 STORE_FAST              23 (o)
    # |                 LOAD_FAST_BORROW        23 (o)
    # |                 LOAD_ATTR               69 (model_dump + NULL|self)
    # |                 CALL                     0
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           21 (to L24)
    # |        L25:     END_FOR
    # |                 POP_ITER
    # |        L26:     SWAP                     2
    # |                 STORE_FAST              23 (o)
    # |  146            BUILD_MAP                2
    # |  148            LOAD_CONST              41 (False)
    # |                 LOAD_SMALL_INT           1
    # |  145            LOAD_CONST              42 (('ensure_ascii', 'indent'))
    # |                 CALL_KW                  3
    # |  148            LOAD_CONST              28 ('utf-8')
    # |  145            CALL                     2
    # |                 POP_TOP
    # |  150   L27:     LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               70 (plagiarism_hits)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       76 (to L30)
    # |                 NOT_TAKEN
    # |  151            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              43 ('   ⚠ 观察里混入了原文片段 ')
    # |                 LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               70 (plagiarism_hits)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              44 (' 处：')
    # |                 BUILD_STRING             3
    # |                 CALL                     1
    # |                 POP_TOP
    # |  152            LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               70 (plagiarism_hits)
    # |                 LOAD_CONST              45 (slice(None, 3, None))
    # |                 BINARY_OP               26 ([])
    # |                 GET_ITER
    # |        L28:     FOR_ITER                18 (to L29)
    # |                 STORE_FAST              25 (hit)
    # |  153            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              46 ('      「')
    # |                 LOAD_FAST_BORROW        25 (hit)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              47 ('」')
    # |                 BUILD_STRING             3
    # |                 CALL                     1
    # |                 POP_TOP
    # |                 JUMP_BACKWARD           20 (to L28)
    # |  152   L29:     END_FOR
    # |                 POP_ITER
    # |  155   L30:     LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_ATTR               58 (observations)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE        15 (to L31)
    # |                 NOT_TAKEN
    # |  156            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              48 ('   ✗ 没有得到任何观察，跳过合成')
    # |                 CALL                     1
    # |                 POP_TOP
    # |  157            EXTENDED_ARG             2
    # |                 JUMP_BACKWARD          642 (to L16)
    # |  159   L31:     LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              49 ('   合成草稿…')
    # |                 LOAD_CONST              12 (' ')
    # |                 LOAD_CONST              13 (True)
    # |                 LOAD_CONST              14 (('end', 'flush'))
    # |                 CALL_KW                  3
    # |                 POP_TOP
    # |  160            NOP
    # |  161   L32:     LOAD_GLOBAL             73 (strip_fences + NULL)
    # |                 LOAD_FAST_BORROW         9 (extractor)
    # |                 LOAD_ATTR               75 (synthesize + NULL|self)
    # |                 LOAD_FAST_BORROW        24 (run)
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 222 (title, guidance)
    # |                 LOAD_CONST              50 (('title', 'guidance'))
    # |                 CALL_KW                  3
    # |                 CALL                     1
    # |                 STORE_FAST              26 (draft)
    # |  166   L33:     LOAD_FAST                8 (index)
    # |                 LOAD_ATTR               81 (find_matches + NULL|self)
    # |                 LOAD_FAST               26 (draft)
    # |                 LOAD_SMALL_INT           5
    # |                 LOAD_CONST              54 (('limit',))
    # |                 CALL_KW                  2
    # |                 STORE_FAST              28 (leaks)
    # |  168            LOAD_GLOBAL             34 (DRAFTS)
    # |                 LOAD_FAST               10 (skill)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              55 ('.md')
    # |                 BUILD_STRING             2
    # |                 BINARY_OP               11 (/)
    # |                 STORE_FAST              29 (out)
    # |  170            LOAD_CONST              56 ('<!-- 草稿：由 scripts/extract_skills.py 从 ')
    # |  171            LOAD_CONST              57 ('、')
    # |                 LOAD_ATTR               83 (join + NULL|self)
    # |                 LOAD_CONST              58 (<code object <genexpr> at 0x1084f3bb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/extract_skills.py", line 171>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_FAST               15 (sources)
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              59 (' 萃取 -->\n<!-- 读了 ')
    # |  172            LOAD_FAST               24 (run)
    # |                 LOAD_ATTR               62 (chapters_read)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              60 (' 章，得到 ')
    # |                 LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST               24 (run)
    # |                 LOAD_ATTR               58 (observations)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              61 (' 条观察 -->\n<!-- 审阅后移动到 skills/ 才会生效 -->\n\n')
    # |  170            BUILD_STRING             7
    # |  169            STORE_FAST              30 (header)
    # |  175            LOAD_FAST               29 (out)
    # |                 LOAD_ATTR               65 (write_text + NULL|self)
    # |                 LOAD_FAST               30 (header)
    # |                 LOAD_CONST              62 ('# ')
    # |                 LOAD_FAST               13 (title)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              63 ('\n\n')
    # |                 BUILD_STRING             3
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_FAST               26 (draft)
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              64 ('\n')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              28 ('utf-8')
    # |                 CALL                     2
    # |                 POP_TOP
    # |  176            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              65 ('→ ')
    # |                 LOAD_FAST               29 (out)
    # |                 LOAD_ATTR               79 (relative_to + NULL|self)
    # |                 LOAD_GLOBAL             20 (ROOT)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              66 ('（')
    # |                 LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST               26 (draft)
    # |                 CALL                     1
    # |                 LOAD_CONST              16 (',')
    # |                 FORMAT_WITH_SPEC
    # |                 LOAD_CONST              67 (' 字符）')
    # |                 BUILD_STRING             5
    # |                 CALL                     1
    # |                 POP_TOP
    # |  177            LOAD_FAST               28 (leaks)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE         4 (to L34)
    # |                 NOT_TAKEN
    # |                 EXTENDED_ARG             3
    # |                 JUMP_BACKWARD          884 (to L16)
    # |  178   L34:     LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              68 ('   ⚠ 草稿中检出与原文雷同 ')
    # |                 LOAD_GLOBAL             31 (len + NULL)
    # |                 LOAD_FAST               28 (leaks)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              69 (' 处，需人工核对：')
    # |                 LOAD_FAST               28 (leaks)
    # |                 LOAD_CONST              70 (slice(None, 2, None))
    # |                 BINARY_OP               26 ([])
    # |                 FORMAT_SIMPLE
    # |                 BUILD_STRING             4
    # |                 CALL                     1
    # |                 POP_TOP
    # |                 EXTENDED_ARG             3
    # |                 JUMP_BACKWARD          920 (to L16)
    # |  119   L35:     END_FOR
    # |                 POP_ITER
    # |  180            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              71 ('\n全部完成。草稿在 ')
    # |                 LOAD_GLOBAL             34 (DRAFTS)
    # |                 LOAD_ATTR               79 (relative_to + NULL|self)
    # |                 LOAD_GLOBAL             20 (ROOT)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              72 ('/，审阅后移到 skills/ 生效。')
    # |                 BUILD_STRING             3
    # |                 CALL                     1
    # |                 POP_TOP
    # |  181            LOAD_SMALL_INT           0
    # |                 RETURN_VALUE
    # |   --   L36:     SWAP                     2
    # |                 POP_TOP
    # |   97            SWAP                     2
    # |                 STORE_FAST               0 (a)
    # |                 RERAISE                  0
    # |   --   L37:     SWAP                     2
    # |                 POP_TOP
    # |  103            SWAP                     2
    # |                 STORE_FAST               4 (w)
    # |                 RERAISE                  0
    # |   --   L38:     SWAP                     2
    # |                 POP_TOP
    # |  135            SWAP                     2
    # |                 STORE_FAST              23 (o)
    # |                 RERAISE                  0
    # |   --   L39:     SWAP                     2
    # |                 POP_TOP
    # |  147            SWAP                     2
    # |                 STORE_FAST              23 (o)
    # |                 RERAISE                  0
    # |   --   L40:     PUSH_EXC_INFO
    # |  162            LOAD_GLOBAL             76 (Exception)
    # |                 CHECK_EXC_MATCH
    # |                 POP_JUMP_IF_FALSE       61 (to L44)
    # |                 NOT_TAKEN
    # |                 STORE_FAST              27 (exc)
    # |  163   L41:     LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              51 ('\n   ✗ 合成失败：')
    # |                 LOAD_FAST               27 (exc)
    # |                 FORMAT_SIMPLE
    # |                 BUILD_STRING             2
    # |                 CALL                     1
    # |                 POP_TOP
    # |  164            LOAD_GLOBAL             17 (print + NULL)
    # |                 LOAD_CONST              52 ('     观察已缓存在 ')
    # |                 LOAD_FAST               17 (cache_file)
    # |                 LOAD_ATTR               79 (relative_to + NULL|self)
    # |                 LOAD_GLOBAL             20 (ROOT)
    # |                 CALL                     1
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST              53 ('，修好后重跑不必重读书')
    # |                 BUILD_STRING             3
    # |                 CALL                     1
    # |                 POP_TOP
    # |  165   L42:     POP_EXCEPT
    # |                 LOAD_CONST               2 (None)
    # |                 STORE_FAST              27 (exc)
    # |                 DELETE_FAST             27 (exc)
    # |                 EXTENDED_ARG             4
    # |                 JUMP_BACKWARD         1048 (to L16)
    # |   --   L43:     LOAD_CONST               2 (None)
    # |                 STORE_FAST              27 (exc)
    # |                 DELETE_FAST             27 (exc)
    # |                 RERAISE                  1
    # |  162   L44:     RERAISE                  0
    # |   --   L45:     COPY                     3
    # |                 POP_EXCEPT
    # |                 RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L3 -> L36 [2]
    # |   L4 to L6 -> L36 [2]
    # |   L9 to L11 -> L37 [2]
    # |   L12 to L14 -> L37 [2]
    # |   L18 to L21 -> L38 [7]
    # |   L23 to L26 -> L39 [10]
    # |   L32 to L33 -> L40 [1]
    # |   L40 to L41 -> L45 [2] lasti
    # |   L41 to L42 -> L43 [2] lasti
    # |   L43 to L45 -> L45 [2] lasti
    # | Disassembly of <code object <genexpr> at 0x1084f3bb0, file "/Users/weizihang/Desktop/agent制作/novel_agent/scripts/extract_skills.py", line 171>:
    # |  171           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (p, p)
    # |                LOAD_ATTR                0 (stem)
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
