# 言情小说写作 Agent 系统

现代都市 + 大学校园言情的自动写作流水线。人只做两件事：提供模板小说、确认卷级大纲。

## 快速开始

```bash
uv venv && uv pip install -e ".[dev,openai]"
cp .env.example .env          # 填入 key，.env 已 gitignore
.venv/bin/python -m pytest -q
```

然后按顺序做两次验证：

```bash
.venv/bin/python scripts/check_setup.py          # 连通性 + 实际可用模型
```

```bash
.venv/bin/python scripts/verify_cache.py writer  # 缓存是否命中（决定成本量级）
```

## 当前接线

| 角色 | 供应商 | 为什么 |
|---|---|---|
| architect / writer / **stitcher** | PackyAPI `cc-sale` → claude-opus-5 | 文笔敏感。stitcher 是最后一道经手正文的工序，必须与 writer 同源，否则文风打架 |
| judge / archivist / extractor | DeepSeek 官方直连 | 只吐结构化 JSON，不需要文笔 |

### ⚠️ 关于 cc-sale 分组

倍率 0.8，是最便宜的 Claude 分组（cc=2 / cc-expensive=2.2 / claude-officially=7），
且**支持第三方接入**——本项目是自己的 Python 程序，属于第三方，这一条是硬要求。
`cc` 分组明确禁止第三方接入，违者封号并进入退款流程，**不要把令牌建在 cc**。

### cc-sale 实测结论（2026-08-19 首测 / 2026-08-21 复核）

官方警告「此分组缓存可能会有异常」。8-19 首测确实是 `cache_creation` 与
`cache_read` 恒为 0（`cache_control` 被中转站吞掉）——**但这个结论在 8-20 之后
不再成立**：8-21 复核 run_log，当天 41 次调用里 23 次 `cache_read` 非零，
累计读回 110 万 token。所以是渠道侧的间歇性行为，不是我方请求的问题，
**别照着"缓存不生效"去做架构取舍**（`prompt_builder` 的分层现在真的在省钱）。

成本按 run_log 实测重算（这条渠道只要官方价的约 11%）：

| 方案 | 全书估算（140 章）|
|---|---|
| **cc-sale 带缓存（实测每章 $0.30）** | **约 $42** |
| cc-sale 若缓存全不命中 | 约 $58（同批实测反推，贵 27%）|
| 官方价 + 缓存正常 | 约 $45 |
| 官方价 无缓存 | 约 $196 |

每章 $0.30 是含修订轮的真实值（第 2 章 13 次调用）。早先 $22 的估算按"一章一遍
过"算，偏乐观。DeepSeek 三角色未填计价表，run_log 记 0。

另一个实测问题是**号池间歇性 403**：同样字节的请求有时 200 有时 403，
失败在 0.5s 内返回、成功要 7-8s，原始成功率约 10-20%。这是 packyapi 转述
上游账号失效，不是对我方的鉴权拒绝。SDK 按语义不重试 403，故在
`config/models.yaml` 里显式配了 `retry_on_status: [403, ...]` + `max_retries: 8`。
**加重试后端到端 6/6 成功**，平均 6.5s/次（含重试等待）。

