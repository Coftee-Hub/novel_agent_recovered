# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/cli.py
# 来源   : cli.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

__doc__ = '命令行入口。\n\n把散落的脚本收口成一套命令。所有命令共享同一份装配逻辑（`build()`），\n避免各脚本各自 new 一遍组件而配置漂移 —— 之前 write_chapter.py 里手写\n死的假卷大纲就是这么来的。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '命令行入口。\n\n把散落的脚本收口成一套命令。所有命令共享同一份装配逻辑（`build()`），\n避免各脚本各自 new 一遍组件而配置漂移 —— 之前 write_chapter.py 里手写\n死的假卷大纲就是这么来的。\n',
    16: '《落款》写作流水线',
    18: 'book',
    19: 'story_state.json',
    24: 'with_rag',
    49: '--force',
    50: '覆盖已有立项',
    54: 'corpus/core',
    55: '语料目录',
    59: '给 architect 的额外要求',
    62: '--volume',
    63: '-v',
    68: 'outline',
    69: 'drafts',
    70: 'checkpoint_db',
    75: '--chapters',
    76: '-n',
    77: '连续写几章',
    78: '从第几章开始，0 表示接着 state 的进度',
    79: '--rag',
    80: '启用语料检索（实测收益存疑）',
    81: '--reuse-outline',
    82: '复用 outline 命令存盘的细纲（人看过的那份），不再重出',
    83: '--resume-drafts',
    84: '复用 book/drafts/ 里已写好的场景，只补没写完的那几场',
    85: '--graph',
    86: '走 LangGraph + sqlite checkpoint：崩了能从崩的那个节点续跑',
    89: '已归档过也重跑',
    92: '要压缩的卷号',
    97: '期望的章号，0 表示不校验',
    100: '__main__',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'None',
    ('load_env', 0): '.env',
    ('load_env', 2): 'utf-8',
    ('load_env', 3): '#',
    ('load_env', 4): '=',
    ('load_env', 5): '"\'',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'dict',
    ('config', 0): 'config',
    ('config', 1): 'project.yaml',
    ('config', 2): 'utf-8',
    ('__annotate__', 1): 'with_rag',
    ('__annotate__', 2): 'bool',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'tuple[ChapterPipeline, LLMClient]',
    ('build', 0): '装配整条流水线。唯一的组件装配点。',
    ('build', 1): 'config',
    ('build', 2): 'models.yaml',
    ('build', 3): 'run_log.jsonl',
    ('build', 5): 'skills',
    ('build', 6): 'judge',
    ('build', 9): 'corpus',
    ('build', 10): 'index',
    ('build', 11): 'passages.json',
    ('build', 12): 'context',
    ('build', 13): 'rag_snippets',
    ('build', 15): '[yellow]未找到语料索引，RAG 跳过（先跑 index 命令）[/]',
    ('build', 16): 'max_chapter_summaries',
    ('build', 18): 'prev_scene_tail_chars',
    ('build', 20): 'project.yaml',
    ('build', 21): 'min_per_dimension',
    ('build', 22): 'min_total',
    ('build', 24): 'max_revisions',
    ('__annotate__', 1): 'client',
    ('__annotate__', 2): 'LLMClient',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'float',
    ('spent', 3): 'utf-8',
    ('<genexpr>', 0): 'cost_usd',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'Path | None',
    ('archive_previous', 0): '覆盖一份文件之前，先把旧版收进同级的 `_versions/`。\n\n大纲和成稿是这条流水线上最贵的东西：卷大纲是**唯一经过人确认**的产物，\n章细纲决定了一章能不能写好（第 3 章就是细纲把心理描写禁掉才反复打回），\n成稿更是几十分钟加真金白银换来的。这些文件都是"重跑一次就原地覆盖"，\n一旦新版更差，旧版没有任何地方找得回来。\n\n版本号顺序递增，`ch_003.v01.json` 存的是**被第一次覆盖掉的那一版**。\n内容一模一样时不留版本 —— 否则重跑几次就攒出一堆无差别副本。\n',
    ('archive_previous', 2): '_versions',
    ('archive_previous', 5): '.v*',
    ('archive_previous', 10): '.v',
    ('archive_previous', 11): '02d',
    ('<genexpr>', 2): '.',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'Path | None',
    ('retire_drafts', 0): '细纲改版后，把这一章的旧草稿整个目录挪开。',
    ('retire_drafts', 1): 'drafts',
    ('retire_drafts', 2): 'ch_',
    ('retire_drafts', 3): '03d',
    ('retire_drafts', 5): '.v',
    ('retire_drafts', 6): '02d',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'name',
    ('__annotate__', 4): 'str',
    ('__annotate__', 5): 'text',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'None',
    ('save_draft', 0): '把刚写好的一段存到 book/drafts/ch_XXX/。\n\n实测第 3 章：三场写完、修订一轮又重写三场，缝合时上游 403 抛出来，\n$0.13 的正文全丢了 —— 连"对话占比为什么是 0"都没法查。草稿是脏的、\n未缝合的，不进 chapters/，但它是花过钱的，不该被一个异常吃掉。\n',
    ('save_draft', 1): 'drafts',
    ('save_draft', 2): 'ch_',
    ('save_draft', 3): '03d',
    ('save_draft', 6): '.md',
    ('save_draft', 8): 'utf-8',
    ('__annotate__', 1): 'row',
    ('__annotate__', 2): 'dict',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('save_judgment', 0): '每次评审追加一行到 book/judgments.jsonl。',
    ('save_judgment', 1): 'judgments.jsonl',
    ('save_judgment', 2): 'a',
    ('save_judgment', 3): 'utf-8',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'outline',
    ('__annotate__', 4): 'ChapterOutline',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'list[str]',
    ('load_scene_drafts', 0): '读回上次崩之前写好的场景草稿，按细纲顺序，遇到第一个缺的就停。\n\n崩点几乎总在后面（实测两次都在缝合），草稿因此是场景列表的一个**前缀**，\n接着往下写就行。同一场有修订版时取版号最大的那份 —— 那才是它最新的样子。\n',
    ('load_scene_drafts', 1): 'drafts',
    ('load_scene_drafts', 2): 'ch_',
    ('load_scene_drafts', 3): '03d',
    ('load_scene_drafts', 4): '.r*.md',
    ('load_scene_drafts', 7): '.md',
    ('load_scene_drafts', 8): 'utf-8',
    ('<lambda>', 0): '.r',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'suffix',
    ('__annotate__', 4): 'str',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'Path',
    ('outline_path', 0): 'outlines',
    ('outline_path', 1): 'ch_',
    ('outline_path', 2): '03d',
    ('__annotate__', 1): 'outline',
    ('__annotate__', 2): 'ChapterOutline',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'Path',
    ('save_chapter_outline', 0): '细纲落盘。\n\n以前它只活在内存里，一章跑完就没了 —— 出了问题（比如第 2 章反复卡在\n对话占比）根本无从查证是 writer 没写出对话，还是细纲里压根没安排对手戏。\n',
    ('save_chapter_outline', 1): 'outlines',
    ('save_chapter_outline', 4): '.json',
    ('save_chapter_outline', 5): '.md',
    ('save_chapter_outline', 8): 'utf-8',
    ('save_chapter_outline', 10): '[yellow]细纲变了，旧草稿已挪到 ',
    ('save_chapter_outline', 11): '[/]',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'ChapterOutline | None',
    ('load_chapter_outline', 0): '.json',
    ('load_chapter_outline', 2): 'utf-8',
    ('__annotate__', 1): 'vol',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'VolumeOutline',
    ('load_volume', 0): 'outlines',
    ('load_volume', 1): 'vol_',
    ('load_volume', 2): '02d',
    ('load_volume', 3): '.json',
    ('load_volume', 4): '[red]找不到第 ',
    ('load_volume', 5): ' 卷大纲[/]  先跑：novel-agent plan ',
    ('load_volume', 6): ' ...',
    ('load_volume', 7): 'utf-8',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'None',
    ('status', 0): '看进度、成本、逾期的情感债。',
    ('status', 1): '[yellow]尚未立项[/]  先跑：novel-agent init',
    ('status', 2): '《',
    ('status', 3): '》',
    ('status', 6): '进度',
    ('status', 7): '第 ',
    ('status', 8): ' 章',
    ('status', 9): '人物',
    ('status', 10): ' 位',
    ('status', 11): '关系',
    ('status', 12): '、',
    ('status', 14): '—',
    ('status', 15): '已用桥段',
    ('status', 16): ' 个',
    ('status', 17): '成稿',
    ('status', 18): 'chapters',
    ('status', 19): '*.md',
    ('status', 20): '0 章',
    ('status', 21): '\n[red]逾期未回收的情感债[/]',
    ('status', 22): '  · ',
    ('status', 23): '（',
    ('status', 24): '）第 ',
    ('status', 25): ' 章埋下，应在第 ',
    ('status', 26): ' 章前回收',
    ('status', 27): 'run_log.jsonl',
    ('status', 28): 'utf-8',
    ('status', 31): '\n调用 ',
    ('status', 32): ' 次，累计 [bold]$',
    ('status', 33): '.4f',
    ('status', 34): '[/]',
    ('status', 35): '，其中 [yellow]',
    ('status', 36): ' 次降级[/]',
    ('<genexpr>', 0): '↔',
    ('<genexpr>', 1): '（',
    ('<genexpr>', 2): '）',
    ('<genexpr>', 0): 'cost_usd',
    ('<genexpr>', 0): 'degraded',
    ('__annotate__', 1): 'force',
    ('__annotate__', 2): 'bool',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('init', 0): '立项：写入初始人物与设定。',
    ('init', 2): 'scripts',
    ('init', 3): 'bootstrap_story.py',
    ('init', 4): '--force',
    ('__annotate__', 1): 'src',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('index', 0): '建语料检索索引（离线，不调模型）。',
    ('index', 2): 'corpus',
    ('index', 3): 'index',
    ('index', 4): 'passages.json',
    ('index', 5): '[green]✓[/] ',
    ('index', 6): ',',
    ('index', 7): ' 个片段 → ',
    ('index', 8): '（',
    ('index', 9): '.0f',
    ('index', 10): 's，',
    ('index', 12): '.1f',
    ('index', 13): 'MB）',
    ('__annotate__', 1): 'volume',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'ch_start',
    ('__annotate__', 4): 'ch_end',
    ('__annotate__', 5): 'stage',
    ('__annotate__', 6): 'str',
    ('__annotate__', 7): 'note',
    ('__annotate__', 8): 'return',
    ('__annotate__', 9): 'None',
    ('plan', 0): '出卷大纲 —— 唯一需要人工确认的环节。',
    ('plan', 1): 'config',
    ('plan', 2): 'models.yaml',
    ('plan', 3): 'run_log.jsonl',
    ('plan', 5): 'skills',
    ('plan', 6): '《',
    ('plan', 7): '》第 ',
    ('plan', 8): ' 卷（第 ',
    ('plan', 9): '-',
    ('plan', 10): ' 章 · ',
    ('plan', 11): '）…',
    ('plan', 13): 'outlines',
    ('plan', 16): 'vol_',
    ('plan', 17): '02d',
    ('plan', 18): '.json',
    ('plan', 19): '.md',
    ('plan', 21): 'utf-8',
    ('plan', 23): '[green]✓[/] ',
    ('plan', 24): '.0f',
    ('plan', 25): 's → vol_',
    ('plan', 26): '.json / .md\n',
    ('plan', 27): '\n[bold]读一遍再往下写。[/]不满意就改 note 重跑，改一句大纲比改三万字成稿便宜得多。',
    ('__annotate__', 1): 'chapter',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'note',
    ('__annotate__', 5): 'str',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'None',
    ('outline', 0): '先出一章细纲给人看，不写正文。\n\n卷大纲有确认断点，章细纲没有 —— 但真正决定一章能不能写好的是细纲：\n三个场景全排成独处，再怎么要求 writer 也变不出对话（第 2 章就这么\n连卡了三次）。看完满意再跑 `write --reuse-outline`，那一步会直接复用\n这份，不会重出。\n',
    ('outline', 2): '[green]✓[/] ',
    ('outline', 3): '.0f',
    ('outline', 4): 's，$',
    ('outline', 5): '.4f',
    ('outline', 6): ' → ',
    ('outline', 7): ' / .md\n',
    ('outline', 8): '\n[yellow]',
    ('outline', 9): '/',
    ('outline', 10): ' 场是独处[/]（',
    ('outline', 11): '、',
    ('outline', 12): '）—— 对话占比下限 15%，独处场太多时 writer 无论如何都够不到。',
    ('outline', 13): '\n改一句细纲比改三千字成稿便宜。满意就跑：[bold]novel-agent write --reuse-outline --start ',
    ('outline', 14): '[/]',
    ('__annotate__', 1): 'payload',
    ('__annotate__', 2): 'dict',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('_fingerprint', 0): '细纲的短指纹，用来给 checkpoint 线程分版本。',
    ('_fingerprint', 5): 'utf-8',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'note',
    ('__annotate__', 4): 'str',
    ('run_via_graph', 0): '走 LangGraph 跑一章，节点级 checkpoint 存在 book/checkpoints.sqlite。\n\n与 `pipeline.run` 的差别只有一个：崩在哪个节点，重跑时就从哪个节点接着来\n（细纲不重出、写好的场景不重写）。业务逻辑全在 pipeline 里，两条路径共用。\n\nthread_id 用「卷-章」标定：同一章重跑会认出上次的 checkpoint，\n换一章则是另一条线程，互不干扰。\n',
    ('run_via_graph', 2): 'ch',
    ('run_via_graph', 3): 'note',
    ('run_via_graph', 4): 'story',
    ('run_via_graph', 5): 'volume',
    ('run_via_graph', 7): 'outline',
    ('run_via_graph', 8): 'scenes',
    ('run_via_graph', 9): 'checkpoints.sqlite',
    ('run_via_graph', 10): 'configurable',
    ('run_via_graph', 11): 'thread_id',
    ('run_via_graph', 12): '  从上次中断处续跑（',
    ('run_via_graph', 13): '，下一个节点：',
    ('run_via_graph', 14): '）',
    ('__annotate__', 1): 'ch',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'seed',
    ('__annotate__', 4): 'dict',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'tuple[str, bool]',
    ('_pick_thread', 0): '挑一条 checkpoint 线程，返回 (线程 id, 是不是续跑)。\n\n规则只有一条：**只续没跑完的那条，其余一律新开。**\n\n踩过的坑：LangGraph 的线程状态是累积的。往一条**已经跑完**的线程再 invoke\n一次，传进去的 seed 只是**合并**进旧状态 —— `revisions` 还停在上次的 2，\n于是新的一轮缝合完、gate 一失败就直接判"修订 2 轮后仍未通过"，一轮修订\n都不做。实测连着两次跑各花 $0.05，只做了一次缝合，白跑。\n\n线程 id 里带细纲指纹：细纲改过之后旧存档里的场景是照旧要求写的，\n不能续。同一份细纲的多次尝试用序号区分，旧的留在库里不动。\n',
    ('_pick_thread', 1): 'vol',
    ('_pick_thread', 2): '02d',
    ('_pick_thread', 3): '-ch',
    ('_pick_thread', 4): '03d',
    ('_pick_thread', 5): 'outline',
    ('_pick_thread', 6): 'auto',
    ('_pick_thread', 7): 'configurable',
    ('_pick_thread', 8): 'thread_id',
    ('_pick_thread', 10): '-',
    ('_pick_thread', 12): '第 ',
    ('_pick_thread', 13): ' 章已经攒了 99 条 checkpoint 线程，先清理再跑',
    ('__annotate__', 1): 'chapters',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'start',
    ('__annotate__', 5): 'rag',
    ('__annotate__', 6): 'bool',
    ('__annotate__', 7): 'note',
    ('__annotate__', 8): 'str',
    ('__annotate__', 9): 'reuse_outline',
    ('__annotate__', 10): 'resume_drafts',
    ('__annotate__', 11): 'graph',
    ('__annotate__', 12): 'return',
    ('__annotate__', 13): 'None',
    ('write', 0): '写作：出细纲 → 逐场景写 → 缝合 → 检查 → 修订 → 归档。\n\n每章写完立刻落盘 state —— 中断后重跑会从下一章接着来，不用从头。\n',
    ('write', 2): '[yellow]第 ',
    ('write', 3): ' 章超出第 ',
    ('write', 4): ' 卷范围，停止[/]',
    ('write', 5): '第 ',
    ('write', 6): ' 章',
    ('write', 8): '  复用 ',
    ('write', 9): '.json',
    ('write', 10): '  [yellow]没有存盘的第 ',
    ('write', 11): ' 章细纲，现出一份[/]',
    ('write', 12): '[red]--resume-drafts 必须配 --reuse-outline[/]：草稿按细纲的场景 id 存盘，细纲重出就对不上了',
    ('write', 13): '  草稿命中 ',
    ('write', 14): '/',
    ('write', 15): ' 场',
    ('write', 16): '，其余现写',
    ('write', 19): '[red]✗ 第 ',
    ('write', 20): ' 章异常：',
    ('write', 21): ': ',
    ('write', 22): '[/]',
    ('write', 23): 'drafts',
    ('write', 24): 'ch_',
    ('write', 25): '03d',
    ('write', 26): '*.md',
    ('write', 27): '  已写好的 ',
    ('write', 28): ' 段草稿留在 book/drafts/ch_',
    ('write', 29): '/，不用重写',
    ('write', 30): 'needs_human',
    ('write', 31): '_',
    ('write', 32): '.md',
    ('write', 36): 'utf-8',
    ('write', 37): '[red]✗ 未通过[/]（',
    ('write', 38): '；',
    ('write', 39): '）→ ',
    ('write', 40): 'chapters',
    ('write', 41): '  旧稿已存 ',
    ('write', 42): '  [yellow]归档失败（',
    ('write', 43): '）[/]',
    ('write', 44): '  成稿已保留：',
    ('write', 45): '  [bold]补录：novel-agent archive ',
    ('write', 46): '[/]，补完再继续往下写',
    ('write', 47): 'story_bible.md',
    ('write', 48): '[green]✓[/] ',
    ('write', 49): ',',
    ('write', 50): ' 字，修订 ',
    ('write', 51): ' 轮，',
    ('write', 52): '.0f',
    ('write', 53): 's',
    ('write', 54): 'volume_summary',
    ('write', 55): '  [cyan]第 ',
    ('write', 56): ' 卷已压成一段梗概[/]（第 ',
    ('write', 57): '-',
    ('write', 58): ' 章 → ',
    ('write', 59): ' 字）',
    ('write', 60): '  [yellow]',
    ('write', 61): '\n完成 ',
    ('write', 62): '，失败于第 ',
    ('write', 63): '，本次花费 $',
    ('write', 64): '.4f',
    ('__annotate__', 1): 'chapter',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'volume',
    ('__annotate__', 4): 'force',
    ('__annotate__', 5): 'bool',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'None',
    ('archive', 0): '把已有章节补录进 state（流水线外写的章节用这个）。\n\n需要重出一次章细纲 —— archivist 要对照场景规格才知道哪些是"该记的"，\n否则它只能凭正文猜，摘要会写成读后感。\n',
    ('archive', 4): '[yellow]第 ',
    ('archive', 5): ' 章已归档过[/]（加 --force 重跑）',
    ('archive', 6): 'chapters',
    ('archive', 7): 'ch_',
    ('archive', 8): '03d',
    ('archive', 9): '.md',
    ('archive', 10): '[red]找不到 ',
    ('archive', 11): '[/]',
    ('archive', 12): '重出第 ',
    ('archive', 13): ' 章细纲…',
    ('archive', 15): '提炼状态增量…',
    ('archive', 16): 'utf-8',
    ('archive', 18): 'story_bible.md',
    ('archive', 19): '[green]✓[/] 第 ',
    ('archive', 20): ' 章已归档，$',
    ('archive', 21): '.4f',
    ('archive', 22): '  摘要：',
    ('archive', 23): '  埋下 ',
    ('archive', 24): ' 条情感债：',
    ('archive', 25): '    · [',
    ('archive', 26): '] ',
    ('archive', 27): '：',
    ('archive', 28): '（第 ',
    ('archive', 29): ' 章前回收）',
    ('archive', 30): '  回收：',
    ('archive', 31): '、',
    ('archive', 32): '  桥段：',
    ('archive', 34): '  关系：',
    ('archive', 35): '↔',
    ('archive', 36): ' → ',
    ('archive', 37): '（',
    ('archive', 38): '）',
    ('__annotate__', 1): 'volume',
    ('__annotate__', 2): 'int',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('compress', 0): '把一卷压成一段卷梗概（卷末自动做，这里是补做用的）。\n\n正常路径是 `write` 写完卷末那一章时自动触发。会用到这个命令的情况：\n压缩当时失败了（渠道挂了）、或者事后重写过某几章想让梗概跟着更新。\n',
    ('compress', 1): '第 ',
    ('compress', 2): ' 卷（第 ',
    ('compress', 3): '-',
    ('compress', 4): ' 章）已归档 ',
    ('compress', 5): ' 章，压缩中…',
    ('compress', 6): '  [yellow]这一卷还没写完，压出来的梗概只覆盖已写的部分[/]',
    ('compress', 7): 'story_bible.md',
    ('compress', 8): 'utf-8',
    ('compress', 9): '[green]✓[/] 第 ',
    ('compress', 10): ' 章 → ',
    ('compress', 11): ' 字，$',
    ('compress', 12): '.4f',
    ('compress', 14): '\n往后这一卷在上下文里就只剩这一段了。不满意就改 `book/story_state.json` 里的 volume_summaries，或者重跑这条命令。',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'None',
    ('judgments', 0): '看 judge 七个维度的实际分布 —— 调阈值的依据。\n\n方案里写着"judge 阈值 24/35 是拍脑袋的起始值，跑 10 章后按实际分布调"。\n要调就得先有分布：分数此前跑完就丢，从 2026-08-22 起才开始记。\n\n看三件事：\n  · 哪一维永远高分 —— 那道线是摆设，没有区分度\n  · 哪一维反复低分 —— 那是系统性弱项，该改 skills 或细纲，**不是调低阈值**\n  · 总分线落在分布的什么位置 —— 决定打回率，卡在中位数上就会一直烧修订\n',
    ('judgments', 3): 'judgments.jsonl',
    ('judgments', 4): '[yellow]还没有评审记录[/]  跑过 write 之后才会有',
    ('judgments', 5): 'utf-8',
    ('judgments', 6): 'judge 评分分布（',
    ('judgments', 7): ' 次评审）',
    ('judgments', 9): '维度',
    ('judgments', 10): 'left',
    ('judgments', 11): 'right',
    ('judgments', 13): 'thresholds',
    ('judgments', 14): 'per_dimension',
    ('judgments', 15): 'scores',
    ('judgments', 17): 'g',
    ('judgments', 18): ' 次',
    ('judgments', 19): '—',
    ('judgments', 20): 'total',
    ('judgments', 21): '总分：最低 ',
    ('judgments', 22): '／中位 ',
    ('judgments', 23): '／最高 ',
    ('judgments', 24): '（当前线 ',
    ('judgments', 25): '/35）',
    ('judgments', 26): '通过 ',
    ('judgments', 28): '/',
    ('judgments', 29): 'ch',
    ('judgments', 30): '修订前后总分变化：',
    ('judgments', 31): '、',
    ('judgments', 33): '（',
    ('judgments', 34): ' 章有过修订）',
    ('judgments', 35): '[dim]还没有哪一章修订后被重新评审过 —— 修订有没有用还看不出来[/]',
    ('<genexpr>', 0): 'passed',
    ('<genexpr>', 0): '+d',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'chapter',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('check', 0): '对已有稿件跑一遍 gate（不调模型）。',
    ('check', 2): 'config',
    ('check', 3): 'project.yaml',
    ('check', 4): 'utf-8',
}

