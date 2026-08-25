# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py
# 来源   : test_ingest.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '语料清洗与分章。\n\n样本刻意做成中文网络小说 txt 的真实样子：GB18030 编码、站点水印、\n混用的章节标记 —— 这三样是实际拿到书之后最先撞上的问题。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '语料清洗与分章。\n\n样本刻意做成中文网络小说 txt 的真实样子：GB18030 编码、站点水印、\n混用的章节标记 —— 这三样是实际拿到书之后最先撞上的问题。\n',
    4: '书名：伞的重量\n更新最快 www.example-novel.com 请收藏本站\n\n第一章 初遇\n\n那天下着雨,她站在图书馆门口。\n\n"你没带伞?"他问。\n\n第2章 旧照片\n\n她在社团旧相册里认出了他...什么也没说。\n\n最新章节请访问 example.com\n\n正文 第三章 雨停了\n\n雨停的时候,两个人都没有动。\n',
    6: 'TestEncoding',
    8: 'TestJunkRemoval',
    10: 'TestPunctuationNormalization',
    12: 'TestChapterSplitting',
    14: 'TestBook',
    16: 'TestHeadingPatternSelection',
    18: 'TestEpub',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('TestEncoding', 0): 'TestEncoding',
    ('TestEncoding', 1): 'encoding',
    ('test_decodes_common_chinese_encodings', 0): 'book.txt',
    ('test_decodes_common_chinese_encodings', 1): '伞的重量',
    ('test_decodes_common_chinese_encodings', 2): '�',
    ('test_decodes_common_chinese_encodings', 3): 'py3',
    ('test_decodes_common_chinese_encodings', 4): 'py5',
    ('test_decodes_common_chinese_encodings', 5): 'text',
    ('test_decodes_common_chinese_encodings', 6): '%(py7)s',
    ('test_decodes_common_chinese_encodings', 7): 'py7',
    ('test_decodes_common_chinese_encodings', 8): 'py10',
    ('test_decodes_common_chinese_encodings', 9): 'py12',
    ('test_decodes_common_chinese_encodings', 10): '%(py14)s',
    ('test_decodes_common_chinese_encodings', 11): 'py14',
    ('test_decodes_common_chinese_encodings', 12): ' 解码失败',
    ('test_decodes_common_chinese_encodings', 13): '\n>assert %(py17)s',
    ('test_decodes_common_chinese_encodings', 14): 'py17',
    ('test_decodes_common_chinese_encodings', 16): 'assert %(py0)s',
    ('test_decodes_common_chinese_encodings', 17): 'py0',
    ('test_decodes_common_chinese_encodings', 18): 'detected',
    ('test_undecodable_bytes_do_not_crash', 0): 'broken.txt',
    ('test_undecodable_bytes_do_not_crash', 2): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}',
    ('test_undecodable_bytes_do_not_crash', 3): 'py0',
    ('test_undecodable_bytes_do_not_crash', 4): 'isinstance',
    ('test_undecodable_bytes_do_not_crash', 5): 'py1',
    ('test_undecodable_bytes_do_not_crash', 6): 'text',
    ('test_undecodable_bytes_do_not_crash', 7): 'py2',
    ('test_undecodable_bytes_do_not_crash', 8): 'str',
    ('test_undecodable_bytes_do_not_crash', 9): 'py4',
    ('TestJunkRemoval', 0): 'TestJunkRemoval',
    ('TestJunkRemoval', 1): 'line',
    ('test_junk_detected', 1): 'assert %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}',
    ('test_junk_detected', 2): 'py0',
    ('test_junk_detected', 3): 'is_junk',
    ('test_junk_detected', 4): 'py1',
    ('test_junk_detected', 5): 'line',
    ('test_junk_detected', 6): 'py3',
    ('test_prose_kept', 1): 'assert not %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}',
    ('test_prose_kept', 2): 'py0',
    ('test_prose_kept', 3): 'is_junk',
    ('test_prose_kept', 4): 'py1',
    ('test_prose_kept', 5): 'line',
    ('test_prose_kept', 6): 'py3',
    ('test_long_line_with_url_kept', 0): '正文里提到网址不该被误删 —— 只有短水印行才判为广告。',
    ('test_long_line_with_url_kept', 1): '他把那个网址念了一遍，www.example.com，然后合上笔记本，说这是他大学四年唯一记住的东西。',
    ('test_long_line_with_url_kept', 2): 'assert not %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}',
    ('test_long_line_with_url_kept', 3): 'py0',
    ('test_long_line_with_url_kept', 4): 'is_junk',
    ('test_long_line_with_url_kept', 5): 'py1',
    ('test_long_line_with_url_kept', 6): 'para',
    ('test_long_line_with_url_kept', 7): 'py3',
    ('test_clean_reports_dropped_count', 1): 'py0',
    ('test_clean_reports_dropped_count', 2): 'dropped',
    ('test_clean_reports_dropped_count', 3): 'py3',
    ('test_clean_reports_dropped_count', 4): 'assert %(py5)s',
    ('test_clean_reports_dropped_count', 5): 'py5',
    ('TestPunctuationNormalization', 0): 'TestPunctuationNormalization',
    ('TestPunctuationNormalization', 1): 'src,expected',
    ('TestPunctuationNormalization', 4): 'src',
    ('test_normalized', 0): '==',
    ('test_normalized', 1): 'py0',
    ('test_normalized', 2): 'normalize_punctuation',
    ('test_normalized', 3): 'py1',
    ('test_normalized', 4): 'src',
    ('test_normalized', 5): 'py3',
    ('test_normalized', 6): 'py5',
    ('test_normalized', 7): 'expected',
    ('test_normalized', 8): 'assert %(py7)s',
    ('test_normalized', 9): 'py7',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 0): '==',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 1): 'py0',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 2): 'normalize_punctuation',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 3): 'py1',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 4): 'src',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 5): 'py3',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 6): 'py5',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 7): 'expected',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 8): 'assert %(py7)s',
    ('test_halfwidth_near_cjk_becomes_fullwidth', 9): 'py7',
    ('test_halfwidth_in_numbers_and_latin_preserved', 0): '"3.5" "Wi-Fi" 里的半角符号是合法的，不能误伤。',
    ('test_halfwidth_in_numbers_and_latin_preserved', 1): 'py0',
    ('test_halfwidth_in_numbers_and_latin_preserved', 2): 'normalize_punctuation',
    ('test_halfwidth_in_numbers_and_latin_preserved', 3): 'py1',
    ('test_halfwidth_in_numbers_and_latin_preserved', 4): 'src',
    ('test_halfwidth_in_numbers_and_latin_preserved', 5): 'py3',
    ('test_halfwidth_in_numbers_and_latin_preserved', 6): 'py5',
    ('test_halfwidth_in_numbers_and_latin_preserved', 7): 'assert %(py7)s',
    ('test_halfwidth_in_numbers_and_latin_preserved', 8): 'py7',
    ('test_already_correct_unchanged', 0): '她想说什么，最终只是摇头——那句话到底没有出口……',
    ('test_already_correct_unchanged', 1): 'py0',
    ('test_already_correct_unchanged', 2): 'normalize_punctuation',
    ('test_already_correct_unchanged', 3): 'py1',
    ('test_already_correct_unchanged', 4): 'good',
    ('test_already_correct_unchanged', 5): 'py3',
    ('test_already_correct_unchanged', 6): 'py5',
    ('test_already_correct_unchanged', 7): 'assert %(py7)s',
    ('test_already_correct_unchanged', 8): 'py7',
    ('TestChapterSplitting', 0): 'TestChapterSplitting',
    ('test_mixed_heading_formats_all_found', 1): 'py0',
    ('test_mixed_heading_formats_all_found', 2): 'len',
    ('test_mixed_heading_formats_all_found', 3): 'py1',
    ('test_mixed_heading_formats_all_found', 4): 'chapters',
    ('test_mixed_heading_formats_all_found', 5): 'py3',
    ('test_mixed_heading_formats_all_found', 6): 'py6',
    ('test_mixed_heading_formats_all_found', 7): '\n>assert %(py8)s',
    ('test_mixed_heading_formats_all_found', 8): 'py8',
    ('test_mixed_heading_formats_all_found', 10): 'py4',
    ('test_mixed_heading_formats_all_found', 11): 'assert %(py6)s',
    ('test_chapters_renumbered_sequentially', 1): 'py1',
    ('test_chapters_renumbered_sequentially', 2): 'py4',
    ('test_chapters_renumbered_sequentially', 3): 'assert %(py6)s',
    ('test_chapters_renumbered_sequentially', 4): 'py6',
    ('test_heading_not_included_in_body', 0): '第一章',
    ('test_heading_not_included_in_body', 1): 'py1',
    ('test_heading_not_included_in_body', 2): 'py4',
    ('test_heading_not_included_in_body', 3): 'py6',
    ('test_heading_not_included_in_body', 4): 'assert %(py8)s',
    ('test_heading_not_included_in_body', 5): 'py8',
    ('test_junk_already_gone_from_body', 1): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_junk_already_gone_from_body', 2): 'py0',
    ('test_junk_already_gone_from_body', 3): 'all',
    ('test_junk_already_gone_from_body', 4): 'py2',
    ('test_junk_already_gone_from_body', 5): 'py4',
    ('<genexpr>', 0): 'example.com',
    ('test_no_headings_yields_single_chapter', 0): '就是一段没有任何章节标记的散文。\n\n第二段。',
    ('test_no_headings_yields_single_chapter', 1): '全文',
    ('test_no_headings_yields_single_chapter', 2): 'py2',
    ('test_no_headings_yields_single_chapter', 3): 'len',
    ('test_no_headings_yields_single_chapter', 4): 'py3',
    ('test_no_headings_yields_single_chapter', 5): 'chapters',
    ('test_no_headings_yields_single_chapter', 6): 'py5',
    ('test_no_headings_yields_single_chapter', 7): 'py8',
    ('test_no_headings_yields_single_chapter', 8): '%(py10)s',
    ('test_no_headings_yields_single_chapter', 9): 'py10',
    ('test_no_headings_yields_single_chapter', 10): 'py13',
    ('test_no_headings_yields_single_chapter', 11): 'py15',
    ('test_no_headings_yields_single_chapter', 12): 'py18',
    ('test_no_headings_yields_single_chapter', 13): '%(py20)s',
    ('test_no_headings_yields_single_chapter', 14): 'py20',
    ('test_no_headings_yields_single_chapter', 15): 'assert %(py23)s',
    ('test_no_headings_yields_single_chapter', 16): 'py23',
    ('test_empty_input', 1): 'py0',
    ('test_empty_input', 2): 'split_chapters',
    ('test_empty_input', 3): 'py2',
    ('test_empty_input', 4): 'py4',
    ('test_empty_input', 5): 'py7',
    ('test_empty_input', 6): 'assert %(py9)s',
    ('test_empty_input', 7): 'py9',
    ('TestBook', 0): 'TestBook',
    ('test_ingest_file', 0): '伞的重量.txt',
    ('test_ingest_file', 1): 'gb18030',
    ('test_ingest_file', 2): '伞的重量',
    ('test_ingest_file', 3): 'py0',
    ('test_ingest_file', 4): 'book',
    ('test_ingest_file', 5): 'py2',
    ('test_ingest_file', 6): 'py5',
    ('test_ingest_file', 7): 'assert %(py7)s',
    ('test_ingest_file', 8): 'py7',
    ('test_ingest_file', 10): 'len',
    ('test_ingest_file', 11): 'py1',
    ('test_ingest_file', 12): 'py3',
    ('test_ingest_file', 13): 'py8',
    ('test_ingest_file', 14): 'assert %(py10)s',
    ('test_ingest_file', 15): 'py10',
    ('test_ingest_dir_writes_markdown', 0): 'raw',
    ('test_ingest_dir_writes_markdown', 1): 'clean',
    ('test_ingest_dir_writes_markdown', 2): 'a.txt',
    ('test_ingest_dir_writes_markdown', 3): 'utf-8',
    ('test_ingest_dir_writes_markdown', 4): 'b.txt',
    ('test_ingest_dir_writes_markdown', 5): 'gb18030',
    ('test_ingest_dir_writes_markdown', 6): 'py0',
    ('test_ingest_dir_writes_markdown', 7): 'len',
    ('test_ingest_dir_writes_markdown', 8): 'py1',
    ('test_ingest_dir_writes_markdown', 9): 'books',
    ('test_ingest_dir_writes_markdown', 10): 'py3',
    ('test_ingest_dir_writes_markdown', 11): 'py6',
    ('test_ingest_dir_writes_markdown', 12): 'assert %(py8)s',
    ('test_ingest_dir_writes_markdown', 13): 'py8',
    ('test_ingest_dir_writes_markdown', 15): 'a.md',
    ('test_ingest_dir_writes_markdown', 16): '# a',
    ('test_ingest_dir_writes_markdown', 17): '## 第1章 初遇',
    ('test_ingest_dir_writes_markdown', 18): '%(py8)s\n{%(py8)s = %(py4)s\n{%(py4)s = %(py2)s.startswith\n}(%(py6)s)\n}',
    ('test_ingest_dir_writes_markdown', 19): 'py2',
    ('test_ingest_dir_writes_markdown', 20): 'out',
    ('test_ingest_dir_writes_markdown', 21): 'py4',
    ('test_ingest_dir_writes_markdown', 22): 'py11',
    ('test_ingest_dir_writes_markdown', 23): 'py13',
    ('test_ingest_dir_writes_markdown', 24): '%(py15)s',
    ('test_ingest_dir_writes_markdown', 25): 'py15',
    ('test_ingest_dir_writes_markdown', 26): 'assert %(py18)s',
    ('test_ingest_dir_writes_markdown', 27): 'py18',
    ('test_chapter_markdown_matches_gate_title_format', 0): '清洗产物的标题格式要与 gate 的硬规范一致，否则语料没法当样本用。',
    ('test_chapter_markdown_matches_gate_title_format', 3): 'config',
    ('test_chapter_markdown_matches_gate_title_format', 4): 'project.yaml',
    ('test_chapter_markdown_matches_gate_title_format', 5): 'utf-8',
    ('test_chapter_markdown_matches_gate_title_format', 6): 'format',
    ('test_chapter_markdown_matches_gate_title_format', 7): 'chapter_title_pattern',
    ('test_chapter_markdown_matches_gate_title_format', 8): '初遇',
    ('test_chapter_markdown_matches_gate_title_format', 9): '正文。',
    ('test_chapter_markdown_matches_gate_title_format', 10): 'assert %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py3)s, %(py5)s)\n}',
    ('test_chapter_markdown_matches_gate_title_format', 11): 'py0',
    ('test_chapter_markdown_matches_gate_title_format', 12): 're',
    ('test_chapter_markdown_matches_gate_title_format', 13): 'py2',
    ('test_chapter_markdown_matches_gate_title_format', 14): 'py3',
    ('test_chapter_markdown_matches_gate_title_format', 15): 'pattern',
    ('test_chapter_markdown_matches_gate_title_format', 16): 'py5',
    ('test_chapter_markdown_matches_gate_title_format', 17): 'py7',
    ('TestHeadingPatternSelection', 0): 'TestHeadingPatternSelection',
    ('TestHeadingPatternSelection', 1): '模式之间存在包含关系（"第N章" ⊂ "第N"），按命中数取胜会让宽松模式\n永远赢，把「章」字留在标题里。实测 66 本语料暴露的问题。',
    ('TestHeadingPatternSelection', 5): 'title,ok',
    ('test_specific_pattern_beats_looser_one', 0): '真章节 + 大量正文噪声时，仍要选中 第N章。',
    ('test_specific_pattern_beats_looser_one', 2): '第',
    ('test_specific_pattern_beats_looser_one', 3): '章 标题',
    ('test_specific_pattern_beats_looser_one', 5): '第N章',
    ('test_specific_pattern_beats_looser_one', 6): 'py0',
    ('test_specific_pattern_beats_looser_one', 7): 'self',
    ('test_specific_pattern_beats_looser_one', 8): 'py2',
    ('test_specific_pattern_beats_looser_one', 9): 'py3',
    ('test_specific_pattern_beats_looser_one', 10): 'body',
    ('test_specific_pattern_beats_looser_one', 11): 'py5',
    ('test_specific_pattern_beats_looser_one', 12): 'py7',
    ('test_specific_pattern_beats_looser_one', 13): 'noise',
    ('test_specific_pattern_beats_looser_one', 14): 'py10',
    ('test_specific_pattern_beats_looser_one', 15): 'py13',
    ('test_specific_pattern_beats_looser_one', 16): 'assert %(py15)s',
    ('test_specific_pattern_beats_looser_one', 17): 'py15',
    ('test_specific_pattern_beats_looser_one', 19): '正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n',
    ('<genexpr>', 0): '第',
    ('<genexpr>', 1): '页',
    ('test_counter_words_not_treated_as_chapters', 2): '第N',
    ('test_counter_words_not_treated_as_chapters', 3): ' 不该被当成章节标记',
    ('test_counter_words_not_treated_as_chapters', 4): '\n>assert not %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py3)s)\n}',
    ('test_counter_words_not_treated_as_chapters', 5): 'py0',
    ('test_counter_words_not_treated_as_chapters', 6): 'bare',
    ('test_counter_words_not_treated_as_chapters', 7): 'py2',
    ('test_counter_words_not_treated_as_chapters', 8): 'py3',
    ('test_counter_words_not_treated_as_chapters', 9): 'counter',
    ('test_counter_words_not_treated_as_chapters', 10): 'py5',
    ('test_counter_words_not_treated_as_chapters', 12): '第1 楔子',
    ('test_counter_words_not_treated_as_chapters', 13): '真正的无「章」标记要能匹配',
    ('test_counter_words_not_treated_as_chapters', 14): '\n>assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py4)s)\n}',
    ('test_counter_words_not_treated_as_chapters', 15): 'py4',
    ('test_counter_words_not_treated_as_chapters', 16): 'py6',
    ('test_title_plausibility', 0): '正文行会被宽松模式误判成标题，句末标点是最可靠的区分点。\n但逗号和省略号常见于真标题，不能一起排除。',
    ('test_title_plausibility', 2): 'py0',
    ('test_title_plausibility', 3): 'is_plausible_title',
    ('test_title_plausibility', 4): 'py1',
    ('test_title_plausibility', 5): 'title',
    ('test_title_plausibility', 6): 'py3',
    ('test_title_plausibility', 7): 'py5',
    ('test_title_plausibility', 8): 'ok',
    ('test_title_plausibility', 9): 'assert %(py7)s',
    ('test_title_plausibility', 10): 'py7',
    ('TestEpub', 0): 'TestEpub',
    ('_make_epub', 2): 'w',
    ('_make_epub', 3): 'META-INF/container.xml',
    ('_make_epub', 4): '<?xml version="1.0"?><container xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf"/></rootfiles></container>',
    ('_make_epub', 5): 'c',
    ('_make_epub', 6): '.xhtml',
    ('_make_epub', 9): 'OEBPS/',
    ('_make_epub', 10): '<html><body><h1>第',
    ('_make_epub', 11): '章 ',
    ('_make_epub', 12): '</h1>',
    ('_make_epub', 13): '</body></html>',
    ('_make_epub', 14): '<item id="i',
    ('_make_epub', 15): '" href="',
    ('_make_epub', 16): '" media-type="application/xhtml+xml"/>',
    ('_make_epub', 17): '<itemref idref="i',
    ('_make_epub', 18): '"/>',
    ('_make_epub', 19): 'OEBPS/content.opf',
    ('_make_epub', 20): '<?xml version="1.0"?><package xmlns="http://www.idpf.org/2007/opf"><manifest>',
    ('_make_epub', 21): '</manifest><spine>',
    ('_make_epub', 22): '</spine></package>',
    ('<genexpr>', 0): '<p>',
    ('<genexpr>', 1): '第',
    ('<genexpr>', 2): '段。</p>',
    ('test_reads_epub_in_spine_order', 2): 'book.epub',
    ('test_reads_epub_in_spine_order', 3): '初遇',
    ('test_reads_epub_in_spine_order', 4): '第一章的正文。',
    ('test_reads_epub_in_spine_order', 5): '重逢',
    ('test_reads_epub_in_spine_order', 6): 'epub',
    ('test_reads_epub_in_spine_order', 7): 'py0',
    ('test_reads_epub_in_spine_order', 8): 'book',
    ('test_reads_epub_in_spine_order', 9): 'py2',
    ('test_reads_epub_in_spine_order', 10): 'py5',
    ('test_reads_epub_in_spine_order', 11): 'assert %(py7)s',
    ('test_reads_epub_in_spine_order', 12): 'py7',
    ('test_reads_epub_in_spine_order', 14): 'py1',
    ('test_reads_epub_in_spine_order', 15): 'py4',
    ('test_reads_epub_in_spine_order', 16): 'assert %(py6)s',
    ('test_reads_epub_in_spine_order', 17): 'py6',
    ('test_reads_epub_in_spine_order', 18): 'assert %(py8)s',
    ('test_reads_epub_in_spine_order', 19): 'py8',
    ('test_html_tags_stripped', 2): 'b.epub',
    ('test_html_tags_stripped', 5): '<em>',
    ('test_html_tags_stripped', 6): '强调',
    ('test_html_tags_stripped', 7): '&',
    ('test_html_tags_stripped', 8): 'py3',
    ('test_html_tags_stripped', 9): 'py5',
    ('test_html_tags_stripped', 10): 'body',
    ('test_html_tags_stripped', 11): '%(py7)s',
    ('test_html_tags_stripped', 12): 'py7',
    ('test_html_tags_stripped', 13): 'py10',
    ('test_html_tags_stripped', 14): 'py12',
    ('test_html_tags_stripped', 15): '%(py14)s',
    ('test_html_tags_stripped', 16): 'py14',
    ('test_html_tags_stripped', 17): 'py17',
    ('test_html_tags_stripped', 18): 'py19',
    ('test_html_tags_stripped', 19): '%(py21)s',
    ('test_html_tags_stripped', 20): 'py21',
    ('test_html_tags_stripped', 21): 'assert %(py24)s',
    ('test_html_tags_stripped', 22): 'py24',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
