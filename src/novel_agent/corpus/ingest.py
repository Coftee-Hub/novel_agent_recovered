# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/corpus/ingest.py
# 来源   : ingest.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '语料清洗与分章 —— 纯 Python，不调 LLM。\n\n处理中文网络小说 txt 的三个现实问题：\n1. 编码乱：大量 txt 是 GB18030 而非 UTF-8，直接按 utf-8 读会乱码或抛错\n2. 广告行：站点水印、"请收藏"、下载链接混在正文里\n3. 分章标记不统一：第一章 / 第1章 / 第 1 章 / 正文 第一章 …… 都有\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '语料清洗与分章 —— 纯 Python，不调 LLM。\n\n处理中文网络小说 txt 的三个现实问题：\n1. 编码乱：大量 txt 是 GB18030 而非 UTF-8，直接按 utf-8 读会乱码或抛错\n2. 广告行：站点水印、"请收藏"、下载链接混在正文里\n3. 分章标记不统一：第一章 / 第1章 / 第 1 章 / 正文 第一章 …… 都有\n',
    7: '第N章',
    8: '^[ \\t\\u3000]*(?:\\d{1,4}[ \\t\\u3000:：.、]+)?(?:正文[ \\t\\u3000]*)?(第[ \\t\\u3000]*[0-9零一二三四五六七八九十百千两]+[ \\t\\u3000]*[章节回卷篇])[ \\t\\u3000]*(.{0,40}?)[ \\t\\u3000]*$',
    9: 'Chapter',
    10: '^[ \\t\\u3000]*(?:\\d{1,4}[ \\t\\u3000:：.、]+)?(Chapter[ \\t\\u3000]*\\d+)[ \\t\\u3000]*(.{0,40}?)[ \\t\\u3000]*$',
    11: '编号：标题',
    12: '^[ \\t\\u3000]*(\\d{1,4})[:：][ \\t\\u3000]*(.{1,40}?)[ \\t\\u3000]*$',
    13: '第N',
    14: '^[ \\t\\u3000]*(第[ \\t\\u3000]*[0-9零一二三四五六七八九十百千两]+)(?![页次条种位个名天年月日节局场步点部集组队轮])[ \\t\\u3000]*(.{0,30}?)[ \\t\\u3000]*$',
    15: 'tuple[tuple[str, re.Pattern[str]], ...]',
    16: '_HEADING_PATTERNS',
    17: '\\n{3,}',
    18: ',',
    19: '，',
    20: ';',
    21: '；',
    22: ':',
    23: '：',
    24: '!',
    25: '！',
    26: '?',
    27: '？',
    28: '[一-鿿]',
    31: 'Book',
    32: '<[^>]+>',
    33: '</(p|div|h[1-6]|li|br)\\s*/?>',
    49: '。！？',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('Chapter', 0): 'Chapter',
    ('Chapter', 1): 'int',
    ('Chapter', 2): 'index',
    ('Chapter', 3): 'str',
    ('Chapter', 4): 'title',
    ('Chapter', 5): 'body',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('word_count', 0): '\\s',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'str',
    ('to_markdown', 0): '## 第',
    ('to_markdown', 1): '章 ',
    ('Book', 0): 'Book',
    ('Book', 1): 'Path',
    ('Book', 2): 'path',
    ('Book', 3): 'str',
    ('Book', 4): 'title',
    ('Book', 5): 'encoding',
    ('Book', 7): 'list[Chapter]',
    ('Book', 8): 'chapters',
    ('Book', 9): 'int',
    ('Book', 10): 'dropped_lines',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'int',
    ('__annotate__', 1): 'raw',
    ('__annotate__', 2): 'bytes',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('_xhtml_to_text', 0): 'XHTML → 纯文本。块级标签转换行，其余标签直接剥掉。',
    ('_xhtml_to_text', 1): 'utf-8',
    ('_xhtml_to_text', 2): 'ignore',
    ('_xhtml_to_text', 4): '<(script|style)\\b.*?</\\1>',
    ('_xhtml_to_text', 8): '<br\\s*/?>',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'str',
    ('read_epub', 0): '按 spine 顺序读 EPUB 正文。\n\n不引 ebooklib：EPUB 就是个 ZIP，标准库够用。按 spine 而非文件名排序 ——\n小说的章节顺序不一定和文件名字典序一致，排错了整本书就乱了。\n',
    ('read_epub', 2): 'META-INF/container.xml',
    ('read_epub', 3): 'rootfile',
    ('read_epub', 4): 'full-path',
    ('read_epub', 6): '/',
    ('read_epub', 8): 'item',
    ('read_epub', 9): 'id',
    ('read_epub', 10): 'href',
    ('read_epub', 11): 'itemref',
    ('read_epub', 12): 'idref',
    ('<genexpr>', 0): '.opf',
    ('<genexpr>', 0): '.xhtml',
    ('<genexpr>', 0): '/',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'tuple[str, str]',
    ('read_text', 0): '按候选编码依次尝试，返回 (文本, 命中的编码)。\n\n不引入 chardet：候选集小且确定，试解码比猜测更可靠。\n',
    ('read_text', 1): '.epub',
    ('read_text', 2): 'epub',
    ('read_text', 3): '�',
    ('read_text', 5): 'utf-8',
    ('read_text', 6): 'replace',
    ('read_text', 8): 'utf-8(替换)',
    ('__annotate__', 1): 'line',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'bool',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('fullwidth_near_cjk', 0): '把紧邻汉字的半角标点转成全角。\n\n只在紧邻汉字时转 —— 否则会毁掉 "3.5" "Wi-Fi" 这类合法的半角用法。\n',
    ('fullwidth_near_cjk', 2): '.',
    ('fullwidth_near_cjk', 3): '。',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('normalize_punctuation', 0): '统一到项目的格式规范，让 RAG 片段与萃取样本口径一致。\n\n顺序要紧：多字符标点（…… ——）必须先处理完，再做单字符全角化。\n反过来会把 "..." 的第一个点转成 "。"，后面的省略号规则就再也匹配不上了。\n',
    ('normalize_punctuation', 1): '．．．',
    ('normalize_punctuation', 2): '……',
    ('normalize_punctuation', 3): '...',
    ('normalize_punctuation', 4): '。。。',
    ('normalize_punctuation', 5): '…(?!…)(?<!……)',
    ('normalize_punctuation', 6): '…{3,}',
    ('normalize_punctuation', 7): '－－',
    ('normalize_punctuation', 8): '——',
    ('normalize_punctuation', 9): '--',
    ('normalize_punctuation', 10): '(?<!—)—(?!—)',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'tuple[str, int]',
    ('clean', 0): '去广告行、统一空白与标点。返回 (清洗后文本, 丢弃行数)。',
    ('__annotate__', 1): 'title',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'bool',
    ('is_plausible_title', 0): '标题合理性检查，用于剔除被误判成标题的正文行。',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'tuple[str, re.Pattern[str]] | None',
    ('detect_heading_pattern', 0): '探测该文件用的是哪种章节标记。\n\n不能简单取命中最多的：模式之间存在包含关系（"第N章" ⊂ "第N"），\n宽松模式必然命中更多，于是总是赢，把「章」字留在标题里。\n_HEADING_PATTERNS 已按"从具体到宽松"排序，所以优先取靠前的，\n只有当靠后的命中数显著更多（说明这本书确实用的是那种格式）才改用。\n',
    ('__annotate__', 1): 'text',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'list[Chapter]',
    ('split_chapters', 0): '按探测到的章节标记切分。找不到标记时整篇作为一章返回。',
    ('split_chapters', 3): '全文',
    ('split_chapters', 6): '无题',
    ('__annotate__', 1): 'path',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'Book',
    ('__annotate__', 1): 'src',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'dst',
    ('__annotate__', 4): 'str | Path | None',
    ('__annotate__', 5): 'patterns',
    ('__annotate__', 6): 'tuple[str, ...]',
    ('__annotate__', 7): 'return',
    ('__annotate__', 8): 'list[Book]',
    ('ingest_dir', 0): '清洗整个目录。给了 dst 就把结果写成每本一个 markdown。',
    ('ingest_dir', 2): '.md',
    ('ingest_dir', 5): '# ',
    ('ingest_dir', 9): 'utf-8',
}

