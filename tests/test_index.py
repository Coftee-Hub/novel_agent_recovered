# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py
# 来源   : test_index.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '语料检索。\n\nBM25 对具象词（地点/物件/节拍名）有效，对抽象情绪无能为力 —— 这是已知\n局限，测试如实反映，不假装它能做到。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '语料检索。\n\nBM25 对具象词（地点/物件/节拍名）有效，对抽象情绪无能为力 —— 这是已知\n局限，测试如实反映，不假装它能做到。\n',
    8: 'TestTokenize',
    10: 'TestSearch',
    12: 'TestRetriever',
    14: 'TestPersistence',
    16: 'TestChunking',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('scene', 0): 's1',
    ('scene', 1): '图书馆',
    ('scene', 2): '周四',
    ('scene', 3): 'a',
    ('scene', 4): '把伞递过去',
    ('scene', 5): '戒备',
    ('scene', 6): '动摇',
    ('scene', 7): '雨中共伞',
    ('index', 0): '甲书',
    ('index', 1): '乙书',
    ('index', 2): '丙书',
    ('index', 3): '雨下得很大，她把伞往他那边偏了偏，两个人挤在图书馆门口的台阶上。雨下得很大，她把伞往他那边偏了偏，两个人挤在图书馆门口的台阶上。雨下得很大，她把伞往他那边偏了偏，两个人挤在图书馆门口的台阶上。雨下得很大，她把伞往他那边偏了偏，两个人挤在图书馆门口的台阶上。',
    ('index', 4): '食堂里人声嘈杂，他端着餐盘找位置，最后坐在窗边那张空桌前。食堂里人声嘈杂，他端着餐盘找位置，最后坐在窗边那张空桌前。食堂里人声嘈杂，他端着餐盘找位置，最后坐在窗边那张空桌前。食堂里人声嘈杂，他端着餐盘找位置，最后坐在窗边那张空桌前。',
    ('index', 5): '他在实验室待到很晚，仪器的指示灯一闪一闪，窗外是空荡的操场。他在实验室待到很晚，仪器的指示灯一闪一闪，窗外是空荡的操场。他在实验室待到很晚，仪器的指示灯一闪一闪，窗外是空荡的操场。他在实验室待到很晚，仪器的指示灯一闪一闪，窗外是空荡的操场。',
    ('index', 6): '又是一场雨。她站在图书馆的屋檐下等，伞在手里攥出了汗。又是一场雨。她站在图书馆的屋檐下等，伞在手里攥出了汗。又是一场雨。她站在图书馆的屋檐下等，伞在手里攥出了汗。又是一场雨。她站在图书馆的屋檐下等，伞在手里攥出了汗。',
    ('TestTokenize', 0): 'TestTokenize',
    ('test_chinese_becomes_bigrams', 0): '下雨',
    ('test_chinese_becomes_bigrams', 1): '下雨天',
    ('test_chinese_becomes_bigrams', 2): 'py1',
    ('test_chinese_becomes_bigrams', 3): 'py3',
    ('test_chinese_becomes_bigrams', 4): 'tokenize',
    ('test_chinese_becomes_bigrams', 5): 'py5',
    ('test_chinese_becomes_bigrams', 6): 'py7',
    ('test_chinese_becomes_bigrams', 7): 'assert %(py9)s',
    ('test_chinese_becomes_bigrams', 8): 'py9',
    ('test_no_bigrams_across_separators', 0): '空格/标点被丢掉后若还两两相邻，会造出语料里不存在的假词：\n查询「雨 伞」曾生成二元组「雨伞」，而语料里只有「雨下」「把伞」。',
    ('test_no_bigrams_across_separators', 1): '雨伞',
    ('test_no_bigrams_across_separators', 2): '雨 伞',
    ('test_no_bigrams_across_separators', 3): 'py1',
    ('test_no_bigrams_across_separators', 4): 'py3',
    ('test_no_bigrams_across_separators', 5): 'tokenize',
    ('test_no_bigrams_across_separators', 6): 'py5',
    ('test_no_bigrams_across_separators', 7): 'py7',
    ('test_no_bigrams_across_separators', 8): 'assert %(py9)s',
    ('test_no_bigrams_across_separators', 9): 'py9',
    ('test_no_bigrams_across_separators', 11): '雨',
    ('test_no_bigrams_across_separators', 12): '伞',
    ('test_no_bigrams_across_separators', 13): 'py0',
    ('test_no_bigrams_across_separators', 14): 'py2',
    ('test_no_bigrams_across_separators', 15): 'py4',
    ('test_single_char_run_kept', 0): '雨',
    ('test_single_char_run_kept', 1): 'py0',
    ('test_single_char_run_kept', 2): 'tokenize',
    ('test_single_char_run_kept', 3): 'py2',
    ('test_single_char_run_kept', 4): 'py4',
    ('test_single_char_run_kept', 5): 'py7',
    ('test_single_char_run_kept', 6): 'assert %(py9)s',
    ('test_single_char_run_kept', 7): 'py9',
    ('test_latin_kept_whole', 0): 'WiFi',
    ('test_latin_kept_whole', 1): 'WiFi 信号',
    ('test_latin_kept_whole', 2): 'py1',
    ('test_latin_kept_whole', 3): 'py3',
    ('test_latin_kept_whole', 4): 'tokenize',
    ('test_latin_kept_whole', 5): 'py5',
    ('test_latin_kept_whole', 6): 'py7',
    ('test_latin_kept_whole', 7): 'assert %(py9)s',
    ('test_latin_kept_whole', 8): 'py9',
    ('test_empty', 0): '！！！',
    ('test_empty', 1): 'py0',
    ('test_empty', 2): 'tokenize',
    ('test_empty', 3): 'py2',
    ('test_empty', 4): 'py4',
    ('test_empty', 5): 'py7',
    ('test_empty', 6): 'assert %(py9)s',
    ('test_empty', 7): 'py9',
    ('TestSearch', 0): 'TestSearch',
    ('test_finds_concrete_scene_match', 0): '具象词是 BM25 的强项。',
    ('test_finds_concrete_scene_match', 1): '雨 伞 图书馆',
    ('test_finds_concrete_scene_match', 3): '甲书',
    ('test_finds_concrete_scene_match', 4): '%(py2)s',
    ('test_finds_concrete_scene_match', 5): 'py2',
    ('test_finds_concrete_scene_match', 6): 'hits',
    ('test_finds_concrete_scene_match', 7): 'py5',
    ('test_finds_concrete_scene_match', 8): 'py7',
    ('test_finds_concrete_scene_match', 9): 'py10',
    ('test_finds_concrete_scene_match', 10): '%(py12)s',
    ('test_finds_concrete_scene_match', 11): 'py12',
    ('test_finds_concrete_scene_match', 12): 'assert %(py15)s',
    ('test_finds_concrete_scene_match', 13): 'py15',
    ('test_irrelevant_query_returns_little', 0): '量子力学 微积分',
    ('test_irrelevant_query_returns_little', 1): 'assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.search\n}(%(py4)s)\n}',
    ('test_irrelevant_query_returns_little', 2): 'py0',
    ('test_irrelevant_query_returns_little', 3): 'index',
    ('test_irrelevant_query_returns_little', 4): 'py2',
    ('test_irrelevant_query_returns_little', 5): 'py4',
    ('test_irrelevant_query_returns_little', 6): 'py6',
    ('test_one_passage_per_book_by_default', 0): '连续多段来自同一处最容易被整段模仿，也会让风格锚偏向单一作者。',
    ('test_one_passage_per_book_by_default', 1): '雨 伞 图书馆',
    ('test_one_passage_per_book_by_default', 3): 'py0',
    ('test_one_passage_per_book_by_default', 4): 'len',
    ('test_one_passage_per_book_by_default', 5): 'py2',
    ('test_one_passage_per_book_by_default', 6): 'py4',
    ('test_one_passage_per_book_by_default', 7): 'py6',
    ('test_one_passage_per_book_by_default', 8): 'py7',
    ('test_one_passage_per_book_by_default', 9): 'hits',
    ('test_one_passage_per_book_by_default', 10): 'py9',
    ('test_one_passage_per_book_by_default', 11): 'assert %(py11)s',
    ('test_one_passage_per_book_by_default', 12): 'py11',
    ('test_per_book_is_configurable', 0): '雨 伞 图书馆',
    ('test_per_book_is_configurable', 3): 'py0',
    ('test_per_book_is_configurable', 4): 'sum',
    ('test_per_book_is_configurable', 5): 'py2',
    ('test_per_book_is_configurable', 6): 'py4',
    ('test_per_book_is_configurable', 7): 'py7',
    ('test_per_book_is_configurable', 8): 'assert %(py9)s',
    ('test_per_book_is_configurable', 9): 'py9',
    ('<genexpr>', 0): '甲书',
    ('test_empty_index_is_safe', 0): '任何内容',
    ('test_empty_index_is_safe', 1): 'py0',
    ('test_empty_index_is_safe', 2): 'PassageIndex',
    ('test_empty_index_is_safe', 3): 'py2',
    ('test_empty_index_is_safe', 4): 'py4',
    ('test_empty_index_is_safe', 5): 'py6',
    ('test_empty_index_is_safe', 6): 'py8',
    ('test_empty_index_is_safe', 7): 'py11',
    ('test_empty_index_is_safe', 8): 'assert %(py13)s',
    ('test_empty_index_is_safe', 9): 'py13',
    ('TestRetriever', 0): 'TestRetriever',
    ('test_query_includes_concrete_descriptors', 0): '雨中共伞',
    ('test_query_includes_concrete_descriptors', 1): '图书馆',
    ('test_query_includes_concrete_descriptors', 2): 'py3',
    ('test_query_includes_concrete_descriptors', 3): 'py5',
    ('test_query_includes_concrete_descriptors', 4): 'q',
    ('test_query_includes_concrete_descriptors', 5): '%(py7)s',
    ('test_query_includes_concrete_descriptors', 6): 'py7',
    ('test_query_includes_concrete_descriptors', 7): 'py10',
    ('test_query_includes_concrete_descriptors', 8): 'py12',
    ('test_query_includes_concrete_descriptors', 9): '%(py14)s',
    ('test_query_includes_concrete_descriptors', 10): 'py14',
    ('test_query_includes_concrete_descriptors', 11): 'assert %(py17)s',
    ('test_query_includes_concrete_descriptors', 12): 'py17',
    ('test_snippets_returned', 2): 'assert %(py12)s\n{%(py12)s = %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py0)s(%(py1)s, limit=%(py3)s)\n}.snippets\n}(%(py10)s\n{%(py10)s = %(py8)s()\n})\n}',
    ('test_snippets_returned', 3): 'py0',
    ('test_snippets_returned', 4): 'SceneRetriever',
    ('test_snippets_returned', 5): 'py1',
    ('test_snippets_returned', 6): 'index',
    ('test_snippets_returned', 7): 'py3',
    ('test_snippets_returned', 8): 'py5',
    ('test_snippets_returned', 9): 'py7',
    ('test_snippets_returned', 10): 'py8',
    ('test_snippets_returned', 11): 'scene',
    ('test_snippets_returned', 12): 'py10',
    ('test_snippets_returned', 13): 'py12',
    ('test_empty_index_yields_no_snippets', 0): '==',
    ('test_empty_index_yields_no_snippets', 1): 'py0',
    ('test_empty_index_yields_no_snippets', 2): 'SceneRetriever',
    ('test_empty_index_yields_no_snippets', 3): 'py1',
    ('test_empty_index_yields_no_snippets', 4): 'PassageIndex',
    ('test_empty_index_yields_no_snippets', 5): 'py3',
    ('test_empty_index_yields_no_snippets', 6): 'py5',
    ('test_empty_index_yields_no_snippets', 7): 'py7',
    ('test_empty_index_yields_no_snippets', 8): 'py8',
    ('test_empty_index_yields_no_snippets', 9): 'scene',
    ('test_empty_index_yields_no_snippets', 10): 'py10',
    ('test_empty_index_yields_no_snippets', 11): 'py12',
    ('test_empty_index_yields_no_snippets', 12): 'py15',
    ('test_empty_index_yields_no_snippets', 13): 'assert %(py17)s',
    ('test_empty_index_yields_no_snippets', 14): 'py17',
    ('test_abstract_emotion_alone_finds_nothing', 0): '如实记录局限：情绪词在正文里几乎不字面出现，词法检索抓不到。\n换成向量检索后这条应当改为能匹配。',
    ('test_abstract_emotion_alone_finds_nothing', 1): '戒备 动摇 不肯承认',
    ('test_abstract_emotion_alone_finds_nothing', 2): 'assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.search\n}(%(py4)s)\n}',
    ('test_abstract_emotion_alone_finds_nothing', 3): 'py0',
    ('test_abstract_emotion_alone_finds_nothing', 4): 'index',
    ('test_abstract_emotion_alone_finds_nothing', 5): 'py2',
    ('test_abstract_emotion_alone_finds_nothing', 6): 'py4',
    ('test_abstract_emotion_alone_finds_nothing', 7): 'py6',
    ('TestPersistence', 0): 'TestPersistence',
    ('test_roundtrip', 0): 'idx.json',
    ('test_roundtrip', 1): 'py0',
    ('test_roundtrip', 2): 'len',
    ('test_roundtrip', 3): 'py1',
    ('test_roundtrip', 4): 'loaded',
    ('test_roundtrip', 5): 'py3',
    ('test_roundtrip', 6): 'py5',
    ('test_roundtrip', 7): 'py6',
    ('test_roundtrip', 8): 'index',
    ('test_roundtrip', 9): 'py8',
    ('test_roundtrip', 10): 'assert %(py10)s',
    ('test_roundtrip', 11): 'py10',
    ('test_roundtrip', 13): '雨中共伞 图书馆',
    ('test_roundtrip', 15): '甲书',
    ('test_roundtrip', 16): 'assert %(py8)s',
    ('TestChunking', 0): 'TestChunking',
    ('test_splits_book_into_passages', 2): '书.txt',
    ('test_splits_book_into_passages', 5): 'utf-8',
    ('test_splits_book_into_passages', 6): 'py0',
    ('test_splits_book_into_passages', 7): 'idx',
    ('test_splits_book_into_passages', 8): 'py2',
    ('test_splits_book_into_passages', 9): 'py3',
    ('test_splits_book_into_passages', 10): 'f',
    ('test_splits_book_into_passages', 11): 'py5',
    ('test_splits_book_into_passages', 12): 'py8',
    ('test_splits_book_into_passages', 13): 'assert %(py10)s',
    ('test_splits_book_into_passages', 14): 'py10',
    ('test_splits_book_into_passages', 17): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_splits_book_into_passages', 18): 'all',
    ('test_splits_book_into_passages', 19): 'py4',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def scene(**kw):
    's1'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  15           RESUME                   0
    # |  16           LOAD_GLOBAL              1 (dict + NULL)
    # |               LOAD_CONST               0 ('s1')
    # |               LOAD_CONST               1 ('图书馆')
    # |               LOAD_CONST               2 ('周四')
    # |               LOAD_CONST               3 ('a')
    # |               BUILD_LIST               1
    # |  17           LOAD_CONST               4 ('把伞递过去')
    # |               LOAD_CONST               5 ('戒备')
    # |               LOAD_CONST               6 ('动摇')
    # |  18           LOAD_CONST               7 ('雨中共伞')
    # |               LOAD_CONST               8 (800)
    # |  16           LOAD_CONST               9 (('id', 'where', 'when', 'present', 'goal', 'entry_emotion', 'exit_emotion', 'beat_type', 'target_words'))
    # |               CALL_KW                  9
    # |               STORE_FAST               1 (base)
    # |  19           LOAD_FAST_BORROW         1 (base)
    # |               LOAD_ATTR                3 (update + NULL|self)
    # |               LOAD_FAST_BORROW         0 (kw)
    # |               CALL                     1
    # |               POP_TOP
    # |  20           LOAD_GLOBAL              5 (SceneSpec + NULL)
    # |               LOAD_CONST              10 (())
    # |               BUILD_MAP                0
    # |               LOAD_FAST_BORROW         1 (base)
    # |               DICT_MERGE               1
    # |               CALL_FUNCTION_EX
    # |               RETURN_VALUE