class TestEncoding:
    'TestEncoding'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  37           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestEncoding')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          37
    # |               STORE_NAME               3 (__firstlineno__)
    # |  38           LOAD_NAME                4 (pytest)
    # |               LOAD_ATTR               10 (mark)
    # |               LOAD_ATTR               13 (parametrize + NULL|self)
    # |               LOAD_CONST               1 ('encoding')
    # |               BUILD_LIST               0
    # |               LOAD_CONST               6 (('utf-8', 'gb18030', 'utf-8-sig'))
    # |               LIST_EXTEND              1
    # |               CALL                     2
    # |  39           LOAD_CONST               2 (<code object test_decodes_common_chinese_encodings at 0x75bd2c1800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 38>)
    # |               MAKE_FUNCTION
    # |  38           CALL                     0
    # |  39           STORE_NAME               7 (test_decodes_common_chinese_encodings)
    # |  46           LOAD_CONST               3 (<code object test_undecodable_bytes_do_not_crash at 0x75bcd95c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 46>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_undecodable_bytes_do_not_crash)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               9 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_decodes_common_chinese_encodings at 0x75bd2c1800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 38>:
    # |  38            RESUME                   0
    # |  40            LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               0 ('book.txt')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               3 (f)
    # |  41            LOAD_FAST_BORROW         3 (f)
    # |                LOAD_ATTR                1 (write_bytes + NULL|self)
    # |                LOAD_GLOBAL              2 (RAW)
    # |                LOAD_ATTR                5 (encode + NULL|self)
    # |                LOAD_FAST_BORROW         2 (encoding)
    # |                CALL                     1
    # |                CALL                     1
    # |                POP_TOP
    # |  42            LOAD_GLOBAL              7 (read_text + NULL)
    # |                LOAD_FAST_BORROW         3 (f)
    # |                CALL                     1
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   69 (text, detected)
    # |  43            BUILD_LIST               0
    # |                STORE_FAST               6 (@py_assert1)
    # |                LOAD_CONST               1 ('伞的重量')
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         4 (text)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
    # |                STORE_FAST_LOAD_FAST   152 (@py_assert0, @py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        8 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_CONST               2 ('�')
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
    # |                LOAD_FAST_BORROW         4 (text)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert11, @py_assert11)
    # |                STORE_FAST               9 (@py_assert0)
    # |        L1:     LOAD_FAST_BORROW         9 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       434 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('in',))
    # |                LOAD_FAST_BORROW         8 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py3)s in %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (@py_assert2, text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py3')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py5')
    # |                LOAD_CONST               5 ('text')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST               5 ('text')
    # |        L4:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format6)
    # |                LOAD_CONST               6 ('%(py7)s')
    # |                LOAD_CONST               7 ('py7')
    # |                LOAD_FAST_BORROW        12 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   214 (@py_format8, @py_assert1)
    # |                LOAD_ATTR               21 (append + NULL|self)
    # |                LOAD_FAST_BORROW        13 (@py_format8)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW         8 (@py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      163 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              21 (('not in',))
    # |                LOAD_FAST_CHECK         11 (@py_assert11)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              22 (('%(py10)s not in %(py12)s',))
    # |                LOAD_FAST_CHECK         10 (@py_assert9)
    # |                LOAD_FAST_BORROW         4 (text)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py10')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py12')
    # |                LOAD_CONST               5 ('text')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               5 ('text')
    # |        L7:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format13)
    # |                LOAD_CONST              10 ('%(py14)s')
    # |                LOAD_CONST              11 ('py14')
    # |                LOAD_FAST_BORROW        14 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   246 (@py_format15, @py_assert1)
    # |                LOAD_ATTR               21 (append + NULL|self)
    # |                LOAD_FAST_BORROW        15 (@py_format15)
    # |                CALL                     1
    # |                POP_TOP
    # |        L8:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format16)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (encoding)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              12 (' 解码失败')
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                LOAD_CONST              13 ('\n>assert %(py17)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              14 ('py17')
    # |                LOAD_FAST_BORROW        16 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format18)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        17 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L9:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  171 (@py_assert9, @py_assert11)
    # |  44            LOAD_FAST_BORROW         5 (detected)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       119 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_CONST              16 ('assert %(py0)s')
    # |                LOAD_CONST              17 ('py0')
    # |                LOAD_CONST              18 ('detected')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (detected)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (detected)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST              18 ('detected')
    # |       L12:     BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format1)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        18 (@py_format1)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L13:     LOAD_CONST              15 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_undecodable_bytes_do_not_crash at 0x75bcd95c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 46>:
    # |  46            RESUME                   0
    # |  47            LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               0 ('broken.txt')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               2 (f)
    # |  48            LOAD_FAST_BORROW         2 (f)
    # |                LOAD_ATTR                1 (write_bytes + NULL|self)
    # |                LOAD_CONST               1 (b'\xff\xfe\x00broken\x00\xff')
    # |                CALL                     1
    # |                POP_TOP
    # |  49            LOAD_GLOBAL              3 (read_text + NULL)
    # |                LOAD_FAST_BORROW         2 (f)
    # |                CALL                     1
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   52 (text, _)
    # |  50            LOAD_GLOBAL              5 (isinstance + NULL)
    # |                LOAD_FAST_BORROW         3 (text)
    # |                LOAD_GLOBAL              6 (str)
    # |                CALL                     2
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       313 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_CONST               2 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}')
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('isinstance')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (isinstance)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (isinstance)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('isinstance')
    # |        L3:     LOAD_CONST               5 ('py1')
    # |                LOAD_CONST               6 ('text')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               6 ('text')
    # |        L6:     LOAD_CONST               7 ('py2')
    # |                LOAD_CONST               8 ('str')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (str)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (str)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               8 ('str')
    # |        L9:     LOAD_CONST               9 ('py4')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format5)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format5)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              10 (None)
    # |                STORE_FAST               5 (@py_assert3)
    # |                LOAD_CONST              10 (None)
    # |                RETURN_VALUE

    def test_decodes_common_chinese_encodings(self, tmp_path, encoding):
        'book.txt'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  38            RESUME                   0
        # |  40            LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               0 ('book.txt')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               3 (f)
        # |  41            LOAD_FAST_BORROW         3 (f)
        # |                LOAD_ATTR                1 (write_bytes + NULL|self)
        # |                LOAD_GLOBAL              2 (RAW)
        # |                LOAD_ATTR                5 (encode + NULL|self)
        # |                LOAD_FAST_BORROW         2 (encoding)
        # |                CALL                     1
        # |                CALL                     1
        # |                POP_TOP
        # |  42            LOAD_GLOBAL              7 (read_text + NULL)
        # |                LOAD_FAST_BORROW         3 (f)
        # |                CALL                     1
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   69 (text, detected)
        # |  43            BUILD_LIST               0
        # |                STORE_FAST               6 (@py_assert1)
        # |                LOAD_CONST               1 ('伞的重量')
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         4 (text)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert4, @py_assert4)
        # |                STORE_FAST_LOAD_FAST   152 (@py_assert0, @py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE        8 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_CONST               2 ('�')
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert9, @py_assert9)
        # |                LOAD_FAST_BORROW         4 (text)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert11, @py_assert11)
        # |                STORE_FAST               9 (@py_assert0)
        # |        L1:     LOAD_FAST_BORROW         9 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       434 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('in',))
        # |                LOAD_FAST_BORROW         8 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py3)s in %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 116 (@py_assert2, text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py3')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py5')
        # |                LOAD_CONST               5 ('text')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST               5 ('text')
        # |        L4:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format6)
        # |                LOAD_CONST               6 ('%(py7)s')
        # |                LOAD_CONST               7 ('py7')
        # |                LOAD_FAST_BORROW        12 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   214 (@py_format8, @py_assert1)
        # |                LOAD_ATTR               21 (append + NULL|self)
        # |                LOAD_FAST_BORROW        13 (@py_format8)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW         8 (@py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      163 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              21 (('not in',))
        # |                LOAD_FAST_CHECK         11 (@py_assert11)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              22 (('%(py10)s not in %(py12)s',))
        # |                LOAD_FAST_CHECK         10 (@py_assert9)
        # |                LOAD_FAST_BORROW         4 (text)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py10')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert9)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py12')
        # |                LOAD_CONST               5 ('text')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               5 ('text')
        # |        L7:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format13)
        # |                LOAD_CONST              10 ('%(py14)s')
        # |                LOAD_CONST              11 ('py14')
        # |                LOAD_FAST_BORROW        14 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   246 (@py_format15, @py_assert1)
        # |                LOAD_ATTR               21 (append + NULL|self)
        # |                LOAD_FAST_BORROW        15 (@py_format15)
        # |                CALL                     1
        # |                POP_TOP
        # |        L8:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format16)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (encoding)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              12 (' 解码失败')
        # |                BUILD_STRING             2
        # |                CALL                     1
        # |                LOAD_CONST              13 ('\n>assert %(py17)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              14 ('py17')
        # |                LOAD_FAST_BORROW        16 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format18)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        17 (@py_format18)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L9:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  171 (@py_assert9, @py_assert11)
        # |  44            LOAD_FAST_BORROW         5 (detected)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       119 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_CONST              16 ('assert %(py0)s')
        # |                LOAD_CONST              17 ('py0')
        # |                LOAD_CONST              18 ('detected')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (detected)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (detected)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST              18 ('detected')
        # |       L12:     BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format1)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        18 (@py_format1)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L13:     LOAD_CONST              15 (None)
        # |                RETURN_VALUE

    def test_undecodable_bytes_do_not_crash(self, tmp_path):
        'broken.txt'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  46            RESUME                   0
        # |  47            LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               0 ('broken.txt')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               2 (f)
        # |  48            LOAD_FAST_BORROW         2 (f)
        # |                LOAD_ATTR                1 (write_bytes + NULL|self)
        # |                LOAD_CONST               1 (b'\xff\xfe\x00broken\x00\xff')
        # |                CALL                     1
        # |                POP_TOP
        # |  49            LOAD_GLOBAL              3 (read_text + NULL)
        # |                LOAD_FAST_BORROW         2 (f)
        # |                CALL                     1
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   52 (text, _)
        # |  50            LOAD_GLOBAL              5 (isinstance + NULL)
        # |                LOAD_FAST_BORROW         3 (text)
        # |                LOAD_GLOBAL              6 (str)
        # |                CALL                     2
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       313 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_CONST               2 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py1)s, %(py2)s)\n}')
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('isinstance')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (isinstance)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (isinstance)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('isinstance')
        # |        L3:     LOAD_CONST               5 ('py1')
        # |                LOAD_CONST               6 ('text')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               6 ('text')
        # |        L6:     LOAD_CONST               7 ('py2')
        # |                LOAD_CONST               8 ('str')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (str)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (str)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               8 ('str')
        # |        L9:     LOAD_CONST               9 ('py4')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format5)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format5)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              10 (None)
        # |                STORE_FAST               5 (@py_assert3)
        # |                LOAD_CONST              10 (None)
        # |                RETURN_VALUE


class TestJunkRemoval:
    'TestJunkRemoval'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  53           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestJunkRemoval')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          53
    # |               STORE_NAME               3 (__firstlineno__)
    # |  54           LOAD_NAME                4 (pytest)
    # |               LOAD_ATTR               10 (mark)
    # |               LOAD_ATTR               13 (parametrize + NULL|self)
    # |  55           LOAD_CONST               1 ('line')
    # |  56           BUILD_LIST               0
    # |               LOAD_CONST               8 (('更新最快 www.example.com', '请收藏本站', '最新章节请访问 example.com', '手机阅读 m.example.net', '========'))
    # |               LIST_EXTEND              1
    # |  54           CALL                     2
    # |  59           LOAD_CONST               2 (<code object test_junk_detected at 0x75bd2f7300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 54>)
    # |               MAKE_FUNCTION
    # |  54           CALL                     0
    # |  59           STORE_NAME               7 (test_junk_detected)
    # |  62           LOAD_NAME                4 (pytest)
    # |               LOAD_ATTR               10 (mark)
    # |               LOAD_ATTR               13 (parametrize + NULL|self)
    # |  63           LOAD_CONST               1 ('line')
    # |  64           BUILD_LIST               0
    # |               LOAD_CONST               9 (('那天下着雨，她站在图书馆门口。', '“你没带伞？”他问。', ''))
    # |               LIST_EXTEND              1
    # |  62           CALL                     2
    # |  66           LOAD_CONST               3 (<code object test_prose_kept at 0x75bd2f7600, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 62>)
    # |               MAKE_FUNCTION
    # |  62           CALL                     0
    # |  66           STORE_NAME               8 (test_prose_kept)
    # |  69           LOAD_CONST               4 (<code object test_long_line_with_url_kept at 0x75bd2f7900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 69>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_long_line_with_url_kept)
    # |  74           LOAD_CONST               5 (<code object test_clean_reports_dropped_count at 0x75bcd52080, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 74>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_clean_reports_dropped_count)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME              11 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_junk_detected at 0x75bd2f7300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 54>:
    # |  54           RESUME                   0
    # |  60           LOAD_GLOBAL              1 (is_junk + NULL)
    # |               LOAD_FAST_BORROW         1 (line)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       227 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('assert %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}')
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('is_junk')
    # |               LOAD_GLOBAL              2 (@py_builtins)
    # |               LOAD_ATTR                4 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (is_junk)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (is_junk)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('is_junk')
    # |       L3:     LOAD_CONST               4 ('py1')
    # |               LOAD_CONST               5 ('line')
    # |               LOAD_GLOBAL              2 (@py_builtins)
    # |               LOAD_ATTR                4 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (line)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (line)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               5 ('line')
    # |       L6:     LOAD_CONST               6 ('py3')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert2)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               3 (@py_format4)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_format4)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST               7 (None)
    # |               STORE_FAST               2 (@py_assert2)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_prose_kept at 0x75bd2f7600, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 62>:
    # |  62           RESUME                   0
    # |  67           LOAD_GLOBAL              1 (is_junk + NULL)
    # |               LOAD_FAST_BORROW         1 (line)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       227 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('assert not %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}')
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('is_junk')
    # |               LOAD_GLOBAL              2 (@py_builtins)
    # |               LOAD_ATTR                4 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (is_junk)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (is_junk)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('is_junk')
    # |       L3:     LOAD_CONST               4 ('py1')
    # |               LOAD_CONST               5 ('line')
    # |               LOAD_GLOBAL              2 (@py_builtins)
    # |               LOAD_ATTR                4 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (line)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (line)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               5 ('line')
    # |       L6:     LOAD_CONST               6 ('py3')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert2)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               4 (@py_format5)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST               7 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   35 (@py_assert2, @py_assert4)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_long_line_with_url_kept at 0x75bd2f7900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 69>:
    # |  69           RESUME                   0
    # |  71           LOAD_CONST               1 ('他把那个网址念了一遍，www.example.com，然后合上笔记本，说这是他大学四年唯一记住的东西。')
    # |               STORE_FAST               1 (para)
    # |  72           LOAD_GLOBAL              1 (is_junk + NULL)
    # |               LOAD_FAST_BORROW         1 (para)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       227 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_CONST               2 ('assert not %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}')
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('is_junk')
    # |               LOAD_GLOBAL              2 (@py_builtins)
    # |               LOAD_ATTR                4 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (is_junk)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (is_junk)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('is_junk')
    # |       L3:     LOAD_CONST               5 ('py1')
    # |               LOAD_CONST               6 ('para')
    # |               LOAD_GLOBAL              2 (@py_builtins)
    # |               LOAD_ATTR                4 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (para)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (para)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               6 ('para')
    # |       L6:     LOAD_CONST               7 ('py3')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert2)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               4 (@py_format5)
    # |               LOAD_GLOBAL             13 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   35 (@py_assert2, @py_assert4)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_clean_reports_dropped_count at 0x75bcd52080, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 74>:
    # |  74           RESUME                   0
    # |  75           LOAD_GLOBAL              1 (clean + NULL)
    # |               LOAD_GLOBAL              2 (RAW)
    # |               CALL                     1
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   18 (_, dropped)
    # |  76           LOAD_SMALL_INT           2
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert2, dropped)
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       177 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               7 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               8 (('%(py0)s == %(py3)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (dropped, @py_assert2)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py0')
    # |               LOAD_CONST               2 ('dropped')
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
    # |               LOAD_FAST_BORROW         2 (dropped)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (dropped)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('dropped')
    # |       L3:     LOAD_CONST               3 ('py3')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert2)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format4)
    # |               LOAD_CONST               4 ('assert %(py5)s')
    # |               LOAD_CONST               5 ('py5')
    # |               LOAD_FAST_BORROW         5 (@py_format4)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert1, @py_assert2)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE

    def test_junk_detected(self, line):
        'assert %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  54           RESUME                   0
        # |  60           LOAD_GLOBAL              1 (is_junk + NULL)
        # |               LOAD_FAST_BORROW         1 (line)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       227 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('assert %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}')
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('is_junk')
        # |               LOAD_GLOBAL              2 (@py_builtins)
        # |               LOAD_ATTR                4 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (is_junk)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (is_junk)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('is_junk')
        # |       L3:     LOAD_CONST               4 ('py1')
        # |               LOAD_CONST               5 ('line')
        # |               LOAD_GLOBAL              2 (@py_builtins)
        # |               LOAD_ATTR                4 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (line)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (line)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               5 ('line')
        # |       L6:     LOAD_CONST               6 ('py3')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert2)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               3 (@py_format4)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_format4)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST               7 (None)
        # |               STORE_FAST               2 (@py_assert2)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_prose_kept(self, line):
        'assert not %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  62           RESUME                   0
        # |  67           LOAD_GLOBAL              1 (is_junk + NULL)
        # |               LOAD_FAST_BORROW         1 (line)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       227 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('assert not %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}')
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('is_junk')
        # |               LOAD_GLOBAL              2 (@py_builtins)
        # |               LOAD_ATTR                4 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (is_junk)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (is_junk)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('is_junk')
        # |       L3:     LOAD_CONST               4 ('py1')
        # |               LOAD_CONST               5 ('line')
        # |               LOAD_GLOBAL              2 (@py_builtins)
        # |               LOAD_ATTR                4 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (line)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (line)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               5 ('line')
        # |       L6:     LOAD_CONST               6 ('py3')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert2)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               4 (@py_format5)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST               7 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   35 (@py_assert2, @py_assert4)
        # |               LOAD_CONST               7 (None)
        # |               RETURN_VALUE

    def test_long_line_with_url_kept(self):
        '正文里提到网址不该被误删 —— 只有短水印行才判为广告。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  69           RESUME                   0
        # |  71           LOAD_CONST               1 ('他把那个网址念了一遍，www.example.com，然后合上笔记本，说这是他大学四年唯一记住的东西。')
        # |               STORE_FAST               1 (para)
        # |  72           LOAD_GLOBAL              1 (is_junk + NULL)
        # |               LOAD_FAST_BORROW         1 (para)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       227 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_CONST               2 ('assert not %(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n}')
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('is_junk')
        # |               LOAD_GLOBAL              2 (@py_builtins)
        # |               LOAD_ATTR                4 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (is_junk)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (is_junk)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('is_junk')
        # |       L3:     LOAD_CONST               5 ('py1')
        # |               LOAD_CONST               6 ('para')
        # |               LOAD_GLOBAL              2 (@py_builtins)
        # |               LOAD_ATTR                4 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (para)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (para)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               6 ('para')
        # |       L6:     LOAD_CONST               7 ('py3')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert2)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               4 (@py_format5)
        # |               LOAD_GLOBAL             13 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   35 (@py_assert2, @py_assert4)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE

    def test_clean_reports_dropped_count(self):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  74           RESUME                   0
        # |  75           LOAD_GLOBAL              1 (clean + NULL)
        # |               LOAD_GLOBAL              2 (RAW)
        # |               CALL                     1
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   18 (_, dropped)
        # |  76           LOAD_SMALL_INT           2
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert2, dropped)
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       177 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               7 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               8 (('%(py0)s == %(py3)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (dropped, @py_assert2)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py0')
        # |               LOAD_CONST               2 ('dropped')
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
        # |               LOAD_FAST_BORROW         2 (dropped)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (dropped)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('dropped')
        # |       L3:     LOAD_CONST               3 ('py3')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert2)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format4)
        # |               LOAD_CONST               4 ('assert %(py5)s')
        # |               LOAD_CONST               5 ('py5')
        # |               LOAD_FAST_BORROW         5 (@py_format4)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert1, @py_assert2)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE


class TestPunctuationNormalization:
    'TestPunctuationNormalization'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  79           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestPunctuationNormalization')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          79
    # |               STORE_NAME               3 (__firstlineno__)
    # |  80           LOAD_NAME                4 (pytest)
    # |               LOAD_ATTR               10 (mark)
    # |               LOAD_ATTR               13 (parametrize + NULL|self)
    # |  81           LOAD_CONST               1 ('src,expected')
    # |  82           BUILD_LIST               0
    # |               LOAD_CONST               9 ((('什么也没说...', '什么也没说……'), ('什么也没说。。。', '什么也没说……'), ('她开口--声音很轻', '她开口——声音很轻'), ('她开口—声音很轻', '她开口——声音很轻'), ('他愣住了…', '他愣住了……')))
    # |               LIST_EXTEND              1
    # |  80           CALL                     2
    # |  86           LOAD_CONST               2 (<code object test_normalized at 0x75bcd96000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 80>)
    # |               MAKE_FUNCTION
    # |  80           CALL                     0
    # |  86           STORE_NAME               7 (test_normalized)
    # |  89           LOAD_NAME                4 (pytest)
    # |               LOAD_ATTR               10 (mark)
    # |               LOAD_ATTR               13 (parametrize + NULL|self)
    # |  90           LOAD_CONST               1 ('src,expected')
    # |  91           BUILD_LIST               0
    # |               LOAD_CONST              10 ((('那天下着雨,她站在门口。', '那天下着雨，她站在门口。'), ('“你没带伞?”他问。', '“你没带伞？”他问。'), ('他喊了一声!没人应。', '他喊了一声！没人应。'), ('她说:算了。', '她说：算了。'), ('他走了.', '他走了。')))
    # |               LIST_EXTEND              1
    # |  89           CALL                     2
    # |  97           LOAD_CONST               3 (<code object test_halfwidth_near_cjk_becomes_fullwidth at 0x75bcd96400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 89>)
    # |               MAKE_FUNCTION
    # |  89           CALL                     0
    # |  97           STORE_NAME               8 (test_halfwidth_near_cjk_becomes_fullwidth)
    # | 100           LOAD_NAME                4 (pytest)
    # |               LOAD_ATTR               10 (mark)
    # |               LOAD_ATTR               13 (parametrize + NULL|self)
    # | 101           LOAD_CONST               4 ('src')
    # |               BUILD_LIST               0
    # |               LOAD_CONST              11 (('教学楼 3.5 公里外', '信号是 Wi-Fi，不是 4G', '版本 v1.2 发布'))
    # |               LIST_EXTEND              1
    # | 100           CALL                     2
    # | 103           LOAD_CONST               5 (<code object test_halfwidth_in_numbers_and_latin_preserved at 0x75bcd96800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 100>)
    # |               MAKE_FUNCTION
    # | 100           CALL                     0
    # | 103           STORE_NAME               9 (test_halfwidth_in_numbers_and_latin_preserved)
    # | 107           LOAD_CONST               6 (<code object test_already_correct_unchanged at 0x75bcd96c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 107>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_already_correct_unchanged)
    # |               LOAD_CONST               7 (())
    # |               STORE_NAME              11 (__static_attributes__)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_normalized at 0x75bcd96000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 80>:
    # |  80            RESUME                   0
    # |  87            LOAD_GLOBAL              1 (normalize_punctuation + NULL)
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         2 (expected)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       341 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              11 (('==',))
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              12 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (@py_assert2, expected)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('normalize_punctuation')
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
    # |                LOAD_GLOBAL              0 (normalize_punctuation)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (normalize_punctuation)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               2 ('normalize_punctuation')
    # |        L3:     LOAD_CONST               3 ('py1')
    # |                LOAD_CONST               4 ('src')
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
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               4 ('src')
    # |        L6:     LOAD_CONST               5 ('py3')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_CONST               7 ('expected')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (expected)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (expected)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               7 ('expected')
    # |        L9:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format6)
    # |                LOAD_CONST               8 ('assert %(py7)s')
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_FAST_BORROW         5 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format8)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              10 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   52 (@py_assert2, @py_assert4)
    # |                LOAD_CONST              10 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_halfwidth_near_cjk_becomes_fullwidth at 0x75bcd96400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 89>:
    # |  89            RESUME                   0
    # |  98            LOAD_GLOBAL              1 (normalize_punctuation + NULL)
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         2 (expected)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       341 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              11 (('==',))
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              12 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (@py_assert2, expected)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('normalize_punctuation')
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
    # |                LOAD_GLOBAL              0 (normalize_punctuation)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (normalize_punctuation)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               2 ('normalize_punctuation')
    # |        L3:     LOAD_CONST               3 ('py1')
    # |                LOAD_CONST               4 ('src')
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
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               4 ('src')
    # |        L6:     LOAD_CONST               5 ('py3')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_CONST               7 ('expected')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (expected)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (expected)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               7 ('expected')
    # |        L9:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format6)
    # |                LOAD_CONST               8 ('assert %(py7)s')
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_FAST_BORROW         5 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format8)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              10 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   52 (@py_assert2, @py_assert4)
    # |                LOAD_CONST              10 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_halfwidth_in_numbers_and_latin_preserved at 0x75bcd96800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 100>:
    # | 100            RESUME                   0
    # | 105            LOAD_GLOBAL              1 (normalize_punctuation + NULL)
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         1 (src)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       341 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              10 (('==',))
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              11 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (@py_assert2, src)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('normalize_punctuation')
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
    # |                LOAD_GLOBAL              0 (normalize_punctuation)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (normalize_punctuation)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               2 ('normalize_punctuation')
    # |        L3:     LOAD_CONST               3 ('py1')
    # |                LOAD_CONST               4 ('src')
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
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               4 ('src')
    # |        L6:     LOAD_CONST               5 ('py3')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_CONST               4 ('src')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (src)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               4 ('src')
    # |        L9:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               4 (@py_format6)
    # |                LOAD_CONST               7 ('assert %(py7)s')
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_FAST_BORROW         4 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format8)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   35 (@py_assert2, @py_assert4)
    # |                LOAD_CONST               9 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_already_correct_unchanged at 0x75bcd96c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 107>:
    # | 107            RESUME                   0
    # | 108            LOAD_CONST               0 ('她想说什么，最终只是摇头——那句话到底没有出口……')
    # |                STORE_FAST               1 (good)
    # | 109            LOAD_GLOBAL              1 (normalize_punctuation + NULL)
    # |                LOAD_FAST_BORROW         1 (good)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         1 (good)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       341 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              10 (('==',))
    # |                LOAD_FAST_BORROW         3 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              11 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (@py_assert2, good)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py0')
    # |                LOAD_CONST               2 ('normalize_punctuation')
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
    # |                LOAD_GLOBAL              0 (normalize_punctuation)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              0 (normalize_punctuation)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               2 ('normalize_punctuation')
    # |        L3:     LOAD_CONST               3 ('py1')
    # |                LOAD_CONST               4 ('good')
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
    # |                LOAD_FAST_BORROW         1 (good)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (good)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               4 ('good')
    # |        L6:     LOAD_CONST               5 ('py3')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_CONST               4 ('good')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (good)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (good)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               4 ('good')
    # |        L9:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               4 (@py_format6)
    # |                LOAD_CONST               7 ('assert %(py7)s')
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_FAST_BORROW         4 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format8)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   35 (@py_assert2, @py_assert4)
    # |                LOAD_CONST               9 (None)
    # |                RETURN_VALUE

    def test_normalized(self, src, expected):
        '=='
        # ── 函数体（字节码重建见 BODY 段）──
        # |  80            RESUME                   0
        # |  87            LOAD_GLOBAL              1 (normalize_punctuation + NULL)
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         2 (expected)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       341 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              11 (('==',))
        # |                LOAD_FAST_BORROW         4 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              12 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (@py_assert2, expected)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('normalize_punctuation')
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
        # |                LOAD_GLOBAL              0 (normalize_punctuation)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (normalize_punctuation)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               2 ('normalize_punctuation')
        # |        L3:     LOAD_CONST               3 ('py1')
        # |                LOAD_CONST               4 ('src')
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
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               4 ('src')
        # |        L6:     LOAD_CONST               5 ('py3')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_CONST               7 ('expected')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (expected)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (expected)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               7 ('expected')
        # |        L9:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format6)
        # |                LOAD_CONST               8 ('assert %(py7)s')
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_FAST_BORROW         5 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format8)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              10 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   52 (@py_assert2, @py_assert4)
        # |                LOAD_CONST              10 (None)
        # |                RETURN_VALUE

    def test_halfwidth_near_cjk_becomes_fullwidth(self, src, expected):
        '=='
        # ── 函数体（字节码重建见 BODY 段）──
        # |  89            RESUME                   0
        # |  98            LOAD_GLOBAL              1 (normalize_punctuation + NULL)
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         2 (expected)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       341 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              11 (('==',))
        # |                LOAD_FAST_BORROW         4 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              12 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 50 (@py_assert2, expected)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('normalize_punctuation')
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
        # |                LOAD_GLOBAL              0 (normalize_punctuation)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (normalize_punctuation)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               2 ('normalize_punctuation')
        # |        L3:     LOAD_CONST               3 ('py1')
        # |                LOAD_CONST               4 ('src')
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
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               4 ('src')
        # |        L6:     LOAD_CONST               5 ('py3')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_CONST               7 ('expected')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (expected)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (expected)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               7 ('expected')
        # |        L9:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format6)
        # |                LOAD_CONST               8 ('assert %(py7)s')
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_FAST_BORROW         5 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format8)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              10 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   52 (@py_assert2, @py_assert4)
        # |                LOAD_CONST              10 (None)
        # |                RETURN_VALUE

    def test_halfwidth_in_numbers_and_latin_preserved(self, src):
        '"3.5" "Wi-Fi" 里的半角符号是合法的，不能误伤。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 100            RESUME                   0
        # | 105            LOAD_GLOBAL              1 (normalize_punctuation + NULL)
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         1 (src)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       341 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              10 (('==',))
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              11 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (@py_assert2, src)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('normalize_punctuation')
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
        # |                LOAD_GLOBAL              0 (normalize_punctuation)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (normalize_punctuation)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               2 ('normalize_punctuation')
        # |        L3:     LOAD_CONST               3 ('py1')
        # |                LOAD_CONST               4 ('src')
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
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               4 ('src')
        # |        L6:     LOAD_CONST               5 ('py3')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_CONST               4 ('src')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (src)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               4 ('src')
        # |        L9:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               4 (@py_format6)
        # |                LOAD_CONST               7 ('assert %(py7)s')
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_FAST_BORROW         4 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format8)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   35 (@py_assert2, @py_assert4)
        # |                LOAD_CONST               9 (None)
        # |                RETURN_VALUE

    def test_already_correct_unchanged(self):
        '她想说什么，最终只是摇头——那句话到底没有出口……'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 107            RESUME                   0
        # | 108            LOAD_CONST               0 ('她想说什么，最终只是摇头——那句话到底没有出口……')
        # |                STORE_FAST               1 (good)
        # | 109            LOAD_GLOBAL              1 (normalize_punctuation + NULL)
        # |                LOAD_FAST_BORROW         1 (good)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    34 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         1 (good)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       341 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              10 (('==',))
        # |                LOAD_FAST_BORROW         3 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              11 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 33 (@py_assert2, good)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py0')
        # |                LOAD_CONST               2 ('normalize_punctuation')
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
        # |                LOAD_GLOBAL              0 (normalize_punctuation)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              0 (normalize_punctuation)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               2 ('normalize_punctuation')
        # |        L3:     LOAD_CONST               3 ('py1')
        # |                LOAD_CONST               4 ('good')
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
        # |                LOAD_FAST_BORROW         1 (good)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (good)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               4 ('good')
        # |        L6:     LOAD_CONST               5 ('py3')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_CONST               4 ('good')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (good)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (good)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               4 ('good')
        # |        L9:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               4 (@py_format6)
        # |                LOAD_CONST               7 ('assert %(py7)s')
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_FAST_BORROW         4 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format8)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   35 (@py_assert2, @py_assert4)
        # |                LOAD_CONST               9 (None)
        # |                RETURN_VALUE