# ───────────── 还原后的源码 ─────────────
import html
import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote
from xml.etree import ElementTree as ET

# TODO(重建): 下列模块级常量无法从 .pyc 精确还原取值，仅依据字节码引用点与
# 模块级常量表反推。值可能不完整，但类型与语义对齐原实现。

# 候选编码表：read_text 依序试解码。docstring 明确提到 GB18030。
_ENCODINGS: tuple[str, ...] = ("utf-8", "gb18030", "gbk", "big5")

# 广告行 / 站点水印的短特征串（is_junk 对 len<40 的行做包含检查）。
_JUNK_TOKENS: tuple[str, ...] = (
    "http://", "https://", "www.", "收藏", "推荐", "打赏",
    "加入书签", "章节列表", "请收藏", "下载地址",
)

# 标题合理性检查用的黑名单字符（is_plausible_title）。
_NOT_IN_TITLE: str = "。！？，、；：…—"

# 章节标记命中率阈值：命中数少于该值 / 平均每章行数少于该值即弃用。
_MIN_LINES_PER_CHAPTER: float = 3.0
_COMPETITIVE_SHARE: float = 0.8
_COMPETITIVE_MIN_HITS: int = 5

# 由模块级常量表（下标 32/33/28/17 等）还原的正则 —— 直接引用常量表保证字节一致。
_TAG = re.compile(_RECOVERED_CONSTS[32])
_BLOCK_END = re.compile(_RECOVERED_CONSTS[33], re.IGNORECASE)
# _IS_CJK 在字节码里被当作可调用对象使用（CALL 1：`_IS_CJK(ch)`），
# 而 re.Pattern 在 3.14 不可调用，故还原为绑定方法 `.match`，语义一致。
_IS_CJK = re.compile(_RECOVERED_CONSTS[28]).match
_BLANK_RUN = re.compile(_RECOVERED_CONSTS[17])