# ───────────── 代码骨架（签名/docstring 原样）─────────────

# ───────────── 模块级 import（重建）─────────────
import os
import json
import time

from pathlib import Path

import yaml
import typer
from rich.console import Console
from rich.table import Table

from .llm import LLMClient, Router
from .agents.pipeline import ChapterPipeline
from .agents.architect import Architect
from .agents.writer import Writer, Stitcher
from .agents.gate import Gate
from .agents.judge import Judge
from .agents.archivist import Archivist
from .agents.schemas import ChapterOutline, VolumeOutline
from .state.store import StateStore, apply_volume_summary
from .state.bible import render

# TODO(重建): 需确认 ROOT 的实际计算方式（原代码未知，这里按 src/novel_agent/cli.py 上溯 3 级取项目根）
ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / 'book'
STATE_PATH = BOOK / 'story_state.json'
console = Console()


def load_env():
    '.env'
    env = ROOT / '.env'
    if not env.exists():
        return None
    for raw in env.read_text('utf-8').splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith('#'):
            continue
        if '=' not in line:
            continue
        key, _, value = line.partition('=')
        os.environ.setdefault(key.strip(), value.strip().strip('"\''))
    return None


def config():
    'config'
    return yaml.safe_load((ROOT / 'config' / 'project.yaml').read_text('utf-8'))


