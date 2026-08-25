# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py
# 来源   : test_gate.cpython-314-pytest-9.1.1.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = 'gate 规则的正反样本。\n\n每条规则都要有一个"违规样本能被抓到"的断言 —— 这是 Phase 1 的验收标准。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'gate 规则的正反样本。\n\n每条规则都要有一个"违规样本能被抓到"的断言 —— 这是 Phase 1 的验收标准。\n',
    12: 'TestBaseline',
    14: 'TestTitle',
    16: 'TestLength',
    18: 'TestPunctuation',
    20: 'TestParagraph',
    22: 'TestDialogue',
    24: 'TestAsciiQuotedDialogueStillCounts',
    26: 'TestPlagiarism',
    28: 'TestSelfRepetition',
    30: 'TestEmotionalDebt',
    32: 'TestDialogueSpeakerDetection',
    34: 'TestToleranceBands',
    36: 'TestStrayNotes',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'Gate',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'set[str]',
    ('rules', 0): 'error',
    ('TestBaseline', 0): 'TestBaseline',
    ('test_compliant_chapter_passes', 2): '\n>assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_compliant_chapter_passes', 3): 'py0',
    ('test_compliant_chapter_passes', 4): 'report',
    ('test_compliant_chapter_passes', 5): 'py2',
    ('test_stats_are_reported', 1): 'word_count',
    ('test_stats_are_reported', 3): 'py1',
    ('test_stats_are_reported', 4): 'py5',
    ('test_stats_are_reported', 5): 'py7',
    ('test_stats_are_reported', 6): 'assert %(py9)s',
    ('test_stats_are_reported', 7): 'py9',
    ('test_stats_are_reported', 9): 'length',
    ('test_stats_are_reported', 10): 'dialogue_ratio_min',
    ('test_stats_are_reported', 11): 'dialogue_ratio_max',
    ('test_stats_are_reported', 12): 'dialogue_ratio',
    ('test_stats_are_reported', 13): 'py0',
    ('test_stats_are_reported', 14): 'lo',
    ('test_stats_are_reported', 15): 'py4',
    ('test_stats_are_reported', 16): 'hi',
    ('test_stats_are_reported', 17): 'assert %(py7)s',
    ('test_stats_are_reported', 18): 'paragraphs',
    ('test_stats_are_reported', 19): 'assert %(py6)s',
    ('test_stats_are_reported', 20): 'py6',
    ('TestTitle', 0): 'TestTitle',
    ('test_missing_title_caught', 0): 'title',
    ('test_missing_title_caught', 1): '正文没有标题。',
    ('test_missing_title_caught', 3): 'py1',
    ('test_missing_title_caught', 4): 'py3',
    ('test_missing_title_caught', 5): 'rules',
    ('test_missing_title_caught', 6): 'py4',
    ('test_missing_title_caught', 7): 'gate',
    ('test_missing_title_caught', 8): 'py6',
    ('test_missing_title_caught', 9): 'py8',
    ('test_missing_title_caught', 10): 'py10',
    ('test_missing_title_caught', 11): 'py13',
    ('test_missing_title_caught', 12): 'py15',
    ('test_missing_title_caught', 13): 'assert %(py17)s',
    ('test_missing_title_caught', 14): 'py17',
    ('test_malformed_title_caught', 0): '## 第1章 雨天',
    ('test_malformed_title_caught', 1): '## 第一章 雨天',
    ('test_malformed_title_caught', 2): 'title',
    ('test_malformed_title_caught', 3): 'py1',
    ('test_malformed_title_caught', 4): 'py3',
    ('test_malformed_title_caught', 5): 'rules',
    ('test_malformed_title_caught', 6): 'py4',
    ('test_malformed_title_caught', 7): 'gate',
    ('test_malformed_title_caught', 8): 'py6',
    ('test_malformed_title_caught', 9): 'py7',
    ('test_malformed_title_caught', 10): 'text',
    ('test_malformed_title_caught', 11): 'py9',
    ('test_malformed_title_caught', 12): 'py11',
    ('test_malformed_title_caught', 13): 'assert %(py13)s',
    ('test_malformed_title_caught', 14): 'py13',
    ('test_wrong_chapter_number_caught', 3): 'title',
    ('test_wrong_chapter_number_caught', 4): 'py1',
    ('test_wrong_chapter_number_caught', 5): 'py3',
    ('test_wrong_chapter_number_caught', 6): 'rules',
    ('test_wrong_chapter_number_caught', 7): 'py4',
    ('test_wrong_chapter_number_caught', 8): 'report',
    ('test_wrong_chapter_number_caught', 9): 'py6',
    ('test_wrong_chapter_number_caught', 10): 'assert %(py8)s',
    ('test_wrong_chapter_number_caught', 11): 'py8',
    ('TestLength', 0): 'TestLength',
    ('test_too_short_caught', 0): 'length',
    ('test_too_short_caught', 3): 'py1',
    ('test_too_short_caught', 4): 'py3',
    ('test_too_short_caught', 5): 'rules',
    ('test_too_short_caught', 6): 'py4',
    ('test_too_short_caught', 7): 'gate',
    ('test_too_short_caught', 8): 'py6',
    ('test_too_short_caught', 9): 'py7',
    ('test_too_short_caught', 10): 'make_chapter',
    ('test_too_short_caught', 11): 'py9',
    ('test_too_short_caught', 12): 'py11',
    ('test_too_short_caught', 13): 'py13',
    ('test_too_short_caught', 14): 'py15',
    ('test_too_short_caught', 15): 'assert %(py17)s',
    ('test_too_short_caught', 16): 'py17',
    ('test_too_long_caught', 0): 'length',
    ('test_too_long_caught', 3): 'py1',
    ('test_too_long_caught', 4): 'py3',
    ('test_too_long_caught', 5): 'rules',
    ('test_too_long_caught', 6): 'py4',
    ('test_too_long_caught', 7): 'gate',
    ('test_too_long_caught', 8): 'py6',
    ('test_too_long_caught', 9): 'py7',
    ('test_too_long_caught', 10): 'make_chapter',
    ('test_too_long_caught', 11): 'py9',
    ('test_too_long_caught', 12): 'py11',
    ('test_too_long_caught', 13): 'py13',
    ('test_too_long_caught', 14): 'py15',
    ('test_too_long_caught', 15): 'assert %(py17)s',
    ('test_too_long_caught', 16): 'py17',
    ('test_dialogue_ratio_too_low_caught', 0): '他没有回答。',
    ('test_dialogue_ratio_too_low_caught', 2): 'dialogue_ratio',
    ('test_dialogue_ratio_too_low_caught', 3): 'py1',
    ('test_dialogue_ratio_too_low_caught', 4): 'py3',
    ('test_dialogue_ratio_too_low_caught', 5): 'rules',
    ('test_dialogue_ratio_too_low_caught', 6): 'py4',
    ('test_dialogue_ratio_too_low_caught', 7): 'gate',
    ('test_dialogue_ratio_too_low_caught', 8): 'py6',
    ('test_dialogue_ratio_too_low_caught', 9): 'py7',
    ('test_dialogue_ratio_too_low_caught', 10): 'text',
    ('test_dialogue_ratio_too_low_caught', 11): 'py9',
    ('test_dialogue_ratio_too_low_caught', 12): 'py11',
    ('test_dialogue_ratio_too_low_caught', 13): 'assert %(py13)s',
    ('test_dialogue_ratio_too_low_caught', 14): 'py13',
    ('test_dialogue_ratio_too_high_caught', 0): '她笑了。',
    ('test_dialogue_ratio_too_high_caught', 2): 'dialogue_ratio',
    ('test_dialogue_ratio_too_high_caught', 3): 'py1',
    ('test_dialogue_ratio_too_high_caught', 4): 'py3',
    ('test_dialogue_ratio_too_high_caught', 5): 'rules',
    ('test_dialogue_ratio_too_high_caught', 6): 'py4',
    ('test_dialogue_ratio_too_high_caught', 7): 'gate',
    ('test_dialogue_ratio_too_high_caught', 8): 'py6',
    ('test_dialogue_ratio_too_high_caught', 9): 'py7',
    ('test_dialogue_ratio_too_high_caught', 10): 'text',
    ('test_dialogue_ratio_too_high_caught', 11): 'py9',
    ('test_dialogue_ratio_too_high_caught', 12): 'py11',
    ('test_dialogue_ratio_too_high_caught', 13): 'assert %(py13)s',
    ('test_dialogue_ratio_too_high_caught', 14): 'py13',
    ('TestPunctuation', 0): 'TestPunctuation',
    ('TestPunctuation', 1): 'bad_para',
    ('test_violation_caught', 1): 'punctuation',
    ('test_violation_caught', 2): 'py1',
    ('test_violation_caught', 3): 'py3',
    ('test_violation_caught', 4): 'rules',
    ('test_violation_caught', 5): 'py4',
    ('test_violation_caught', 6): 'gate',
    ('test_violation_caught', 7): 'py6',
    ('test_violation_caught', 8): 'py7',
    ('test_violation_caught', 9): 'text',
    ('test_violation_caught', 10): 'py9',
    ('test_violation_caught', 11): 'py11',
    ('test_violation_caught', 12): '漏判：',
    ('test_violation_caught', 13): '\n>assert %(py13)s',
    ('test_violation_caught', 14): 'py13',
    ('test_correct_forms_pass', 0): '她想说什么，最终只是摇头——那句话到底没有出口……',
    ('test_correct_forms_pass', 2): 'punctuation',
    ('test_correct_forms_pass', 3): 'py1',
    ('test_correct_forms_pass', 4): 'py3',
    ('test_correct_forms_pass', 5): 'rules',
    ('test_correct_forms_pass', 6): 'py4',
    ('test_correct_forms_pass', 7): 'gate',
    ('test_correct_forms_pass', 8): 'py6',
    ('test_correct_forms_pass', 9): 'py7',
    ('test_correct_forms_pass', 10): 'text',
    ('test_correct_forms_pass', 11): 'py9',
    ('test_correct_forms_pass', 12): 'py11',
    ('test_correct_forms_pass', 13): 'assert %(py13)s',
    ('test_correct_forms_pass', 14): 'py13',
    ('test_halfwidth_in_numbers_not_flagged', 0): '"3.5" "Wi-Fi" 里的半角符号是合法的，不能误伤。',
    ('test_halfwidth_in_numbers_not_flagged', 1): '教学楼 3.5 公里外，Wi-Fi 信号断断续续，她把伞往他那边偏了偏。',
    ('test_halfwidth_in_numbers_not_flagged', 3): 'punctuation',
    ('test_halfwidth_in_numbers_not_flagged', 4): 'py1',
    ('test_halfwidth_in_numbers_not_flagged', 5): 'py3',
    ('test_halfwidth_in_numbers_not_flagged', 6): 'rules',
    ('test_halfwidth_in_numbers_not_flagged', 7): 'py4',
    ('test_halfwidth_in_numbers_not_flagged', 8): 'gate',
    ('test_halfwidth_in_numbers_not_flagged', 9): 'py6',
    ('test_halfwidth_in_numbers_not_flagged', 10): 'py7',
    ('test_halfwidth_in_numbers_not_flagged', 11): 'text',
    ('test_halfwidth_in_numbers_not_flagged', 12): 'py9',
    ('test_halfwidth_in_numbers_not_flagged', 13): 'py11',
    ('test_halfwidth_in_numbers_not_flagged', 14): 'assert %(py13)s',
    ('test_halfwidth_in_numbers_not_flagged', 15): 'py13',
    ('TestParagraph', 0): 'TestParagraph',
    ('test_overlong_paragraph_caught', 0): '她想起很多事情。',
    ('test_overlong_paragraph_caught', 2): 'paragraph',
    ('test_overlong_paragraph_caught', 3): 'py1',
    ('test_overlong_paragraph_caught', 4): 'py3',
    ('test_overlong_paragraph_caught', 5): 'rules',
    ('test_overlong_paragraph_caught', 6): 'py4',
    ('test_overlong_paragraph_caught', 7): 'gate',
    ('test_overlong_paragraph_caught', 8): 'py6',
    ('test_overlong_paragraph_caught', 9): 'py7',
    ('test_overlong_paragraph_caught', 10): 'text',
    ('test_overlong_paragraph_caught', 11): 'py9',
    ('test_overlong_paragraph_caught', 12): 'py11',
    ('test_overlong_paragraph_caught', 13): 'assert %(py13)s',
    ('test_overlong_paragraph_caught', 14): 'py13',
    ('test_overlong_paragraph_caught', 16): '她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。',
    ('TestDialogue', 0): 'TestDialogue',
    ('test_two_speakers_in_one_paragraph_caught', 0): '“你会湿透的。”他摇头。“我不冷。”',
    ('test_two_speakers_in_one_paragraph_caught', 2): 'dialogue',
    ('test_two_speakers_in_one_paragraph_caught', 3): 'py1',
    ('test_two_speakers_in_one_paragraph_caught', 4): 'py3',
    ('test_two_speakers_in_one_paragraph_caught', 5): 'rules',
    ('test_two_speakers_in_one_paragraph_caught', 6): 'py4',
    ('test_two_speakers_in_one_paragraph_caught', 7): 'gate',
    ('test_two_speakers_in_one_paragraph_caught', 8): 'py6',
    ('test_two_speakers_in_one_paragraph_caught', 9): 'py7',
    ('test_two_speakers_in_one_paragraph_caught', 10): 'text',
    ('test_two_speakers_in_one_paragraph_caught', 11): 'py9',
    ('test_two_speakers_in_one_paragraph_caught', 12): 'py11',
    ('test_two_speakers_in_one_paragraph_caught', 13): 'assert %(py13)s',
    ('test_two_speakers_in_one_paragraph_caught', 14): 'py13',
    ('TestAsciiQuotedDialogueStillCounts', 0): 'TestAsciiQuotedDialogueStillCounts',
    ('TestAsciiQuotedDialogueStillCounts', 1): '实测事故：模型把整章引号吐成了 ASCII，gate 于是同时报两条 ——\n「ASCII 引号」（真问题）和「对话占比 0.0%，叙述压过了场景」（假问题）。\n后者把 writer 支去补根本不缺的对话，白烧一轮修订。',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 0): '“',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 1): '"',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 2): '”',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 3): 'dialogue_ratio',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 5): 'py1',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 6): 'py4',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 7): '对话还在，只是引号写错了',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 8): '\n>assert %(py6)s',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 9): 'py6',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 11): 'py3',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 12): 'rules',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 13): 'report',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 14): '别把格式问题报成缺对话',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 15): '\n>assert %(py8)s',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 16): 'py8',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 17): 'punctuation',
    ('test_ascii_quoted_chapter_is_not_read_as_zero_dialogue', 18): '引号错了仍然要报',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 0): '别为了修上面那条把真正的缺对话放过去。',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 1): 'dialogue_ratio',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 2): '他没说话。',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 4): 'py1',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 5): 'py3',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 6): 'rules',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 7): 'py4',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 8): 'gate',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 9): 'py6',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 10): 'py7',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 11): 'make_chapter',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 12): 'py9',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 13): 'py11',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 14): 'py13',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 15): 'py15',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 16): 'assert %(py17)s',
    ('test_a_chapter_really_short_on_dialogue_still_caught', 17): 'py17',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 0): '单个撇号不成对，不该被当成一句对话吞进占比里。',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 1): 'dialogue_ratio',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 2): "她在纸上写下 don't，又划掉了。",
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 5): 'py0',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 6): 'abs',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 7): 'py2',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 8): 'py3',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 9): 'base',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 10): 'py6',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 11): 'py9',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 12): 'assert %(py11)s',
    ('test_apostrophe_in_prose_is_not_counted_as_speech', 13): 'py11',
    ('TestPlagiarism', 0): 'TestPlagiarism',
    ('test_copied_passage_is_hard_failure', 0): '她把伞往他那边偏了偏，雨水顺着自己的肩膀淌下来，一直凉到手肘。',
    ('test_copied_passage_is_hard_failure', 4): 'plagiarism',
    ('test_copied_passage_is_hard_failure', 5): 'py1',
    ('test_copied_passage_is_hard_failure', 6): 'py3',
    ('test_copied_passage_is_hard_failure', 7): 'rules',
    ('test_copied_passage_is_hard_failure', 8): 'py4',
    ('test_copied_passage_is_hard_failure', 9): 'report',
    ('test_copied_passage_is_hard_failure', 10): 'py6',
    ('test_copied_passage_is_hard_failure', 11): 'assert %(py8)s',
    ('test_copied_passage_is_hard_failure', 12): 'py8',
    ('test_original_text_not_flagged', 3): 'plagiarism',
    ('test_original_text_not_flagged', 4): 'py1',
    ('test_original_text_not_flagged', 5): 'py3',
    ('test_original_text_not_flagged', 6): 'rules',
    ('test_original_text_not_flagged', 7): 'py4',
    ('test_original_text_not_flagged', 8): 'gate',
    ('test_original_text_not_flagged', 9): 'py6',
    ('test_original_text_not_flagged', 10): 'py7',
    ('test_original_text_not_flagged', 11): 'make_chapter',
    ('test_original_text_not_flagged', 12): 'py9',
    ('test_original_text_not_flagged', 13): 'py11',
    ('test_original_text_not_flagged', 14): 'py13',
    ('test_original_text_not_flagged', 15): 'assert %(py15)s',
    ('test_original_text_not_flagged', 16): 'py15',
    ('test_original_text_not_flagged', 18): '完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。',
    ('test_no_index_means_check_skipped', 1): 'assert %(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.check\n}(%(py5)s\n{%(py5)s = %(py3)s()\n})\n}.passed\n}',
    ('test_no_index_means_check_skipped', 2): 'py0',
    ('test_no_index_means_check_skipped', 3): 'gate',
    ('test_no_index_means_check_skipped', 4): 'py2',
    ('test_no_index_means_check_skipped', 5): 'py3',
    ('test_no_index_means_check_skipped', 6): 'make_chapter',
    ('test_no_index_means_check_skipped', 7): 'py5',
    ('test_no_index_means_check_skipped', 8): 'py7',
    ('test_no_index_means_check_skipped', 9): 'py9',
    ('TestSelfRepetition', 0): 'TestSelfRepetition',
    ('test_reusing_own_earlier_phrasing_warns_not_fails', 0): '自我重复是警告不是错误 —— 回响式的刻意重复是合法手法。',
    ('test_reusing_own_earlier_phrasing_warns_not_fails', 4): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_reusing_own_earlier_phrasing_warns_not_fails', 5): 'py0',
    ('test_reusing_own_earlier_phrasing_warns_not_fails', 6): 'report',
    ('test_reusing_own_earlier_phrasing_warns_not_fails', 7): 'py2',
    ('test_reusing_own_earlier_phrasing_warns_not_fails', 10): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_reusing_own_earlier_phrasing_warns_not_fails', 11): 'any',
    ('test_reusing_own_earlier_phrasing_warns_not_fails', 12): 'py4',
    ('<genexpr>', 0): 'self_repetition',
    ('TestEmotionalDebt', 0): 'TestEmotionalDebt',
    ('test_overdue_debt_warns', 1): 'd1',
    ('test_overdue_debt_warns', 2): '误会',
    ('test_overdue_debt_warns', 3): '她以为那通电话是打给别人的',
    ('test_overdue_debt_warns', 8): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_overdue_debt_warns', 9): 'py0',
    ('test_overdue_debt_warns', 10): 'any',
    ('test_overdue_debt_warns', 11): 'py2',
    ('test_overdue_debt_warns', 12): 'py4',
    ('test_overdue_debt_warns', 14): 'assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_overdue_debt_warns', 15): 'report',
    ('<genexpr>', 0): 'emotional_debt',
    ('test_paid_debt_silent', 1): 'd1',
    ('test_paid_debt_silent', 2): '误会',
    ('test_paid_debt_silent', 3): 'x',
    ('test_paid_debt_silent', 4): 'paid',
    ('test_paid_debt_silent', 8): 'assert not %(py10)s\n{%(py10)s = %(py8)s\n{%(py8)s = %(py2)s\n{%(py2)s = %(py0)s.check\n}(%(py5)s\n{%(py5)s = %(py3)s()\n}, state=%(py6)s)\n}.warnings\n}',
    ('test_paid_debt_silent', 9): 'py0',
    ('test_paid_debt_silent', 10): 'gate',
    ('test_paid_debt_silent', 11): 'py2',
    ('test_paid_debt_silent', 12): 'py3',
    ('test_paid_debt_silent', 13): 'make_chapter',
    ('test_paid_debt_silent', 14): 'py5',
    ('test_paid_debt_silent', 15): 'py6',
    ('test_paid_debt_silent', 16): 'state',
    ('test_paid_debt_silent', 17): 'py8',
    ('test_paid_debt_silent', 18): 'py10',
    ('TestDialogueSpeakerDetection', 0): 'TestDialogueSpeakerDetection',
    ('TestDialogueSpeakerDetection', 1): '只数段内引号对数会把标准写法判成错。实测第 13 章被误报 4 处。',
    ('TestDialogueSpeakerDetection', 3): 'para',
    ('TestDialogueSpeakerDetection', 5): '“九本。”他摇头。“不到六点。”她说。',
    ('TestDialogueSpeakerDetection', 6): '“你会湿透的。”她把伞递过去。“我不冷。”',
    ('_check', 1): 'dialogue',
    ('test_same_speaker_with_inline_attribution_is_valid', 0): '提示语插在中间、逗号收尾 —— 同一个人在说话，是标准写法。',
    ('test_same_speaker_with_inline_attribution_is_valid', 1): '误判了标准写法：',
    ('test_same_speaker_with_inline_attribution_is_valid', 2): '\n>assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s._check\n}(%(py3)s, %(py4)s)\n}',
    ('test_same_speaker_with_inline_attribution_is_valid', 3): 'py0',
    ('test_same_speaker_with_inline_attribution_is_valid', 4): 'self',
    ('test_same_speaker_with_inline_attribution_is_valid', 5): 'py2',
    ('test_same_speaker_with_inline_attribution_is_valid', 6): 'py3',
    ('test_same_speaker_with_inline_attribution_is_valid', 7): 'gate',
    ('test_same_speaker_with_inline_attribution_is_valid', 8): 'py4',
    ('test_same_speaker_with_inline_attribution_is_valid', 9): 'para',
    ('test_same_speaker_with_inline_attribution_is_valid', 10): 'py6',
    ('test_two_speakers_still_caught', 0): '句号收尾说明提示语已结束，后面是另一个人 —— 必须分段。',
    ('test_two_speakers_still_caught', 1): '漏判了两个说话人：',
    ('test_two_speakers_still_caught', 2): '\n>assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s._check\n}(%(py3)s, %(py4)s)\n}',
    ('test_two_speakers_still_caught', 3): 'py0',
    ('test_two_speakers_still_caught', 4): 'self',
    ('test_two_speakers_still_caught', 5): 'py2',
    ('test_two_speakers_still_caught', 6): 'py3',
    ('test_two_speakers_still_caught', 7): 'gate',
    ('test_two_speakers_still_caught', 8): 'py4',
    ('test_two_speakers_still_caught', 9): 'para',
    ('test_two_speakers_still_caught', 10): 'py6',
    ('TestToleranceBands', 0): 'TestToleranceBands',
    ('TestToleranceBands', 1): '统计特征擦边不该当作错误。实测第 2 章连续三次对话占比落在\n13.3%~13.6%（下限 15%），因为那一章的场景本身就偏独处 ——\n硬性打回会让修订环去修一个本不该由它修的问题。',
    ('test_bound_check_three_states', 6): 'ok',
    ('test_bound_check_three_states', 7): 'py1',
    ('test_bound_check_three_states', 8): 'py4',
    ('test_bound_check_three_states', 9): 'assert %(py6)s',
    ('test_bound_check_three_states', 10): 'py6',
    ('test_bound_check_three_states', 13): 'soft',
    ('test_bound_check_three_states', 15): 'hard',
    ('test_upper_bound_tolerance', 6): 'soft',
    ('test_upper_bound_tolerance', 7): 'py1',
    ('test_upper_bound_tolerance', 8): 'py4',
    ('test_upper_bound_tolerance', 9): 'assert %(py6)s',
    ('test_upper_bound_tolerance', 10): 'py6',
    ('test_upper_bound_tolerance', 13): 'hard',
    ('test_zero_tolerance_is_strict', 6): 'hard',
    ('test_zero_tolerance_is_strict', 7): 'py1',
    ('test_zero_tolerance_is_strict', 8): 'py4',
    ('test_zero_tolerance_is_strict', 9): 'assert %(py6)s',
    ('test_zero_tolerance_is_strict', 10): 'py6',
    ('test_soft_dialogue_ratio_passes_gate', 0): '擦边的稿子放行，把判定交给 judge。',
    ('test_soft_dialogue_ratio_passes_gate', 1): '“嗯呢。”',
    ('test_soft_dialogue_ratio_passes_gate', 3): 'dialogue_ratio',
    ('test_soft_dialogue_ratio_passes_gate', 4): '%(py2)s',
    ('test_soft_dialogue_ratio_passes_gate', 5): 'py2',
    ('test_soft_dialogue_ratio_passes_gate', 6): 'soft',
    ('test_soft_dialogue_ratio_passes_gate', 7): '%(py4)s',
    ('test_soft_dialogue_ratio_passes_gate', 8): 'py4',
    ('test_soft_dialogue_ratio_passes_gate', 9): 'hard',
    ('test_soft_dialogue_ratio_passes_gate', 10): '同一项不该既是警告又是错误',
    ('test_soft_dialogue_ratio_passes_gate', 11): '\n>assert not %(py7)s',
    ('test_soft_dialogue_ratio_passes_gate', 12): 'py7',
    ('test_far_out_of_band_still_fails', 0): '浮动不是放弃底线 —— 差太远仍然打回。',
    ('test_far_out_of_band_still_fails', 1): 'dialogue_ratio',
    ('test_far_out_of_band_still_fails', 2): '他没说话。',
    ('test_far_out_of_band_still_fails', 4): 'py1',
    ('test_far_out_of_band_still_fails', 5): 'py3',
    ('test_far_out_of_band_still_fails', 6): 'rules',
    ('test_far_out_of_band_still_fails', 7): 'py4',
    ('test_far_out_of_band_still_fails', 8): 'gate',
    ('test_far_out_of_band_still_fails', 9): 'py6',
    ('test_far_out_of_band_still_fails', 10): 'py7',
    ('test_far_out_of_band_still_fails', 11): 'make_chapter',
    ('test_far_out_of_band_still_fails', 12): 'py9',
    ('test_far_out_of_band_still_fails', 13): 'py11',
    ('test_far_out_of_band_still_fails', 14): 'py13',
    ('test_far_out_of_band_still_fails', 15): 'py15',
    ('test_far_out_of_band_still_fails', 16): 'assert %(py17)s',
    ('test_far_out_of_band_still_fails', 17): 'py17',
    ('test_soft_violation_labelled', 0): '报告里要看得出是"擦边"还是"真的不行"。',
    ('test_soft_violation_labelled', 2): 'pathlib',
    ('test_soft_violation_labelled', 3): 'config',
    ('test_soft_violation_labelled', 4): 'project.yaml',
    ('test_soft_violation_labelled', 5): 'warn',
    ('test_soft_violation_labelled', 6): '容差内',
    ('test_soft_violation_labelled', 7): 'py1',
    ('test_soft_violation_labelled', 8): 'py3',
    ('test_soft_violation_labelled', 9): 'f',
    ('test_soft_violation_labelled', 10): 'py5',
    ('test_soft_violation_labelled', 11): 'assert %(py7)s',
    ('test_soft_violation_labelled', 12): 'py7',
    ('TestStrayNotes', 0): 'TestStrayNotes',
    ('TestStrayNotes', 2): '第二道防线：writer 那边机械剥掉了，这里再拦一次。\n附言未必总以分隔线开头，但只要它以某种排版元素起头，这条就抓得住。',
    ('test_separator_line_is_an_error', 2): '\n\n---\n\n缝合说明：我统一了年份。',
    ('test_separator_line_is_an_error', 4): 'assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}',
    ('test_separator_line_is_an_error', 5): 'py0',
    ('test_separator_line_is_an_error', 6): 'report',
    ('test_separator_line_is_an_error', 7): 'py2',
    ('test_separator_line_is_an_error', 10): 'assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_separator_line_is_an_error', 11): 'any',
    ('test_separator_line_is_an_error', 12): 'py4',
    ('<genexpr>', 0): 'stray_notes',
    ('test_clean_chapter_has_none', 4): 'assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_clean_chapter_has_none', 5): 'py0',
    ('test_clean_chapter_has_none', 6): 'any',
    ('test_clean_chapter_has_none', 7): 'py2',
    ('test_clean_chapter_has_none', 8): 'py4',
    ('<genexpr>', 0): 'stray_notes',
    ('test_em_dash_paragraph_is_not_flagged', 0): '整段只有一个破折号的写法很少见但合法，不该误伤。',
    ('test_em_dash_paragraph_is_not_flagged', 4): 'assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}',
    ('test_em_dash_paragraph_is_not_flagged', 5): 'py0',
    ('test_em_dash_paragraph_is_not_flagged', 6): 'any',
    ('test_em_dash_paragraph_is_not_flagged', 7): 'py2',
    ('test_em_dash_paragraph_is_not_flagged', 8): 'py4',
    ('<genexpr>', 0): 'stray_notes',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────