# 半角 → 全角 标点映射（fullwidth_near_cjk 用）。配对来自常量表下标 18-27。
_HALFWIDTH = {
    _RECOVERED_CONSTS[18]: _RECOVERED_CONSTS[19],
    _RECOVERED_CONSTS[20]: _RECOVERED_CONSTS[21],
    _RECOVERED_CONSTS[22]: _RECOVERED_CONSTS[23],
    _RECOVERED_CONSTS[24]: _RECOVERED_CONSTS[25],
    _RECOVERED_CONSTS[26]: _RECOVERED_CONSTS[27],
}

# 章节标记模式，按"从具体到宽松"排序（detect_heading_pattern 依赖此顺序）。
# 名字/正则字符串均直接取自已还原的常量表。
_HEADING_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (_RECOVERED_CONSTS[7], re.compile(_RECOVERED_CONSTS[8])),
    (_RECOVERED_CONSTS[9], re.compile(_RECOVERED_CONSTS[10])),
    (_RECOVERED_CONSTS[11], re.compile(_RECOVERED_CONSTS[12])),
    (_RECOVERED_CONSTS[13], re.compile(_RECOVERED_CONSTS[14])),
)


@dataclass
class Chapter:
    index: int
    title: str
    body: str

    @property
    def word_count(self) -> int:
        return len(re.sub(r"\s", "", self.body))

    def to_markdown(self) -> str:
        return f"## 第{self.index}章 {self.title}\n\n{self.body}\n"


@dataclass
class Book:
    path: Path
    title: str
    encoding: str
    chapters: list[Chapter] = field(default_factory=list)
    dropped_lines: int = 0

    @property
    def word_count(self) -> int:
        return sum(c.word_count for c in self.chapters)


def _xhtml_to_text(raw: bytes) -> str:
    """XHTML → 纯文本。块级标签转换行，其余标签直接剥掉。"""
    s = raw.decode("utf-8", errors="ignore")
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = _BLOCK_END.sub("\n", s)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = _TAG.sub("", s)
    return html.unescape(s)


def read_epub(path: str | Path) -> str:
    """按 spine 顺序读 EPUB 正文。

    不引 ebooklib：EPUB 就是个 ZIP，标准库够用。按 spine 而非文件名排序 ——
    小说的章节顺序不一定和文件名字典序一致，排错了整本书就乱了。
    """
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()

        opf_name: str | None = None
        if "META-INF/container.xml" in names:
            root = ET.fromstring(zf.read("META-INF/container.xml"))
            for el in root.iter():
                if el.tag.endswith("rootfile"):
                    opf_name = el.get("full-path")
                    break
        if opf_name is None:
            opf_name = next((n for n in names if n.endswith(".opf")), None)

        docs: list[str] = []
        if opf_name:
            base = opf_name.rsplit("/", 1)[0] if "/" in opf_name else ""
            opf = ET.fromstring(zf.read(opf_name))
            manifest: dict[str, str] = {}
            for el in opf.iter():
                if el.tag.endswith("item"):
                    iid = el.get("id")
                    href = el.get("href")
                    if iid and href:
                        manifest[iid] = unquote(href)
            for el in opf.iter():
                if el.tag.endswith("itemref"):
                    href = manifest.get(el.get("idref")) or ""
                    if href:
                        docs.append(f"{base}/{href}" if base else href)

        if not docs:
            docs = sorted(
                n for n in names if n.lower().endswith((".xhtml", ".html", ".htm"))
            )

        parts: list[str] = []
        for name in docs:
            if name not in names:
                name = next(
                    (n for n in names if n.endswith(name.split("/")[-1])), None
                )
                if name is None:
                    continue
            parts.append(_xhtml_to_text(zf.read(name)))
    return "\n\n".join(parts)


def read_text(path: str | Path) -> tuple[str, str]:
    """按候选编码依次尝试，返回 (文本, 命中的编码)。

    不引入 chardet：候选集小且确定，试解码比猜测更可靠。
    """
    p = Path(path)
    if p.suffix.lower() == ".epub":
        return read_epub(p), "epub"
    raw = p.read_bytes()
    for enc in _ENCODINGS:
        try:
            text = raw.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
        if text.count("�") < max(len(text), 1) * 0.001:
            return text, enc
    return raw.decode("utf-8", errors="replace"), "utf-8(替换)"


