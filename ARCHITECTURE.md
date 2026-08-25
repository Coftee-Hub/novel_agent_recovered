# 《落款》代码全览

这份文档回答一个问题：**每个模块负责什么，以及为什么是这个形状**。

三份文档的分工：

| 文档 | 回答什么 |
|---|---|
| `README.md` | 供应商实测结论、成本账、怎么把环境跑起来 |
| `HANDOFF.md` | **当前进度**、五条最容易被误改的设计、已知问题 |
| 本文 | 代码结构：模块职责、依赖方向、不变量守在哪 |

每个决策的**理由写在代码注释里**，这里只讲结构。真要改某处之前，先读那处的注释。

---

## 一、一条稿子怎么走完全程

```
                   人：确认卷大纲（唯一的人工断点）
                            │
config/*.yaml ─┐            ▼
skills/*.md  ──┼──→ architect ──→ 章细纲 + 场景规格（2-4 场）
book/story_   ─┘                        │
  state.json                            ▼
                          writer ──→ 逐场景正文（串行，每场看得到上一场结尾）
                                        │
                                        ▼
                        stitcher ──→ 缝合成整章（只调接缝）
                                        │
                                        ▼
                   gate（纯 Python，0 次调用）── 不过 ─┐
                                        │ 过           │
                                        ▼              │
                   judge（7 维打分 + 定位到场景的修改意见）
                                        │ 不过 ────────┤
                                        │ 过           ▼
                                        │        定向修订（≤2 轮）
                                        ▼              │
                   archivist ──→ StatePatch ──→ 合并进 state
                                        │        （超限 → needs_human）
                                        ▼
                          book/chapters/ch_XXX.md
```

**成本形状**：一章约 13 次调用、$0.30。其中 architect 1 次、writer 3-6 次、
stitcher 1-2 次（最长的单次调用，实测 90-970 秒）、judge 与 archivist 各 1-2 次
（走 DeepSeek，计价表未填，记 0）。

---

## 二、分层与依赖方向

```
cli.py ──────────────→ graph/ ──→ agents/ ──→ llm/ ──→ backends/
   │                                 │  │        │
   └─────────────────────────────────┘  ├──→ state/
                                        └──→ corpus/   skills.py
```

依赖是单向的：**下层不认识上层**。`agents/` 不知道命令行的存在，`llm/` 不知道
小说的存在，`state/` 谁都不认识。所以换掉 CLI 不影响 agents，换掉供应商只动
`llm/backends/`。

---

## 三、模块逐个说

### `llm/` —— 模型调用层（1036 行）

这一层的存在理由是**成本**：prompt 缓存是前缀匹配，前缀里错一个字节，
几万 token 就要全价重算。

| 文件 | 职责 | 关键设计 |
|---|---|---|
| `prompt_builder.py` | **全项目唯一的 prompt 组装入口** | 四层结构，稳定的在前、易变的在后；`audit()` 主动扫描稳定层里的时间戳/UUID —— 缓存失效不会报错，只会让账单静默翻倍，所以由测试守着 |
| `client.py` | 统一调用入口：路由 → 后端 → 归一化 → 记账 | `complete()` 出散文，`parse()` 出结构化；每次调用逐行追加进 `run_log.jsonl`（token/缓存/耗时/成本/前缀指纹） |
| `router.py` | 逐角色的模型路由 + 成本核算 | 角色 → 供应商+模型+fallback 链；`cost_usd()` 按 usage 算钱，缓存读按 0.1 倍计 |
| `json_mode.py` | 结构化输出的兜底路径 | 中转站会剥掉 `output_config.format`，于是把 schema 追加进 **instruction**（易变层，不动缓存前缀）+ 宽松解析 + 一次定向修复 |
| `backends/base.py` | 后端抽象 + 额外重试 | 只重试 SDK **自己不重试**的状态码（403/422），重复列会变成乘法重试 |
| `backends/anthropic_backend.py` | Anthropic 原生协议 | `cache_control` 断点只在这条路上有效 |
| `backends/openai_backend.py` | OpenAI 兼容协议 | 结构化输出逐级降级：严格 schema → json_object → 纯文本 |

**为什么不用 LangChain 发请求**：需要在指定内容块上精确放 `cache_control`、
需要读 `usage.cache_read_input_tokens` 做验收 —— 这两件事经过一层封装都容易静默失效。
LangGraph 只用来编排。

### `state/` —— 全书唯一事实源（524 行）

| 文件 | 职责 | 关键设计 |
|---|---|---|
| `schema.py` | Pydantic 类型定义 | **人物内核跨阶段恒定**：`core_wound`/`speech_habits`/`value_line` 挂在 `Character` 上，只有 `arcs` 随阶段变 —— "时间一跳人物像换了个人"这个崩法被类型系统挡住，不靠提示词自觉 |
| `store.py` | 读写 + patch 合并 + 引用完整性校验 | **原子写入**（事实源写到一半崩溃会毁掉整本书的记忆）；`apply_patch()` 返回新对象，绝不原地改 |
| `bible.py` | JSON → `story_bible.md` 渲染 | 人读渲染产物，机器读 JSON。不让模型自由写 markdown 记忆 —— 几十章后必然字段漂移 |