def index():
    '甲书'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  23           RESUME                   0
    # |  25           LOAD_GLOBAL              1 (PassageIndex + NULL)
    # |  26           LOAD_GLOBAL              3 (Passage + NULL)
    # |               LOAD_CONST               0 ('甲书')
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               3 ('雨下得很大，她把伞往他那边偏了偏，两个人挤在图书馆门口的台阶上。雨下得很大，她把伞往他那边偏了偏，两个人挤在图书馆门口的台阶上。雨下得很大，她把伞往他那边偏了偏，两个人挤在图书馆门口的台阶上。雨下得很大，她把伞往他那边偏了偏，两个人挤在图书馆门口的台阶上。')
    # |               CALL                     3
    # |  27           LOAD_GLOBAL              3 (Passage + NULL)
    # |               LOAD_CONST               1 ('乙书')
    # |               LOAD_SMALL_INT           3
    # |               LOAD_CONST               4 ('食堂里人声嘈杂，他端着餐盘找位置，最后坐在窗边那张空桌前。食堂里人声嘈杂，他端着餐盘找位置，最后坐在窗边那张空桌前。食堂里人声嘈杂，他端着餐盘找位置，最后坐在窗边那张空桌前。食堂里人声嘈杂，他端着餐盘找位置，最后坐在窗边那张空桌前。')
    # |               CALL                     3
    # |  28           LOAD_GLOBAL              3 (Passage + NULL)
    # |               LOAD_CONST               2 ('丙书')
    # |               LOAD_SMALL_INT           5
    # |               LOAD_CONST               5 ('他在实验室待到很晚，仪器的指示灯一闪一闪，窗外是空荡的操场。他在实验室待到很晚，仪器的指示灯一闪一闪，窗外是空荡的操场。他在实验室待到很晚，仪器的指示灯一闪一闪，窗外是空荡的操场。他在实验室待到很晚，仪器的指示灯一闪一闪，窗外是空荡的操场。')
    # |               CALL                     3
    # |  29           LOAD_GLOBAL              3 (Passage + NULL)
    # |               LOAD_CONST               0 ('甲书')
    # |               LOAD_SMALL_INT           9
    # |               LOAD_CONST               6 ('又是一场雨。她站在图书馆的屋檐下等，伞在手里攥出了汗。又是一场雨。她站在图书馆的屋檐下等，伞在手里攥出了汗。又是一场雨。她站在图书馆的屋檐下等，伞在手里攥出了汗。又是一场雨。她站在图书馆的屋檐下等，伞在手里攥出了汗。')
    # |               CALL                     3
    # |  25           BUILD_LIST               4
    # |               CALL                     1
    # |               RETURN_VALUE