def build(*, with_rag):
    '装配整条流水线。唯一的组件装配点。'
    load_env()
    cfg = config()
    client = LLMClient(Router(ROOT / 'config' / 'models.yaml'), log_path=BOOK / 'run_log.jsonl')
    skills = ROOT / 'skills'
    jc = cfg['judge']
    retriever = None
    if with_rag:
        from .corpus.index import PassageIndex, SceneRetriever
        idx_file = ROOT / 'corpus' / 'index' / 'passages.json'
        if idx_file.exists():
            retriever = SceneRetriever(PassageIndex.load(idx_file), limit=cfg['context']['rag_snippets'])
        else:
            console.print('[yellow]未找到语料索引，RAG 跳过（先跑 index 命令）[/]')
    pipeline = ChapterPipeline(
        architect=Architect(client, skills, summary_cap=cfg['context']['max_chapter_summaries']),
        writer=Writer(client, skills, prev_tail_chars=cfg['context']['prev_scene_tail_chars'], summary_cap=cfg['context']['max_chapter_summaries']),
        stitcher=Stitcher(client, skills),
        gate=Gate.from_config(ROOT / 'config' / 'project.yaml'),
        judge=Judge(client, skills, jc['min_per_dimension'], min_total=jc['min_total']),
        archivist=Archivist(client),
        max_revisions=jc['max_revisions'],
        retriever=retriever,
        outline_sink=save_chapter_outline,
        judgment_sink=save_judgment,
        draft_sink=save_draft,
        log=lambda m: console.print(f'  {m}'),
    )
    return pipeline, client