**两层摘要的分界线**在 `StoryState.live_summaries()`：进上下文的章级摘要是
「尚未被卷梗概覆盖的那些」，往卷只留一段梗概。用"有没有被压缩过"划界而不是
"最近 N 章"，是因为 N 与故事结构无关 —— 旧的 N=10 会让第 11 章再也看不到第 1 章，
而那时本卷还没结束、卷梗概还没产生。

三个字段撑起了整个设计：`core_wound`（人物动机的根）、`EmotionalDebt.due_by_ch`
（让 gate 能机械检查"第 12 章埋的伏笔到第 60 章还没收"，防烂尾且零调用）、
`UsedBeat`（写之前塞给 architect 一份"这些桥段用过，不许重复"）。

### `agents/` —— 六个角色（1734 行）

| 文件 | 角色 | 职责 |
|---|---|---|
| `architect.py` | 卷大纲 → 章细纲 → 场景规格 | 唯一带人工确认断点的节点（卷级） |
| `writer.py` | `Writer` 逐场景写正文 | 一次只写一场，看得到上一场结尾和本场规格，看不到全章 |
| `writer.py` | `Stitcher` 缝合 | 只调接缝不重写；比对字数（保留率 <60% 判定崩了）并检查结尾是否落在完整句上 |
| `gate.py` | 确定性闸门 | **零 LLM 调用**：字数、标点、段落、对话、文风统计、n-gram 抄袭、情感债到期 |
| `judge.py` | 7 维质量评审 | 输出结构化评分 + **定位到具体场景**的修改指令，不是笼统的"再细腻些" |
| `archivist.py` | 归档 + 卷末压缩 | 把一章读成 `StatePatch` 增量；卷末再把整卷压成一段 `VolumeSummary`。**刻意收不到全量设定集**（否则会归档错对象） |
| `pipeline.py` | 单章闭环编排 | 出细纲 → 写 → 缝 → 检 → 定向修订（≤2 轮）→ 归档 |
| `schemas.py` | architect 的输出契约 | `SceneSpec` 是 architect 与 writer 之间的接口；情绪起止相同的场景在出图阶段就被拦下 |
| `prompts.py` | 各角色的角色定义文本 | prompt 里的数字是**瞄准点**，config 里的是**验收线**，两者故意不相等 |

**gate 在 judge 之前跑**：格式不合规的稿子不该浪费一次 LLM 评审。
**修订只重写被点名的那一场**，但整章级的文风问题定位不到单场，只能分摊给全部场景 ——
此时必须给**完整文风剖面**（通过的项也列出来），只给失败项会打地鼠。

### `corpus/` —— 语料处理（1028 行）

| 文件 | 职责 | 状态 |
|---|---|---|
| `ingest.py` | EPUB/TXT 清洗、分章、标点归一 | 在用 |
| `extract.py` | 从范本萃取写作手法 → skills 草稿 | 已完成使命，6 份 skills 已定稿 |
| `index.py` | BM25 检索，给写作提供同类场景参照 | **默认关闭**，实测收益为负 |
| `similarity.py` | n-gram 抄袭检测（连续 13 字相同即硬失败） | 在用（选了 RAG 就必须有这道防线） |

`index.py` 的换血点很小：换向量检索只需替换 `PassageIndex.score()` 一个方法。

### `graph/build.py` —— LangGraph 编排（273 行）

`pipeline.py` 已经能跑完一章，图层只在一件事上有实质增益：**章内断点**。
一章十几分钟、6-8 次调用，缝合阶段崩了不该让前面写好的场景作废。

节点：`plan → write_scenes → stitch → gate →(过) judge →(过) archive`，
不过则 `revise`（回到 stitch，因为重写的是场景），超过 2 轮转 `give_up`。
业务逻辑全在 `pipeline` 里，节点只搬运状态 —— 两条路径不会各自长出不同的 bug。

`ChapterResultView` 把图输出的 dict 适配成 `ChapterResult` 那套字段，
让 CLI 的落盘/归档/报错代码两条路共用。

### `cli.py` —— 命令行入口（562 行）

`build()` 是**唯一的组件装配点**，所有命令共享，避免各命令各自 new 一遍而配置漂移。

| 命令 | 做什么 | 花钱 |
|---|---|---|
| `status` | 进度 / 成本 / 逾期的情感债 | 否 |
| `init` | 立项：写入初始人物设定 | 否 |
| `index` | 建语料检索索引 | 否 |
| `check <文件>` | 对已有稿件跑一遍 gate | 否 |
| `plan <卷> <起> <止> <阶段>` | 出卷大纲（**要人工确认**） | 1 次 |
| `outline <章>` | 只出章细纲给人看，不写正文 | 1 次 |
| `write` | 写作全流程 | 约 13 次/章 |
| `archive <章>` | 把流水线外写的章节补录进 state | 2 次 |
| `compress <卷>` | 补做卷末压缩（正常由 `write` 自动触发） | 1 次 |

