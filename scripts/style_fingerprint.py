"""量化文风指纹 —— 给"选谁当文风源"提供依据，而不是凭印象。

测的都是可复现的表层特征：句长、短句率、比喻密度、心理描写密度、
感官通道、语气词。这些恰好是 writer 能被 prompt 影响的维度。
"""

from __future__ import annotations

import re
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from novel_agent.corpus.ingest import clean, read_text, split_chapters  # noqa: E402

CJK = re.compile(r"[一-鿿]")
SENT = re.compile(r"[^。！？…]+[。！？…]+")
DIALOGUE = re.compile(r"[“][^”]*[”]")

MARKERS: dict[str, tuple[str, ...]] = {
    "比喻": ("像", "仿佛", "如同", "似的", "宛如", "好比"),
    "心理": ("想", "觉得", "以为", "意识到", "明白", "知道", "记得", "察觉"),
    "视觉": ("看", "望", "瞥", "盯", "视线", "目光", "眼神"),
    "触温": ("凉", "暖", "热", "冷", "烫", "指尖", "掌心", "温度"),
    "听觉": ("听", "声音", "响", "安静", "寂静", "脚步声"),
    "语气词": ("吧", "呢", "啊", "嘛", "呀", "啦"),
    "转折": ("却", "可是", "但是", "然而", "只是", "偏偏"),
}


def analyse(path: Path) -> dict | None:
    raw, _ = read_text(path)
    body, _ = clean(raw)
    chapters = [c for c in split_chapters(body) if c.word_count > 500]
    if len(chapters) < 5:
        return None
    # 取中段，避开开头铺陈与结尾收束
    sample = "\n".join(c.body for c in chapters[len(chapters) // 3:][:30])
    chars = len(CJK.findall(sample)) or 1
    per10k = 10_000 / chars

    narration = DIALOGUE.sub("", sample)          # 剥掉对话，只看叙述
    sents = [s.strip() for s in SENT.findall(narration) if len(s.strip()) > 1]
    lens = [len(CJK.findall(s)) for s in sents] or [0]
    paras = [len(p.strip()) for p in sample.split("\n") if p.strip()]

    return {
        "句长中位": st.median(lens),
        "短句率": sum(1 for x in lens if x <= 10) / len(lens),
        "长句率": sum(1 for x in lens if x >= 30) / len(lens),
        "段中位": st.median(paras),
        "对话占比": sum(len(m) for m in DIALOGUE.findall(sample)) / (len(re.sub(r"\s", "", sample)) or 1),
        **{k: sum(sample.count(w) for w in ws) * per10k for k, ws in MARKERS.items()},
    }


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "corpus" / "core"
    rows = []
    for f in sorted(src.glob("*.txt")):
        r = analyse(f)
        if r:
            rows.append((f.stem, r))

    cols = ["句长中位", "短句率", "长句率", "段中位", "对话占比",
            "比喻", "心理", "视觉", "触温", "听觉", "语气词", "转折"]
    head = f"{'书名':16}" + "".join(f"{c:>7}" for c in cols)
    print(head); print("-" * len(head.encode("gbk", "ignore")))
    for name, r in sorted(rows, key=lambda x: -x[1]["短句率"]):
        cells = ""
        for c in cols:
            v = r[c]
            cells += f"{v:>7.0%}" if c in ("短句率", "长句率", "对话占比") else f"{v:>7.1f}"
        print(f"{name[:15]:16}{cells}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