第三个实测问题是**结构化输出被剥掉**：请求里的 `output_config.format` 不被受理，
模型返回 markdown 散文而非 JSON。影响 architect（judge / archivist 走 DeepSeek，
另行验证）。已实现兜底路径：把 JSON schema 追加到 instruction（易变层，不动缓存
前缀）+ 宽松解析（容忍 ``` 围栏与前后废话）+ 一次定向修复。供应商配
`supports_structured_output: false` 走兜底；配 `None` 则首次调用自动探测。

`prompt_builder` 的缓存分层设计**已在此渠道生效**（见上方 8-21 复核）。
跑之前仍建议 `scripts/verify_cache.py` 确认一次——这条渠道的缓存是间歇性的。

### 退路：aws-q（不到万不得已不用）

| 分组 | 倍率 | 模型 | 问题 |
|---|---|---|---|
| cc-sale（主） | 0.8 | 7 个，含 opus-5 | 缓存可能异常 |
| aws-q（退路） | **0.3** | **同样 7 个，含 opus-5** | 易出 422；上下文 200K |

模型清单与 cc-sale 完全一致，倍率还便宜 2.67 倍。两个代价：

- **上下文 200K**（非 opus-5 官方的 1M）。本项目单次输入约 25-45K，**不构成约束**。
- **易出 422**。anthropic SDK 默认只重试连接错误 / 408 / 409 / 429 / 5xx，
  **422 不在其中**——自动跑 N 章撞一次就整轮中断。所以 `packyapi_awsq` 显式配了
  `retry_on_status: [422]`。注意这个列表**只填 SDK 不管的码**，把 429/5xx 再列一遍
  会变成乘法重试，失败时白等很久。

切换方式（把三个文笔角色改到退路）：

```bash
sed -i '' 's/    provider: packyapi$/    provider: packyapi_awsq/' config/models.yaml
```

### DeepSeek 型号

`deepseek-v4-flash`，走官方直连。`check_setup.py` 会核对它是否在你的 key
可见的模型清单里。

## 换模型供应商

架构上只有 `src/novel_agent/llm/backends/` 是供应商相关的，其余代码全部中立。
中转站与官方的认证方式不同：官方用 `x-api-key`，多数中转站用
`Authorization: Bearer`。在 provider 里用 `auth_style: bearer` 切换，搞错必然 401。

**大多数替代品都提供 OpenAI 兼容端点**（DeepSeek、通义千问、智谱 GLM、Kimi、
MiniMax、Ollama、vLLM），所以换供应商只改 `config/models.yaml`，代码一行不动：

```yaml
roles:
  writer:
    provider: deepseek        # 改这一行
    model: deepseek-chat
```

`providers:` 段里已经预置了常见端点。用之前把对应的 key 填进 `.env`，
并在 `pricing:` 里补上价目（不补也能跑，只是成本统计会记 0）。

**可以按角色混用**：`writer` / `stitcher` 用文笔最好的，`judge` / `archivist`
只输出结构化 JSON，不需要文笔，用最便宜的即可。

换完务必跑一次缓存验证：

```bash
.venv/bin/python scripts/verify_cache.py writer
```

第二次调用必须出现 `cache_read > 0`。这个数字决定全书是几十美元还是几百美元。

## 目录

```
config/          项目规范（字数/标点/评分阈值）与模型路由
skills/          写作经验库，直接进 prompt 的 system_core
corpus/          语料（.gitignore，不进版本控制）
src/novel_agent/
  llm/           prompt 分层组装、后端适配、成本记账
  state/         故事状态 schema、patch 合并、bible 渲染
  corpus/        清洗分章、n-gram 抄袭检测
  agents/        gate（零 LLM 闸门）等
book/            产出：章节、story_state.json、run_log.jsonl
examples/        示例 state 与渲染出的 bible
```

## 两条贯穿全项目的硬约束

**1. 缓存前缀不能被污染。** prompt 分四层组装，稳定的在前、易变的在后：

```
system_core   全书不变     ← skills + 硬规范
bible         每卷变一次   ← 人物卡 + 设定
volume        每卷变一次   ← 卷大纲 + 摘要
────────── 以上是缓存前缀，卷内所有章节共享 ──────────
rag / prev_tail / instruction   每次都变
```

`Prompt.audit()` 会主动拦截稳定层里的时间戳与 UUID。缓存失效**不会报错**，
只会让账单静默翻数倍，所以由测试守住。

**2. 人物内核跨阶段恒定。** `core_wound` / `speech_habits` / `value_line` 挂在
`Character` 上，只有 `arcs` 随阶段（大学 → 毕业过渡 → 职场）变。archivist 提交的
patch 在**类型上**就够不到内核字段——"时间一跳人物像换了个人"这个崩法被
类型系统挡住，不靠提示词自觉。

## 进度

**以 `HANDOFF.md` 为准**，那里记的是当前现状（进度、供应商、已知问题、
以及五条最容易被误改的设计）。这里只留一句总览：

Phase 0-7 全部完成并真实跑通 —— LLM 层 / state + gate / 语料萃取（6 份 skills
已定稿）/ architect / writer + stitcher / judge + archivist + 修订环 / RAG
（建成但默认关闭，实测收益为负）/ CLI + LangGraph。第 1 卷大纲已确认，
正文在逐章产出中。