def spent(client):
    'utf-8'
    log = client.log_path
    if log is None or not log.exists():
        return 0.0
    return sum(json.loads(l)['cost_usd'] for l in log.read_text('utf-8').splitlines() if l.strip())


def archive_previous(path):
    '覆盖一份文件之前，先把旧版收进同级的 `_versions/`。\n\n大纲和成稿是这条流水线上最贵的东西：卷大纲是**唯一经过人确认**的产物，\n章细纲决定了一章能不能写好（第 3 章就是细纲把心理描写禁掉才反复打回），\n成稿更是几十分钟加真金白银换来的。这些文件都是"重跑一次就原地覆盖"，\n一旦新版更差，旧版没有任何地方找得回来。\n\n版本号顺序递增，`ch_003.v01.json` 存的是**被第一次覆盖掉的那一版**。\n内容一模一样时不留版本 —— 否则重跑几次就攒出一堆无差别副本。\n'
    if not path.exists():
        return None
    old = path.read_bytes()
    vdir = path.parent / '_versions'
    vdir.mkdir(parents=True, exist_ok=True)
    existing = sorted(vdir.glob(f'{path.stem}.v*{path.suffix}'))
    if any(f.read_bytes() == old for f in existing):
        return None
    n = max((int(f.name[len(path.stem) + 2:].split('.')[0]) for f in existing), default=0) + 1
    dest = vdir / f'{path.stem}.v{n:02d}{path.suffix}'
    dest.write_bytes(old)
    return dest