def gate(project_config):
    pass  # 无 docstring
    # ── 函数体（字节码重建见 BODY 段）──
    # |  17           RESUME                   0
    # |  19           LOAD_GLOBAL              1 (Gate + NULL)
    # |               LOAD_FAST_BORROW         0 (project_config)
    # |               CALL                     1
    # |               RETURN_VALUE

def rules(report):
    'error'
    # ── 函数体（字节码重建见 BODY 段）──
    # |   22           RESUME                   0
    # |   23           LOAD_FAST_BORROW         0 (report)
    # |                LOAD_ATTR                0 (findings)
    # |                GET_ITER
    # |                LOAD_FAST_AND_CLEAR      1 (f)
    # |                SWAP                     2
    # |        L1:     BUILD_SET                0
    # |                SWAP                     2
    # |        L2:     FOR_ITER                33 (to L5)
    # |                STORE_FAST_LOAD_FAST    17 (f, f)
    # |                LOAD_ATTR                2 (severity)
    # |                LOAD_CONST               0 ('error')
    # |                COMPARE_OP              88 (bool(==))
    # |        L3:     POP_JUMP_IF_TRUE         3 (to L4)
    # |                NOT_TAKEN
    # |                JUMP_BACKWARD           21 (to L2)
    # |        L4:     LOAD_FAST_BORROW         1 (f)
    # |                LOAD_ATTR                4 (rule)
    # |                SET_ADD                  2
    # |                JUMP_BACKWARD           35 (to L2)
    # |        L5:     END_FOR
    # |                POP_ITER
    # |        L6:     SWAP                     2
    # |                STORE_FAST               1 (f)
    # |                RETURN_VALUE
    # |   --   L7:     SWAP                     2
    # |                POP_TOP
    # |   23           SWAP                     2
    # |                STORE_FAST               1 (f)
    # |                RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L3 -> L7 [2]
    # |   L4 to L6 -> L7 [2]

class TestBaseline:
    'TestBaseline'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  26           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestBaseline')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          26
    # |               STORE_NAME               3 (__firstlineno__)
    # |  27           LOAD_CONST               1 (<code object test_compliant_chapter_passes at 0x7a752f3300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 27>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_compliant_chapter_passes)
    # |  31           LOAD_CONST               2 (<code object test_stats_are_reported at 0x7a74c96a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 31>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_stats_are_reported)
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_compliant_chapter_passes at 0x7a752f3300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 27>:
    # |  27           RESUME                   0
    # |  28           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                1 (check + NULL|self)
    # |               LOAD_GLOBAL              3 (make_chapter + NULL)
    # |               CALL                     0
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               1 (('expected_ch',))
    # |               CALL_KW                  2
    # |               STORE_FAST               2 (report)
    # |  29           LOAD_FAST_BORROW         2 (report)
    # |               LOAD_ATTR                4 (passed)
    # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       182 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_format_assertmsg)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (report)
    # |               LOAD_ATTR               11 (render + NULL|self)
    # |               CALL                     0
    # |               CALL                     1
    # |               LOAD_CONST               2 ('\n>assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |               BINARY_OP                0 (+)
    # |               LOAD_CONST               3 ('py0')
    # |               LOAD_CONST               4 ('report')
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
    # |               LOAD_FAST_BORROW         2 (report)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (report)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               4 ('report')
    # |       L3:     LOAD_CONST               5 ('py2')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               4 (@py_format3)
    # |               LOAD_GLOBAL             21 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               22 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_format3)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               6 (None)
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_stats_are_reported at 0x7a74c96a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 31>:
    # |  31            RESUME                   0
    # |  32            LOAD_FAST_BORROW         1 (gate)
    # |                LOAD_ATTR                1 (check + NULL|self)
    # |                LOAD_GLOBAL              3 (make_chapter + NULL)
    # |                CALL                     0
    # |                CALL                     1
    # |                LOAD_ATTR                4 (stats)
    # |                STORE_FAST               3 (stats)
    # |  33            LOAD_CONST               0 (2800)
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert0, stats)
    # |                LOAD_CONST               1 ('word_count')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                COMPARE_OP              42 (<=)
    # |                STORE_FAST               6 (@py_assert2)
    # |                LOAD_CONST               2 (3600)
    # |                STORE_FAST_LOAD_FAST   117 (@py_assert6, @py_assert4)
    # |                LOAD_FAST_BORROW         7 (@py_assert6)
    # |                COMPARE_OP              42 (<=)
    # |                STORE_FAST_LOAD_FAST   134 (@py_assert3, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE        9 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       144 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              21 (('<=', '<='))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert2, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                LOAD_CONST              22 (('%(py1)s <= %(py5)s', '%(py5)s <= %(py7)s'))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert4)
    # |                LOAD_FAST_BORROW         7 (@py_assert6)
    # |                BUILD_TUPLE              3
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py5')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py7')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert6)
    # |                CALL                     1
    # |                BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format8)
    # |                LOAD_CONST               6 ('assert %(py9)s')
    # |                LOAD_CONST               7 ('py9')
    # |                LOAD_FAST_BORROW         9 (@py_format8)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format10)
    # |                LOAD_GLOBAL             13 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format10)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L2:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert3)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   87 (@py_assert4, @py_assert6)
    # |  34            LOAD_FAST_BORROW         2 (project_config)
    # |                LOAD_CONST               9 ('length')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              10 ('dialogue_ratio_min')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST              11 (lo)
    # |  35            LOAD_FAST_BORROW         2 (project_config)
    # |                LOAD_CONST               9 ('length')
    # |                BINARY_OP               26 ([])
    # |                LOAD_CONST              11 ('dialogue_ratio_max')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST              12 (hi)
    # |  36            LOAD_FAST_BORROW         3 (stats)
    # |                LOAD_CONST              12 ('dialogue_ratio')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST_LOAD_FAST   139 (@py_assert3, lo)
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                COMPARE_OP              42 (<=)
    # |                STORE_FAST_LOAD_FAST   216 (@py_assert1, @py_assert3)
    # |                LOAD_FAST_BORROW        12 (hi)
    # |                COMPARE_OP              42 (<=)
    # |                STORE_FAST_LOAD_FAST   109 (@py_assert2, @py_assert1)
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       10 (to L3)
    # |                NOT_TAKEN
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       256 (to L10)
    # |                NOT_TAKEN
    # |        L3:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              21 (('<=', '<='))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 214 (@py_assert1, @py_assert2)
    # |                BUILD_TUPLE              2
    # |                LOAD_CONST              23 (('%(py0)s <= %(py4)s', '%(py4)s <= %(py5)s'))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 184 (lo, @py_assert3)
    # |                LOAD_FAST_BORROW        12 (hi)
    # |                BUILD_TUPLE              3
    # |                CALL                     4
    # |                LOAD_CONST              13 ('py0')
    # |                LOAD_CONST              14 ('lo')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (lo)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (lo)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST              14 ('lo')
    # |        L6:     LOAD_CONST              15 ('py4')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py5')
    # |                LOAD_CONST              16 ('hi')
    # |                LOAD_GLOBAL             16 (@py_builtins)
    # |                LOAD_ATTR               18 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (hi)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        12 (hi)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              16 ('hi')
    # |        L9:     BUILD_MAP                3
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              14 (@py_format6)
    # |                LOAD_CONST              17 ('assert %(py7)s')
    # |                LOAD_CONST               5 ('py7')
    # |                LOAD_FAST_BORROW        14 (@py_format6)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format8)
    # |                LOAD_GLOBAL             13 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format8)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST              13 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  104 (@py_assert2, @py_assert3)
    # |  37            LOAD_FAST_BORROW         3 (stats)
    # |                LOAD_CONST              18 ('paragraphs')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               4 (@py_assert0)
    # |                LOAD_SMALL_INT           0
    # |                STORE_FAST_LOAD_FAST   132 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                COMPARE_OP             132 (>)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       121 (to L11)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              24 (('>',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              25 (('%(py1)s > %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py4')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert3)
    # |                CALL                     1
    # |                BUILD_MAP                2
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              15 (@py_format5)
    # |                LOAD_CONST              19 ('assert %(py6)s')
    # |                LOAD_CONST              20 ('py6')
    # |                LOAD_FAST_BORROW        15 (@py_format5)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              16 (@py_format7)
    # |                LOAD_GLOBAL             13 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               14 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        16 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L11:     LOAD_CONST               8 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  104 (@py_assert2, @py_assert3)
    # |                LOAD_CONST               8 (None)
    # |                RETURN_VALUE

    def test_compliant_chapter_passes(self, gate):
        '\n>assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  27           RESUME                   0
        # |  28           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                1 (check + NULL|self)
        # |               LOAD_GLOBAL              3 (make_chapter + NULL)
        # |               CALL                     0
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               1 (('expected_ch',))
        # |               CALL_KW                  2
        # |               STORE_FAST               2 (report)
        # |  29           LOAD_FAST_BORROW         2 (report)
        # |               LOAD_ATTR                4 (passed)
        # |               STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       182 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_format_assertmsg)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (report)
        # |               LOAD_ATTR               11 (render + NULL|self)
        # |               CALL                     0
        # |               CALL                     1
        # |               LOAD_CONST               2 ('\n>assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |               BINARY_OP                0 (+)
        # |               LOAD_CONST               3 ('py0')
        # |               LOAD_CONST               4 ('report')
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
        # |               LOAD_FAST_BORROW         2 (report)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (report)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               4 ('report')
        # |       L3:     LOAD_CONST               5 ('py2')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               4 (@py_format3)
        # |               LOAD_GLOBAL             21 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               22 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_format3)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               6 (None)
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_CONST               6 (None)
        # |               RETURN_VALUE

    def test_stats_are_reported(self, gate, project_config):
        'word_count'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  31            RESUME                   0
        # |  32            LOAD_FAST_BORROW         1 (gate)
        # |                LOAD_ATTR                1 (check + NULL|self)
        # |                LOAD_GLOBAL              3 (make_chapter + NULL)
        # |                CALL                     0
        # |                CALL                     1
        # |                LOAD_ATTR                4 (stats)
        # |                STORE_FAST               3 (stats)
        # |  33            LOAD_CONST               0 (2800)
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert0, stats)
        # |                LOAD_CONST               1 ('word_count')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert4, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                COMPARE_OP              42 (<=)
        # |                STORE_FAST               6 (@py_assert2)
        # |                LOAD_CONST               2 (3600)
        # |                STORE_FAST_LOAD_FAST   117 (@py_assert6, @py_assert4)
        # |                LOAD_FAST_BORROW         7 (@py_assert6)
        # |                COMPARE_OP              42 (<=)
        # |                STORE_FAST_LOAD_FAST   134 (@py_assert3, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE        9 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       144 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              21 (('<=', '<='))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 104 (@py_assert2, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                LOAD_CONST              22 (('%(py1)s <= %(py5)s', '%(py5)s <= %(py7)s'))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert4)
        # |                LOAD_FAST_BORROW         7 (@py_assert6)
        # |                BUILD_TUPLE              3
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py5')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py7')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert6)
        # |                CALL                     1
        # |                BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format8)
        # |                LOAD_CONST               6 ('assert %(py9)s')
        # |                LOAD_CONST               7 ('py9')
        # |                LOAD_FAST_BORROW         9 (@py_format8)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format10)
        # |                LOAD_GLOBAL             13 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               14 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format10)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L2:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert3)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   87 (@py_assert4, @py_assert6)
        # |  34            LOAD_FAST_BORROW         2 (project_config)
        # |                LOAD_CONST               9 ('length')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              10 ('dialogue_ratio_min')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST              11 (lo)
        # |  35            LOAD_FAST_BORROW         2 (project_config)
        # |                LOAD_CONST               9 ('length')
        # |                BINARY_OP               26 ([])
        # |                LOAD_CONST              11 ('dialogue_ratio_max')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST              12 (hi)
        # |  36            LOAD_FAST_BORROW         3 (stats)
        # |                LOAD_CONST              12 ('dialogue_ratio')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST_LOAD_FAST   139 (@py_assert3, lo)
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                COMPARE_OP              42 (<=)
        # |                STORE_FAST_LOAD_FAST   216 (@py_assert1, @py_assert3)
        # |                LOAD_FAST_BORROW        12 (hi)
        # |                COMPARE_OP              42 (<=)
        # |                STORE_FAST_LOAD_FAST   109 (@py_assert2, @py_assert1)
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       10 (to L3)
        # |                NOT_TAKEN
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       256 (to L10)
        # |                NOT_TAKEN
        # |        L3:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              21 (('<=', '<='))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 214 (@py_assert1, @py_assert2)
        # |                BUILD_TUPLE              2
        # |                LOAD_CONST              23 (('%(py0)s <= %(py4)s', '%(py4)s <= %(py5)s'))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 184 (lo, @py_assert3)
        # |                LOAD_FAST_BORROW        12 (hi)
        # |                BUILD_TUPLE              3
        # |                CALL                     4
        # |                LOAD_CONST              13 ('py0')
        # |                LOAD_CONST              14 ('lo')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (lo)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (lo)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST              14 ('lo')
        # |        L6:     LOAD_CONST              15 ('py4')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py5')
        # |                LOAD_CONST              16 ('hi')
        # |                LOAD_GLOBAL             16 (@py_builtins)
        # |                LOAD_ATTR               18 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (hi)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        12 (hi)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              16 ('hi')
        # |        L9:     BUILD_MAP                3
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              14 (@py_format6)
        # |                LOAD_CONST              17 ('assert %(py7)s')
        # |                LOAD_CONST               5 ('py7')
        # |                LOAD_FAST_BORROW        14 (@py_format6)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format8)
        # |                LOAD_GLOBAL             13 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               14 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format8)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST              13 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  104 (@py_assert2, @py_assert3)
        # |  37            LOAD_FAST_BORROW         3 (stats)
        # |                LOAD_CONST              18 ('paragraphs')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               4 (@py_assert0)
        # |                LOAD_SMALL_INT           0
        # |                STORE_FAST_LOAD_FAST   132 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                COMPARE_OP             132 (>)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       121 (to L11)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              24 (('>',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              25 (('%(py1)s > %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py4')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert3)
        # |                CALL                     1
        # |                BUILD_MAP                2
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              15 (@py_format5)
        # |                LOAD_CONST              19 ('assert %(py6)s')
        # |                LOAD_CONST              20 ('py6')
        # |                LOAD_FAST_BORROW        15 (@py_format5)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              16 (@py_format7)
        # |                LOAD_GLOBAL             13 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               14 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        16 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L11:     LOAD_CONST               8 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  104 (@py_assert2, @py_assert3)
        # |                LOAD_CONST               8 (None)
        # |                RETURN_VALUE


class TestTitle:
    'TestTitle'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  40           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestTitle')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          40
    # |               STORE_NAME               3 (__firstlineno__)
    # |  41           LOAD_CONST               1 (<code object test_missing_title_caught at 0x7a74d88a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 41>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_missing_title_caught)
    # |  44           LOAD_CONST               2 (<code object test_malformed_title_caught at 0x7a74d8a300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 44>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_malformed_title_caught)
    # |  48           LOAD_CONST               3 (<code object test_wrong_chapter_number_caught at 0x7a74d96400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 48>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_wrong_chapter_number_caught)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_missing_title_caught at 0x7a74d88a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 41>:
    # |  41           RESUME                   0
    # |  42           LOAD_CONST               0 ('title')
    # |               STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
    # |               LOAD_ATTR                0 (check)
    # |               STORE_FAST               3 (@py_assert5)
    # |               LOAD_CONST               1 ('正文没有标题。')
    # |               STORE_FAST               4 (@py_assert7)
    # |               LOAD_CONST               2 (400)
    # |               STORE_FAST_LOAD_FAST    84 (@py_assert9, @py_assert7)
    # |               LOAD_FAST_BORROW         5 (@py_assert9)
    # |               BINARY_OP                5 (*)
    # |               STORE_FAST_LOAD_FAST    99 (@py_assert11, @py_assert5)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert11)
    # |               CALL                     1
    # |               STORE_FAST               7 (@py_assert12)
    # |               LOAD_GLOBAL              3 (rules + NULL)
    # |               LOAD_FAST_BORROW         7 (@py_assert12)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   130 (@py_assert14, @py_assert0)
    # |               LOAD_FAST_BORROW         8 (@py_assert14)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       373 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('in',))
    # |               LOAD_FAST_BORROW         9 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}((%(py8)s * %(py10)s))\n})\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 40 (@py_assert0, @py_assert14)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               3 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               4 ('py3')
    # |               LOAD_CONST               5 ('rules')
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
    # |               LOAD_GLOBAL              2 (rules)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              2 (rules)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               5 ('rules')
    # |       L3:     LOAD_CONST               6 ('py4')
    # |               LOAD_CONST               7 ('gate')
    # |               LOAD_GLOBAL             10 (@py_builtins)
    # |               LOAD_ATTR               12 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               14 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (gate)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (gate)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               7 ('gate')
    # |       L6:     LOAD_CONST               8 ('py6')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py8')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert7)
    # |               CALL                     1
    # |               LOAD_CONST              10 ('py10')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert9)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py13')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert12)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py15')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert14)
    # |               CALL                     1
    # |               BUILD_MAP                8
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format16)
    # |               LOAD_CONST              13 ('assert %(py17)s')
    # |               LOAD_CONST              14 ('py17')
    # |               LOAD_FAST_BORROW        10 (@py_format16)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              11 (@py_format18)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        11 (@py_format18)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              15 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST               9 (@py_assert2)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert7)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert9)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert11)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  120 (@py_assert12, @py_assert14)
    # |               LOAD_CONST              15 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_malformed_title_caught at 0x7a74d8a300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 44>:
    # |  44            RESUME                   0
    # |  45            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                CALL                     0
    # |                LOAD_ATTR                3 (replace + NULL|self)
    # |                LOAD_CONST               0 ('## 第1章 雨天')
    # |                LOAD_CONST               1 ('## 第一章 雨天')
    # |                CALL                     2
    # |                STORE_FAST               2 (text)
    # |  46            LOAD_CONST               2 ('title')
    # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
    # |                LOAD_ATTR                4 (check)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_GLOBAL              7 (rules + NULL)
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       407 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('rules')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('rules')
    # |        L3:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST               7 ('gate')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('text')
    # |                LOAD_GLOBAL             14 (@py_builtins)
    # |                LOAD_ATTR               16 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('text')
    # |        L9:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format12)
    # |                LOAD_CONST              13 ('assert %(py13)s')
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_FAST_BORROW         8 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format14)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_wrong_chapter_number_caught at 0x7a74d96400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 48>:
    # |  48           RESUME                   0
    # |  49           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                1 (check + NULL|self)
    # |               LOAD_GLOBAL              3 (make_chapter + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               1 (('ch',))
    # |               CALL_KW                  1
    # |               LOAD_SMALL_INT           7
    # |               LOAD_CONST               2 (('expected_ch',))
    # |               CALL_KW                  2
    # |               STORE_FAST               2 (report)
    # |  50           LOAD_CONST               3 ('title')
    # |               STORE_FAST               3 (@py_assert0)
    # |               LOAD_GLOBAL              5 (rules + NULL)
    # |               LOAD_FAST_BORROW         2 (report)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    67 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       285 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR                8 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              13 (('in',))
    # |               LOAD_FAST_BORROW         5 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              14 (('%(py1)s in %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               4 ('py1')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py3')
    # |               LOAD_CONST               6 ('rules')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (rules)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              4 (rules)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               6 ('rules')
    # |       L3:     LOAD_CONST               7 ('py4')
    # |               LOAD_CONST               8 ('report')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               16 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (report)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (report)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               8 ('report')
    # |       L6:     LOAD_CONST               9 ('py6')
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               10 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_CONST              10 ('assert %(py8)s')
    # |               LOAD_CONST              11 ('py8')
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format9)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL              6 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              12 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert5)
    # |               LOAD_CONST              12 (None)
    # |               RETURN_VALUE

    def test_missing_title_caught(self, gate):
        'title'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  41           RESUME                   0
        # |  42           LOAD_CONST               0 ('title')
        # |               STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
        # |               LOAD_ATTR                0 (check)
        # |               STORE_FAST               3 (@py_assert5)
        # |               LOAD_CONST               1 ('正文没有标题。')
        # |               STORE_FAST               4 (@py_assert7)
        # |               LOAD_CONST               2 (400)
        # |               STORE_FAST_LOAD_FAST    84 (@py_assert9, @py_assert7)
        # |               LOAD_FAST_BORROW         5 (@py_assert9)
        # |               BINARY_OP                5 (*)
        # |               STORE_FAST_LOAD_FAST    99 (@py_assert11, @py_assert5)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert11)
        # |               CALL                     1
        # |               STORE_FAST               7 (@py_assert12)
        # |               LOAD_GLOBAL              3 (rules + NULL)
        # |               LOAD_FAST_BORROW         7 (@py_assert12)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   130 (@py_assert14, @py_assert0)
        # |               LOAD_FAST_BORROW         8 (@py_assert14)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       373 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('in',))
        # |               LOAD_FAST_BORROW         9 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}((%(py8)s * %(py10)s))\n})\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 40 (@py_assert0, @py_assert14)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               3 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               4 ('py3')
        # |               LOAD_CONST               5 ('rules')
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
        # |               LOAD_GLOBAL              2 (rules)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              2 (rules)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               5 ('rules')
        # |       L3:     LOAD_CONST               6 ('py4')
        # |               LOAD_CONST               7 ('gate')
        # |               LOAD_GLOBAL             10 (@py_builtins)
        # |               LOAD_ATTR               12 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               14 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (gate)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (gate)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               7 ('gate')
        # |       L6:     LOAD_CONST               8 ('py6')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py8')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert7)
        # |               CALL                     1
        # |               LOAD_CONST              10 ('py10')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert9)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py13')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert12)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py15')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert14)
        # |               CALL                     1
        # |               BUILD_MAP                8
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format16)
        # |               LOAD_CONST              13 ('assert %(py17)s')
        # |               LOAD_CONST              14 ('py17')
        # |               LOAD_FAST_BORROW        10 (@py_format16)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              11 (@py_format18)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        11 (@py_format18)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              15 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST               9 (@py_assert2)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert7)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert9)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert11)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  120 (@py_assert12, @py_assert14)
        # |               LOAD_CONST              15 (None)
        # |               RETURN_VALUE

    def test_malformed_title_caught(self, gate):
        '## 第1章 雨天'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  44            RESUME                   0
        # |  45            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                CALL                     0
        # |                LOAD_ATTR                3 (replace + NULL|self)
        # |                LOAD_CONST               0 ('## 第1章 雨天')
        # |                LOAD_CONST               1 ('## 第一章 雨天')
        # |                CALL                     2
        # |                STORE_FAST               2 (text)
        # |  46            LOAD_CONST               2 ('title')
        # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
        # |                LOAD_ATTR                4 (check)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_GLOBAL              7 (rules + NULL)
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       407 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('rules')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('rules')
        # |        L3:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST               7 ('gate')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('text')
        # |                LOAD_GLOBAL             14 (@py_builtins)
        # |                LOAD_ATTR               16 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              10 ('text')
        # |        L9:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format12)
        # |                LOAD_CONST              13 ('assert %(py13)s')
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_FAST_BORROW         8 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format14)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE

    def test_wrong_chapter_number_caught(self, gate):
        'title'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  48           RESUME                   0
        # |  49           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                1 (check + NULL|self)
        # |               LOAD_GLOBAL              3 (make_chapter + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               1 (('ch',))
        # |               CALL_KW                  1
        # |               LOAD_SMALL_INT           7
        # |               LOAD_CONST               2 (('expected_ch',))
        # |               CALL_KW                  2
        # |               STORE_FAST               2 (report)
        # |  50           LOAD_CONST               3 ('title')
        # |               STORE_FAST               3 (@py_assert0)
        # |               LOAD_GLOBAL              5 (rules + NULL)
        # |               LOAD_FAST_BORROW         2 (report)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    67 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       285 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR                8 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              13 (('in',))
        # |               LOAD_FAST_BORROW         5 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              14 (('%(py1)s in %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 52 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               4 ('py1')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py3')
        # |               LOAD_CONST               6 ('rules')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (rules)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              4 (rules)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               6 ('rules')
        # |       L3:     LOAD_CONST               7 ('py4')
        # |               LOAD_CONST               8 ('report')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               16 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (report)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (report)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               8 ('report')
        # |       L6:     LOAD_CONST               9 ('py6')
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               10 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_CONST              10 ('assert %(py8)s')
        # |               LOAD_CONST              11 ('py8')
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format9)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL              6 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              12 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   84 (@py_assert2, @py_assert5)
        # |               LOAD_CONST              12 (None)
        # |               RETURN_VALUE


