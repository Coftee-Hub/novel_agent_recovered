# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/agents/writer.py
# 来源   : writer.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = 'agent_write —— 逐场景生成正文，再缝合成章。\n\n分场景写而不是整章写：中文长文本生成的通病是中后段节奏塌陷、人设漂移，\n一次 800-1500 字的输出稳得多。代价是要额外一道缝合。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'agent_write —— 逐场景生成正文，再缝合成章。\n\n分场景写而不是整章写：中文长文本生成的通病是中后段节奏塌陷、人设漂移，\n一次 800-1500 字的输出稳得多。代价是要额外一道缝合。\n',
    11: 'L0',
    12: '本场为 L0：无身体接触，靠对话、视线、心理与克制的肢体距离推张力。',
    13: 'L1',
    14: '本场为 L1：可以有亲密场景，但在关键处转场留白，不要写下去。',
    15: 'L2',
    16: '本场为 L2：可以展开触觉、温度、呼吸的感官描写，到性行为本身收住。',
    18: 'Writer',
    20: 'StitchFailed',
    22: 'Stitcher',
    23: '^\\s*(?:-{3,}|\\*{3,}|_{3,})\\s*$',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Writer', 0): 'Writer',
    ('Writer', 1): 'prev_tail_chars',
    ('Writer', 3): 'summary_cap',
    ('Writer', 12): 'prev_text',
    ('Writer', 14): 'rag_snippets',
    ('Writer', 20): 'rag',
    ('Writer', 21): 'on_scene',
    ('Writer', 22): 'already',
    ('__annotate__', 1): 'client',
    ('__annotate__', 2): 'LLMClient',
    ('__annotate__', 3): 'skills_dir',
    ('__annotate__', 4): 'str | Path',
    ('__annotate__', 5): 'prev_tail_chars',
    ('__annotate__', 6): 'int',
    ('__annotate__', 7): 'summary_cap',
    ('__annotate__', 8): 'return',
    ('__annotate__', 9): 'None',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('system_core', 0): '全书不变。刻意不含 character_design / romance_beats / campus_to_career\n—— 那些是设计期技能，writer 拿到的是它们的产物。',
    ('system_core', 1): '\n\n---\n\n',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('bible_layer', 0): '全量人物卡与设定。\n\n刻意不按出场人物裁剪：裁剪会让 bible 随场景变化，击穿缓存前缀，\n而省下的那点 token 远不值这个代价。场景规格里已写明谁在场。\n',
    ('bible_layer', 2): '<设定集>\n',
    ('bible_layer', 3): '\n</设定集>',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'outline',
    ('__annotate__', 4): 'ChapterOutline',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'str',
    ('volume_layer', 0): '卷内稳定的部分。本章细纲也放这里 —— 同一章的各场景共享它。',
    ('volume_layer', 5): '<往卷梗概>\n',
    ('volume_layer', 6): '\n</往卷梗概>',
    ('volume_layer', 9): '<前情提要>\n',
    ('volume_layer', 10): '\n</前情提要>',
    ('volume_layer', 12): '<本章安排>\n第 ',
    ('volume_layer', 13): ' 章《',
    ('volume_layer', 14): '》\n本章意图：',
    ('volume_layer', 15): '\n场景清单（你每次只写其中一个）：\n',
    ('volume_layer', 16): '\n</本章安排>',
    ('<genexpr>', 0): '- 第 ',
    ('<genexpr>', 1): ' 卷（第 ',
    ('<genexpr>', 2): '-',
    ('<genexpr>', 3): ' 章）：',
    ('<genexpr>', 0): '- 第 ',
    ('<genexpr>', 1): ' 章 ',
    ('<genexpr>', 2): '：',
    ('<genexpr>', 1): '. ',
    ('<genexpr>', 2): '｜',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'outline',
    ('__annotate__', 4): 'ChapterOutline',
    ('__annotate__', 5): 'scene',
    ('__annotate__', 6): 'SceneSpec',
    ('__annotate__', 7): 'prev_text',
    ('__annotate__', 8): 'str',
    ('__annotate__', 9): 'rag_snippets',
    ('__annotate__', 10): 'list[str] | None',
    ('__annotate__', 11): 'return',
    ('write_scene', 0): '、',
    ('write_scene', 2): '写场景 **',
    ('write_scene', 3): '**，目标 ',
    ('write_scene', 4): ' 字。',
    ('write_scene', 6): '- 地点：',
    ('write_scene', 7): '- 时间：',
    ('write_scene', 8): '- 在场：',
    ('write_scene', 9): '- 这一场要达成：',
    ('write_scene', 10): '- **情绪位移：',
    ('write_scene', 11): ' → ',
    ('write_scene', 12): '**',
    ('write_scene', 13): '- 节拍类型：',
    ('write_scene', 14): '必须出现（自然长进情节，不要生硬塞入）：',
    ('write_scene', 15): '- ',
    ('write_scene', 16): '**禁止出现**：',
    ('write_scene', 17): '只输出正文，不要标题，不要任何说明文字。',
    ('write_scene', 18): 'writer',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'outline',
    ('__annotate__', 4): 'ChapterOutline',
    ('__annotate__', 5): 'scene',
    ('__annotate__', 6): 'SceneSpec',
    ('__annotate__', 7): 'previous',
    ('__annotate__', 8): 'str',
    ('__annotate__', 9): 'problems',
    ('__annotate__', 10): 'list[str]',
    ('__annotate__', 11): 'prev_text',
    ('__annotate__', 12): 'return',
    ('revise_scene', 0): '按意见重写一个场景。\n\n给出原文而不是从头写：修订的目标是修掉具体问题，不是碰运气重抽一次。\n整章重写会把本来合格的场景也搅掉，而且下一轮可能出新问题，\n修订环就永远收敛不了。\n',
    ('revise_scene', 3): '重写场景 **',
    ('revise_scene', 4): '**，目标 ',
    ('revise_scene', 5): ' 字。\n\n下面是这一场的原文和它的问题。**只修问题，其余保持原样** —— 没被点到的段落、对话、细节都要保留下来。\n\n要修的问题：\n',
    ('revise_scene', 6): '\n\n这一场仍然要完成的情绪位移：',
    ('revise_scene', 7): ' → ',
    ('revise_scene', 8): '\n这一场要达成：',
    ('revise_scene', 9): '\n\n<原文>\n',
    ('revise_scene', 10): '\n</原文>\n\n只输出重写后的正文，不要标题，不要说明改了什么。',
    ('revise_scene', 11): 'writer',
    ('<genexpr>', 0): '- ',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'outline',
    ('__annotate__', 4): 'ChapterOutline',
    ('__annotate__', 5): 'rag',
    ('__annotate__', 6): 'dict[str, list[str]] | None',
    ('__annotate__', 7): 'already',
    ('__annotate__', 8): 'list[str] | None',
    ('__annotate__', 9): 'return',
    ('__annotate__', 10): 'list[str]',
    ('write_chapter_scenes', 0): '按顺序写完一章的所有场景。\n\n必须串行：每一场都要看到上一场的结尾才能接得上。\n\n`on_scene` 在每一场**刚写完**时回调一次。一场正文是花掉的钱和几分钟\n等待，后面任何一步抛异常（实测：缝合时上游 403）都会把整章草稿连同\n已写好的场景一起丢掉 —— 回调让调用方能先把它存下来。\n\n`already` 是上次崩之前已经写好的前几场（按顺序）。崩点几乎总在后面，\n草稿就是场景列表的一个前缀，接着往下写即可 —— 已经付过钱的场景\n不重写，也不重复触发 `on_scene`（盘上那份就是它自己）。\n',
    ('write_chapter_scenes', 1): '第 ',
    ('write_chapter_scenes', 2): ' 章只有 ',
    ('write_chapter_scenes', 3): ' 场，却给了 ',
    ('write_chapter_scenes', 4): ' 段草稿 —— 细纲和草稿对不上，多半是细纲重出过。',
    ('StitchFailed', 0): 'StitchFailed',
    ('StitchFailed', 1): '缝合没做成，但**附带一份机械拼接的兜底稿**。\n\n调用方几乎总该用上 `fallback`：场景正文是花过钱、检查过的东西，\n没缝上不等于没写出来。实测第 3 章四次尝试有三次死在缝合，\n每次都是三场好正文换来零产出。\n\n但兜底稿不是成稿 —— 它没打磨过接缝、没处理章末钩子，所以带着它的那一章\n一律判为不通过，落 needs_human 由人看。\n',
    ('__annotate__', 1): 'reason',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'fallback',
    ('__annotate__', 4): 'return',
    ('__annotate__', 5): 'None',
    ('Stitcher', 0): 'Stitcher',
    ('Stitcher', 1): '把分开写的场景缝合成一章。只调接缝，不重写内容。',
    ('Stitcher', 7): 'tries',
    ('Stitcher', 12): 'retry',
    ('__annotate__', 1): 'client',
    ('__annotate__', 2): 'LLMClient',
    ('__annotate__', 3): 'skills_dir',
    ('__annotate__', 4): 'str | Path',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('system_core', 0): '\n\n---\n\n',
    ('__annotate__', 1): 'outline',
    ('__annotate__', 2): 'ChapterOutline',
    ('__annotate__', 3): 'scenes',
    ('__annotate__', 4): 'list[str]',
    ('__annotate__', 5): 'tries',
    ('__annotate__', 6): 'int',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'str',
    ('stitch', 0): '缝合，并检查结果是否完整。\n\n实测一次 stitcher 只吐出 87 字就 end_turn 收工（场景总和 4,491 字），\n正文停在半个词上。stop_reason 不是 length，所以光看它发现不了 ——\n必须比对字数并检查结尾标点。\n',
    ('stitch', 2): '没跑成',
    ('stitch', 3): '，重试',
    ('stitch', 6): ': ',
    ('stitch', 7): '    ! 缝合调用失败（',
    ('stitch', 9): '）',
    ('stitch', 13): '只产出 ',
    ('stitch', 14): ' 字，低于场景总和 ',
    ('stitch', 15): ' 字的 ',
    ('stitch', 16): '.0%',
    ('stitch', 17): '，或结尾被截断（',
    ('stitch', 18): '    ! 缝合结果异常（',
    ('stitch', 19): ' 字，场景总和 ',
    ('stitch', 20): ' 字）',
    ('stitch', 21): '缝合失败：',
    ('__annotate__', 1): 'outline',
    ('__annotate__', 2): 'ChapterOutline',
    ('__annotate__', 3): 'scenes',
    ('__annotate__', 4): 'list[str]',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'str',
    ('mechanical', 0): '不调模型的兜底拼接：补标题，场景之间空行分隔。\n\n它交出的东西**不是成稿**：接缝没打磨、重复没删、章末钩子没处理。\n它的意义只有一个 —— 让人能看到"正文是好的，只是没缝上"，\n而不是面对一句"第 3 章异常"和三个孤立的草稿文件。\n',
    ('mechanical', 3): '## 第',
    ('mechanical', 4): '章 ',
    ('__annotate__', 1): 'outline',
    ('__annotate__', 2): 'ChapterOutline',
    ('__annotate__', 3): 'scenes',
    ('__annotate__', 4): 'list[str]',
    ('__annotate__', 5): 'retry',
    ('__annotate__', 6): 'bool',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'str',
    ('_stitch_once', 2): '把下面 ',
    ('_stitch_once', 3): ' 个场景缝合成第 ',
    ('_stitch_once', 4): ' 章。\n\n- 标题：',
    ('_stitch_once', 5): '，输出为 `## 第',
    ('_stitch_once', 6): '章 ',
    ('_stitch_once', 7): '`\n- 章末钩子：',
    ('_stitch_once', 8): '\n- 全章目标 ',
    ('_stitch_once', 9): ' 字，缝合后不要偏离太多\n\n记住：只调接缝、删重复、处理结尾钩子。情节、对话、人物行为保持原样。\n\n',
    ('_stitch_once', 10): '\n\n注意：上一次的输出严重不完整，只产出了很少的内容就停了。这次务必把每个场景的正文都保留下来，从头到尾输出完整的一章。',
    ('_stitch_once', 11): 'stitcher',
    ('<genexpr>', 0): '<场景 ',
    ('<genexpr>', 1): '｜',
    ('<genexpr>', 2): '→',
    ('<genexpr>', 3): '>\n',
    ('<genexpr>', 4): '\n</场景 ',
    ('<genexpr>', 5): '>',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('_postprocess', 0): '生成结果的机械修正 —— 确定性的、不动内容的那几样。\n\n顺序要紧：**先剥说明再规范标点**。`normalize_punctuation` 会把 `--` 换成\n`——`，先规范化的话 `---` 分隔线就成了 `——-`，剥离规则再也匹配不上。\n',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('_normalize_quotes', 0): 'ASCII 双引号按行配对转成全角。\n\n实测两次事故都出在这上面：一轮修订后整章冒出 46 处 `"`，gate 全判成\n标点错误，整轮修订白烧；更早还有一次「整章对话占比 0.0%」的悬案 ——\n对话占比的统计只认全角引号，模型一吐 ASCII 引号，整章就被判成"没有对话"，\n于是三个场景全部重写，而正文其实是好的。\n\n这是纯机械缺陷，不该让修订环去救 —— 它一轮要花三次 writer 调用。\n\n**配对**而不是简单替换：`"` 有开有合，一律换成 `“` 会得到 `“内容“`。\n按行重置配对状态：一行里引号不闭合是常态（对话跨段），跨行累计会把\n后面所有引号的开合弄反。单引号不动 —— 英文缩写 don\'t 里的撇号会被误伤。\n',
    ('_normalize_quotes', 3): '"',
    ('_normalize_quotes', 4): '“',
    ('_normalize_quotes', 5): '”',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('_strip_trailing_notes', 0): '剥掉正文末尾的"缝合说明"。\n\n实测：stitcher 三次缝合三次都在正文后面加了一段 `---` + 改动说明\n（「年份原本三个场景各说一套…我按 s2 统一为…」）。它写的内容其实有用，\n但**输出会被原样当作成稿存盘**，于是说明变成了小说的一部分。\n\n更麻烦的是这种缺陷修订环修不掉：重写场景改变不了 stitcher 的习惯，\n每重缝一次就再加一遍，两轮上限白烧。所以在这里机械剥掉。\n\n合格成稿里不该出现独立的分隔线 —— 第 1、2 章各 0 处，三个缝合稿各 1 处。\n',
    ('_strip_trailing_notes', 3): '    ! 剥掉正文末尾的说明文字（',
    ('_strip_trailing_notes', 4): ' 字，第 ',
    ('_strip_trailing_notes', 5): ' 行起）',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'bool',
    ('_ends_cleanly', 0): '结尾是否落在完整句上。截断的生成会停在半个词或逗号上。',
    ('_ends_cleanly', 1): '。！？…”』」',
}

