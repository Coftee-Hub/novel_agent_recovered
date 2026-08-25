# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/corpus/extract.py
# 来源   : extract.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '从范本里萃取写作手法，产出 skills 草稿。\n\n两阶段 map-reduce：\n  map    逐章读，输出结构化"手法观察"（抽象描述，不含原文）\n  reduce 把几十条观察合成一份 markdown skill 草稿\n\n为什么要结构化中间层：直接让模型"读完几本书写一份文风指南"，它会退回\n通用言情常识——那正是要避开的。强制它对**每一章**给出具体观察，再汇总，\n观察才会真的来自这些书。\n\n抄袭防线：prompt 明令禁止引用原文，产出再用 NGramIndex 反查一遍。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '从范本里萃取写作手法，产出 skills 草稿。\n\n两阶段 map-reduce：\n  map    逐章读，输出结构化"手法观察"（抽象描述，不含原文）\n  reduce 把几十条观察合成一份 markdown skill 草稿\n\n为什么要结构化中间层：直接让模型"读完几本书写一份文风指南"，它会退回\n通用言情常识——那正是要避开的。强制它对**每一章**给出具体观察，再汇总，\n观察才会真的来自这些书。\n\n抄袭防线：prompt 明令禁止引用原文，产出再用 NGramIndex 反查一遍。\n',
    12: 'Observation',
    14: 'ChapterExtraction',
    15: '你是一位小说技法分析者。你读小说不是为了看故事，而是为了拆解作者的手法。\n\n## 铁律\n\n**绝对禁止引用原文。** 不许摘抄任何句子、比喻、台词、意象组合。你的产出是\n「作者在这里做了什么」的抽象描述，不是「作者写了什么」的复述。\n\n错误示范：`她把伞往他那边偏了偏，雨水淌到自己肩上`\n正确示范：`用一个未被言明的照顾动作替代告白，让付出方承担可见的代价`\n\n**具体细节也要抽象化。** 不要写「咬河粉」「把伞往他那边偏」这类原文里的\n具体物件与动作，要写它们所属的**类别**：「一个重复性的进食动作」「一个\n无需言明的照顾动作」。原因是你的产出会被写作 AI 当模板用，你写下的具体\n细节它会照抄，于是全书都是同一根河粉。\n\n如果你发现自己正在复述一个具体场景，停下，退一步问：这个场景在**结构上**\n做了什么？把结构写出来。\n\n## 你要找的东西\n\n不是"这一章讲了什么"，而是：\n- 作者用什么方式完成情绪推进，而不是直接写出情绪\n- 对话里的信息是怎么藏的，潜台词怎么埋\n- 一个场景的开头怎么切入、结尾怎么收\n- 人物的性格是通过什么被读者感知的\n\n## 你要避开的\n\n- 「文笔细腻」「情感真挚」这类评语。这不是手法，是感想。\n- 通用的写作常识。如果一条观察放在任何一本言情小说上都成立，它就没有价值。\n- 情节复述。\n',
    17: 'ExtractionRun',
    18: 'style_voice',
    19: '叙述语感：句子的长短节奏、什么时候用短句、心理活动怎么与动作交织、视角贴多近、什么被写出来什么被省略。',
    20: 'romance_beats',
    21: '情绪节拍：这一章把两人关系推进了什么，靠什么具体事件完成的，推进前后的情绪状态各是什么，作者怎么控制推进的速度。',
    22: 'dialogue',
    23: '对话技法：潜台词怎么埋、话里的信息怎么藏、谁在回避什么、提示语（他说/她笑）怎么用、沉默和打断怎么处理。',
    24: 'character_design',
    25: '人物塑造：性格是通过什么细节被读者感知的、人物的行为逻辑锚在哪个心理创伤上、说话习惯有什么辨识度、什么事这个人绝不会做。',
    26: 'campus_to_career',
    27: '阶段跨越：校园到职场的过渡怎么处理、时间跳跃怎么交代、人物在新阶段保留了什么改变了什么、环境变化怎么施加压力。',
    28: 'cliche_blacklist',
    29: '俗套识别：这一章里哪些处理是套路化的、哪些地方作者明明可以走俗套却绕开了、绕开的方式是什么。',
    30: 'dict[str, str]',
    31: 'FOCUS',
    33: 'Extractor',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Observation', 0): 'Observation',
    ('Observation', 1): '一条可复用的手法观察。',
    ('Observation', 2): 'str',
    ('Observation', 3): 'name',
    ('Observation', 4): 'context',
    ('Observation', 5): 'how',
    ('Observation', 6): 'why',
    ('ChapterExtraction', 0): 'ChapterExtraction',
    ('ChapterExtraction', 2): 'list[Observation]',
    ('ChapterExtraction', 3): 'observations',
    ('ExtractionRun', 0): 'ExtractionRun',
    ('ExtractionRun', 1): 'str',
    ('ExtractionRun', 2): 'skill',
    ('ExtractionRun', 4): 'list[Observation]',
    ('ExtractionRun', 5): 'observations',
    ('ExtractionRun', 6): 'int',
    ('ExtractionRun', 7): 'chapters_read',
    ('ExtractionRun', 9): 'float',
    ('ExtractionRun', 10): 'cost_usd',
    ('ExtractionRun', 11): 'elapsed_s',
    ('ExtractionRun', 12): 'list[str]',
    ('ExtractionRun', 13): 'plagiarism_hits',
    ('Extractor', 0): 'Extractor',
    ('Extractor', 6): 'per_book',
    ('Extractor', 7): 'seed_offset',
    ('Extractor', 8): 'workers',
    ('Extractor', 11): 'guidance',
    ('Extractor', 19): 'tries',
    ('__annotate__', 1): 'client',
    ('__annotate__', 2): 'LLMClient',
    ('__annotate__', 3): 'corpus_index',
    ('__annotate__', 4): 'NGramIndex | None',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('__annotate__', 1): 'skill',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'chapter',
    ('__annotate__', 4): 'Chapter',
    ('__annotate__', 5): 'book',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'ChapterExtraction',
    ('read_chapter', 0): '下面是《',
    ('read_chapter', 1): '》的一章。请针对以下侧面给出 2-5 条手法观察：\n\n**关注点**：',
    ('read_chapter', 2): '\n\n记住：写作者做了什么，不要复述作者写了什么，不要引用任何原句。\n\n<章节>\n',
    ('read_chapter', 3): '\n</章节>',
    ('read_chapter', 4): 'extractor',
    ('__annotate__', 1): 'skill',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'books',
    ('__annotate__', 4): 'list[Path]',
    ('__annotate__', 5): 'per_book',
    ('__annotate__', 6): 'int',
    ('__annotate__', 7): 'seed_offset',
    ('__annotate__', 8): 'workers',
    ('__annotate__', 9): 'return',
    ('__annotate__', 10): 'ExtractionRun',
    ('run', 0): '从若干本书里各抽 per_book 章做萃取。\n\n并发跑：单章约 40 秒，全量上百章串行要一个多小时。萃取是一次性的\n离线任务，没有前后依赖，正适合并发。\n',
    ('run', 4): '    ! ',
    ('run', 5): ' 第',
    ('run', 6): '章 失败：',
    ('run', 7): ': ',
    ('__annotate__', 1): 'run',
    ('__annotate__', 2): 'ExtractionRun',
    ('__annotate__', 3): 'title',
    ('__annotate__', 4): 'str',
    ('__annotate__', 5): 'guidance',
    ('__annotate__', 6): 'return',
    ('synthesize', 0): '把观察汇总成 skill 草稿。\n\n观察多时分批：一次喂 117 条会让思考模型把 token 预算全耗在推理上，\n正文一个字都出不来（实测 stop_reason=length、text 为空）。\n先分批各出一份，再合并。\n',
    ('__annotate__', 1): 'partials',
    ('__annotate__', 2): 'list[str]',
    ('__annotate__', 3): 'title',
    ('__annotate__', 4): 'str',
    ('__annotate__', 5): 'guidance',
    ('__annotate__', 6): 'return',
    ('_merge', 0): '\n\n---\n\n',
    ('_merge', 2): '下面是同一批范本分批整理出的 ',
    ('_merge', 3): ' 份「',
    ('_merge', 4): '」草稿。请合并成一份，去掉重复、保留互补，按可操作性排序。\n要求同前：可直接执行、不要空话、不许引用原文、markdown、无一级标题。\n',
    ('<genexpr>', 0): '## 第 ',
    ('<genexpr>', 1): ' 份\n',
    ('__annotate__', 1): 'run',
    ('__annotate__', 2): 'ExtractionRun',
    ('__annotate__', 3): 'title',
    ('__annotate__', 4): 'str',
    ('__annotate__', 5): 'guidance',
    ('__annotate__', 6): 'return',
    ('_synthesize_once', 0): '- **',
    ('_synthesize_once', 1): '**（',
    ('_synthesize_once', 2): '）：',
    ('_synthesize_once', 3): ' —— ',
    ('_synthesize_once', 4): '下面是从范本小说里萃取的 ',
    ('_synthesize_once', 5): ' 条手法观察。请把它们整理成一份给**写作 AI 看的**操作指南，标题是「',
    ('_synthesize_once', 6): '」。\n\n要求：\n- 合并重复的观察，保留互相冲突的（注明适用场景不同）\n- 按可操作性排序：越具体越靠前\n- 每条都要能被直接执行，不要出现「注意细节」这类空话\n- 删掉放在任何言情小说上都成立的通用常识\n- 用 markdown，不要用一级标题\n- **不许引用任何原文**\n',
    ('_synthesize_once', 7): '\n额外要求：',
    ('_synthesize_once', 9): '\n<观察>\n',
    ('_synthesize_once', 10): '\n</观察>',
    ('__annotate__', 1): 'instruction',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'tries',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'return',
    ('_complete', 0): '发一次合成请求，空输出或截断都要报错，不能静默写出残缺草稿。\n\n思考模型会把 token 预算优先花在推理上。预算不够时有两种表现：\n正文完全为空（stop_reason=length），或正文写到一半戛然而止\n（stop_reason 仍报 stop，但结尾没有终止标点）。后者更阴险 ——\n文件看起来正常，内容却缺了一大截。\n',
    ('_complete', 2): '\n\n注意：上一次的输出超长被截断了。这次请更紧凑——合并近似条目、砍掉冗长铺陈，务必把结构写完整。',
    ('_complete', 3): 'extractor',
    ('_complete', 5): '合成返回空文本（stop_reason=',
    ('_complete', 6): '，输出 ',
    ('_complete', 7): ' tokens）。思考模型把预算耗在推理上了 —— 调高 max_tokens 或减少单批观察数。',
    ('_complete', 8): '合成结果被截断（',
    ('_complete', 9): ' 字符，结尾：',
    ('_complete', 11): '）。重试 ',
    ('_complete', 12): ' 次仍未写完 —— 调小 Extractor.BATCH 或提高 max_tokens。',
    ('__annotate__', 1): 'observations',
    ('__annotate__', 2): 'list[Observation]',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[str]',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'float',
    ('_spent', 3): 'utf-8',
    ('<genexpr>', 0): 'cost_usd',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'Path',
    ('__annotate__', 3): 'count',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'offset',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'list[Chapter]',
    ('sample_chapters', 0): '均匀取样，跳过开头结尾。\n\n开头在铺设定、结尾在收线，中段才是常态叙事 —— 要学的是常态。\n',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('strip_fences', 0): '模型偶尔会把 markdown 包进 ``` 围栏。',
    ('strip_fences', 1): '```',
    ('strip_fences', 2): '^```[a-zA-Z]*\\n',
    ('strip_fences', 4): '\\n```$',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'bool',
    ('_looks_complete', 0): '判断合成结果是否被截断。\n\n判据是结尾标点。中文正文正常收尾必然落在句号/问号/感叹号/省略号，\n或是 markdown 的列表、表格、引用行。停在冒号、逗号、半个词上就是被切了。\n',
    ('_looks_complete', 3): '。！？…”』」.!?',
}