class TestLength:
    'TestLength'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  53           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestLength')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          53
    # |               STORE_NAME               3 (__firstlineno__)
    # |  54           LOAD_CONST               1 (<code object test_too_short_caught at 0x7a74d8ad00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 54>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_too_short_caught)
    # |  57           LOAD_CONST               2 (<code object test_too_long_caught at 0x7a74d8b700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 57>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_too_long_caught)
    # |  60           LOAD_CONST               3 (<code object test_dialogue_ratio_too_low_caught at 0x7a74d75e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 60>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_dialogue_ratio_too_low_caught)
    # |  64           LOAD_CONST               4 (<code object test_dialogue_ratio_too_high_caught at 0x7a74d75900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 64>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_dialogue_ratio_too_high_caught)
    # |               LOAD_CONST               5 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_too_short_caught at 0x7a74d8ad00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 54>:
    # |  54            RESUME                   0
    # |  55            LOAD_CONST               0 ('length')
    # |                STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
    # |                LOAD_ATTR                0 (check)
    # |                STORE_FAST               3 (@py_assert5)
    # |                LOAD_CONST               1 (500)
    # |                STORE_FAST               4 (@py_assert8)
    # |                LOAD_GLOBAL              3 (make_chapter + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                LOAD_CONST               2 (('target_words',))
    # |                CALL_KW                  1
    # |                STORE_FAST_LOAD_FAST    83 (@py_assert10, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert10)
    # |                CALL                     1
    # |                STORE_FAST               6 (@py_assert12)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         6 (@py_assert12)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   114 (@py_assert14, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert14)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       459 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              18 (('in',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py11)s\n{%(py11)s = %(py7)s(target_words=%(py9)s)\n})\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (@py_assert0, @py_assert14)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('rules')
    # |        L3:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST               7 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('make_chapter')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (make_chapter)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (make_chapter)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('make_chapter')
    # |        L9:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py13')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert12)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py15')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert14)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format16)
    # |                LOAD_CONST              15 ('assert %(py17)s')
    # |                LOAD_CONST              16 ('py17')
    # |                LOAD_FAST_BORROW         9 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format18)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              17 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert10)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert12, @py_assert14)
    # |                LOAD_CONST              17 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_too_long_caught at 0x7a74d8b700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 57>:
    # |  57            RESUME                   0
    # |  58            LOAD_CONST               0 ('length')
    # |                STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
    # |                LOAD_ATTR                0 (check)
    # |                STORE_FAST               3 (@py_assert5)
    # |                LOAD_CONST               1 (6000)
    # |                STORE_FAST               4 (@py_assert8)
    # |                LOAD_GLOBAL              3 (make_chapter + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                LOAD_CONST               2 (('target_words',))
    # |                CALL_KW                  1
    # |                STORE_FAST_LOAD_FAST    83 (@py_assert10, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert10)
    # |                CALL                     1
    # |                STORE_FAST               6 (@py_assert12)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         6 (@py_assert12)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   114 (@py_assert14, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert14)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       459 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              18 (('in',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              19 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py11)s\n{%(py11)s = %(py7)s(target_words=%(py9)s)\n})\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (@py_assert0, @py_assert14)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('rules')
    # |        L3:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST               7 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('make_chapter')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (make_chapter)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (make_chapter)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('make_chapter')
    # |        L9:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py13')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert12)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py15')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert14)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format16)
    # |                LOAD_CONST              15 ('assert %(py17)s')
    # |                LOAD_CONST              16 ('py17')
    # |                LOAD_FAST_BORROW         9 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format18)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              17 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert10)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert12, @py_assert14)
    # |                LOAD_CONST              17 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_dialogue_ratio_too_low_caught at 0x7a74d75e00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 60>:
    # |  60            RESUME                   0
    # |  61            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                LOAD_CONST               0 ('他没有回答。')
    # |                LOAD_CONST               1 (('dialogue',))
    # |                CALL_KW                  1
    # |                STORE_FAST               2 (text)
    # |  62            LOAD_CONST               2 ('dialogue_ratio')
    # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
    # |                LOAD_ATTR                2 (check)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       407 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('rules')
    # |        L3:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST               7 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('text')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('text')
    # |        L9:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format12)
    # |                LOAD_CONST              13 ('assert %(py13)s')
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_FAST_BORROW         8 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format14)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_dialogue_ratio_too_high_caught at 0x7a74d75900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 64>:
    # |  64            RESUME                   0
    # |  65            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                LOAD_CONST               0 ('她笑了。')
    # |                LOAD_CONST               1 (('narration',))
    # |                CALL_KW                  1
    # |                STORE_FAST               2 (text)
    # |  66            LOAD_CONST               2 ('dialogue_ratio')
    # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
    # |                LOAD_ATTR                2 (check)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       407 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('rules')
    # |        L3:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST               7 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('text')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('text')
    # |        L9:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format12)
    # |                LOAD_CONST              13 ('assert %(py13)s')
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_FAST_BORROW         8 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format14)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE

    def test_too_short_caught(self, gate):
        'length'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  54            RESUME                   0
        # |  55            LOAD_CONST               0 ('length')
        # |                STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
        # |                LOAD_ATTR                0 (check)
        # |                STORE_FAST               3 (@py_assert5)
        # |                LOAD_CONST               1 (500)
        # |                STORE_FAST               4 (@py_assert8)
        # |                LOAD_GLOBAL              3 (make_chapter + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                LOAD_CONST               2 (('target_words',))
        # |                CALL_KW                  1
        # |                STORE_FAST_LOAD_FAST    83 (@py_assert10, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert10)
        # |                CALL                     1
        # |                STORE_FAST               6 (@py_assert12)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         6 (@py_assert12)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   114 (@py_assert14, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert14)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       459 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              18 (('in',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py11)s\n{%(py11)s = %(py7)s(target_words=%(py9)s)\n})\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (@py_assert0, @py_assert14)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('rules')
        # |        L3:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST               7 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('make_chapter')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (make_chapter)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (make_chapter)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              10 ('make_chapter')
        # |        L9:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert10)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py13')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert12)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py15')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert14)
        # |                CALL                     1
        # |                BUILD_MAP                9
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format16)
        # |                LOAD_CONST              15 ('assert %(py17)s')
        # |                LOAD_CONST              16 ('py17')
        # |                LOAD_FAST_BORROW         9 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format18)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format18)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              17 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert10)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert12, @py_assert14)
        # |                LOAD_CONST              17 (None)
        # |                RETURN_VALUE

    def test_too_long_caught(self, gate):
        'length'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  57            RESUME                   0
        # |  58            LOAD_CONST               0 ('length')
        # |                STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
        # |                LOAD_ATTR                0 (check)
        # |                STORE_FAST               3 (@py_assert5)
        # |                LOAD_CONST               1 (6000)
        # |                STORE_FAST               4 (@py_assert8)
        # |                LOAD_GLOBAL              3 (make_chapter + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                LOAD_CONST               2 (('target_words',))
        # |                CALL_KW                  1
        # |                STORE_FAST_LOAD_FAST    83 (@py_assert10, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert10)
        # |                CALL                     1
        # |                STORE_FAST               6 (@py_assert12)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         6 (@py_assert12)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   114 (@py_assert14, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert14)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       459 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              18 (('in',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              19 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py11)s\n{%(py11)s = %(py7)s(target_words=%(py9)s)\n})\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (@py_assert0, @py_assert14)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('rules')
        # |        L3:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST               7 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('make_chapter')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (make_chapter)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (make_chapter)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              10 ('make_chapter')
        # |        L9:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert10)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py13')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert12)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py15')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert14)
        # |                CALL                     1
        # |                BUILD_MAP                9
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format16)
        # |                LOAD_CONST              15 ('assert %(py17)s')
        # |                LOAD_CONST              16 ('py17')
        # |                LOAD_FAST_BORROW         9 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format18)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format18)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              17 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert10)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert12, @py_assert14)
        # |                LOAD_CONST              17 (None)
        # |                RETURN_VALUE

    def test_dialogue_ratio_too_low_caught(self, gate):
        '他没有回答。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  60            RESUME                   0
        # |  61            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                LOAD_CONST               0 ('他没有回答。')
        # |                LOAD_CONST               1 (('dialogue',))
        # |                CALL_KW                  1
        # |                STORE_FAST               2 (text)
        # |  62            LOAD_CONST               2 ('dialogue_ratio')
        # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
        # |                LOAD_ATTR                2 (check)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       407 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('rules')
        # |        L3:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST               7 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('text')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              10 ('text')
        # |        L9:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format12)
        # |                LOAD_CONST              13 ('assert %(py13)s')
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_FAST_BORROW         8 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format14)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE

    def test_dialogue_ratio_too_high_caught(self, gate):
        '她笑了。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  64            RESUME                   0
        # |  65            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                LOAD_CONST               0 ('她笑了。')
        # |                LOAD_CONST               1 (('narration',))
        # |                CALL_KW                  1
        # |                STORE_FAST               2 (text)
        # |  66            LOAD_CONST               2 ('dialogue_ratio')
        # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
        # |                LOAD_ATTR                2 (check)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       407 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('rules')
        # |        L3:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST               7 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('text')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              10 ('text')
        # |        L9:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format12)
        # |                LOAD_CONST              13 ('assert %(py13)s')
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_FAST_BORROW         8 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format14)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE


class TestPunctuation:
    'TestPunctuation'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  69           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestPunctuation')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          69
    # |               STORE_NAME               3 (__firstlineno__)
    # |  70           LOAD_NAME                4 (pytest)
    # |               LOAD_ATTR               10 (mark)
    # |               LOAD_ATTR               13 (parametrize + NULL|self)
    # |  71           LOAD_CONST               1 ('bad_para')
    # |  72           BUILD_LIST               0
    # |               LOAD_CONST               7 (('她停下来,没有回头。', '他问她要去哪里?她摇头。', '她说"我不去了"，然后走了。', '他愣住了...什么也没说。', '他愣住了…什么也没说。', '她终于开口--声音很轻。', '她终于开口—声音很轻。', '他喊了一声！！她没有回头。'))
    # |               LIST_EXTEND              1
    # |  70           CALL                     2
    # |  83           LOAD_CONST               2 (<code object test_violation_caught at 0x7a74c9b200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 70>)
    # |               MAKE_FUNCTION
    # |  70           CALL                     0
    # |  83           STORE_NAME               7 (test_violation_caught)
    # |  87           LOAD_CONST               3 (<code object test_correct_forms_pass at 0x7a74c99400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 87>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_correct_forms_pass)
    # |  92           LOAD_CONST               4 (<code object test_halfwidth_in_numbers_not_flagged at 0x7a74d98000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 92>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_halfwidth_in_numbers_not_flagged)
    # |               LOAD_CONST               5 (())
    # |               STORE_NAME              10 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_violation_caught at 0x7a74c9b200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 70>:
    # |  70            RESUME                   0
    # |  84            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                LOAD_FAST_BORROW         2 (bad_para)
    # |                LOAD_CONST               0 (('inject',))
    # |                CALL_KW                  1
    # |                STORE_FAST               3 (text)
    # |  85            LOAD_CONST               1 ('punctuation')
    # |                STORE_FAST_LOAD_FAST    65 (@py_assert0, gate)
    # |                LOAD_ATTR                2 (check)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                STORE_FAST               6 (@py_assert8)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   116 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       437 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('in',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               2 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               3 ('py3')
    # |                LOAD_CONST               4 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('rules')
    # |        L3:     LOAD_CONST               5 ('py4')
    # |                LOAD_CONST               6 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               6 ('gate')
    # |        L6:     LOAD_CONST               7 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               8 ('py7')
    # |                LOAD_CONST               9 ('text')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               9 ('text')
    # |        L9:     LOAD_CONST              10 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format12)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              12 ('漏判：')
    # |                LOAD_FAST_BORROW         2 (bad_para)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                LOAD_CONST              13 ('\n>assert %(py13)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_FAST_BORROW         9 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format14)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert8, @py_assert10)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_correct_forms_pass at 0x7a74c99400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 87>:
    # |  87            RESUME                   0
    # |  88            LOAD_CONST               0 ('她想说什么，最终只是摇头——那句话到底没有出口……')
    # |                STORE_FAST               2 (good)
    # |  89            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                LOAD_FAST_BORROW         2 (good)
    # |                LOAD_CONST               1 (('inject',))
    # |                CALL_KW                  1
    # |                STORE_FAST               3 (text)
    # |  90            LOAD_CONST               2 ('punctuation')
    # |                STORE_FAST_LOAD_FAST    65 (@py_assert0, gate)
    # |                LOAD_ATTR                2 (check)
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                STORE_FAST               6 (@py_assert8)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   116 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       407 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('not in',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py1)s not in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('rules')
    # |        L3:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST               7 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('text')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('text')
    # |        L9:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format12)
    # |                LOAD_CONST              13 ('assert %(py13)s')
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_FAST_BORROW         9 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format14)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert8, @py_assert10)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_halfwidth_in_numbers_not_flagged at 0x7a74d98000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 92>:
    # |  92            RESUME                   0
    # |  94            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                LOAD_CONST               1 ('教学楼 3.5 公里外，Wi-Fi 信号断断续续，她把伞往他那边偏了偏。')
    # |                LOAD_CONST               2 (('inject',))
    # |                CALL_KW                  1
    # |                STORE_FAST               2 (text)
    # |  95            LOAD_CONST               3 ('punctuation')
    # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
    # |                LOAD_ATTR                2 (check)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       407 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('not in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py1)s not in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py3')
    # |                LOAD_CONST               6 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               6 ('rules')
    # |        L3:     LOAD_CONST               7 ('py4')
    # |                LOAD_CONST               8 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               8 ('gate')
    # |        L6:     LOAD_CONST               9 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_CONST              11 ('text')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              11 ('text')
    # |        L9:     LOAD_CONST              12 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format12)
    # |                LOAD_CONST              14 ('assert %(py13)s')
    # |                LOAD_CONST              15 ('py13')
    # |                LOAD_FAST_BORROW         8 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format14)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              16 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
    # |                LOAD_CONST              16 (None)
    # |                RETURN_VALUE

    def test_violation_caught(self, gate, bad_para):
        'punctuation'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  70            RESUME                   0
        # |  84            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                LOAD_FAST_BORROW         2 (bad_para)
        # |                LOAD_CONST               0 (('inject',))
        # |                CALL_KW                  1
        # |                STORE_FAST               3 (text)
        # |  85            LOAD_CONST               1 ('punctuation')
        # |                STORE_FAST_LOAD_FAST    65 (@py_assert0, gate)
        # |                LOAD_ATTR                2 (check)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                STORE_FAST               6 (@py_assert8)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   116 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       437 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('in',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               2 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               3 ('py3')
        # |                LOAD_CONST               4 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('rules')
        # |        L3:     LOAD_CONST               5 ('py4')
        # |                LOAD_CONST               6 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               6 ('gate')
        # |        L6:     LOAD_CONST               7 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               8 ('py7')
        # |                LOAD_CONST               9 ('text')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               9 ('text')
        # |        L9:     LOAD_CONST              10 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format12)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              12 ('漏判：')
        # |                LOAD_FAST_BORROW         2 (bad_para)
        # |                FORMAT_SIMPLE
        # |                BUILD_STRING             2
        # |                CALL                     1
        # |                LOAD_CONST              13 ('\n>assert %(py13)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_FAST_BORROW         9 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format14)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert8, @py_assert10)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE

    def test_correct_forms_pass(self, gate):
        '她想说什么，最终只是摇头——那句话到底没有出口……'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  87            RESUME                   0
        # |  88            LOAD_CONST               0 ('她想说什么，最终只是摇头——那句话到底没有出口……')
        # |                STORE_FAST               2 (good)
        # |  89            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                LOAD_FAST_BORROW         2 (good)
        # |                LOAD_CONST               1 (('inject',))
        # |                CALL_KW                  1
        # |                STORE_FAST               3 (text)
        # |  90            LOAD_CONST               2 ('punctuation')
        # |                STORE_FAST_LOAD_FAST    65 (@py_assert0, gate)
        # |                LOAD_ATTR                2 (check)
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                STORE_FAST               6 (@py_assert8)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   116 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       407 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('not in',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py1)s not in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 71 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('rules')
        # |        L3:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST               7 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('text')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              10 ('text')
        # |        L9:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format12)
        # |                LOAD_CONST              13 ('assert %(py13)s')
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_FAST_BORROW         9 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format14)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert8, @py_assert10)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE

    def test_halfwidth_in_numbers_not_flagged(self, gate):
        '"3.5" "Wi-Fi" 里的半角符号是合法的，不能误伤。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  92            RESUME                   0
        # |  94            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                LOAD_CONST               1 ('教学楼 3.5 公里外，Wi-Fi 信号断断续续，她把伞往他那边偏了偏。')
        # |                LOAD_CONST               2 (('inject',))
        # |                CALL_KW                  1
        # |                STORE_FAST               2 (text)
        # |  95            LOAD_CONST               3 ('punctuation')
        # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
        # |                LOAD_ATTR                2 (check)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       407 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('not in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py1)s not in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py3')
        # |                LOAD_CONST               6 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               6 ('rules')
        # |        L3:     LOAD_CONST               7 ('py4')
        # |                LOAD_CONST               8 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               8 ('gate')
        # |        L6:     LOAD_CONST               9 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_CONST              11 ('text')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              11 ('text')
        # |        L9:     LOAD_CONST              12 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format12)
        # |                LOAD_CONST              14 ('assert %(py13)s')
        # |                LOAD_CONST              15 ('py13')
        # |                LOAD_FAST_BORROW         8 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format14)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              16 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
        # |                LOAD_CONST              16 (None)
        # |                RETURN_VALUE


class TestParagraph:
    'TestParagraph'
    # ── 函数体（字节码重建见 BODY 段）──
    # |  98           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestParagraph')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT          98
    # |               STORE_NAME               3 (__firstlineno__)
    # |  99           LOAD_CONST               1 (<code object test_overlong_paragraph_caught at 0x7a74d98500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 99>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_overlong_paragraph_caught)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_overlong_paragraph_caught at 0x7a74d98500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 99>:
    # |  99            RESUME                   0
    # | 100            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                LOAD_CONST              16 ('她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。')
    # |                LOAD_CONST               1 (('inject',))
    # |                CALL_KW                  1
    # |                STORE_FAST               2 (text)
    # | 101            LOAD_CONST               2 ('paragraph')
    # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
    # |                LOAD_ATTR                2 (check)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       407 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              17 (('in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              18 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('rules')
    # |        L3:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST               7 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('text')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('text')
    # |        L9:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format12)
    # |                LOAD_CONST              13 ('assert %(py13)s')
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_FAST_BORROW         8 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format14)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE

    def test_overlong_paragraph_caught(self, gate):
        '她想起很多事情。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  99            RESUME                   0
        # | 100            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                LOAD_CONST              16 ('她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。她想起很多事情。')
        # |                LOAD_CONST               1 (('inject',))
        # |                CALL_KW                  1
        # |                STORE_FAST               2 (text)
        # | 101            LOAD_CONST               2 ('paragraph')
        # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
        # |                LOAD_ATTR                2 (check)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       407 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              17 (('in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              18 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('rules')
        # |        L3:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST               7 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('text')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              10 ('text')
        # |        L9:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format12)
        # |                LOAD_CONST              13 ('assert %(py13)s')
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_FAST_BORROW         8 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format14)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE


class TestDialogue:
    'TestDialogue'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 104           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestDialogue')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         104
    # |               STORE_NAME               3 (__firstlineno__)
    # | 105           LOAD_CONST               1 (<code object test_two_speakers_in_one_paragraph_caught at 0x7a74d98a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 105>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_two_speakers_in_one_paragraph_caught)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_two_speakers_in_one_paragraph_caught at 0x7a74d98a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 105>:
    # | 105            RESUME                   0
    # | 107            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                LOAD_CONST               0 ('“你会湿透的。”他摇头。“我不冷。”')
    # |                LOAD_CONST               1 (('inject',))
    # |                CALL_KW                  1
    # |                STORE_FAST               2 (text)
    # | 108            LOAD_CONST               2 ('dialogue')
    # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
    # |                LOAD_ATTR                2 (check)
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST               5 (@py_assert8)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       407 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              16 (('in',))
    # |                LOAD_FAST_BORROW         7 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               3 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               4 ('py3')
    # |                LOAD_CONST               5 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               5 ('rules')
    # |        L3:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST               7 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST               9 ('py7')
    # |                LOAD_CONST              10 ('text')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              10 ('text')
    # |        L9:     LOAD_CONST              11 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert10)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format12)
    # |                LOAD_CONST              13 ('assert %(py13)s')
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_FAST_BORROW         8 (@py_format12)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format14)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_format14)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              15 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               7 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
    # |                LOAD_CONST              15 (None)
    # |                RETURN_VALUE

    def test_two_speakers_in_one_paragraph_caught(self, gate):
        '“你会湿透的。”他摇头。“我不冷。”'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 105            RESUME                   0
        # | 107            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                LOAD_CONST               0 ('“你会湿透的。”他摇头。“我不冷。”')
        # |                LOAD_CONST               1 (('inject',))
        # |                CALL_KW                  1
        # |                STORE_FAST               2 (text)
        # | 108            LOAD_CONST               2 ('dialogue')
        # |                STORE_FAST_LOAD_FAST    49 (@py_assert0, gate)
        # |                LOAD_ATTR                2 (check)
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST               5 (@py_assert8)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST    99 (@py_assert10, @py_assert0)
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       407 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              16 (('in',))
        # |                LOAD_FAST_BORROW         7 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              17 (('%(py1)s in %(py11)s\n{%(py11)s = %(py3)s(%(py9)s\n{%(py9)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py7)s)\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 54 (@py_assert0, @py_assert10)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               3 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               4 ('py3')
        # |                LOAD_CONST               5 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               5 ('rules')
        # |        L3:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST               7 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST               9 ('py7')
        # |                LOAD_CONST              10 ('text')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              10 ('text')
        # |        L9:     LOAD_CONST              11 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert10)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format12)
        # |                LOAD_CONST              13 ('assert %(py13)s')
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_FAST_BORROW         8 (@py_format12)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format14)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_format14)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              15 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               7 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   86 (@py_assert8, @py_assert10)
        # |                LOAD_CONST              15 (None)
        # |                RETURN_VALUE