class TestChapterSplitting:
    'TestChapterSplitting'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 112           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestChapterSplitting')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         112
    # |               STORE_NAME               3 (__firstlineno__)
    # | 113           LOAD_CONST               1 (<code object test_mixed_heading_formats_all_found at 0x75bd2c1e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 113>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_mixed_heading_formats_all_found)
    # | 119           LOAD_CONST               2 (<code object test_chapters_renumbered_sequentially at 0x75bcd52300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 119>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_chapters_renumbered_sequentially)
    # | 123           LOAD_CONST               3 (<code object test_heading_not_included_in_body at 0x75bcd52800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 123>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_heading_not_included_in_body)
    # | 127           LOAD_CONST               4 (<code object test_junk_already_gone_from_body at 0x75bd2f7c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 127>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_junk_already_gone_from_body)
    # | 131           LOAD_CONST               5 (<code object test_no_headings_yields_single_chapter at 0x75bd2c2400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 131>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_no_headings_yields_single_chapter)
    # | 135           LOAD_CONST               6 (<code object test_empty_input at 0x75bd2bf900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 135>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_empty_input)
    # |               LOAD_CONST               7 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_mixed_heading_formats_all_found at 0x75bd2c1e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 113>:
    # |  113            RESUME                   0
    # |  114            LOAD_GLOBAL              1 (clean + NULL)
    # |                 LOAD_GLOBAL              2 (RAW)
    # |                 CALL                     1
    # |                 UNPACK_SEQUENCE          2
    # |                 STORE_FAST_STORE_FAST   18 (cleaned, _)
    # |  115            LOAD_GLOBAL              5 (split_chapters + NULL)
    # |                 LOAD_FAST_BORROW         1 (cleaned)
    # |                 CALL                     1
    # |                 STORE_FAST               3 (chapters)
    # |  116            LOAD_GLOBAL              7 (len + NULL)
    # |                 LOAD_FAST_BORROW         3 (chapters)
    # |                 CALL                     1
    # |                 STORE_FAST               4 (@py_assert2)
    # |                 LOAD_SMALL_INT           3
    # |                 STORE_FAST_LOAD_FAST    84 (@py_assert5, @py_assert2)
    # |                 LOAD_FAST_BORROW         5 (@py_assert5)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   102 (@py_assert4, @py_assert4)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       337 (to L11)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              12 (('==',))
    # |                 LOAD_FAST_BORROW         6 (@py_assert4)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              13 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert2, @py_assert5)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               1 ('py0')
    # |                 LOAD_CONST               2 ('len')
    # |                 LOAD_GLOBAL             12 (@py_builtins)
    # |                 LOAD_ATTR               14 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        33 (to L1)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              6 (len)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       27 (to L2)
    # |                 NOT_TAKEN
    # |         L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_GLOBAL              6 (len)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L3)
    # |         L2:     LOAD_CONST               2 ('len')
    # |         L3:     LOAD_CONST               3 ('py1')
    # |                 LOAD_CONST               4 ('chapters')
    # |                 LOAD_GLOBAL             12 (@py_builtins)
    # |                 LOAD_ATTR               14 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (chapters)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L5)
    # |                 NOT_TAKEN
    # |         L4:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (chapters)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L6)
    # |         L5:     LOAD_CONST               4 ('chapters')
    # |         L6:     LOAD_CONST               5 ('py3')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert2)
    # |                 CALL                     1
    # |                 LOAD_CONST               6 ('py6')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert5)
    # |                 CALL                     1
    # |                 BUILD_MAP                4
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format7)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (chapters)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      8 (c)
    # |                 SWAP                     2
    # |         L7:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L8:     FOR_ITER                14 (to L9)
    # |                 STORE_FAST_LOAD_FAST   136 (c, c)
    # |                 LOAD_ATTR               22 (title)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           16 (to L8)
    # |         L9:     END_FOR
    # |                 POP_ITER
    # |        L10:     SWAP                     2
    # |                 STORE_FAST               8 (c)
    # |                 CALL                     1
    # |                 LOAD_CONST               7 ('\n>assert %(py8)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST               8 ('py8')
    # |                 LOAD_FAST_BORROW         7 (@py_format7)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format9)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L11:     LOAD_CONST               9 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  101 (@py_assert4, @py_assert5)
    # |  117            LOAD_FAST_BORROW         3 (chapters)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      8 (c)
    # |                 SWAP                     2
    # |        L12:     BUILD_LIST               0
    # |                 SWAP                     2
    # |        L13:     FOR_ITER                14 (to L14)
    # |                 STORE_FAST_LOAD_FAST   136 (c, c)
    # |                 LOAD_ATTR               22 (title)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           16 (to L13)
    # |        L14:     END_FOR
    # |                 POP_ITER
    # |        L15:     STORE_FAST              10 (@py_assert0)
    # |                 STORE_FAST               8 (c)
    # |                 BUILD_LIST               0
    # |                 LOAD_CONST              14 (('初遇', '旧照片', '雨停了'))
    # |                 LIST_EXTEND              1
    # |                 STORE_FAST_LOAD_FAST   186 (@py_assert3, @py_assert0)
    # |                 LOAD_FAST_BORROW        11 (@py_assert3)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       121 (to L16)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              12 (('==',))
    # |                 LOAD_FAST_BORROW         4 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              15 (('%(py1)s == %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               3 ('py1')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        10 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST              10 ('py4')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format5)
    # |                 LOAD_CONST              11 ('assert %(py6)s')
    # |                 LOAD_CONST               6 ('py6')
    # |                 LOAD_FAST_BORROW        12 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               7 (@py_format7)
    # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               26 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L16:     LOAD_CONST               9 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              10 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST   75 (@py_assert2, @py_assert3)
    # |                 LOAD_CONST               9 (None)
    # |                 RETURN_VALUE
    # |   --   L17:     SWAP                     2
    # |                 POP_TOP
    # |  116            SWAP                     2
    # |                 STORE_FAST               8 (c)
    # |                 RERAISE                  0
    # |   --   L18:     SWAP                     2
    # |                 POP_TOP
    # |  117            SWAP                     2
    # |                 STORE_FAST               8 (c)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L7 to L10 -> L17 [4]
    # |   L12 to L15 -> L18 [2]
    # | Disassembly of <code object test_chapters_renumbered_sequentially at 0x75bcd52300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 119>:
    # |  119           RESUME                   0
    # |  120           LOAD_GLOBAL              1 (clean + NULL)
    # |                LOAD_GLOBAL              2 (RAW)
    # |                CALL                     1
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST_STORE_FAST   18 (cleaned, _)
    # |  121           LOAD_GLOBAL              5 (split_chapters + NULL)
    # |                LOAD_FAST_BORROW         1 (cleaned)
    # |                CALL                     1
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      3 (c)
    # |                SWAP                     2
    # |        L1:     BUILD_LIST               0
    # |                SWAP                     2
    # |        L2:     FOR_ITER                14 (to L3)
    # |                STORE_FAST_LOAD_FAST    51 (c, c)
    # |                LOAD_ATTR                6 (index)
    # |                LIST_APPEND              2
    # |                JUMP_BACKWARD           16 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |        L4:     STORE_FAST               4 (@py_assert0)
    # |                STORE_FAST               3 (c)
    # |                BUILD_LIST               0
    # |                LOAD_CONST               6 ((1, 2, 3))
    # |                LIST_EXTEND              1
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST               7 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               8 (('%(py1)s == %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               1 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               2 ('py4')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format5)
    # |                LOAD_CONST               3 ('assert %(py6)s')
    # |                LOAD_CONST               4 ('py6')
    # |                LOAD_FAST_BORROW         7 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format7)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L5:     LOAD_CONST               5 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               5 (None)
    # |                RETURN_VALUE
    # |   --   L6:     SWAP                     2
    # |                POP_TOP
    # |  121           SWAP                     2
    # |                STORE_FAST               3 (c)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L6 [2]
    # | Disassembly of <code object test_heading_not_included_in_body at 0x75bcd52800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 123>:
    # | 123           RESUME                   0
    # | 124           LOAD_GLOBAL              1 (clean + NULL)
    # |               LOAD_GLOBAL              2 (RAW)
    # |               CALL                     1
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   18 (cleaned, _)
    # | 125           LOAD_CONST               0 ('第一章')
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_GLOBAL              5 (split_chapters + NULL)
    # |               LOAD_FAST_BORROW         1 (cleaned)
    # |               CALL                     1
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |               LOAD_ATTR                6 (body)
    # |               STORE_FAST_LOAD_FAST    83 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               CONTAINS_OP              1 (not in)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       143 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST               7 (('not in',))
    # |               LOAD_FAST_BORROW         6 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST               8 (('%(py1)s not in %(py6)s\n{%(py6)s = %(py4)s.body\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               1 ('py1')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               2 ('py4')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               LOAD_CONST               3 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format7)
    # |               LOAD_CONST               4 ('assert %(py8)s')
    # |               LOAD_CONST               5 ('py8')
    # |               LOAD_FAST_BORROW         7 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               8 (@py_format9)
    # |               LOAD_GLOBAL             15 (AssertionError + NULL)
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               16 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_junk_already_gone_from_body at 0x75bd2f7c00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 127>:
    # | 127           RESUME                   0
    # | 128           LOAD_GLOBAL              1 (clean + NULL)
    # |               LOAD_GLOBAL              2 (RAW)
    # |               CALL                     1
    # |               UNPACK_SEQUENCE          2
    # |               STORE_FAST_STORE_FAST   18 (cleaned, _)
    # | 129           LOAD_CONST               0 (<code object <genexpr> at 0x105757dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 129>)
    # |               MAKE_FUNCTION
    # |               LOAD_GLOBAL              5 (split_chapters + NULL)
    # |               LOAD_FAST_BORROW         1 (cleaned)
    # |               CALL                     1
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_GLOBAL              7 (all + NULL)
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('all')
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
    # |               LOAD_GLOBAL              6 (all)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              6 (all)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('all')
    # |       L3:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               6 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   52 (@py_assert1, @py_assert3)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x105757dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 129>:
    # |  129           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                20 (to L3)
    # |                STORE_FAST               1 (c)
    # |                LOAD_CONST               0 ('example.com')
    # |                LOAD_FAST_BORROW         1 (c)
    # |                LOAD_ATTR                0 (body)
    # |                CONTAINS_OP              1 (not in)
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           22 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
    # | Disassembly of <code object test_no_headings_yields_single_chapter at 0x75bd2c2400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 131>:
    # | 131           RESUME                   0
    # | 132           LOAD_GLOBAL              1 (split_chapters + NULL)
    # |               LOAD_CONST               0 ('就是一段没有任何章节标记的散文。\n\n第二段。')
    # |               CALL                     1
    # |               STORE_FAST               1 (chapters)
    # | 133           BUILD_LIST               0
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_GLOBAL              3 (len + NULL)
    # |               LOAD_FAST_BORROW         1 (chapters)
    # |               CALL                     1
    # |               STORE_FAST               3 (@py_assert4)
    # |               LOAD_SMALL_INT           1
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert7, @py_assert4)
    # |               LOAD_FAST_BORROW         4 (@py_assert7)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert0, @py_assert6)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       28 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_FAST_BORROW         1 (chapters)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   119 (@py_assert12, @py_assert12)
    # |               LOAD_ATTR                4 (title)
    # |               STORE_FAST               8 (@py_assert14)
    # |               LOAD_CONST               1 ('全文')
    # |               STORE_FAST_LOAD_FAST   152 (@py_assert17, @py_assert14)
    # |               LOAD_FAST_BORROW         9 (@py_assert17)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST   170 (@py_assert16, @py_assert16)
    # |               STORE_FAST               6 (@py_assert0)
    # |       L1:     LOAD_FAST_BORROW         6 (@py_assert0)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       478 (to L9)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              18 (('==',))
    # |               LOAD_FAST_BORROW         5 (@py_assert6)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              19 (('%(py5)s\n{%(py5)s = %(py2)s(%(py3)s)\n} == %(py8)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert4, @py_assert7)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               2 ('py2')
    # |               LOAD_CONST               3 ('len')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              2 (len)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L3)
    # |               NOT_TAKEN
    # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              2 (len)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L4)
    # |       L3:     LOAD_CONST               3 ('len')
    # |       L4:     LOAD_CONST               4 ('py3')
    # |               LOAD_CONST               5 ('chapters')
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
    # |               LOAD_FAST_BORROW         1 (chapters)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (chapters)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST               5 ('chapters')
    # |       L7:     LOAD_CONST               6 ('py5')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               7 ('py8')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert7)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format9)
    # |               LOAD_CONST               8 ('%(py10)s')
    # |               LOAD_CONST               9 ('py10')
    # |               LOAD_FAST_BORROW        11 (@py_format9)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   194 (@py_format11, @py_assert1)
    # |               LOAD_ATTR               19 (append + NULL|self)
    # |               LOAD_FAST_BORROW        12 (@py_format11)
    # |               CALL                     1
    # |               POP_TOP
    # |               LOAD_FAST_BORROW         5 (@py_assert6)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE      129 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              18 (('==',))
    # |               LOAD_FAST_CHECK         10 (@py_assert16)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              20 (('%(py15)s\n{%(py15)s = %(py13)s.title\n} == %(py18)s',))
    # |               LOAD_FAST_CHECK          8 (@py_assert14)
    # |               LOAD_FAST_CHECK          9 (@py_assert17)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST              10 ('py13')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_CHECK          7 (@py_assert12)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py15')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert14)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py18')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_assert17)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              13 (@py_format19)
    # |               LOAD_CONST              13 ('%(py20)s')
    # |               LOAD_CONST              14 ('py20')
    # |               LOAD_FAST_BORROW        13 (@py_format19)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST_LOAD_FAST   226 (@py_format21, @py_assert1)
    # |               LOAD_ATTR               19 (append + NULL|self)
    # |               LOAD_FAST_BORROW        14 (@py_format21)
    # |               CALL                     1
    # |               POP_TOP
    # |       L8:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_boolop)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               LOAD_SMALL_INT           0
    # |               CALL                     2
    # |               BUILD_MAP                0
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              15 (@py_format22)
    # |               LOAD_CONST              15 ('assert %(py23)s')
    # |               LOAD_CONST              16 ('py23')
    # |               LOAD_FAST_BORROW        15 (@py_format22)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              16 (@py_format24)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        16 (@py_format24)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L9:     LOAD_CONST              17 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert6)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST               7 (@py_assert12)
    # |               COPY                     1
    # |               STORE_FAST               8 (@py_assert14)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  169 (@py_assert16, @py_assert17)
    # |               LOAD_CONST              17 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_empty_input at 0x75bd2bf900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 135>:
    # | 135           RESUME                   0
    # | 136           LOAD_CONST               0 ('')
    # |               STORE_FAST               1 (@py_assert1)
    # |               LOAD_GLOBAL              1 (split_chapters + NULL)
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
    # |               LOAD_CONST               2 ('split_chapters')
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
    # |               LOAD_GLOBAL              0 (split_chapters)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |               LOAD_ATTR               12 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              0 (split_chapters)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               2 ('split_chapters')
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

    def test_mixed_heading_formats_all_found(self):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  113            RESUME                   0
        # |  114            LOAD_GLOBAL              1 (clean + NULL)
        # |                 LOAD_GLOBAL              2 (RAW)
        # |                 CALL                     1
        # |                 UNPACK_SEQUENCE          2
        # |                 STORE_FAST_STORE_FAST   18 (cleaned, _)
        # |  115            LOAD_GLOBAL              5 (split_chapters + NULL)
        # |                 LOAD_FAST_BORROW         1 (cleaned)
        # |                 CALL                     1
        # |                 STORE_FAST               3 (chapters)
        # |  116            LOAD_GLOBAL              7 (len + NULL)
        # |                 LOAD_FAST_BORROW         3 (chapters)
        # |                 CALL                     1
        # |                 STORE_FAST               4 (@py_assert2)
        # |                 LOAD_SMALL_INT           3
        # |                 STORE_FAST_LOAD_FAST    84 (@py_assert5, @py_assert2)
        # |                 LOAD_FAST_BORROW         5 (@py_assert5)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   102 (@py_assert4, @py_assert4)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       337 (to L11)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              12 (('==',))
        # |                 LOAD_FAST_BORROW         6 (@py_assert4)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              13 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert2, @py_assert5)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               1 ('py0')
        # |                 LOAD_CONST               2 ('len')
        # |                 LOAD_GLOBAL             12 (@py_builtins)
        # |                 LOAD_ATTR               14 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        33 (to L1)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              6 (len)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       27 (to L2)
        # |                 NOT_TAKEN
        # |         L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_GLOBAL              6 (len)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L3)
        # |         L2:     LOAD_CONST               2 ('len')
        # |         L3:     LOAD_CONST               3 ('py1')
        # |                 LOAD_CONST               4 ('chapters')
        # |                 LOAD_GLOBAL             12 (@py_builtins)
        # |                 LOAD_ATTR               14 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (chapters)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L5)
        # |                 NOT_TAKEN
        # |         L4:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (chapters)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L6)
        # |         L5:     LOAD_CONST               4 ('chapters')
        # |         L6:     LOAD_CONST               5 ('py3')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert2)
        # |                 CALL                     1
        # |                 LOAD_CONST               6 ('py6')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert5)
        # |                 CALL                     1
        # |                 BUILD_MAP                4
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format7)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (chapters)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      8 (c)
        # |                 SWAP                     2
        # |         L7:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L8:     FOR_ITER                14 (to L9)
        # |                 STORE_FAST_LOAD_FAST   136 (c, c)
        # |                 LOAD_ATTR               22 (title)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           16 (to L8)
        # |         L9:     END_FOR
        # |                 POP_ITER
        # |        L10:     SWAP                     2
        # |                 STORE_FAST               8 (c)
        # |                 CALL                     1
        # |                 LOAD_CONST               7 ('\n>assert %(py8)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST               8 ('py8')
        # |                 LOAD_FAST_BORROW         7 (@py_format7)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format9)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L11:     LOAD_CONST               9 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  101 (@py_assert4, @py_assert5)
        # |  117            LOAD_FAST_BORROW         3 (chapters)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      8 (c)
        # |                 SWAP                     2
        # |        L12:     BUILD_LIST               0
        # |                 SWAP                     2
        # |        L13:     FOR_ITER                14 (to L14)
        # |                 STORE_FAST_LOAD_FAST   136 (c, c)
        # |                 LOAD_ATTR               22 (title)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           16 (to L13)
        # |        L14:     END_FOR
        # |                 POP_ITER
        # |        L15:     STORE_FAST              10 (@py_assert0)
        # |                 STORE_FAST               8 (c)
        # |                 BUILD_LIST               0
        # |                 LOAD_CONST              14 (('初遇', '旧照片', '雨停了'))
        # |                 LIST_EXTEND              1
        # |                 STORE_FAST_LOAD_FAST   186 (@py_assert3, @py_assert0)
        # |                 LOAD_FAST_BORROW        11 (@py_assert3)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       121 (to L16)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              12 (('==',))
        # |                 LOAD_FAST_BORROW         4 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              15 (('%(py1)s == %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 171 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               3 ('py1')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        10 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST              10 ('py4')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format5)
        # |                 LOAD_CONST              11 ('assert %(py6)s')
        # |                 LOAD_CONST               6 ('py6')
        # |                 LOAD_FAST_BORROW        12 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               7 (@py_format7)
        # |                 LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               26 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L16:     LOAD_CONST               9 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              10 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST   75 (@py_assert2, @py_assert3)
        # |                 LOAD_CONST               9 (None)
        # |                 RETURN_VALUE
        # |   --   L17:     SWAP                     2
        # |                 POP_TOP
        # |  116            SWAP                     2
        # |                 STORE_FAST               8 (c)
        # |                 RERAISE                  0
        # |   --   L18:     SWAP                     2
        # |                 POP_TOP
        # |  117            SWAP                     2
        # |                 STORE_FAST               8 (c)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L7 to L10 -> L17 [4]
        # |   L12 to L15 -> L18 [2]

    def test_chapters_renumbered_sequentially(self):
        'py1'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  119           RESUME                   0
        # |  120           LOAD_GLOBAL              1 (clean + NULL)
        # |                LOAD_GLOBAL              2 (RAW)
        # |                CALL                     1
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST_STORE_FAST   18 (cleaned, _)
        # |  121           LOAD_GLOBAL              5 (split_chapters + NULL)
        # |                LOAD_FAST_BORROW         1 (cleaned)
        # |                CALL                     1
        # |                GET_ITER
        # |                LOAD_FAST_AND_CLEAR      3 (c)
        # |                SWAP                     2
        # |        L1:     BUILD_LIST               0
        # |                SWAP                     2
        # |        L2:     FOR_ITER                14 (to L3)
        # |                STORE_FAST_LOAD_FAST    51 (c, c)
        # |                LOAD_ATTR                6 (index)
        # |                LIST_APPEND              2
        # |                JUMP_BACKWARD           16 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |        L4:     STORE_FAST               4 (@py_assert0)
        # |                STORE_FAST               3 (c)
        # |                BUILD_LIST               0
        # |                LOAD_CONST               6 ((1, 2, 3))
        # |                LIST_EXTEND              1
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST               7 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               8 (('%(py1)s == %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               1 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               2 ('py4')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format5)
        # |                LOAD_CONST               3 ('assert %(py6)s')
        # |                LOAD_CONST               4 ('py6')
        # |                LOAD_FAST_BORROW         7 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format7)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L5:     LOAD_CONST               5 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               5 (None)
        # |                RETURN_VALUE
        # |   --   L6:     SWAP                     2
        # |                POP_TOP
        # |  121           SWAP                     2
        # |                STORE_FAST               3 (c)
        # |                RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L6 [2]

    def test_heading_not_included_in_body(self):
        '第一章'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 123           RESUME                   0
        # | 124           LOAD_GLOBAL              1 (clean + NULL)
        # |               LOAD_GLOBAL              2 (RAW)
        # |               CALL                     1
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   18 (cleaned, _)
        # | 125           LOAD_CONST               0 ('第一章')
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_GLOBAL              5 (split_chapters + NULL)
        # |               LOAD_FAST_BORROW         1 (cleaned)
        # |               CALL                     1
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |               LOAD_ATTR                6 (body)
        # |               STORE_FAST_LOAD_FAST    83 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               CONTAINS_OP              1 (not in)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       143 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST               7 (('not in',))
        # |               LOAD_FAST_BORROW         6 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST               8 (('%(py1)s not in %(py6)s\n{%(py6)s = %(py4)s.body\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 53 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               1 ('py1')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               2 ('py4')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               LOAD_CONST               3 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format7)
        # |               LOAD_CONST               4 ('assert %(py8)s')
        # |               LOAD_CONST               5 ('py8')
        # |               LOAD_FAST_BORROW         7 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               8 (@py_format9)
        # |               LOAD_GLOBAL             15 (AssertionError + NULL)
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               16 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE

    def test_junk_already_gone_from_body(self):
        'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 127           RESUME                   0
        # | 128           LOAD_GLOBAL              1 (clean + NULL)
        # |               LOAD_GLOBAL              2 (RAW)
        # |               CALL                     1
        # |               UNPACK_SEQUENCE          2
        # |               STORE_FAST_STORE_FAST   18 (cleaned, _)
        # | 129           LOAD_CONST               0 (<code object <genexpr> at 0x105757dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 129>)
        # |               MAKE_FUNCTION
        # |               LOAD_GLOBAL              5 (split_chapters + NULL)
        # |               LOAD_FAST_BORROW         1 (cleaned)
        # |               CALL                     1
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_GLOBAL              7 (all + NULL)
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('all')
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
        # |               LOAD_GLOBAL              6 (all)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              6 (all)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('all')
        # |       L3:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               6 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   52 (@py_assert1, @py_assert3)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x105757dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 129>:
        # |  129           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                20 (to L3)
        # |                STORE_FAST               1 (c)
        # |                LOAD_CONST               0 ('example.com')
        # |                LOAD_FAST_BORROW         1 (c)
        # |                LOAD_ATTR                0 (body)
        # |                CONTAINS_OP              1 (not in)
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           22 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti

    def test_no_headings_yields_single_chapter(self):
        '就是一段没有任何章节标记的散文。\n\n第二段。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 131           RESUME                   0
        # | 132           LOAD_GLOBAL              1 (split_chapters + NULL)
        # |               LOAD_CONST               0 ('就是一段没有任何章节标记的散文。\n\n第二段。')
        # |               CALL                     1
        # |               STORE_FAST               1 (chapters)
        # | 133           BUILD_LIST               0
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_GLOBAL              3 (len + NULL)
        # |               LOAD_FAST_BORROW         1 (chapters)
        # |               CALL                     1
        # |               STORE_FAST               3 (@py_assert4)
        # |               LOAD_SMALL_INT           1
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert7, @py_assert4)
        # |               LOAD_FAST_BORROW         4 (@py_assert7)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert6, @py_assert6)
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert0, @py_assert6)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       28 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_FAST_BORROW         1 (chapters)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   119 (@py_assert12, @py_assert12)
        # |               LOAD_ATTR                4 (title)
        # |               STORE_FAST               8 (@py_assert14)
        # |               LOAD_CONST               1 ('全文')
        # |               STORE_FAST_LOAD_FAST   152 (@py_assert17, @py_assert14)
        # |               LOAD_FAST_BORROW         9 (@py_assert17)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST   170 (@py_assert16, @py_assert16)
        # |               STORE_FAST               6 (@py_assert0)
        # |       L1:     LOAD_FAST_BORROW         6 (@py_assert0)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       478 (to L9)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              18 (('==',))
        # |               LOAD_FAST_BORROW         5 (@py_assert6)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              19 (('%(py5)s\n{%(py5)s = %(py2)s(%(py3)s)\n} == %(py8)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert4, @py_assert7)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               2 ('py2')
        # |               LOAD_CONST               3 ('len')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              2 (len)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L3)
        # |               NOT_TAKEN
        # |       L2:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              2 (len)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L4)
        # |       L3:     LOAD_CONST               3 ('len')
        # |       L4:     LOAD_CONST               4 ('py3')
        # |               LOAD_CONST               5 ('chapters')
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
        # |               LOAD_FAST_BORROW         1 (chapters)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (chapters)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST               5 ('chapters')
        # |       L7:     LOAD_CONST               6 ('py5')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               7 ('py8')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert7)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format9)
        # |               LOAD_CONST               8 ('%(py10)s')
        # |               LOAD_CONST               9 ('py10')
        # |               LOAD_FAST_BORROW        11 (@py_format9)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   194 (@py_format11, @py_assert1)
        # |               LOAD_ATTR               19 (append + NULL|self)
        # |               LOAD_FAST_BORROW        12 (@py_format11)
        # |               CALL                     1
        # |               POP_TOP
        # |               LOAD_FAST_BORROW         5 (@py_assert6)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE      129 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              18 (('==',))
        # |               LOAD_FAST_CHECK         10 (@py_assert16)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              20 (('%(py15)s\n{%(py15)s = %(py13)s.title\n} == %(py18)s',))
        # |               LOAD_FAST_CHECK          8 (@py_assert14)
        # |               LOAD_FAST_CHECK          9 (@py_assert17)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST              10 ('py13')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_CHECK          7 (@py_assert12)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py15')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert14)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py18')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_assert17)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              13 (@py_format19)
        # |               LOAD_CONST              13 ('%(py20)s')
        # |               LOAD_CONST              14 ('py20')
        # |               LOAD_FAST_BORROW        13 (@py_format19)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST_LOAD_FAST   226 (@py_format21, @py_assert1)
        # |               LOAD_ATTR               19 (append + NULL|self)
        # |               LOAD_FAST_BORROW        14 (@py_format21)
        # |               CALL                     1
        # |               POP_TOP
        # |       L8:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_boolop)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               LOAD_SMALL_INT           0
        # |               CALL                     2
        # |               BUILD_MAP                0
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              15 (@py_format22)
        # |               LOAD_CONST              15 ('assert %(py23)s')
        # |               LOAD_CONST              16 ('py23')
        # |               LOAD_FAST_BORROW        15 (@py_format22)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              16 (@py_format24)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        16 (@py_format24)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L9:     LOAD_CONST              17 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert6)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST               7 (@py_assert12)
        # |               COPY                     1
        # |               STORE_FAST               8 (@py_assert14)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  169 (@py_assert16, @py_assert17)
        # |               LOAD_CONST              17 (None)
        # |               RETURN_VALUE

    def test_empty_input(self):
        'py0'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 135           RESUME                   0
        # | 136           LOAD_CONST               0 ('')
        # |               STORE_FAST               1 (@py_assert1)
        # |               LOAD_GLOBAL              1 (split_chapters + NULL)
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
        # |               LOAD_CONST               2 ('split_chapters')
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
        # |               LOAD_GLOBAL              0 (split_chapters)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |               LOAD_ATTR               12 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              0 (split_chapters)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               2 ('split_chapters')
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