class TestTokenize:
    'TestTokenize'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  33           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestTokenize')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          33
    # |               STORE_NAME               3 (__firstlineno__)
    # |  34           LOAD_CONST               1 (<code object test_chinese_becomes_bigrams at 0x7c9ce73300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 34>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_chinese_becomes_bigrams)
    # |  37           LOAD_CONST               2 (<code object test_no_bigrams_across_separators at 0x7c9d1d6300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 37>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_no_bigrams_across_separators)
    # |  43           LOAD_CONST               3 (<code object test_single_char_run_kept at 0x7c9ce73600, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 43>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_single_char_run_kept)
    # |  46           LOAD_CONST               4 (<code object test_latin_kept_whole at 0x7c9ce73900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 46>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_latin_kept_whole)
    # |  49           LOAD_CONST               5 (<code object test_empty at 0x7c9ce73c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 49>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_empty)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_chinese_becomes_bigrams at 0x7c9ce73300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 34>:
    # |  34           RESUME                   0
    # |  35           LOAD_CONST               0 ('下雨')
    # |               STORE_FAST               1 (@py_assert0)
    # |               LOAD_CONST               1 ('下雨天')
    # |               STORE_FAST               2 (@py_assert4)
    # |               LOAD_GLOBAL              1 (tokenize + NULL)
    # |               LOAD_FAST_BORROW         2 (@py_assert4)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    49 (@py_assert6, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       229 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('in',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py3)s(%(py5)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (@py_assert0, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_CONST               4 ('tokenize')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('tokenize')
    # |       L3:     LOAD_CONST               5 ('py5')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py7')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format8)
    # |               LOAD_CONST               7 ('assert %(py9)s')
    # |               LOAD_CONST               8 ('py9')
    # |               LOAD_FAST_BORROW         5 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format10)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   35 (@py_assert4, @py_assert6)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_no_bigrams_across_separators at 0x7c9d1d6300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 37>:
    # |  37           RESUME                   0
    # |  40           LOAD_CONST               1 ('雨伞')
    # |               STORE_FAST               1 (@py_assert0)
    # |               LOAD_CONST               2 ('雨 伞')
    # |               STORE_FAST               2 (@py_assert4)
    # |               LOAD_GLOBAL              1 (tokenize + NULL)
    # |               LOAD_FAST_BORROW         2 (@py_assert4)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    49 (@py_assert6, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CONTAINS_OP              1 (not in)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       229 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('not in',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py1)s not in %(py7)s\n{%(py7)s = %(py3)s(%(py5)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (@py_assert0, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py3')
    # |               LOAD_CONST               5 ('tokenize')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('tokenize')
    # |       L3:     LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py7')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format8)
    # |               LOAD_CONST               8 ('assert %(py9)s')
    # |               LOAD_CONST               9 ('py9')
    # |               LOAD_FAST_BORROW         5 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format10)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   35 (@py_assert4, @py_assert6)
    # |  41           LOAD_CONST               2 ('雨 伞')
    # |               STORE_FAST               7 (@py_assert1)
    # |               LOAD_GLOBAL              1 (tokenize + NULL)
    # |               LOAD_FAST_BORROW         7 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST               8 (@py_assert3)
    # |               LOAD_CONST              11 ('雨')
    # |               LOAD_CONST              12 ('伞')
    # |               BUILD_LIST               2
    # |               STORE_FAST_LOAD_FAST    56 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       229 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              18 (('==',))
    # |               LOAD_FAST_BORROW         9 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              19 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 131 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              13 ('py0')
    # |               LOAD_CONST               5 ('tokenize')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               5 ('tokenize')
    # |       L7:     LOAD_CONST              14 ('py2')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              15 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py7')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format8)
    # |               LOAD_CONST               8 ('assert %(py9)s')
    # |               LOAD_CONST               9 ('py9')
    # |               LOAD_FAST_BORROW         5 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format10)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  147 (@py_assert5, @py_assert6)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_single_char_run_kept at 0x7c9ce73600, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 43>:
    # |  43           RESUME                   0
    # |  44           LOAD_CONST               0 ('雨')
    # |               STORE_FAST               1 (@py_assert1)
    # |               LOAD_GLOBAL              1 (tokenize + NULL)
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST               2 (@py_assert3)
    # |               LOAD_CONST               0 ('雨')
    # |               BUILD_LIST               1
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       229 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              10 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('tokenize')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('tokenize')
    # |       L3:     LOAD_CONST               3 ('py2')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py7')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format8)
    # |               LOAD_CONST               6 ('assert %(py9)s')
    # |               LOAD_CONST               7 ('py9')
    # |               LOAD_FAST_BORROW         5 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format10)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert5, @py_assert6)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_latin_kept_whole at 0x7c9ce73900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 46>:
    # |  46           RESUME                   0
    # |  47           LOAD_CONST               0 ('WiFi')
    # |               STORE_FAST               1 (@py_assert0)
    # |               LOAD_CONST               1 ('WiFi 信号')
    # |               STORE_FAST               2 (@py_assert4)
    # |               LOAD_GLOBAL              1 (tokenize + NULL)
    # |               LOAD_FAST_BORROW         2 (@py_assert4)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    49 (@py_assert6, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       229 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              10 (('in',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py3)s(%(py5)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (@py_assert0, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py1')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py3')
    # |               LOAD_CONST               4 ('tokenize')
    # |               LOAD_GLOBAL              8 (@py_builtins)
    # |               LOAD_ATTR               10 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('tokenize')
    # |       L3:     LOAD_CONST               5 ('py5')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py7')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                6 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format8)
    # |               LOAD_CONST               7 ('assert %(py9)s')
    # |               LOAD_CONST               8 ('py9')
    # |               LOAD_FAST_BORROW         5 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format10)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   35 (@py_assert4, @py_assert6)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_empty at 0x7c9ce73c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 49>:
    # |  49           RESUME                   0
    # |  50           LOAD_CONST               0 ('！！！')
    # |               STORE_FAST               1 (@py_assert1)
    # |               LOAD_GLOBAL              1 (tokenize + NULL)
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST               2 (@py_assert3)
    # |               BUILD_LIST               0
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       229 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR                4 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               9 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              10 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('tokenize')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (tokenize)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('tokenize')
    # |       L3:     LOAD_CONST               3 ('py2')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py4')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py7')
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format8)
    # |               LOAD_CONST               6 ('assert %(py9)s')
    # |               LOAD_CONST               7 ('py9')
    # |               LOAD_FAST_BORROW         5 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format10)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               1 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert5, @py_assert6)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE

    def test_chinese_becomes_bigrams(self):
        '下雨'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  34           RESUME                   0
        # |  35           LOAD_CONST               0 ('下雨')
        # |               STORE_FAST               1 (@py_assert0)
        # |               LOAD_CONST               1 ('下雨天')
        # |               STORE_FAST               2 (@py_assert4)
        # |               LOAD_GLOBAL              1 (tokenize + NULL)
        # |               LOAD_FAST_BORROW         2 (@py_assert4)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    49 (@py_assert6, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       229 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('in',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py3)s(%(py5)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (@py_assert0, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_CONST               4 ('tokenize')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('tokenize')
        # |       L3:     LOAD_CONST               5 ('py5')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py7')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format8)
        # |               LOAD_CONST               7 ('assert %(py9)s')
        # |               LOAD_CONST               8 ('py9')
        # |               LOAD_FAST_BORROW         5 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format10)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   35 (@py_assert4, @py_assert6)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_no_bigrams_across_separators(self):
        '空格/标点被丢掉后若还两两相邻，会造出语料里不存在的假词：\n查询「雨 伞」曾生成二元组「雨伞」，而语料里只有「雨下」「把伞」。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  37           RESUME                   0
        # |  40           LOAD_CONST               1 ('雨伞')
        # |               STORE_FAST               1 (@py_assert0)
        # |               LOAD_CONST               2 ('雨 伞')
        # |               STORE_FAST               2 (@py_assert4)
        # |               LOAD_GLOBAL              1 (tokenize + NULL)
        # |               LOAD_FAST_BORROW         2 (@py_assert4)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    49 (@py_assert6, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CONTAINS_OP              1 (not in)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       229 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('not in',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py1)s not in %(py7)s\n{%(py7)s = %(py3)s(%(py5)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (@py_assert0, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py3')
        # |               LOAD_CONST               5 ('tokenize')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('tokenize')
        # |       L3:     LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py7')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format8)
        # |               LOAD_CONST               8 ('assert %(py9)s')
        # |               LOAD_CONST               9 ('py9')
        # |               LOAD_FAST_BORROW         5 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format10)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   35 (@py_assert4, @py_assert6)
        # |  41           LOAD_CONST               2 ('雨 伞')
        # |               STORE_FAST               7 (@py_assert1)
        # |               LOAD_GLOBAL              1 (tokenize + NULL)
        # |               LOAD_FAST_BORROW         7 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST               8 (@py_assert3)
        # |               LOAD_CONST              11 ('雨')
        # |               LOAD_CONST              12 ('伞')
        # |               BUILD_LIST               2
        # |               STORE_FAST_LOAD_FAST    56 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       229 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              18 (('==',))
        # |               LOAD_FAST_BORROW         9 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              19 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 131 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              13 ('py0')
        # |               LOAD_CONST               5 ('tokenize')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               5 ('tokenize')
        # |       L7:     LOAD_CONST              14 ('py2')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              15 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py7')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format8)
        # |               LOAD_CONST               8 ('assert %(py9)s')
        # |               LOAD_CONST               9 ('py9')
        # |               LOAD_FAST_BORROW         5 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format10)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  147 (@py_assert5, @py_assert6)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE

    def test_single_char_run_kept(self):
        '雨'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  43           RESUME                   0
        # |  44           LOAD_CONST               0 ('雨')
        # |               STORE_FAST               1 (@py_assert1)
        # |               LOAD_GLOBAL              1 (tokenize + NULL)
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST               2 (@py_assert3)
        # |               LOAD_CONST               0 ('雨')
        # |               BUILD_LIST               1
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       229 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              10 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('tokenize')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('tokenize')
        # |       L3:     LOAD_CONST               3 ('py2')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py7')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format8)
        # |               LOAD_CONST               6 ('assert %(py9)s')
        # |               LOAD_CONST               7 ('py9')
        # |               LOAD_FAST_BORROW         5 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format10)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert5, @py_assert6)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE

    def test_latin_kept_whole(self):
        'WiFi'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  46           RESUME                   0
        # |  47           LOAD_CONST               0 ('WiFi')
        # |               STORE_FAST               1 (@py_assert0)
        # |               LOAD_CONST               1 ('WiFi 信号')
        # |               STORE_FAST               2 (@py_assert4)
        # |               LOAD_GLOBAL              1 (tokenize + NULL)
        # |               LOAD_FAST_BORROW         2 (@py_assert4)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    49 (@py_assert6, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       229 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              10 (('in',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              11 (('%(py1)s in %(py7)s\n{%(py7)s = %(py3)s(%(py5)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (@py_assert0, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py1')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py3')
        # |               LOAD_CONST               4 ('tokenize')
        # |               LOAD_GLOBAL              8 (@py_builtins)
        # |               LOAD_ATTR               10 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('tokenize')
        # |       L3:     LOAD_CONST               5 ('py5')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py7')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                6 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format8)
        # |               LOAD_CONST               7 ('assert %(py9)s')
        # |               LOAD_CONST               8 ('py9')
        # |               LOAD_FAST_BORROW         5 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format10)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   35 (@py_assert4, @py_assert6)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE

    def test_empty(self):
        '！！！'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  49           RESUME                   0
        # |  50           LOAD_CONST               0 ('！！！')
        # |               STORE_FAST               1 (@py_assert1)
        # |               LOAD_GLOBAL              1 (tokenize + NULL)
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST               2 (@py_assert3)
        # |               BUILD_LIST               0
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       229 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR                4 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               9 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              10 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('tokenize')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (tokenize)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('tokenize')
        # |       L3:     LOAD_CONST               3 ('py2')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py4')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py7')
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format8)
        # |               LOAD_CONST               6 ('assert %(py9)s')
        # |               LOAD_CONST               7 ('py9')
        # |               LOAD_FAST_BORROW         5 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format10)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               1 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert5, @py_assert6)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE


class TestSearch:
    'TestSearch'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  53           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestSearch')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          53
    # |               STORE_NAME               3 (__firstlineno__)
    # |  54           LOAD_CONST               1 (<code object test_finds_concrete_scene_match at 0x7c9ce75c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 54>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_finds_concrete_scene_match)
    # |  59           LOAD_CONST               2 (<code object test_irrelevant_query_returns_little at 0x7c9ce57900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 59>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_irrelevant_query_returns_little)
    # |  62           LOAD_CONST               3 (<code object test_one_passage_per_book_by_default at 0x7c9d1d6800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 62>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_one_passage_per_book_by_default)
    # |  67           LOAD_CONST               4 (<code object test_per_book_is_configurable at 0x7c9ce68700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 67>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_per_book_is_configurable)
    # |  71           LOAD_CONST               5 (<code object test_empty_index_is_safe at 0x7c9ce68a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 71>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_empty_index_is_safe)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_finds_concrete_scene_match at 0x7c9ce75c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 54>:
    # |  54           RESUME                   0
    # |  56           LOAD_FAST_BORROW         1 (index)
    # |               LOAD_ATTR                1 (search + NULL|self)
    # |               LOAD_CONST               1 ('雨 伞 图书馆')
    # |               LOAD_SMALL_INT           2
    # |               LOAD_CONST               2 (('limit',))
    # |               CALL_KW                  2
    # |               STORE_FAST               2 (hits)
    # |  57           BUILD_LIST               0
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert1, hits)
    # |               STORE_FAST_LOAD_FAST    66 (@py_assert0, hits)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       35 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_FAST_BORROW         2 (hits)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               LOAD_SMALL_INT           1
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
    # |               LOAD_ATTR                2 (book)
    # |               STORE_FAST               6 (@py_assert6)
    # |               LOAD_CONST               3 ('甲书')
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert9, @py_assert6)
    # |               LOAD_FAST_BORROW         7 (@py_assert9)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert8, @py_assert8)
    # |               STORE_FAST               4 (@py_assert0)
    # |       L1:     LOAD_FAST_BORROW         4 (@py_assert0)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       312 (to L6)
    # |               NOT_TAKEN
    # |               LOAD_CONST               4 ('%(py2)s')
    # |               LOAD_CONST               5 ('py2')
    # |               LOAD_CONST               6 ('hits')
    # |               LOAD_GLOBAL              4 (@py_builtins)
    # |               LOAD_ATTR                6 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (hits)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (hits)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               6 ('hits')
    # |       L4:     BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   147 (@py_format3, @py_assert1)
    # |               LOAD_ATTR               15 (append + NULL|self)
    # |               LOAD_FAST_BORROW         9 (@py_format3)
    # |               CALL                     1
    # |               POP_TOP
    # |               LOAD_FAST_BORROW         2 (hits)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE      129 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('==',))
    # |               LOAD_FAST_CHECK          8 (@py_assert8)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py7)s\n{%(py7)s = %(py5)s.book\n} == %(py10)s',))
    # |               LOAD_FAST_CHECK          6 (@py_assert6)
    # |               LOAD_FAST_CHECK          7 (@py_assert9)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py5')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_CHECK          5 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert6)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py10')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert9)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format11)
    # |               LOAD_CONST              10 ('%(py12)s')
    # |               LOAD_CONST              11 ('py12')
    # |               LOAD_FAST_BORROW        10 (@py_format11)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   179 (@py_format13, @py_assert1)
    # |               LOAD_ATTR               15 (append + NULL|self)
    # |               LOAD_FAST_BORROW        11 (@py_format13)
    # |               CALL                     1
    # |               POP_TOP
    # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_boolop)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BUILD_MAP                0
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              12 (@py_format14)
    # |               LOAD_CONST              12 ('assert %(py15)s')
    # |               LOAD_CONST              13 ('py15')
    # |               LOAD_FAST_BORROW        12 (@py_format14)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format16)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        13 (@py_format16)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L6:     LOAD_CONST              14 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert6)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert8, @py_assert9)
    # |               LOAD_CONST              14 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_irrelevant_query_returns_little at 0x7c9ce57900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 59>:
    # |  59           RESUME                   0
    # |  60           LOAD_FAST_BORROW         1 (index)
    # |               LOAD_ATTR                0 (search)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               0 ('量子力学 微积分')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       185 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.search\n}(%(py4)s)\n}')
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('index')
    # |               LOAD_GLOBAL              2 (@py_builtins)
    # |               LOAD_ATTR                4 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (index)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (index)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('index')
    # |       L3:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py6')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert5, @py_assert7)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_one_passage_per_book_by_default at 0x7c9d1d6800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 62>:
    # |   62            RESUME                   0
    # |   64            LOAD_FAST_BORROW         1 (index)
    # |                 LOAD_ATTR                1 (search + NULL|self)
    # |                 LOAD_CONST               1 ('雨 伞 图书馆')
    # |                 LOAD_SMALL_INT           4
    # |                 LOAD_CONST               2 (('limit',))
    # |                 CALL_KW                  2
    # |                 STORE_FAST               2 (hits)
    # |   65            LOAD_FAST_BORROW         2 (hits)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      3 (_)
    # |                 LOAD_FAST_AND_CLEAR      4 (p)
    # |                 SWAP                     3
    # |         L1:     BUILD_SET                0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                17 (to L3)
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST   52 (_, p)
    # |                 LOAD_FAST_BORROW         4 (p)
    # |                 LOAD_ATTR                2 (book)
    # |                 SET_ADD                  2
    # |                 JUMP_BACKWARD           19 (to L2)
    # |         L3:     END_FOR
    # |                 POP_ITER
    # |         L4:     STORE_FAST               5 (@py_assert1)
    # |                 STORE_FAST               3 (_)
    # |                 STORE_FAST               4 (p)
    # |                 LOAD_GLOBAL              5 (len + NULL)
    # |                 LOAD_FAST_BORROW         5 (@py_assert1)
    # |                 CALL                     1
    # |                 STORE_FAST               6 (@py_assert3)
    # |                 LOAD_GLOBAL              5 (len + NULL)
    # |                 LOAD_FAST_BORROW         2 (hits)
    # |                 CALL                     1
    # |                 STORE_FAST_LOAD_FAST   118 (@py_assert8, @py_assert3)
    # |                 LOAD_FAST_BORROW         7 (@py_assert8)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   136 (@py_assert5, @py_assert5)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       393 (to L14)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR                8 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              14 (('==',))
    # |                 LOAD_FAST_BORROW         8 (@py_assert5)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              15 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py9)s\n{%(py9)s = %(py6)s(%(py7)s)\n}',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert3, @py_assert8)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               3 ('py0')
    # |                 LOAD_CONST               4 ('len')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L5)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              4 (len)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L6)
    # |                 NOT_TAKEN
    # |         L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              4 (len)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L7)
    # |         L6:     LOAD_CONST               4 ('len')
    # |         L7:     LOAD_CONST               5 ('py2')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST               6 ('py4')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST               7 ('py6')
    # |                 LOAD_CONST               4 ('len')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              4 (len)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              4 (len)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST               4 ('len')
    # |        L10:     LOAD_CONST               8 ('py7')
    # |                 LOAD_CONST               9 ('hits')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (hits)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L12)
    # |                 NOT_TAKEN
    # |        L11:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (hits)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L13)
    # |        L12:     LOAD_CONST               9 ('hits')
    # |        L13:     LOAD_CONST              10 ('py9')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert8)
    # |                 CALL                     1
    # |                 BUILD_MAP                6
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format10)
    # |                 LOAD_CONST              11 ('assert %(py11)s')
    # |                 LOAD_CONST              12 ('py11')
    # |                 LOAD_FAST_BORROW         9 (@py_format10)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              10 (@py_format12)
    # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_format12)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L14:     LOAD_CONST              13 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST               6 (@py_assert3)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  135 (@py_assert5, @py_assert8)
    # |                 LOAD_CONST              13 (None)
    # |                 RETURN_VALUE
    # |   --   L15:     SWAP                     2
    # |                 POP_TOP
    # |   65            SWAP                     3
    # |                 STORE_FAST               4 (p)
    # |                 STORE_FAST               3 (_)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L15 [3]
    # | Disassembly of <code object test_per_book_is_configurable at 0x7c9ce68700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 67>:
    # |  67           RESUME                   0
    # |  68           LOAD_FAST_BORROW         1 (index)
    # |               LOAD_ATTR                1 (search + NULL|self)
    # |               LOAD_CONST               0 ('雨 伞 图书馆')
    # |               LOAD_SMALL_INT           4
    # |               LOAD_SMALL_INT           2
    # |               LOAD_CONST               1 (('limit', 'per_book'))
    # |               CALL_KW                  3
    # |               STORE_FAST               2 (hits)
    # |  69           LOAD_CONST               2 (<code object <genexpr> at 0x101f96af0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 69>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         2 (hits)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_GLOBAL              3 (sum + NULL)
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST               4 (@py_assert3)
    # |               LOAD_SMALL_INT           2
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert6, @py_assert3)
    # |               LOAD_FAST_BORROW         5 (@py_assert6)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       229 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              11 (('==',))
    # |               LOAD_FAST_BORROW         6 (@py_assert5)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              12 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert3, @py_assert6)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('sum')
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
    # |               LOAD_GLOBAL              2 (sum)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              2 (sum)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('sum')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py7')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format8)
    # |               LOAD_CONST               8 ('assert %(py9)s')
    # |               LOAD_CONST               9 ('py9')
    # |               LOAD_FAST_BORROW         7 (@py_format8)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format10)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  101 (@py_assert5, @py_assert6)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x101f96af0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 69>:
    # |   69           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                28 (to L5)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   18 (_, p)
    # |                LOAD_FAST_BORROW         2 (p)
    # |                LOAD_ATTR                0 (book)
    # |                LOAD_CONST               0 ('甲书')
    # |                COMPARE_OP              88 (bool(==))
    # |        L3:     POP_JUMP_IF_TRUE         3 (to L4)
    # |                NOT_TAKEN
    # |                JUMP_BACKWARD           24 (to L2)
    # |        L4:     LOAD_SMALL_INT           1
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           30 (to L2)
    # |        L5:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L3 -> L6 [0] lasti
    # |   L4 to L6 -> L6 [0] lasti
    # | Disassembly of <code object test_empty_index_is_safe at 0x7c9ce68a80, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 71>:
    # |  71           RESUME                   0
    # |  72           LOAD_GLOBAL              1 (PassageIndex + NULL)
    # |               CALL                     0
    # |               STORE_FAST_LOAD_FAST    17 (@py_assert1, @py_assert1)
    # |               LOAD_ATTR                2 (search)
    # |               STORE_FAST               2 (@py_assert3)
    # |               LOAD_CONST               0 ('任何内容')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert5, @py_assert3)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert5)
    # |               CALL                     1
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
    # |               LOAD_CONST              12 (('%(py8)s\n{%(py8)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}.search\n}(%(py6)s)\n} == %(py11)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert7, @py_assert10)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('PassageIndex')
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
    # |               LOAD_GLOBAL              0 (PassageIndex)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (PassageIndex)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('PassageIndex')
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
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE

    def test_finds_concrete_scene_match(self, index):
        '具象词是 BM25 的强项。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  54           RESUME                   0
        # |  56           LOAD_FAST_BORROW         1 (index)
        # |               LOAD_ATTR                1 (search + NULL|self)
        # |               LOAD_CONST               1 ('雨 伞 图书馆')
        # |               LOAD_SMALL_INT           2
        # |               LOAD_CONST               2 (('limit',))
        # |               CALL_KW                  2
        # |               STORE_FAST               2 (hits)
        # |  57           BUILD_LIST               0
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert1, hits)
        # |               STORE_FAST_LOAD_FAST    66 (@py_assert0, hits)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       35 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_FAST_BORROW         2 (hits)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               LOAD_SMALL_INT           1
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
        # |               LOAD_ATTR                2 (book)
        # |               STORE_FAST               6 (@py_assert6)
        # |               LOAD_CONST               3 ('甲书')
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert9, @py_assert6)
        # |               LOAD_FAST_BORROW         7 (@py_assert9)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert8, @py_assert8)
        # |               STORE_FAST               4 (@py_assert0)
        # |       L1:     LOAD_FAST_BORROW         4 (@py_assert0)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       312 (to L6)
        # |               NOT_TAKEN
        # |               LOAD_CONST               4 ('%(py2)s')
        # |               LOAD_CONST               5 ('py2')
        # |               LOAD_CONST               6 ('hits')
        # |               LOAD_GLOBAL              4 (@py_builtins)
        # |               LOAD_ATTR                6 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (hits)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (hits)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               6 ('hits')
        # |       L4:     BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   147 (@py_format3, @py_assert1)
        # |               LOAD_ATTR               15 (append + NULL|self)
        # |               LOAD_FAST_BORROW         9 (@py_format3)
        # |               CALL                     1
        # |               POP_TOP
        # |               LOAD_FAST_BORROW         2 (hits)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE      129 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('==',))
        # |               LOAD_FAST_CHECK          8 (@py_assert8)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py7)s\n{%(py7)s = %(py5)s.book\n} == %(py10)s',))
        # |               LOAD_FAST_CHECK          6 (@py_assert6)
        # |               LOAD_FAST_CHECK          7 (@py_assert9)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py5')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_CHECK          5 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert6)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py10')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert9)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format11)
        # |               LOAD_CONST              10 ('%(py12)s')
        # |               LOAD_CONST              11 ('py12')
        # |               LOAD_FAST_BORROW        10 (@py_format11)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   179 (@py_format13, @py_assert1)
        # |               LOAD_ATTR               15 (append + NULL|self)
        # |               LOAD_FAST_BORROW        11 (@py_format13)
        # |               CALL                     1
        # |               POP_TOP
        # |       L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_boolop)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BUILD_MAP                0
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              12 (@py_format14)
        # |               LOAD_CONST              12 ('assert %(py15)s')
        # |               LOAD_CONST              13 ('py15')
        # |               LOAD_FAST_BORROW        12 (@py_format14)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format16)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        13 (@py_format16)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L6:     LOAD_CONST              14 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert6)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert8, @py_assert9)
        # |               LOAD_CONST              14 (None)
        # |               RETURN_VALUE

    def test_irrelevant_query_returns_little(self, index):
        '量子力学 微积分'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  59           RESUME                   0
        # |  60           LOAD_FAST_BORROW         1 (index)
        # |               LOAD_ATTR                0 (search)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               0 ('量子力学 微积分')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       185 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.search\n}(%(py4)s)\n}')
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('index')
        # |               LOAD_GLOBAL              2 (@py_builtins)
        # |               LOAD_ATTR                4 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (index)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (index)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('index')
        # |       L3:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py6')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert5, @py_assert7)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_one_passage_per_book_by_default(self, index):
        '连续多段来自同一处最容易被整段模仿，也会让风格锚偏向单一作者。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   62            RESUME                   0
        # |   64            LOAD_FAST_BORROW         1 (index)
        # |                 LOAD_ATTR                1 (search + NULL|self)
        # |                 LOAD_CONST               1 ('雨 伞 图书馆')
        # |                 LOAD_SMALL_INT           4
        # |                 LOAD_CONST               2 (('limit',))
        # |                 CALL_KW                  2
        # |                 STORE_FAST               2 (hits)
        # |   65            LOAD_FAST_BORROW         2 (hits)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      3 (_)
        # |                 LOAD_FAST_AND_CLEAR      4 (p)
        # |                 SWAP                     3
        # |         L1:     BUILD_SET                0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                17 (to L3)
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST_STORE_FAST   52 (_, p)
        # |                 LOAD_FAST_BORROW         4 (p)
        # |                 LOAD_ATTR                2 (book)
        # |                 SET_ADD                  2
        # |                 JUMP_BACKWARD           19 (to L2)
        # |         L3:     END_FOR
        # |                 POP_ITER
        # |         L4:     STORE_FAST               5 (@py_assert1)
        # |                 STORE_FAST               3 (_)
        # |                 STORE_FAST               4 (p)
        # |                 LOAD_GLOBAL              5 (len + NULL)
        # |                 LOAD_FAST_BORROW         5 (@py_assert1)
        # |                 CALL                     1
        # |                 STORE_FAST               6 (@py_assert3)
        # |                 LOAD_GLOBAL              5 (len + NULL)
        # |                 LOAD_FAST_BORROW         2 (hits)
        # |                 CALL                     1
        # |                 STORE_FAST_LOAD_FAST   118 (@py_assert8, @py_assert3)
        # |                 LOAD_FAST_BORROW         7 (@py_assert8)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   136 (@py_assert5, @py_assert5)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       393 (to L14)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR                8 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              14 (('==',))
        # |                 LOAD_FAST_BORROW         8 (@py_assert5)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              15 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py9)s\n{%(py9)s = %(py6)s(%(py7)s)\n}',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert3, @py_assert8)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               3 ('py0')
        # |                 LOAD_CONST               4 ('len')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L5)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              4 (len)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L6)
        # |                 NOT_TAKEN
        # |         L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              4 (len)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L7)
        # |         L6:     LOAD_CONST               4 ('len')
        # |         L7:     LOAD_CONST               5 ('py2')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST               6 ('py4')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST               7 ('py6')
        # |                 LOAD_CONST               4 ('len')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              4 (len)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              4 (len)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST               4 ('len')
        # |        L10:     LOAD_CONST               8 ('py7')
        # |                 LOAD_CONST               9 ('hits')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (hits)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L12)
        # |                 NOT_TAKEN
        # |        L11:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (hits)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L13)
        # |        L12:     LOAD_CONST               9 ('hits')
        # |        L13:     LOAD_CONST              10 ('py9')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert8)
        # |                 CALL                     1
        # |                 BUILD_MAP                6
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format10)
        # |                 LOAD_CONST              11 ('assert %(py11)s')
        # |                 LOAD_CONST              12 ('py11')
        # |                 LOAD_FAST_BORROW         9 (@py_format10)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              10 (@py_format12)
        # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_format12)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L14:     LOAD_CONST              13 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST               6 (@py_assert3)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  135 (@py_assert5, @py_assert8)
        # |                 LOAD_CONST              13 (None)
        # |                 RETURN_VALUE
        # |   --   L15:     SWAP                     2
        # |                 POP_TOP
        # |   65            SWAP                     3
        # |                 STORE_FAST               4 (p)
        # |                 STORE_FAST               3 (_)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L15 [3]

    def test_per_book_is_configurable(self, index):
        '雨 伞 图书馆'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  67           RESUME                   0
        # |  68           LOAD_FAST_BORROW         1 (index)
        # |               LOAD_ATTR                1 (search + NULL|self)
        # |               LOAD_CONST               0 ('雨 伞 图书馆')
        # |               LOAD_SMALL_INT           4
        # |               LOAD_SMALL_INT           2
        # |               LOAD_CONST               1 (('limit', 'per_book'))
        # |               CALL_KW                  3
        # |               STORE_FAST               2 (hits)
        # |  69           LOAD_CONST               2 (<code object <genexpr> at 0x101f96af0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 69>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         2 (hits)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_GLOBAL              3 (sum + NULL)
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST               4 (@py_assert3)
        # |               LOAD_SMALL_INT           2
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert6, @py_assert3)
        # |               LOAD_FAST_BORROW         5 (@py_assert6)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       229 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              11 (('==',))
        # |               LOAD_FAST_BORROW         6 (@py_assert5)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              12 (('%(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n} == %(py7)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert3, @py_assert6)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('sum')
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
        # |               LOAD_GLOBAL              2 (sum)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              2 (sum)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('sum')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py7')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format8)
        # |               LOAD_CONST               8 ('assert %(py9)s')
        # |               LOAD_CONST               9 ('py9')
        # |               LOAD_FAST_BORROW         7 (@py_format8)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format10)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  101 (@py_assert5, @py_assert6)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x101f96af0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 69>:
        # |   69           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                28 (to L5)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   18 (_, p)
        # |                LOAD_FAST_BORROW         2 (p)
        # |                LOAD_ATTR                0 (book)
        # |                LOAD_CONST               0 ('甲书')
        # |                COMPARE_OP              88 (bool(==))
        # |        L3:     POP_JUMP_IF_TRUE         3 (to L4)
        # |                NOT_TAKEN
        # |                JUMP_BACKWARD           24 (to L2)
        # |        L4:     LOAD_SMALL_INT           1
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           30 (to L2)
        # |        L5:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L6:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L3 -> L6 [0] lasti
        # |   L4 to L6 -> L6 [0] lasti

    def test_empty_index_is_safe(self):
        '任何内容'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  71           RESUME                   0
        # |  72           LOAD_GLOBAL              1 (PassageIndex + NULL)
        # |               CALL                     0
        # |               STORE_FAST_LOAD_FAST    17 (@py_assert1, @py_assert1)
        # |               LOAD_ATTR                2 (search)
        # |               STORE_FAST               2 (@py_assert3)
        # |               LOAD_CONST               0 ('任何内容')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert5, @py_assert3)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert5)
        # |               CALL                     1
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
        # |               LOAD_CONST              12 (('%(py8)s\n{%(py8)s = %(py4)s\n{%(py4)s = %(py2)s\n{%(py2)s = %(py0)s()\n}.search\n}(%(py6)s)\n} == %(py11)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert7, @py_assert10)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('PassageIndex')
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
        # |               LOAD_GLOBAL              0 (PassageIndex)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (PassageIndex)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('PassageIndex')
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
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE


