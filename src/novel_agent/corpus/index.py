# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/corpus/index.py
# 来源   : index.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '语料检索 —— 给写作时提供同类场景的写法参照。\n\n## 为什么是 BM25 而不是向量检索\n\n可用的两个供应商（PackyAPI / DeepSeek）都不提供 embedding 模型，本地\nembedding 要拖进 torch（约 2GB）。而 RAG 在本项目里的价值尚未验证 ——\nskills 已经承载了文风，检索片段只是额外的锚。\n\n场景规格里最有区分度的是**具象词**：地点、物件、节拍名（「雨中共伞」）。\nBM25 对这些够用，对抽象情绪（「戒备→动摇」）不行 —— 这是已知的局限。\n\n打分器做成可替换的：若实测发现词法检索不够，换成 embedding 只需实现\n同一个 `score()` 接口，索引结构和调用方都不用动。\n\n## 抄袭风险\n\n检索出来的是**原文片段**，会进 writer 的 prompt。三道防线里这是第一道\n（prompt 层的禁止复用指令由 prompt_builder 负责），gate 的 n-gram 硬闸门\n是第二道。这里额外做一件事：**同一本书的片段最多取一条**，避免连续多段\n来自同一处，那样最容易被整段模仿。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '语料检索 —— 给写作时提供同类场景的写法参照。\n\n## 为什么是 BM25 而不是向量检索\n\n可用的两个供应商（PackyAPI / DeepSeek）都不提供 embedding 模型，本地\nembedding 要拖进 torch（约 2GB）。而 RAG 在本项目里的价值尚未验证 ——\nskills 已经承载了文风，检索片段只是额外的锚。\n\n场景规格里最有区分度的是**具象词**：地点、物件、节拍名（「雨中共伞」）。\nBM25 对这些够用，对抽象情绪（「戒备→动摇」）不行 —— 这是已知的局限。\n\n打分器做成可替换的：若实测发现词法检索不够，换成 embedding 只需实现\n同一个 `score()` 接口，索引结构和调用方都不用动。\n\n## 抄袭风险\n\n检索出来的是**原文片段**，会进 writer 的 prompt。三道防线里这是第一道\n（prompt 层的禁止复用指令由 prompt_builder 负责），gate 的 n-gram 硬闸门\n是第二道。这里额外做一件事：**同一本书的片段最多取一条**，避免连续多段\n来自同一处，那样最容易被整段模仿。\n',
    7: '[一-鿿]+',
    8: '[a-zA-Z0-9]+',
    12: 'Passage',
    14: 'PassageIndex',
    16: 'SceneRetriever',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[str]',
    ('tokenize', 0): '切成检索用的词法单元。\n\n中文没有空格分词。用二元字组（bigram）做词法单元：对中文检索效果接近\n分词，又不需要词典和分词器依赖。单字的段落保留为单字，否则「雨」这样\n的单字查询会得到空结果。\n',
    ('Passage', 0): 'Passage',
    ('Passage', 1): 'str',
    ('Passage', 2): 'book',
    ('Passage', 3): 'int',
    ('Passage', 4): 'chapter',
    ('Passage', 5): 'text',
    ('Passage', 8): 'Counter[str]',
    ('Passage', 9): 'tokens',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('PassageIndex', 0): 'PassageIndex',
    ('PassageIndex', 1): 'BM25 检索。\n\n参数取 Robertson 的经典默认值：k1 控制词频饱和，b 控制长度归一化。\n',
    ('PassageIndex', 11): 'min_chars',
    ('PassageIndex', 13): 'max_chars',
    ('PassageIndex', 23): 'limit',
    ('PassageIndex', 24): 'per_book',
    ('__annotate__', 1): 'passages',
    ('__annotate__', 2): 'list[Passage] | None',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'bool',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'min_chars',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'max_chars',
    ('__annotate__', 6): 'return',
    ('add_book', 0): '把一本书切成检索片段。\n\n按段落聚合到目标长度，不跨章。片段太短没有风格信息，太长会挤占\nwriter 的上下文，也更容易被整段模仿。\n',
    ('__annotate__', 1): 'src',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'patterns',
    ('__annotate__', 4): 'tuple[str, ...]',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'int',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'None',
    ('__annotate__', 1): 'query_tokens',
    ('__annotate__', 2): 'list[str]',
    ('__annotate__', 3): 'passage',
    ('__annotate__', 4): 'Passage',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'float',
    ('score', 0): 'BM25。换成向量检索时替换这个方法即可，其余不用动。',
    ('__annotate__', 1): 'query',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'limit',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'per_book',
    ('__annotate__', 6): 'return',
    ('__annotate__', 7): 'list[tuple[float, Passage]]',
    ('search', 0): '检索。\n\n`per_book` 限制同一本书最多取几条 —— 连续多段来自同一处最容易\n被整段模仿，也会让风格锚偏向单一作者。\n',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('save', 2): 'book',
    ('save', 3): 'chapter',
    ('save', 4): 'text',
    ('save', 7): 'utf-8',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'PassageIndex',
    ('load', 0): 'utf-8',
    ('load', 1): 'book',
    ('load', 2): 'chapter',
    ('load', 3): 'text',
    ('SceneRetriever', 0): 'SceneRetriever',
    ('SceneRetriever', 1): '把场景规格翻译成检索式，取回风格参照片段。',
    ('SceneRetriever', 2): 'limit',
    ('__annotate__', 1): 'index',
    ('__annotate__', 2): 'PassageIndex',
    ('__annotate__', 3): 'limit',
    ('__annotate__', 4): 'int',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'None',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('query_for', 0): '从规格里取有检索价值的部分。\n\n情绪词（「戒备」「动摇」）在正文里几乎不会字面出现，词法检索对它们\n无能为力 —— 但留着无害，换成向量检索后它们正是最有价值的部分。\n',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[str]',
}

