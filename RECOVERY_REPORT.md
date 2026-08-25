# novel_agent 代码恢复报告

> 生成时间：2026-08-25
> 背景：`/Users/weizihang/Desktop/agent制作/novel_agent` 的 `.py` 源码被机器上的透明文档加密 DLP（联软 UniAccess / 天锐）加密为 `%TSD-Header-###%` 密文。本目录是从**加密前编译的 `.pyc` 字节码**恢复的项目副本，与原加密目录互不影响。

## 恢复方法与可信度分层

| 分层 | 说明 | 可信度 |
|---|---|---|
| **A 原样拷贝** | 未被 DLP 加密的 `.py`，直接复制原文件 | 100% 原版 |
| **B 字符串/签名/docstring** | 从 `.pyc` 用明文 Python 3.14 原生 `marshal` 读取 | 100% 原样 |
| **C 函数体重建** | 由字节码 `dis` 反汇编 + 常量表还原逻辑 | 尽力还原，个别处留 `# TODO(重建)` |
| **D 无法恢复** | 无对应 `.pyc`（模块从未被 import/编译） | 缺失 |

## 总览

- 全项目 `.py` 共 **64** 个
- ✅ **A 原样拷贝：15 个**
- ✅ **B+C 从 pyc 重建：41 个**，其中：
  - **23 个核心模块**已完成**函数体重建**（字符串/签名/docstring 100% 原样 + 函数体从字节码还原 + 全量编译通过）
  - **18 个文件**（16 测试 + 2 scripts）为**骨架恢复**（字符串/签名/docstring 100% 原样，函数体保留为反汇编注释，未做函数体重建）
- ❌ **D 无法恢复：8 个**（无对应 pyc）

## 关键校验结果

- **全量语法编译：56/56 通过**（明文 Python 3.14.6 `py_compile`）
- **运行时验证**：恢复出的 `test_router.py`+`test_retry.py` 33 通过、`test_prompt_builder.py` 38 通过、1 跳过；gate/architect/state/corpus/llm 各模块用桩依赖做了行为实测
- **原样性**：`_RECOVERED_CONSTS` / `_RECOVERED_FN_CONSTS` 常量表、全部函数签名、全部 docstring、模块 `__doc__` —— 各代理均做了逐字节比对，**一致**

## 函数体重建完成的核心模块（23 个）

| 模块 | 重建内容 |
|---|---|
| `agents/writer.py` | Writer/Stitcher/StitchFailed，17 个代码对象，含缝合、修订、引号规范化 |
| `agents/gate.py` | Gate 检查器 + GateReport + Finding，全部检查项 |
| `agents/architect.py` | Architect 大纲设计，plan_volume/plan_chapter |
| `agents/pipeline.py` | ChapterPipeline 状态机主循环 |
| `agents/archivist.py` | 归档 + 卷末压缩 |
| `agents/prompts.py` | ARCHITECT_ROLE / WRITER_ROLE / STITCHER_ROLE |
| `agents/schemas.py` | SceneSpec/ChapterOutline/VolumeOutline 等 pydantic 模型 |
| `cli.py` | Typer CLI：10 命令 + 16 辅助函数 |
| `graph/build.py` | LangGraph 构图 + checkpointed_graph |
| `state/schema.py` | 12 个 pydantic 模型（StoryState 等） |
| `state/store.py` | StateStore + apply_patch |
| `state/bible.py` | 设定集渲染 6 函数 |
| `corpus/ingest.py` | epub/txt 解析、分章 |
| `corpus/extract.py` | 语料萃取 Extractor |
| `corpus/index.py` | BM25 索引 + SceneRetriever |
| `skills.py` | SkillLibrary |
| `llm/` 7 个 | LLMClient/Router/Prompt/json_mode/backends |

## 骨架恢复（函数体未重建，18 个）

- `tests/` 16 个（test_writer/test_gate/test_ingest 等）— 字符串/签名/docstring 原样，函数体为反汇编注释
- `scripts/classify_corpus.py`、`scripts/extract_skills.py`

## 已知不完整 / 留 TODO 处（无法从 pyc 还原，未编造）

1. **缺失的枚举类型定义**：`Stage` / `RelationStage` / `DebtKind`（state/schema.py）、`IntimacyLevel`（agents/schemas.py）——pyc 里只有字符串注解，枚举本体在加密原文件中丢失，需按使用处补定义。
2. **模块级常量**：gate.py 的 `STYLE_MARKERS` 词表、skills.py 的 `WRITER_SKILLS`/`ARCHITECT_SKILLS` 内容、ingest.py 若干阈值常量——只在常量表里有名字或零散值，词表/列表本体不可还原。
3. **cli.py 的装饰器**：10 个命令的 `@app.command()` 及选项参数（Typer CLI 确认无疑，但参数具体值不可还原）。
4. **类基类**：`ChapterResult` / `ChapterState` 的基类（pydantic / dataclass / TypedDict 不定）。
5. **若干 import 需确认**：writer 的 `WRITER_SKILLS` 来源、prompt_builder 的 `PromptLayerError` 基类等（均以 `# TODO(重建)` 标注在代码里）。

## D. 无法恢复（8 个，无对应 pyc）

- scripts/bootstrap_story.py、scripts/check_setup.py、scripts/plan_volume.py、scripts/select_corpus.py、scripts/verify_cache.py、scripts/write_chapter.py
- snapshots/v1_low_psychology/prompts.py、snapshots/v2_planA/prompts.py

> 这些文件的**业务逻辑可参考**项目内完好的 HANDOFF.md / ARCHITECTURE.md / README.md 与根目录那份《设计与落地方案》（agent-agent-agent-ai-agent-1-ai-2-agent-groovy-hickey_副本.md）。

## 后续建议

1. **正路仍是让 IT 把开发工具加入 DLP 白名单**，直接读原目录明文最可靠。
2. 本目录为独立副本；重建出的函数体建议按 `# TODO(重建)` 逐一核对后再用于运行。
3. 如需继续：可对 18 个骨架文件（tests/scripts）继续做函数体重建，或补缺失的枚举/常量定义。