class TestAsciiQuotedDialogueStillCounts:
    'TestAsciiQuotedDialogueStillCounts'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 111           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestAsciiQuotedDialogueStillCounts')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         111
    # |               STORE_NAME               3 (__firstlineno__)
    # | 112           LOAD_CONST               1 ('实测事故：模型把整章引号吐成了 ASCII，gate 于是同时报两条 ——\n「ASCII 引号」（真问题）和「对话占比 0.0%，叙述压过了场景」（假问题）。\n后者把 writer 支去补根本不缺的对话，白烧一轮修订。')
    # |               STORE_NAME               4 (__doc__)
    # | 116           LOAD_CONST               2 (<code object test_ascii_quoted_chapter_is_not_read_as_zero_dialogue at 0x7a752b4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 116>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_ascii_quoted_chapter_is_not_read_as_zero_dialogue)
    # | 123           LOAD_CONST               3 (<code object test_a_chapter_really_short_on_dialogue_still_caught at 0x7a74d99400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 123>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_a_chapter_really_short_on_dialogue_still_caught)
    # | 127           LOAD_CONST               4 (<code object test_apostrophe_in_prose_is_not_counted_as_speech at 0x7a74d99900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 127>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_apostrophe_in_prose_is_not_counted_as_speech)
    # |               LOAD_CONST               5 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               6 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_ascii_quoted_chapter_is_not_read_as_zero_dialogue at 0x7a752b4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 116>:
    # | 116            RESUME                   0
    # | 117            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                CALL                     0
    # |                LOAD_ATTR                3 (replace + NULL|self)
    # |                LOAD_CONST               0 ('“')
    # |                LOAD_CONST               1 ('"')
    # |                CALL                     2
    # |                LOAD_ATTR                3 (replace + NULL|self)
    # |                LOAD_CONST               2 ('”')
    # |                LOAD_CONST               1 ('"')
    # |                CALL                     2
    # |                STORE_FAST               2 (text)
    # | 118            LOAD_FAST_BORROW         1 (gate)
    # |                LOAD_ATTR                5 (check + NULL|self)
    # |                LOAD_FAST_BORROW         2 (text)
    # |                CALL                     1
    # |                STORE_FAST               3 (report)
    # | 119            LOAD_FAST_BORROW         3 (report)
    # |                LOAD_ATTR                6 (stats)
    # |                LOAD_CONST               3 ('dialogue_ratio')
    # |                BINARY_OP               26 ([])
    # |                STORE_FAST               4 (@py_assert0)
    # |                LOAD_CONST               4 (0.1)
    # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
    # |                LOAD_FAST_BORROW         5 (@py_assert3)
    # |                COMPARE_OP             132 (>)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                POP_JUMP_IF_TRUE       148 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('>',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py1)s > %(py4)s',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py4')
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
    # |                LOAD_CONST               7 ('对话还在，只是引号写错了')
    # |                CALL                     1
    # |                LOAD_CONST               8 ('\n>assert %(py6)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               9 ('py6')
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
    # |        L1:     LOAD_CONST              10 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
    # | 120            LOAD_CONST               3 ('dialogue_ratio')
    # |                STORE_FAST               4 (@py_assert0)
    # |                LOAD_GLOBAL             21 (rules + NULL)
    # |                LOAD_FAST_BORROW         3 (report)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   148 (@py_assert5, @py_assert0)
    # |                LOAD_FAST_BORROW         9 (@py_assert5)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       312 (to L8)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              21 (('not in',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              22 (('%(py1)s not in %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert0, @py_assert5)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py3')
    # |                LOAD_CONST              12 ('rules')
    # |                LOAD_GLOBAL             22 (@py_builtins)
    # |                LOAD_ATTR               24 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L2)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               26 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             20 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L3)
    # |                NOT_TAKEN
    # |        L2:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             20 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L4)
    # |        L3:     LOAD_CONST              12 ('rules')
    # |        L4:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST              13 ('report')
    # |                LOAD_GLOBAL             22 (@py_builtins)
    # |                LOAD_ATTR               24 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L5)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               26 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (report)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L6)
    # |                NOT_TAKEN
    # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (report)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L7)
    # |        L6:     LOAD_CONST              13 ('report')
    # |        L7:     LOAD_CONST               9 ('py6')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format7)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               14 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              14 ('别把格式问题报成缺对话')
    # |                CALL                     1
    # |                LOAD_CONST              15 ('\n>assert %(py8)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              16 ('py8')
    # |                LOAD_FAST_BORROW         8 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format9)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |        L8:     LOAD_CONST              10 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  105 (@py_assert2, @py_assert5)
    # | 121            LOAD_CONST              17 ('punctuation')
    # |                STORE_FAST               4 (@py_assert0)
    # |                LOAD_GLOBAL             21 (rules + NULL)
    # |                LOAD_FAST_BORROW         3 (report)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   148 (@py_assert5, @py_assert0)
    # |                LOAD_FAST_BORROW         9 (@py_assert5)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       312 (to L15)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               10 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              23 (('in',))
    # |                LOAD_FAST_BORROW         6 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              24 (('%(py1)s in %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert0, @py_assert5)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               5 ('py1')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST              11 ('py3')
    # |                LOAD_CONST              12 ('rules')
    # |                LOAD_GLOBAL             22 (@py_builtins)
    # |                LOAD_ATTR               24 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L9)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               26 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             20 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L10)
    # |                NOT_TAKEN
    # |        L9:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             20 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L11)
    # |       L10:     LOAD_CONST              12 ('rules')
    # |       L11:     LOAD_CONST               6 ('py4')
    # |                LOAD_CONST              13 ('report')
    # |                LOAD_GLOBAL             22 (@py_builtins)
    # |                LOAD_ATTR               24 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L12)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               26 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (report)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L13)
    # |                NOT_TAKEN
    # |       L12:     LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (report)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L14)
    # |       L13:     LOAD_CONST              13 ('report')
    # |       L14:     LOAD_CONST               9 ('py6')
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         9 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                4
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format7)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               14 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST              18 ('引号错了仍然要报')
    # |                CALL                     1
    # |                LOAD_CONST              15 ('\n>assert %(py8)s')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST              16 ('py8')
    # |                LOAD_FAST_BORROW         8 (@py_format7)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format9)
    # |                LOAD_GLOBAL             17 (AssertionError + NULL)
    # |                LOAD_GLOBAL              8 (@pytest_ar)
    # |                LOAD_ATTR               18 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format9)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L15:     LOAD_CONST              10 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  105 (@py_assert2, @py_assert5)
    # |                LOAD_CONST              10 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_a_chapter_really_short_on_dialogue_still_caught at 0x7a74d99400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 123>:
    # | 123            RESUME                   0
    # | 125            LOAD_CONST               1 ('dialogue_ratio')
    # |                STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
    # |                LOAD_ATTR                0 (check)
    # |                STORE_FAST               3 (@py_assert5)
    # |                LOAD_CONST               2 ('他没说话。')
    # |                STORE_FAST               4 (@py_assert8)
    # |                LOAD_GLOBAL              3 (make_chapter + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                LOAD_CONST               3 (('dialogue',))
    # |                CALL_KW                  1
    # |                STORE_FAST_LOAD_FAST    83 (@py_assert10, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert10)
    # |                CALL                     1
    # |                STORE_FAST               6 (@py_assert12)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         6 (@py_assert12)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   114 (@py_assert14, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert14)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       459 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('in',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py11)s\n{%(py11)s = %(py7)s(dialogue=%(py9)s)\n})\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (@py_assert0, @py_assert14)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py3')
    # |                LOAD_CONST               6 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               6 ('rules')
    # |        L3:     LOAD_CONST               7 ('py4')
    # |                LOAD_CONST               8 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               8 ('gate')
    # |        L6:     LOAD_CONST               9 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_CONST              11 ('make_chapter')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (make_chapter)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (make_chapter)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              11 ('make_chapter')
    # |        L9:     LOAD_CONST              12 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert12)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py15')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert14)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format16)
    # |                LOAD_CONST              16 ('assert %(py17)s')
    # |                LOAD_CONST              17 ('py17')
    # |                LOAD_FAST_BORROW         9 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format18)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert10)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert12, @py_assert14)
    # |                LOAD_CONST              18 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_apostrophe_in_prose_is_not_counted_as_speech at 0x7a74d99900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 127>:
    # | 127           RESUME                   0
    # | 129           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                1 (check + NULL|self)
    # |               LOAD_GLOBAL              3 (make_chapter + NULL)
    # |               CALL                     0
    # |               CALL                     1
    # |               LOAD_ATTR                4 (stats)
    # |               LOAD_CONST               1 ('dialogue_ratio')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (base)
    # | 130           LOAD_GLOBAL              3 (make_chapter + NULL)
    # |               LOAD_CONST               2 ("她在纸上写下 don't，又划掉了。")
    # |               LOAD_CONST               3 (('inject',))
    # |               CALL_KW                  1
    # |               STORE_FAST               3 (text)
    # | 131           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                1 (check + NULL|self)
    # |               LOAD_FAST_BORROW         3 (text)
    # |               CALL                     1
    # |               LOAD_ATTR                4 (stats)
    # |               LOAD_CONST               1 ('dialogue_ratio')
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |               LOAD_FAST_BORROW         2 (base)
    # |               BINARY_OP               10 (-)
    # |               STORE_FAST               5 (@py_assert4)
    # |               LOAD_GLOBAL              7 (abs + NULL)
    # |               LOAD_FAST_BORROW         5 (@py_assert4)
    # |               CALL                     1
    # |               STORE_FAST               6 (@py_assert5)
    # |               LOAD_CONST               4 (0.02)
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert8, @py_assert5)
    # |               LOAD_FAST_BORROW         7 (@py_assert8)
    # |               COMPARE_OP               2 (<)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert7, @py_assert7)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       307 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               10 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('<',))
    # |               LOAD_FAST_BORROW         8 (@py_assert7)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py6)s\n{%(py6)s = %(py0)s((%(py2)s - %(py3)s))\n} < %(py9)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert5, @py_assert8)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST               6 ('abs')
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
    # |               LOAD_GLOBAL              6 (abs)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              6 (abs)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               6 ('abs')
    # |       L3:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py3')
    # |               LOAD_CONST               9 ('base')
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
    # |               LOAD_FAST_BORROW         2 (base)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (base)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               9 ('base')
    # |       L6:     LOAD_CONST              10 ('py6')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert5)
    # |               CALL                     1
    # |               LOAD_CONST              11 ('py9')
    # |               LOAD_GLOBAL              8 (@pytest_ar)
    # |               LOAD_ATTR               18 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                5
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format10)
    # |               LOAD_CONST              12 ('assert %(py11)s')
    # |               LOAD_CONST              13 ('py11')
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
    # |       L7:     LOAD_CONST              14 (None)
    # |               COPY                     1
    # |               STORE_FAST               4 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               5 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert5)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert7, @py_assert8)
    # |               LOAD_CONST              14 (None)
    # |               RETURN_VALUE

    def test_ascii_quoted_chapter_is_not_read_as_zero_dialogue(self, gate):
        '“'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 116            RESUME                   0
        # | 117            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                CALL                     0
        # |                LOAD_ATTR                3 (replace + NULL|self)
        # |                LOAD_CONST               0 ('“')
        # |                LOAD_CONST               1 ('"')
        # |                CALL                     2
        # |                LOAD_ATTR                3 (replace + NULL|self)
        # |                LOAD_CONST               2 ('”')
        # |                LOAD_CONST               1 ('"')
        # |                CALL                     2
        # |                STORE_FAST               2 (text)
        # | 118            LOAD_FAST_BORROW         1 (gate)
        # |                LOAD_ATTR                5 (check + NULL|self)
        # |                LOAD_FAST_BORROW         2 (text)
        # |                CALL                     1
        # |                STORE_FAST               3 (report)
        # | 119            LOAD_FAST_BORROW         3 (report)
        # |                LOAD_ATTR                6 (stats)
        # |                LOAD_CONST               3 ('dialogue_ratio')
        # |                BINARY_OP               26 ([])
        # |                STORE_FAST               4 (@py_assert0)
        # |                LOAD_CONST               4 (0.1)
        # |                STORE_FAST_LOAD_FAST    84 (@py_assert3, @py_assert0)
        # |                LOAD_FAST_BORROW         5 (@py_assert3)
        # |                COMPARE_OP             132 (>)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                POP_JUMP_IF_TRUE       148 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('>',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py1)s > %(py4)s',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 69 (@py_assert0, @py_assert3)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py4')
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
        # |                LOAD_CONST               7 ('对话还在，只是引号写错了')
        # |                CALL                     1
        # |                LOAD_CONST               8 ('\n>assert %(py6)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               9 ('py6')
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
        # |        L1:     LOAD_CONST              10 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  101 (@py_assert2, @py_assert3)
        # | 120            LOAD_CONST               3 ('dialogue_ratio')
        # |                STORE_FAST               4 (@py_assert0)
        # |                LOAD_GLOBAL             21 (rules + NULL)
        # |                LOAD_FAST_BORROW         3 (report)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   148 (@py_assert5, @py_assert0)
        # |                LOAD_FAST_BORROW         9 (@py_assert5)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       312 (to L8)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              21 (('not in',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              22 (('%(py1)s not in %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert0, @py_assert5)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py3')
        # |                LOAD_CONST              12 ('rules')
        # |                LOAD_GLOBAL             22 (@py_builtins)
        # |                LOAD_ATTR               24 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L2)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               26 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             20 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L3)
        # |                NOT_TAKEN
        # |        L2:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             20 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L4)
        # |        L3:     LOAD_CONST              12 ('rules')
        # |        L4:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST              13 ('report')
        # |                LOAD_GLOBAL             22 (@py_builtins)
        # |                LOAD_ATTR               24 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L5)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               26 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (report)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L6)
        # |                NOT_TAKEN
        # |        L5:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (report)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L7)
        # |        L6:     LOAD_CONST              13 ('report')
        # |        L7:     LOAD_CONST               9 ('py6')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format7)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               14 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              14 ('别把格式问题报成缺对话')
        # |                CALL                     1
        # |                LOAD_CONST              15 ('\n>assert %(py8)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              16 ('py8')
        # |                LOAD_FAST_BORROW         8 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format9)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format9)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |        L8:     LOAD_CONST              10 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  105 (@py_assert2, @py_assert5)
        # | 121            LOAD_CONST              17 ('punctuation')
        # |                STORE_FAST               4 (@py_assert0)
        # |                LOAD_GLOBAL             21 (rules + NULL)
        # |                LOAD_FAST_BORROW         3 (report)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   148 (@py_assert5, @py_assert0)
        # |                LOAD_FAST_BORROW         9 (@py_assert5)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       312 (to L15)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               10 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              23 (('in',))
        # |                LOAD_FAST_BORROW         6 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              24 (('%(py1)s in %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 73 (@py_assert0, @py_assert5)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               5 ('py1')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST              11 ('py3')
        # |                LOAD_CONST              12 ('rules')
        # |                LOAD_GLOBAL             22 (@py_builtins)
        # |                LOAD_ATTR               24 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L9)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               26 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             20 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L10)
        # |                NOT_TAKEN
        # |        L9:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             20 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L11)
        # |       L10:     LOAD_CONST              12 ('rules')
        # |       L11:     LOAD_CONST               6 ('py4')
        # |                LOAD_CONST              13 ('report')
        # |                LOAD_GLOBAL             22 (@py_builtins)
        # |                LOAD_ATTR               24 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L12)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               26 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (report)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L13)
        # |                NOT_TAKEN
        # |       L12:     LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (report)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L14)
        # |       L13:     LOAD_CONST              13 ('report')
        # |       L14:     LOAD_CONST               9 ('py6')
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         9 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                4
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format7)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               14 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST              18 ('引号错了仍然要报')
        # |                CALL                     1
        # |                LOAD_CONST              15 ('\n>assert %(py8)s')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST              16 ('py8')
        # |                LOAD_FAST_BORROW         8 (@py_format7)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format9)
        # |                LOAD_GLOBAL             17 (AssertionError + NULL)
        # |                LOAD_GLOBAL              8 (@pytest_ar)
        # |                LOAD_ATTR               18 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format9)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L15:     LOAD_CONST              10 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  105 (@py_assert2, @py_assert5)
        # |                LOAD_CONST              10 (None)
        # |                RETURN_VALUE

    def test_a_chapter_really_short_on_dialogue_still_caught(self, gate):
        '别为了修上面那条把真正的缺对话放过去。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 123            RESUME                   0
        # | 125            LOAD_CONST               1 ('dialogue_ratio')
        # |                STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
        # |                LOAD_ATTR                0 (check)
        # |                STORE_FAST               3 (@py_assert5)
        # |                LOAD_CONST               2 ('他没说话。')
        # |                STORE_FAST               4 (@py_assert8)
        # |                LOAD_GLOBAL              3 (make_chapter + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                LOAD_CONST               3 (('dialogue',))
        # |                CALL_KW                  1
        # |                STORE_FAST_LOAD_FAST    83 (@py_assert10, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert10)
        # |                CALL                     1
        # |                STORE_FAST               6 (@py_assert12)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         6 (@py_assert12)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   114 (@py_assert14, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert14)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       459 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('in',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py11)s\n{%(py11)s = %(py7)s(dialogue=%(py9)s)\n})\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (@py_assert0, @py_assert14)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py3')
        # |                LOAD_CONST               6 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               6 ('rules')
        # |        L3:     LOAD_CONST               7 ('py4')
        # |                LOAD_CONST               8 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               8 ('gate')
        # |        L6:     LOAD_CONST               9 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_CONST              11 ('make_chapter')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (make_chapter)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (make_chapter)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              11 ('make_chapter')
        # |        L9:     LOAD_CONST              12 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert10)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert12)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py15')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert14)
        # |                CALL                     1
        # |                BUILD_MAP                9
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format16)
        # |                LOAD_CONST              16 ('assert %(py17)s')
        # |                LOAD_CONST              17 ('py17')
        # |                LOAD_FAST_BORROW         9 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format18)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format18)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert10)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert12, @py_assert14)
        # |                LOAD_CONST              18 (None)
        # |                RETURN_VALUE

    def test_apostrophe_in_prose_is_not_counted_as_speech(self, gate):
        '单个撇号不成对，不该被当成一句对话吞进占比里。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 127           RESUME                   0
        # | 129           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                1 (check + NULL|self)
        # |               LOAD_GLOBAL              3 (make_chapter + NULL)
        # |               CALL                     0
        # |               CALL                     1
        # |               LOAD_ATTR                4 (stats)
        # |               LOAD_CONST               1 ('dialogue_ratio')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (base)
        # | 130           LOAD_GLOBAL              3 (make_chapter + NULL)
        # |               LOAD_CONST               2 ("她在纸上写下 don't，又划掉了。")
        # |               LOAD_CONST               3 (('inject',))
        # |               CALL_KW                  1
        # |               STORE_FAST               3 (text)
        # | 131           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                1 (check + NULL|self)
        # |               LOAD_FAST_BORROW         3 (text)
        # |               CALL                     1
        # |               LOAD_ATTR                4 (stats)
        # |               LOAD_CONST               1 ('dialogue_ratio')
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |               LOAD_FAST_BORROW         2 (base)
        # |               BINARY_OP               10 (-)
        # |               STORE_FAST               5 (@py_assert4)
        # |               LOAD_GLOBAL              7 (abs + NULL)
        # |               LOAD_FAST_BORROW         5 (@py_assert4)
        # |               CALL                     1
        # |               STORE_FAST               6 (@py_assert5)
        # |               LOAD_CONST               4 (0.02)
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert8, @py_assert5)
        # |               LOAD_FAST_BORROW         7 (@py_assert8)
        # |               COMPARE_OP               2 (<)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert7, @py_assert7)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       307 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               10 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('<',))
        # |               LOAD_FAST_BORROW         8 (@py_assert7)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py6)s\n{%(py6)s = %(py0)s((%(py2)s - %(py3)s))\n} < %(py9)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert5, @py_assert8)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST               6 ('abs')
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
        # |               LOAD_GLOBAL              6 (abs)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              6 (abs)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               6 ('abs')
        # |       L3:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py3')
        # |               LOAD_CONST               9 ('base')
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
        # |               LOAD_FAST_BORROW         2 (base)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (base)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               9 ('base')
        # |       L6:     LOAD_CONST              10 ('py6')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert5)
        # |               CALL                     1
        # |               LOAD_CONST              11 ('py9')
        # |               LOAD_GLOBAL              8 (@pytest_ar)
        # |               LOAD_ATTR               18 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                5
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format10)
        # |               LOAD_CONST              12 ('assert %(py11)s')
        # |               LOAD_CONST              13 ('py11')
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
        # |       L7:     LOAD_CONST              14 (None)
        # |               COPY                     1
        # |               STORE_FAST               4 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               5 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert5)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert7, @py_assert8)
        # |               LOAD_CONST              14 (None)
        # |               RETURN_VALUE


