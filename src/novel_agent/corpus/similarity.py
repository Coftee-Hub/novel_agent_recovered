"""n-gram 抄袭检测 —— 抄袭防线的第 2 道（硬闸门）。

第 1 道是 prompt 里的禁止复用指令，那道靠模型自觉。这一道不靠。

索引只存 n-gram 的哈希，不存原文：内存小，且索引文件本身不含版权内容。
比对前会剥掉所有标点与空白，所以改排版、加逗号都逃不掉。
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

# 只保留会构成"实质内容"的字符：汉字、字母、数字。
# 标点/空白全部剥掉 —— 否则把「，」改成「、」就能绕过检测。
_NOISE = re.compile(r"[^一-鿿0-9A-Za-z]+")

DEFAULT_N = 13


def normalize(text: str) -> str:
    return _NOISE.sub("", text)


def _hash(gram: str) -> str:
    return hashlib.blake2b(gram.encode("utf-8"), digest_size=8).hexdigest()


class NGramIndex:
    def __init__(self, n: int = DEFAULT_N) -> None:
        self.n = n
        self._hashes: set[str] = set()

    def __len__(self) -> int:
        return len(self._hashes)

    @property
    def is_empty(self) -> bool:
        return not self._hashes

    def add_text(self, text: str) -> int:
        norm = normalize(text)
        added = 0
        for i in range(len(norm) - self.n + 1):
            self._hashes.add(_hash(norm[i : i + self.n]))
            added += 1
        return added

    def add_path(self, path: str | Path, patterns: tuple[str, ...] = ("*.txt", "*.md")) -> int:
        """索引一个文件或整个目录。"""
        p = Path(path)
        files = [p] if p.is_file() else [f for pat in patterns for f in p.rglob(pat)]
        total = 0
        for f in files:
            try:
                total += self.add_text(f.read_text("utf-8", errors="ignore"))
            except OSError:
                continue
        return total

    def find_matches(self, text: str, limit: int = 5) -> list[str]:
        """返回生成文本中与语料重合的 n-gram 片段（去重、不重叠）。"""
        norm = normalize(text)
        hits: list[str] = []
        i = 0
        while i <= len(norm) - self.n:
            gram = norm[i : i + self.n]
            if _hash(gram) in self._hashes:
                hits.append(gram)
                if len(hits) >= limit:
                    break
                i += self.n  # 跳过整段，避免同一处报 n 次
            else:
                i += 1
        return hits

    # ---- 持久化 ----

    def save(self, path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            json.dumps({"n": self.n, "hashes": sorted(self._hashes)}, sort_keys=True),
            "utf-8",
        )

    @classmethod
    def load(cls, path: str | Path) -> NGramIndex:
        data = json.loads(Path(path).read_text("utf-8"))
        idx = cls(n=data["n"])
        idx._hashes = set(data["hashes"])
        return idx