# ───────────── 还原后的源码 ─────────────
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path

from pydantic import BaseModel, Field

from novel_agent.corpus.ingest import Chapter, clean, read_text, split_chapters
from novel_agent.corpus.similarity import NGramIndex
from novel_agent.llm.client import LLMClient
from novel_agent.llm.prompt_builder import Prompt

# 角色提示词：直接取自模块级常量表原文，保证字节一致。
EXTRACTOR_ROLE = _RECOVERED_CONSTS[15]

# 各 skill 的萃取关注点：key 是模块级常量表下标 18/20/22/24/26/28 的字符串，
# value 取紧随其后的描述。
FOCUS: dict[str, str] = {
    _RECOVERED_CONSTS[18]: _RECOVERED_CONSTS[19],
    _RECOVERED_CONSTS[20]: _RECOVERED_CONSTS[21],
    _RECOVERED_CONSTS[22]: _RECOVERED_CONSTS[23],
    _RECOVERED_CONSTS[24]: _RECOVERED_CONSTS[25],
    _RECOVERED_CONSTS[26]: _RECOVERED_CONSTS[27],
    _RECOVERED_CONSTS[28]: _RECOVERED_CONSTS[29],
}


class Observation(BaseModel):
    """一条可复用的手法观察。"""

    name: str
    context: str
    how: str
    why: str