def retire_drafts(ch):
    '细纲改版后，把这一章的旧草稿整个目录挪开。'
    d = BOOK / 'drafts' / f'ch_{ch:03d}'
    if not d.exists() or not any(d.iterdir()):
        return None
    n = 1
    while True:
        dest = d.with_name(f'{d.name}.v{n:02d}')
        if not dest.exists():
            break
        n += 1
    d.rename(dest)
    return dest


def save_draft(ch, name, text):
    '把刚写好的一段存到 book/drafts/ch_XXX/。\n\n实测第 3 章：三场写完、修订一轮又重写三场，缝合时上游 403 抛出来，\n$0.13 的正文全丢了 —— 连"对话占比为什么是 0"都没法查。草稿是脏的、\n未缝合的，不进 chapters/，但它是花过钱的，不该被一个异常吃掉。\n'
    d = BOOK / 'drafts' / f'ch_{ch:03d}'
    d.mkdir(parents=True, exist_ok=True)
    (d / f'{name}.md').write_text(text + '\n', 'utf-8')
    return None


def save_judgment(row):
    '每次评审追加一行到 book/judgments.jsonl。'
    with (BOOK / 'judgments.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')
    return None


def load_scene_drafts(ch, outline):
    '读回上次崩之前写好的场景草稿，按细纲顺序，遇到第一个缺的就停。\n\n崩点几乎总在后面（实测两次都在缝合），草稿因此是场景列表的一个**前缀**，\n接着往下写就行。同一场有修订版时取版号最大的那份 —— 那才是它最新的样子。\n'
    d = BOOK / 'drafts' / f'ch_{ch:03d}'
    if not d.exists():
        return []
    found = []
    for spec in outline.scenes:
        revs = sorted(d.glob(f'{spec.id}.r*.md'), key=lambda f: int(f.name.rsplit('.r', 1)[-1][:-3]))
        f = revs[-1] if revs else d / f'{spec.id}.md'
        if not f.exists():
            return found
        found.append(f.read_text('utf-8').strip())
    return found


def outline_path(ch, suffix):
    'outlines'
    return BOOK / 'outlines' / f'ch_{ch:03d}{suffix}'


def save_chapter_outline(outline):
    '细纲落盘。\n\n以前它只活在内存里，一章跑完就没了 —— 出了问题（比如第 2 章反复卡在\n对话占比）根本无从查证是 writer 没写出对话，还是细纲里压根没安排对手戏。\n'
    d = BOOK / 'outlines'
    d.mkdir(parents=True, exist_ok=True)
    f = outline_path(outline.ch, '.json')
    md = outline_path(outline.ch, '.md')
    changed = archive_previous(f) is not None
    archive_previous(md)
    f.write_text(outline.model_dump_json(indent=2), 'utf-8')
    md.write_text(outline.to_markdown() + '\n', 'utf-8')
    if changed:
        retired = retire_drafts(outline.ch)
        if retired:
            console.print(f'[yellow]细纲变了，旧草稿已挪到 {retired.relative_to(ROOT)}[/]')
    return f


def load_chapter_outline(ch):
    '.json'
    f = outline_path(ch, '.json')
    if not f.exists():
        return None
    return ChapterOutline.model_validate_json(f.read_text('utf-8'))


