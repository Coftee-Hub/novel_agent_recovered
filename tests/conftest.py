# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/conftest.py
# 来源   : conftest.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'title',
    ('__annotate__', 4): 'str',
    ('__annotate__', 5): 'target_words',
    ('__annotate__', 6): 'narration',
    ('__annotate__', 7): 'str | None',
    ('__annotate__', 8): 'dialogue',
    ('__annotate__', 9): 'inject',
    ('__annotate__', 10): 'return',
    ('make_chapter', 0): '造一份各项都合规的样章，作为测试基线。\n\n每轮「1 长 + 3 中 + 1 短 + 2 对话」，长/中/短句比例约 20/60/20，\n对话占比约 21% —— 贴近范本实测的 24-33%。\n\n传 narration / dialogue 可定向破坏某一项；传 inject 可插入一个待测段落。\n用 inject 而不是让测试去 replace 夹具内部的句子 —— 那样换句池就会\n把几十个测试一起打断。\n',
    ('make_chapter', 2): '## 第',
    ('make_chapter', 3): '章 ',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'dict',
    ('project_config', 0): 'config',
    ('project_config', 1): 'project.yaml',
    ('project_config', 2): 'utf-8',
    ('sample_state', 2): '伞的重量',
    ('sample_state', 3): 'shen',
    ('sample_state', 4): '沈知微',
    ('sample_state', 5): '微微',
    ('sample_state', 6): '句子短，常用反问收尾',
    ('sample_state', 7): '父母离异时无人问过她的意见，从此认定表达需求等于添麻烦',
    ('sample_state', 8): '绝不主动要求任何人为她改变计划',
    ('sample_state', 9): '大学',
    ('sample_state', 10): '中文系大三',
    ('sample_state', 11): '拿到保研名额',
    ('sample_state', 12): '被人认真问一次想要什么',
    ('sample_state', 13): '与陆时予同在文学社',
    ('sample_state', 15): '你不是本来就要走吗？',
    ('sample_state', 17): 'lu',
    ('sample_state', 18): '陆时予',
    ('sample_state', 19): '陈述句为主，很少用语气词',
    ('sample_state', 20): "长期被当作'可靠的人'，没人问过他累不累",
    ('sample_state', 21): '答应过的事绝不反悔',
    ('sample_state', 22): '建筑系大四',
    ('sample_state', 23): '完成毕业设计',
    ('sample_state', 24): '有人看见他的疲惫',
    ('sample_state', 25): '准备保研',
    ('sample_state', 27): '暧昧',
    ('sample_state', 28): '双方都在等对方先开口',
    ('sample_state', 29): '那把伞到底是谁的',
    ('sample_state', 31): 'd_umbrella',
    ('sample_state', 32): '物件',
    ('sample_state', 33): '陆时予留下的那把伞一直没还',
    ('sample_state', 35): 'd_call',
    ('sample_state', 36): '误会',
    ('sample_state', 37): '她以为那通电话是打给别人的',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def make_chapter(ch, title, target_words, narration, dialogue, inject):
    '造一份各项都合规的样章，作为测试基线。\n\n每轮「1 长 + 3 中 + 1 短 + 2 对话」，长/中/短句比例约 20/60/20，\n对话占比约 21% —— 贴近范本实测的 24-33%。\n\n传 narration / dialogue 可定向破坏某一项；传 inject 可插入一个待测段落。\n用 inject 而不是让测试去 replace 夹具内部的句子 —— 那样换句池就会\n把几十个测试一起打断。\n'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  57            RESUME                   0
    # |  74            LOAD_FAST_BORROW         3 (narration)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        4 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         3 (narration)
    # |                BUILD_LIST               1
    # |                JUMP_FORWARD             5 (to L2)
    # |        L1:     LOAD_GLOBAL              0 (LONG)
    # |        L2:     STORE_FAST               6 (longs)
    # |  75            LOAD_FAST_BORROW         3 (narration)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       11 (to L3)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         3 (narration)
    # |                BUILD_LIST               1
    # |                LOAD_SMALL_INT           3
    # |                BINARY_OP                5 (*)
    # |                JUMP_FORWARD             5 (to L4)
    # |        L3:     LOAD_GLOBAL              2 (MID)
    # |        L4:     STORE_FAST               7 (mids)
    # |  76            LOAD_FAST_BORROW         3 (narration)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        4 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         3 (narration)
    # |                BUILD_LIST               1
    # |                JUMP_FORWARD             5 (to L6)
    # |        L5:     LOAD_GLOBAL              4 (SHORT)
    # |        L6:     STORE_FAST               8 (shorts)
    # |  77            LOAD_FAST_BORROW         4 (dialogue)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       11 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         4 (dialogue)
    # |                BUILD_LIST               1
    # |                LOAD_SMALL_INT           2
    # |                BINARY_OP                5 (*)
    # |                JUMP_FORWARD             5 (to L8)
    # |        L7:     LOAD_GLOBAL              6 (DIA)
    # |        L8:     STORE_FAST               9 (says)
    # |  79            BUILD_LIST               0
    # |                STORE_FAST              10 (paras)
    # |  80            LOAD_SMALL_INT           0
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  188 (n, count)
    # |  81    L9:     LOAD_FAST_BORROW_LOAD_FAST_BORROW 194 (count, target_words)
    # |                COMPARE_OP              18 (bool(<))
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_FALSE      265 (to L10)
    # |                NOT_TAKEN
    # |  82            LOAD_FAST_BORROW_LOAD_FAST_BORROW 107 (longs, n)
    # |                LOAD_GLOBAL              9 (len + NULL)
    # |                LOAD_FAST_BORROW         6 (longs)
    # |                CALL                     1
    # |                BINARY_OP                6 (%)
    # |                BINARY_OP               26 ([])
    # |  83            LOAD_FAST_BORROW_LOAD_FAST_BORROW 123 (mids, n)
    # |                LOAD_SMALL_INT           3
    # |                BINARY_OP                5 (*)
    # |                LOAD_GLOBAL              9 (len + NULL)
    # |                LOAD_FAST_BORROW         7 (mids)
    # |                CALL                     1
    # |                BINARY_OP                6 (%)
    # |                BINARY_OP               26 ([])
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 123 (mids, n)
    # |                LOAD_SMALL_INT           3
    # |                BINARY_OP                5 (*)
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP                0 (+)
    # |                LOAD_GLOBAL              9 (len + NULL)
    # |                LOAD_FAST_BORROW         7 (mids)
    # |                CALL                     1
    # |                BINARY_OP                6 (%)
    # |                BINARY_OP               26 ([])
    # |  84            LOAD_FAST_BORROW_LOAD_FAST_BORROW 123 (mids, n)
    # |                LOAD_SMALL_INT           3
    # |                BINARY_OP                5 (*)
    # |                LOAD_SMALL_INT           2
    # |                BINARY_OP                0 (+)
    # |                LOAD_GLOBAL              9 (len + NULL)
    # |                LOAD_FAST_BORROW         7 (mids)
    # |                CALL                     1
    # |                BINARY_OP                6 (%)
    # |                BINARY_OP               26 ([])
    # |  85            LOAD_FAST_BORROW_LOAD_FAST_BORROW 139 (shorts, n)
    # |                LOAD_GLOBAL              9 (len + NULL)
    # |                LOAD_FAST_BORROW         8 (shorts)
    # |                CALL                     1
    # |                BINARY_OP                6 (%)
    # |                BINARY_OP               26 ([])
    # |  86            LOAD_FAST_BORROW_LOAD_FAST_BORROW 155 (says, n)
    # |                LOAD_SMALL_INT           2
    # |                BINARY_OP                5 (*)
    # |                LOAD_GLOBAL              9 (len + NULL)
    # |                LOAD_FAST_BORROW         9 (says)
    # |                CALL                     1
    # |                BINARY_OP                6 (%)
    # |                BINARY_OP               26 ([])
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 155 (says, n)
    # |                LOAD_SMALL_INT           2
    # |                BINARY_OP                5 (*)
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP                0 (+)
    # |                LOAD_GLOBAL              9 (len + NULL)
    # |                LOAD_FAST_BORROW         9 (says)
    # |                CALL                     1
    # |                BINARY_OP                6 (%)
    # |                BINARY_OP               26 ([])
    # |  82            BUILD_LIST               7
    # |                STORE_FAST              13 (chunk)
    # |  87            LOAD_FAST_BORROW_LOAD_FAST_BORROW 173 (paras, chunk)
    # |                BINARY_OP               13 (+=)
    # |                STORE_FAST              10 (paras)
    # |  88            LOAD_FAST_BORROW        12 (count)
    # |                LOAD_GLOBAL             11 (sum + NULL)
    # |                LOAD_CONST               1 (<code object <genexpr> at 0x10867bcc0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/conftest.py", line 88>)
    # |                MAKE_FUNCTION
    # |                LOAD_FAST_BORROW        13 (chunk)
    # |                GET_ITER
    # |                CALL                     0
    # |                CALL                     1
    # |                BINARY_OP               13 (+=)
    # |                STORE_FAST              12 (count)
    # |  89            LOAD_FAST_BORROW        11 (n)
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               13 (+=)
    # |                STORE_FAST              11 (n)
    # |                EXTENDED_ARG             1
    # |                JUMP_BACKWARD          271 (to L9)
    # |  90   L10:     LOAD_FAST_BORROW         5 (inject)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       19 (to L11)
    # |                NOT_TAKEN
    # |  91            LOAD_FAST_BORROW        10 (paras)
    # |                LOAD_ATTR               13 (insert + NULL|self)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_FAST_BORROW         5 (inject)
    # |                CALL                     2
    # |                POP_TOP
    # |  92   L11:     LOAD_CONST               2 ('## 第')
    # |                LOAD_FAST_BORROW         0 (ch)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               3 ('章 ')
    # |                LOAD_FAST_BORROW         1 (title)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               4 ('\n\n')
    # |                BUILD_STRING             5
    # |                LOAD_CONST               4 ('\n\n')
    # |                LOAD_ATTR               15 (join + NULL|self)
    # |                LOAD_FAST_BORROW        10 (paras)
    # |                CALL                     1
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               5 ('\n')
    # |                BINARY_OP                0 (+)
    # |                RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x10867bcc0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/conftest.py", line 88>:
    # |   88           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST               1 (x)
    # |                LOAD_GLOBAL              1 (len + NULL)
    # |                LOAD_FAST_BORROW         1 (x)
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

