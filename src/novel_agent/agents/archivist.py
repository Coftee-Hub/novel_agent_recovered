# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/agents/archivist.py
# 来源   : archivist.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '归档 —— 把一章读成结构化的状态增量。\n\n没有它，state 永远停在第 0 章：第 2 章不会知道第 1 章发生过什么，\n人物关系不会推进，埋下的伏笔不会被记住，用过的桥段会被重复使用。\n\n它只输出**增量 patch**，合并逻辑全在 Python 侧（state/store.py）。\n让模型直接重写整个 state 是本项目最容易出的事故 —— 几十章后字段会\n静默漂移、丢失。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '归档 —— 把一章读成结构化的状态增量。\n\n没有它，state 永远停在第 0 章：第 2 章不会知道第 1 章发生过什么，\n人物关系不会推进，埋下的伏笔不会被记住，用过的桥段会被重复使用。\n\n它只输出**增量 patch**，合并逻辑全在 Python 侧（state/store.py）。\n让模型直接重写整个 state 是本项目最容易出的事故 —— 几十章后字段会\n静默漂移、丢失。\n',
    6: '你是这部小说的记录员。你读完一章，把其中会影响后续章节的信息提炼出来。\n\n## 你要记什么\n\n**只记会被后面用到的东西。** 判断标准：如果第 50 章的作者需要知道这件事\n才能写对，就记；如果只是这一章内部的细节，不记。\n\n- **章节摘要**：一到两句。写发生了什么、关系变到哪一步，不要写氛围和评价。\n- **关系变化**：阶段是否推进、张力来源是否改变、好感度大致到什么程度。\n  没有实质变化就不要为了填而填。\n- **情感债**：这一章埋下的误会、秘密、承诺、未说出口的话、有意义的物件。\n  **每一条都必须给出到期章号** —— 没有到期章的伏笔在长篇里必然被遗忘。\n  同时记录这一章回收了哪些既有的债。\n- **已用桥段**：这一章用了什么处理方式（如「雨中共伞」「醉酒告白」）。\n  记下来是为了让后面的章节避开，所以命名要能被认出来。\n- **时间线**：这一章发生在什么时候、什么地点、谁在场。\n- **新人物**：只记有名字且后面还会出现的。路人不记。\n\n## 你不能做的\n\n**不要修改人物的性格内核、说话习惯、核心创伤、价值观底线。**\n这四项跨阶段恒定，是全书的地基。人物的处境、目标、身份可以变化，\n但他不能变成另一个人。你的输出格式里根本没有修改它们的位置，这是有意的。\n\n## 关于摘要\n\n摘要会被后面几十章反复读到，所以要**精确而不是生动**。\n\n不合格：「这一章两人的关系有了微妙的变化，气氛暧昧。」\n合格：「她接下了没人肯做的校对活，没有问工期；他被指派画图，翻了日程本\n       但一项也没划掉。两人在筹备会上第一次同框，没有说话。」\n',
    7: '你是这部小说的记录员。一卷写完了，你要把这一卷压成一段梗概。\n\n## 这段梗概会被怎么用\n\n它会**替代**这一卷的全部章节摘要，出现在后面每一卷的写作上下文里。\n也就是说：这一卷发生过的事，以后只剩你写的这一段。你没写进去的，\n后面的章节就再也看不到了。\n\n## 写什么\n\n一段连续的文字，150-250 字，按时间顺序。必须包含：\n\n- 这一卷里**关系推进到哪一步**，靠哪几件具体的事推进的\n- **改变了后续格局的事件**：身份变化、决定、决裂、承诺\n- 还**没有了结**的东西：没收的伏笔、没说出口的话、悬着的物件\n\n## 不要写什么\n\n- 不写氛围、不写评价、不写"这一卷展现了…"这类总结腔\n- 不写只在卷内起作用、已经了结的细节\n- 不复述章节标题，也不要写成分章列表 —— 那是目录，不是梗概\n\n## 判断标准\n\n后面第 60 章的作者只读到你这一段，能不能不写出与这一卷矛盾的情节？\n能，才算合格。\n',
    9: 'Archivist',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Archivist', 0): 'Archivist',
    ('__annotate__', 1): 'client',
    ('__annotate__', 2): 'LLMClient',
    ('__annotate__', 3): 'skills_dir',
    ('__annotate__', 4): 'str | Path | None',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'outline',
    ('__annotate__', 4): 'ChapterOutline',
    ('__annotate__', 5): 'text',
    ('__annotate__', 6): 'str',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'StatePatch',
    ('archive', 0): '、',
    ('archive', 2): '（尚无）',
    ('archive', 5): '下面 <正文> 标签里的内容是**第 ',
    ('archive', 6): ' 章的小说正文**，你要归档的就是它。\n不要归档任何设定资料、人物介绍或大纲 —— 那些是给你的参考，不是对象。\nchapter_summary 的 ch 字段必须填 ',
    ('archive', 7): '。\n\n第 ',
    ('archive', 8): ' 章《',
    ('archive', 9): '》，人生阶段：',
    ('archive', 10): '。\n\n已有人物：',
    ('archive', 11): '\n**引用时必须用括号里的 id。这几个人已经存在，不要作为 new_characters 重新登记 —— 只有正文里真正新出场、且后面还会再出现的角色才填进去。**\n\n未回收的情感债（本章若回收了其中某条，写进 resolved_debt_ids）：\n',
    ('archive', 12): '\n\n已用过的桥段（本章若又用了同一个，照原名记录）：',
    ('archive', 13): '\n\n本章意图：',
    ('archive', 14): '\n\n<正文>\n',
    ('archive', 15): '\n</正文>',
    ('archive', 16): 'archivist',
    ('archive', 20): 'archivist 归档的是第 ',
    ('archive', 21): ' 章「',
    ('archive', 22): '」，要求的是第 ',
    ('archive', 23): '」—— 它很可能归档了设定资料而不是正文。',
    ('<genexpr>', 0): '(',
    ('<genexpr>', 1): ')',
    ('<genexpr>', 0): '- [',
    ('<genexpr>', 1): '] ',
    ('<genexpr>', 2): '：',
    ('<genexpr>', 3): '（第 ',
    ('<genexpr>', 4): ' 章埋下，应在第 ',
    ('<genexpr>', 5): ' 章前回收）',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'VolumeOutline',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'VolumeSummary',
    ('compress_volume', 0): '卷末压缩：把本卷的章节摘要压成一段卷梗概。\n\n为什么必须有这一步：进上下文的章节摘要只保留"尚未被卷梗概覆盖"的那些。\n没有压缩，这个窗口会一路长到 140 章；有压缩但压丢了信息，后面的章节\n就会写出与前卷矛盾的情节。所以输入里要带上卷大纲 —— 模型据此知道\n这一卷**本来要达成什么**，不至于把主线漏在一堆细节外面。\n',
    ('compress_volume', 3): '第 ',
    ('compress_volume', 4): ' 卷（第 ',
    ('compress_volume', 5): '-',
    ('compress_volume', 6): ' 章）没有任何章节摘要可压缩 —— 这一卷还没开始写，或者归档漏了',
    ('compress_volume', 10): '（无）',
    ('compress_volume', 11): '把第 ',
    ('compress_volume', 12): ' 章，共 ',
    ('compress_volume', 13): ' 章有摘要）压成一段梗概。\n\nvolume 字段填 ',
    ('compress_volume', 14): '，ch_start 填 ',
    ('compress_volume', 15): '，ch_end 填 ',
    ('compress_volume', 16): '。\n\n<本卷当初的大纲>\n',
    ('compress_volume', 17): '\n</本卷当初的大纲>\n\n<本卷各章摘要>\n',
    ('compress_volume', 18): '\n</本卷各章摘要>\n\n<写到这里仍未回收的情感债>\n',
    ('compress_volume', 19): '\n</写到这里仍未回收的情感债>\n\n注意：大纲是当初的计划，各章摘要才是**实际写出来的东西**。两者不一致时以摘要为准。',
    ('compress_volume', 20): 'archivist',
    ('compress_volume', 23): '压缩出来的是第 ',
    ('compress_volume', 24): ' 卷的梗概，要求的是第 ',
    ('compress_volume', 25): ' 卷',
    ('compress_volume', 26): 'ch_start',
    ('compress_volume', 27): 'ch_end',
    ('<genexpr>', 0): '- 第 ',
    ('<genexpr>', 1): ' 章《',
    ('<genexpr>', 2): '》：',
    ('<genexpr>', 0): '- [',
    ('<genexpr>', 1): '] ',
    ('<genexpr>', 2): '：',
    ('<genexpr>', 3): '（第 ',
    ('<genexpr>', 4): ' 章埋下，应在第 ',
    ('<genexpr>', 5): ' 章前回收）',
}