def load_volume(vol):
    'outlines'
    f = BOOK / 'outlines' / f'vol_{vol:02d}.json'
    if not f.exists():
        console.print(f'[red]找不到第 {vol} 卷大纲[/]  先跑：novel-agent plan {vol} ...')
        raise typer.Exit(2)
    return VolumeOutline.model_validate_json(f.read_text('utf-8'))


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def status():
    '看进度、成本、逾期的情感债。'
    if not STATE_PATH.exists():
        console.print('[yellow]尚未立项[/]  先跑：novel-agent init')
        raise typer.Exit(1)
    state = StateStore(STATE_PATH).load()
    t = Table(title=f'《{state.title}》', show_header=False)
    t.add_row('进度', f'第 {state.current_chapter} 章')
    t.add_row('人物', f'{len(state.characters)} 位')
    rels = '、'.join(
        f"{state.character(r.a_id).name if state.character(r.a_id) else r.a_id}"
        f"↔{state.character(r.b_id).name if state.character(r.b_id) else r.b_id}"
        f"（{r.stage}）"
        for r in state.relationships
    )
    t.add_row('关系', rels or '—')
    t.add_row('已用桥段', f'{len(state.used_beats)} 个')
    t.add_row('成稿', f'{len(list((BOOK / "chapters").glob("*.md")))} 章' if (BOOK / 'chapters').exists() else '0 章')
    console.print(t)
    overdue = state.overdue_debts()
    if overdue:
        console.print('\n[red]逾期未回收的情感债[/]')
        for d in overdue:
            console.print(f'  · {d.desc}（{d.kind}）第 {d.planted_ch} 章埋下，应在第 {d.due_by_ch} 章前回收')
    log = BOOK / 'run_log.jsonl'
    if log.exists():
        rows = [json.loads(l) for l in log.read_text('utf-8').splitlines() if l.strip()]
        cost = sum(r['cost_usd'] for r in rows)
        degraded = sum(1 for r in rows if r.get('degraded'))
        console.print(
            f'\n调用 {len(rows)} 次，累计 [bold]${cost:.4f}[/]'
            + (f'，其中 [yellow]{degraded} 次降级[/]' if degraded else '')
        )
    return None


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def init(force):
    '立项：写入初始人物与设定。'
    import subprocess
    import sys
    cmd = [sys.executable, str(ROOT / 'scripts' / 'bootstrap_story.py')]
    if force:
        cmd.append('--force')
    raise typer.Exit(subprocess.call(cmd))


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def index(src):
    '建语料检索索引（离线，不调模型）。'
    from .corpus.index import PassageIndex
    started = time.time()
    idx = PassageIndex()
    n = idx.add_dir(ROOT / src)
    out = ROOT / 'corpus' / 'index' / 'passages.json'
    idx.save(out)
    console.print(
        f'[green]✓[/] {n:,} 个片段 → {out.relative_to(ROOT)}'
        f'（{time.time() - started:.0f}s，{out.stat().st_size / 1000000.0:.1f}MB）'
    )
    return None


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def plan(volume, ch_start, ch_end, stage, note):
    '出卷大纲 —— 唯一需要人工确认的环节。'
    load_env()
    client = LLMClient(Router(ROOT / 'config' / 'models.yaml'), log_path=BOOK / 'run_log.jsonl')
    state = StateStore(STATE_PATH).load()
    architect = Architect(client, ROOT / 'skills')
    console.print(f'《{state.title}》第 {volume} 卷（第 {ch_start}-{ch_end} 章 · {stage}）…')
    started = time.time()
    outline = architect.plan_volume(state, volume=volume, ch_start=ch_start, ch_end=ch_end, stage=stage, note=note)
    d = BOOK / 'outlines'
    d.mkdir(parents=True, exist_ok=True)
    vj = d / f'vol_{volume:02d}.json'
    vm = d / f'vol_{volume:02d}.md'
    for stale in (vj, vm):
        archive_previous(stale)
    vj.write_text(outline.model_dump_json(indent=2), 'utf-8')
    vm.write_text(outline.to_markdown() + '\n', 'utf-8')
    console.print(f'[green]✓[/] {time.time() - started:.0f}s → vol_{volume:02d}.json / .md\n')
    console.print(outline.to_markdown())
    console.print('\n[bold]读一遍再往下写。[/]不满意就改 note 重跑，改一句大纲比改三万字成稿便宜得多。')
    return None


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def outline(chapter, volume, note):
    '先出一章细纲给人看，不写正文。\n\n卷大纲有确认断点，章细纲没有 —— 但真正决定一章能不能写好的是细纲：\n三个场景全排成独处，再怎么要求 writer 也变不出对话（第 2 章就这么\n连卡了三次）。看完满意再跑 `write --reuse-outline`，那一步会直接复用\n这份，不会重出。\n'
    pipeline, client = build()
    state = StateStore(STATE_PATH).load()
    vol = load_volume(volume)
    base = spent(client)
    started = time.time()
    plan = pipeline.architect.plan_chapter(state, vol, ch=chapter, note=note)
    f = save_chapter_outline(plan)
    console.print(f'[green]✓[/] {time.time() - started:.0f}s，${spent(client) - base:.4f} → {f.relative_to(ROOT)} / .md\n')
    console.print(plan.to_markdown())
    solo = [s.id for s in plan.scenes if len(s.present) == 1]
    if solo:
        console.print(f'\n[yellow]{len(solo)}/{len(plan.scenes)} 场是独处[/]（{"、".join(solo)}）—— 对话占比下限 15%，独处场太多时 writer 无论如何都够不到。')
    console.print(f'\n改一句细纲比改三千字成稿便宜。满意就跑：[bold]novel-agent write --reuse-outline --start {chapter}[/]')
    return None


def _fingerprint(payload):
    '细纲的短指纹，用来给 checkpoint 线程分版本。'
    import hashlib
    import json as _json
    raw = _json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()[:8]


def run_via_graph(pipeline, state, vol, ch, *, note, outline, drafts, checkpoint_db):
    '走 LangGraph 跑一章，节点级 checkpoint 存在 book/checkpoints.sqlite。\n\n与 `pipeline.run` 的差别只有一个：崩在哪个节点，重跑时就从哪个节点接着来\n（细纲不重出、写好的场景不重写）。业务逻辑全在 pipeline 里，两条路径共用。\n\nthread_id 用「卷-章」标定：同一章重跑会认出上次的 checkpoint，\n换一章则是另一条线程，互不干扰。\n'
    from .graph.build import ChapterResultView, checkpointed_graph
    seed = {'ch': ch, 'note': note, 'story': state.model_dump(), 'volume': vol.model_dump()}
    if outline is not None:
        seed['outline'] = outline.model_dump()
    if drafts:
        seed['scenes'] = list(drafts)
    db = checkpoint_db or BOOK / 'checkpoints.sqlite'
    with checkpointed_graph(pipeline, db) as app_graph:
        thread, resuming = _pick_thread(app_graph, vol, ch, seed, outline)
        cfg = {'configurable': {'thread_id': thread}}
        if resuming:
            console.print(f'  从上次中断处续跑（{thread}，下一个节点：{app_graph.get_state(cfg).next[0]}）')
        out = app_graph.invoke(None if resuming else seed, cfg)
    return ChapterResultView(out, pipeline)