# ───────────── 重建的源码（签名/docstring 原样，函数体由反汇编还原）─────────────
import re

from ..corpus.ingest import normalize_punctuation
from ..llm.client import LLMClient
from ..llm.prompt_builder import Prompt
from ..skills import SkillLibrary, WRITER_SKILLS  # TODO(重建): 需确认 import —— WRITER_SKILLS 确切来源（skills.py 或 prompts.py）
from ..state.bible import render as render_bible
from ..state.schema import StoryState
from .prompts import STITCHER_ROLE, WRITER_ROLE
from .schemas import ChapterOutline, SceneSpec

# 亲密档位 → 提示语。write_scene 里按 scene.intimacy_level 查表，查不到给空串。
_INTIMACY_HINT = {
    'L0': '本场为 L0：无身体接触，靠对话、视线、心理与克制的肢体距离推张力。',
    'L1': '本场为 L1：可以有亲密场景，但在关键处转场留白，不要写下去。',
    'L2': '本场为 L2：可以展开触觉、温度、呼吸的感官描写，到性行为本身收住。',
}

# 独立分隔线的匹配器：--- / *** / ___
SEPARATOR = re.compile(r'^\s*(?:-{3,}|\*{3,}|_{3,})\s*$')


class Writer:
    'Writer'

    def __init__(self, client, skills_dir, *, prev_tail_chars=300, summary_cap=24):
        pass  # 无 docstring
        self.client = client
        self.skills = SkillLibrary(skills_dir)
        self.prev_tail_chars = prev_tail_chars
        self.summary_cap = summary_cap

    def system_core(self):
        '全书不变。刻意不含 character_design / romance_beats / campus_to_career\n—— 那些是设计期技能，writer 拿到的是它们的产物。'
        return f'{WRITER_ROLE}\n\n---\n\n{self.skills.compose(WRITER_SKILLS, strict=False)}'

    def bible_layer(self, state):
        '全量人物卡与设定。\n\n刻意不按出场人物裁剪：裁剪会让 bible 随场景变化，击穿缓存前缀，\n而省下的那点 token 远不值这个代价。场景规格里已写明谁在场。\n'
        if not state.characters:
            return ''
        return f'<设定集>\n{render_bible(state)}\n</设定集>'

    def volume_layer(self, state, outline):
        '卷内稳定的部分。本章细纲也放这里 —— 同一章的各场景共享它。'
        parts = []
        if state.volume_summaries:
            rows = '\n'.join(
                f'- 第 {v.volume} 卷（第 {v.ch_start}-{v.ch_end} 章）：{v.summary}'
                for v in sorted(state.volume_summaries, key=lambda x: x.volume)
            )
            parts.append(f'<往卷梗概>\n{rows}\n</往卷梗概>')
        live = state.live_summaries(cap=self.summary_cap)
        if live:
            rows = '\n'.join(
                f'- 第 {s.ch} 章 {s.title}：{s.summary}'
                for s in live
            )
            parts.append(f'<前情提要>\n{rows}\n</前情提要>')
        scene_list = '\n'.join(
            f'  {i}. {s.id}｜{s.where}｜{s.goal}'
            for i, s in enumerate(outline.scenes, 1)
        )
        parts.append(
            f'<本章安排>\n第 {outline.ch} 章《{outline.title}》\n本章意图：{outline.intent}\n'
            f'场景清单（你每次只写其中一个）：\n{scene_list}\n</本章安排>'
        )
        return '\n\n'.join(parts)

    def write_scene(self, state, outline, scene, *, prev_text, rag_snippets):
        '、'
        present = '、'.join(
            state.character(cid).name if state.character(cid) else cid
            for cid in scene.present
        )
        lines = [
            f'写场景 **{scene.id}**，目标 {scene.target_words} 字。',
            '',
            f'- 地点：{scene.where}',
            f'- 时间：{scene.when}',
            f'- 在场：{present}',
            f'- 这一场要达成：{scene.goal}',
            f'- **情绪位移：{scene.entry_emotion} → {scene.exit_emotion}**',
            f'- 节拍类型：{scene.beat_type}',
            _INTIMACY_HINT.get(scene.intimacy_level, ''),
        ]
        if scene.must_include:
            lines += ['', '必须出现（自然长进情节，不要生硬塞入）：']
            lines += [f'- {x}' for x in scene.must_include]
        if scene.must_not:
            lines += ['', '**禁止出现**：']
            lines += [f'- {x}' for x in scene.must_not]
        lines += ['', '只输出正文，不要标题，不要任何说明文字。']
        result = self.client.complete(
            'writer',
            Prompt(
                system_core=self.system_core(),
                bible=self.bible_layer(state),
                volume=self.volume_layer(state, outline),
                rag_snippets=rag_snippets or [],
                prev_tail=prev_text[-self.prev_tail_chars:] if prev_text else '',
                instruction='\n'.join(x for x in lines if x is not None),
            ),
        )
        return _postprocess(result.text)

    def revise_scene(self, state, outline, scene, previous, problems, *, prev_text):
        '按意见重写一个场景。\n\n给出原文而不是从头写：修订的目标是修掉具体问题，不是碰运气重抽一次。\n整章重写会把本来合格的场景也搅掉，而且下一轮可能出新问题，\n修订环就永远收敛不了。\n'
        issues = '\n'.join(f'- {p}' for p in problems)
        instruction = (
            f'重写场景 **{scene.id}**，目标 {scene.target_words} 字。\n\n'
            f'下面是这一场的原文和它的问题。**只修问题，其余保持原样** —— 没被点到的段落、对话、细节都要保留下来。\n\n'
            f'要修的问题：\n{issues}\n\n'
            f'这一场仍然要完成的情绪位移：{scene.entry_emotion} → {scene.exit_emotion}\n'
            f'这一场要达成：{scene.goal}\n\n'
            f'<原文>\n{previous}\n</原文>\n\n只输出重写后的正文，不要标题，不要说明改了什么。'
        )
        result = self.client.complete(
            'writer',
            Prompt(
                system_core=self.system_core(),
                bible=self.bible_layer(state),
                volume=self.volume_layer(state, outline),
                prev_tail=prev_text[-self.prev_tail_chars:] if prev_text else '',
                instruction=instruction,
            ),
        )
        return _postprocess(result.text)

    def write_chapter_scenes(self, state, outline, *, rag, on_scene, already):
        '按顺序写完一章的所有场景。\n\n必须串行：每一场都要看到上一场的结尾才能接得上。\n\n`on_scene` 在每一场**刚写完**时回调一次。一场正文是花掉的钱和几分钟\n等待，后面任何一步抛异常（实测：缝合时上游 403）都会把整章草稿连同\n已写好的场景一起丢掉 —— 回调让调用方能先把它存下来。\n\n`already` 是上次崩之前已经写好的前几场（按顺序）。崩点几乎总在后面，\n草稿就是场景列表的一个前缀，接着往下写即可 —— 已经付过钱的场景\n不重写，也不重复触发 `on_scene`（盘上那份就是它自己）。\n'
        written = list(already or [])
        if len(written) > len(outline.scenes):
            raise ValueError(
                f'第 {outline.ch} 章只有 {len(outline.scenes)} 场，却给了 {len(written)} 段草稿 —— 细纲和草稿对不上，多半是细纲重出过。'
            )
        for scene in outline.scenes[len(written):]:
            text = self.write_scene(
                state, outline, scene,
                prev_text=written[-1] if written else '',
                rag_snippets=(rag or {}).get(scene.id),
            )
            written.append(text)
            if on_scene is not None:
                on_scene(scene, text)
        return written