# ───────────── 还原后的源码 ─────────────
from pathlib import Path

from novel_agent.agents.schemas import ChapterOutline, VolumeOutline
from novel_agent.llm.client import LLMClient
from novel_agent.llm.prompt_builder import Prompt
from novel_agent.state.schema import StatePatch, StoryState, VolumeSummary

# 角色提示词：直接取自模块级常量表原文，保证字节一致。
ARCHIVIST_ROLE = _RECOVERED_CONSTS[6]
VOLUME_ROLE = _RECOVERED_CONSTS[7]


class Archivist:
    def __init__(
        self, client: LLMClient, skills_dir: str | Path | None = None
    ) -> None:
        # 字节码仅把 client 存入实例；skills_dir 在签名里但未被使用。
        self.client = client

    def archive(self, state: StoryState, outline: ChapterOutline, text: str) -> StatePatch:
        known = "、".join(f"{c.name}({c.id})" for c in state.characters) or "（尚无）"
        open_debts = "\n".join(
            f"- [{d.id}] {d.kind}：{d.desc}（第 {d.planted_ch} 章埋下，应在第 {d.due_by_ch} 章前回收）"
            for d in state.open_debts()
        ) or "（尚无）"
        used = "、".join(state.used_beat_types()) or "（尚无）"
        instruction = (
            f"下面 <正文> 标签里的内容是**第 {outline.ch} 章的小说正文**，你要归档的就是它。\n"
            "不要归档任何设定资料、人物介绍或大纲 —— 那些是给你的参考，不是对象。\n"
            f"chapter_summary 的 ch 字段必须填 {outline.ch}。\n\n"
            f"第 {outline.ch} 章《{outline.title}》，人生阶段：{outline.stage}。\n\n"
            f"已有人物：{known}\n"
            "**引用时必须用括号里的 id。这几个人已经存在，不要作为 new_characters 重新登记 —— 只有正文里真正新出场、且后面还会再出现的角色才填进去。**\n\n"
            "未回收的情感债（本章若回收了其中某条，写进 resolved_debt_ids）：\n"
            f"{open_debts}\n\n"
            f"已用过的桥段（本章若又用了同一个，照原名记录）：{used}\n\n"
            f"本章意图：{outline.intent}\n\n"
            f"<正文>\n{text}\n</正文>"
        )
        result = self.client.parse(
            "archivist",
            Prompt(system_core=ARCHIVIST_ROLE, bible="", instruction=instruction),
            StatePatch,
        )
        patch = result.parsed
        patch.volume_summary = None
        if patch.chapter_summary.ch != outline.ch:
            raise ValueError(
                f"archivist 归档的是第 {patch.chapter_summary.ch} 章「{patch.chapter_summary.title}」，"
                f"要求的是第 {outline.ch} 章「{outline.title}」—— 它很可能归档了设定资料而不是正文。"
            )
        return patch

    def compress_volume(self, state: StoryState, volume: VolumeOutline) -> VolumeSummary:
        """卷末压缩：把本卷的章节摘要压成一段卷梗概。

        为什么必须有这一步：进上下文的章节摘要只保留"尚未被卷梗概覆盖"的那些。
        没有压缩，这个窗口会一路长到 140 章；有压缩但压丢了信息，后面的章节
        就会写出与前卷矛盾的情节。所以输入里要带上卷大纲 —— 模型据此知道
        这一卷**本来要达成什么**，不至于把主线漏在一堆细节外面。
        """
        rows = [
            s
            for s in sorted(state.chapter_summaries, key=lambda s: s.ch)
            if volume.ch_start <= s.ch <= volume.ch_end
        ]
        if not rows:
            raise ValueError(
                f"第 {volume.volume} 卷（第 {volume.ch_start}-{volume.ch_end} 章）没有任何章节摘要可压缩 —— 这一卷还没开始写，或者归档漏了"
            )
        chapters = "\n".join(
            f"- 第 {s.ch} 章《{s.title}》：{s.summary}" for s in rows
        )
        open_debts = "\n".join(
            f"- [{d.id}] {d.kind}：{d.desc}（第 {d.planted_ch} 章埋下，应在第 {d.due_by_ch} 章前回收）"
            for d in state.open_debts()
        ) or "（无）"
        instruction = (
            f"把第 {volume.volume} 卷（第 {volume.ch_start}-{volume.ch_end} 章，共 {len(rows)} 章有摘要）压成一段梗概。\n\n"
            f"volume 字段填 {volume.volume}，ch_start 填 {volume.ch_start}，ch_end 填 {volume.ch_end}。\n\n"
            f"<本卷当初的大纲>\n{volume.to_markdown()}\n</本卷当初的大纲>\n\n"
            f"<本卷各章摘要>\n{chapters}\n</本卷各章摘要>\n\n"
            f"<写到这里仍未回收的情感债>\n{open_debts}\n</写到这里仍未回收的情感债>\n\n"
            "注意：大纲是当初的计划，各章摘要才是**实际写出来的东西**。两者不一致时以摘要为准。"
        )
        result = self.client.parse(
            "archivist",
            Prompt(system_core=VOLUME_ROLE, bible="", instruction=instruction),
            VolumeSummary,
        )
        got = result.parsed
        if got.volume != volume.volume:
            raise ValueError(
                f"压缩出来的是第 {got.volume} 卷的梗概，要求的是第 {volume.volume} 卷"
            )
        return got.model_copy(update={"ch_start": volume.ch_start, "ch_end": rows[-1].ch})