class ChapterExtraction(BaseModel):
    observations: list[Observation] = Field(min_length=1, max_length=6)


@dataclass
class ExtractionRun:
    skill: str
    observations: list[Observation] = field(default_factory=list)
    chapters_read: int = 0
    cost_usd: float = 0.0
    elapsed_s: float = 0.0
    plagiarism_hits: list[str] = field(default_factory=list)


class Extractor:
    BATCH = 30

    def __init__(self, client: LLMClient, corpus_index: NGramIndex | None = None) -> None:
        self.client = client
        self.corpus_index = corpus_index

    def read_chapter(self, skill: str, chapter: Chapter, book: str) -> ChapterExtraction:
        """下面是《"""
        focus = FOCUS[skill]
        instruction = (
            f"下面是《{book}》的一章。请针对以下侧面给出 2-5 条手法观察：\n\n**关注点**："
            f"{focus}"
            f"\n\n记住：写作者做了什么，不要复述作者写了什么，不要引用任何原句。\n\n<章节>\n"
            f"{chapter.body}"
            f"\n</章节>"
        )
        result = self.client.parse(
            "extractor",
            Prompt(system_core=EXTRACTOR_ROLE, instruction=instruction),
            ChapterExtraction,
        )
        return result.parsed

    def run(
        self,
        skill: str,
        books: list[Path],
        *,
        per_book: int,
        seed_offset: int,
        workers: int,
    ) -> ExtractionRun:
        """从若干本书里各抽 per_book 章做萃取。

        并发跑：单章约 40 秒，全量上百章串行要一个多小时。萃取是一次性的
        离线任务，没有前后依赖，正适合并发。
        """
        run = ExtractionRun(skill=skill)
        before = self._spent()

        jobs = [
            (path, ch)
            for path in books
            for ch in sample_chapters(path, per_book, seed_offset)
        ]
        lock = threading.Lock()

        def work(job):
            path, chapter = job
            got = self.read_chapter(skill, chapter, path.stem)
            with lock:
                run.observations.extend(got.observations)
                run.chapters_read += 1

        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(work, j): j for j in jobs}
            for fut in as_completed(futures):
                path, chapter = futures[fut]
                try:
                    fut.result()
                except Exception as exc:
                    print(
                        f"    ! {path.stem} 第{chapter.index}章 失败："
                        f"{type(exc).__name__}: {str(exc)[:80]}"
                    )

        run.cost_usd = self._spent() - before
        run.plagiarism_hits = self._check(run.observations)
        return run

    def synthesize(
        self, run: ExtractionRun, *, title: str, guidance: str = ""
    ) -> str:
        """把观察汇总成 skill 草稿。

        观察多时分批：一次喂 117 条会让思考模型把 token 预算全耗在推理上，
        正文一个字都出不来（实测 stop_reason=length、text 为空）。
        先分批各出一份，再合并。
        """
        if len(run.observations) > self.BATCH:
            partials: list[str] = []
            for i in range(0, len(run.observations), self.BATCH):
                chunk = ExtractionRun(
                    skill=run.skill, observations=run.observations[i : i + self.BATCH]
                )
                partials.append(
                    self._synthesize_once(chunk, title=title, guidance=guidance)
                )
            return self._merge(partials, title=title, guidance=guidance)
        return self._synthesize_once(run, title=title, guidance=guidance)

    def _merge(
        self, partials: list[str], *, title: str, guidance: str
    ) -> str:
        joined = "\n\n---\n\n".join(
            f"## 第 {i} 份\n{p}" for i, p in enumerate(partials, 1)
        )
        instruction = (
            f"下面是同一批范本分批整理出的 {len(partials)} 份「{title}」草稿。"
            "请合并成一份，去掉重复、保留互补，按可操作性排序。\n"
            "要求同前：可直接执行、不要空话、不许引用原文、markdown、无一级标题。\n"
        )
        if guidance:
            instruction += f"\n{guidance}\n"
        instruction += f"\n{joined}"
        return self._complete(instruction)

    def _synthesize_once(
        self, run: ExtractionRun, *, title: str, guidance: str
    ) -> str:
        lines = [
            f"- **{o.name}**（{o.context}）：{o.how} —— {o.why}"
            for o in run.observations
        ]
        instruction = (
            f"下面是从范本小说里萃取的 {len(lines)} 条手法观察。"
            "请把它们整理成一份给**写作 AI 看的**操作指南，标题是「"
            f"{title}"
            "」。\n\n要求：\n"
            "- 合并重复的观察，保留互相冲突的（注明适用场景不同）\n"
            "- 按可操作性排序：越具体越靠前\n"
            "- 每条都要能被直接执行，不要出现「注意细节」这类空话\n"
            "- 删掉放在任何言情小说上都成立的通用常识\n"
            "- 用 markdown，不要用一级标题\n"
            "- **不许引用任何原文**\n"
        )
        if guidance:
            instruction += f"\n额外要求：{guidance}\n"
        instruction += f"\n<观察>\n" + "\n".join(lines) + "\n</观察>"
        return self._complete(instruction)

    def _complete(self, instruction: str, *, tries: int = 2) -> str:
        """发一次合成请求，空输出或截断都要报错，不能静默写出残缺草稿。

        思考模型会把 token 预算优先花在推理上。预算不够时有两种表现：
        正文完全为空（stop_reason=length），或正文写到一半戛然而止
        （stop_reason 仍报 stop，但结尾没有终止标点）。后者更阴险 ——
        文件看起来正常，内容却缺了一大截。
        """
        last_text = ""
        for attempt in range(tries):
            ask = instruction
            if attempt:
                ask += "\n\n注意：上一次的输出超长被截断了。这次请更紧凑——合并近似条目、砍掉冗长铺陈，务必把结构写完整。"
            result = self.client.complete(
                "extractor",
                Prompt(system_core=EXTRACTOR_ROLE, instruction=ask),
            )
            text = result.text.strip()
            if not text:
                raise RuntimeError(
                    f"合成返回空文本（stop_reason={result.stop_reason}，输出 "
                    f"{result.output_tokens} tokens）。思考模型把预算耗在推理上了 —— 调高 max_tokens 或减少单批观察数。"
                )
            if _looks_complete(text):
                return text
            last_text = text
        raise RuntimeError(
            f"合成结果被截断（{len(last_text)} 字符，结尾：{last_text[-40:]!r}）。"
            f"重试 {tries} 次仍未写完 —— 调小 Extractor.BATCH 或提高 max_tokens。"
        )

    def _check(self, observations: list[Observation]) -> list[str]:
        if self.corpus_index is None or self.corpus_index.is_empty:
            return []
        blob = "\n".join(
            f"{o.name} {o.context} {o.how} {o.why}" for o in observations
        )
        return self.corpus_index.find_matches(blob, limit=10)

    def _spent(self) -> float:
        log = self.client.log_path
        if log is None or not log.exists():
            return 0.0
        import json

        return sum(
            json.loads(line)["cost_usd"]
            for line in log.read_text("utf-8").splitlines()
            if line.strip()
        )