class TestPlagiarism:
    'TestPlagiarism'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 134           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestPlagiarism')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         134
    # |               STORE_NAME               3 (__firstlineno__)
    # | 135           LOAD_CONST               1 (<code object test_copied_passage_is_hard_failure at 0x7a74d9c400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 135>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_copied_passage_is_hard_failure)
    # | 143           LOAD_CONST               2 (<code object test_original_text_not_flagged at 0x7a752c5800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 143>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_original_text_not_flagged)
    # | 149           LOAD_CONST               3 (<code object test_no_index_means_check_skipped at 0x7a74d9c800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 149>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_no_index_means_check_skipped)
    # |               LOAD_CONST               4 (())
    # |               STORE_NAME               7 (__static_attributes__)
    # |               LOAD_CONST               5 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_copied_passage_is_hard_failure at 0x7a74d9c400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 135>:
    # | 135           RESUME                   0
    # | 136           LOAD_CONST               0 ('她把伞往他那边偏了偏，雨水顺着自己的肩膀淌下来，一直凉到手肘。')
    # |               STORE_FAST               2 (source)
    # | 137           LOAD_GLOBAL              1 (NGramIndex + NULL)
    # |               LOAD_SMALL_INT          13
    # |               LOAD_CONST               1 (('n',))
    # |               CALL_KW                  1
    # |               STORE_FAST               3 (index)
    # | 138           LOAD_FAST_BORROW         3 (index)
    # |               LOAD_ATTR                3 (add_text + NULL|self)
    # |               LOAD_FAST_BORROW         2 (source)
    # |               CALL                     1
    # |               POP_TOP
    # | 139           LOAD_GLOBAL              5 (Gate + NULL)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (project_config, index)
    # |               LOAD_CONST               2 (('corpus_index',))
    # |               CALL_KW                  2
    # |               STORE_FAST               4 (gate)
    # | 140           LOAD_FAST_BORROW         4 (gate)
    # |               LOAD_ATTR                7 (check + NULL|self)
    # |               LOAD_GLOBAL              9 (make_chapter + NULL)
    # |               LOAD_FAST_BORROW         2 (source)
    # |               LOAD_CONST               3 (('narration',))
    # |               CALL_KW                  1
    # |               CALL                     1
    # |               STORE_FAST               5 (report)
    # | 141           LOAD_CONST               4 ('plagiarism')
    # |               STORE_FAST               6 (@py_assert0)
    # |               LOAD_GLOBAL             11 (rules + NULL)
    # |               LOAD_FAST_BORROW         5 (report)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert5, @py_assert0)
    # |               LOAD_FAST_BORROW         7 (@py_assert5)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       285 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               14 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('in',))
    # |               LOAD_FAST_BORROW         8 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py1)s in %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert5)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               5 ('py1')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               6 ('py3')
    # |               LOAD_CONST               7 ('rules')
    # |               LOAD_GLOBAL             18 (@py_builtins)
    # |               LOAD_ATTR               20 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               22 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             10 (rules)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             10 (rules)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               7 ('rules')
    # |       L3:     LOAD_CONST               8 ('py4')
    # |               LOAD_CONST               9 ('report')
    # |               LOAD_GLOBAL             18 (@py_builtins)
    # |               LOAD_ATTR               20 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               22 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (report)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (report)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               9 ('report')
    # |       L6:     LOAD_CONST              10 ('py6')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert5)
    # |               CALL                     1
    # |               BUILD_MAP                4
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format7)
    # |               LOAD_CONST              11 ('assert %(py8)s')
    # |               LOAD_CONST              12 ('py8')
    # |               LOAD_FAST_BORROW         9 (@py_format7)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format9)
    # |               LOAD_GLOBAL             25 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               26 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format9)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert5)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_original_text_not_flagged at 0x7a752c5800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 143>:
    # | 143            RESUME                   0
    # | 144            LOAD_GLOBAL              1 (NGramIndex + NULL)
    # |                LOAD_SMALL_INT          13
    # |                LOAD_CONST               1 (('n',))
    # |                CALL_KW                  1
    # |                STORE_FAST               2 (index)
    # | 145            LOAD_FAST_BORROW         2 (index)
    # |                LOAD_ATTR                3 (add_text + NULL|self)
    # |                LOAD_CONST              18 ('完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。')
    # |                CALL                     1
    # |                POP_TOP
    # | 146            LOAD_GLOBAL              5 (Gate + NULL)
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (project_config, index)
    # |                LOAD_CONST               2 (('corpus_index',))
    # |                CALL_KW                  2
    # |                STORE_FAST               3 (gate)
    # | 147            LOAD_CONST               3 ('plagiarism')
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert0, gate)
    # |                LOAD_ATTR                6 (check)
    # |                STORE_FAST               5 (@py_assert5)
    # |                LOAD_GLOBAL              9 (make_chapter + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST   101 (@py_assert8, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                CALL                     1
    # |                STORE_FAST               7 (@py_assert10)
    # |                LOAD_GLOBAL             11 (rules + NULL)
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   132 (@py_assert12, @py_assert0)
    # |                LOAD_FAST_BORROW         8 (@py_assert12)
    # |                CONTAINS_OP              1 (not in)
    # |                STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       437 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               14 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('not in',))
    # |                LOAD_FAST_BORROW         9 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py1)s not in %(py13)s\n{%(py13)s = %(py3)s(%(py11)s\n{%(py11)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py9)s\n{%(py9)s = %(py7)s()\n})\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (@py_assert0, @py_assert12)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py1')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py3')
    # |                LOAD_CONST               6 ('rules')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL             10 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               6 ('rules')
    # |        L3:     LOAD_CONST               7 ('py4')
    # |                LOAD_CONST               8 ('gate')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               8 ('gate')
    # |        L6:     LOAD_CONST               9 ('py6')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_CONST              11 ('make_chapter')
    # |                LOAD_GLOBAL             18 (@py_builtins)
    # |                LOAD_ATTR               20 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               22 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (make_chapter)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              8 (make_chapter)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              11 ('make_chapter')
    # |        L9:     LOAD_CONST              12 ('py9')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py11')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               16 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_assert12)
    # |                CALL                     1
    # |                BUILD_MAP                8
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format14)
    # |                LOAD_CONST              15 ('assert %(py15)s')
    # |                LOAD_CONST              16 ('py15')
    # |                LOAD_FAST_BORROW        10 (@py_format14)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              11 (@py_format16)
    # |                LOAD_GLOBAL             25 (AssertionError + NULL)
    # |                LOAD_GLOBAL             12 (@pytest_ar)
    # |                LOAD_ATTR               26 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        11 (@py_format16)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              17 (None)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               9 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               6 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  120 (@py_assert10, @py_assert12)
    # |                LOAD_CONST              17 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_no_index_means_check_skipped at 0x7a74d9c800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 149>:
    # | 149           RESUME                   0
    # | 150           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                0 (check)
    # |               STORE_FAST               2 (@py_assert1)
    # |               LOAD_GLOBAL              3 (make_chapter + NULL)
    # |               CALL                     0
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert1)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert4)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert6, @py_assert6)
    # |               LOAD_ATTR                4 (passed)
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert8, @py_assert8)
    # |               TO_BOOL
    # |               EXTENDED_ARG             1
    # |               POP_JUMP_IF_TRUE       293 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_CONST               1 ('assert %(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.check\n}(%(py5)s\n{%(py5)s = %(py3)s()\n})\n}.passed\n}')
    # |               LOAD_CONST               2 ('py0')
    # |               LOAD_CONST               3 ('gate')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (gate)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         1 (gate)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               3 ('gate')
    # |       L3:     LOAD_CONST               4 ('py2')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               5 ('py3')
    # |               LOAD_CONST               6 ('make_chapter')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              2 (make_chapter)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              2 (make_chapter)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               6 ('make_chapter')
    # |       L6:     LOAD_CONST               7 ('py5')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert4)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py7')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert6)
    # |               CALL                     1
    # |               LOAD_CONST               9 ('py9')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert8)
    # |               CALL                     1
    # |               BUILD_MAP                6
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format10)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format10)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              10 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert4)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert6, @py_assert8)
    # |               LOAD_CONST              10 (None)
    # |               RETURN_VALUE

    def test_copied_passage_is_hard_failure(self, project_config):
        '她把伞往他那边偏了偏，雨水顺着自己的肩膀淌下来，一直凉到手肘。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 135           RESUME                   0
        # | 136           LOAD_CONST               0 ('她把伞往他那边偏了偏，雨水顺着自己的肩膀淌下来，一直凉到手肘。')
        # |               STORE_FAST               2 (source)
        # | 137           LOAD_GLOBAL              1 (NGramIndex + NULL)
        # |               LOAD_SMALL_INT          13
        # |               LOAD_CONST               1 (('n',))
        # |               CALL_KW                  1
        # |               STORE_FAST               3 (index)
        # | 138           LOAD_FAST_BORROW         3 (index)
        # |               LOAD_ATTR                3 (add_text + NULL|self)
        # |               LOAD_FAST_BORROW         2 (source)
        # |               CALL                     1
        # |               POP_TOP
        # | 139           LOAD_GLOBAL              5 (Gate + NULL)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (project_config, index)
        # |               LOAD_CONST               2 (('corpus_index',))
        # |               CALL_KW                  2
        # |               STORE_FAST               4 (gate)
        # | 140           LOAD_FAST_BORROW         4 (gate)
        # |               LOAD_ATTR                7 (check + NULL|self)
        # |               LOAD_GLOBAL              9 (make_chapter + NULL)
        # |               LOAD_FAST_BORROW         2 (source)
        # |               LOAD_CONST               3 (('narration',))
        # |               CALL_KW                  1
        # |               CALL                     1
        # |               STORE_FAST               5 (report)
        # | 141           LOAD_CONST               4 ('plagiarism')
        # |               STORE_FAST               6 (@py_assert0)
        # |               LOAD_GLOBAL             11 (rules + NULL)
        # |               LOAD_FAST_BORROW         5 (report)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert5, @py_assert0)
        # |               LOAD_FAST_BORROW         7 (@py_assert5)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       285 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               14 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('in',))
        # |               LOAD_FAST_BORROW         8 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              15 (('%(py1)s in %(py6)s\n{%(py6)s = %(py3)s(%(py4)s)\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert5)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               5 ('py1')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               6 ('py3')
        # |               LOAD_CONST               7 ('rules')
        # |               LOAD_GLOBAL             18 (@py_builtins)
        # |               LOAD_ATTR               20 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               22 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             10 (rules)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             10 (rules)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               7 ('rules')
        # |       L3:     LOAD_CONST               8 ('py4')
        # |               LOAD_CONST               9 ('report')
        # |               LOAD_GLOBAL             18 (@py_builtins)
        # |               LOAD_ATTR               20 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               22 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (report)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (report)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               9 ('report')
        # |       L6:     LOAD_CONST              10 ('py6')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert5)
        # |               CALL                     1
        # |               BUILD_MAP                4
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format7)
        # |               LOAD_CONST              11 ('assert %(py8)s')
        # |               LOAD_CONST              12 ('py8')
        # |               LOAD_FAST_BORROW         9 (@py_format7)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format9)
        # |               LOAD_GLOBAL             25 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               26 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format9)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert5)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE

    def test_original_text_not_flagged(self, project_config):
        'plagiarism'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 143            RESUME                   0
        # | 144            LOAD_GLOBAL              1 (NGramIndex + NULL)
        # |                LOAD_SMALL_INT          13
        # |                LOAD_CONST               1 (('n',))
        # |                CALL_KW                  1
        # |                STORE_FAST               2 (index)
        # | 145            LOAD_FAST_BORROW         2 (index)
        # |                LOAD_ATTR                3 (add_text + NULL|self)
        # |                LOAD_CONST              18 ('完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。完全无关的另一本书的段落，讲的是海边的黄昏与渔船。')
        # |                CALL                     1
        # |                POP_TOP
        # | 146            LOAD_GLOBAL              5 (Gate + NULL)
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (project_config, index)
        # |                LOAD_CONST               2 (('corpus_index',))
        # |                CALL_KW                  2
        # |                STORE_FAST               3 (gate)
        # | 147            LOAD_CONST               3 ('plagiarism')
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert0, gate)
        # |                LOAD_ATTR                6 (check)
        # |                STORE_FAST               5 (@py_assert5)
        # |                LOAD_GLOBAL              9 (make_chapter + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST   101 (@py_assert8, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                CALL                     1
        # |                STORE_FAST               7 (@py_assert10)
        # |                LOAD_GLOBAL             11 (rules + NULL)
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   132 (@py_assert12, @py_assert0)
        # |                LOAD_FAST_BORROW         8 (@py_assert12)
        # |                CONTAINS_OP              1 (not in)
        # |                STORE_FAST_LOAD_FAST   153 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       437 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               14 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('not in',))
        # |                LOAD_FAST_BORROW         9 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py1)s not in %(py13)s\n{%(py13)s = %(py3)s(%(py11)s\n{%(py11)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py9)s\n{%(py9)s = %(py7)s()\n})\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 72 (@py_assert0, @py_assert12)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py1')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py3')
        # |                LOAD_CONST               6 ('rules')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL             10 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               6 ('rules')
        # |        L3:     LOAD_CONST               7 ('py4')
        # |                LOAD_CONST               8 ('gate')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               8 ('gate')
        # |        L6:     LOAD_CONST               9 ('py6')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_CONST              11 ('make_chapter')
        # |                LOAD_GLOBAL             18 (@py_builtins)
        # |                LOAD_ATTR               20 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               22 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (make_chapter)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              8 (make_chapter)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              11 ('make_chapter')
        # |        L9:     LOAD_CONST              12 ('py9')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py11')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert10)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               16 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_assert12)
        # |                CALL                     1
        # |                BUILD_MAP                8
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format14)
        # |                LOAD_CONST              15 ('assert %(py15)s')
        # |                LOAD_CONST              16 ('py15')
        # |                LOAD_FAST_BORROW        10 (@py_format14)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              11 (@py_format16)
        # |                LOAD_GLOBAL             25 (AssertionError + NULL)
        # |                LOAD_GLOBAL             12 (@pytest_ar)
        # |                LOAD_ATTR               26 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        11 (@py_format16)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              17 (None)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               9 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               6 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  120 (@py_assert10, @py_assert12)
        # |                LOAD_CONST              17 (None)
        # |                RETURN_VALUE

    def test_no_index_means_check_skipped(self, gate):
        'assert %(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.check\n}(%(py5)s\n{%(py5)s = %(py3)s()\n})\n}.passed\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 149           RESUME                   0
        # | 150           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                0 (check)
        # |               STORE_FAST               2 (@py_assert1)
        # |               LOAD_GLOBAL              3 (make_chapter + NULL)
        # |               CALL                     0
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert4, @py_assert1)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert4)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert6, @py_assert6)
        # |               LOAD_ATTR                4 (passed)
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert8, @py_assert8)
        # |               TO_BOOL
        # |               EXTENDED_ARG             1
        # |               POP_JUMP_IF_TRUE       293 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_CONST               1 ('assert %(py9)s\n{%(py9)s = %(py7)s\n{%(py7)s = %(py2)s\n{%(py2)s = %(py0)s.check\n}(%(py5)s\n{%(py5)s = %(py3)s()\n})\n}.passed\n}')
        # |               LOAD_CONST               2 ('py0')
        # |               LOAD_CONST               3 ('gate')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (gate)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         1 (gate)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               3 ('gate')
        # |       L3:     LOAD_CONST               4 ('py2')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               5 ('py3')
        # |               LOAD_CONST               6 ('make_chapter')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              2 (make_chapter)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              2 (make_chapter)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               6 ('make_chapter')
        # |       L6:     LOAD_CONST               7 ('py5')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert4)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py7')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert6)
        # |               CALL                     1
        # |               LOAD_CONST               9 ('py9')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert8)
        # |               CALL                     1
        # |               BUILD_MAP                6
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format10)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format10)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              10 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert4)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert6, @py_assert8)
        # |               LOAD_CONST              10 (None)
        # |               RETURN_VALUE


class TestSelfRepetition:
    'TestSelfRepetition'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 153           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestSelfRepetition')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         153
    # |               STORE_NAME               3 (__firstlineno__)
    # | 154           LOAD_CONST               1 (<code object test_reusing_own_earlier_phrasing_warns_not_fails at 0x7a74d9a300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 154>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_reusing_own_earlier_phrasing_warns_not_fails)
    # |               LOAD_CONST               2 (())
    # |               STORE_NAME               5 (__static_attributes__)
    # |               LOAD_CONST               3 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_reusing_own_earlier_phrasing_warns_not_fails at 0x7a74d9a300, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 154>:
    # | 154           RESUME                   0
    # | 156           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('SHORT_PHRASE_FOR_REPEAT',))
    # |               IMPORT_NAME              0 (conftest)
    # |               IMPORT_FROM              1 (SHORT_PHRASE_FOR_REPEAT)
    # |               STORE_FAST               2 (SHORT_PHRASE_FOR_REPEAT)
    # |               POP_TOP
    # | 158           LOAD_GLOBAL              5 (NGramIndex + NULL)
    # |               LOAD_SMALL_INT          13
    # |               LOAD_CONST               2 (('n',))
    # |               CALL_KW                  1
    # |               STORE_FAST               3 (prior)
    # | 159           LOAD_FAST_BORROW         3 (prior)
    # |               LOAD_ATTR                7 (add_text + NULL|self)
    # |               LOAD_FAST_BORROW         2 (SHORT_PHRASE_FOR_REPEAT)
    # |               CALL                     1
    # |               POP_TOP
    # | 160           LOAD_GLOBAL              9 (Gate + NULL)
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (project_config, prior)
    # |               LOAD_CONST               3 (('self_index',))
    # |               CALL_KW                  2
    # |               STORE_FAST               4 (gate)
    # | 161           LOAD_FAST_BORROW         4 (gate)
    # |               LOAD_ATTR               11 (check + NULL|self)
    # |               LOAD_GLOBAL             13 (make_chapter + NULL)
    # |               CALL                     0
    # |               CALL                     1
    # |               STORE_FAST               5 (report)
    # | 162           LOAD_FAST_BORROW         5 (report)
    # |               LOAD_ATTR               14 (passed)
    # |               STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       141 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               4 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST               6 ('report')
    # |               LOAD_GLOBAL             16 (@py_builtins)
    # |               LOAD_ATTR               18 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               22 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (report)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (report)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               6 ('report')
    # |       L3:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format3)
    # |               LOAD_GLOBAL             27 (AssertionError + NULL)
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               28 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format3)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               STORE_FAST               6 (@py_assert1)
    # | 163           LOAD_CONST               9 (<code object <genexpr> at 0x103d13dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 163>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         5 (report)
    # |               LOAD_ATTR               30 (warnings)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               6 (@py_assert1)
    # |               LOAD_GLOBAL             33 (any + NULL)
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_CONST              10 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST              11 ('any')
    # |               LOAD_GLOBAL             16 (@py_builtins)
    # |               LOAD_ATTR               18 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L5)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               22 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             32 (any)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             32 (any)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST              11 ('any')
    # |       L7:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py4')
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               24 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         8 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format5)
    # |               LOAD_GLOBAL             27 (AssertionError + NULL)
    # |               LOAD_GLOBAL             20 (@pytest_ar)
    # |               LOAD_ATTR               28 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         9 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  104 (@py_assert1, @py_assert3)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x103d13dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 163>:
    # |  163           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                19 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (f, f)
    # |                LOAD_ATTR                0 (rule)
    # |                LOAD_CONST               0 ('self_repetition')
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

    def test_reusing_own_earlier_phrasing_warns_not_fails(self, project_config):
        '自我重复是警告不是错误 —— 回响式的刻意重复是合法手法。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 154           RESUME                   0
        # | 156           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('SHORT_PHRASE_FOR_REPEAT',))
        # |               IMPORT_NAME              0 (conftest)
        # |               IMPORT_FROM              1 (SHORT_PHRASE_FOR_REPEAT)
        # |               STORE_FAST               2 (SHORT_PHRASE_FOR_REPEAT)
        # |               POP_TOP
        # | 158           LOAD_GLOBAL              5 (NGramIndex + NULL)
        # |               LOAD_SMALL_INT          13
        # |               LOAD_CONST               2 (('n',))
        # |               CALL_KW                  1
        # |               STORE_FAST               3 (prior)
        # | 159           LOAD_FAST_BORROW         3 (prior)
        # |               LOAD_ATTR                7 (add_text + NULL|self)
        # |               LOAD_FAST_BORROW         2 (SHORT_PHRASE_FOR_REPEAT)
        # |               CALL                     1
        # |               POP_TOP
        # | 160           LOAD_GLOBAL              9 (Gate + NULL)
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 19 (project_config, prior)
        # |               LOAD_CONST               3 (('self_index',))
        # |               CALL_KW                  2
        # |               STORE_FAST               4 (gate)
        # | 161           LOAD_FAST_BORROW         4 (gate)
        # |               LOAD_ATTR               11 (check + NULL|self)
        # |               LOAD_GLOBAL             13 (make_chapter + NULL)
        # |               CALL                     0
        # |               CALL                     1
        # |               STORE_FAST               5 (report)
        # | 162           LOAD_FAST_BORROW         5 (report)
        # |               LOAD_ATTR               14 (passed)
        # |               STORE_FAST_LOAD_FAST   102 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       141 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               4 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST               6 ('report')
        # |               LOAD_GLOBAL             16 (@py_builtins)
        # |               LOAD_ATTR               18 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               22 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (report)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (report)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               6 ('report')
        # |       L3:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format3)
        # |               LOAD_GLOBAL             27 (AssertionError + NULL)
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               28 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format3)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               STORE_FAST               6 (@py_assert1)
        # | 163           LOAD_CONST               9 (<code object <genexpr> at 0x103d13dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 163>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         5 (report)
        # |               LOAD_ATTR               30 (warnings)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               6 (@py_assert1)
        # |               LOAD_GLOBAL             33 (any + NULL)
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_CONST              10 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST              11 ('any')
        # |               LOAD_GLOBAL             16 (@py_builtins)
        # |               LOAD_ATTR               18 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L5)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               22 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             32 (any)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             32 (any)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST              11 ('any')
        # |       L7:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py4')
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               24 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         8 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format5)
        # |               LOAD_GLOBAL             27 (AssertionError + NULL)
        # |               LOAD_GLOBAL             20 (@pytest_ar)
        # |               LOAD_ATTR               28 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         9 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  104 (@py_assert1, @py_assert3)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x103d13dd0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 163>:
        # |  163           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                19 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (f, f)
        # |                LOAD_ATTR                0 (rule)
        # |                LOAD_CONST               0 ('self_repetition')
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


class TestEmotionalDebt:
    'TestEmotionalDebt'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 166           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestEmotionalDebt')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         166
    # |               STORE_NAME               3 (__firstlineno__)
    # | 167           LOAD_CONST               1 (<code object test_overdue_debt_warns at 0x7a74d9a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 167>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               4 (test_overdue_debt_warns)
    # | 181           LOAD_CONST               2 (<code object test_paid_debt_silent at 0x7a74d9ad00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 181>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_paid_debt_silent)
    # |               LOAD_CONST               3 (())
    # |               STORE_NAME               6 (__static_attributes__)
    # |               LOAD_CONST               4 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_overdue_debt_warns at 0x7a74d9a800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 167>:
    # | 167           RESUME                   0
    # | 168           LOAD_GLOBAL              1 (StoryState + NULL)
    # | 169           LOAD_SMALL_INT          60
    # | 171           LOAD_GLOBAL              3 (EmotionalDebt + NULL)
    # | 172           LOAD_CONST               1 ('d1')
    # |               LOAD_CONST               2 ('误会')
    # |               LOAD_CONST               3 ('她以为那通电话是打给别人的')
    # | 173           LOAD_SMALL_INT          12
    # |               LOAD_SMALL_INT          40
    # | 171           LOAD_CONST               4 (('id', 'kind', 'desc', 'planted_ch', 'due_by_ch'))
    # |               CALL_KW                  5
    # | 170           BUILD_LIST               1
    # | 168           LOAD_CONST               5 (('current_chapter', 'debts'))
    # |               CALL_KW                  2
    # |               STORE_FAST               2 (state)
    # | 177           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                5 (check + NULL|self)
    # |               LOAD_GLOBAL              7 (make_chapter + NULL)
    # |               CALL                     0
    # |               LOAD_FAST_BORROW         2 (state)
    # |               LOAD_CONST               6 (('state',))
    # |               CALL_KW                  2
    # |               STORE_FAST               3 (report)
    # | 178           LOAD_CONST               7 (<code object <genexpr> at 0x103d68030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 178>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         3 (report)
    # |               LOAD_ATTR                8 (warnings)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               4 (@py_assert1)
    # |               LOAD_GLOBAL             11 (any + NULL)
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               8 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               9 ('py0')
    # |               LOAD_CONST              10 ('any')
    # |               LOAD_GLOBAL             12 (@py_builtins)
    # |               LOAD_ATTR               14 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        33 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               18 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             10 (any)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             10 (any)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST              10 ('any')
    # |       L3:     LOAD_CONST              11 ('py2')
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py4')
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format5)
    # |               LOAD_GLOBAL             23 (AssertionError + NULL)
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               24 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
    # | 179           LOAD_FAST_BORROW         3 (report)
    # |               LOAD_ATTR               26 (passed)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       141 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_CONST              14 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |               LOAD_CONST               9 ('py0')
    # |               LOAD_CONST              15 ('report')
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
    # |               LOAD_FAST_BORROW         3 (report)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (report)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST              15 ('report')
    # |       L7:     LOAD_CONST              11 ('py2')
    # |               LOAD_GLOBAL             16 (@pytest_ar)
    # |               LOAD_ATTR               20 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
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
    # |       L8:     LOAD_CONST              13 (None)
    # |               STORE_FAST               4 (@py_assert1)
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x103d68030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 178>:
    # |  178           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                19 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (f, f)
    # |                LOAD_ATTR                0 (rule)
    # |                LOAD_CONST               0 ('emotional_debt')
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
    # | Disassembly of <code object test_paid_debt_silent at 0x7a74d9ad00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 181>:
    # | 181            RESUME                   0
    # | 182            LOAD_GLOBAL              1 (StoryState + NULL)
    # | 183            LOAD_SMALL_INT          60
    # | 185            LOAD_GLOBAL              3 (EmotionalDebt + NULL)
    # |                LOAD_CONST               1 ('d1')
    # |                LOAD_CONST               2 ('误会')
    # |                LOAD_CONST               3 ('x')
    # | 186            LOAD_SMALL_INT          12
    # |                LOAD_SMALL_INT          40
    # |                LOAD_CONST               4 ('paid')
    # | 185            LOAD_CONST               5 (('id', 'kind', 'desc', 'planted_ch', 'due_by_ch', 'status'))
    # |                CALL_KW                  6
    # | 184            BUILD_LIST               1
    # | 182            LOAD_CONST               6 (('current_chapter', 'debts'))
    # |                CALL_KW                  2
    # |                STORE_FAST               2 (state)
    # | 189            LOAD_FAST_BORROW         1 (gate)
    # |                LOAD_ATTR                4 (check)
    # |                STORE_FAST               3 (@py_assert1)
    # |                LOAD_GLOBAL              7 (make_chapter + NULL)
    # |                CALL                     0
    # |                STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (@py_assert4, state)
    # |                LOAD_CONST               7 (('state',))
    # |                CALL_KW                  2
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert7, @py_assert7)
    # |                LOAD_ATTR                8 (warnings)
    # |                STORE_FAST_LOAD_FAST   102 (@py_assert9, @py_assert9)
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                STORE_FAST_LOAD_FAST   119 (@py_assert11, @py_assert11)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       371 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_CONST               8 ('assert not %(py10)s\n{%(py10)s = %(py8)s\n{%(py8)s = %(py2)s\n{%(py2)s = %(py0)s.check\n}(%(py5)s\n{%(py5)s = %(py3)s()\n}, state=%(py6)s)\n}.warnings\n}')
    # |                LOAD_CONST               9 ('py0')
    # |                LOAD_CONST              10 ('gate')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST              10 ('gate')
    # |        L3:     LOAD_CONST              11 ('py2')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST              12 ('py3')
    # |                LOAD_CONST              13 ('make_chapter')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (make_chapter)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              6 (make_chapter)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST              13 ('make_chapter')
    # |        L6:     LOAD_CONST              14 ('py5')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert4)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py6')
    # |                LOAD_CONST              16 ('state')
    # |                LOAD_GLOBAL             10 (@py_builtins)
    # |                LOAD_ATTR               12 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (state)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (state)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              16 ('state')
    # |        L9:     LOAD_CONST              17 ('py8')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert7)
    # |                CALL                     1
    # |                LOAD_CONST              18 ('py10')
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               18 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert9)
    # |                CALL                     1
    # |                BUILD_MAP                7
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               8 (@py_format12)
    # |                LOAD_GLOBAL             21 (AssertionError + NULL)
    # |                LOAD_GLOBAL             14 (@pytest_ar)
    # |                LOAD_ATTR               22 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         8 (@py_format12)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              19 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert4)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert7)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert9, @py_assert11)
    # |                LOAD_CONST              19 (None)
    # |                RETURN_VALUE

    def test_overdue_debt_warns(self, gate):
        'd1'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 167           RESUME                   0
        # | 168           LOAD_GLOBAL              1 (StoryState + NULL)
        # | 169           LOAD_SMALL_INT          60
        # | 171           LOAD_GLOBAL              3 (EmotionalDebt + NULL)
        # | 172           LOAD_CONST               1 ('d1')
        # |               LOAD_CONST               2 ('误会')
        # |               LOAD_CONST               3 ('她以为那通电话是打给别人的')
        # | 173           LOAD_SMALL_INT          12
        # |               LOAD_SMALL_INT          40
        # | 171           LOAD_CONST               4 (('id', 'kind', 'desc', 'planted_ch', 'due_by_ch'))
        # |               CALL_KW                  5
        # | 170           BUILD_LIST               1
        # | 168           LOAD_CONST               5 (('current_chapter', 'debts'))
        # |               CALL_KW                  2
        # |               STORE_FAST               2 (state)
        # | 177           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                5 (check + NULL|self)
        # |               LOAD_GLOBAL              7 (make_chapter + NULL)
        # |               CALL                     0
        # |               LOAD_FAST_BORROW         2 (state)
        # |               LOAD_CONST               6 (('state',))
        # |               CALL_KW                  2
        # |               STORE_FAST               3 (report)
        # | 178           LOAD_CONST               7 (<code object <genexpr> at 0x103d68030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 178>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         3 (report)
        # |               LOAD_ATTR                8 (warnings)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               4 (@py_assert1)
        # |               LOAD_GLOBAL             11 (any + NULL)
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               8 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               9 ('py0')
        # |               LOAD_CONST              10 ('any')
        # |               LOAD_GLOBAL             12 (@py_builtins)
        # |               LOAD_ATTR               14 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        33 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               18 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             10 (any)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             10 (any)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST              10 ('any')
        # |       L3:     LOAD_CONST              11 ('py2')
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py4')
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format5)
        # |               LOAD_GLOBAL             23 (AssertionError + NULL)
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               24 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
        # | 179           LOAD_FAST_BORROW         3 (report)
        # |               LOAD_ATTR               26 (passed)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       141 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_CONST              14 ('assert %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |               LOAD_CONST               9 ('py0')
        # |               LOAD_CONST              15 ('report')
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
        # |               LOAD_FAST_BORROW         3 (report)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (report)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST              15 ('report')
        # |       L7:     LOAD_CONST              11 ('py2')
        # |               LOAD_GLOBAL             16 (@pytest_ar)
        # |               LOAD_ATTR               20 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
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
        # |       L8:     LOAD_CONST              13 (None)
        # |               STORE_FAST               4 (@py_assert1)
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x103d68030, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 178>:
        # |  178           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                19 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (f, f)
        # |                LOAD_ATTR                0 (rule)
        # |                LOAD_CONST               0 ('emotional_debt')
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

    def test_paid_debt_silent(self, gate):
        'd1'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 181            RESUME                   0
        # | 182            LOAD_GLOBAL              1 (StoryState + NULL)
        # | 183            LOAD_SMALL_INT          60
        # | 185            LOAD_GLOBAL              3 (EmotionalDebt + NULL)
        # |                LOAD_CONST               1 ('d1')
        # |                LOAD_CONST               2 ('误会')
        # |                LOAD_CONST               3 ('x')
        # | 186            LOAD_SMALL_INT          12
        # |                LOAD_SMALL_INT          40
        # |                LOAD_CONST               4 ('paid')
        # | 185            LOAD_CONST               5 (('id', 'kind', 'desc', 'planted_ch', 'due_by_ch', 'status'))
        # |                CALL_KW                  6
        # | 184            BUILD_LIST               1
        # | 182            LOAD_CONST               6 (('current_chapter', 'debts'))
        # |                CALL_KW                  2
        # |                STORE_FAST               2 (state)
        # | 189            LOAD_FAST_BORROW         1 (gate)
        # |                LOAD_ATTR                4 (check)
        # |                STORE_FAST               3 (@py_assert1)
        # |                LOAD_GLOBAL              7 (make_chapter + NULL)
        # |                CALL                     0
        # |                STORE_FAST_LOAD_FAST    67 (@py_assert4, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 66 (@py_assert4, state)
        # |                LOAD_CONST               7 (('state',))
        # |                CALL_KW                  2
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert7, @py_assert7)
        # |                LOAD_ATTR                8 (warnings)
        # |                STORE_FAST_LOAD_FAST   102 (@py_assert9, @py_assert9)
        # |                TO_BOOL
        # |                UNARY_NOT
        # |                STORE_FAST_LOAD_FAST   119 (@py_assert11, @py_assert11)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       371 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_CONST               8 ('assert not %(py10)s\n{%(py10)s = %(py8)s\n{%(py8)s = %(py2)s\n{%(py2)s = %(py0)s.check\n}(%(py5)s\n{%(py5)s = %(py3)s()\n}, state=%(py6)s)\n}.warnings\n}')
        # |                LOAD_CONST               9 ('py0')
        # |                LOAD_CONST              10 ('gate')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST              10 ('gate')
        # |        L3:     LOAD_CONST              11 ('py2')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST              12 ('py3')
        # |                LOAD_CONST              13 ('make_chapter')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (make_chapter)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              6 (make_chapter)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST              13 ('make_chapter')
        # |        L6:     LOAD_CONST              14 ('py5')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert4)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py6')
        # |                LOAD_CONST              16 ('state')
        # |                LOAD_GLOBAL             10 (@py_builtins)
        # |                LOAD_ATTR               12 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (state)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (state)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              16 ('state')
        # |        L9:     LOAD_CONST              17 ('py8')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert7)
        # |                CALL                     1
        # |                LOAD_CONST              18 ('py10')
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               18 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert9)
        # |                CALL                     1
        # |                BUILD_MAP                7
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               8 (@py_format12)
        # |                LOAD_GLOBAL             21 (AssertionError + NULL)
        # |                LOAD_GLOBAL             14 (@pytest_ar)
        # |                LOAD_ATTR               22 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         8 (@py_format12)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              19 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert4)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert7)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert9, @py_assert11)
        # |                LOAD_CONST              19 (None)
        # |                RETURN_VALUE