class TestRetriever:
    'TestRetriever'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  75           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestRetriever')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          75
    # |               STORE_NAME               3 (__firstlineno__)
    # |  76           LOAD_CONST               1 (<code object test_query_includes_concrete_descriptors at 0x7c9d1d6d00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 76>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_query_includes_concrete_descriptors)
    # |  80           LOAD_CONST               2 (<code object test_snippets_returned at 0x7c9d1d7200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 80>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_snippets_returned)
    # |  83           LOAD_CONST               3 (<code object test_empty_index_yields_no_snippets at 0x7c9ce59200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 83>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_empty_index_yields_no_snippets)
    # |  86           LOAD_CONST               4 (<code object test_abstract_emotion_alone_finds_nothing at 0x7c9ce78300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 86>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_abstract_emotion_alone_finds_nothing)
    # |               LOAD_CONST               5 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_query_includes_concrete_descriptors at 0x7c9d1d6d00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 76>:
    # |  76           RESUME                   0
    # |  77           LOAD_GLOBAL              1 (SceneRetriever + NULL)
    # |               LOAD_FAST_BORROW         1 (index)
    # |               CALL                     1
    # |               LOAD_ATTR                3 (query_for + NULL|self)
    # |               LOAD_GLOBAL              5 (scene + NULL)
    # |               CALL                     0
    # |               CALL                     1
    # |               STORE_FAST               2 (q)
    # |  78           BUILD_LIST               0
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               0 ('雨中共伞')
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               LOAD_FAST_BORROW         2 (q)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert0, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE        8 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('图书馆')
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert9, @py_assert9)
    # |               LOAD_FAST_BORROW         2 (q)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert11, @py_assert11)
    # |               STORE_FAST               6 (@py_assert0)
    # |       L1:     LOAD_FAST_BORROW         6 (@py_assert0)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       404 (to L9)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('in',))
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py3)s in %(py5)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (@py_assert2, q)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py3')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py5')
    # |               LOAD_CONST               4 ('q')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (q)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (q)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               4 ('q')
    # |       L4:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format6)
    # |               LOAD_CONST               5 ('%(py7)s')
    # |               LOAD_CONST               6 ('py7')
    # |               LOAD_FAST_BORROW         9 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   163 (@py_format8, @py_assert1)
    # |               LOAD_ATTR               19 (append + NULL|self)
    # |               LOAD_FAST_BORROW        10 (@py_format8)
    # |               CALL                     1
    # |               POP_TOP
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE      163 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('in',))
    # |               LOAD_FAST_CHECK          8 (@py_assert11)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py10)s in %(py12)s',))
    # |               LOAD_FAST_CHECK          7 (@py_assert9)
    # |               LOAD_FAST_BORROW         2 (q)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py10')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert9)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py12')
    # |               LOAD_CONST               4 ('q')
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
    # |               LOAD_FAST_BORROW         2 (q)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (q)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               4 ('q')
    # |       L7:     BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format13)
    # |               LOAD_CONST               9 ('%(py14)s')
    # |               LOAD_CONST              10 ('py14')
    # |               LOAD_FAST_BORROW        11 (@py_format13)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   195 (@py_format15, @py_assert1)
    # |               LOAD_ATTR               19 (append + NULL|self)
    # |               LOAD_FAST_BORROW        12 (@py_format15)
    # |               CALL                     1
    # |               POP_TOP
    # |       L8:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_boolop)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BUILD_MAP                0
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format16)
    # |               LOAD_CONST              11 ('assert %(py17)s')
    # |               LOAD_CONST              12 ('py17')
    # |               LOAD_FAST_BORROW        13 (@py_format16)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              14 (@py_format18)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        14 (@py_format18)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L9:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert9, @py_assert11)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_snippets_returned at 0x7c9d1d7200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 80>:
    # |  80            RESUME                   0
    # |  81            LOAD_SMALL_INT           2
    # |                STORE_FAST               2 (@py_assert2)
    # |                LOAD_GLOBAL              1 (SceneRetriever + NULL)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (index, @py_assert2)
    # |                LOAD_CONST               1 (('limit',))
    # |                CALL_KW                  2
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |                LOAD_ATTR                2 (snippets)
    # |                STORE_FAST               4 (@py_assert6)
    # |                LOAD_GLOBAL              5 (scene + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert9, @py_assert6)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert9)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert11, @py_assert11)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       401 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_CONST               2 ('assert %(py12)s\n{%(py12)s = %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py0)s(%(py1)s, limit=%(py3)s)\n}.snippets\n}(%(py10)s\n{%(py10)s = %(py8)s()\n})\n}')
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('SceneRetriever')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (SceneRetriever)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (SceneRetriever)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('SceneRetriever')
    # |        L3:     LOAD_CONST               5 ('py1')
    # |                LOAD_CONST               6 ('index')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (index)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (index)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               6 ('index')
    # |        L6:     LOAD_CONST               7 ('py3')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py8')
    # |                LOAD_CONST              11 ('scene')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (scene)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (scene)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              11 ('scene')
    # |        L9:     LOAD_CONST              12 ('py10')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py12')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert11)
    # |                CALL                     1
    # |                BUILD_MAP                8
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format13)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format13)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              14 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert9, @py_assert11)
    # |                LOAD_CONST              14 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_empty_index_yields_no_snippets at 0x7c9ce59200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 83>:
    # |  83            RESUME                   0
    # |  84            LOAD_GLOBAL              1 (PassageIndex + NULL)
    # |                CALL                     0
    # |                STORE_FAST               1 (@py_assert2)
    # |                LOAD_GLOBAL              3 (SceneRetriever + NULL)
    # |                LOAD_FAST_BORROW         1 (@py_assert2)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    34 (@py_assert4, @py_assert4)
    # |                LOAD_ATTR                4 (snippets)
    # |                STORE_FAST               3 (@py_assert6)
    # |                LOAD_GLOBAL              7 (scene + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert9, @py_assert6)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert9)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert11)
    # |                BUILD_LIST               0
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert14, @py_assert11)
    # |                LOAD_FAST_BORROW         6 (@py_assert14)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert13, @py_assert13)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       467 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert13)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py12)s\n{%(py12)s = %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s()\n})\n}.snippets\n}(%(py10)s\n{%(py10)s = %(py8)s()\n})\n} == %(py15)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert11, @py_assert14)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('SceneRetriever')
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
    # |                LOAD_GLOBAL              2 (SceneRetriever)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (SceneRetriever)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               2 ('SceneRetriever')
    # |        L3:     LOAD_CONST               3 ('py1')
    # |                LOAD_CONST               4 ('PassageIndex')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (PassageIndex)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (PassageIndex)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               4 ('PassageIndex')
    # |        L6:     LOAD_CONST               5 ('py3')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py7')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert6)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py8')
    # |                LOAD_CONST               9 ('scene')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (scene)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (scene)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               9 ('scene')
    # |        L9:     LOAD_CONST              10 ('py10')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py12')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert11)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py15')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert14)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format16)
    # |                LOAD_CONST              13 ('assert %(py17)s')
    # |                LOAD_CONST              14 ('py17')
    # |                LOAD_FAST_BORROW         8 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format18)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               1 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert6)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert9)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert11)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  118 (@py_assert13, @py_assert14)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_abstract_emotion_alone_finds_nothing at 0x7c9ce78300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 86>:
    # |  86           RESUME                   0
    # |  89           LOAD_FAST_BORROW         1 (index)
    # |               LOAD_ATTR                0 (search)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_CONST               1 ('戒备 动摇 不肯承认')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       185 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               2 ('assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.search\n}(%(py4)s)\n}')
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('index')
    # |               LOAD_GLOBAL              2 (@py_builtins)
    # |               LOAD_ATTR                4 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (index)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (index)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('index')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py4')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py6')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format8)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert3)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert5, @py_assert7)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE

    def test_query_includes_concrete_descriptors(self, index):
        '雨中共伞'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  76           RESUME                   0
        # |  77           LOAD_GLOBAL              1 (SceneRetriever + NULL)
        # |               LOAD_FAST_BORROW         1 (index)
        # |               CALL                     1
        # |               LOAD_ATTR                3 (query_for + NULL|self)
        # |               LOAD_GLOBAL              5 (scene + NULL)
        # |               CALL                     0
        # |               CALL                     1
        # |               STORE_FAST               2 (q)
        # |  78           BUILD_LIST               0
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               0 ('雨中共伞')
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               LOAD_FAST_BORROW         2 (q)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert0, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE        8 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('图书馆')
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert9, @py_assert9)
        # |               LOAD_FAST_BORROW         2 (q)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert11, @py_assert11)
        # |               STORE_FAST               6 (@py_assert0)
        # |       L1:     LOAD_FAST_BORROW         6 (@py_assert0)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       404 (to L9)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('in',))
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              15 (('%(py3)s in %(py5)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (@py_assert2, q)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py3')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py5')
        # |               LOAD_CONST               4 ('q')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (q)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (q)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               4 ('q')
        # |       L4:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format6)
        # |               LOAD_CONST               5 ('%(py7)s')
        # |               LOAD_CONST               6 ('py7')
        # |               LOAD_FAST_BORROW         9 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   163 (@py_format8, @py_assert1)
        # |               LOAD_ATTR               19 (append + NULL|self)
        # |               LOAD_FAST_BORROW        10 (@py_format8)
        # |               CALL                     1
        # |               POP_TOP
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE      163 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('in',))
        # |               LOAD_FAST_CHECK          8 (@py_assert11)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py10)s in %(py12)s',))
        # |               LOAD_FAST_CHECK          7 (@py_assert9)
        # |               LOAD_FAST_BORROW         2 (q)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py10')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert9)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py12')
        # |               LOAD_CONST               4 ('q')
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
        # |               LOAD_FAST_BORROW         2 (q)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (q)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               4 ('q')
        # |       L7:     BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format13)
        # |               LOAD_CONST               9 ('%(py14)s')
        # |               LOAD_CONST              10 ('py14')
        # |               LOAD_FAST_BORROW        11 (@py_format13)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   195 (@py_format15, @py_assert1)
        # |               LOAD_ATTR               19 (append + NULL|self)
        # |               LOAD_FAST_BORROW        12 (@py_format15)
        # |               CALL                     1
        # |               POP_TOP
        # |       L8:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_boolop)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BUILD_MAP                0
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format16)
        # |               LOAD_CONST              11 ('assert %(py17)s')
        # |               LOAD_CONST              12 ('py17')
        # |               LOAD_FAST_BORROW        13 (@py_format16)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              14 (@py_format18)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        14 (@py_format18)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L9:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert9, @py_assert11)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE

    def test_snippets_returned(self, index):
        'assert %(py12)s\n{%(py12)s = %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py0)s(%(py1)s, limit=%(py3)s)\n}.snippets\n}(%(py10)s\n{%(py10)s = %(py8)s()\n})\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  80            RESUME                   0
        # |  81            LOAD_SMALL_INT           2
        # |                STORE_FAST               2 (@py_assert2)
        # |                LOAD_GLOBAL              1 (SceneRetriever + NULL)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (index, @py_assert2)
        # |                LOAD_CONST               1 (('limit',))
        # |                CALL_KW                  2
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |                LOAD_ATTR                2 (snippets)
        # |                STORE_FAST               4 (@py_assert6)
        # |                LOAD_GLOBAL              5 (scene + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert9, @py_assert6)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert9)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert11, @py_assert11)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       401 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_CONST               2 ('assert %(py12)s\n{%(py12)s = %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py0)s(%(py1)s, limit=%(py3)s)\n}.snippets\n}(%(py10)s\n{%(py10)s = %(py8)s()\n})\n}')
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('SceneRetriever')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (SceneRetriever)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (SceneRetriever)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('SceneRetriever')
        # |        L3:     LOAD_CONST               5 ('py1')
        # |                LOAD_CONST               6 ('index')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (index)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (index)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               6 ('index')
        # |        L6:     LOAD_CONST               7 ('py3')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py8')
        # |                LOAD_CONST              11 ('scene')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (scene)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (scene)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              11 ('scene')
        # |        L9:     LOAD_CONST              12 ('py10')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert9)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py12')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert11)
        # |                CALL                     1
        # |                BUILD_MAP                8
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format13)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format13)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              14 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert9, @py_assert11)
        # |                LOAD_CONST              14 (None)
        # |                RETURN_VALUE

    def test_empty_index_yields_no_snippets(self):
        '=='
        # ── 函数体（字节码重建见 BODY 段）──
        # |  83            RESUME                   0
        # |  84            LOAD_GLOBAL              1 (PassageIndex + NULL)
        # |                CALL                     0
        # |                STORE_FAST               1 (@py_assert2)
        # |                LOAD_GLOBAL              3 (SceneRetriever + NULL)
        # |                LOAD_FAST_BORROW         1 (@py_assert2)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    34 (@py_assert4, @py_assert4)
        # |                LOAD_ATTR                4 (snippets)
        # |                STORE_FAST               3 (@py_assert6)
        # |                LOAD_GLOBAL              7 (scene + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert9, @py_assert6)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert9)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert11)
        # |                BUILD_LIST               0
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert14, @py_assert11)
        # |                LOAD_FAST_BORROW         6 (@py_assert14)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert13, @py_assert13)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       467 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert13)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py12)s\n{%(py12)s = %(py7)s\n{%(py7)s = %(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s()\n})\n}.snippets\n}(%(py10)s\n{%(py10)s = %(py8)s()\n})\n} == %(py15)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert11, @py_assert14)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('SceneRetriever')
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
        # |                LOAD_GLOBAL              2 (SceneRetriever)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (SceneRetriever)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               2 ('SceneRetriever')
        # |        L3:     LOAD_CONST               3 ('py1')
        # |                LOAD_CONST               4 ('PassageIndex')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (PassageIndex)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (PassageIndex)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               4 ('PassageIndex')
        # |        L6:     LOAD_CONST               5 ('py3')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py7')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert6)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py8')
        # |                LOAD_CONST               9 ('scene')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (scene)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (scene)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               9 ('scene')
        # |        L9:     LOAD_CONST              10 ('py10')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert9)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py12')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert11)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py15')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert14)
        # |                CALL                     1
        # |                BUILD_MAP                9
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format16)
        # |                LOAD_CONST              13 ('assert %(py17)s')
        # |                LOAD_CONST              14 ('py17')
        # |                LOAD_FAST_BORROW         8 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format18)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format18)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               1 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert6)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert9)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert11)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  118 (@py_assert13, @py_assert14)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE

    def test_abstract_emotion_alone_finds_nothing(self, index):
        '如实记录局限：情绪词在正文里几乎不字面出现，词法检索抓不到。\n换成向量检索后这条应当改为能匹配。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  86           RESUME                   0
        # |  89           LOAD_FAST_BORROW         1 (index)
        # |               LOAD_ATTR                0 (search)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_CONST               1 ('戒备 动摇 不肯承认')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       185 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               2 ('assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.search\n}(%(py4)s)\n}')
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('index')
        # |               LOAD_GLOBAL              2 (@py_builtins)
        # |               LOAD_ATTR                4 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (index)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (index)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('index')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py4')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py6')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format8)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert3)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert5, @py_assert7)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE


class TestPersistence:
    'TestPersistence'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  92           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestPersistence')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          92
    # |               STORE_NAME               3 (__firstlineno__)
    # |  93           LOAD_CONST               1 (<code object test_roundtrip at 0x7c9d09ea00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 93>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_roundtrip)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_roundtrip at 0x7c9d09ea00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 93>:
    # |  93            RESUME                   0
    # |  94            LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               0 ('idx.json')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               3 (f)
    # |  95            LOAD_FAST_BORROW         2 (index)
    # |                LOAD_ATTR                1 (save + NULL|self)
    # |                LOAD_FAST_BORROW         3 (f)
    # |                CALL                     1
    # |                POP_TOP
    # |  96            LOAD_GLOBAL              2 (PassageIndex)
    # |                LOAD_ATTR                4 (load)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (f)
    # |                CALL                     1
    # |                STORE_FAST               4 (loaded)
    # |  97            LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_FAST_BORROW         4 (loaded)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert2)
    # |                LOAD_GLOBAL              7 (len + NULL)
    # |                LOAD_FAST_BORROW         2 (index)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert7, @py_assert2)
    # |                LOAD_FAST_BORROW         6 (@py_assert7)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       449 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py8)s\n{%(py8)s = %(py5)s(%(py6)s)\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert7)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('len')
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
    # |        L2:     LOAD_CONST               2 ('len')
    # |        L3:     LOAD_CONST               3 ('py1')
    # |                LOAD_CONST               4 ('loaded')
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
    # |                LOAD_FAST_BORROW         4 (loaded)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (loaded)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               4 ('loaded')
    # |        L6:     LOAD_CONST               5 ('py3')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_CONST               2 ('len')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (len)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (len)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               2 ('len')
    # |        L9:     LOAD_CONST               7 ('py6')
    # |                LOAD_CONST               8 ('index')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (index)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (index)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST               8 ('index')
    # |       L12:     LOAD_CONST               9 ('py8')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert7)
    # |                CALL                     1
    # |                BUILD_MAP                6
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format9)
    # |                LOAD_CONST              10 ('assert %(py10)s')
    # |                LOAD_CONST              11 ('py10')
    # |                LOAD_FAST_BORROW         8 (@py_format9)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format11)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format11)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L13:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  118 (@py_assert4, @py_assert7)
    # | 101            LOAD_FAST_BORROW         4 (loaded)
    # |                LOAD_ATTR               25 (search + NULL|self)
    # |                LOAD_CONST              13 ('雨中共伞 图书馆')
    # |                LOAD_SMALL_INT           1
    # |                LOAD_CONST              14 (('limit',))
    # |                CALL_KW                  2
    # |                LOAD_SMALL_INT           0
    # |                BINARY_OP               26 ([])
    # |                LOAD_SMALL_INT           1
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert0, @py_assert0)
    # |                LOAD_ATTR               26 (book)
    # |                STORE_FAST               5 (@py_assert2)
    # |                LOAD_CONST              15 ('甲书')
    # |                STORE_FAST_LOAD_FAST   181 (@py_assert5, @py_assert2)
    # |                LOAD_FAST_BORROW        11 (@py_assert5)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       143 (to L14)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py3)s\n{%(py3)s = %(py1)s.book\n} == %(py6)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 91 (@py_assert2, @py_assert5)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py3')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py6')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format7)
    # |                LOAD_CONST              16 ('assert %(py8)s')
    # |                LOAD_CONST               9 ('py8')
    # |                LOAD_FAST_BORROW        12 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format9)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L14:     LOAD_CONST              12 (None)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  123 (@py_assert4, @py_assert5)
    # |                LOAD_CONST              12 (None)
    # |                RETURN_VALUE

    def test_roundtrip(self, tmp_path, index):
        'idx.json'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  93            RESUME                   0
        # |  94            LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               0 ('idx.json')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               3 (f)
        # |  95            LOAD_FAST_BORROW         2 (index)
        # |                LOAD_ATTR                1 (save + NULL|self)
        # |                LOAD_FAST_BORROW         3 (f)
        # |                CALL                     1
        # |                POP_TOP
        # |  96            LOAD_GLOBAL              2 (PassageIndex)
        # |                LOAD_ATTR                4 (load)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (f)
        # |                CALL                     1
        # |                STORE_FAST               4 (loaded)
        # |  97            LOAD_GLOBAL              7 (len + NULL)
        # |                LOAD_FAST_BORROW         4 (loaded)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert2)
        # |                LOAD_GLOBAL              7 (len + NULL)
        # |                LOAD_FAST_BORROW         2 (index)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert7, @py_assert2)
        # |                LOAD_FAST_BORROW         6 (@py_assert7)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       449 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py8)s\n{%(py8)s = %(py5)s(%(py6)s)\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert7)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('len')
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
        # |        L2:     LOAD_CONST               2 ('len')
        # |        L3:     LOAD_CONST               3 ('py1')
        # |                LOAD_CONST               4 ('loaded')
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
        # |                LOAD_FAST_BORROW         4 (loaded)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (loaded)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               4 ('loaded')
        # |        L6:     LOAD_CONST               5 ('py3')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_CONST               2 ('len')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (len)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (len)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               2 ('len')
        # |        L9:     LOAD_CONST               7 ('py6')
        # |                LOAD_CONST               8 ('index')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (index)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (index)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST               8 ('index')
        # |       L12:     LOAD_CONST               9 ('py8')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert7)
        # |                CALL                     1
        # |                BUILD_MAP                6
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format9)
        # |                LOAD_CONST              10 ('assert %(py10)s')
        # |                LOAD_CONST              11 ('py10')
        # |                LOAD_FAST_BORROW         8 (@py_format9)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format11)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format11)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L13:     LOAD_CONST              12 (None)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  118 (@py_assert4, @py_assert7)
        # | 101            LOAD_FAST_BORROW         4 (loaded)
        # |                LOAD_ATTR               25 (search + NULL|self)
        # |                LOAD_CONST              13 ('雨中共伞 图书馆')
        # |                LOAD_SMALL_INT           1
        # |                LOAD_CONST              14 (('limit',))
        # |                CALL_KW                  2
        # |                LOAD_SMALL_INT           0
        # |                BINARY_OP               26 ([])
        # |                LOAD_SMALL_INT           1
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert0, @py_assert0)
        # |                LOAD_ATTR               26 (book)
        # |                STORE_FAST               5 (@py_assert2)
        # |                LOAD_CONST              15 ('甲书')
        # |                STORE_FAST_LOAD_FAST   181 (@py_assert5, @py_assert2)
        # |                LOAD_FAST_BORROW        11 (@py_assert5)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       143 (to L14)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py3)s\n{%(py3)s = %(py1)s.book\n} == %(py6)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 91 (@py_assert2, @py_assert5)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py3')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py6')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format7)
        # |                LOAD_CONST              16 ('assert %(py8)s')
        # |                LOAD_CONST               9 ('py8')
        # |                LOAD_FAST_BORROW        12 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format9)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format9)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L14:     LOAD_CONST              12 (None)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  123 (@py_assert4, @py_assert5)
        # |                LOAD_CONST              12 (None)
        # |                RETURN_VALUE