def project_config():
    'config'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  95           RESUME                   0
    # |  97           LOAD_GLOBAL              0 (yaml)
    # |               LOAD_ATTR                2 (safe_load)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (ROOT)
    # |               LOAD_CONST               0 ('config')
    # |               BINARY_OP               11 (/)
    # |               LOAD_CONST               1 ('project.yaml')
    # |               BINARY_OP               11 (/)
    # |               LOAD_ATTR                7 (read_text + NULL|self)
    # |               LOAD_CONST               2 ('utf-8')
    # |               CALL                     1
    # |               CALL                     1
    # |               RETURN_VALUE

def sample_state():
    '伞的重量'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 100           RESUME                   0
    # | 102           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('Character', 'CharacterArc', 'EmotionalDebt', 'Relationship', 'StoryState'))
    # |               IMPORT_NAME              0 (novel_agent.state.schema)
    # |               IMPORT_FROM              1 (Character)
    # |               STORE_FAST               0 (Character)
    # |               IMPORT_FROM              2 (CharacterArc)
    # |               STORE_FAST               1 (CharacterArc)
    # |               IMPORT_FROM              3 (EmotionalDebt)
    # |               STORE_FAST               2 (EmotionalDebt)
    # |               IMPORT_FROM              4 (Relationship)
    # |               STORE_FAST               3 (Relationship)
    # |               IMPORT_FROM              5 (StoryState)
    # |               STORE_FAST               4 (StoryState)
    # |               POP_TOP
    # | 106           LOAD_FAST_BORROW         4 (StoryState)
    # |               PUSH_NULL
    # | 107           LOAD_CONST               2 ('伞的重量')
    # | 108           LOAD_SMALL_INT          12
    # | 110           LOAD_FAST_BORROW         0 (Character)
    # |               PUSH_NULL
    # | 111           LOAD_CONST               3 ('shen')
    # |               LOAD_CONST               4 ('沈知微')
    # |               LOAD_CONST               5 ('微微')
    # |               BUILD_LIST               1
    # | 112           BUILD_LIST               0
    # |               LOAD_CONST              39 (('克制', '观察力强', '不肯先开口'))
    # |               LIST_EXTEND              1
    # | 113           LOAD_CONST               6 ('句子短，常用反问收尾')
    # | 114           LOAD_CONST               7 ('父母离异时无人问过她的意见，从此认定表达需求等于添麻烦')
    # | 115           LOAD_CONST               8 ('绝不主动要求任何人为她改变计划')
    # | 116           LOAD_FAST_BORROW         1 (CharacterArc)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 ('大学')
    # |               LOAD_SMALL_INT          20
    # |               LOAD_CONST              10 ('中文系大三')
    # | 117           LOAD_CONST              11 ('拿到保研名额')
    # |               LOAD_CONST              12 ('被人认真问一次想要什么')
    # | 118           LOAD_CONST              13 ('与陆时予同在文学社')
    # | 116           LOAD_CONST              14 (('stage', 'age', 'identity', 'outer_goal', 'inner_want', 'status'))
    # |               CALL_KW                  6
    # |               BUILD_LIST               1
    # | 119           LOAD_CONST              15 ('你不是本来就要走吗？')
    # |               BUILD_LIST               1
    # | 110           LOAD_CONST              16 (('id', 'name', 'aliases', 'core_traits', 'speech_habits', 'core_wound', 'value_line', 'arcs', 'voice_samples'))
    # |               CALL_KW                  9
    # | 121           LOAD_FAST_BORROW         0 (Character)
    # |               PUSH_NULL
    # | 122           LOAD_CONST              17 ('lu')
    # |               LOAD_CONST              18 ('陆时予')
    # | 123           BUILD_LIST               0
    # |               LOAD_CONST              40 (('直接', '迟钝于情绪', '行动快于言语'))
    # |               LIST_EXTEND              1
    # | 124           LOAD_CONST              19 ('陈述句为主，很少用语气词')
    # | 125           LOAD_CONST              20 ("长期被当作'可靠的人'，没人问过他累不累")
    # | 126           LOAD_CONST              21 ('答应过的事绝不反悔')
    # | 127           LOAD_FAST_BORROW         1 (CharacterArc)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 ('大学')
    # |               LOAD_SMALL_INT          21
    # |               LOAD_CONST              22 ('建筑系大四')
    # | 128           LOAD_CONST              23 ('完成毕业设计')
    # |               LOAD_CONST              24 ('有人看见他的疲惫')
    # | 129           LOAD_CONST              25 ('准备保研')
    # | 127           LOAD_CONST              14 (('stage', 'age', 'identity', 'outer_goal', 'inner_want', 'status'))
    # |               CALL_KW                  6
    # |               BUILD_LIST               1
    # | 121           LOAD_CONST              26 (('id', 'name', 'core_traits', 'speech_habits', 'core_wound', 'value_line', 'arcs'))
    # |               CALL_KW                  7
    # | 109           BUILD_LIST               2
    # | 133           LOAD_FAST_BORROW         3 (Relationship)
    # |               PUSH_NULL
    # |               LOAD_CONST               3 ('shen')
    # |               LOAD_CONST              17 ('lu')
    # |               LOAD_CONST              27 ('暧昧')
    # | 134           LOAD_CONST              28 ('双方都在等对方先开口')
    # | 135           LOAD_CONST               3 ('shen')
    # |               LOAD_SMALL_INT          62
    # |               LOAD_CONST              17 ('lu')
    # |               LOAD_SMALL_INT          58
    # |               BUILD_MAP                2
    # |               LOAD_SMALL_INT          11
    # | 136           LOAD_CONST              29 ('那把伞到底是谁的')
    # |               BUILD_LIST               1
    # | 133           LOAD_CONST              30 (('a_id', 'b_id', 'stage', 'tension_source', 'affection', 'last_advanced_ch', 'unresolved'))
    # |               CALL_KW                  7
    # | 132           BUILD_LIST               1
    # | 139           LOAD_FAST_BORROW         2 (EmotionalDebt)
    # |               PUSH_NULL
    # |               LOAD_CONST              31 ('d_umbrella')
    # |               LOAD_CONST              32 ('物件')
    # | 140           LOAD_CONST              33 ('陆时予留下的那把伞一直没还')
    # |               LOAD_SMALL_INT           3
    # |               LOAD_SMALL_INT          30
    # | 139           LOAD_CONST              34 (('id', 'kind', 'desc', 'planted_ch', 'due_by_ch'))
    # |               CALL_KW                  5
    # | 141           LOAD_FAST_BORROW         2 (EmotionalDebt)
    # |               PUSH_NULL
    # |               LOAD_CONST              35 ('d_call')
    # |               LOAD_CONST              36 ('误会')
    # | 142           LOAD_CONST              37 ('她以为那通电话是打给别人的')
    # |               LOAD_SMALL_INT           5
    # |               LOAD_SMALL_INT          10
    # | 141           LOAD_CONST              34 (('id', 'kind', 'desc', 'planted_ch', 'due_by_ch'))
    # |               CALL_KW                  5
    # | 138           BUILD_LIST               2
    # | 106           LOAD_CONST              38 (('title', 'current_chapter', 'characters', 'relationships', 'debts'))
    # |               CALL_KW                  5
    # |               RETURN_VALUE