class TestDialogueSpeakerDetection:
    'TestDialogueSpeakerDetection'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 192           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestDialogueSpeakerDetection')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         192
    # |               STORE_NAME               3 (__firstlineno__)
    # | 193           LOAD_CONST               1 ('只数段内引号对数会把标准写法判成错。实测第 13 章被误报 4 处。')
    # |               STORE_NAME               4 (__doc__)
    # | 195           LOAD_CONST               2 (<code object _check at 0x103d1a760, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 195>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (_check)
    # | 199           LOAD_NAME                6 (pytest)
    # |               LOAD_ATTR               14 (mark)
    # |               LOAD_ATTR               17 (parametrize + NULL|self)
    # | 200           LOAD_CONST               3 ('para')
    # | 201           BUILD_LIST               0
    # |               LOAD_CONST              10 (('“社刊旧刊。”他说，“九本。”', '“中午。”他说，“不到六点。”', '“排版通知你看了吧——”箱子往上顶了顶，“你不是两点就问过吗。”'))
    # |               LIST_EXTEND              1
    # | 199           CALL                     2
    # | 205           LOAD_CONST               4 (<code object test_same_speaker_with_inline_attribution_is_valid at 0x7a74d9d400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 199>)
    # |               MAKE_FUNCTION
    # | 199           CALL                     0
    # | 205           STORE_NAME               9 (test_same_speaker_with_inline_attribution_is_valid)
    # | 209           LOAD_NAME                6 (pytest)
    # |               LOAD_ATTR               14 (mark)
    # |               LOAD_ATTR               17 (parametrize + NULL|self)
    # | 210           LOAD_CONST               3 ('para')
    # | 211           LOAD_CONST               5 ('“九本。”他摇头。“不到六点。”她说。')
    # | 212           LOAD_CONST               6 ('“你会湿透的。”她把伞递过去。“我不冷。”')
    # | 211           BUILD_LIST               2
    # | 209           CALL                     2
    # | 214           LOAD_CONST               7 (<code object test_two_speakers_still_caught at 0x7a74d9d800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 209>)
    # |               MAKE_FUNCTION
    # | 209           CALL                     0
    # | 214           STORE_NAME              10 (test_two_speakers_still_caught)
    # |               LOAD_CONST               8 (())
    # |               STORE_NAME              11 (__static_attributes__)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object _check at 0x103d1a760, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 195>:
    # | 195           RESUME                   0
    # | 196           LOAD_GLOBAL              1 (make_chapter + NULL)
    # |               LOAD_FAST_BORROW         2 (para)
    # |               LOAD_CONST               0 (('inject',))
    # |               CALL_KW                  1
    # |               STORE_FAST               3 (text)
    # | 197           LOAD_CONST               1 ('dialogue')
    # |               LOAD_GLOBAL              3 (rules + NULL)
    # |               LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                5 (check + NULL|self)
    # |               LOAD_FAST_BORROW         3 (text)
    # |               CALL                     1
    # |               CALL                     1
    # |               CONTAINS_OP              0 (in)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_same_speaker_with_inline_attribution_is_valid at 0x7a74d9d400, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 199>:
    # | 199            RESUME                   0
    # | 207            LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                0 (_check)
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (gate, para)
    # |                CALL                     2
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                UNARY_NOT
    # |                STORE_FAST_LOAD_FAST    85 (@py_assert7, @py_assert7)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       349 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST               1 ('误判了标准写法：')
    # |                LOAD_FAST_BORROW         2 (para)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                LOAD_CONST               2 ('\n>assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s._check\n}(%(py3)s, %(py4)s)\n}')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('self')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (self)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (self)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('self')
    # |        L3:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py3')
    # |                LOAD_CONST               7 ('gate')
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
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py4')
    # |                LOAD_CONST               9 ('para')
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
    # |                LOAD_FAST_BORROW         2 (para)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (para)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               9 ('para')
    # |        L9:     LOAD_CONST              10 ('py6')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                5
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
    # |       L10:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert1)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   69 (@py_assert5, @py_assert7)
    # |                LOAD_CONST              11 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_two_speakers_still_caught at 0x7a74d9d800, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 209>:
    # | 209            RESUME                   0
    # | 216            LOAD_FAST_BORROW         0 (self)
    # |                LOAD_ATTR                0 (_check)
    # |                STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (gate, para)
    # |                CALL                     2
    # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       349 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR                4 (_format_assertmsg)
    # |                PUSH_NULL
    # |                LOAD_CONST               1 ('漏判了两个说话人：')
    # |                LOAD_FAST_BORROW         2 (para)
    # |                FORMAT_SIMPLE
    # |                BUILD_STRING             2
    # |                CALL                     1
    # |                LOAD_CONST               2 ('\n>assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s._check\n}(%(py3)s, %(py4)s)\n}')
    # |                BINARY_OP                0 (+)
    # |                LOAD_CONST               3 ('py0')
    # |                LOAD_CONST               4 ('self')
    # |                LOAD_GLOBAL              6 (@py_builtins)
    # |                LOAD_ATTR                8 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               10 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (self)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         0 (self)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               4 ('self')
    # |        L3:     LOAD_CONST               5 ('py2')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert1)
    # |                CALL                     1
    # |                LOAD_CONST               6 ('py3')
    # |                LOAD_CONST               7 ('gate')
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
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               7 ('gate')
    # |        L6:     LOAD_CONST               8 ('py4')
    # |                LOAD_CONST               9 ('para')
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
    # |                LOAD_FAST_BORROW         2 (para)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (para)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST               9 ('para')
    # |        L9:     LOAD_CONST              10 ('py6')
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               12 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert5)
    # |                CALL                     1
    # |                BUILD_MAP                5
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               5 (@py_format7)
    # |                LOAD_GLOBAL             15 (AssertionError + NULL)
    # |                LOAD_GLOBAL              2 (@pytest_ar)
    # |                LOAD_ATTR               16 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_format7)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              11 (None)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST   52 (@py_assert1, @py_assert5)
    # |                LOAD_CONST              11 (None)
    # |                RETURN_VALUE

    def _check(self, gate, para):
        'dialogue'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 195           RESUME                   0
        # | 196           LOAD_GLOBAL              1 (make_chapter + NULL)
        # |               LOAD_FAST_BORROW         2 (para)
        # |               LOAD_CONST               0 (('inject',))
        # |               CALL_KW                  1
        # |               STORE_FAST               3 (text)
        # | 197           LOAD_CONST               1 ('dialogue')
        # |               LOAD_GLOBAL              3 (rules + NULL)
        # |               LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                5 (check + NULL|self)
        # |               LOAD_FAST_BORROW         3 (text)
        # |               CALL                     1
        # |               CALL                     1
        # |               CONTAINS_OP              0 (in)
        # |               RETURN_VALUE

    def test_same_speaker_with_inline_attribution_is_valid(self, gate, para):
        '提示语插在中间、逗号收尾 —— 同一个人在说话，是标准写法。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 199            RESUME                   0
        # | 207            LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                0 (_check)
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (gate, para)
        # |                CALL                     2
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                UNARY_NOT
        # |                STORE_FAST_LOAD_FAST    85 (@py_assert7, @py_assert7)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       349 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST               1 ('误判了标准写法：')
        # |                LOAD_FAST_BORROW         2 (para)
        # |                FORMAT_SIMPLE
        # |                BUILD_STRING             2
        # |                CALL                     1
        # |                LOAD_CONST               2 ('\n>assert not %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s._check\n}(%(py3)s, %(py4)s)\n}')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('self')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         0 (self)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         0 (self)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('self')
        # |        L3:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py3')
        # |                LOAD_CONST               7 ('gate')
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
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py4')
        # |                LOAD_CONST               9 ('para')
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
        # |                LOAD_FAST_BORROW         2 (para)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (para)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               9 ('para')
        # |        L9:     LOAD_CONST              10 ('py6')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                5
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
        # |       L10:     LOAD_CONST              11 (None)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert1)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   69 (@py_assert5, @py_assert7)
        # |                LOAD_CONST              11 (None)
        # |                RETURN_VALUE

    def test_two_speakers_still_caught(self, gate, para):
        '句号收尾说明提示语已结束，后面是另一个人 —— 必须分段。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 209            RESUME                   0
        # | 216            LOAD_FAST_BORROW         0 (self)
        # |                LOAD_ATTR                0 (_check)
        # |                STORE_FAST_LOAD_FAST    51 (@py_assert1, @py_assert1)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 18 (gate, para)
        # |                CALL                     2
        # |                STORE_FAST_LOAD_FAST    68 (@py_assert5, @py_assert5)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       349 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR                4 (_format_assertmsg)
        # |                PUSH_NULL
        # |                LOAD_CONST               1 ('漏判了两个说话人：')
        # |                LOAD_FAST_BORROW         2 (para)
        # |                FORMAT_SIMPLE
        # |                BUILD_STRING             2
        # |                CALL                     1
        # |                LOAD_CONST               2 ('\n>assert %(py6)s\n{%(py6)s = %(py2)s\n{%(py2)s = %(py0)s._check\n}(%(py3)s, %(py4)s)\n}')
        # |                BINARY_OP                0 (+)
        # |                LOAD_CONST               3 ('py0')
        # |                LOAD_CONST               4 ('self')
        # |                LOAD_GLOBAL              6 (@py_builtins)
        # |                LOAD_ATTR                8 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               10 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         0 (self)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         0 (self)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               4 ('self')
        # |        L3:     LOAD_CONST               5 ('py2')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert1)
        # |                CALL                     1
        # |                LOAD_CONST               6 ('py3')
        # |                LOAD_CONST               7 ('gate')
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
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               7 ('gate')
        # |        L6:     LOAD_CONST               8 ('py4')
        # |                LOAD_CONST               9 ('para')
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
        # |                LOAD_FAST_BORROW         2 (para)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (para)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST               9 ('para')
        # |        L9:     LOAD_CONST              10 ('py6')
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               12 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert5)
        # |                CALL                     1
        # |                BUILD_MAP                5
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               5 (@py_format7)
        # |                LOAD_GLOBAL             15 (AssertionError + NULL)
        # |                LOAD_GLOBAL              2 (@pytest_ar)
        # |                LOAD_ATTR               16 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_format7)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              11 (None)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST   52 (@py_assert1, @py_assert5)
        # |                LOAD_CONST              11 (None)
        # |                RETURN_VALUE