class TestBook:
    'TestBook'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 139           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestBook')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         139
    # |               STORE_NAME               3 (__firstlineno__)
    # | 140           LOAD_CONST               1 (<code object test_ingest_file at 0x75bd2ad400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 140>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_ingest_file)
    # | 149           LOAD_CONST               2 (<code object test_ingest_dir_writes_markdown at 0x75bd2ade00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 149>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_ingest_dir_writes_markdown)
    # | 159           LOAD_CONST               3 (<code object test_chapter_markdown_matches_gate_title_format at 0x75bcd8a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 159>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_chapter_markdown_matches_gate_title_format)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_ingest_file at 0x75bd2ad400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 140>:
    # | 140            RESUME                   0
    # | 141            LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               0 ('伞的重量.txt')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               2 (f)
    # | 142            LOAD_FAST_BORROW         2 (f)
    # |                LOAD_ATTR                1 (write_bytes + NULL|self)
    # |                LOAD_GLOBAL              2 (RAW)
    # |                LOAD_ATTR                5 (encode + NULL|self)
    # |                LOAD_CONST               1 ('gb18030')
    # |                CALL                     1
    # |                CALL                     1
    # |                POP_TOP
    # | 143            LOAD_GLOBAL              7 (ingest_file + NULL)
    # |                LOAD_FAST_BORROW         2 (f)
    # |                CALL                     1
    # |                STORE_FAST               3 (book)
    # | 144            LOAD_FAST_BORROW         3 (book)
    # |                LOAD_ATTR                8 (title)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_CONST               2 ('伞的重量')
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.title\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('book')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (book)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (book)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('book')
    # |        L3:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format6)
    # |                LOAD_CONST               7 ('assert %(py7)s')
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_FAST_BORROW         7 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format8)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L4:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
    # | 145            LOAD_FAST_BORROW         3 (book)
    # |                LOAD_ATTR               26 (chapters)
    # |                STORE_FAST               9 (@py_assert2)
    # |                LOAD_GLOBAL             29 (len + NULL)
    # |                LOAD_FAST_BORROW         9 (@py_assert2)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert4)
    # |                LOAD_SMALL_INT           3
    # |                STORE_FAST_LOAD_FAST   165 (@py_assert7, @py_assert4)
    # |                LOAD_FAST_BORROW        10 (@py_assert7)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert6, @py_assert6)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       307 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('==',))
    # |                LOAD_FAST_BORROW        11 (@py_assert6)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s.chapters\n})\n} == %(py8)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 90 (@py_assert4, @py_assert7)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST              10 ('len')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             28 (len)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             28 (len)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST              10 ('len')
    # |        L7:     LOAD_CONST              11 ('py1')
    # |                LOAD_CONST               4 ('book')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (book)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (book)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST               4 ('book')
    # |       L10:     LOAD_CONST              12 ('py3')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py8')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_assert7)
    # |                CALL                     1
    # |                BUILD_MAP                5
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              12 (@py_format9)
    # |                LOAD_CONST              14 ('assert %(py10)s')
    # |                LOAD_CONST              15 ('py10')
    # |                LOAD_FAST_BORROW        12 (@py_format9)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format11)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_format11)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L11:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  186 (@py_assert6, @py_assert7)
    # | 146            LOAD_FAST_BORROW         3 (book)
    # |                LOAD_ATTR               30 (word_count)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                COMPARE_OP             132 (>)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L15)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('>',))
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py2)s\n{%(py2)s = %(py0)s.word_count\n} > %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('book')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (book)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L13)
    # |                NOT_TAKEN
    # |       L12:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (book)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L14)
    # |       L13:     LOAD_CONST               4 ('book')
    # |       L14:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format6)
    # |                LOAD_CONST               7 ('assert %(py7)s')
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_FAST_BORROW         7 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format8)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L15:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
    # | 147            LOAD_FAST_BORROW         3 (book)
    # |                LOAD_ATTR               32 (dropped_lines)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_SMALL_INT           2
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       199 (to L19)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('==',))
    # |                LOAD_FAST_BORROW         6 (@py_assert3)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              21 (('%(py2)s\n{%(py2)s = %(py0)s.dropped_lines\n} == %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('book')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L16)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (book)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L17)
    # |                NOT_TAKEN
    # |       L16:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (book)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L18)
    # |       L17:     LOAD_CONST               4 ('book')
    # |       L18:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py5')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format6)
    # |                LOAD_CONST               7 ('assert %(py7)s')
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_FAST_BORROW         7 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format8)
    # |                LOAD_GLOBAL             23 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L19:     LOAD_CONST               9 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
    # |                LOAD_CONST               9 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_ingest_dir_writes_markdown at 0x75bd2ade00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 149>:
    # | 149            RESUME                   0
    # | 150            LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               0 ('raw')
    # |                BINARY_OP               11 (/)
    # |                LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               1 ('clean')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST_STORE_FAST   50 (dst, src)
    # | 151            LOAD_FAST_BORROW         2 (src)
    # |                LOAD_ATTR                1 (mkdir + NULL|self)
    # |                CALL                     0
    # |                POP_TOP
    # | 152            LOAD_FAST_BORROW         2 (src)
    # |                LOAD_CONST               2 ('a.txt')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR                3 (write_bytes + NULL|self)
    # |                LOAD_GLOBAL              4 (RAW)
    # |                LOAD_ATTR                7 (encode + NULL|self)
    # |                LOAD_CONST               3 ('utf-8')
    # |                CALL                     1
    # |                CALL                     1
    # |                POP_TOP
    # | 153            LOAD_FAST_BORROW         2 (src)
    # |                LOAD_CONST               4 ('b.txt')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR                3 (write_bytes + NULL|self)
    # |                LOAD_GLOBAL              4 (RAW)
    # |                LOAD_ATTR                7 (encode + NULL|self)
    # |                LOAD_CONST               5 ('gb18030')
    # |                CALL                     1
    # |                CALL                     1
    # |                POP_TOP
    # | 154            LOAD_GLOBAL              9 (ingest_dir + NULL)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (src, dst)
    # |                CALL                     2
    # |                STORE_FAST               4 (books)
    # | 155            LOAD_GLOBAL             11 (len + NULL)
    # |                LOAD_FAST_BORROW         4 (books)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert2)
    # |                LOAD_SMALL_INT           2
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert5, @py_assert2)
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                COMPARE_OP              72 (==)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       285 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              28 (('==',))
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              29 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert5)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               6 ('py0')
    # |                LOAD_CONST               7 ('len')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (len)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (len)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               7 ('len')
    # |        L3:     LOAD_CONST               8 ('py1')
    # |                LOAD_CONST               9 ('books')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (books)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (books)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               9 ('books')
    # |        L6:     LOAD_CONST              10 ('py3')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py6')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format7)
    # |                LOAD_CONST              12 ('assert %(py8)s')
    # |                LOAD_CONST              13 ('py8')
    # |                LOAD_FAST_BORROW         8 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format9)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               26 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L7:     LOAD_CONST              14 (None)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  118 (@py_assert4, @py_assert5)
    # | 156            LOAD_FAST_BORROW         3 (dst)
    # |                LOAD_CONST              15 ('a.md')
    # |                BINARY_OP               11 (/)
    # |                LOAD_ATTR               29 (read_text + NULL|self)
    # |                LOAD_CONST               3 ('utf-8')
    # |                CALL                     1
    # |                STORE_FAST              10 (out)
    # | 157            BUILD_LIST               0
    # |                STORE_FAST_LOAD_FAST   186 (@py_assert1, out)
    # |                LOAD_ATTR               30 (startswith)
    # |                STORE_FAST              12 (@py_assert3)
    # |                LOAD_CONST              16 ('# a')
    # |                STORE_FAST_LOAD_FAST   108 (@py_assert5, @py_assert3)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   221 (@py_assert7, @py_assert7)
    # |                STORE_FAST_LOAD_FAST   237 (@py_assert0, @py_assert7)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        9 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_CONST              17 ('## 第1章 初遇')
    # |                STORE_FAST_LOAD_FAST   255 (@py_assert10, @py_assert10)
    # |                LOAD_FAST_BORROW        10 (out)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST              16 (@py_assert12)
    # |                LOAD_FAST               16 (@py_assert12)
    # |                STORE_FAST              14 (@py_assert0)
    # |        L8:     LOAD_FAST_BORROW        14 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       413 (to L16)
    # |                NOT_TAKEN
    # |                LOAD_CONST              18 ('%(py8)s\n{%(py8)s = %(py4)s\n{%(py4)s = %(py2)s.startswith\n}(%(py6)s)\n}')
    # |                LOAD_CONST              19 ('py2')
    # |                LOAD_CONST              20 ('out')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (out)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L10)
    # |                NOT_TAKEN
    # |        L9:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (out)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L11)
    # |       L10:     LOAD_CONST              20 ('out')
    # |       L11:     LOAD_CONST              21 ('py4')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py6')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py8')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        13 (@py_assert7)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   155 (@py_format9, @py_assert1)
    # |                LOAD_ATTR               33 (append + NULL|self)
    # |                LOAD_FAST_BORROW         9 (@py_format9)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW        13 (@py_assert7)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      164 (to L15)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              30 (('in',))
    # |                LOAD_FAST_CHECK         16 (@py_assert12)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              31 (('%(py11)s in %(py13)s',))
    # |                LOAD_FAST_CHECK         15 (@py_assert10)
    # |                LOAD_FAST_BORROW        10 (out)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              22 ('py11')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        15 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              23 ('py13')
    # |                LOAD_CONST              20 ('out')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (out)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L13)
    # |                NOT_TAKEN
    # |       L12:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (out)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L14)
    # |       L13:     LOAD_CONST              20 ('out')
    # |       L14:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format14)
    # |                LOAD_CONST              24 ('%(py15)s')
    # |                LOAD_CONST              25 ('py15')
    # |                LOAD_FAST_BORROW        17 (@py_format14)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format16)
    # |                LOAD_FAST_BORROW        11 (@py_assert1)
    # |                LOAD_ATTR               33 (append + NULL|self)
    # |                LOAD_FAST_BORROW        18 (@py_format16)
    # |                CALL                     1
    # |                POP_TOP
    # |       L15:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               34 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              19 (@py_format17)
    # |                LOAD_CONST              26 ('assert %(py18)s')
    # |                LOAD_CONST              27 ('py18')
    # |                LOAD_FAST_BORROW        19 (@py_format17)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              20 (@py_format19)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               26 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        20 (@py_format19)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L16:     LOAD_CONST              14 (None)
    # |                COPY                     1
    # |                STORE_FAST              14 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST              11 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST              12 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST              15 (@py_assert10)
    # |                STORE_FAST              16 (@py_assert12)
    # |                LOAD_CONST              14 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_chapter_markdown_matches_gate_title_format at 0x75bcd8a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 159>:
    # | 159           RESUME                   0
    # | 161           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (None)
    # |               IMPORT_NAME              0 (re)
    # |               STORE_FAST               1 (re)
    # |               LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (None)
    # |               IMPORT_NAME              1 (yaml)
    # |               STORE_FAST               2 (yaml)
    # | 162           LOAD_SMALL_INT           0
    # |               LOAD_CONST               2 (('Path',))
    # |               IMPORT_NAME              2 (pathlib)
    # |               IMPORT_FROM              3 (Path)
    # |               STORE_FAST               3 (Path)
    # |               POP_TOP
    # | 164           LOAD_FAST_BORROW         2 (yaml)
    # |               LOAD_ATTR                9 (safe_load + NULL|self)
    # | 165           LOAD_FAST_BORROW         3 (Path)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             10 (__file__)
    # |               CALL                     1
    # |               LOAD_ATTR               13 (resolve + NULL|self)
    # |               CALL                     0
    # |               LOAD_ATTR               14 (parent)
    # |               LOAD_ATTR               14 (parent)
    # |               LOAD_CONST               3 ('config')
    # |               BINARY_OP               11 (/)
    # |               LOAD_CONST               4 ('project.yaml')
    # |               BINARY_OP               11 (/)
    # |               LOAD_ATTR               17 (read_text + NULL|self)
    # |               LOAD_CONST               5 ('utf-8')
    # |               CALL                     1
    # | 164           CALL                     1
    # | 166           LOAD_CONST               6 ('format')
    # | 164           BINARY_OP               26 ([])
    # | 166           LOAD_CONST               7 ('chapter_title_pattern')
    # | 164           BINARY_OP               26 ([])
    # |               STORE_FAST               4 (pattern)
    # | 167           LOAD_GLOBAL             19 (Chapter + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               8 ('初遇')
    # |               LOAD_CONST               9 ('正文。')
    # |               CALL                     3
    # |               LOAD_ATTR               21 (to_markdown + NULL|self)
    # |               CALL                     0
    # |               STORE_FAST               5 (md)
    # | 168           LOAD_FAST_BORROW         1 (re)
    # |               LOAD_ATTR               22 (match)
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert1, md)
    # |               LOAD_ATTR               25 (splitlines + NULL|self)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert4, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (pattern, @py_assert4)
    # |               CALL                     2
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert6, @py_assert6)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       263 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_CONST              10 ('assert %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py3)s, %(py5)s)\n}')
    # |               LOAD_CONST              11 ('py0')
    # |               LOAD_CONST              12 ('re')
    # |               LOAD_GLOBAL             26 (@py_builtins)
    # |               LOAD_ATTR               28 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             30 (@pytest_ar)
    # |               LOAD_ATTR               32 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (re)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             30 (@pytest_ar)
    # |               LOAD_ATTR               34 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (re)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST              12 ('re')
    # |       L3:     LOAD_CONST              13 ('py2')
    # |               LOAD_GLOBAL             30 (@pytest_ar)
    # |               LOAD_ATTR               34 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              14 ('py3')
    # |               LOAD_CONST              15 ('pattern')
    # |               LOAD_GLOBAL             26 (@py_builtins)
    # |               LOAD_ATTR               28 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             30 (@pytest_ar)
    # |               LOAD_ATTR               32 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (pattern)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL             30 (@pytest_ar)
    # |               LOAD_ATTR               34 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (pattern)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST              15 ('pattern')
    # |       L6:     LOAD_CONST              16 ('py5')
    # |               LOAD_GLOBAL             30 (@pytest_ar)
    # |               LOAD_ATTR               34 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST              17 ('py7')
    # |               LOAD_GLOBAL             30 (@pytest_ar)
    # |               LOAD_ATTR               34 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert6)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format8)
    # |               LOAD_GLOBAL             37 (AssertionError + NULL)
    # |               LOAD_GLOBAL             30 (@pytest_ar)
    # |               LOAD_ATTR               38 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST               1 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert4, @py_assert6)
    # |               LOAD_CONST               1 (None)
    # |               RETURN_VALUE

    def test_ingest_file(self, tmp_path):
        '伞的重量.txt'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 140            RESUME                   0
        # | 141            LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               0 ('伞的重量.txt')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               2 (f)
        # | 142            LOAD_FAST_BORROW         2 (f)
        # |                LOAD_ATTR                1 (write_bytes + NULL|self)
        # |                LOAD_GLOBAL              2 (RAW)
        # |                LOAD_ATTR                5 (encode + NULL|self)
        # |                LOAD_CONST               1 ('gb18030')
        # |                CALL                     1
        # |                CALL                     1
        # |                POP_TOP
        # | 143            LOAD_GLOBAL              7 (ingest_file + NULL)
        # |                LOAD_FAST_BORROW         2 (f)
        # |                CALL                     1
        # |                STORE_FAST               3 (book)
        # | 144            LOAD_FAST_BORROW         3 (book)
        # |                LOAD_ATTR                8 (title)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_CONST               2 ('伞的重量')
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py2)s\n{%(py2)s = %(py0)s.title\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('book')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (book)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (book)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('book')
        # |        L3:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format6)
        # |                LOAD_CONST               7 ('assert %(py7)s')
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_FAST_BORROW         7 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format8)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L4:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
        # | 145            LOAD_FAST_BORROW         3 (book)
        # |                LOAD_ATTR               26 (chapters)
        # |                STORE_FAST               9 (@py_assert2)
        # |                LOAD_GLOBAL             29 (len + NULL)
        # |                LOAD_FAST_BORROW         9 (@py_assert2)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert4)
        # |                LOAD_SMALL_INT           3
        # |                STORE_FAST_LOAD_FAST   165 (@py_assert7, @py_assert4)
        # |                LOAD_FAST_BORROW        10 (@py_assert7)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert6, @py_assert6)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       307 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('==',))
        # |                LOAD_FAST_BORROW        11 (@py_assert6)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py5)s\n{%(py5)s = %(py0)s(%(py3)s\n{%(py3)s = %(py1)s.chapters\n})\n} == %(py8)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 90 (@py_assert4, @py_assert7)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST              10 ('len')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             28 (len)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             28 (len)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST              10 ('len')
        # |        L7:     LOAD_CONST              11 ('py1')
        # |                LOAD_CONST               4 ('book')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (book)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (book)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST               4 ('book')
        # |       L10:     LOAD_CONST              12 ('py3')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py8')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_assert7)
        # |                CALL                     1
        # |                BUILD_MAP                5
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              12 (@py_format9)
        # |                LOAD_CONST              14 ('assert %(py10)s')
        # |                LOAD_CONST              15 ('py10')
        # |                LOAD_FAST_BORROW        12 (@py_format9)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format11)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_format11)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L11:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  186 (@py_assert6, @py_assert7)
        # | 146            LOAD_FAST_BORROW         3 (book)
        # |                LOAD_ATTR               30 (word_count)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                COMPARE_OP             132 (>)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L15)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('>',))
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py2)s\n{%(py2)s = %(py0)s.word_count\n} > %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('book')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (book)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L13)
        # |                NOT_TAKEN
        # |       L12:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (book)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L14)
        # |       L13:     LOAD_CONST               4 ('book')
        # |       L14:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format6)
        # |                LOAD_CONST               7 ('assert %(py7)s')
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_FAST_BORROW         7 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format8)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L15:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
        # | 147            LOAD_FAST_BORROW         3 (book)
        # |                LOAD_ATTR               32 (dropped_lines)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_SMALL_INT           2
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert1)
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert3, @py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       199 (to L19)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('==',))
        # |                LOAD_FAST_BORROW         6 (@py_assert3)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              21 (('%(py2)s\n{%(py2)s = %(py0)s.dropped_lines\n} == %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert1, @py_assert4)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('book')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L16)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (book)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L17)
        # |                NOT_TAKEN
        # |       L16:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (book)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L18)
        # |       L17:     LOAD_CONST               4 ('book')
        # |       L18:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py5')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format6)
        # |                LOAD_CONST               7 ('assert %(py7)s')
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_FAST_BORROW         7 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format8)
        # |                LOAD_GLOBAL             23 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L19:     LOAD_CONST               9 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert3, @py_assert4)
        # |                LOAD_CONST               9 (None)
        # |                RETURN_VALUE

    def test_ingest_dir_writes_markdown(self, tmp_path):
        'raw'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 149            RESUME                   0
        # | 150            LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               0 ('raw')
        # |                BINARY_OP               11 (/)
        # |                LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               1 ('clean')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST_STORE_FAST   50 (dst, src)
        # | 151            LOAD_FAST_BORROW         2 (src)
        # |                LOAD_ATTR                1 (mkdir + NULL|self)
        # |                CALL                     0
        # |                POP_TOP
        # | 152            LOAD_FAST_BORROW         2 (src)
        # |                LOAD_CONST               2 ('a.txt')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR                3 (write_bytes + NULL|self)
        # |                LOAD_GLOBAL              4 (RAW)
        # |                LOAD_ATTR                7 (encode + NULL|self)
        # |                LOAD_CONST               3 ('utf-8')
        # |                CALL                     1
        # |                CALL                     1
        # |                POP_TOP
        # | 153            LOAD_FAST_BORROW         2 (src)
        # |                LOAD_CONST               4 ('b.txt')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR                3 (write_bytes + NULL|self)
        # |                LOAD_GLOBAL              4 (RAW)
        # |                LOAD_ATTR                7 (encode + NULL|self)
        # |                LOAD_CONST               5 ('gb18030')
        # |                CALL                     1
        # |                CALL                     1
        # |                POP_TOP
        # | 154            LOAD_GLOBAL              9 (ingest_dir + NULL)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (src, dst)
        # |                CALL                     2
        # |                STORE_FAST               4 (books)
        # | 155            LOAD_GLOBAL             11 (len + NULL)
        # |                LOAD_FAST_BORROW         4 (books)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert2)
        # |                LOAD_SMALL_INT           2
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert5, @py_assert2)
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                COMPARE_OP              72 (==)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       285 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              28 (('==',))
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              29 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} == %(py6)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert2, @py_assert5)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               6 ('py0')
        # |                LOAD_CONST               7 ('len')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (len)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (len)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               7 ('len')
        # |        L3:     LOAD_CONST               8 ('py1')
        # |                LOAD_CONST               9 ('books')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (books)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (books)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               9 ('books')
        # |        L6:     LOAD_CONST              10 ('py3')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py6')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format7)
        # |                LOAD_CONST              12 ('assert %(py8)s')
        # |                LOAD_CONST              13 ('py8')
        # |                LOAD_FAST_BORROW         8 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format9)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               26 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format9)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L7:     LOAD_CONST              14 (None)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  118 (@py_assert4, @py_assert5)
        # | 156            LOAD_FAST_BORROW         3 (dst)
        # |                LOAD_CONST              15 ('a.md')
        # |                BINARY_OP               11 (/)
        # |                LOAD_ATTR               29 (read_text + NULL|self)
        # |                LOAD_CONST               3 ('utf-8')
        # |                CALL                     1
        # |                STORE_FAST              10 (out)
        # | 157            BUILD_LIST               0
        # |                STORE_FAST_LOAD_FAST   186 (@py_assert1, out)
        # |                LOAD_ATTR               30 (startswith)
        # |                STORE_FAST              12 (@py_assert3)
        # |                LOAD_CONST              16 ('# a')
        # |                STORE_FAST_LOAD_FAST   108 (@py_assert5, @py_assert3)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   221 (@py_assert7, @py_assert7)
        # |                STORE_FAST_LOAD_FAST   237 (@py_assert0, @py_assert7)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE        9 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_CONST              17 ('## 第1章 初遇')
        # |                STORE_FAST_LOAD_FAST   255 (@py_assert10, @py_assert10)
        # |                LOAD_FAST_BORROW        10 (out)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST              16 (@py_assert12)
        # |                LOAD_FAST               16 (@py_assert12)
        # |                STORE_FAST              14 (@py_assert0)
        # |        L8:     LOAD_FAST_BORROW        14 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       413 (to L16)
        # |                NOT_TAKEN
        # |                LOAD_CONST              18 ('%(py8)s\n{%(py8)s = %(py4)s\n{%(py4)s = %(py2)s.startswith\n}(%(py6)s)\n}')
        # |                LOAD_CONST              19 ('py2')
        # |                LOAD_CONST              20 ('out')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (out)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L10)
        # |                NOT_TAKEN
        # |        L9:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (out)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L11)
        # |       L10:     LOAD_CONST              20 ('out')
        # |       L11:     LOAD_CONST              21 ('py4')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py6')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py8')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        13 (@py_assert7)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   155 (@py_format9, @py_assert1)
        # |                LOAD_ATTR               33 (append + NULL|self)
        # |                LOAD_FAST_BORROW         9 (@py_format9)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW        13 (@py_assert7)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      164 (to L15)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              30 (('in',))
        # |                LOAD_FAST_CHECK         16 (@py_assert12)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              31 (('%(py11)s in %(py13)s',))
        # |                LOAD_FAST_CHECK         15 (@py_assert10)
        # |                LOAD_FAST_BORROW        10 (out)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              22 ('py11')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        15 (@py_assert10)
        # |                CALL                     1
        # |                LOAD_CONST              23 ('py13')
        # |                LOAD_CONST              20 ('out')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (out)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L13)
        # |                NOT_TAKEN
        # |       L12:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (out)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L14)
        # |       L13:     LOAD_CONST              20 ('out')
        # |       L14:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format14)
        # |                LOAD_CONST              24 ('%(py15)s')
        # |                LOAD_CONST              25 ('py15')
        # |                LOAD_FAST_BORROW        17 (@py_format14)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format16)
        # |                LOAD_FAST_BORROW        11 (@py_assert1)
        # |                LOAD_ATTR               33 (append + NULL|self)
        # |                LOAD_FAST_BORROW        18 (@py_format16)
        # |                CALL                     1
        # |                POP_TOP
        # |       L15:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               34 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              19 (@py_format17)
        # |                LOAD_CONST              26 ('assert %(py18)s')
        # |                LOAD_CONST              27 ('py18')
        # |                LOAD_FAST_BORROW        19 (@py_format17)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              20 (@py_format19)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               26 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        20 (@py_format19)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L16:     LOAD_CONST              14 (None)
        # |                COPY                     1
        # |                STORE_FAST              14 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST              11 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST              12 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST              13 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST              15 (@py_assert10)
        # |                STORE_FAST              16 (@py_assert12)
        # |                LOAD_CONST              14 (None)
        # |                RETURN_VALUE

    def test_chapter_markdown_matches_gate_title_format(self):
        '清洗产物的标题格式要与 gate 的硬规范一致，否则语料没法当样本用。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 159           RESUME                   0
        # | 161           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (None)
        # |               IMPORT_NAME              0 (re)
        # |               STORE_FAST               1 (re)
        # |               LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (None)
        # |               IMPORT_NAME              1 (yaml)
        # |               STORE_FAST               2 (yaml)
        # | 162           LOAD_SMALL_INT           0
        # |               LOAD_CONST               2 (('Path',))
        # |               IMPORT_NAME              2 (pathlib)
        # |               IMPORT_FROM              3 (Path)
        # |               STORE_FAST               3 (Path)
        # |               POP_TOP
        # | 164           LOAD_FAST_BORROW         2 (yaml)
        # |               LOAD_ATTR                9 (safe_load + NULL|self)
        # | 165           LOAD_FAST_BORROW         3 (Path)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             10 (__file__)
        # |               CALL                     1
        # |               LOAD_ATTR               13 (resolve + NULL|self)
        # |               CALL                     0
        # |               LOAD_ATTR               14 (parent)
        # |               LOAD_ATTR               14 (parent)
        # |               LOAD_CONST               3 ('config')
        # |               BINARY_OP               11 (/)
        # |               LOAD_CONST               4 ('project.yaml')
        # |               BINARY_OP               11 (/)
        # |               LOAD_ATTR               17 (read_text + NULL|self)
        # |               LOAD_CONST               5 ('utf-8')
        # |               CALL                     1
        # | 164           CALL                     1
        # | 166           LOAD_CONST               6 ('format')
        # | 164           BINARY_OP               26 ([])
        # | 166           LOAD_CONST               7 ('chapter_title_pattern')
        # | 164           BINARY_OP               26 ([])
        # |               STORE_FAST               4 (pattern)
        # | 167           LOAD_GLOBAL             19 (Chapter + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               8 ('初遇')
        # |               LOAD_CONST               9 ('正文。')
        # |               CALL                     3
        # |               LOAD_ATTR               21 (to_markdown + NULL|self)
        # |               CALL                     0
        # |               STORE_FAST               5 (md)
        # | 168           LOAD_FAST_BORROW         1 (re)
        # |               LOAD_ATTR               22 (match)
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert1, md)
        # |               LOAD_ATTR               25 (splitlines + NULL|self)
        # |               CALL                     0
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert4, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (pattern, @py_assert4)
        # |               CALL                     2
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert6, @py_assert6)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       263 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_CONST              10 ('assert %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py3)s, %(py5)s)\n}')
        # |               LOAD_CONST              11 ('py0')
        # |               LOAD_CONST              12 ('re')
        # |               LOAD_GLOBAL             26 (@py_builtins)
        # |               LOAD_ATTR               28 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             30 (@pytest_ar)
        # |               LOAD_ATTR               32 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (re)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             30 (@pytest_ar)
        # |               LOAD_ATTR               34 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (re)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST              12 ('re')
        # |       L3:     LOAD_CONST              13 ('py2')
        # |               LOAD_GLOBAL             30 (@pytest_ar)
        # |               LOAD_ATTR               34 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              14 ('py3')
        # |               LOAD_CONST              15 ('pattern')
        # |               LOAD_GLOBAL             26 (@py_builtins)
        # |               LOAD_ATTR               28 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             30 (@pytest_ar)
        # |               LOAD_ATTR               32 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (pattern)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL             30 (@pytest_ar)
        # |               LOAD_ATTR               34 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (pattern)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST              15 ('pattern')
        # |       L6:     LOAD_CONST              16 ('py5')
        # |               LOAD_GLOBAL             30 (@pytest_ar)
        # |               LOAD_ATTR               34 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST              17 ('py7')
        # |               LOAD_GLOBAL             30 (@pytest_ar)
        # |               LOAD_ATTR               34 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert6)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format8)
        # |               LOAD_GLOBAL             37 (AssertionError + NULL)
        # |               LOAD_GLOBAL             30 (@pytest_ar)
        # |               LOAD_ATTR               38 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST               1 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert4, @py_assert6)
        # |               LOAD_CONST               1 (None)
        # |               RETURN_VALUE