# ───────────── 还原后的源码 ─────────────
import json
import math
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from novel_agent.corpus.ingest import clean, read_text, split_chapters

# 由模块级常量表（下标 7/8）还原的正则。
_CJK_RUN = re.compile(_RECOVERED_CONSTS[7])
_LATIN_RUN = re.compile(_RECOVERED_CONSTS[8])


def tokenize(text: str) -> list[str]:
    """切成检索用的词法单元。

    中文没有空格分词。用二元字组（bigram）做词法单元：对中文检索效果接近
    分词，又不需要词典和分词器依赖。单字的段落保留为单字，否则「雨」这样
    的单字查询会得到空结果。
    """
    tokens: list[str] = []
    for run in _CJK_RUN.findall(text):
        if len(run) == 1:
            tokens.append(run)
        else:
            tokens += [run[i : i + 2] for i in range(len(run) - 1)]
    tokens += _LATIN_RUN.findall(text)
    return tokens


@dataclass
class Passage:
    book: str
    chapter: int
    text: str
    tokens: Counter[str] = field(default_factory=Counter, repr=False)

    @property
    def length(self) -> int:
        return sum(self.tokens.values())


class PassageIndex:
    """BM25 检索。

    参数取 Robertson 的经典默认值：k1 控制词频饱和，b 控制长度归一化。
    """

    K1 = 1.5
    B = 0.75

    def __init__(self, passages: list[Passage] | None = None) -> None:
        self.passages: list[Passage] = passages or []
        self._df: Counter[str] = Counter()
        self._avg_len = 0.0
        if self.passages:
            self._reindex()

    def __len__(self) -> int:
        return len(self.passages)

    @property
    def is_empty(self) -> bool:
        return not self.passages

    def add_book(
        self, path: str | Path, *, min_chars: int = 300, max_chars: int = 1200
    ) -> int:
        """把一本书切成检索片段。

        按段落聚合到目标长度，不跨章。片段太短没有风格信息，太长会挤占
        writer 的上下文，也更容易被整段模仿。
        """
        raw, _ = read_text(path)
        body, _ = clean(raw)
        book = Path(path).stem
        added = 0
        for chapter in split_chapters(body):
            buf: list[str] = []
            size = 0
            for para in chapter.body.split("\n"):
                para = para.strip()
                if not para:
                    continue
                buf.append(para)
                size += len(para)
                if size >= min_chars:
                    if size <= max_chars or len(buf) == 1:
                        self.passages.append(Passage(book, chapter.index, "\n".join(buf)))
                        added += 1
                        size, buf = 0, []
                    else:
                        tail = buf.pop()
                        self.passages.append(Passage(book, chapter.index, "\n".join(buf)))
                        added += 1
                        size, buf = len(tail), [tail]
            if buf and size >= min_chars // 2:
                self.passages.append(Passage(book, chapter.index, "\n".join(buf)))
                added += 1
        self._reindex()
        return added

    def add_dir(
        self,
        src: str | Path,
        patterns: tuple[str, ...] = ("*.txt", "*.md", "*.epub"),
    ) -> int:
        total = 0
        for f in sorted(f for pat in patterns for f in Path(src).glob(pat)):
            total += self.add_book(f)
        return total

    def _reindex(self) -> None:
        self._df = Counter()
        for p in self.passages:
            if not p.tokens:
                p.tokens = Counter(tokenize(p.text))
            self._df.update(p.tokens.keys())
        if self.passages:
            self._avg_len = sum(p.length for p in self.passages) / len(self.passages)
        else:
            self._avg_len = 0.0

    def score(self, query_tokens: list[str], passage: Passage) -> float:
        """BM25。换成向量检索时替换这个方法即可，其余不用动。"""
        n = len(self.passages)
        total = 0.0
        for token in query_tokens:
            tf = passage.tokens.get(token, 0)
            if not tf:
                continue
            df = self._df.get(token, 0)
            idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
            norm = 1 - self.B + self.B * passage.length / (self._avg_len or 1)
            total += idf * tf * (self.K1 + 1) / (tf + self.K1 * norm)
        return total

    def search(
        self, query: str, *, limit: int = 4, per_book: int = 1
    ) -> list[tuple[float, Passage]]:
        """检索。

        `per_book` 限制同一本书最多取几条 —— 连续多段来自同一处最容易
        被整段模仿，也会让风格锚偏向单一作者。
        """
        if self.is_empty:
            return []
        tokens = tokenize(query)
        if not tokens:
            return []
        ranked = sorted(
            ((self.score(tokens, p), p) for p in self.passages),
            key=lambda x: -x[0],
        )
        picked: list[tuple[float, Passage]] = []
        seen: Counter[str] = Counter()
        for score, passage in ranked:
            if score <= 0:
                return picked
            if seen[passage.book] >= per_book:
                continue
            picked.append((score, passage))
            seen[passage.book] += 1
            if len(picked) >= limit:
                return picked
        return picked

    def save(self, path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            json.dumps(
                [
                    {"book": x.book, "chapter": x.chapter, "text": x.text}
                    for x in self.passages
                ],
                ensure_ascii=False,
            ),
            "utf-8",
        )

    @classmethod
    def load(cls, path: str | Path) -> PassageIndex:
        rows = json.loads(Path(path).read_text("utf-8"))
        return cls([Passage(r["book"], r["chapter"], r["text"]) for r in rows])


class SceneRetriever:
    """把场景规格翻译成检索式，取回风格参照片段。"""

    def __init__(self, index: PassageIndex, *, limit: int = 4) -> None:
        self.index = index
        self.limit = limit

    def query_for(self, scene) -> str:
        """从规格里取有检索价值的部分。

        情绪词（「戒备」「动摇」）在正文里几乎不会字面出现，词法检索对它们
        无能为力 —— 但留着无害，换成向量检索后它们正是最有价值的部分。
        """
        parts = [scene.beat_type, scene.where, scene.goal, scene.entry_emotion, scene.exit_emotion]
        return " ".join(p for p in parts if p)

    def snippets(self, scene) -> list[str]:
        if self.index.is_empty:
            return []
        return [p.text for _, p in self.index.search(self.query_for(scene), limit=self.limit)]