class TestToleranceBands:
    'TestToleranceBands'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 219           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestToleranceBands')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_SMALL_INT         219
    # |               STORE_NAME               3 (__firstlineno__)
    # | 220           LOAD_CONST               1 ('统计特征擦边不该当作错误。实测第 2 章连续三次对话占比落在\n13.3%~13.6%（下限 15%），因为那一章的场景本身就偏独处 ——\n硬性打回会让修订环去修一个本不该由它修的问题。')
    # |               STORE_NAME               4 (__doc__)
    # | 224           LOAD_CONST               2 (<code object test_bound_check_three_states at 0x7a74d9b200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 224>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_bound_check_three_states)
    # | 231           LOAD_CONST               3 (<code object test_upper_bound_tolerance at 0x7a752ed180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 231>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_upper_bound_tolerance)
    # | 237           LOAD_CONST               4 (<code object test_zero_tolerance_is_strict at 0x7a74d71180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 237>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_zero_tolerance_is_strict)
    # | 242           LOAD_CONST               5 (<code object test_soft_dialogue_ratio_passes_gate at 0x7a74d9b700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 242>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               8 (test_soft_dialogue_ratio_passes_gate)
    # | 250           LOAD_CONST               6 (<code object test_far_out_of_band_still_fails at 0x7a74da4500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 250>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               9 (test_far_out_of_band_still_fails)
    # | 254           LOAD_CONST               7 (<code object test_soft_violation_labelled at 0x7a74da4a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 254>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME              10 (test_soft_violation_labelled)
    # |               LOAD_CONST               8 (())
    # |               STORE_NAME              11 (__static_attributes__)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_bound_check_three_states at 0x7a74d9b200, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 224>:
    # | 224           RESUME                   0
    # | 225           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('bound_check',))
    # |               IMPORT_NAME              0 (novel_agent.agents.gate)
    # |               IMPORT_FROM              1 (bound_check)
    # |               STORE_FAST               1 (bound_check)
    # |               POP_TOP
    # | 227           LOAD_FAST_BORROW         1 (bound_check)
    # |               PUSH_NULL
    # |               LOAD_CONST               2 (0.22)
    # |               LOAD_CONST               3 (0.15)
    # |               LOAD_CONST               4 (0.4)
    # |               LOAD_CONST               5 (0.2)
    # |               CALL                     4
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               6 ('ok')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               9 ('assert %(py6)s')
    # |               LOAD_CONST              10 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             11 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # | 228           LOAD_FAST_BORROW         1 (bound_check)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 (0.133)
    # |               LOAD_CONST               3 (0.15)
    # |               LOAD_CONST               4 (0.4)
    # |               LOAD_CONST               5 (0.2)
    # |               CALL                     4
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST              13 ('soft')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               9 ('assert %(py6)s')
    # |               LOAD_CONST              10 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             11 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # | 229           LOAD_FAST_BORROW         1 (bound_check)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (0.1)
    # |               LOAD_CONST               3 (0.15)
    # |               LOAD_CONST               4 (0.4)
    # |               LOAD_CONST               5 (0.2)
    # |               CALL                     4
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST              15 ('hard')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L3)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              16 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              17 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               9 ('assert %(py6)s')
    # |               LOAD_CONST              10 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             11 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L3:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |               LOAD_CONST              11 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_upper_bound_tolerance at 0x7a752ed180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 231>:
    # | 231           RESUME                   0
    # | 232           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('bound_check',))
    # |               IMPORT_NAME              0 (novel_agent.agents.gate)
    # |               IMPORT_FROM              1 (bound_check)
    # |               STORE_FAST               1 (bound_check)
    # |               POP_TOP
    # | 234           LOAD_FAST_BORROW         1 (bound_check)
    # |               PUSH_NULL
    # |               LOAD_CONST               2 (40.7)
    # |               LOAD_CONST               3 (14.0)
    # |               LOAD_CONST               4 (40.0)
    # |               LOAD_CONST               5 (0.2)
    # |               CALL                     4
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               6 ('soft')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               9 ('assert %(py6)s')
    # |               LOAD_CONST              10 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             11 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # | 235           LOAD_FAST_BORROW         1 (bound_check)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 (55.0)
    # |               LOAD_CONST               3 (14.0)
    # |               LOAD_CONST               4 (40.0)
    # |               LOAD_CONST               5 (0.2)
    # |               CALL                     4
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST              13 ('hard')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L2)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              14 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              15 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               9 ('assert %(py6)s')
    # |               LOAD_CONST              10 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             11 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L2:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |               LOAD_CONST              11 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_zero_tolerance_is_strict at 0x7a74d71180, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 237>:
    # | 237           RESUME                   0
    # | 238           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('bound_check',))
    # |               IMPORT_NAME              0 (novel_agent.agents.gate)
    # |               IMPORT_FROM              1 (bound_check)
    # |               STORE_FAST               1 (bound_check)
    # |               POP_TOP
    # | 240           LOAD_FAST_BORROW         1 (bound_check)
    # |               PUSH_NULL
    # |               LOAD_CONST               2 (0.149)
    # |               LOAD_CONST               3 (0.15)
    # |               LOAD_CONST               4 (0.4)
    # |               LOAD_CONST               5 (0.0)
    # |               CALL                     4
    # |               LOAD_SMALL_INT           0
    # |               BINARY_OP               26 ([])
    # |               STORE_FAST               2 (@py_assert0)
    # |               LOAD_CONST               6 ('hard')
    # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               COMPARE_OP              72 (==)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       121 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                6 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              12 (('==',))
    # |               LOAD_FAST_BORROW         4 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              13 (('%(py1)s == %(py4)s',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         2 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR                8 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               5 (@py_format5)
    # |               LOAD_CONST               9 ('assert %(py6)s')
    # |               LOAD_CONST              10 ('py6')
    # |               LOAD_FAST_BORROW         5 (@py_format5)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format7)
    # |               LOAD_GLOBAL             11 (AssertionError + NULL)
    # |               LOAD_GLOBAL              4 (@pytest_ar)
    # |               LOAD_ATTR               12 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format7)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L1:     LOAD_CONST              11 (None)
    # |               COPY                     1
    # |               STORE_FAST               2 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
    # |               LOAD_CONST              11 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_soft_dialogue_ratio_passes_gate at 0x7a74d9b700, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 242>:
    # |  242            RESUME                   0
    # |  244            LOAD_GLOBAL              1 (make_chapter + NULL)
    # |                 LOAD_CONST               1 ('“嗯呢。”')
    # |                 LOAD_CONST               2 (('dialogue',))
    # |                 CALL_KW                  1
    # |                 STORE_FAST               2 (text)
    # |  245            LOAD_FAST_BORROW         1 (gate)
    # |                 LOAD_ATTR                3 (check + NULL|self)
    # |                 LOAD_FAST_BORROW         2 (text)
    # |                 CALL                     1
    # |                 STORE_FAST               3 (report)
    # |  246            LOAD_FAST_BORROW         3 (report)
    # |                 LOAD_ATTR                4 (warnings)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      4 (f)
    # |                 SWAP                     2
    # |         L1:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L2:     FOR_ITER                23 (to L5)
    # |                 STORE_FAST_LOAD_FAST    68 (f, f)
    # |                 LOAD_ATTR                6 (rule)
    # |                 LOAD_CONST               3 ('dialogue_ratio')
    # |                 COMPARE_OP              88 (bool(==))
    # |         L3:     POP_JUMP_IF_TRUE         3 (to L4)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD           21 (to L2)
    # |         L4:     LOAD_FAST_BORROW         4 (f)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           25 (to L2)
    # |         L5:     END_FOR
    # |                 POP_ITER
    # |         L6:     STORE_FAST               5 (soft)
    # |                 STORE_FAST               4 (f)
    # |  247            LOAD_FAST_BORROW         3 (report)
    # |                 LOAD_ATTR                8 (errors)
    # |                 GET_ITER
    # |                 LOAD_FAST_AND_CLEAR      4 (f)
    # |                 SWAP                     2
    # |         L7:     BUILD_LIST               0
    # |                 SWAP                     2
    # |         L8:     FOR_ITER                23 (to L11)
    # |                 STORE_FAST_LOAD_FAST    68 (f, f)
    # |                 LOAD_ATTR                6 (rule)
    # |                 LOAD_CONST               3 ('dialogue_ratio')
    # |                 COMPARE_OP              88 (bool(==))
    # |         L9:     POP_JUMP_IF_TRUE         3 (to L10)
    # |                 NOT_TAKEN
    # |                 JUMP_BACKWARD           21 (to L8)
    # |        L10:     LOAD_FAST_BORROW         4 (f)
    # |                 LIST_APPEND              2
    # |                 JUMP_BACKWARD           25 (to L8)
    # |        L11:     END_FOR
    # |                 POP_ITER
    # |        L12:     STORE_FAST               6 (hard)
    # |                 STORE_FAST               4 (f)
    # |  248            BUILD_LIST               0
    # |                 STORE_FAST_LOAD_FAST   117 (@py_assert1, soft)
    # |                 STORE_FAST_LOAD_FAST   133 (@py_assert0, soft)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE        3 (to L13)
    # |                 NOT_TAKEN
    # |                 LOAD_FAST                6 (hard)
    # |                 STORE_FAST               8 (@py_assert0)
    # |        L13:     LOAD_FAST_BORROW         8 (@py_assert0)
    # |                 TO_BOOL
    # |                 UNARY_NOT
    # |                 STORE_FAST_LOAD_FAST   153 (@py_assert8, @py_assert8)
    # |                 TO_BOOL
    # |                 EXTENDED_ARG             1
    # |                 POP_JUMP_IF_TRUE       314 (to L21)
    # |                 NOT_TAKEN
    # |                 LOAD_CONST               4 ('%(py2)s')
    # |                 LOAD_CONST               5 ('py2')
    # |                 LOAD_CONST               6 ('soft')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L14)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (soft)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L15)
    # |                 NOT_TAKEN
    # |        L14:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         5 (soft)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L16)
    # |        L15:     LOAD_CONST               6 ('soft')
    # |        L16:     BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST_LOAD_FAST   167 (@py_format3, @py_assert1)
    # |                 LOAD_ATTR               21 (append + NULL|self)
    # |                 LOAD_FAST_BORROW        10 (@py_format3)
    # |                 CALL                     1
    # |                 POP_TOP
    # |                 LOAD_FAST_BORROW         5 (soft)
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE      104 (to L20)
    # |                 NOT_TAKEN
    # |                 LOAD_CONST               7 ('%(py4)s')
    # |                 LOAD_CONST               8 ('py4')
    # |                 LOAD_CONST               9 ('hard')
    # |                 LOAD_GLOBAL             10 (@py_builtins)
    # |                 LOAD_ATTR               12 (locals)
    # |                 PUSH_NULL
    # |                 CALL                     0
    # |                 CONTAINS_OP              0 (in)
    # |                 POP_JUMP_IF_TRUE        29 (to L17)
    # |                 NOT_TAKEN
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               16 (_should_repr_global_name)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (hard)
    # |                 CALL                     1
    # |                 TO_BOOL
    # |                 POP_JUMP_IF_FALSE       23 (to L18)
    # |                 NOT_TAKEN
    # |        L17:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               18 (_saferepr)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         6 (hard)
    # |                 CALL                     1
    # |                 JUMP_FORWARD             1 (to L19)
    # |        L18:     LOAD_CONST               9 ('hard')
    # |        L19:     BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST_LOAD_FAST   183 (@py_format5, @py_assert1)
    # |                 LOAD_ATTR               21 (append + NULL|self)
    # |                 LOAD_FAST_BORROW        11 (@py_format5)
    # |                 CALL                     1
    # |                 POP_TOP
    # |        L20:     LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               22 (_format_boolop)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW         7 (@py_assert1)
    # |                 LOAD_SMALL_INT           0
    # |                 CALL                     2
    # |                 BUILD_MAP                0
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              12 (@py_format6)
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               24 (_format_assertmsg)
    # |                 PUSH_NULL
    # |                 LOAD_CONST              10 ('同一项不该既是警告又是错误')
    # |                 CALL                     1
    # |                 LOAD_CONST              11 ('\n>assert not %(py7)s')
    # |                 BINARY_OP                0 (+)
    # |                 LOAD_CONST              12 ('py7')
    # |                 LOAD_FAST_BORROW        12 (@py_format6)
    # |                 BUILD_MAP                1
    # |                 BINARY_OP                6 (%)
    # |                 STORE_FAST              13 (@py_format9)
    # |                 LOAD_GLOBAL             27 (AssertionError + NULL)
    # |                 LOAD_GLOBAL             14 (@pytest_ar)
    # |                 LOAD_ATTR               28 (_format_explanation)
    # |                 PUSH_NULL
    # |                 LOAD_FAST_BORROW        13 (@py_format9)
    # |                 CALL                     1
    # |                 CALL                     1
    # |                 RAISE_VARARGS            1
    # |        L21:     LOAD_CONST              13 (None)
    # |                 COPY                     1
    # |                 STORE_FAST               8 (@py_assert0)
    # |                 COPY                     1
    # |                 STORE_FAST_STORE_FAST  121 (@py_assert1, @py_assert8)
    # |                 LOAD_CONST              13 (None)
    # |                 RETURN_VALUE
    # |   --   L22:     SWAP                     2
    # |                 POP_TOP
    # |  246            SWAP                     2
    # |                 STORE_FAST               4 (f)
    # |                 RERAISE                  0
    # |   --   L23:     SWAP                     2
    # |                 POP_TOP
    # |  247            SWAP                     2
    # |                 STORE_FAST               4 (f)
    # |                 RERAISE                  0
    # | ExceptionTable:
    # |   L1 to L3 -> L22 [2]
    # |   L4 to L6 -> L22 [2]
    # |   L7 to L9 -> L23 [2]
    # |   L10 to L12 -> L23 [2]
    # | Disassembly of <code object test_far_out_of_band_still_fails at 0x7a74da4500, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 250>:
    # | 250            RESUME                   0
    # | 252            LOAD_CONST               1 ('dialogue_ratio')
    # |                STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
    # |                LOAD_ATTR                0 (check)
    # |                STORE_FAST               3 (@py_assert5)
    # |                LOAD_CONST               2 ('他没说话。')
    # |                STORE_FAST               4 (@py_assert8)
    # |                LOAD_GLOBAL              3 (make_chapter + NULL)
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                LOAD_CONST               3 (('dialogue',))
    # |                CALL_KW                  1
    # |                STORE_FAST_LOAD_FAST    83 (@py_assert10, @py_assert5)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert10)
    # |                CALL                     1
    # |                STORE_FAST               6 (@py_assert12)
    # |                LOAD_GLOBAL              5 (rules + NULL)
    # |                LOAD_FAST_BORROW         6 (@py_assert12)
    # |                CALL                     1
    # |                STORE_FAST_LOAD_FAST   114 (@py_assert14, @py_assert0)
    # |                LOAD_FAST_BORROW         7 (@py_assert14)
    # |                CONTAINS_OP              0 (in)
    # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |                TO_BOOL
    # |                EXTENDED_ARG             1
    # |                POP_JUMP_IF_TRUE       459 (to L10)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR                8 (_call_reprcompare)
    # |                PUSH_NULL
    # |                LOAD_CONST              19 (('in',))
    # |                LOAD_FAST_BORROW         8 (@py_assert2)
    # |                BUILD_TUPLE              1
    # |                LOAD_CONST              20 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py11)s\n{%(py11)s = %(py7)s(dialogue=%(py9)s)\n})\n})\n}',))
    # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (@py_assert0, @py_assert14)
    # |                BUILD_TUPLE              2
    # |                CALL                     4
    # |                LOAD_CONST               4 ('py1')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         2 (@py_assert0)
    # |                CALL                     1
    # |                LOAD_CONST               5 ('py3')
    # |                LOAD_CONST               6 ('rules')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L1)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L2)
    # |                NOT_TAKEN
    # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              4 (rules)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L3)
    # |        L2:     LOAD_CONST               6 ('rules')
    # |        L3:     LOAD_CONST               7 ('py4')
    # |                LOAD_CONST               8 ('gate')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        29 (to L4)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       23 (to L5)
    # |                NOT_TAKEN
    # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         1 (gate)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L6)
    # |        L5:     LOAD_CONST               8 ('gate')
    # |        L6:     LOAD_CONST               9 ('py6')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         3 (@py_assert5)
    # |                CALL                     1
    # |                LOAD_CONST              10 ('py7')
    # |                LOAD_CONST              11 ('make_chapter')
    # |                LOAD_GLOBAL             12 (@py_builtins)
    # |                LOAD_ATTR               14 (locals)
    # |                PUSH_NULL
    # |                CALL                     0
    # |                CONTAINS_OP              0 (in)
    # |                POP_JUMP_IF_TRUE        33 (to L7)
    # |                NOT_TAKEN
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               16 (_should_repr_global_name)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (make_chapter)
    # |                CALL                     1
    # |                TO_BOOL
    # |                POP_JUMP_IF_FALSE       27 (to L8)
    # |                NOT_TAKEN
    # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_GLOBAL              2 (make_chapter)
    # |                CALL                     1
    # |                JUMP_FORWARD             1 (to L9)
    # |        L8:     LOAD_CONST              11 ('make_chapter')
    # |        L9:     LOAD_CONST              12 ('py9')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         4 (@py_assert8)
    # |                CALL                     1
    # |                LOAD_CONST              13 ('py11')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         5 (@py_assert10)
    # |                CALL                     1
    # |                LOAD_CONST              14 ('py13')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         6 (@py_assert12)
    # |                CALL                     1
    # |                LOAD_CONST              15 ('py15')
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               10 (_saferepr)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW         7 (@py_assert14)
    # |                CALL                     1
    # |                BUILD_MAP                9
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST               9 (@py_format16)
    # |                LOAD_CONST              16 ('assert %(py17)s')
    # |                LOAD_CONST              17 ('py17')
    # |                LOAD_FAST_BORROW         9 (@py_format16)
    # |                BUILD_MAP                1
    # |                BINARY_OP                6 (%)
    # |                STORE_FAST              10 (@py_format18)
    # |                LOAD_GLOBAL             19 (AssertionError + NULL)
    # |                LOAD_GLOBAL              6 (@pytest_ar)
    # |                LOAD_ATTR               20 (_format_explanation)
    # |                PUSH_NULL
    # |                LOAD_FAST_BORROW        10 (@py_format18)
    # |                CALL                     1
    # |                CALL                     1
    # |                RAISE_VARARGS            1
    # |       L10:     LOAD_CONST              18 (None)
    # |                COPY                     1
    # |                STORE_FAST               2 (@py_assert0)
    # |                COPY                     1
    # |                STORE_FAST               8 (@py_assert2)
    # |                COPY                     1
    # |                STORE_FAST               3 (@py_assert5)
    # |                COPY                     1
    # |                STORE_FAST               4 (@py_assert8)
    # |                COPY                     1
    # |                STORE_FAST               5 (@py_assert10)
    # |                COPY                     1
    # |                STORE_FAST_STORE_FAST  103 (@py_assert12, @py_assert14)
    # |                LOAD_CONST              18 (None)
    # |                RETURN_VALUE
    # | Disassembly of <code object test_soft_violation_labelled at 0x7a74da4a00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 254>:
    # | 254           RESUME                   0
    # | 256           LOAD_SMALL_INT           0
    # |               LOAD_CONST               1 (('Gate',))
    # |               IMPORT_NAME              0 (novel_agent.agents.gate)
    # |               IMPORT_FROM              1 (Gate)
    # |               STORE_FAST               2 (Gate)
    # |               POP_TOP
    # | 258           LOAD_GLOBAL              5 (make_chapter + NULL)
    # |               CALL                     0
    # |               STORE_FAST               3 (text)
    # | 259           LOAD_FAST_BORROW         2 (Gate)
    # |               LOAD_ATTR                6 (from_config)
    # |               PUSH_NULL
    # | 260           LOAD_GLOBAL              9 (__import__ + NULL)
    # |               LOAD_CONST               2 ('pathlib')
    # |               CALL                     1
    # |               LOAD_ATTR               11 (Path + NULL|self)
    # |               LOAD_GLOBAL             12 (__file__)
    # |               CALL                     1
    # |               LOAD_ATTR               15 (resolve + NULL|self)
    # |               CALL                     0
    # |               LOAD_ATTR               16 (parent)
    # |               LOAD_ATTR               16 (parent)
    # | 261           LOAD_CONST               3 ('config')
    # | 260           BINARY_OP               11 (/)
    # | 261           LOAD_CONST               4 ('project.yaml')
    # | 260           BINARY_OP               11 (/)
    # | 259           CALL                     1
    # | 261           LOAD_ATTR               19 (check + NULL|self)
    # |               LOAD_FAST_BORROW         3 (text)
    # |               CALL                     1
    # | 259           STORE_FAST               4 (r)
    # | 262           LOAD_FAST_BORROW         4 (r)
    # |               LOAD_ATTR               20 (findings)
    # |               GET_ITER
    # |       L1:     EXTENDED_ARG             1
    # |               FOR_ITER               269 (to L8)
    # |               STORE_FAST               5 (f)
    # | 263           LOAD_FAST_BORROW         5 (f)
    # |               LOAD_ATTR               22 (severity)
    # |               LOAD_CONST               5 ('warn')
    # |               COMPARE_OP              88 (bool(==))
    # |               POP_JUMP_IF_TRUE         3 (to L2)
    # |               NOT_TAKEN
    # |               JUMP_BACKWARD           23 (to L1)
    # |       L2:     LOAD_FAST_BORROW         5 (f)
    # |               LOAD_ATTR               24 (rule)
    # |               LOAD_CONST              14 (frozenset({'dialogue_ratio', 'style'}))
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE         3 (to L3)
    # |               NOT_TAKEN
    # |               JUMP_BACKWARD           42 (to L1)
    # | 264   L3:     LOAD_CONST               6 ('容差内')
    # |               STORE_FAST_LOAD_FAST   101 (@py_assert0, f)
    # |               LOAD_ATTR               26 (message)
    # |               STORE_FAST_LOAD_FAST   118 (@py_assert4, @py_assert0)
    # |               LOAD_FAST_BORROW         7 (@py_assert4)
    # |               CONTAINS_OP              0 (in)
    # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       199 (to L7)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             28 (@pytest_ar)
    # |               LOAD_ATTR               30 (_call_reprcompare)
    # |               PUSH_NULL
    # |               LOAD_CONST              15 (('in',))
    # |               LOAD_FAST_BORROW         8 (@py_assert2)
    # |               BUILD_TUPLE              1
    # |               LOAD_CONST              16 (('%(py1)s in %(py5)s\n{%(py5)s = %(py3)s.message\n}',))
    # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert4)
    # |               BUILD_TUPLE              2
    # |               CALL                     4
    # |               LOAD_CONST               7 ('py1')
    # |               LOAD_GLOBAL             28 (@pytest_ar)
    # |               LOAD_ATTR               32 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_assert0)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py3')
    # |               LOAD_CONST               9 ('f')
    # |               LOAD_GLOBAL             34 (@py_builtins)
    # |               LOAD_ATTR               36 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             28 (@pytest_ar)
    # |               LOAD_ATTR               38 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (f)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L5)
    # |               NOT_TAKEN
    # |       L4:     LOAD_GLOBAL             28 (@pytest_ar)
    # |               LOAD_ATTR               32 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (f)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L6)
    # |       L5:     LOAD_CONST               9 ('f')
    # |       L6:     LOAD_CONST              10 ('py5')
    # |               LOAD_GLOBAL             28 (@pytest_ar)
    # |               LOAD_ATTR               32 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_assert4)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               9 (@py_format6)
    # |               LOAD_CONST              11 ('assert %(py7)s')
    # |               LOAD_CONST              12 ('py7')
    # |               LOAD_FAST_BORROW         9 (@py_format6)
    # |               BUILD_MAP                1
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST              10 (@py_format8)
    # |               LOAD_GLOBAL             41 (AssertionError + NULL)
    # |               LOAD_GLOBAL             28 (@pytest_ar)
    # |               LOAD_ATTR               42 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW        10 (@py_format8)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L7:     LOAD_CONST              13 (None)
    # |               COPY                     1
    # |               STORE_FAST               6 (@py_assert0)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert4)
    # |               EXTENDED_ARG             1
    # |               JUMP_BACKWARD          272 (to L1)
    # | 262   L8:     END_FOR
    # |               POP_ITER
    # |               LOAD_CONST              13 (None)
    # |               RETURN_VALUE

    def test_bound_check_three_states(self):
        'ok'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 224           RESUME                   0
        # | 225           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('bound_check',))
        # |               IMPORT_NAME              0 (novel_agent.agents.gate)
        # |               IMPORT_FROM              1 (bound_check)
        # |               STORE_FAST               1 (bound_check)
        # |               POP_TOP
        # | 227           LOAD_FAST_BORROW         1 (bound_check)
        # |               PUSH_NULL
        # |               LOAD_CONST               2 (0.22)
        # |               LOAD_CONST               3 (0.15)
        # |               LOAD_CONST               4 (0.4)
        # |               LOAD_CONST               5 (0.2)
        # |               CALL                     4
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               6 ('ok')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               9 ('assert %(py6)s')
        # |               LOAD_CONST              10 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             11 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # | 228           LOAD_FAST_BORROW         1 (bound_check)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 (0.133)
        # |               LOAD_CONST               3 (0.15)
        # |               LOAD_CONST               4 (0.4)
        # |               LOAD_CONST               5 (0.2)
        # |               CALL                     4
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST              13 ('soft')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               9 ('assert %(py6)s')
        # |               LOAD_CONST              10 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             11 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # | 229           LOAD_FAST_BORROW         1 (bound_check)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (0.1)
        # |               LOAD_CONST               3 (0.15)
        # |               LOAD_CONST               4 (0.4)
        # |               LOAD_CONST               5 (0.2)
        # |               CALL                     4
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST              15 ('hard')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L3)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              16 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              17 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               9 ('assert %(py6)s')
        # |               LOAD_CONST              10 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             11 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L3:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |               LOAD_CONST              11 (None)
        # |               RETURN_VALUE

    def test_upper_bound_tolerance(self):
        'soft'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 231           RESUME                   0
        # | 232           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('bound_check',))
        # |               IMPORT_NAME              0 (novel_agent.agents.gate)
        # |               IMPORT_FROM              1 (bound_check)
        # |               STORE_FAST               1 (bound_check)
        # |               POP_TOP
        # | 234           LOAD_FAST_BORROW         1 (bound_check)
        # |               PUSH_NULL
        # |               LOAD_CONST               2 (40.7)
        # |               LOAD_CONST               3 (14.0)
        # |               LOAD_CONST               4 (40.0)
        # |               LOAD_CONST               5 (0.2)
        # |               CALL                     4
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               6 ('soft')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              15 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               9 ('assert %(py6)s')
        # |               LOAD_CONST              10 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             11 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # | 235           LOAD_FAST_BORROW         1 (bound_check)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 (55.0)
        # |               LOAD_CONST               3 (14.0)
        # |               LOAD_CONST               4 (40.0)
        # |               LOAD_CONST               5 (0.2)
        # |               CALL                     4
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST              13 ('hard')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L2)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              14 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              15 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               9 ('assert %(py6)s')
        # |               LOAD_CONST              10 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             11 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L2:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |               LOAD_CONST              11 (None)
        # |               RETURN_VALUE

    def test_zero_tolerance_is_strict(self):
        'hard'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 237           RESUME                   0
        # | 238           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('bound_check',))
        # |               IMPORT_NAME              0 (novel_agent.agents.gate)
        # |               IMPORT_FROM              1 (bound_check)
        # |               STORE_FAST               1 (bound_check)
        # |               POP_TOP
        # | 240           LOAD_FAST_BORROW         1 (bound_check)
        # |               PUSH_NULL
        # |               LOAD_CONST               2 (0.149)
        # |               LOAD_CONST               3 (0.15)
        # |               LOAD_CONST               4 (0.4)
        # |               LOAD_CONST               5 (0.0)
        # |               CALL                     4
        # |               LOAD_SMALL_INT           0
        # |               BINARY_OP               26 ([])
        # |               STORE_FAST               2 (@py_assert0)
        # |               LOAD_CONST               6 ('hard')
        # |               STORE_FAST_LOAD_FAST    50 (@py_assert3, @py_assert0)
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               COMPARE_OP              72 (==)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       121 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                6 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              12 (('==',))
        # |               LOAD_FAST_BORROW         4 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              13 (('%(py1)s == %(py4)s',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 35 (@py_assert0, @py_assert3)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         2 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR                8 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               5 (@py_format5)
        # |               LOAD_CONST               9 ('assert %(py6)s')
        # |               LOAD_CONST              10 ('py6')
        # |               LOAD_FAST_BORROW         5 (@py_format5)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format7)
        # |               LOAD_GLOBAL             11 (AssertionError + NULL)
        # |               LOAD_GLOBAL              4 (@pytest_ar)
        # |               LOAD_ATTR               12 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format7)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L1:     LOAD_CONST              11 (None)
        # |               COPY                     1
        # |               STORE_FAST               2 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   67 (@py_assert2, @py_assert3)
        # |               LOAD_CONST              11 (None)
        # |               RETURN_VALUE

    def test_soft_dialogue_ratio_passes_gate(self, gate):
        '擦边的稿子放行，把判定交给 judge。'
        # ── 函数体（字节码重建见 BODY 段）──
        # |  242            RESUME                   0
        # |  244            LOAD_GLOBAL              1 (make_chapter + NULL)
        # |                 LOAD_CONST               1 ('“嗯呢。”')
        # |                 LOAD_CONST               2 (('dialogue',))
        # |                 CALL_KW                  1
        # |                 STORE_FAST               2 (text)
        # |  245            LOAD_FAST_BORROW         1 (gate)
        # |                 LOAD_ATTR                3 (check + NULL|self)
        # |                 LOAD_FAST_BORROW         2 (text)
        # |                 CALL                     1
        # |                 STORE_FAST               3 (report)
        # |  246            LOAD_FAST_BORROW         3 (report)
        # |                 LOAD_ATTR                4 (warnings)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      4 (f)
        # |                 SWAP                     2
        # |         L1:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L2:     FOR_ITER                23 (to L5)
        # |                 STORE_FAST_LOAD_FAST    68 (f, f)
        # |                 LOAD_ATTR                6 (rule)
        # |                 LOAD_CONST               3 ('dialogue_ratio')
        # |                 COMPARE_OP              88 (bool(==))
        # |         L3:     POP_JUMP_IF_TRUE         3 (to L4)
        # |                 NOT_TAKEN
        # |                 JUMP_BACKWARD           21 (to L2)
        # |         L4:     LOAD_FAST_BORROW         4 (f)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           25 (to L2)
        # |         L5:     END_FOR
        # |                 POP_ITER
        # |         L6:     STORE_FAST               5 (soft)
        # |                 STORE_FAST               4 (f)
        # |  247            LOAD_FAST_BORROW         3 (report)
        # |                 LOAD_ATTR                8 (errors)
        # |                 GET_ITER
        # |                 LOAD_FAST_AND_CLEAR      4 (f)
        # |                 SWAP                     2
        # |         L7:     BUILD_LIST               0
        # |                 SWAP                     2
        # |         L8:     FOR_ITER                23 (to L11)
        # |                 STORE_FAST_LOAD_FAST    68 (f, f)
        # |                 LOAD_ATTR                6 (rule)
        # |                 LOAD_CONST               3 ('dialogue_ratio')
        # |                 COMPARE_OP              88 (bool(==))
        # |         L9:     POP_JUMP_IF_TRUE         3 (to L10)
        # |                 NOT_TAKEN
        # |                 JUMP_BACKWARD           21 (to L8)
        # |        L10:     LOAD_FAST_BORROW         4 (f)
        # |                 LIST_APPEND              2
        # |                 JUMP_BACKWARD           25 (to L8)
        # |        L11:     END_FOR
        # |                 POP_ITER
        # |        L12:     STORE_FAST               6 (hard)
        # |                 STORE_FAST               4 (f)
        # |  248            BUILD_LIST               0
        # |                 STORE_FAST_LOAD_FAST   117 (@py_assert1, soft)
        # |                 STORE_FAST_LOAD_FAST   133 (@py_assert0, soft)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE        3 (to L13)
        # |                 NOT_TAKEN
        # |                 LOAD_FAST                6 (hard)
        # |                 STORE_FAST               8 (@py_assert0)
        # |        L13:     LOAD_FAST_BORROW         8 (@py_assert0)
        # |                 TO_BOOL
        # |                 UNARY_NOT
        # |                 STORE_FAST_LOAD_FAST   153 (@py_assert8, @py_assert8)
        # |                 TO_BOOL
        # |                 EXTENDED_ARG             1
        # |                 POP_JUMP_IF_TRUE       314 (to L21)
        # |                 NOT_TAKEN
        # |                 LOAD_CONST               4 ('%(py2)s')
        # |                 LOAD_CONST               5 ('py2')
        # |                 LOAD_CONST               6 ('soft')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L14)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (soft)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L15)
        # |                 NOT_TAKEN
        # |        L14:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         5 (soft)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L16)
        # |        L15:     LOAD_CONST               6 ('soft')
        # |        L16:     BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST_LOAD_FAST   167 (@py_format3, @py_assert1)
        # |                 LOAD_ATTR               21 (append + NULL|self)
        # |                 LOAD_FAST_BORROW        10 (@py_format3)
        # |                 CALL                     1
        # |                 POP_TOP
        # |                 LOAD_FAST_BORROW         5 (soft)
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE      104 (to L20)
        # |                 NOT_TAKEN
        # |                 LOAD_CONST               7 ('%(py4)s')
        # |                 LOAD_CONST               8 ('py4')
        # |                 LOAD_CONST               9 ('hard')
        # |                 LOAD_GLOBAL             10 (@py_builtins)
        # |                 LOAD_ATTR               12 (locals)
        # |                 PUSH_NULL
        # |                 CALL                     0
        # |                 CONTAINS_OP              0 (in)
        # |                 POP_JUMP_IF_TRUE        29 (to L17)
        # |                 NOT_TAKEN
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               16 (_should_repr_global_name)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (hard)
        # |                 CALL                     1
        # |                 TO_BOOL
        # |                 POP_JUMP_IF_FALSE       23 (to L18)
        # |                 NOT_TAKEN
        # |        L17:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               18 (_saferepr)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         6 (hard)
        # |                 CALL                     1
        # |                 JUMP_FORWARD             1 (to L19)
        # |        L18:     LOAD_CONST               9 ('hard')
        # |        L19:     BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST_LOAD_FAST   183 (@py_format5, @py_assert1)
        # |                 LOAD_ATTR               21 (append + NULL|self)
        # |                 LOAD_FAST_BORROW        11 (@py_format5)
        # |                 CALL                     1
        # |                 POP_TOP
        # |        L20:     LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               22 (_format_boolop)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW         7 (@py_assert1)
        # |                 LOAD_SMALL_INT           0
        # |                 CALL                     2
        # |                 BUILD_MAP                0
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              12 (@py_format6)
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               24 (_format_assertmsg)
        # |                 PUSH_NULL
        # |                 LOAD_CONST              10 ('同一项不该既是警告又是错误')
        # |                 CALL                     1
        # |                 LOAD_CONST              11 ('\n>assert not %(py7)s')
        # |                 BINARY_OP                0 (+)
        # |                 LOAD_CONST              12 ('py7')
        # |                 LOAD_FAST_BORROW        12 (@py_format6)
        # |                 BUILD_MAP                1
        # |                 BINARY_OP                6 (%)
        # |                 STORE_FAST              13 (@py_format9)
        # |                 LOAD_GLOBAL             27 (AssertionError + NULL)
        # |                 LOAD_GLOBAL             14 (@pytest_ar)
        # |                 LOAD_ATTR               28 (_format_explanation)
        # |                 PUSH_NULL
        # |                 LOAD_FAST_BORROW        13 (@py_format9)
        # |                 CALL                     1
        # |                 CALL                     1
        # |                 RAISE_VARARGS            1
        # |        L21:     LOAD_CONST              13 (None)
        # |                 COPY                     1
        # |                 STORE_FAST               8 (@py_assert0)
        # |                 COPY                     1
        # |                 STORE_FAST_STORE_FAST  121 (@py_assert1, @py_assert8)
        # |                 LOAD_CONST              13 (None)
        # |                 RETURN_VALUE
        # |   --   L22:     SWAP                     2
        # |                 POP_TOP
        # |  246            SWAP                     2
        # |                 STORE_FAST               4 (f)
        # |                 RERAISE                  0
        # |   --   L23:     SWAP                     2
        # |                 POP_TOP
        # |  247            SWAP                     2
        # |                 STORE_FAST               4 (f)
        # |                 RERAISE                  0
        # | ExceptionTable:
        # |   L1 to L3 -> L22 [2]
        # |   L4 to L6 -> L22 [2]
        # |   L7 to L9 -> L23 [2]
        # |   L10 to L12 -> L23 [2]

    def test_far_out_of_band_still_fails(self, gate):
        '浮动不是放弃底线 —— 差太远仍然打回。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 250            RESUME                   0
        # | 252            LOAD_CONST               1 ('dialogue_ratio')
        # |                STORE_FAST_LOAD_FAST    33 (@py_assert0, gate)
        # |                LOAD_ATTR                0 (check)
        # |                STORE_FAST               3 (@py_assert5)
        # |                LOAD_CONST               2 ('他没说话。')
        # |                STORE_FAST               4 (@py_assert8)
        # |                LOAD_GLOBAL              3 (make_chapter + NULL)
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                LOAD_CONST               3 (('dialogue',))
        # |                CALL_KW                  1
        # |                STORE_FAST_LOAD_FAST    83 (@py_assert10, @py_assert5)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert10)
        # |                CALL                     1
        # |                STORE_FAST               6 (@py_assert12)
        # |                LOAD_GLOBAL              5 (rules + NULL)
        # |                LOAD_FAST_BORROW         6 (@py_assert12)
        # |                CALL                     1
        # |                STORE_FAST_LOAD_FAST   114 (@py_assert14, @py_assert0)
        # |                LOAD_FAST_BORROW         7 (@py_assert14)
        # |                CONTAINS_OP              0 (in)
        # |                STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |                TO_BOOL
        # |                EXTENDED_ARG             1
        # |                POP_JUMP_IF_TRUE       459 (to L10)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR                8 (_call_reprcompare)
        # |                PUSH_NULL
        # |                LOAD_CONST              19 (('in',))
        # |                LOAD_FAST_BORROW         8 (@py_assert2)
        # |                BUILD_TUPLE              1
        # |                LOAD_CONST              20 (('%(py1)s in %(py15)s\n{%(py15)s = %(py3)s(%(py13)s\n{%(py13)s = %(py6)s\n{%(py6)s = %(py4)s.check\n}(%(py11)s\n{%(py11)s = %(py7)s(dialogue=%(py9)s)\n})\n})\n}',))
        # |                LOAD_FAST_BORROW_LOAD_FAST_BORROW 39 (@py_assert0, @py_assert14)
        # |                BUILD_TUPLE              2
        # |                CALL                     4
        # |                LOAD_CONST               4 ('py1')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         2 (@py_assert0)
        # |                CALL                     1
        # |                LOAD_CONST               5 ('py3')
        # |                LOAD_CONST               6 ('rules')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L1)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L2)
        # |                NOT_TAKEN
        # |        L1:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              4 (rules)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L3)
        # |        L2:     LOAD_CONST               6 ('rules')
        # |        L3:     LOAD_CONST               7 ('py4')
        # |                LOAD_CONST               8 ('gate')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        29 (to L4)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       23 (to L5)
        # |                NOT_TAKEN
        # |        L4:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         1 (gate)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L6)
        # |        L5:     LOAD_CONST               8 ('gate')
        # |        L6:     LOAD_CONST               9 ('py6')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         3 (@py_assert5)
        # |                CALL                     1
        # |                LOAD_CONST              10 ('py7')
        # |                LOAD_CONST              11 ('make_chapter')
        # |                LOAD_GLOBAL             12 (@py_builtins)
        # |                LOAD_ATTR               14 (locals)
        # |                PUSH_NULL
        # |                CALL                     0
        # |                CONTAINS_OP              0 (in)
        # |                POP_JUMP_IF_TRUE        33 (to L7)
        # |                NOT_TAKEN
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               16 (_should_repr_global_name)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (make_chapter)
        # |                CALL                     1
        # |                TO_BOOL
        # |                POP_JUMP_IF_FALSE       27 (to L8)
        # |                NOT_TAKEN
        # |        L7:     LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_GLOBAL              2 (make_chapter)
        # |                CALL                     1
        # |                JUMP_FORWARD             1 (to L9)
        # |        L8:     LOAD_CONST              11 ('make_chapter')
        # |        L9:     LOAD_CONST              12 ('py9')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         4 (@py_assert8)
        # |                CALL                     1
        # |                LOAD_CONST              13 ('py11')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         5 (@py_assert10)
        # |                CALL                     1
        # |                LOAD_CONST              14 ('py13')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         6 (@py_assert12)
        # |                CALL                     1
        # |                LOAD_CONST              15 ('py15')
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               10 (_saferepr)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW         7 (@py_assert14)
        # |                CALL                     1
        # |                BUILD_MAP                9
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST               9 (@py_format16)
        # |                LOAD_CONST              16 ('assert %(py17)s')
        # |                LOAD_CONST              17 ('py17')
        # |                LOAD_FAST_BORROW         9 (@py_format16)
        # |                BUILD_MAP                1
        # |                BINARY_OP                6 (%)
        # |                STORE_FAST              10 (@py_format18)
        # |                LOAD_GLOBAL             19 (AssertionError + NULL)
        # |                LOAD_GLOBAL              6 (@pytest_ar)
        # |                LOAD_ATTR               20 (_format_explanation)
        # |                PUSH_NULL
        # |                LOAD_FAST_BORROW        10 (@py_format18)
        # |                CALL                     1
        # |                CALL                     1
        # |                RAISE_VARARGS            1
        # |       L10:     LOAD_CONST              18 (None)
        # |                COPY                     1
        # |                STORE_FAST               2 (@py_assert0)
        # |                COPY                     1
        # |                STORE_FAST               8 (@py_assert2)
        # |                COPY                     1
        # |                STORE_FAST               3 (@py_assert5)
        # |                COPY                     1
        # |                STORE_FAST               4 (@py_assert8)
        # |                COPY                     1
        # |                STORE_FAST               5 (@py_assert10)
        # |                COPY                     1
        # |                STORE_FAST_STORE_FAST  103 (@py_assert12, @py_assert14)
        # |                LOAD_CONST              18 (None)
        # |                RETURN_VALUE

    def test_soft_violation_labelled(self, gate):
        '报告里要看得出是"擦边"还是"真的不行"。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 254           RESUME                   0
        # | 256           LOAD_SMALL_INT           0
        # |               LOAD_CONST               1 (('Gate',))
        # |               IMPORT_NAME              0 (novel_agent.agents.gate)
        # |               IMPORT_FROM              1 (Gate)
        # |               STORE_FAST               2 (Gate)
        # |               POP_TOP
        # | 258           LOAD_GLOBAL              5 (make_chapter + NULL)
        # |               CALL                     0
        # |               STORE_FAST               3 (text)
        # | 259           LOAD_FAST_BORROW         2 (Gate)
        # |               LOAD_ATTR                6 (from_config)
        # |               PUSH_NULL
        # | 260           LOAD_GLOBAL              9 (__import__ + NULL)
        # |               LOAD_CONST               2 ('pathlib')
        # |               CALL                     1
        # |               LOAD_ATTR               11 (Path + NULL|self)
        # |               LOAD_GLOBAL             12 (__file__)
        # |               CALL                     1
        # |               LOAD_ATTR               15 (resolve + NULL|self)
        # |               CALL                     0
        # |               LOAD_ATTR               16 (parent)
        # |               LOAD_ATTR               16 (parent)
        # | 261           LOAD_CONST               3 ('config')
        # | 260           BINARY_OP               11 (/)
        # | 261           LOAD_CONST               4 ('project.yaml')
        # | 260           BINARY_OP               11 (/)
        # | 259           CALL                     1
        # | 261           LOAD_ATTR               19 (check + NULL|self)
        # |               LOAD_FAST_BORROW         3 (text)
        # |               CALL                     1
        # | 259           STORE_FAST               4 (r)
        # | 262           LOAD_FAST_BORROW         4 (r)
        # |               LOAD_ATTR               20 (findings)
        # |               GET_ITER
        # |       L1:     EXTENDED_ARG             1
        # |               FOR_ITER               269 (to L8)
        # |               STORE_FAST               5 (f)
        # | 263           LOAD_FAST_BORROW         5 (f)
        # |               LOAD_ATTR               22 (severity)
        # |               LOAD_CONST               5 ('warn')
        # |               COMPARE_OP              88 (bool(==))
        # |               POP_JUMP_IF_TRUE         3 (to L2)
        # |               NOT_TAKEN
        # |               JUMP_BACKWARD           23 (to L1)
        # |       L2:     LOAD_FAST_BORROW         5 (f)
        # |               LOAD_ATTR               24 (rule)
        # |               LOAD_CONST              14 (frozenset({'dialogue_ratio', 'style'}))
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE         3 (to L3)
        # |               NOT_TAKEN
        # |               JUMP_BACKWARD           42 (to L1)
        # | 264   L3:     LOAD_CONST               6 ('容差内')
        # |               STORE_FAST_LOAD_FAST   101 (@py_assert0, f)
        # |               LOAD_ATTR               26 (message)
        # |               STORE_FAST_LOAD_FAST   118 (@py_assert4, @py_assert0)
        # |               LOAD_FAST_BORROW         7 (@py_assert4)
        # |               CONTAINS_OP              0 (in)
        # |               STORE_FAST_LOAD_FAST   136 (@py_assert2, @py_assert2)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       199 (to L7)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             28 (@pytest_ar)
        # |               LOAD_ATTR               30 (_call_reprcompare)
        # |               PUSH_NULL
        # |               LOAD_CONST              15 (('in',))
        # |               LOAD_FAST_BORROW         8 (@py_assert2)
        # |               BUILD_TUPLE              1
        # |               LOAD_CONST              16 (('%(py1)s in %(py5)s\n{%(py5)s = %(py3)s.message\n}',))
        # |               LOAD_FAST_BORROW_LOAD_FAST_BORROW 103 (@py_assert0, @py_assert4)
        # |               BUILD_TUPLE              2
        # |               CALL                     4
        # |               LOAD_CONST               7 ('py1')
        # |               LOAD_GLOBAL             28 (@pytest_ar)
        # |               LOAD_ATTR               32 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_assert0)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py3')
        # |               LOAD_CONST               9 ('f')
        # |               LOAD_GLOBAL             34 (@py_builtins)
        # |               LOAD_ATTR               36 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             28 (@pytest_ar)
        # |               LOAD_ATTR               38 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (f)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L5)
        # |               NOT_TAKEN
        # |       L4:     LOAD_GLOBAL             28 (@pytest_ar)
        # |               LOAD_ATTR               32 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (f)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L6)
        # |       L5:     LOAD_CONST               9 ('f')
        # |       L6:     LOAD_CONST              10 ('py5')
        # |               LOAD_GLOBAL             28 (@pytest_ar)
        # |               LOAD_ATTR               32 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_assert4)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               9 (@py_format6)
        # |               LOAD_CONST              11 ('assert %(py7)s')
        # |               LOAD_CONST              12 ('py7')
        # |               LOAD_FAST_BORROW         9 (@py_format6)
        # |               BUILD_MAP                1
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST              10 (@py_format8)
        # |               LOAD_GLOBAL             41 (AssertionError + NULL)
        # |               LOAD_GLOBAL             28 (@pytest_ar)
        # |               LOAD_ATTR               42 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW        10 (@py_format8)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L7:     LOAD_CONST              13 (None)
        # |               COPY                     1
        # |               STORE_FAST               6 (@py_assert0)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST  135 (@py_assert2, @py_assert4)
        # |               EXTENDED_ARG             1
        # |               JUMP_BACKWARD          272 (to L1)
        # | 262   L8:     END_FOR
        # |               POP_ITER
        # |               LOAD_CONST              13 (None)
        # |               RETURN_VALUE