def sample_chapters(path: Path, count: int, offset: int) -> list[Chapter]:
    """均匀取样，跳过开头结尾。

    开头在铺设定、结尾在收线，中段才是常态叙事 —— 要学的是常态。
    """
    raw, _ = read_text(path)
    body, _ = clean(raw)
    chapters = [
        c for c in split_chapters(body) if 1500 < c.word_count < 12000
    ]
    if len(chapters) <= count:
        return chapters
    lo = int(len(chapters) * 0.15)
    hi = int(len(chapters) * 0.85)
    span = chapters[lo:hi] or chapters
    step = max(len(span) // count, 1)
    return [span[(i * step + offset) % len(span)] for i in range(count)]


def strip_fences(text: str) -> str:
    """模型偶尔会把 markdown 包进 ``` 围栏。"""
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```[a-zA-Z]*\n", "", stripped)
        stripped = re.sub(r"\n```$", "", stripped)
    return stripped.strip()


def _looks_complete(text: str) -> bool:
    """判断合成结果是否被截断。

    判据是结尾标点。中文正文正常收尾必然落在句号/问号/感叹号/省略号，
    或是 markdown 的列表、表格、引用行。停在冒号、逗号、半个词上就是被切了。
    """
    tail = text.rstrip()
    if not tail:
        return False
    last_line = tail.splitlines()[-1].rstrip()
    if last_line.endswith(("|", "-", ")", "）", "`")):
        return True
    return tail[-1] in "。！？…”』」.!?"