class TestHeadingPatternSelection:
    'TestHeadingPatternSelection'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 171           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestHeadingPatternSelection')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         171
    # |               STORE_NAME               3 (__firstlineno__)
    # | 172           LOAD_CONST               1 ('模式之间存在包含关系（"第N章" ⊂ "第N"），按命中数取胜会让宽松模式\n永远赢，把「章」字留在标题里。实测 66 本语料暴露的问题。')
    # |               STORE_NAME               4 (__doc__)
    # | 175           LOAD_CONST               2 (<code object _detect at 0x1056f6c10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 175>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (_detect)
    # | 181           LOAD_CONST               3 (<code object test_specific_pattern_beats_looser_one at 0x75bd2c2a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 181>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_specific_pattern_beats_looser_one)
    # | 189           LOAD_CONST               4 (<code object test_counter_words_not_treated_as_chapters at 0x75bd2c3000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 189>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_counter_words_not_treated_as_chapters)
    # | 197           LOAD_NAME                8 (pytest)
    # |               LOAD_ATTR               18 (mark)
    # |               LOAD_ATTR               21 (parametrize + NULL|self)
    # | 198           LOAD_CONST               5 ('title,ok')
    # | 199           BUILD_LIST               0
    # |               LOAD_CONST               9 ((('再遇', True), ('你好，再见', True), ('(听说你还没有女朋友，那从……)', True), ('', True), ('第二天早上陆嫣照例是被闹钟叫醒的。', False), ('节比赛，公牛队三线开花！', False)))
    # |               LIST_EXTEND              1
    # | 197           CALL                     2
    # | 203           LOAD_CONST               6 (<code object test_title_plausibility at 0x75bcd97400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 197>)
    # |               MAKE_FUNCTION
    # | 197           CALL                     0
    # | 203           STORE_NAME              11 (test_title_plausibility)
    # |               LOAD_CONST               7 (())
    # |               STORE_NAME              12 (__static_attributes__)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object _detect at 0x1056f6c10, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 175>:
    # | 175           RESUME                   0
    # | 176           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('detect_heading_pattern',))
    # |               IMPORT_NAME              0 (novel_agent.corpus.ingest)
    # |               IMPORT_FROM              1 (detect_heading_pattern)
    # |               STORE_FAST               2 (detect_heading_pattern)
    # |               POP_TOP
    # | 178           LOAD_FAST_BORROW         2 (detect_heading_pattern)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (text)
    # |               CALL                     1
    # |               STORE_FAST               3 (d)
    # | 179           LOAD_FAST_BORROW         3 (d)
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       10 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_FAST_BORROW         3 (d)
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               RETURN_VALUE
    # |       L1:     LOAD_CONST               2 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_specific_pattern_beats_looser_one at 0x75bd2c2a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 181>:
    # |  181            RESUME                   0
    # |  183            LOAD_CONST               1 ('\n')
    # |                 LOAD_ATTR                1 (join + NULL|self)
    # |  184            LOAD_GLOBAL              3 (range + NULL)
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_SMALL_INT          21
    # |                 CALL                     2
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      1 (i)
    # |                 SWAP                     2
    # |         L1:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                19 (to L3)
    # |                 STORE_FAST               1 (i)
    # |                 LOAD_CONST               2 ('第')
    # |                 LOAD_FAST_BORROW         1 (i)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST               3 ('章 标题')
    # |                 LOAD_FAST_BORROW         1 (i)
    # |                 FORMAT_SIMPLE
    # |                 LOAD_CONST               1 ('\n')
    # |                 BUILD_STRING             5
    # |                 LOAD_CONST              19 ('正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n')
    # |                 BINARY_OP                0 (+)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           21 (to L2)
    # |         L3:     END_FOR
    # |                 POP_ITER
    # |         L4:     SWAP                     2
    # |                 STORE_FAST               1 (i)
    # |  183            CALL                     1
    # |                 STORE_FAST               2 (body)
    # |  186            LOAD_CONST               1 ('\n')
    # |                 LOAD_ATTR                1 (join + NULL|self)
    # |                 LOAD_CONST               4 (<code object <genexpr> at 0x1056d3430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 186>)
    # |                 MAKE_FUNCTION
    # |                 LOAD_GLOBAL              3 (range + NULL)
    # |                 LOAD_SMALL_INT           1
    # |                 LOAD_SMALL_INT          60
    # |                 CALL                     2
    # |                 GET_ITER
    # |                 CALL                     0
    # |                 CALL                     1
    # |                 STORE_FAST               3 (noise)
    # |  187            LOAD_FAST_BORROW         0 (self)
    # |                 LOAD_ATTR                4 (_detect)
    # |                 STORE_FAST               4 (@py_assert1)
    # |                 LOAD_CONST               1 ('\n')
    # |                 STORE_FAST_LOAD_FAST    82 (@py_assert4, body)
    # |                 LOAD_FAST_BORROW         5 (@py_assert4)
    # |                 BINARY_OP                0 (+)
    # |                 STORE_FAST_LOAD_FAST   102 (@py_assert6, @py_assert6)
    # |                 LOAD_FAST_BORROW         3 (noise)
    # |                 BINARY_OP                0 (+)
    # |                 STORE_FAST_LOAD_FAST   116 (@py_assert8, @py_assert1)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert8)
    # |                 CALL                     1
    # |                 STORE_FAST               8 (@py_assert9)
    # |                 LOAD_CONST               5 ('第N章')
    # |                 STORE_FAST_LOAD_FAST   152 (@py_assert12, @py_assert9)
    # |                 LOAD_FAST_BORROW         9 (@py_assert12)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   170 (@py_assert11, @py_assert11)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       399 (to L14)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR                8 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              20 (('==',))
    # |                 LOAD_FAST_BORROW        10 (@py_assert11)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              21 (('%(py10)s\n{%(py10)s = %(py2)s\n{%(py2)s = %(py0)s._detect\n}(((%(py3)s + %(py5)s) + %(py7)s))\n} == %(py13)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert9, @py_assert12)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               6 ('py0')
    # |                 LOAD_CONST               7 ('self')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L5)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         0 (self)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L6)
    # |                 NOT_TAKEN
    # |         L5:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         0 (self)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L7)
    # |         L6:     LOAD_CONST               7 ('self')
    # |         L7:     LOAD_CONST               8 ('py2')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST               9 ('py3')
    # |                 LOAD_CONST              10 ('body')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L8)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               14 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (body)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L9)
    # |                 NOT_TAKEN
    # |         L8:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         2 (body)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L10)
    # |         L9:     LOAD_CONST              10 ('body')
    # |        L10:     LOAD_CONST              11 ('py5')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert4)
    # |                 CALL                     1
    # |                 LOAD_CONST              12 ('py7')
    # |                 LOAD_CONST              13 ('noise')
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
    # |                 LOAD_FAST_BORROW         3 (noise)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L12)
    # |                 NOT_TAKEN
    # |        L11:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (noise)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L13)
    # |        L12:     LOAD_CONST              13 ('noise')
    # |        L13:     LOAD_CONST              14 ('py10')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         8 (@py_assert9)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py13')
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_assert12)
    # |                 CALL                     1
    # |                 BUILD_MAP                7
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              11 (@py_format14)
    # |                 LOAD_CONST              16 ('assert %(py15)s')
    # |                 LOAD_CONST              17 ('py15')
    # |                 LOAD_FAST_BORROW        11 (@py_format14)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format16)
    # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              6 (@pytest_ar)
    # |                 LOAD_ATTR               20 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        12 (@py_format16)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L14:     LOAD_CONST              18 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               4 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert4)
    # |                 COPY                     1
    # |                 STORE_FAST               6 (@py_assert6)
    # |                 COPY                     1
    # |                 STORE_FAST               7 (@py_assert8)
    # |                 COPY                     1
    # |                 STORE_FAST               8 (@py_assert9)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  169 (@py_assert11, @py_assert12)
    # |                 LOAD_CONST              18 (None)
    # |                 RETURN_VALUE
    # |   --   L15:     SWAP                     2
    # |                 POP_TOP
    # |  184            SWAP                     2
    # |                 STORE_FAST               1 (i)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L4 -> L15 [4]
    # | Disassembly of <code object <genexpr> at 0x1056d3430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 186>:
    # |  186           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                11 (to L3)
    # |                STORE_FAST               1 (i)
    # |                LOAD_CONST               0 ('第')
    # |                LOAD_FAST_BORROW         1 (i)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               1 ('页')
    # |                BUILD_STRING             3
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           13 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               2 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
    # | Disassembly of <code object test_counter_words_not_treated_as_chapters at 0x75bd2c3000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 189>:
    # | 189            RESUME                   0
    # | 190            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('_HEADING_PATTERNS',))
    # |                IMPORT_NAME              0 (novel_agent.corpus.ingest)
    # |                IMPORT_FROM              1 (_HEADING_PATTERNS)
    # |                STORE_FAST               1 (_HEADING_PATTERNS)
    # |                POP_TOP
    # | 192            LOAD_GLOBAL              5 (dict + NULL)
    # |                LOAD_FAST_BORROW         1 (_HEADING_PATTERNS)
    # |                CALL                     1
    # |                LOAD_CONST               2 ('第N')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               2 (bare)
    # | 193            LOAD_CONST              17 (('第1页', '第3次', '第二节', '第五局'))
    # |                GET_ITER
    # |        L1:     EXTENDED_ARG             1
    # |                FOR_ITER               312 (to L9)
    # |                STORE_FAST               3 (counter)
    # | 194            LOAD_FAST_BORROW         2 (bare)
    # |                LOAD_ATTR                6 (match)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (counter)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert6, @py_assert6)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       271 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (counter)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               3 (' 不该被当成章节标记')
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                LOAD_CONST               4 ('\n>assert not %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py3)s)\n}')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('bare')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (bare)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (bare)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST               6 ('bare')
    # |        L4:     LOAD_CONST               7 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py3')
    # |                LOAD_CONST               9 ('counter')
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
    # |                LOAD_FAST_BORROW         3 (counter)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (counter)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST               9 ('counter')
    # |        L7:     LOAD_CONST              10 ('py5')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format7)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert4, @py_assert6)
    # |                EXTENDED_ARG             1
    # |                JUMP_BACKWARD          315 (to L1)
    # | 193    L9:     END_FOR
    # |                POP_ITER
    # | 195            LOAD_FAST_BORROW         2 (bare)
    # |                LOAD_ATTR                6 (match)
    # |                STORE_FAST               4 (@py_assert1)
    # |                LOAD_CONST              12 ('第1 楔子')
    # |                STORE_FAST_LOAD_FAST   132 (@py_assert3, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       212 (to L13)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              13 ('真正的无「章」标记要能匹配')
    # |                CALL                     1
    # |                LOAD_CONST              14 ('\n>assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py4)s)\n}')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               5 ('py0')
    # |                LOAD_CONST               6 ('bare')
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
    # |                LOAD_FAST_BORROW         2 (bare)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L11)
    # |                NOT_TAKEN
    # |       L10:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (bare)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L12)
    # |       L11:     LOAD_CONST               6 ('bare')
    # |       L12:     LOAD_CONST               7 ('py2')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py4')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST              16 ('py6')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format7)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L13:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  137 (@py_assert3, @py_assert5)
    # |                LOAD_CONST              11 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_title_plausibility at 0x75bcd97400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 197>:
    # | 197            RESUME                   0
    # | 206            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('is_plausible_title',))
    # |                IMPORT_NAME              0 (novel_agent.corpus.ingest)
    # |                IMPORT_FROM              1 (is_plausible_title)
    # |                STORE_FAST               3 (is_plausible_title)
    # |                POP_TOP
    # | 208            LOAD_FAST_BORROW         3 (is_plausible_title)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (title)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         2 (ok)
    # |                IS_OP                    0 (is)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       333 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR                6 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              12 (('is',))
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              13 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} is %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (@py_assert2, ok)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py0')
    # |                LOAD_CONST               3 ('is_plausible_title')
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
    # |                LOAD_FAST_BORROW         3 (is_plausible_title)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (is_plausible_title)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               3 ('is_plausible_title')
    # |        L3:     LOAD_CONST               4 ('py1')
    # |                LOAD_CONST               5 ('title')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (title)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (title)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               5 ('title')
    # |        L6:     LOAD_CONST               6 ('py3')
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               7 ('py5')
    # |                LOAD_CONST               8 ('ok')
    # |                LOAD_GLOBAL              8 (@py_builtins)
    # |                LOAD_ATTR               10 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               12 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (ok)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (ok)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               8 ('ok')
    # |        L9:     BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               6 (@py_format6)
    # |                LOAD_CONST               9 ('assert %(py7)s')
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_FAST_BORROW         6 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               7 (@py_format8)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              4 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   69 (@py_assert2, @py_assert4)
    # |                LOAD_CONST              11 (None)
    # |                RETURN_VALUE

    def _detect(self, text):
        pass  # 无 docstring
        # ── 函数体（字节码重建见 BODY 段）──
        # | 175           RESUME                   0
        # | 176           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('detect_heading_pattern',))
        # |               IMPORT_NAME              0 (novel_agent.corpus.ingest)
        # |               IMPORT_FROM              1 (detect_heading_pattern)
        # |               STORE_FAST               2 (detect_heading_pattern)
        # |               POP_TOP
        # | 178           LOAD_FAST_BORROW         2 (detect_heading_pattern)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (text)
        # |               CALL                     1
        # |               STORE_FAST               3 (d)
        # | 179           LOAD_FAST_BORROW         3 (d)
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       10 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_FAST_BORROW         3 (d)
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               RETURN_VALUE
        # |       L1:     LOAD_CONST               2 (None)
        # |               RETURN_VALUE

    def test_specific_pattern_beats_looser_one(self):
        '真章节 + 大量正文噪声时，仍要选中 第N章。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  181            RESUME                   0
        # |  183            LOAD_CONST               1 ('\n')
        # |                 LOAD_ATTR                1 (join + NULL|self)
        # |  184            LOAD_GLOBAL              3 (range + NULL)
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_SMALL_INT          21
        # |                 CALL                     2
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      1 (i)
        # |                 SWAP                     2
        # |         L1:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                19 (to L3)
        # |                 STORE_FAST               1 (i)
        # |                 LOAD_CONST               2 ('第')
        # |                 LOAD_FAST_BORROW         1 (i)
        # |                 FORMAT_SIMPLE
        # |                 LOAD_CONST               3 ('章 标题')
        # |                 LOAD_FAST_BORROW         1 (i)
        # |                 FORMAT_SIMPLE
        # |                 LOAD_CONST               1 ('\n')
        # |                 BUILD_STRING             5
        # |                 LOAD_CONST              19 ('正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n正文一段。\n')
        # |                 BINARY_OP                0 (+)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           21 (to L2)
        # |         L3:     END_FOR
        # |                 POP_ITER
        # |         L4:     SWAP                     2
        # |                 STORE_FAST               1 (i)
        # |  183            CALL                     1
        # |                 STORE_FAST               2 (body)
        # |  186            LOAD_CONST               1 ('\n')
        # |                 LOAD_ATTR                1 (join + NULL|self)
        # |                 LOAD_CONST               4 (<code object <genexpr> at 0x1056d3430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 186>)
        # |                 MAKE_FUNCTION
        # |                 LOAD_GLOBAL              3 (range + NULL)
        # |                 LOAD_SMALL_INT           1
        # |                 LOAD_SMALL_INT          60
        # |                 CALL                     2
        # |                 GET_ITER
        # |                 CALL                     0
        # |                 CALL                     1
        # |                 STORE_FAST               3 (noise)
        # |  187            LOAD_FAST_BORROW         0 (self)
        # |                 LOAD_ATTR                4 (_detect)
        # |                 STORE_FAST               4 (@py_assert1)
        # |                 LOAD_CONST               1 ('\n')
        # |                 STORE_FAST_LOAD_FAST    82 (@py_assert4, body)
        # |                 LOAD_FAST_BORROW         5 (@py_assert4)
        # |                 BINARY_OP                0 (+)
        # |                 STORE_FAST_LOAD_FAST   102 (@py_assert6, @py_assert6)
        # |                 LOAD_FAST_BORROW         3 (noise)
        # |                 BINARY_OP                0 (+)
        # |                 STORE_FAST_LOAD_FAST   116 (@py_assert8, @py_assert1)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert8)
        # |                 CALL                     1
        # |                 STORE_FAST               8 (@py_assert9)
        # |                 LOAD_CONST               5 ('第N章')
        # |                 STORE_FAST_LOAD_FAST   152 (@py_assert12, @py_assert9)
        # |                 LOAD_FAST_BORROW         9 (@py_assert12)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   170 (@py_assert11, @py_assert11)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       399 (to L14)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR                8 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              20 (('==',))
        # |                 LOAD_FAST_BORROW        10 (@py_assert11)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              21 (('%(py10)s\n{%(py10)s = %(py2)s\n{%(py2)s = %(py0)s._detect\n}(((%(py3)s + %(py5)s) + %(py7)s))\n} == %(py13)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 137 (@py_assert9, @py_assert12)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               6 ('py0')
        # |                 LOAD_CONST               7 ('self')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L5)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         0 (self)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L6)
        # |                 NOT_TAKEN
        # |         L5:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         0 (self)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L7)
        # |         L6:     LOAD_CONST               7 ('self')
        # |         L7:     LOAD_CONST               8 ('py2')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST               9 ('py3')
        # |                 LOAD_CONST              10 ('body')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L8)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               14 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (body)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L9)
        # |                 NOT_TAKEN
        # |         L8:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         2 (body)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L10)
        # |         L9:     LOAD_CONST              10 ('body')
        # |        L10:     LOAD_CONST              11 ('py5')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert4)
        # |                 CALL                     1
        # |                 LOAD_CONST              12 ('py7')
        # |                 LOAD_CONST              13 ('noise')
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
        # |                 LOAD_FAST_BORROW         3 (noise)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L12)
        # |                 NOT_TAKEN
        # |        L11:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (noise)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L13)
        # |        L12:     LOAD_CONST              13 ('noise')
        # |        L13:     LOAD_CONST              14 ('py10')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         8 (@py_assert9)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py13')
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_assert12)
        # |                 CALL                     1
        # |                 BUILD_MAP                7
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              11 (@py_format14)
        # |                 LOAD_CONST              16 ('assert %(py15)s')
        # |                 LOAD_CONST              17 ('py15')
        # |                 LOAD_FAST_BORROW        11 (@py_format14)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format16)
        # |                 LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              6 (@pytest_ar)
        # |                 LOAD_ATTR               20 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        12 (@py_format16)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L14:     LOAD_CONST              18 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               4 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert4)
        # |                 COPY                     1
        # |                 STORE_FAST               6 (@py_assert6)
        # |                 COPY                     1
        # |                 STORE_FAST               7 (@py_assert8)
        # |                 COPY                     1
        # |                 STORE_FAST               8 (@py_assert9)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  169 (@py_assert11, @py_assert12)
        # |                 LOAD_CONST              18 (None)
        # |                 RETURN_VALUE
        # |   --   L15:     SWAP                     2
        # |                 POP_TOP
        # |  184            SWAP                     2
        # |                 STORE_FAST               1 (i)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L4 -> L15 [4]
        # | Disassembly of <code object <genexpr> at 0x1056d3430, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 186>:
        # |  186           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                11 (to L3)
        # |                STORE_FAST               1 (i)
        # |                LOAD_CONST               0 ('第')
        # |                LOAD_FAST_BORROW         1 (i)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST               1 ('页')
        # |                BUILD_STRING             3
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           13 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               2 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti

    def test_counter_words_not_treated_as_chapters(self):
        '第N'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 189            RESUME                   0
        # | 190            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('_HEADING_PATTERNS',))
        # |                IMPORT_NAME              0 (novel_agent.corpus.ingest)
        # |                IMPORT_FROM              1 (_HEADING_PATTERNS)
        # |                STORE_FAST               1 (_HEADING_PATTERNS)
        # |                POP_TOP
        # | 192            LOAD_GLOBAL              5 (dict + NULL)
        # |                LOAD_FAST_BORROW         1 (_HEADING_PATTERNS)
        # |                CALL                     1
        # |                LOAD_CONST               2 ('第N')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               2 (bare)
        # | 193            LOAD_CONST              17 (('第1页', '第3次', '第二节', '第五局'))
        # |                GET_ITER
        # |        L1:     EXTENDED_ARG             1
        # |                FOR_ITER               312 (to L9)
        # |                STORE_FAST               3 (counter)
        # | 194            LOAD_FAST_BORROW         2 (bare)
        # |                LOAD_ATTR                6 (match)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (counter)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                UNARY_NOT
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert6, @py_assert6)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       271 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (counter)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST               3 (' 不该被当成章节标记')
        # |                BUILD_STRING             2
        # |                CALL                     1
        # |                LOAD_CONST               4 ('\n>assert not %(py5)s\n{%(py5)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py3)s)\n}')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('bare')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (bare)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (bare)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST               6 ('bare')
        # |        L4:     LOAD_CONST               7 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py3')
        # |                LOAD_CONST               9 ('counter')
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
        # |                LOAD_FAST_BORROW         3 (counter)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (counter)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST               9 ('counter')
        # |        L7:     LOAD_CONST              10 ('py5')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format7)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST              11 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert4, @py_assert6)
        # |                EXTENDED_ARG             1
        # |                JUMP_BACKWARD          315 (to L1)
        # | 193    L9:     END_FOR
        # |                POP_ITER
        # | 195            LOAD_FAST_BORROW         2 (bare)
        # |                LOAD_ATTR                6 (match)
        # |                STORE_FAST               4 (@py_assert1)
        # |                LOAD_CONST              12 ('第1 楔子')
        # |                STORE_FAST_LOAD_FAST   132 (@py_assert3, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       212 (to L13)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              13 ('真正的无「章」标记要能匹配')
        # |                CALL                     1
        # |                LOAD_CONST              14 ('\n>assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s.match\n}(%(py4)s)\n}')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               5 ('py0')
        # |                LOAD_CONST               6 ('bare')
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
        # |                LOAD_FAST_BORROW         2 (bare)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L11)
        # |                NOT_TAKEN
        # |       L10:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (bare)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L12)
        # |       L11:     LOAD_CONST               6 ('bare')
        # |       L12:     LOAD_CONST               7 ('py2')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py4')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST              16 ('py6')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format7)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L13:     LOAD_CONST              11 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  137 (@py_assert3, @py_assert5)
        # |                LOAD_CONST              11 (None)
        # |                RETURN_VALUE

    def test_title_plausibility(self, title, ok):
        '正文行会被宽松模式误判成标题，句末标点是最可靠的区分点。\n但逗号和省略号常见于真标题，不能一起排除。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 197            RESUME                   0
        # | 206            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('is_plausible_title',))
        # |                IMPORT_NAME              0 (novel_agent.corpus.ingest)
        # |                IMPORT_FROM              1 (is_plausible_title)
        # |                STORE_FAST               3 (is_plausible_title)
        # |                POP_TOP
        # | 208            LOAD_FAST_BORROW         3 (is_plausible_title)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (title)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         2 (ok)
        # |                IS_OP                    0 (is)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert4, @py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       333 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR                6 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              12 (('is',))
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              13 (('%(py3)s\n{%(py3)s = %(py0)s(%(py1)s)\n} is %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (@py_assert2, ok)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py0')
        # |                LOAD_CONST               3 ('is_plausible_title')
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
        # |                LOAD_FAST_BORROW         3 (is_plausible_title)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (is_plausible_title)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               3 ('is_plausible_title')
        # |        L3:     LOAD_CONST               4 ('py1')
        # |                LOAD_CONST               5 ('title')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (title)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (title)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               5 ('title')
        # |        L6:     LOAD_CONST               6 ('py3')
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               7 ('py5')
        # |                LOAD_CONST               8 ('ok')
        # |                LOAD_GLOBAL              8 (@py_builtins)
        # |                LOAD_ATTR               10 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               12 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (ok)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (ok)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               8 ('ok')
        # |        L9:     BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               6 (@py_format6)
        # |                LOAD_CONST               9 ('assert %(py7)s')
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_FAST_BORROW         6 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               7 (@py_format8)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              4 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              11 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   69 (@py_assert2, @py_assert4)
        # |                LOAD_CONST              11 (None)
        # |                RETURN_VALUE


class TestEpub:
    'TestEpub'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 211           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestEpub')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         211
    # |               STORE_NAME               3 (__firstlineno__)
    # | 212           LOAD_CONST               1 (<code object _make_epub at 0x75bd2f1500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 212>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (_make_epub)
    # | 235           LOAD_CONST               2 (<code object test_reads_epub_in_spine_order at 0x75bd119e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 235>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_reads_epub_in_spine_order)
    # | 245           LOAD_CONST               3 (<code object test_html_tags_stripped at 0x75bccb6a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 245>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_html_tags_stripped)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object _make_epub at 0x75bd2f1500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 212>:
    # |   --           MAKE_CELL               11 (body)
    # |  212           RESUME                   0
    # |  213           LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (None)
    # |                IMPORT_NAME              0 (zipfile)
    # |                STORE_FAST               3 (zipfile)
    # |  215           LOAD_FAST_BORROW         3 (zipfile)
    # |                LOAD_ATTR                3 (ZipFile + NULL|self)
    # |                LOAD_FAST_BORROW         1 (path)
    # |                LOAD_CONST               2 ('w')
    # |                CALL                     2
    # |                COPY                     1
    # |                LOAD_SPECIAL             1 (__exit__)
    # |                SWAP                     2
    # |                SWAP                     3
    # |                LOAD_SPECIAL             0 (__enter__)
    # |                CALL                     0
    # |        L1:     STORE_FAST               4 (zf)
    # |  216           LOAD_FAST_BORROW         4 (zf)
    # |                LOAD_ATTR                5 (writestr + NULL|self)
    # |                LOAD_CONST               3 ('META-INF/container.xml')
    # |  217           LOAD_CONST               4 ('<?xml version="1.0"?><container xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf"/></rootfiles></container>')
    # |  216           CALL                     2
    # |                POP_TOP
    # |  220           BUILD_LIST               0
    # |                BUILD_LIST               0
    # |                STORE_FAST_STORE_FAST  101 (refs, items)
    # |  221           LOAD_GLOBAL              7 (enumerate + NULL)
    # |                LOAD_FAST_BORROW         2 (chapters)
    # |                LOAD_SMALL_INT           1
    # |                CALL                     2
    # |                GET_ITER
    # |        L2:     FOR_ITER               128 (to L3)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST               7 (i)
    # |                UNPACK_SEQUENCE          2
    # |                STORE_FAST               8 (title)
    # |                STORE_DEREF             11 (body)
    # |  222           LOAD_CONST               5 ('c')
    # |                LOAD_FAST_BORROW         7 (i)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               6 ('.xhtml')
    # |                BUILD_STRING             3
    # |                STORE_FAST               9 (name)
    # |  225           LOAD_CONST               7 ('')
    # |                LOAD_ATTR                9 (join + NULL|self)
    # |                LOAD_FAST_BORROW        11 (body)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST               8 (<code object <genexpr> at 0x1057ac030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 225>)
    # |                MAKE_FUNCTION
    # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
    # |                LOAD_GLOBAL             11 (range + NULL)
    # |                LOAD_SMALL_INT           1
    # |                LOAD_SMALL_INT           9
    # |                CALL                     2
    # |                GET_ITER
    # |                CALL                     0
    # |                CALL                     1
    # |                STORE_FAST              10 (paras)
    # |  226           LOAD_FAST_BORROW         4 (zf)
    # |                LOAD_ATTR                5 (writestr + NULL|self)
    # |                LOAD_CONST               9 ('OEBPS/')
    # |                LOAD_FAST_BORROW         9 (name)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |  227           LOAD_CONST              10 ('<html><body><h1>第')
    # |                LOAD_FAST_BORROW         7 (i)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              11 ('章 ')
    # |                LOAD_FAST_BORROW         8 (title)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              12 ('</h1>')
    # |                LOAD_FAST_BORROW        10 (paras)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              13 ('</body></html>')
    # |                BUILD_STRING             7
    # |  226           CALL                     2
    # |                POP_TOP
    # |  228           LOAD_FAST_BORROW         5 (items)
    # |                LOAD_ATTR               13 (append + NULL|self)
    # |                LOAD_CONST              14 ('<item id="i')
    # |                LOAD_FAST_BORROW         7 (i)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              15 ('" href="')
    # |                LOAD_FAST_BORROW         9 (name)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              16 ('" media-type="application/xhtml+xml"/>')
    # |                BUILD_STRING             5
    # |                CALL                     1
    # |                POP_TOP
    # |  229           LOAD_FAST_BORROW         6 (refs)
    # |                LOAD_ATTR               13 (append + NULL|self)
    # |                LOAD_CONST              17 ('<itemref idref="i')
    # |                LOAD_FAST_BORROW         7 (i)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              18 ('"/>')
    # |                BUILD_STRING             3
    # |                CALL                     1
    # |                POP_TOP
    # |                JUMP_BACKWARD          130 (to L2)
    # |  221   L3:     END_FOR
    # |                POP_ITER
    # |  230           LOAD_FAST_BORROW         4 (zf)
    # |                LOAD_ATTR                5 (writestr + NULL|self)
    # |                LOAD_CONST              19 ('OEBPS/content.opf')
    # |  231           LOAD_CONST              20 ('<?xml version="1.0"?><package xmlns="http://www.idpf.org/2007/opf"><manifest>')
    # |  232           LOAD_CONST               7 ('')
    # |                LOAD_ATTR                9 (join + NULL|self)
    # |                LOAD_FAST_BORROW         5 (items)
    # |                CALL                     1
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              21 ('</manifest><spine>')
    # |  233           LOAD_CONST               7 ('')
    # |                LOAD_ATTR                9 (join + NULL|self)
    # |                LOAD_FAST_BORROW         6 (refs)
    # |                CALL                     1
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST              22 ('</spine></package>')
    # |  231           BUILD_STRING             5
    # |  230           CALL                     2
    # |                POP_TOP
    # |  215   L4:     LOAD_CONST               1 (None)
    # |                LOAD_CONST               1 (None)
    # |                LOAD_CONST               1 (None)
    # |                CALL                     3
    # |                POP_TOP
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |        L5:     PUSH_EXC_INFO
    # |                WITH_EXCEPT_START
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE         2 (to L6)
    # |                NOT_TAKEN
    # |                RERAISE                  2
    # |        L6:     POP_TOP
    # |        L7:     POP_EXCEPT
    # |                POP_TOP
    # |                POP_TOP
    # |                POP_TOP
    # |                LOAD_CONST               1 (None)
    # |                RETURN_VALUE
    # |   --   L8:     COPY                     3
    # |                POP_EXCEPT
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L5 [2] lasti
    # |   L5 to L7 -> L8 [4] lasti
    # | Disassembly of <code object <genexpr> at 0x1057ac030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 225>:
    # |   --           COPY_FREE_VARS           1
    # |  225           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                14 (to L3)
    # |                STORE_FAST               1 (n)
    # |                LOAD_CONST               0 ('<p>')
    # |                LOAD_DEREF               2 (body)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               1 ('第')
    # |                LOAD_FAST_BORROW         1 (n)
    # |                FORMAT_SIMPLE
    # |                LOAD_CONST               2 ('段。</p>')
    # |                BUILD_STRING             5
    # |                YIELD_VALUE              0
    # |                RESUME                   5
    # |                POP_TOP
    # |                JUMP_BACKWARD           16 (to L2)
    # |        L3:     END_FOR
    # |                POP_ITER
    # |                LOAD_CONST               3 (None)
    # |                RETURN_VALUE
    # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
    # |                RERAISE                  1
    # | ExceptionTable:
    # |   L1 to L4 -> L4 [0] lasti
    # | Disassembly of <code object test_reads_epub_in_spine_order at 0x75bd119e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 235>:
    # |  235            RESUME                   0
    # |  236            LOAD_SMALL_INT           0
    # |                 LOAD_CONST               1 (('ingest_file',))
    # |                 IMPORT_NAME              0 (novel_agent.corpus.ingest)
    # |                 IMPORT_FROM              1 (ingest_file)
    # |                 STORE_FAST               2 (ingest_file)
    # |                 POP_TOP
    # |  238            LOAD_FAST_BORROW         1 (tmp_path)
    # |                 LOAD_CONST               2 ('book.epub')
    # |                 BINARY_OP               11 (/)
    # |                 STORE_FAST               3 (f)
    # |  239            LOAD_FAST_BORROW         0 (self)
    # |                 LOAD_ATTR                5 (_make_epub + NULL|self)
    # |                 LOAD_FAST_BORROW         3 (f)
    # |                 LOAD_CONST              20 (('初遇', '第一章的正文。'))
    # |                 LOAD_CONST              21 (('重逢', '第二章的正文。'))
    # |                 BUILD_LIST               2
    # |                 CALL                     2
    # |                 POP_TOP
    # |  240            LOAD_FAST_BORROW         2 (ingest_file)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         3 (f)
    # |                 CALL                     1
    # |                 STORE_FAST               4 (book)
    # |  241            LOAD_FAST_BORROW         4 (book)
    # |                 LOAD_ATTR                6 (encoding)
    # |                 STORE_FAST               5 (@py_assert1)
    # |                 LOAD_CONST               6 ('epub')
    # |                 STORE_FAST_LOAD_FAST   101 (@py_assert4, @py_assert1)
    # |                 LOAD_FAST_BORROW         6 (@py_assert4)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       199 (to L4)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              22 (('==',))
    # |                 LOAD_FAST_BORROW         7 (@py_assert3)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              23 (('%(py2)s\n{%(py2)s = %(py0)s.encoding\n} == %(py5)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert1, @py_assert4)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST               7 ('py0')
    # |                 LOAD_CONST               8 ('book')
    # |                 LOAD_GLOBAL             12 (@py_builtins)
    # |                 LOAD_ATTR               14 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L1)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (book)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L2)
    # |                 NOT_TAKEN
    # |         L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         4 (book)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L3)
    # |         L2:     LOAD_CONST               8 ('book')
    # |         L3:     LOAD_CONST               9 ('py2')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (@py_assert1)
    # |                 CALL                     1
    # |                 LOAD_CONST              10 ('py5')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (@py_assert4)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               8 (@py_format6)
    # |                 LOAD_CONST              11 ('assert %(py7)s')
    # |                 LOAD_CONST              12 ('py7')
    # |                 LOAD_FAST_BORROW         8 (@py_format6)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST               9 (@py_format8)
    # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         9 (@py_format8)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L4:     LOAD_CONST              13 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               5 (@py_assert1)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  118 (@py_assert3, @py_assert4)
    # |  242            LOAD_FAST_BORROW         4 (book)
    # |                 LOAD_ATTR               24 (chapters)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR     10 (c)
    # |                 SWAP                     2
    # |         L5:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L6:     FOR_ITER                14 (to L7)
    # |                 STORE_FAST_LOAD_FAST   170 (c, c)
    # |                 LOAD_ATTR               26 (title)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           16 (to L6)
    # |         L7:     END_FOR
    # |                 POP_ITER
    # |         L8:     STORE_FAST              11 (@py_assert0)
    # |                 STORE_FAST              10 (c)
    # |                 LOAD_CONST               3 ('初遇')
    # |                 LOAD_CONST               5 ('重逢')
    # |                 BUILD_LIST               2
    # |                 STORE_FAST_LOAD_FAST   123 (@py_assert3, @py_assert0)
    # |                 LOAD_FAST_BORROW         7 (@py_assert3)
    # |                 COMPARE_OP              72 (==)
    # |                 STORE_FAST_LOAD_FAST   204 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       121 (to L9)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              22 (('==',))
    # |                 LOAD_FAST_BORROW        12 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              24 (('%(py1)s == %(py4)s',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 183 (@py_assert0, @py_assert3)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST              14 ('py1')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py4')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert3)
    # |                 CALL                     1
    # |                 BUILD_MAP                2
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format5)
    # |                 LOAD_CONST              16 ('assert %(py6)s')
    # |                 LOAD_CONST              17 ('py6')
    # |                 LOAD_FAST_BORROW        13 (@py_format5)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              14 (@py_format7)
    # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        14 (@py_format7)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |         L9:     LOAD_CONST              13 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              11 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  199 (@py_assert2, @py_assert3)
    # |  243            LOAD_CONST               4 ('第一章的正文。')
    # |                 STORE_FAST_LOAD_FAST   180 (@py_assert0, book)
    # |                 LOAD_ATTR               24 (chapters)
    # |                 LOAD_SMALL_INT           0
    # |                 BINARY_OP               26 ([])
    # |                 STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
    # |                 LOAD_ATTR               28 (body)
    # |                 STORE_FAST_LOAD_FAST   251 (@py_assert5, @py_assert0)
    # |                 LOAD_FAST_BORROW        15 (@py_assert5)
    # |                 CONTAINS_OP              0 (in)
    # |                 STORE_FAST_LOAD_FAST   204 (@py_assert2, @py_assert2)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_TRUE       143 (to L10)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               10 (_call_reprcompare)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              25 (('in',))
    # |                 LOAD_FAST_BORROW        12 (@py_assert2)
    # |                 BUILD_TUPLE              1
    # |                 LOAD_CONST              26 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.body\n}',))
    # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 191 (@py_assert0, @py_assert5)
    # |                 BUILD_TUPLE              2
    # |                 CALL                     4
    # |                 LOAD_CONST              14 ('py1')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        11 (@py_assert0)
    # |                 CALL                     1
    # |                 LOAD_CONST              15 ('py4')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert3)
    # |                 CALL                     1
    # |                 LOAD_CONST              17 ('py6')
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        15 (@py_assert5)
    # |                 CALL                     1
    # |                 BUILD_MAP                3
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              14 (@py_format7)
    # |                 LOAD_CONST              18 ('assert %(py8)s')
    # |                 LOAD_CONST              19 ('py8')
    # |                 LOAD_FAST_BORROW        14 (@py_format7)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              16 (@py_format9)
    # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                 LOAD_GLOBAL              8 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        16 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L10:     LOAD_CONST              13 (None)
    # |                 COPY                     1
    # |                 STORE_FAST              11 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST              12 (@py_assert2)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  127 (@py_assert3, @py_assert5)
    # |                 LOAD_CONST              13 (None)
    # |                 RETURN_VALUE
    # |   --   L11:     SWAP                     2
    # |                 POP_TOP
    # |  242            SWAP                     2
    # |                 STORE_FAST              10 (c)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L5 to L8 -> L11 [2]
    # | Disassembly of <code object test_html_tags_stripped at 0x75bccb6a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 245>:
    # | 245            RESUME                   0
    # | 246            LOAD_SMALL_INT           0
    # |                LOAD_CONST               1 (('ingest_file',))
    # |                IMPORT_NAME              0 (novel_agent.corpus.ingest)
    # |                IMPORT_FROM              1 (ingest_file)
    # |                STORE_FAST               2 (ingest_file)
    # |                POP_TOP
    # | 248            LOAD_FAST_BORROW         1 (tmp_path)
    # |                LOAD_CONST               2 ('b.epub')
    # |                BINARY_OP               11 (/)
    # |                STORE_FAST               3 (f)
    # | 249            LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                5 (_make_epub + NULL|self)
    # |                LOAD_FAST_BORROW         3 (f)
    # |                LOAD_CONST              24 (('t', '正文有<em>强调</em>与&amp;实体。'))
    # |                BUILD_LIST               1
    # |                CALL                     2
    # |                POP_TOP
    # | 250            LOAD_CONST               3 ('\n')
    # |                LOAD_ATTR                7 (join + NULL|self)
    # |                LOAD_CONST               4 (<code object <genexpr> at 0x1057ac470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 250>)
    # |                MAKE_FUNCTION
    # |                LOAD_FAST_BORROW         2 (ingest_file)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (f)
    # |                CALL                     1
    # |                LOAD_ATTR                8 (chapters)
    # |                GET_ITER
    # |                CALL                     0
    # |                CALL                     1
    # |                STORE_FAST               4 (body)
    # | 251            BUILD_LIST               0
    # |                STORE_FAST               5 (@py_assert1)
    # |                LOAD_CONST               5 ('<em>')
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
    # |                STORE_FAST_LOAD_FAST   135 (@py_assert0, @py_assert4)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       22 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_CONST               6 ('强调')
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert9, @py_assert9)
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   170 (@py_assert11, @py_assert11)
    # |                STORE_FAST_LOAD_FAST   138 (@py_assert0, @py_assert11)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        8 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_CONST               7 ('&')
    # |                STORE_FAST_LOAD_FAST   187 (@py_assert16, @py_assert16)
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   204 (@py_assert18, @py_assert18)
    # |                STORE_FAST               8 (@py_assert0)
    # |        L1:     LOAD_FAST_BORROW         8 (@py_assert0)
    # |                TO_BOOL
    # |                EXTENDED_ARG             2
    # |                POP_JUMP_IF_TRUE       577 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              25 (('not in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              26 (('%(py3)s not in %(py5)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (@py_assert2, body)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               8 ('py3')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py5')
    # |                LOAD_CONST              10 ('body')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST              10 ('body')
    # |        L4:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              13 (@py_format6)
    # |                LOAD_CONST              11 ('%(py7)s')
    # |                LOAD_CONST              12 ('py7')
    # |                LOAD_FAST_BORROW        13 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST_LOAD_FAST   229 (@py_format8, @py_assert1)
    # |                LOAD_ATTR               23 (append + NULL|self)
    # |                LOAD_FAST_BORROW        14 (@py_format8)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW         7 (@py_assert4)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_FALSE      335 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              27 (('in',))
    # |                LOAD_FAST_CHECK         10 (@py_assert11)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              28 (('%(py10)s in %(py12)s',))
    # |                LOAD_FAST_CHECK          9 (@py_assert9)
    # |                LOAD_FAST_BORROW         4 (body)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              13 ('py10')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert9)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py12')
    # |                LOAD_CONST              10 ('body')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST              10 ('body')
    # |        L7:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format13)
    # |                LOAD_CONST              15 ('%(py14)s')
    # |                LOAD_CONST              16 ('py14')
    # |                LOAD_FAST_BORROW        15 (@py_format13)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format15)
    # |                LOAD_FAST_BORROW         5 (@py_assert1)
    # |                LOAD_ATTR               23 (append + NULL|self)
    # |                LOAD_FAST_BORROW        16 (@py_format15)
    # |                CALL                     1
    # |                POP_TOP
    # |                LOAD_FAST_BORROW        10 (@py_assert11)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE      164 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               12 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              27 (('in',))
    # |                LOAD_FAST_CHECK         12 (@py_assert18)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              29 (('%(py17)s in %(py19)s',))
    # |                LOAD_FAST_CHECK         11 (@py_assert16)
    # |                LOAD_FAST_BORROW         4 (body)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST              17 ('py17')
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_assert16)
    # |                CALL                     1
    # |                LOAD_CONST              18 ('py19')
    # |                LOAD_CONST              10 ('body')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L9)
    # |                NOT_TAKEN
    # |        L8:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               14 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (body)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L10)
    # |        L9:     LOAD_CONST              10 ('body')
    # |       L10:     BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              17 (@py_format20)
    # |                LOAD_CONST              19 ('%(py21)s')
    # |                LOAD_CONST              20 ('py21')
    # |                LOAD_FAST_BORROW        17 (@py_format20)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              18 (@py_format22)
    # |                LOAD_FAST_BORROW         5 (@py_assert1)
    # |                LOAD_ATTR               23 (append + NULL|self)
    # |                LOAD_FAST_BORROW        18 (@py_format22)
    # |                CALL                     1
    # |                POP_TOP
    # |       L11:     LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               24 (_format_boolop)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert1)
    # |                LOAD_SMALL_INT           0
    # |                CALL                     2
    # |                BUILD_MAP                0
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              19 (@py_format23)
    # |                LOAD_CONST              21 ('assert %(py24)s')
    # |                LOAD_CONST              22 ('py24')
    # |                LOAD_FAST_BORROW        19 (@py_format23)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              20 (@py_format25)
    # |                LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                LOAD_GLOBAL             10 (@pytest_ar)
    # |                LOAD_ATTR               28 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        20 (@py_format25)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L12:     LOAD_CONST              23 (None)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert9)
    # |                COPY                     1
    # |                STORE_FAST              10 (@py_assert11)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  188 (@py_assert16, @py_assert18)
    # |                LOAD_CONST              23 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x1057ac470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 250>:
    # |  250           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                16 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (c, c)
    # |                LOAD_ATTR                0 (body)
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

    def _make_epub(self, path, chapters):
        'w'
        # ── 函数体（字节码重建见 BODY 段）──
        # |   --           MAKE_CELL               11 (body)
        # |  212           RESUME                   0
        # |  213           LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (None)
        # |                IMPORT_NAME              0 (zipfile)
        # |                STORE_FAST               3 (zipfile)
        # |  215           LOAD_FAST_BORROW         3 (zipfile)
        # |                LOAD_ATTR                3 (ZipFile + NULL|self)
        # |                LOAD_FAST_BORROW         1 (path)
        # |                LOAD_CONST               2 ('w')
        # |                CALL                     2
        # |                COPY                     1
        # |                LOAD_SPECIAL             1 (__exit__)
        # |                SWAP                     2
        # |                SWAP                     3
        # |                LOAD_SPECIAL             0 (__enter__)
        # |                CALL                     0
        # |        L1:     STORE_FAST               4 (zf)
        # |  216           LOAD_FAST_BORROW         4 (zf)
        # |                LOAD_ATTR                5 (writestr + NULL|self)
        # |                LOAD_CONST               3 ('META-INF/container.xml')
        # |  217           LOAD_CONST               4 ('<?xml version="1.0"?><container xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf"/></rootfiles></container>')
        # |  216           CALL                     2
        # |                POP_TOP
        # |  220           BUILD_LIST               0
        # |                BUILD_LIST               0
        # |                STORE_FAST_STORE_FAST  101 (refs, items)
        # |  221           LOAD_GLOBAL              7 (enumerate + NULL)
        # |                LOAD_FAST_BORROW         2 (chapters)
        # |                LOAD_SMALL_INT           1
        # |                CALL                     2
        # |                GET_ITER
        # |        L2:     FOR_ITER               128 (to L3)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST               7 (i)
        # |                UNPACK_SEQUENCE          2
        # |                STORE_FAST               8 (title)
        # |                STORE_DEREF             11 (body)
        # |  222           LOAD_CONST               5 ('c')
        # |                LOAD_FAST_BORROW         7 (i)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST               6 ('.xhtml')
        # |                BUILD_STRING             3
        # |                STORE_FAST               9 (name)
        # |  225           LOAD_CONST               7 ('')
        # |                LOAD_ATTR                9 (join + NULL|self)
        # |                LOAD_FAST_BORROW        11 (body)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST               8 (<code object <genexpr> at 0x1057ac030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 225>)
        # |                MAKE_FUNCTION
        # |                SET_FUNCTION_ATTRIBUTE   8 (closure)
        # |                LOAD_GLOBAL             11 (range + NULL)
        # |                LOAD_SMALL_INT           1
        # |                LOAD_SMALL_INT           9
        # |                CALL                     2
        # |                GET_ITER
        # |                CALL                     0
        # |                CALL                     1
        # |                STORE_FAST              10 (paras)
        # |  226           LOAD_FAST_BORROW         4 (zf)
        # |                LOAD_ATTR                5 (writestr + NULL|self)
        # |                LOAD_CONST               9 ('OEBPS/')
        # |                LOAD_FAST_BORROW         9 (name)
        # |                FORMAT_SIMPLE
        # |                BUILD_STRING             2
        # |  227           LOAD_CONST              10 ('<html><body><h1>第')
        # |                LOAD_FAST_BORROW         7 (i)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              11 ('章 ')
        # |                LOAD_FAST_BORROW         8 (title)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              12 ('</h1>')
        # |                LOAD_FAST_BORROW        10 (paras)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              13 ('</body></html>')
        # |                BUILD_STRING             7
        # |  226           CALL                     2
        # |                POP_TOP
        # |  228           LOAD_FAST_BORROW         5 (items)
        # |                LOAD_ATTR               13 (append + NULL|self)
        # |                LOAD_CONST              14 ('<item id="i')
        # |                LOAD_FAST_BORROW         7 (i)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              15 ('" href="')
        # |                LOAD_FAST_BORROW         9 (name)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              16 ('" media-type="application/xhtml+xml"/>')
        # |                BUILD_STRING             5
        # |                CALL                     1
        # |                POP_TOP
        # |  229           LOAD_FAST_BORROW         6 (refs)
        # |                LOAD_ATTR               13 (append + NULL|self)
        # |                LOAD_CONST              17 ('<itemref idref="i')
        # |                LOAD_FAST_BORROW         7 (i)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              18 ('"/>')
        # |                BUILD_STRING             3
        # |                CALL                     1
        # |                POP_TOP
        # |                JUMP_BACKWARD          130 (to L2)
        # |  221   L3:     END_FOR
        # |                POP_ITER
        # |  230           LOAD_FAST_BORROW         4 (zf)
        # |                LOAD_ATTR                5 (writestr + NULL|self)
        # |                LOAD_CONST              19 ('OEBPS/content.opf')
        # |  231           LOAD_CONST              20 ('<?xml version="1.0"?><package xmlns="http://www.idpf.org/2007/opf"><manifest>')
        # |  232           LOAD_CONST               7 ('')
        # |                LOAD_ATTR                9 (join + NULL|self)
        # |                LOAD_FAST_BORROW         5 (items)
        # |                CALL                     1
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              21 ('</manifest><spine>')
        # |  233           LOAD_CONST               7 ('')
        # |                LOAD_ATTR                9 (join + NULL|self)
        # |                LOAD_FAST_BORROW         6 (refs)
        # |                CALL                     1
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST              22 ('</spine></package>')
        # |  231           BUILD_STRING             5
        # |  230           CALL                     2
        # |                POP_TOP
        # |  215   L4:     LOAD_CONST               1 (None)
        # |                LOAD_CONST               1 (None)
        # |                LOAD_CONST               1 (None)
        # |                CALL                     3
        # |                POP_TOP
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |        L5:     PUSH_EXC_INFO
        # |                WITH_EXCEPT_START
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE         2 (to L6)
        # |                NOT_TAKEN
        # |                RERAISE                  2
        # |        L6:     POP_TOP
        # |        L7:     POP_EXCEPT
        # |                POP_TOP
        # |                POP_TOP
        # |                POP_TOP
        # |                LOAD_CONST               1 (None)
        # |                RETURN_VALUE
        # |   --   L8:     COPY                     3
        # |                POP_EXCEPT
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L5 [2] lasti
        # |   L5 to L7 -> L8 [4] lasti
        # | Disassembly of <code object <genexpr> at 0x1057ac030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 225>:
        # |   --           COPY_FREE_VARS           1
        # |  225           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                14 (to L3)
        # |                STORE_FAST               1 (n)
        # |                LOAD_CONST               0 ('<p>')
        # |                LOAD_DEREF               2 (body)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST               1 ('第')
        # |                LOAD_FAST_BORROW         1 (n)
        # |                FORMAT_SIMPLE
        # |                LOAD_CONST               2 ('段。</p>')
        # |                BUILD_STRING             5
        # |                YIELD_VALUE              0
        # |                RESUME                   5
        # |                POP_TOP
        # |                JUMP_BACKWARD           16 (to L2)
        # |        L3:     END_FOR
        # |                POP_ITER
        # |                LOAD_CONST               3 (None)
        # |                RETURN_VALUE
        # |   --   L4:     CALL_INTRINSIC_1         3 (INTRINSIC_STOPITERATION_ERROR)
        # |                RERAISE                  1
        # | ExceptionTable:
        # |   L1 to L4 -> L4 [0] lasti

    def test_reads_epub_in_spine_order(self, tmp_path):
        'book.epub'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  235            RESUME                   0
        # |  236            LOAD_SMALL_INT           0
        # |                 LOAD_CONST               1 (('ingest_file',))
        # |                 IMPORT_NAME              0 (novel_agent.corpus.ingest)
        # |                 IMPORT_FROM              1 (ingest_file)
        # |                 STORE_FAST               2 (ingest_file)
        # |                 POP_TOP
        # |  238            LOAD_FAST_BORROW         1 (tmp_path)
        # |                 LOAD_CONST               2 ('book.epub')
        # |                 BINARY_OP               11 (/)
        # |                 STORE_FAST               3 (f)
        # |  239            LOAD_FAST_BORROW         0 (self)
        # |                 LOAD_ATTR                5 (_make_epub + NULL|self)
        # |                 LOAD_FAST_BORROW         3 (f)
        # |                 LOAD_CONST              20 (('初遇', '第一章的正文。'))
        # |                 LOAD_CONST              21 (('重逢', '第二章的正文。'))
        # |                 BUILD_LIST               2
        # |                 CALL                     2
        # |                 POP_TOP
        # |  240            LOAD_FAST_BORROW         2 (ingest_file)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         3 (f)
        # |                 CALL                     1
        # |                 STORE_FAST               4 (book)
        # |  241            LOAD_FAST_BORROW         4 (book)
        # |                 LOAD_ATTR                6 (encoding)
        # |                 STORE_FAST               5 (@py_assert1)
        # |                 LOAD_CONST               6 ('epub')
        # |                 STORE_FAST_LOAD_FAST   101 (@py_assert4, @py_assert1)
        # |                 LOAD_FAST_BORROW         6 (@py_assert4)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       199 (to L4)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              22 (('==',))
        # |                 LOAD_FAST_BORROW         7 (@py_assert3)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              23 (('%(py2)s\n{%(py2)s = %(py0)s.encoding\n} == %(py5)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 86 (@py_assert1, @py_assert4)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST               7 ('py0')
        # |                 LOAD_CONST               8 ('book')
        # |                 LOAD_GLOBAL             12 (@py_builtins)
        # |                 LOAD_ATTR               14 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L1)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (book)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L2)
        # |                 NOT_TAKEN
        # |         L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         4 (book)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L3)
        # |         L2:     LOAD_CONST               8 ('book')
        # |         L3:     LOAD_CONST               9 ('py2')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (@py_assert1)
        # |                 CALL                     1
        # |                 LOAD_CONST              10 ('py5')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (@py_assert4)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               8 (@py_format6)
        # |                 LOAD_CONST              11 ('assert %(py7)s')
        # |                 LOAD_CONST              12 ('py7')
        # |                 LOAD_FAST_BORROW         8 (@py_format6)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST               9 (@py_format8)
        # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         9 (@py_format8)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L4:     LOAD_CONST              13 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               5 (@py_assert1)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  118 (@py_assert3, @py_assert4)
        # |  242            LOAD_FAST_BORROW         4 (book)
        # |                 LOAD_ATTR               24 (chapters)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR     10 (c)
        # |                 SWAP                     2
        # |         L5:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L6:     FOR_ITER                14 (to L7)
        # |                 STORE_FAST_LOAD_FAST   170 (c, c)
        # |                 LOAD_ATTR               26 (title)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           16 (to L6)
        # |         L7:     END_FOR
        # |                 POP_ITER
        # |         L8:     STORE_FAST              11 (@py_assert0)
        # |                 STORE_FAST              10 (c)
        # |                 LOAD_CONST               3 ('初遇')
        # |                 LOAD_CONST               5 ('重逢')
        # |                 BUILD_LIST               2
        # |                 STORE_FAST_LOAD_FAST   123 (@py_assert3, @py_assert0)
        # |                 LOAD_FAST_BORROW         7 (@py_assert3)
        # |                 COMPARE_OP              72 (==)
        # |                 STORE_FAST_LOAD_FAST   204 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       121 (to L9)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              22 (('==',))
        # |                 LOAD_FAST_BORROW        12 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              24 (('%(py1)s == %(py4)s',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 183 (@py_assert0, @py_assert3)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST              14 ('py1')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py4')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert3)
        # |                 CALL                     1
        # |                 BUILD_MAP                2
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format5)
        # |                 LOAD_CONST              16 ('assert %(py6)s')
        # |                 LOAD_CONST              17 ('py6')
        # |                 LOAD_FAST_BORROW        13 (@py_format5)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              14 (@py_format7)
        # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        14 (@py_format7)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |         L9:     LOAD_CONST              13 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              11 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  199 (@py_assert2, @py_assert3)
        # |  243            LOAD_CONST               4 ('第一章的正文。')
        # |                 STORE_FAST_LOAD_FAST   180 (@py_assert0, book)
        # |                 LOAD_ATTR               24 (chapters)
        # |                 LOAD_SMALL_INT           0
        # |                 BINARY_OP               26 ([])
        # |                 STORE_FAST_LOAD_FAST   119 (@py_assert3, @py_assert3)
        # |                 LOAD_ATTR               28 (body)
        # |                 STORE_FAST_LOAD_FAST   251 (@py_assert5, @py_assert0)
        # |                 LOAD_FAST_BORROW        15 (@py_assert5)
        # |                 CONTAINS_OP              0 (in)
        # |                 STORE_FAST_LOAD_FAST   204 (@py_assert2, @py_assert2)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_TRUE       143 (to L10)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               10 (_call_reprcompare)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              25 (('in',))
        # |                 LOAD_FAST_BORROW        12 (@py_assert2)
        # |                 BUILD_TUPLE              1
        # |                 LOAD_CONST              26 (('%(py1)s in %(py6)s\n{%(py6)s = %(py4)s.body\n}',))
        # |                 LOAD_FAST_BORROW_LOAD_FAST_BORROW 191 (@py_assert0, @py_assert5)
        # |                 BUILD_TUPLE              2
        # |                 CALL                     4
        # |                 LOAD_CONST              14 ('py1')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        11 (@py_assert0)
        # |                 CALL                     1
        # |                 LOAD_CONST              15 ('py4')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert3)
        # |                 CALL                     1
        # |                 LOAD_CONST              17 ('py6')
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        15 (@py_assert5)
        # |                 CALL                     1
        # |                 BUILD_MAP                3
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              14 (@py_format7)
        # |                 LOAD_CONST              18 ('assert %(py8)s')
        # |                 LOAD_CONST              19 ('py8')
        # |                 LOAD_FAST_BORROW        14 (@py_format7)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              16 (@py_format9)
        # |                 LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                 LOAD_GLOBAL              8 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        16 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L10:     LOAD_CONST              13 (None)
        # |                 COPY                     1
        # |                 STORE_FAST              11 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST              12 (@py_assert2)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  127 (@py_assert3, @py_assert5)
        # |                 LOAD_CONST              13 (None)
        # |                 RETURN_VALUE
        # |   --   L11:     SWAP                     2
        # |                 POP_TOP
        # |  242            SWAP                     2
        # |                 STORE_FAST              10 (c)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L5 to L8 -> L11 [2]

    def test_html_tags_stripped(self, tmp_path):
        'b.epub'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 245            RESUME                   0
        # | 246            LOAD_SMALL_INT           0
        # |                LOAD_CONST               1 (('ingest_file',))
        # |                IMPORT_NAME              0 (novel_agent.corpus.ingest)
        # |                IMPORT_FROM              1 (ingest_file)
        # |                STORE_FAST               2 (ingest_file)
        # |                POP_TOP
        # | 248            LOAD_FAST_BORROW         1 (tmp_path)
        # |                LOAD_CONST               2 ('b.epub')
        # |                BINARY_OP               11 (/)
        # |                STORE_FAST               3 (f)
        # | 249            LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                5 (_make_epub + NULL|self)
        # |                LOAD_FAST_BORROW         3 (f)
        # |                LOAD_CONST              24 (('t', '正文有<em>强调</em>与&amp;实体。'))
        # |                BUILD_LIST               1
        # |                CALL                     2
        # |                POP_TOP
        # | 250            LOAD_CONST               3 ('\n')
        # |                LOAD_ATTR                7 (join + NULL|self)
        # |                LOAD_CONST               4 (<code object <genexpr> at 0x1057ac470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 250>)
        # |                MAKE_FUNCTION
        # |                LOAD_FAST_BORROW         2 (ingest_file)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (f)
        # |                CALL                     1
        # |                LOAD_ATTR                8 (chapters)
        # |                GET_ITER
        # |                CALL                     0
        # |                CALL                     1
        # |                STORE_FAST               4 (body)
        # | 251            BUILD_LIST               0
        # |                STORE_FAST               5 (@py_assert1)
        # |                LOAD_CONST               5 ('<em>')
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert4, @py_assert4)
        # |                STORE_FAST_LOAD_FAST   135 (@py_assert0, @py_assert4)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       22 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_CONST               6 ('强调')
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert9, @py_assert9)
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   170 (@py_assert11, @py_assert11)
        # |                STORE_FAST_LOAD_FAST   138 (@py_assert0, @py_assert11)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE        8 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_CONST               7 ('&')
        # |                STORE_FAST_LOAD_FAST   187 (@py_assert16, @py_assert16)
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   204 (@py_assert18, @py_assert18)
        # |                STORE_FAST               8 (@py_assert0)
        # |        L1:     LOAD_FAST_BORROW         8 (@py_assert0)
        # |                TO_BOOL
        # |                EXTENDED_ARG             2
        # |                POP_JUMP_IF_TRUE       577 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              25 (('not in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              26 (('%(py3)s not in %(py5)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 100 (@py_assert2, body)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               8 ('py3')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py5')
        # |                LOAD_CONST              10 ('body')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST              10 ('body')
        # |        L4:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              13 (@py_format6)
        # |                LOAD_CONST              11 ('%(py7)s')
        # |                LOAD_CONST              12 ('py7')
        # |                LOAD_FAST_BORROW        13 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST_LOAD_FAST   229 (@py_format8, @py_assert1)
        # |                LOAD_ATTR               23 (append + NULL|self)
        # |                LOAD_FAST_BORROW        14 (@py_format8)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW         7 (@py_assert4)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_FALSE      335 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              27 (('in',))
        # |                LOAD_FAST_CHECK         10 (@py_assert11)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              28 (('%(py10)s in %(py12)s',))
        # |                LOAD_FAST_CHECK          9 (@py_assert9)
        # |                LOAD_FAST_BORROW         4 (body)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              13 ('py10')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert9)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py12')
        # |                LOAD_CONST              10 ('body')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST              10 ('body')
        # |        L7:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format13)
        # |                LOAD_CONST              15 ('%(py14)s')
        # |                LOAD_CONST              16 ('py14')
        # |                LOAD_FAST_BORROW        15 (@py_format13)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format15)
        # |                LOAD_FAST_BORROW         5 (@py_assert1)
        # |                LOAD_ATTR               23 (append + NULL|self)
        # |                LOAD_FAST_BORROW        16 (@py_format15)
        # |                CALL                     1
        # |                POP_TOP
        # |                LOAD_FAST_BORROW        10 (@py_assert11)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE      164 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               12 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              27 (('in',))
        # |                LOAD_FAST_CHECK         12 (@py_assert18)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              29 (('%(py17)s in %(py19)s',))
        # |                LOAD_FAST_CHECK         11 (@py_assert16)
        # |                LOAD_FAST_BORROW         4 (body)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST              17 ('py17')
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_assert16)
        # |                CALL                     1
        # |                LOAD_CONST              18 ('py19')
        # |                LOAD_CONST              10 ('body')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L9)
        # |                NOT_TAKEN
        # |        L8:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               14 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (body)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L10)
        # |        L9:     LOAD_CONST              10 ('body')
        # |       L10:     BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              17 (@py_format20)
        # |                LOAD_CONST              19 ('%(py21)s')
        # |                LOAD_CONST              20 ('py21')
        # |                LOAD_FAST_BORROW        17 (@py_format20)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              18 (@py_format22)
        # |                LOAD_FAST_BORROW         5 (@py_assert1)
        # |                LOAD_ATTR               23 (append + NULL|self)
        # |                LOAD_FAST_BORROW        18 (@py_format22)
        # |                CALL                     1
        # |                POP_TOP
        # |       L11:     LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               24 (_format_boolop)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert1)
        # |                LOAD_SMALL_INT           0
        # |                CALL                     2
        # |                BUILD_MAP                0
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              19 (@py_format23)
        # |                LOAD_CONST              21 ('assert %(py24)s')
        # |                LOAD_CONST              22 ('py24')
        # |                LOAD_FAST_BORROW        19 (@py_format23)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              20 (@py_format25)
        # |                LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                LOAD_GLOBAL             10 (@pytest_ar)
        # |                LOAD_ATTR               28 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        20 (@py_format25)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L12:     LOAD_CONST              23 (None)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert9)
        # |                COPY                     1
        # |                STORE_FAST              10 (@py_assert11)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  188 (@py_assert16, @py_assert18)
        # |                LOAD_CONST              23 (None)
        # |                RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x1057ac470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_ingest.py", line 250>:
        # |  250           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                16 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (c, c)
        # |                LOAD_ATTR                0 (body)
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