class TestStrayNotes:
    'TestStrayNotes'
    # ── 函数体（字节码重建见 BODY 段）──
    # | 267           RESUME                   0
    # |               LOAD_NAME                0 (__name__)
    # |               STORE_NAME               1 (__module__)
    # |               LOAD_CONST               0 ('TestStrayNotes')
    # |               STORE_NAME               2 (__qualname__)
    # |               LOAD_CONST               1 (267)
    # |               STORE_NAME               3 (__firstlineno__)
    # | 268           LOAD_CONST               2 ('第二道防线：writer 那边机械剥掉了，这里再拦一次。\n附言未必总以分隔线开头，但只要它以某种排版元素起头，这条就抓得住。')
    # |               STORE_NAME               4 (__doc__)
    # | 271           LOAD_CONST               3 (<code object test_separator_line_is_an_error at 0x7a74da4f00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 271>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               5 (test_separator_line_is_an_error)
    # | 277           LOAD_CONST               4 (<code object test_clean_chapter_has_none at 0x7a752c3900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 277>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               6 (test_clean_chapter_has_none)
    # | 281           LOAD_CONST               5 (<code object test_em_dash_paragraph_is_not_flagged at 0x7a752f4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 281>)
    # |               MAKE_FUNCTION
    # |               STORE_NAME               7 (test_em_dash_paragraph_is_not_flagged)
    # |               LOAD_CONST               6 (())
    # |               STORE_NAME               8 (__static_attributes__)
    # |               LOAD_CONST               7 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object test_separator_line_is_an_error at 0x7a74da4f00, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 271>:
    # | 271           RESUME                   0
    # | 272           LOAD_GLOBAL              1 (make_chapter + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               1 (('ch',))
    # |               CALL_KW                  1
    # |               LOAD_CONST               2 ('\n\n---\n\n缝合说明：我统一了年份。')
    # |               BINARY_OP                0 (+)
    # |               STORE_FAST               2 (text)
    # | 273           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                3 (check + NULL|self)
    # |               LOAD_FAST_BORROW         2 (text)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               3 (('expected_ch',))
    # |               CALL_KW                  2
    # |               STORE_FAST               3 (report)
    # | 274           LOAD_FAST_BORROW         3 (report)
    # |               LOAD_ATTR                4 (passed)
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       141 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               4 ('assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST               6 ('report')
    # |               LOAD_GLOBAL              6 (@py_builtins)
    # |               LOAD_ATTR                8 (locals)
    # |               PUSH_NULL
    # |               CALL                     0
    # |               CONTAINS_OP              0 (in)
    # |               POP_JUMP_IF_TRUE        29 (to L1)
    # |               NOT_TAKEN
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               12 (_should_repr_global_name)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (report)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       23 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (report)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               6 ('report')
    # |       L3:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               BUILD_MAP                2
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format4)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format4)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
    # | 275           LOAD_CONST               9 (<code object <genexpr> at 0x103d68470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 275>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         3 (report)
    # |               LOAD_ATTR               20 (errors)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               4 (@py_assert1)
    # |               LOAD_GLOBAL             23 (any + NULL)
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L8)
    # |               NOT_TAKEN
    # |               LOAD_CONST              10 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST              11 ('any')
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
    # |               LOAD_GLOBAL             22 (any)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L6)
    # |               NOT_TAKEN
    # |       L5:     LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL             22 (any)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L7)
    # |       L6:     LOAD_CONST              11 ('any')
    # |       L7:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST              12 ('py4')
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               14 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         5 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               7 (@py_format5)
    # |               LOAD_GLOBAL             17 (AssertionError + NULL)
    # |               LOAD_GLOBAL             10 (@pytest_ar)
    # |               LOAD_ATTR               18 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         7 (@py_format5)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L8:     LOAD_CONST               8 (None)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
    # |               LOAD_CONST               8 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x103d68470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 275>:
    # |  275           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                19 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (f, f)
    # |                LOAD_ATTR                0 (rule)
    # |                LOAD_CONST               0 ('stray_notes')
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
    # | Disassembly of <code object test_clean_chapter_has_none at 0x7a752c3900, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 277>:
    # | 277           RESUME                   0
    # | 278           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                1 (check + NULL|self)
    # |               LOAD_GLOBAL              3 (make_chapter + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               1 (('ch',))
    # |               CALL_KW                  1
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               2 (('expected_ch',))
    # |               CALL_KW                  2
    # |               STORE_FAST               2 (report)
    # | 279           LOAD_CONST               3 (<code object <genexpr> at 0x103d68690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 279>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         2 (report)
    # |               LOAD_ATTR                4 (findings)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_GLOBAL              7 (any + NULL)
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               4 ('assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST               6 ('any')
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
    # |               LOAD_GLOBAL              6 (any)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              6 (any)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               6 ('any')
    # |       L3:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x103d68690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 279>:
    # |  279           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                19 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (f, f)
    # |                LOAD_ATTR                0 (rule)
    # |                LOAD_CONST               0 ('stray_notes')
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
    # | Disassembly of <code object test_em_dash_paragraph_is_not_flagged at 0x7a752f4000, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 281>:
    # | 281           RESUME                   0
    # | 283           LOAD_FAST_BORROW         1 (gate)
    # |               LOAD_ATTR                1 (check + NULL|self)
    # |               LOAD_GLOBAL              3 (make_chapter + NULL)
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               1 (('ch',))
    # |               CALL_KW                  1
    # |               LOAD_SMALL_INT           1
    # |               LOAD_CONST               2 (('expected_ch',))
    # |               CALL_KW                  2
    # |               STORE_FAST               2 (report)
    # | 284           LOAD_CONST               3 (<code object <genexpr> at 0x103d688b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 284>)
    # |               MAKE_FUNCTION
    # |               LOAD_FAST_BORROW         2 (report)
    # |               LOAD_ATTR                4 (findings)
    # |               GET_ITER
    # |               CALL                     0
    # |               STORE_FAST               3 (@py_assert1)
    # |               LOAD_GLOBAL              7 (any + NULL)
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
    # |               TO_BOOL
    # |               UNARY_NOT
    # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
    # |               TO_BOOL
    # |               POP_JUMP_IF_TRUE       171 (to L4)
    # |               NOT_TAKEN
    # |               LOAD_CONST               4 ('assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
    # |               LOAD_CONST               5 ('py0')
    # |               LOAD_CONST               6 ('any')
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
    # |               LOAD_GLOBAL              6 (any)
    # |               CALL                     1
    # |               TO_BOOL
    # |               POP_JUMP_IF_FALSE       27 (to L2)
    # |               NOT_TAKEN
    # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_GLOBAL              6 (any)
    # |               CALL                     1
    # |               JUMP_FORWARD             1 (to L3)
    # |       L2:     LOAD_CONST               6 ('any')
    # |       L3:     LOAD_CONST               7 ('py2')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         3 (@py_assert1)
    # |               CALL                     1
    # |               LOAD_CONST               8 ('py4')
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               16 (_saferepr)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         4 (@py_assert3)
    # |               CALL                     1
    # |               BUILD_MAP                3
    # |               BINARY_OP                6 (%)
    # |               STORE_FAST               6 (@py_format6)
    # |               LOAD_GLOBAL             19 (AssertionError + NULL)
    # |               LOAD_GLOBAL             12 (@pytest_ar)
    # |               LOAD_ATTR               20 (_format_explanation)
    # |               PUSH_NULL
    # |               LOAD_FAST_BORROW         6 (@py_format6)
    # |               CALL                     1
    # |               CALL                     1
    # |               RAISE_VARARGS            1
    # |       L4:     LOAD_CONST               9 (None)
    # |               COPY                     1
    # |               STORE_FAST               3 (@py_assert1)
    # |               COPY                     1
    # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
    # |               LOAD_CONST               9 (None)
    # |               RETURN_VALUE
    # | Disassembly of <code object <genexpr> at 0x103d688b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 284>:
    # |  284           RETURN_GENERATOR
    # |                POP_TOP
    # |        L1:     RESUME                   0
    # |                LOAD_FAST                0 (.0)
    # |        L2:     FOR_ITER                19 (to L3)
    # |                STORE_FAST_LOAD_FAST    17 (f, f)
    # |                LOAD_ATTR                0 (rule)
    # |                LOAD_CONST               0 ('stray_notes')
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

    def test_separator_line_is_an_error(self, gate):
        '\n\n---\n\n缝合说明：我统一了年份。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 271           RESUME                   0
        # | 272           LOAD_GLOBAL              1 (make_chapter + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               1 (('ch',))
        # |               CALL_KW                  1
        # |               LOAD_CONST               2 ('\n\n---\n\n缝合说明：我统一了年份。')
        # |               BINARY_OP                0 (+)
        # |               STORE_FAST               2 (text)
        # | 273           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                3 (check + NULL|self)
        # |               LOAD_FAST_BORROW         2 (text)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               3 (('expected_ch',))
        # |               CALL_KW                  2
        # |               STORE_FAST               3 (report)
        # | 274           LOAD_FAST_BORROW         3 (report)
        # |               LOAD_ATTR                4 (passed)
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert1, @py_assert1)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       141 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               4 ('assert not %(py2)s\n{%(py2)s = %(py0)s.passed\n}')
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST               6 ('report')
        # |               LOAD_GLOBAL              6 (@py_builtins)
        # |               LOAD_ATTR                8 (locals)
        # |               PUSH_NULL
        # |               CALL                     0
        # |               CONTAINS_OP              0 (in)
        # |               POP_JUMP_IF_TRUE        29 (to L1)
        # |               NOT_TAKEN
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               12 (_should_repr_global_name)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (report)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       23 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (report)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               6 ('report')
        # |       L3:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               BUILD_MAP                2
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format4)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format4)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
        # | 275           LOAD_CONST               9 (<code object <genexpr> at 0x103d68470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 275>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         3 (report)
        # |               LOAD_ATTR               20 (errors)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               4 (@py_assert1)
        # |               LOAD_GLOBAL             23 (any + NULL)
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L8)
        # |               NOT_TAKEN
        # |               LOAD_CONST              10 ('assert %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST              11 ('any')
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
        # |               LOAD_GLOBAL             22 (any)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L6)
        # |               NOT_TAKEN
        # |       L5:     LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL             22 (any)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L7)
        # |       L6:     LOAD_CONST              11 ('any')
        # |       L7:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST              12 ('py4')
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               14 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         5 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               7 (@py_format5)
        # |               LOAD_GLOBAL             17 (AssertionError + NULL)
        # |               LOAD_GLOBAL             10 (@pytest_ar)
        # |               LOAD_ATTR               18 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         7 (@py_format5)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L8:     LOAD_CONST               8 (None)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert1, @py_assert3)
        # |               LOAD_CONST               8 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x103d68470, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 275>:
        # |  275           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                19 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (f, f)
        # |                LOAD_ATTR                0 (rule)
        # |                LOAD_CONST               0 ('stray_notes')
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

    def test_clean_chapter_has_none(self, gate):
        'assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 277           RESUME                   0
        # | 278           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                1 (check + NULL|self)
        # |               LOAD_GLOBAL              3 (make_chapter + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               1 (('ch',))
        # |               CALL_KW                  1
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               2 (('expected_ch',))
        # |               CALL_KW                  2
        # |               STORE_FAST               2 (report)
        # | 279           LOAD_CONST               3 (<code object <genexpr> at 0x103d68690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 279>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         2 (report)
        # |               LOAD_ATTR                4 (findings)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_GLOBAL              7 (any + NULL)
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               4 ('assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST               6 ('any')
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
        # |               LOAD_GLOBAL              6 (any)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              6 (any)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               6 ('any')
        # |       L3:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x103d68690, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 279>:
        # |  279           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                19 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (f, f)
        # |                LOAD_ATTR                0 (rule)
        # |                LOAD_CONST               0 ('stray_notes')
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

    def test_em_dash_paragraph_is_not_flagged(self, gate):
        '整段只有一个破折号的写法很少见但合法，不该误伤。'
        # ── 函数体（字节码重建见 BODY 段）──
        # | 281           RESUME                   0
        # | 283           LOAD_FAST_BORROW         1 (gate)
        # |               LOAD_ATTR                1 (check + NULL|self)
        # |               LOAD_GLOBAL              3 (make_chapter + NULL)
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               1 (('ch',))
        # |               CALL_KW                  1
        # |               LOAD_SMALL_INT           1
        # |               LOAD_CONST               2 (('expected_ch',))
        # |               CALL_KW                  2
        # |               STORE_FAST               2 (report)
        # | 284           LOAD_CONST               3 (<code object <genexpr> at 0x103d688b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 284>)
        # |               MAKE_FUNCTION
        # |               LOAD_FAST_BORROW         2 (report)
        # |               LOAD_ATTR                4 (findings)
        # |               GET_ITER
        # |               CALL                     0
        # |               STORE_FAST               3 (@py_assert1)
        # |               LOAD_GLOBAL              7 (any + NULL)
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               STORE_FAST_LOAD_FAST    68 (@py_assert3, @py_assert3)
        # |               TO_BOOL
        # |               UNARY_NOT
        # |               STORE_FAST_LOAD_FAST    85 (@py_assert5, @py_assert5)
        # |               TO_BOOL
        # |               POP_JUMP_IF_TRUE       171 (to L4)
        # |               NOT_TAKEN
        # |               LOAD_CONST               4 ('assert not %(py4)s\n{%(py4)s = %(py0)s(%(py2)s)\n}')
        # |               LOAD_CONST               5 ('py0')
        # |               LOAD_CONST               6 ('any')
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
        # |               LOAD_GLOBAL              6 (any)
        # |               CALL                     1
        # |               TO_BOOL
        # |               POP_JUMP_IF_FALSE       27 (to L2)
        # |               NOT_TAKEN
        # |       L1:     LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_GLOBAL              6 (any)
        # |               CALL                     1
        # |               JUMP_FORWARD             1 (to L3)
        # |       L2:     LOAD_CONST               6 ('any')
        # |       L3:     LOAD_CONST               7 ('py2')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         3 (@py_assert1)
        # |               CALL                     1
        # |               LOAD_CONST               8 ('py4')
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               16 (_saferepr)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         4 (@py_assert3)
        # |               CALL                     1
        # |               BUILD_MAP                3
        # |               BINARY_OP                6 (%)
        # |               STORE_FAST               6 (@py_format6)
        # |               LOAD_GLOBAL             19 (AssertionError + NULL)
        # |               LOAD_GLOBAL             12 (@pytest_ar)
        # |               LOAD_ATTR               20 (_format_explanation)
        # |               PUSH_NULL
        # |               LOAD_FAST_BORROW         6 (@py_format6)
        # |               CALL                     1
        # |               CALL                     1
        # |               RAISE_VARARGS            1
        # |       L4:     LOAD_CONST               9 (None)
        # |               COPY                     1
        # |               STORE_FAST               3 (@py_assert1)
        # |               COPY                     1
        # |               STORE_FAST_STORE_FAST   69 (@py_assert3, @py_assert5)
        # |               LOAD_CONST               9 (None)
        # |               RETURN_VALUE
        # | Disassembly of <code object <genexpr> at 0x103d688b0, file "/Users/weizihang/Desktop/agent制作/novel_agent/tests/test_gate.py", line 284>:
        # |  284           RETURN_GENERATOR
        # |                POP_TOP
        # |        L1:     RESUME                   0
        # |                LOAD_FAST                0 (.0)
        # |        L2:     FOR_ITER                19 (to L3)
        # |                STORE_FAST_LOAD_FAST    17 (f, f)
        # |                LOAD_ATTR                0 (rule)
        # |                LOAD_CONST               0 ('stray_notes')
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

