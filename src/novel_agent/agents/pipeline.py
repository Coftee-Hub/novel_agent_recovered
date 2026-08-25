# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/agents/pipeline.py
# 来源   : pipeline.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════


from __future__ import annotations

import re
from datetime import datetime

from pydantic import Field as field  # TODO(重建): 需确认 import —— 字节码用 LOAD_NAME field（小写别名）

from ..agents.writer import StitchFailed
from ..state import apply_patch, apply_volume_summary  # TODO(重建): 需确认 import —— 或 from ..state.store import ...

__doc__ = '单章闭环：出细纲 → 逐场景写 → 缝合 → 检查 → 定向修订 → 归档。\n\n修订上限是硬的。没有上限的修订环是烧钱死循环 —— 每轮都可能修掉旧问题\n引入新问题，模型不会自己收敛。超限就落到 needs_human，交给人。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '单章闭环：出细纲 → 逐场景写 → 缝合 → 检查 → 定向修订 → 归档。\n\n修订上限是硬的。没有上限的修订环是烧钱死循环 —— 每轮都可能修掉旧问题\n引入新问题，模型不会自己收敛。超限就落到 needs_human，交给人。\n',
    15: 'ChapterResult',
    17: 'ChapterPipeline',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('ChapterResult', 0): 'ChapterResult',
    ('ChapterResult', 1): 'int',
    ('ChapterResult', 2): 'ch',
    ('ChapterResult', 3): 'ChapterOutline',
    ('ChapterResult', 4): 'outline',
    ('ChapterResult', 5): 'str',
    ('ChapterResult', 6): 'text',
    ('ChapterResult', 7): 'GateReport',
    ('ChapterResult', 8): 'gate',
    ('ChapterResult', 9): 'JudgeVerdict | None',
    ('ChapterResult', 10): 'verdict',
    ('ChapterResult', 11): 'revisions',
    ('ChapterResult', 13): 'bool',
    ('ChapterResult', 14): 'stitch_degraded',
    ('ChapterResult', 16): 'StatePatch | None',
    ('ChapterResult', 17): 'patch',
    ('ChapterResult', 18): 'StoryState | None',
    ('ChapterResult', 19): 'state',
    ('ChapterResult', 20): 'VolumeSummary | None',
    ('ChapterResult', 21): 'volume_summary',
    ('ChapterResult', 22): 'str | None',
    ('ChapterResult', 23): 'archive_error',
    ('ChapterResult', 25): 'list[str]',
    ('ChapterResult', 26): 'notes',
    ('ChapterResult', 29): '_floor',
    ('ChapterResult', 30): '_total',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'bool',
    ('ChapterPipeline', 0): 'ChapterPipeline',
    ('ChapterPipeline', 1): 'max_revisions',
    ('ChapterPipeline', 2): 'retriever',
    ('ChapterPipeline', 4): 'outline_sink',
    ('ChapterPipeline', 5): 'draft_sink',
    ('ChapterPipeline', 6): 'judgment_sink',
    ('ChapterPipeline', 7): 'log',
    ('ChapterPipeline', 10): 'note',
    ('ChapterPipeline', 12): 'outline',
    ('ChapterPipeline', 13): 'drafts',
    ('ChapterPipeline', 18): 'revision',
    ('__annotate__', 1): 'writer',
    ('__annotate__', 2): 'Writer',
    ('__annotate__', 3): 'stitcher',
    ('__annotate__', 4): 'Stitcher',
    ('__annotate__', 5): 'gate',
    ('__annotate__', 6): 'Gate',
    ('__annotate__', 7): 'judge',
    ('__annotate__', 8): 'Judge',
    ('__annotate__', 9): 'archivist',
    ('__annotate__', 10): 'Archivist',
    ('__annotate__', 11): 'max_revisions',
    ('__annotate__', 12): 'int',
    ('__annotate__', 13): 'return',
    ('__annotate__', 14): 'None',
    ('__annotate__', 1): 'state',
    ('__annotate__', 2): 'StoryState',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'VolumeOutline',
    ('__annotate__', 5): 'ch',
    ('__annotate__', 6): 'int',
    ('__annotate__', 7): 'note',
    ('__annotate__', 8): 'str',
    ('__annotate__', 9): 'outline',
    ('__annotate__', 10): 'ChapterOutline | None',
    ('__annotate__', 11): 'drafts',
    ('__annotate__', 12): 'list[str] | None',
    ('__annotate__', 13): 'return',
    ('__annotate__', 14): 'ChapterResult',
    ('run', 1): '[第 ',
    ('run', 2): ' 章] 出细纲…',
    ('run', 4): ' 章] 复用已确认的细纲',
    ('run', 6): ' 场，目标 ',
    ('run', 7): ' 字',
    ('run', 9): '[检索] 取到 ',
    ('run', 10): ' 段风格参照',
    ('run', 11): '[写作] 复用 ',
    ('run', 12): '/',
    ('run', 13): ' 段已写好的草稿',
    ('run', 14): '[写作] 逐场景生成…',
    ('run', 18): '  ! 检查未过但定位不到具体场景，无法定向修订',
    ('run', 19): '[修订 ',
    ('run', 20): '] 重写 ',
    ('run', 21): ' 个场景',
    ('run', 22): '：',
    ('run', 23): '；',
    ('run', 27): '.r',
    ('run', 30): '缝合降级为机械拼接（接缝未打磨、章末钩子未处理）—— 正文是好的，渠道恢复后重跑即可',
    ('run', 31): '修订 ',
    ('run', 32): ' 轮后仍未通过',
    ('run', 33): '首轮即未通过且无法定位场景',
    ('run', 34): '[归档] 提炼状态增量…',
    ('run', 35): ': ',
    ('run', 36): '  ! 归档失败：',
    ('run', 37): '    正文合格，照常落盘；补录用：novel-agent archive ',
    ('__annotate__', 1): 'result',
    ('__annotate__', 2): 'ChapterResult',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'VolumeOutline',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('compress_volume', 0): '卷末把本卷压成一段梗概。失败不影响这一章已经拿到的成果。\n\n压缩是记账动作，正文已经写完、检查过、归档了。因为一次 DeepSeek 调用\n失败就把一整章判为失败，是拿贵的东西赔便宜的东西 —— 补做只要\n`novel-agent compress <卷号>`。\n',
    ('compress_volume', 1): '[压缩] 第 ',
    ('compress_volume', 2): ' 卷写完了，压一段卷梗概…',
    ('compress_volume', 3): '第 ',
    ('compress_volume', 4): ' 卷卷末压缩失败：',
    ('compress_volume', 5): ': ',
    ('compress_volume', 6): '（本章已归档，补做：novel-agent compress ',
    ('compress_volume', 7): '）',
    ('compress_volume', 8): '  ! ',
    ('compress_volume', 11): ' 字，第 ',
    ('compress_volume', 12): '-',
    ('compress_volume', 13): ' 章已压成一段',
    ('__annotate__', 1): 'scenes',
    ('__annotate__', 2): 'list[str]',
    ('__annotate__', 3): 'ch',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'revision',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'tuple[str, bool]',
    ('_stitch', 0): '缝合一次，失败就用机械拼接顶上。返回 (正文, 是否降级)。\n\n为什么不让它直接抛：缝合是全流程单次输出最大的请求，也是实测最常失败的\n一步（第 3 章四次尝试三次死在这里）。抛出去意味着三场写好的正文换来\n零产出，连"内容到底行不行"都没法判断。降级的那一版不会被当成成稿。\n',
    ('_stitch', 1): '整章',
    ('_stitch', 2): '整章.r',
    ('_stitch', 3): '  ! ',
    ('_stitch', 4): '    用机械拼接兜底：正文保留，接缝未打磨，本章不作为成稿',
    ('_stitch', 5): '.机械拼接',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'name',
    ('__annotate__', 4): 'str',
    ('__annotate__', 5): 'text',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'None',
    ('_save_draft', 0): '存草稿。存不下来不该拖垮正在跑的一章 —— 它只是个安全网。',
    ('_save_draft', 2): '  ! 草稿没存下来（',
    ('_save_draft', 3): '），继续跑',
    ('__annotate__', 1): 'outline',
    ('__annotate__', 2): 'ChapterOutline',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict[str, list[str]] | None',
    ('__annotate__', 1): 'report',
    ('__annotate__', 2): 'GateReport',
    ('__annotate__', 3): 'revision',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'JudgeVerdict | None',
    ('_judge_if_gate_passed', 0): 'gate 不过就不评审 —— 格式不合规的稿子不该浪费一次 LLM 调用。',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'revision',
    ('__annotate__', 4): 'text',
    ('__annotate__', 5): 'str',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'None',
    ('record_judgment', 0): '把一次评审的七维分数记下来。\n\n两个用途：**调阈值**（方案里写的"跑 10 章后按实际分布调"，没有分布\n就无从谈起），以及**判断修订到底有没有用** —— 同一章修订前后的分数\n变化此前完全是黑箱。\n\n连同当时的阈值一起记：阈值以后会改，不记下来旧数据就没法解读。\n记账失败不许拖垮一章，理由同缝合与归档。\n',
    ('record_judgment', 2): 'ts',
    ('record_judgment', 3): 'seconds',
    ('record_judgment', 5): 'ch',
    ('record_judgment', 6): 'revision',
    ('record_judgment', 7): 'scores',
    ('record_judgment', 8): 'total',
    ('record_judgment', 9): 'lowest',
    ('record_judgment', 11): 'passed',
    ('record_judgment', 13): 'thresholds',
    ('record_judgment', 14): 'per_dimension',
    ('record_judgment', 15): 'word_count',
    ('record_judgment', 16): '\\s',
    ('record_judgment', 18): 'notes',
    ('record_judgment', 19): '  ! 评审记录没写成：',
    ('record_judgment', 20): ': ',
    ('__annotate__', 1): 'report',
    ('__annotate__', 2): 'GateReport',
    ('__annotate__', 3): 'verdict',
    ('__annotate__', 4): 'JudgeVerdict | None',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'bool',
    ('__annotate__', 1): 'outline',
    ('__annotate__', 2): 'ChapterOutline',
    ('__annotate__', 3): 'report',
    ('__annotate__', 4): 'GateReport',
    ('__annotate__', 5): 'verdict',
    ('__annotate__', 6): 'JudgeVerdict | None',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'dict[int, list[str]]',
    ('_targets', 0): '把问题映射到场景下标。\n\njudge 的意见自带 scene_id；gate 的多数问题是整章级的统计特征，\n没法归到某一场，只能分摊给全部场景。\n',
    ('_targets', 1): ' → ',
}



# ───────────── 代码骨架（签名/docstring 原样）─────────────

# TODO(重建): 需确认基类/装饰器 —— 骨架未含基类（可能是 pydantic BaseModel 或 @dataclass），
# 但字节码显示类体只有注解 + Field + property，无显式 __init__。
class ChapterResult:
    ch: int
    outline: ChapterOutline
    text: str
    gate: GateReport
    verdict: JudgeVerdict | None
    revisions: int

    stitch_degraded = False
    stitch_degraded: bool
    patch = None
    patch: StatePatch | None
    state = None
    state: StoryState | None
    volume_summary = None
    volume_summary: VolumeSummary | None
    archive_error = None
    archive_error: str | None
    notes = field(list, default_factory=list)
    notes: list[str]

    @property
    def passed(self) -> bool:
        if self.stitch_degraded:
            return False
        if not self.gate.passed:
            return False
        return self.verdict is None or self.verdict.passed(
            min_per_dimension=self._floor,
            min_total=self._total,
        )

    _floor = 3
    _floor: int
    _total = 24
    _total: int


class ChapterPipeline:
    def __init__(
        self, *,
        architect,
        writer: Writer,
        stitcher: Stitcher,
        gate: Gate,
        judge: Judge,
        archivist: Archivist,
        max_revisions: int = 2,
        retriever=None,
        outline_sink=None,
        draft_sink=None,
        judgment_sink=None,
        log=print,
    ) -> None:
        self.architect = architect
        self.writer = writer
        self.stitcher = stitcher
        self.gate = gate
        self.judge = judge
        self.archivist = archivist
        self.max_revisions = max_revisions
        self.retriever = retriever
        self.outline_sink = outline_sink
        self.judgment_sink = judgment_sink
        self.draft_sink = draft_sink
        self.log = log

    def run(
        self,
        state: StoryState,
        volume: VolumeOutline,
        ch: int,
        *,
        note: str = '',
        outline: ChapterOutline | None = None,
        drafts: list[str] | None = None,
    ) -> ChapterResult:
        if outline is None:
            self.log(f'[第 {ch} 章] 出细纲…')
            outline = self.architect.plan_chapter(state, volume, ch=ch, note=note)
            if self.outline_sink is not None:
                self.outline_sink(outline)
        else:
            self.log(f'[第 {ch} 章] 复用已确认的细纲')
        self.log(f'  {len(outline.scenes)} 场，目标 {outline.target_words} 字')

        rag = self._retrieve(outline)
        if rag:
            hits = sum(len(v) for v in rag.values())
            self.log(f'[检索] 取到 {hits} 段风格参照')
        if drafts:
            self.log(f'[写作] 复用 {len(drafts)}/{len(outline.scenes)} 段已写好的草稿')
        else:
            self.log('[写作] 逐场景生成…')

        scenes = self.writer.write_chapter_scenes(
            state,
            outline,
            rag=rag,
            on_scene=lambda spec, txt: self._save_draft(ch, spec.id, txt),
            already=drafts,
        )

        text, degraded = self._stitch(outline, scenes, ch)
        report = self.gate.check(text, state=state, expected_ch=ch)
        verdict = self._judge_if_gate_passed(state, outline, text, report)
        revisions = 0

        while not degraded and revisions < self.max_revisions and not self._ok(report, verdict):
            revisions += 1
            targets = self._targets(outline, report, verdict)
            if not targets:
                self.log('  ! 检查未过但定位不到具体场景，无法定向修订')
                break
            self.log(f'[修订 {revisions}/{self.max_revisions}] 重写 {len(targets)} 个场景')
            for idx, problems in sorted(targets.items()):
                spec = outline.scenes[idx]
                self.log(f'  {spec.id}：{"；".join(problems)[:60]}')
                scenes[idx] = self.writer.revise_scene(
                    state,
                    outline,
                    spec,
                    scenes[idx],
                    problems,
                    prev_text=scenes[idx - 1] if idx else '',
                )
                self._save_draft(ch, f'{spec.id}.r{revisions}', scenes[idx])
            text, degraded = self._stitch(outline, scenes, ch, revision=revisions)
            report = self.gate.check(text, state=state, expected_ch=ch)
            verdict = self._judge_if_gate_passed(state, outline, text, report, revisions)

        result = ChapterResult(
            ch=ch,
            outline=outline,
            text=text,
            gate=report,
            verdict=verdict,
            revisions=revisions,
            stitch_degraded=degraded,
            _floor=self.judge.min_per_dimension,
            _total=self.judge.min_total,
        )

        if not result.passed:
            if degraded:
                result.notes.append('缝合降级为机械拼接（接缝未打磨、章末钩子未处理）—— 正文是好的，渠道恢复后重跑即可')
                return result
            elif revisions:
                result.notes.append(f'修订 {revisions} 轮后仍未通过')
                return result
            else:
                result.notes.append('首轮即未通过且无法定位场景')
                return result

        self.log('[归档] 提炼状态增量…')
        try:
            result.patch = self.archivist.archive(state, outline, text)
            result.state = apply_patch(state, result.patch)
        except Exception as exc:
            result.archive_error = f'{type(exc).__name__}: {exc}'
            self.log(f'  ! 归档失败：{result.archive_error}')
            self.log(f'    正文合格，照常落盘；补录用：novel-agent archive {ch}')
            return result
        if ch == volume.ch_end:
            self.compress_volume(result, volume)
        return result

    def compress_volume(self, result: ChapterResult, volume: VolumeOutline) -> None:
        '卷末把本卷压成一段梗概。失败不影响这一章已经拿到的成果。\n\n压缩是记账动作，正文已经写完、检查过、归档了。因为一次 DeepSeek 调用\n失败就把一整章判为失败，是拿贵的东西赔便宜的东西 —— 补做只要\n`novel-agent compress <卷号>`。\n'
        self.log(f'[压缩] 第 {volume.volume} 卷写完了，压一段卷梗概…')
        try:
            summary = self.archivist.compress_volume(result.state, volume)
        except Exception as exc:
            note = f'第 {volume.volume} 卷卷末压缩失败：{type(exc).__name__}: {exc}（本章已归档，补做：novel-agent compress {volume.volume}）'
            self.log(f'  ! {note}')
            result.notes.append(note)
        else:
            result.state = apply_volume_summary(result.state, summary)
            result.volume_summary = summary
            self.log(f'  {len(summary.summary)} 字，第 {summary.ch_start}-{summary.ch_end} 章已压成一段')

    def _stitch(self, outline, scenes: list[str], ch: int, *, revision: int = 0) -> tuple[str, bool]:
        '缝合一次，失败就用机械拼接顶上。返回 (正文, 是否降级)。\n\n为什么不让它直接抛：缝合是全流程单次输出最大的请求，也是实测最常失败的\n一步（第 3 章四次尝试三次死在这里）。抛出去意味着三场写好的正文换来\n零产出，连"内容到底行不行"都没法判断。降级的那一版不会被当成成稿。\n'
        name = f'整章.r{revision}' if revision else '整章'
        try:
            text = self.stitcher.stitch(outline, scenes)
        except StitchFailed as exc:
            self.log(f'  ! {exc}')
            self.log('    用机械拼接兜底：正文保留，接缝未打磨，本章不作为成稿')
            self._save_draft(ch, f'{name}.机械拼接', exc.fallback)
            return exc.fallback, True
        else:
            self._save_draft(ch, name, text)
            return text, False

    def _save_draft(self, ch: int, name: str, text: str) -> None:
        '存草稿。存不下来不该拖垮正在跑的一章 —— 它只是个安全网。'
        if self.draft_sink is None:
            return None
        try:
            self.draft_sink(ch, name, text)
        except OSError as exc:
            self.log(f'  ! 草稿没存下来（{exc}），继续跑')
        return None

    def _retrieve(self, outline: ChapterOutline) -> dict[str, list[str]] | None:
        if self.retriever is None:
            return None
        return {s.id: self.retriever.snippets(s) for s in outline.scenes}

    def _judge_if_gate_passed(
        self, state, outline, text, report: GateReport, revision: int = 0
    ) -> JudgeVerdict | None:
        'gate 不过就不评审 —— 格式不合规的稿子不该浪费一次 LLM 调用。'
        if not report.passed:
            return None
        verdict = self.judge.review(state, outline, text)
        self.record_judgment(outline.ch, revision, verdict, text)
        return verdict

    def record_judgment(self, ch: int, revision: int, verdict, text: str) -> None:
        '把一次评审的七维分数记下来。\n\n两个用途：**调阈值**（方案里写的"跑 10 章后按实际分布调"，没有分布\n就无从谈起），以及**判断修订到底有没有用** —— 同一章修订前后的分数\n变化此前完全是黑箱。\n\n连同当时的阈值一起记：阈值以后会改，不记下来旧数据就没法解读。\n记账失败不许拖垮一章，理由同缝合与归档。\n'
        if self.judgment_sink is None:
            return None
        try:
            self.judgment_sink({
                'ts': datetime.now().isoformat(timespec='seconds'),
                'ch': ch,
                'revision': revision,
                'scores': {s.dimension: s.score for s in verdict.scores},
                'total': verdict.total,
                'lowest': min(s.score for s in verdict.scores),
                'passed': verdict.passed(
                    min_per_dimension=self.judge.min_per_dimension,
                    min_total=self.judge.min_total,
                ),
                'thresholds': {
                    'per_dimension': self.judge.min_per_dimension,
                    'total': self.judge.min_total,
                },
                'word_count': len(re.sub(r'\s', '', text)),
                'notes': [n.scene_id for n in verdict.notes],
            })
        except Exception as exc:
            self.log(f'  ! 评审记录没写成：{type(exc).__name__}: {exc}')
        return None

    def _ok(self, report: GateReport, verdict: JudgeVerdict | None) -> bool:
        if not report.passed:
            return False
        return verdict is None or verdict.passed(
            min_per_dimension=self.judge.min_per_dimension,
            min_total=self.judge.min_total,
        )

    def _targets(
        self, outline: ChapterOutline, report: GateReport, verdict: JudgeVerdict | None
    ) -> dict[int, list[str]]:
        '把问题映射到场景下标。\n\njudge 的意见自带 scene_id；gate 的多数问题是整章级的统计特征，\n没法归到某一场，只能分摊给全部场景。\n'
        by_index = {}
        index_of = {s.id: i for i, s in enumerate(outline.scenes)}
        if verdict:
            for note in verdict.notes:
                idx = index_of.get(note.scene_id)
                if idx is None:
                    continue
                by_index.setdefault(idx, []).append(f'{note.problem} → {note.fix}')
        chapter_wide = [
            f.message
            for f in report.errors
            if f.rule in frozenset({'paragraph_rhythm', 'style', 'length', 'dialogue_ratio'})
        ]
        if chapter_wide:
            profile = report.style_profile(self.gate.style)
            for i in range(len(outline.scenes)):
                by_index.setdefault(i, []).extend(chapter_wide)
                by_index[i].append(profile)
        claimed = {*frozenset({'paragraph_rhythm', 'style', 'length', 'dialogue_ratio'})}
        local = [str(f) for f in report.errors if f.rule not in claimed]
        if local and not by_index:
            for i in range(len(outline.scenes)):
                by_index[i] = list(local)
        return by_index