def _pick_thread(app_graph, vol, ch, seed, outline):
    '挑一条 checkpoint 线程，返回 (线程 id, 是不是续跑)。\n\n规则只有一条：**只续没跑完的那条，其余一律新开。**\n\n踩过的坑：LangGraph 的线程状态是累积的。往一条**已经跑完**的线程再 invoke\n一次，传进去的 seed 只是**合并**进旧状态 —— `revisions` 还停在上次的 2，\n于是新的一轮缝合完、gate 一失败就直接判"修订 2 轮后仍未通过"，一轮修订\n都不做。实测连着两次跑各花 $0.05，只做了一次缝合，白跑。\n\n线程 id 里带细纲指纹：细纲改过之后旧存档里的场景是照旧要求写的，\n不能续。同一份细纲的多次尝试用序号区分，旧的留在库里不动。\n'
    base = f'vol{vol.volume:02d}-ch{ch:03d}'
    fp = _fingerprint(seed['outline']) if outline is not None else 'auto'
    legacy = app_graph.get_state({'configurable': {'thread_id': base}})
    if legacy.next and (legacy.values or {}).get('outline') == seed.get('outline'):
        return base, True
    for n in range(1, 100):
        tid = f'{base}-{fp}-{n:02d}'
        state = app_graph.get_state({'configurable': {'thread_id': tid}})
        if not state.values:
            return tid, False
        if not state.next:
            continue
        return tid, True
    raise RuntimeError(f'第 {ch} 章已经攒了 99 条 checkpoint 线程，先清理再跑')


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def write(chapters, volume, start, rag, note, reuse_outline, resume_drafts, graph):
    '写作：出细纲 → 逐场景写 → 缝合 → 检查 → 修订 → 归档。\n\n每章写完立刻落盘 state —— 中断后重跑会从下一章接着来，不用从头。\n'
    pipeline, client = build(with_rag=rag)
    store = StateStore(STATE_PATH)
    state = store.load()
    vol = load_volume(volume)
    first = start if start else max(state.current_chapter + 1, vol.ch_start)
    base_cost = spent(client)
    done = 0
    failed = []
    for ch in range(first, first + chapters):
        if ch > vol.ch_end:
            console.print(f'[yellow]第 {ch} 章超出第 {volume} 卷范围，停止[/]')
            break
        console.rule(f'第 {ch} 章')
        started = time.time()
        saved = load_chapter_outline(ch) if reuse_outline else None
        if reuse_outline:
            if saved:
                console.print(f'  复用 {outline_path(ch, ".json").name}')
            else:
                console.print(f'  [yellow]没有存盘的第 {ch} 章细纲，现出一份[/]')
        drafts = []
        if resume_drafts:
            if saved is not None:
                drafts = load_scene_drafts(ch, saved)
                console.print(f'  草稿命中 {len(drafts)}/{len(saved.scenes)} 场' + ('，其余现写' if len(drafts) < len(saved.scenes) else ''))
            else:
                console.print('[red]--resume-drafts 必须配 --reuse-outline[/]：草稿按细纲的场景 id 存盘，细纲重出就对不上了')
                raise typer.Exit(2)
        try:
            if graph:
                result = run_via_graph(pipeline, state, vol, ch, note=note, outline=saved, drafts=drafts)
            else:
                result = pipeline.run(state, vol, ch, note=note, outline=saved, drafts=drafts)
        except Exception as exc:
            console.print(f'[red]✗ 第 {ch} 章异常：{type(exc).__name__}: {exc}[/]')
            drafts = sorted((BOOK / 'drafts' / f'ch_{ch:03d}').glob('*.md'))
            if drafts:
                console.print(f'  已写好的 {len(drafts)} 段草稿留在 book/drafts/ch_{ch:03d}/，不用重写')
            failed.append(ch)
            break
        if not result.passed:
            out = BOOK / 'needs_human' / f'ch_{ch:03d}_{int(time.time())}.md'
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(result.text + '\n', 'utf-8')
            console.print(f'[red]✗ 未通过[/]（{"；".join(result.notes)}）→ {out.relative_to(ROOT)}')
            console.print(result.gate.render())
            if result.verdict:
                console.print(result.verdict.render())
            failed.append(ch)
            break
        (BOOK / 'chapters').mkdir(parents=True, exist_ok=True)
        final = BOOK / 'chapters' / f'ch_{ch:03d}.md'
        kept = archive_previous(final)
        if kept:
            console.print(f'  旧稿已存 {kept.relative_to(ROOT)}')
        final.write_text(result.text + '\n', 'utf-8')
        if result.archive_error:
            console.print(f'  [yellow]归档失败（{result.archive_error}）[/]')
            console.print(f'  成稿已保留：{final.relative_to(ROOT)}')
            console.print(f'  [bold]补录：novel-agent archive {ch}[/]，补完再继续往下写')
            failed.append(ch)
            break
        state = result.state
        store.save(state)
        (BOOK / 'story_bible.md').write_text(render(state), 'utf-8')
        done += 1
        console.print(f'[green]✓[/] {len(result.text):,} 字，修订 {result.revisions} 轮，{time.time() - started:.0f}s')
        vs = getattr(result, 'volume_summary', None)
        if vs:
            console.print(f'  [cyan]第 {vs.volume} 卷已压成一段梗概[/]（第 {vs.ch_start}-{vs.ch_end} 章 → {len(vs.summary)} 字）')
        for note in result.notes:
            console.print(f'  [yellow]{note}[/]')
    console.print(
        f'\n完成 {done} 章'
        + (f'，失败于第 {failed[0]} 章' if failed else '')
        + f'，本次花费 ${spent(client) - base_cost:.4f}'
    )
    if failed:
        raise typer.Exit(1)
    return None


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def archive(chapter, volume, force):
    '把已有章节补录进 state（流水线外写的章节用这个）。\n\n需要重出一次章细纲 —— archivist 要对照场景规格才知道哪些是"该记的"，\n否则它只能凭正文猜，摘要会写成读后感。\n'
    load_env()
    store = StateStore(STATE_PATH)
    state = store.load()
    if any(s.ch == chapter for s in state.chapter_summaries) and not force:
        console.print(f'[yellow]第 {chapter} 章已归档过[/]（加 --force 重跑）')
        raise typer.Exit(1)
    f = BOOK / 'chapters' / f'ch_{chapter:03d}.md'
    if not f.exists():
        console.print(f'[red]找不到 {f.relative_to(ROOT)}[/]')
        raise typer.Exit(2)
    pipeline, client = build()
    vol = load_volume(volume)
    base = spent(client)
    console.print(f'重出第 {chapter} 章细纲…')
    outline = pipeline.architect.plan_chapter(state, vol, ch=chapter)
    console.print('提炼状态增量…')
    patch = pipeline.archivist.archive(state, outline, f.read_text('utf-8'))
    from .state import apply_patch
    state = apply_patch(state, patch)
    store.save(state)
    (BOOK / 'story_bible.md').write_text(render(state), 'utf-8')
    console.print(f'[green]✓[/] 第 {chapter} 章已归档，${spent(client) - base:.4f}')
    console.print(f'  摘要：{patch.chapter_summary.summary}')
    if patch.new_debts:
        console.print(f'  埋下 {len(patch.new_debts)} 条情感债：')
        for d in patch.new_debts:
            console.print(f'    · [{d.id}] {d.kind}：{d.desc}（第 {d.due_by_ch} 章前回收）')
    if patch.resolved_debt_ids:
        console.print(f'  回收：{"、".join(patch.resolved_debt_ids)}')
    if patch.used_beats:
        console.print(f'  桥段：{"、".join(b.beat_type for b in patch.used_beats)}')
    if patch.relationship_updates:
        for r in patch.relationship_updates:
            console.print(f'  关系：{r.a_id}↔{r.b_id} → {r.stage}（{r.tension_source}）')
    return None


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def compress(volume):
    '把一卷压成一段卷梗概（卷末自动做，这里是补做用的）。\n\n正常路径是 `write` 写完卷末那一章时自动触发。会用到这个命令的情况：\n压缩当时失败了（渠道挂了）、或者事后重写过某几章想让梗概跟着更新。\n'
    load_env()
    store = StateStore(STATE_PATH)
    state = store.load()
    vol = load_volume(volume)
    pipeline, client = build()
    base = spent(client)
    written = [s for s in state.chapter_summaries if vol.ch_start <= s.ch <= vol.ch_end]
    console.print(f'第 {volume} 卷（第 {vol.ch_start}-{vol.ch_end} 章）已归档 {len(written)} 章，压缩中…')
    if len(written) < vol.ch_end - vol.ch_start + 1:
        console.print('  [yellow]这一卷还没写完，压出来的梗概只覆盖已写的部分[/]')
    summary = pipeline.archivist.compress_volume(state, vol)
    state = apply_volume_summary(state, summary)
    store.save(state)
    (BOOK / 'story_bible.md').write_text(render(state), 'utf-8')
    console.print(f'[green]✓[/] 第 {summary.ch_start}-{summary.ch_end} 章 → {len(summary.summary)} 字，${spent(client) - base:.4f}\n')
    console.print(summary.summary)
    console.print('\n往后这一卷在上下文里就只剩这一段了。不满意就改 `book/story_state.json` 里的 volume_summaries，或者重跑这条命令。')
    return None


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def judgments():
    '看 judge 七个维度的实际分布 —— 调阈值的依据。\n\n方案里写着"judge 阈值 24/35 是拍脑袋的起始值，跑 10 章后按实际分布调"。\n要调就得先有分布：分数此前跑完就丢，从 2026-08-22 起才开始记。\n\n看三件事：\n  · 哪一维永远高分 —— 那道线是摆设，没有区分度\n  · 哪一维反复低分 —— 那是系统性弱项，该改 skills 或细纲，**不是调低阈值**\n  · 总分线落在分布的什么位置 —— 决定打回率，卡在中位数上就会一直烧修订\n'
    from statistics import median
    from .agents.judge import LABELS
    f = BOOK / 'judgments.jsonl'
    if not f.exists():
        console.print('[yellow]还没有评审记录[/]  跑过 write 之后才会有')
        raise typer.Exit(1)
    rows = [json.loads(l) for l in f.read_text('utf-8').splitlines() if l.strip()]
    t = Table(title=f'judge 评分分布（{len(rows)} 次评审）')
    for col in ('维度', '最低', '中位', '最高', '低于线'):
        t.add_column(col, justify='left' if col == '维度' else 'right')
    floor = rows[-1]['thresholds']['per_dimension']
    for dim, label in LABELS.items():
        vals = [r['scores'][dim] for r in rows if dim in r['scores']]
        if not vals:
            continue
        below = sum(1 for v in vals if v < floor)
        t.add_row(label, str(min(vals)), f'{median(vals):g}', str(max(vals)), f'{below} 次' if below else '—')
    console.print(t)
    totals = [r['total'] for r in rows]
    limit = rows[-1]['thresholds']['total']
    console.print(f'总分：最低 {min(totals)}／中位 {median(totals):g}／最高 {max(totals)}（当前线 {limit}/35）')
    console.print(f'通过 {sum(1 for r in rows if r["passed"])}/{len(rows)} 次')
    by_ch = {}
    for r in rows:
        by_ch.setdefault(r['ch'], []).append(r)
    deltas = [rs[-1]['total'] - rs[0]['total'] for rs in by_ch.values() if len(rs) > 1]
    if deltas:
        console.print(f'修订前后总分变化：{"、".join(f"{d:+d}" for d in deltas)}（{len(deltas)} 章有过修订）')
    else:
        console.print('[dim]还没有哪一章修订后被重新评审过 —— 修订有没有用还看不出来[/]')
    return None


# TODO(重建): 需确认装饰器（原代码为 typer CLI，命令函数应有 @app.command() 及选项参数）
def check(path, chapter):
    '对已有稿件跑一遍 gate（不调模型）。'
    state = StateStore(STATE_PATH).load() if STATE_PATH.exists() else None
    report = Gate.from_config(ROOT / 'config' / 'project.yaml').check(
        Path(path).read_text('utf-8'), state=state, expected_ch=chapter or None
    )
    console.print(report.render())
    raise typer.Exit(0 if report.passed else 1)


# TODO(重建): 原文件常量表含 '__main__'，应有 `if __name__ == '__main__':` 入口（typer app() 调用），骨架未含模块级字节码，需确认