def is_junk(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if len(stripped) < 40 and any(tok in stripped for tok in _JUNK_TOKENS):
        return True
    return stripped.startswith(("---", "===", "***")) and len(set(stripped)) <= 2


def fullwidth_near_cjk(text: str) -> str:
    """把紧邻汉字的半角标点转成全角。

    只在紧邻汉字时转 —— 否则会毁掉 "3.5" "Wi-Fi" 这类合法的半角用法。
    """
    out: list[str] = []
    for i, ch in enumerate(text):
        prev = text[i - 1] if i else ""
        nxt = text[i + 1] if i + 1 < len(text) else ""
        near_cjk = bool(_IS_CJK(prev) or _IS_CJK(nxt))
        if ch in _HALFWIDTH and near_cjk:
            out.append(_HALFWIDTH[ch])
        elif ch == "." and _IS_CJK(prev) and not nxt.isdigit():
            out.append("。")
        else:
            out.append(ch)
    return "".join(out)


def normalize_punctuation(text: str) -> str:
    """统一到项目的格式规范，让 RAG 片段与萃取样本口径一致。

    顺序要紧：多字符标点（…… ——）必须先处理完，再做单字符全角化。
    反过来会把 "..." 的第一个点转成 "。"，后面的省略号规则就再也匹配不上了。
    """
    text = text.replace("．．．", "……").replace("...", "……").replace("。。。", "……")
    text = re.sub(r"…(?!…)(?<!……)", "……", text)
    text = re.sub(r"…{3,}", "……", text)
    text = text.replace("－－", "——").replace("--", "——")
    text = re.sub(r"(?<!—)—(?!—)", "——", text)
    return fullwidth_near_cjk(text)


def clean(text: str) -> tuple[str, int]:
    """去广告行、统一空白与标点。返回 (清洗后文本, 丢弃行数)。"""
    kept: list[str] = []
    dropped = 0
    for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if is_junk(line):
            dropped += 1
        else:
            kept.append(line.strip("　 \t"))
    joined = _BLANK_RUN.sub("\n\n", "\n".join(kept))
    return normalize_punctuation(joined).strip(), dropped


def is_plausible_title(title: str) -> bool:
    """标题合理性检查，用于剔除被误判成标题的正文行。"""
    t = title.strip()
    if not t:
        return True
    return not (len(t) <= 30 and any(ch in t for ch in _NOT_IN_TITLE))


def detect_heading_pattern(text: str) -> tuple[str, re.Pattern[str]] | None:
    """探测该文件用的是哪种章节标记。

    不能简单取命中最多的：模式之间存在包含关系（"第N章" ⊂ "第N"），
    宽松模式必然命中更多，于是总是赢，把「章」字留在标题里。
    _HEADING_PATTERNS 已按"从具体到宽松"排序，所以优先取靠前的，
    只有当靠后的命中数显著更多（说明这本书确实用的是那种格式）才改用。
    """
    lines = text.split("\n")
    viable: list[tuple[int, int, str, re.Pattern[str]]] = []
    for rank, (name, pattern) in enumerate(_HEADING_PATTERNS):
        hits = 0
        for ln in lines:
            m = pattern.match(ln)
            if not m:
                continue
            title = m.group(2) if m.lastindex and m.lastindex >= 2 and m.group(2) else ""
            if is_plausible_title(title):
                hits += 1
        if hits < 2:
            continue
        if len(lines) / hits < _MIN_LINES_PER_CHAPTER:
            continue
        viable.append((rank, hits, name, pattern))

    if not viable:
        return None

    top = max(hits for _, hits, _, _ in viable)
    competitive = [
        v
        for v in viable
        if v[1] >= top * _COMPETITIVE_SHARE or v[1] >= min(_COMPETITIVE_MIN_HITS, top)
    ]
    _, _, name, pattern = min(competitive, key=lambda v: v[0])
    return name, pattern


def split_chapters(text: str) -> list[Chapter]:
    """按探测到的章节标记切分。找不到标记时整篇作为一章返回。"""
    detected = detect_heading_pattern(text)
    if detected is None:
        body = "\n".join(ln for ln in text.split("\n") if ln.strip())
        if body:
            return [Chapter(1, "全文", body)]
        return []

    _, pattern = detected
    lines = text.split("\n")
    marks: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = pattern.match(line)
        if not m:
            continue
        title = m.group(2) if m.lastindex and m.lastindex >= 2 and m.group(2) else ""
        if not is_plausible_title(title):
            continue
        marks.append((i, title))

    chapters: list[Chapter] = []
    for n, (start, title) in enumerate(marks):
        end = marks[n + 1][0] if n + 1 < len(marks) else len(lines)
        body = "\n".join(ln for ln in lines[start + 1 : end] if ln.strip())
        if not body:
            continue
        chapters.append(Chapter(len(chapters) + 1, title or "无题", body))
    return chapters


def ingest_file(path: str | Path) -> Book:
    p = Path(path)
    text, encoding = read_text(p)
    cleaned, dropped = clean(text)
    return Book(
        path=p,
        title=p.stem,
        encoding=encoding,
        chapters=split_chapters(cleaned),
        dropped_lines=dropped,
    )


def ingest_dir(src: str | Path, dst: str | Path | None, patterns: tuple[str, ...]) -> list[Book]:
    """清洗整个目录。给了 dst 就把结果写成每本一个 markdown。"""
    src_path = Path(src)
    files = sorted(
        f
        for pat in patterns
        for f in src_path.rglob(pat)
    )
    books: list[Book] = []
    for f in files:
        book = ingest_file(f)
        if not book.chapters:
            continue
        books.append(book)
        if dst is not None:
            out = Path(dst) / f"{book.title}.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            content = f"# {book.title}\n\n" + "\n".join(
                c.to_markdown() for c in book.chapters
            )
            out.write_text(content, "utf-8")
    return books
