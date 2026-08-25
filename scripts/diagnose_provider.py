"""隔离供应商拒绝的是哪个请求特性。

中转站/号池渠道常见两类失败，症状相同但处置完全不同：
  - 确定性拒绝：某个参数不被支持 → 去掉即可
  - 号池抖动：随机路由到失效账号 → 靠重试

所以每种变体重复多次，用成功率区分二者。

    .venv/bin/python scripts/diagnose_provider.py [provider] [repeats]
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from novel_agent.llm import Router  # noqa: E402

BIG = "你是一位专精现代言情的中文小说写作者。写作时注重人物内心的克制与留白。\n" * 14


def load_env() -> None:
    env = ROOT / ".env"
    if not env.exists():
        return
    for raw in env.read_text("utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip().strip("\"'"))


def attempt(url: str, headers: dict, body: dict) -> tuple[bool, str]:
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(), headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            usage = json.loads(resp.read().decode()).get("usage", {})
            return True, (
                f"in={usage.get('input_tokens')} "
                f"cw={usage.get('cache_creation_input_tokens')} "
                f"cr={usage.get('cache_read_input_tokens')}"
            )
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "ignore")
        return False, f"{exc.code} {detail[:80]}"
    except Exception as exc:  # noqa: BLE001
        return False, f"{type(exc).__name__}"


def main() -> int:
    load_env()
    name = sys.argv[1] if len(sys.argv) > 1 else "packyapi"
    repeats = int(sys.argv[2]) if len(sys.argv) > 2 else 3

    router = Router(ROOT / "config" / "models.yaml")
    cfg = router.provider(name)
    secret = os.environ.get(cfg.api_key_env)
    if not secret:
        print(f"✗ {cfg.api_key_env} 未设置")
        return 2

    url = f"{(cfg.base_url or 'https://api.anthropic.com').rstrip('/')}/v1/messages"
    headers = {
        "Authorization": f"Bearer {secret}" if cfg.auth_style == "bearer" else secret,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    if cfg.auth_style != "bearer":
        headers = {k: v for k, v in headers.items() if k != "Authorization"}
        headers["x-api-key"] = secret

    msg = [{"role": "user", "content": "说一个字"}]
    model = "claude-opus-5"
    variants: list[tuple[str, dict]] = [
        ("基线：裸请求", {"model": model, "max_tokens": 16, "messages": msg}),
        ("+ system 字符串", {"model": model, "max_tokens": 16, "messages": msg,
                             "system": BIG}),
        ("+ system 块 + cache_control", {"model": model, "max_tokens": 16, "messages": msg,
            "system": [{"type": "text", "text": BIG,
                        "cache_control": {"type": "ephemeral"}}]}),
        ("+ 多块 cache_control", {"model": model, "max_tokens": 16,
            "system": [{"type": "text", "text": BIG,
                        "cache_control": {"type": "ephemeral"}}],
            "messages": [{"role": "user", "content": [
                {"type": "text", "text": BIG, "cache_control": {"type": "ephemeral"}}]},
                {"role": "user", "content": [{"type": "text", "text": "说一个字"}]}]}),
        ("+ output_config.effort", {"model": model, "max_tokens": 16, "messages": msg,
            "output_config": {"effort": "high"}}),
        ("+ thinking adaptive", {"model": model, "max_tokens": 16, "messages": msg,
            "thinking": {"type": "adaptive"}}),
    ]

    print(f"供应商 {name} | {url} | 每项重复 {repeats} 次\n")
    print(f"{'变体':32} {'成功率':>8}  详情")
    print("-" * 78)
    for label, body in variants:
        oks, notes = 0, []
        for _ in range(repeats):
            ok, note = attempt(url, headers, body)
            oks += ok
            notes.append(note)
        rate = f"{oks}/{repeats}"
        sample = notes[-1] if oks else next((n for n in notes if n), "")
        mark = "✓" if oks == repeats else ("~" if oks else "✗")
        print(f"{mark} {label:30} {rate:>8}  {sample[:44]}")

    print("\n判读：")
    print("  某项 0/N 而基线 N/N → 该参数被确定性拒绝，去掉它")
    print("  各项都是中间值      → 号池抖动，加重试而非改参数")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