class StitchFailed(Exception):
    'StitchFailed'

    def __init__(self, reason, fallback):
        pass  # 无 docstring
        super().__init__(reason)
        self.fallback = fallback


class Stitcher:
    'Stitcher'

    def __init__(self, client, skills_dir):
        pass  # 无 docstring
        self.client = client
        self.skills = SkillLibrary(skills_dir)

    def system_core(self):
        '\n\n---\n\n'
        return f'{STITCHER_ROLE}\n\n---\n\n{self.skills.compose(WRITER_SKILLS, strict=False)}'

    MIN_KEEP_RATIO = 0.6

    def stitch(self, outline, scenes, *, tries=2):
        '缝合，并检查结果是否完整。\n\n实测一次 stitcher 只吐出 87 字就 end_turn 收工（场景总和 4,491 字），\n正文停在半个词上。stop_reason 不是 length，所以光看它发现不了 ——\n必须比对字数并检查结尾标点。\n'
        raw_total = sum(len(s) for s in scenes)
        floor = int(raw_total * self.MIN_KEEP_RATIO)
        why = '没跑成'
        for attempt in range(tries):
            more = '，重试' if attempt + 1 < tries else ''
            try:
                text = self._stitch_once(outline, scenes, retry=attempt > 0)
            except Exception as exc:
                why = f'{type(exc).__name__}: {exc}'
                print(f'    ! 缝合调用失败（{why[:80]}）{more}', flush=True)
                continue
            if len(text) >= floor and _ends_cleanly(text):
                return text
            why = (
                f'只产出 {len(text)} 字，低于场景总和 {raw_total} 字的 '
                f'{self.MIN_KEEP_RATIO:.0%}，或结尾被截断（{text[-30:]!r}）'
            )
            print(f'    ! 缝合结果异常（{len(text)} 字，场景总和 {raw_total} 字）{more}', flush=True)
        raise StitchFailed(f'缝合失败：{why}', self.mechanical(outline, scenes))

    def mechanical(self, outline, scenes):
        '不调模型的兜底拼接：补标题，场景之间空行分隔。\n\n它交出的东西**不是成稿**：接缝没打磨、重复没删、章末钩子没处理。\n它的意义只有一个 —— 让人能看到"正文是好的，只是没缝上"，\n而不是面对一句"第 3 章异常"和三个孤立的草稿文件。\n'
        body = '\n\n'.join(s.strip() for s in scenes if s.strip())
        return f'## 第{outline.ch}章 {outline.title}\n\n{body}'.strip()

    def _stitch_once(self, outline, scenes, *, retry=False):
        '把下面 '
        blocks = '\n\n'.join(
            f'<场景 {spec.id}｜{spec.where}｜{spec.entry_emotion}→{spec.exit_emotion}>\n{text}\n</场景 {spec.id}>'
            for spec, text in zip(outline.scenes, scenes)
        )
        instruction = (
            f'把下面 {len(scenes)} 个场景缝合成第 {outline.ch} 章。\n\n- 标题：{outline.title}，输出为 `## 第{outline.ch}章 {outline.title}`\n'
            f'- 章末钩子：{outline.hook}\n'
            f'- 全章目标 {outline.target_words} 字，缝合后不要偏离太多\n\n'
            f'记住：只调接缝、删重复、处理结尾钩子。情节、对话、人物行为保持原样。\n\n'
            f'{blocks}'
        )
        if retry:
            instruction += '\n\n注意：上一次的输出严重不完整，只产出了很少的内容就停了。这次务必把每个场景的正文都保留下来，从头到尾输出完整的一章。'
        result = self.client.complete(
            'stitcher',
            Prompt(
                system_core=self.system_core(),
                instruction=instruction,
            ),
        )
        return _postprocess(result.text)