class TestChunking:
    'TestChunking'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 104           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestChunking')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         104
    # |               STORE_NAME               3 (__firstlineno__)
    # | 105           LOAD_CONST               1 (<code object test_splits_book_into_passages at 0x7c9ce59e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 105>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_splits_book_into_passages)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_splits_book_into_passages at 0x7c9ce59e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 105>:
    # |   --            MAKE_CELL               12 (make_chapter)
    # |  105            RESUME                   0
    # |  106            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               1 (('make_chapter',))
    # |                 IMPORT_NAME              0 (conftest)
    # |                 IMPORT_FROM              1 (make_chapter)
    # |                 STORE_DEREF             12 (make_chapter)
    # |                 POP_TOP
    # |  108            LOAD_FAST_BORROW         1 (tmp_path)
    # |                 LOAD_CONST               2 ('书.txt')
    # |                 BINARY_OP               11 (/)
    # |                 STORE_FAST               2 (f)
    # |  109            LOAD_FAST_BORROW         2 (f)
    # |                 LOAD_ATTR                5 (write_text + NULL|self)
    # |                 LOAD_CONST               3 ('\n\n')
    # |                 LOAD_ATTR                7 (join + NULL|self)
    # |                 LOAD_FAST_BORROW        12 (make_chapter)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST               4 (<code object <genexpr> at 0x106aac690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 109>)
    # |                 MAKE_FUNCTION
    # |                 SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                 LOAD_CONST              20 ((1, 2))
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 LOAD_CONST               5 ('utf-8')
    # |                 CALL                     2
    # |                 POP_TOP
    # |  110            LOAD_GLOBAL              9 (PassageIndex + NULL)
    # |                 CALL                     0
    # |                 STORE_FAST               3 (idx)
    # |  111            LOAD_FAST_BORROW         3 (idx)
    # |                 LOAD_ATTR               10 (add_book)
    # |                 STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (f)
    # |                 CALL                     1
    # |                 STORE_FAST               5 (@py_assert4)
    # |                 LOAD_SMALL_INT           0
    # |                 STORE_FAST_LOAD_FAST   101 (@py_assert7, @py_assert4)
    # |                 LOAD_FAST_BORROW         6 (@py_assert7)
    # |                 COMPARE_OP             132 (>)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert6, @py_assert6)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       299 (to L7)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              21 (('>',))
    # |                 LOAD_FAST_BORROW         7 (@py_assert6)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              22 (('%(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.add_book\n}(%(py3)s)\n} > %(py8)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert4, @py_assert7)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               6 ('py0')
    # |                 LOAD_CONST               7 ('idx')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L1)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (idx)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L2)
    # |                 NOT_TAKEN
    # |         L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (idx)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L3)
    # |         L2:     LOAD_CONST               7 ('idx')
    # |         L3:     LOAD_CONST               8 ('py2')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST               9 ('py3')
    # |                 LOAD_CONST              10 ('f')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (f)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (f)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST              10 ('f')
    # |         L6:     LOAD_CONST              11 ('py5')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py8')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert7)
    # |                 CALL                     1
    # |                 BUILD_MAP                5
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format9)
    # |                 LOAD_CONST              13 ('assert %(py10)s')
    # |                 LOAD_CONST              14 ('py10')
    # |                 LOAD_FAST_BORROW         8 (@py_format9)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format11)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_format11)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L7:     LOAD_CONST              15 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert4)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  118 (@py_assert6, @py_assert7)
    # |  112            LOAD_CONST              16 (<code object <genexpr> at 0x101ffe630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 112>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_FAST_BORROW         3 (idx)
    # |                 LOAD_ATTR               28 (passages)
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 STORE_FAST               4 (@py_assert1)
    # |                 LOAD_GLOBAL             31 (all + NULL)
    # |                 LOAD_FAST_BORROW         4 (@py_assert1)
    # |                 CALL                     1
    # |                 STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       171 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_CONST              17 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |                 LOAD_CONST               6 ('py0')
    # |                 LOAD_CONST              18 ('all')
    # |                 LOAD_GLOBAL             16 (@py_builtins)
    # |                 LOAD_ATTR               18 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             30 (all)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL             30 (all)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST              18 ('all')
    # |        L10:     LOAD_CONST               8 ('py2')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              19 ('py4')
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              11 (@py_format5)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             12 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_format5)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST              15 (None)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   74 (@py_assert1, @py_assert3)
    # |                 LOAD_CONST              15 (None)
    # |                 RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x106aac690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 109>:
    # |   --           COPY_FREE_VARS           1
    # |  109           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                14 (to L3)
    # |                STORE_FAST               1 (i)
    # |                LOAD_DEREF               2 (make_chapter)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (i)
    # |                LOAD_CONST               0 (('ch',))
    # |                CALL_KW                  1
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
    # | Disassembly of <code object <genexpr> at 0x101ffe630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 112>:
    # |  112           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                29 (to L3)
    # |                STORE_FAST               1 (p)
    # |                LOAD_GLOBAL              1 (len + NULL)
    # |                LOAD_FAST_BORROW         1 (p)
    # |                LOAD_ATTR                2 (text)
    # |                CALL                     1
    # |                LOAD_SMALL_INT         100
    # |                COMPARE_OP             172 (>=)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           31 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti

    def test_splits_book_into_passages(self, tmp_path):
        '书.txt'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --            MAKE_CELL               12 (make_chapter)
        # |  105            RESUME                   0
        # |  106            LOAD_SMALL_INT           0
        # |                 LOAD_CONST               1 (('make_chapter',))
        # |                 IMPORT_NAME              0 (conftest)
        # |                 IMPORT_FROM              1 (make_chapter)
        # |                 STORE_DEREF             12 (make_chapter)
        # |                 POP_TOP
        # |  108            LOAD_FAST_BORROW         1 (tmp_path)
        # |                 LOAD_CONST               2 ('书.txt')
        # |                 BINARY_OP               11 (/)
        # |                 STORE_FAST               2 (f)
        # |  109            LOAD_FAST_BORROW         2 (f)
        # |                 LOAD_ATTR                5 (write_text + NULL|self)
        # |                 LOAD_CONST               3 ('\n\n')
        # |                 LOAD_ATTR                7 (join + NULL|self)
        # |                 LOAD_FAST_BORROW        12 (make_chapter)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST               4 (<code object <genexpr> at 0x106aac690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 109>)
        # |                 MAKE_FUNCTION
        # |                 SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                 LOAD_CONST              20 ((1, 2))
        # |                 GET_ITER
        # |                 CALL                     0
        # |                 CALL                     1
        # |                 LOAD_CONST               5 ('utf-8')
        # |                 CALL                     2
        # |                 POP_TOP
        # |  110            LOAD_GLOBAL              9 (PassageIndex + NULL)
        # |                 CALL                     0
        # |                 STORE_FAST               3 (idx)
        # |  111            LOAD_FAST_BORROW         3 (idx)
        # |                 LOAD_ATTR               10 (add_book)
        # |                 STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (f)
        # |                 CALL                     1
        # |                 STORE_FAST               5 (@py_assert4)
        # |                 LOAD_SMALL_INT           0
        # |                 STORE_FAST_LOAD_FAST   101 (@py_assert7, @py_assert4)
        # |                 LOAD_FAST_BORROW         6 (@py_assert7)
        # |                 COMPARE_OP             132 (>)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert6, @py_assert6)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       299 (to L7)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              21 (('>',))
        # |                 LOAD_FAST_BORROW         7 (@py_assert6)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              22 (('%(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.add_book\n}(%(py3)s)\n} > %(py8)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert4, @py_assert7)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               6 ('py0')
        # |                 LOAD_CONST               7 ('idx')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L1)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (idx)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L2)
        # |                 NOT_TAKEN
        # |         L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (idx)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L3)
        # |         L2:     LOAD_CONST               7 ('idx')
        # |         L3:     LOAD_CONST               8 ('py2')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST               9 ('py3')
        # |                 LOAD_CONST              10 ('f')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (f)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (f)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST              10 ('f')
        # |         L6:     LOAD_CONST              11 ('py5')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py8')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert7)
        # |                 CALL                     1
        # |                 BUILD_MAP                5
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format9)
        # |                 LOAD_CONST              13 ('assert %(py10)s')
        # |                 LOAD_CONST              14 ('py10')
        # |                 LOAD_FAST_BORROW         8 (@py_format9)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format11)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_format11)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L7:     LOAD_CONST              15 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert4)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  118 (@py_assert6, @py_assert7)
        # |  112            LOAD_CONST              16 (<code object <genexpr> at 0x101ffe630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 112>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_FAST_BORROW         3 (idx)
        # |                 LOAD_ATTR               28 (passages)
        # |                 GET_ITER
        # |                 CALL                     0
        # |                 STORE_FAST               4 (@py_assert1)
        # |                 LOAD_GLOBAL             31 (all + NULL)
        # |                 LOAD_FAST_BORROW         4 (@py_assert1)
        # |                 CALL                     1
        # |                 STORE_FAST_LOAD_FAST   170 (@py_assert3, @py_assert3)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       171 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_CONST              17 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |                 LOAD_CONST               6 ('py0')
        # |                 LOAD_CONST              18 ('all')
        # |                 LOAD_GLOBAL             16 (@py_builtins)
        # |                 LOAD_ATTR               18 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             30 (all)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL             30 (all)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST              18 ('all')
        # |        L10:     LOAD_CONST               8 ('py2')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              19 ('py4')
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              11 (@py_format5)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             12 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_format5)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST              15 (None)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   74 (@py_assert1, @py_assert3)
        # |                 LOAD_CONST              15 (None)
        # |                 RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x106aac690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 109>:
        # |   --           COPY_FREE_VARS           1
        # |  109           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                14 (to L3)
        # |                STORE_FAST               1 (i)
        # |                LOAD_DEREF               2 (make_chapter)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (i)
        # |                LOAD_CONST               0 (('ch',))
        # |                CALL_KW                  1
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
        # | Disassembly of <code object <genexpr> at 0x101ffe630, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_index.py", line 112>:
        # |  112           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                29 (to L3)
        # |                STORE_FAST               1 (p)
        # |                LOAD_GLOBAL              1 (len + NULL)
        # |                LOAD_FAST_BORROW         1 (p)
        # |                LOAD_ATTR                2 (text)
        # |                CALL                     1
        # |                LOAD_SMALL_INT         100
        # |                COMPARE_OP             172 (>=)
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           31 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti

