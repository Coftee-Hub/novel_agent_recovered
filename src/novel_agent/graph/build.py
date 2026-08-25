# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/graph/build.py
# 来源   : build.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════


from __future__ import annotations

from pathlib import Path

from langgraph.graph import END, START, StateGraph

from ..agents.pipeline import ChapterPipeline

__doc__ = 'LangGraph 编排 —— 把单章流程拆成可断点续跑的节点图。\n\n## 它比 pipeline.py 多做了什么\n\n`ChapterPipeline.run()` 已经能跑完一章，CLI 的 write 命令也已经做到"每章\n落盘、中断后接着跑"。图层只在一件事上有实质增益：**章内断点**。\n\n一章要跑 6-8 次模型调用、十几分钟。若在缝合阶段崩了（网络断、号池挂），\n没有图层就得从出细纲重来，前面写好的三个场景全部作废。有了 checkpointer，\n恢复时直接从崩的那个节点继续。\n\n代价是把线性流程拆成节点、状态要能序列化。对 140 章的长跑，这笔交易划算。\n\n## 节点\n\n    plan → write_scenes → stitch → gate ─┬─(过)→ judge ─┬─(过)→ archive → END\n                                          │              └─(不过)→ revise ↑\n                                          └─(不过)────────────────→ revise ↑\n\nrevise 回到 stitch（重写的是场景，缝合要重做），修订次数超限则转 END。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: 'LangGraph 编排 —— 把单章流程拆成可断点续跑的节点图。\n\n## 它比 pipeline.py 多做了什么\n\n`ChapterPipeline.run()` 已经能跑完一章，CLI 的 write 命令也已经做到"每章\n落盘、中断后接着跑"。图层只在一件事上有实质增益：**章内断点**。\n\n一章要跑 6-8 次模型调用、十几分钟。若在缝合阶段崩了（网络断、号池挂），\n没有图层就得从出细纲重来，前面写好的三个场景全部作废。有了 checkpointer，\n恢复时直接从崩的那个节点继续。\n\n代价是把线性流程拆成节点、状态要能序列化。对 140 章的长跑，这笔交易划算。\n\n## 节点\n\n    plan → write_scenes → stitch → gate ─┬─(过)→ judge ─┬─(过)→ archive → END\n                                          │              └─(不过)→ revise ↑\n                                          └─(不过)────────────────→ revise ↑\n\nrevise 回到 stitch（重写的是场景，缝合要重做），修订次数超限则转 END。\n',
    8: 'ChapterState',
    12: 'ChapterResultView',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('ChapterState', 0): 'ChapterState',
    ('ChapterState', 1): '图的状态。必须可序列化 —— checkpointer 要把它存进 sqlite。\n\nstory / outline / verdict 等 pydantic 对象用 model_dump() 存，\n在节点里再还原。这是为了让崩溃恢复真的能用。\n',
    ('ChapterState', 2): 'int',
    ('ChapterState', 3): 'ch',
    ('ChapterState', 4): 'str',
    ('ChapterState', 5): 'note',
    ('ChapterState', 6): 'dict',
    ('ChapterState', 7): 'story',
    ('ChapterState', 8): 'volume',
    ('ChapterState', 9): 'dict | None',
    ('ChapterState', 10): 'outline',
    ('ChapterState', 11): 'list[str]',
    ('ChapterState', 12): 'scenes',
    ('ChapterState', 13): 'text',
    ('ChapterState', 14): 'bool',
    ('ChapterState', 15): 'gate_ok',
    ('ChapterState', 16): 'gate_errors',
    ('ChapterState', 17): 'verdict',
    ('ChapterState', 18): 'judge_ok',
    ('ChapterState', 19): 'volume_summary',
    ('ChapterState', 20): 'compress_error',
    ('ChapterState', 21): 'archive_error',
    ('ChapterState', 22): 'revisions',
    ('ChapterState', 23): 'stitch_degraded',
    ('ChapterState', 24): 'dict[str, list[str]]',
    ('ChapterState', 25): 'targets',
    ('ChapterState', 26): 'patch',
    ('ChapterState', 27): 'done_reason',
    ('ChapterResultView', 0): 'ChapterResultView',
    ('ChapterResultView', 1): '把图输出的 dict 适配成 `ChapterResult` 那套字段。\n\nCLI 只认一套结果接口，两条路径（直调 pipeline / 走图）才能共用同一段\n落盘、归档、报错代码 —— 否则图这条路必然长出自己的分支和自己的 bug。\n',
    ('__annotate__', 1): 'out',
    ('__annotate__', 2): 'dict',
    ('__annotate__', 3): 'pipeline',
    ('__annotate__', 4): 'ChapterPipeline',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('ch', 0): 'ch',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'bool',
    ('passed', 0): 'done_reason',
    ('passed', 1): 'passed',
    ('passed', 2): 'stitch_degraded',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('text', 0): 'text',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('revisions', 0): 'revisions',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[str]',
    ('notes', 0): 'done_reason',
    ('notes', 1): '没跑到终点',
    ('notes', 2): 'compress_error',
    ('notes', 3): '卷末压缩失败：',
    ('state', 2): 'story',
    ('patch', 2): 'patch',
    ('outline', 2): 'outline',
    ('gate', 0): '重算一遍 gate 报告。\n\ngate 是纯 Python，重算不花钱；而把 GateReport 对象塞进图状态会连累\ncheckpoint 序列化 —— 那是这条路径上最不该出岔子的地方。\n',
    ('gate', 2): 'story',
    ('gate', 3): 'ch',
    ('verdict', 2): 'verdict',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str | None',
    ('archive_error', 0): 'archive_error',
    ('volume_summary', 2): 'volume_summary',
    ('__annotate__', 1): 'pipeline',
    ('__annotate__', 2): 'ChapterPipeline',
    ('build_graph', 0): '装配并编译节点图（无 checkpoint）。要断点续跑用 `checkpointed_graph`。',
    ('__annotate__', 1): 'pipeline',
    ('__annotate__', 2): 'ChapterPipeline',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'StateGraph',
    ('_graph_builder', 0): '装配节点图。\n\npipeline 里已经有全部业务逻辑，节点只负责搬运状态 —— 这样两条路径\n（直接调 pipeline vs 走图）行为一致，不会各自演化出不同的 bug。\n',
    ('_graph_builder', 27): 'plan',
    ('_graph_builder', 28): 'write_scenes',
    ('_graph_builder', 29): 'stitch',
    ('_graph_builder', 30): 'gate',
    ('_graph_builder', 31): 'judge',
    ('_graph_builder', 32): 'revise',
    ('_graph_builder', 33): 'archive',
    ('_graph_builder', 34): 'give_up',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'StoryState',
    ('_story', 0): 'story',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'ChapterOutline',
    ('_outline', 0): 'outline',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('plan', 0): 'outline',
    ('plan', 1): 'revisions',
    ('plan', 2): 'volume',
    ('plan', 3): 'ch',
    ('plan', 4): 'note',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('write_scenes', 0): 'scenes',
    ('<lambda>', 0): 'ch',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('stitch', 0): 'scenes',
    ('stitch', 1): 'ch',
    ('stitch', 2): 'revisions',
    ('stitch', 4): 'text',
    ('stitch', 5): 'stitch_degraded',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('run_gate', 0): 'text',
    ('run_gate', 1): 'ch',
    ('run_gate', 3): 'gate_ok',
    ('run_gate', 4): 'gate_errors',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('run_judge', 0): 'text',
    ('run_judge', 1): 'ch',
    ('run_judge', 2): 'revisions',
    ('run_judge', 4): 'verdict',
    ('run_judge', 5): 'judge_ok',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('revise', 2): 'text',
    ('revise', 3): 'ch',
    ('revise', 5): 'verdict',
    ('revise', 7): 'scenes',
    ('revise', 8): 'revisions',
    ('revise', 11): '.r',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('archive', 2): 'volume',
    ('archive', 3): 'text',
    ('archive', 4): 'done_reason',
    ('archive', 5): 'passed',
    ('archive', 6): 'story',
    ('archive', 7): 'archive_error',
    ('archive', 8): ': ',
    ('archive', 10): 'patch',
    ('archive', 11): 'ch',
    ('archive', 12): 'volume_summary',
    ('archive', 13): '（补做：novel-agent compress ',
    ('archive', 14): '）',
    ('archive', 15): 'compress_error',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('after_gate', 0): 'stitch_degraded',
    ('after_gate', 1): 'give_up',
    ('after_gate', 2): 'gate_ok',
    ('after_gate', 3): 'judge',
    ('after_gate', 4): 'revisions',
    ('after_gate', 5): 'revise',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('after_judge', 0): 'judge_ok',
    ('after_judge', 1): 'archive',
    ('after_judge', 2): 'revisions',
    ('after_judge', 3): 'revise',
    ('after_judge', 4): 'give_up',
    ('__annotate__', 1): 's',
    ('__annotate__', 2): 'ChapterState',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'dict',
    ('give_up', 0): 'stitch_degraded',
    ('give_up', 1): 'done_reason',
    ('give_up', 2): '缝合降级为机械拼接（接缝未打磨、章末钩子未处理）—— 正文是好的，渠道恢复后重跑即可',
    ('give_up', 3): '修订 ',
    ('give_up', 4): 'revisions',
    ('give_up', 5): ' 轮后仍未通过',
    ('__annotate__', 1): 'pipeline',
    ('__annotate__', 2): 'ChapterPipeline',
    ('__annotate__', 3): 'checkpoint_db',
    ('__annotate__', 4): 'str | Path',
    ('checkpointed_graph', 0): '带 sqlite checkpoint 的图，用 with 打开。\n\n以前这里是 `return g, SqliteSaver.from_conn_string(...)` —— 把图和一个\n**还没进入**的上下文管理器一起扔给调用方，调用方得自己知道要 with 一下、\n再自己 compile。结果就是没人用：CLI 一直直调 pipeline，checkpoint 形同\n虚设，第 3 章两次崩在缝合都得从出细纲重来。\n\n编译期把 checkpointer 装进去，调用方只拿到一个能 invoke 的图。\n',
}



# ───────────── 代码骨架（签名/docstring 原样）─────────────

# TODO(重建): 需确认基类 —— 骨架未含基类（LangGraph 状态通常为 typing.TypedDict）。
class ChapterState:
    '图的状态。必须可序列化 —— checkpointer 要把它存进 sqlite。\n\nstory / outline / verdict 等 pydantic 对象用 model_dump() 存，\n在节点里再还原。这是为了让崩溃恢复真的能用。\n'
    ch: int
    note: str
    story: dict
    volume: dict
    outline: dict | None
    scenes: list[str]
    text: str
    gate_ok: bool
    gate_errors: list[str]
    verdict: dict | None
    judge_ok: bool
    volume_summary: dict | None
    compress_error: str
    archive_error: str
    revisions: int
    stitch_degraded: bool
    targets: dict[str, list[str]]
    patch: dict | None
    done_reason: str


class ChapterResultView:
    '把图输出的 dict 适配成 `ChapterResult` 那套字段。\n\nCLI 只认一套结果接口，两条路径（直调 pipeline / 走图）才能共用同一段\n落盘、归档、报错代码 —— 否则图这条路必然长出自己的分支和自己的 bug。\n'

    def __init__(self, out: dict, pipeline: ChapterPipeline) -> None:
        self._out = out
        self._pipeline = pipeline

    @property
    def ch(self) -> int:
        return self._out['ch']

    @property
    def passed(self) -> bool:
        return self._out.get('done_reason') == 'passed' and not self._out.get('stitch_degraded')

    @property
    def text(self) -> str:
        return self._out.get('text', '')

    @property
    def revisions(self) -> int:
        return self._out.get('revisions', 0)

    @property
    def notes(self) -> list[str]:
        reason = self._out.get('done_reason', '没跑到终点')
        notes = [] if self.passed else [reason]
        if self._out.get('compress_error'):
            notes.append(f'卷末压缩失败：{self._out["compress_error"]}')
        return notes

    @property
    def state(self):
        from ..state.schema import StoryState
        return StoryState.model_validate(self._out['story'])

    @property
    def patch(self):
        from ..state.schema import StatePatch
        raw = self._out.get('patch')
        if raw:
            return StatePatch.model_validate(raw)
        return None

    @property
    def outline(self):
        from ..agents.schemas import ChapterOutline
        return ChapterOutline.model_validate(self._out['outline'])

    @property
    def gate(self):
        '重算一遍 gate 报告。\n\ngate 是纯 Python，重算不花钱；而把 GateReport 对象塞进图状态会连累\ncheckpoint 序列化 —— 那是这条路径上最不该出岔子的地方。\n'
        from ..state.schema import StoryState
        return self._pipeline.gate.check(
            self.text,
            state=StoryState.model_validate(self._out['story']),
            expected_ch=self._out['ch'],
        )

    @property
    def verdict(self):
        from ..agents.judge import JudgeVerdict
        raw = self._out.get('verdict')
        if raw:
            return JudgeVerdict.model_validate(raw)
        return None

    @property
    def archive_error(self) -> str | None:
        return self._out.get('archive_error')

    @property
    def volume_summary(self):
        from ..state.schema import VolumeSummary
        raw = self._out.get('volume_summary')
        if raw:
            return VolumeSummary.model_validate(raw)
        return None


def build_graph(pipeline: ChapterPipeline) -> StateGraph:
    '装配并编译节点图（无 checkpoint）。要断点续跑用 `checkpointed_graph`。'
    return _graph_builder(pipeline).compile()


def _graph_builder(pipeline: ChapterPipeline) -> StateGraph:
    '装配节点图。\n\npipeline 里已经有全部业务逻辑，节点只负责搬运状态 —— 这样两条路径\n（直接调 pipeline vs 走图）行为一致，不会各自演化出不同的 bug。\n'
    from ..agents.schemas import ChapterOutline, VolumeOutline
    from ..state.schema import StoryState

    def _story(s: ChapterState) -> StoryState:
        return StoryState.model_validate(s['story'])

    def _outline(s: ChapterState) -> ChapterOutline:
        return ChapterOutline.model_validate(s['outline'])

    def plan(s: ChapterState) -> dict:
        if s.get('outline'):
            return {'outline': s['outline'], 'revisions': s.get('revisions', 0)}
        outline = pipeline.architect.plan_chapter(
            _story(s),
            VolumeOutline.model_validate(s['volume']),
            ch=s['ch'],
            note=s.get('note', ''),
        )
        if pipeline.outline_sink is not None:
            pipeline.outline_sink(outline)
        return {'outline': outline.model_dump(), 'revisions': 0}

    def write_scenes(s: ChapterState) -> dict:
        story, outline = _story(s), _outline(s)
        rag = pipeline._retrieve(outline)
        scenes = pipeline.writer.write_chapter_scenes(
            story,
            outline,
            rag=rag,
            already=s.get('scenes') or None,
            on_scene=lambda spec, txt: pipeline._save_draft(s['ch'], spec.id, txt),
        )
        return {'scenes': scenes}

    def stitch(s: ChapterState) -> dict:
        text, degraded = pipeline._stitch(
            _outline(s),
            s['scenes'],
            s['ch'],
            revision=s.get('revisions', 0),
        )
        return {'text': text, 'stitch_degraded': degraded}

    def run_gate(s: ChapterState) -> dict:
        report = pipeline.gate.check(
            s['text'],
            state=_story(s),
            expected_ch=s['ch'],
        )
        return {
            'gate_ok': report.passed,
            'gate_errors': [str(f) for f in report.errors],
        }

    def run_judge(s: ChapterState) -> dict:
        verdict = pipeline.judge.review(
            _story(s),
            _outline(s),
            s['text'],
        )
        pipeline.record_judgment(s['ch'], s.get('revisions', 0), verdict, s['text'])
        ok = verdict.passed(
            min_per_dimension=pipeline.judge.min_per_dimension,
            min_total=pipeline.judge.min_total,
        )
        return {'verdict': verdict.model_dump(), 'judge_ok': ok}

    def revise(s: ChapterState) -> dict:
        from ..agents.judge import JudgeVerdict
        story, outline = _story(s), _outline(s)
        report = pipeline.gate.check(
            s['text'],
            state=story,
            expected_ch=s['ch'],
        )
        verdict = JudgeVerdict.model_validate(s['verdict']) if s.get('verdict') else None
        targets = pipeline._targets(outline, report, verdict)
        scenes = list(s['scenes'])
        n = s.get('revisions', 0) + 1
        for idx, problems in sorted(targets.items()):
            scenes[idx] = pipeline.writer.revise_scene(
                story,
                outline,
                outline.scenes[idx],
                scenes[idx],
                problems,
                prev_text=scenes[idx - 1] if idx else '',
            )
            pipeline._save_draft(s['ch'], f'{outline.scenes[idx].id}.r{n}', scenes[idx])
        return {'scenes': scenes, 'revisions': n}

    def archive(s: ChapterState) -> dict:
        from ..state import apply_patch, apply_volume_summary
        story, outline = _story(s), _outline(s)
        vol = VolumeOutline.model_validate(s['volume'])
        try:
            patch = pipeline.archivist.archive(story, outline, s['text'])
        except Exception as exc:
            return {
                'done_reason': 'passed',
                'story': s['story'],
                'archive_error': f'{type(exc).__name__}: {exc}',
            }
        merged = apply_patch(story, patch)
        out = {'patch': patch.model_dump(), 'done_reason': 'passed'}
        if s['ch'] == vol.ch_end:
            try:
                summary = pipeline.archivist.compress_volume(merged, vol)
            except Exception as exc:
                out['compress_error'] = f'{type(exc).__name__}: {exc}（补做：novel-agent compress {vol.volume}）'
            else:
                merged = apply_volume_summary(merged, summary)
                out['volume_summary'] = summary.model_dump()
        out['story'] = merged.model_dump()
        return out

    def after_gate(s: ChapterState) -> str:
        if s.get('stitch_degraded'):
            return 'give_up'
        if s['gate_ok']:
            return 'judge'
        if s.get('revisions', 0) < pipeline.max_revisions:
            return 'revise'
        return 'give_up'

    def after_judge(s: ChapterState) -> str:
        if s['judge_ok']:
            return 'archive'
        if s.get('revisions', 0) < pipeline.max_revisions:
            return 'revise'
        return 'give_up'

    def give_up(s: ChapterState) -> dict:
        if s.get('stitch_degraded'):
            return {'done_reason': '缝合降级为机械拼接（接缝未打磨、章末钩子未处理）—— 正文是好的，渠道恢复后重跑即可'}
        return {'done_reason': f'修订 {s.get("revisions", 0)} 轮后仍未通过'}

    g = StateGraph(ChapterState)

    for name, fn in [
        ('plan', plan),
        ('write_scenes', write_scenes),
        ('stitch', stitch),
        ('gate', run_gate),
        ('judge', run_judge),
        ('revise', revise),
        ('archive', archive),
        ('give_up', give_up),
    ]:
        g.add_node(name, fn)

    g.add_edge(START, 'plan')
    g.add_edge('plan', 'write_scenes')
    g.add_edge('write_scenes', 'stitch')
    g.add_edge('stitch', 'gate')
    g.add_conditional_edges(
        'gate',
        after_gate,
        {
            'judge': 'judge',
            'revise': 'revise',
            'give_up': 'give_up',
        },
    )
    g.add_conditional_edges(
        'judge',
        after_judge,
        {
            'archive': 'archive',
            'revise': 'revise',
            'give_up': 'give_up',
        },
    )
    g.add_edge('revise', 'stitch')
    g.add_edge('archive', END)
    g.add_edge('give_up', END)

    return g


def checkpointed_graph(pipeline: ChapterPipeline, checkpoint_db: str | Path):
    '带 sqlite checkpoint 的图，用 with 打开。\n\n以前这里是 `return g, SqliteSaver.from_conn_string(...)` —— 把图和一个\n**还没进入**的上下文管理器一起扔给调用方，调用方得自己知道要 with 一下、\n再自己 compile。结果就是没人用：CLI 一直直调 pipeline，checkpoint 形同\n虚设，第 3 章两次崩在缝合都得从出细纲重来。\n\n编译期把 checkpointer 装进去，调用方只拿到一个能 invoke 的图。\n'
    from langgraph.checkpoint.sqlite import SqliteSaver
    Path(checkpoint_db).parent.mkdir(parents=True, exist_ok=True)
    builder = _graph_builder(pipeline)
    with SqliteSaver.from_conn_string(str(checkpoint_db)) as saver:
        yield builder.compile(checkpointer=saver)