def _postprocess(text):
    '生成结果的机械修正 —— 确定性的、不动内容的那几样。\n\n顺序要紧：**先剥说明再规范标点**。`normalize_punctuation` 会把 `--` 换成\n`——`，先规范化的话 `---` 分隔线就成了 `——-`，剥离规则再也匹配不上。\n'
    return normalize_punctuation(_normalize_quotes(_strip_trailing_notes(text.strip())))


def _normalize_quotes(text):
    'ASCII 双引号按行配对转成全角。\n\n实测两次事故都出在这上面：一轮修订后整章冒出 46 处 `"`，gate 全判成\n标点错误，整轮修订白烧；更早还有一次「整章对话占比 0.0%」的悬案 ——\n对话占比的统计只认全角引号，模型一吐 ASCII 引号，整章就被判成"没有对话"，\n于是三个场景全部重写，而正文其实是好的。\n\n这是纯机械缺陷，不该让修订环去救 —— 它一轮要花三次 writer 调用。\n\n**配对**而不是简单替换：`"` 有开有合，一律换成 `“` 会得到 `“内容“`。\n按行重置配对状态：一行里引号不闭合是常态（对话跨段），跨行累计会把\n后面所有引号的开合弄反。单引号不动 —— 英文缩写 don\'t 里的撇号会被误伤。\n'
    out = []
    for line in text.split('\n'):
        chars = []
        opening = True
        for ch in line:
            if ch == '"':
                chars.append('“' if opening else '”')
                opening = not opening
            else:
                chars.append(ch)
        out.append(''.join(chars))
    return '\n'.join(out)


def _strip_trailing_notes(text):
    '剥掉正文末尾的"缝合说明"。\n\n实测：stitcher 三次缝合三次都在正文后面加了一段 `---` + 改动说明\n（「年份原本三个场景各说一套…我按 s2 统一为…」）。它写的内容其实有用，\n但**输出会被原样当作成稿存盘**，于是说明变成了小说的一部分。\n\n更麻烦的是这种缺陷修订环修不掉：重写场景改变不了 stitcher 的习惯，\n每重缝一次就再加一遍，两轮上限白烧。所以在这里机械剥掉。\n\n合格成稿里不该出现独立的分隔线 —— 第 1、2 章各 0 处，三个缝合稿各 1 处。\n'
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if i and SEPARATOR.match(line):
            dropped = len('\n'.join(lines[:i]))
            print(f'    ! 剥掉正文末尾的说明文字（{dropped} 字，第 {i + 1} 行起）', flush=True)
            return '\n'.join(lines[:i]).rstrip()
    return text


def _ends_cleanly(text):
    '结尾是否落在完整句上。截断的生成会停在半个词或逗号上。'
    tail = text.rstrip()
    return bool(tail) and tail[-1] in '。！？…”』」'