`write` 的开关：`--reuse-outline`（复用人看过的细纲）、`--resume-drafts`
（捡回已写好的场景）、`--graph`（走图 + checkpoint）、`--rag`、`--note`、`-n`。

### `skills/` —— 写作经验库（8 份，约 59K 字符）

人类可读可编辑的 markdown，直接进 prompt。6 份从范本萃取后由人定稿
（`style_voice`/`romance_beats`/`character_design`/`dialogue`/`campus_to_career`/
`cliche_blacklist`），2 份来自规范（`format_spec`/`intimacy_levels`）。

**writer 拿不到三份"设计期"skill**（`character_design`/`romance_beats`/
`campus_to_career`）：它一次只写一场，拿到的是这些设计的**产物**，不需要知道
它们怎么被设计出来。剔掉后 writer 的 system_core 从 41K 降到 22K token。

### `config/`

- `project.yaml` —— 字数/标点/段落/文风区间/judge 阈值/亲密尺度。所有数字都标了来源
  （18 本同题材范本实测，不是拍脑袋）
- `models.yaml` —— 逐角色的供应商路由、重试策略、计价表

---

## 四、产物目录 `book/`

| 路径 | 是什么 | 谁写的 |
|---|---|---|
| `story_state.json` | **唯一事实源** | archivist 的 patch 合并后 |
| `story_bible.md` | 人读视图 | 由 JSON 渲染，不要手改 |
| `chapters/ch_XXX.md` | 正式成稿 | 只有通过全部检查才落这里 |
| `chapters/_versions/` | 被覆盖掉的旧成稿 | 重跑已有章节时自动归档 |
| `outlines/vol_XX.*` | 卷大纲（人确认过） | `plan` |
| `outlines/ch_XXX.*` | 章细纲 | 生成的那一刻就落盘 |
| `outlines/_versions/` | 旧版大纲 | 覆盖前自动归档 |
| `drafts/ch_XXX/` | 场景草稿、缝合稿、修订稿 | 每写完一段就存 |
| `drafts/ch_XXX.vNN/` | 细纲改版后退休的旧草稿 | 自动 |
| `needs_human/` | 修订超限仍不合格的稿子 | **绝不覆盖已有成稿** |
| `checkpoints.sqlite` | 图的节点级存档 | `--graph` |
| `run_log.jsonl` | 每次调用的 token/缓存/耗时/成本 | `LLMClient` |

### 四层保护，各管各的

| 层 | 保住什么 | 崩了/改了之后 |
|---|---|---|
| `drafts/` | 已经花掉的钱（每场正文） | `--resume-drafts` 只补没写完的场景 |
| `checkpoints.sqlite` | 已经走过的流程 | `--graph` 从崩掉的节点续跑 |
| `_versions/` | 被覆盖掉的大纲与成稿 | 直接取回 |
| 每章落盘 state | 已经写完的章节 | 重跑从下一章开始 |

两个防呆：细纲一改版，这一章的旧草稿自动退休（否则 `--resume-drafts` 会捡回
照旧要求写的东西）；`--graph` 续跑前比对 checkpoint 里的细纲，不一致就不续旧档。

---

## 五、测试地图（318 个用例）

测试不是为覆盖率写的，每个文件守着一类**会静默出错**的东西：

| 文件 | 用例 | 守什么 |
|---|---|---|
| `test_state.py` | 35 | patch 合并、引用完整性、bible 渲染 |
| `test_gate.py` | 31 | 每条格式规范的正反样本 |
| `test_architect.py` | 31 | 输出契约与上下文分层 |
| `test_pipeline.py` | 31 | 修订收敛、未通过不归档、草稿落盘 |
| `test_prompt_builder.py` | 27 | **`cache_control` 位置正确、RAG 在最后** —— 缓存失效不报错，只能靠测试 |
| `test_ingest.py` | 24 | 清洗与分章 |
| `test_writer.py` | 23 | 上下文分层（含"设计期 skill 不进 writer"） |
| `test_config_wiring.py` | 21 | 哪个角色用哪家 —— 改路由是有代价的决定 |
| `test_router.py` | 19 | 路由与成本核算 |
| `test_index.py` / `test_skills.py` | 16 / 16 | 检索、skills 拼装 |
| `test_graph.py` | 14 | 节点连线、分支、checkpoint 续跑 |
| `test_retry.py` | 14 | 只重试 SDK 不重试的那些 |
| `test_versions.py` | 9 | 覆盖前留旧版 |
| `test_cli_graph.py` | 7 | CLI 真的走上了图这条路 |

```bash
.venv/bin/python -m pytest -q      # 全部，约 1.5 秒，不打任何真实 API
```

---

## 六、这份代码里还缺什么

见 `TODO.md`（分档标准是**不做会怎样**，不是工作量）与 `HANDOFF.md` 的「已知问题」。
当前最要紧的两条：**Phase 7 的连续 5 章验收从没做过**；**修订环对"细纲与文风
目标打架"的章节收敛不了**（第 3 章实证：一轮把心理密度修好，句长和段落又坏了）。
