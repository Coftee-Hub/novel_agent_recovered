# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# 本文件由 pyc 恢复生成（加密前的编译产物）
# 原文件 : /Users/weizihang/Desktop/agent制作/novel_agent/src/novel_agent/skills.py
# 来源   : skills.cpython-314.pyc
# 方法   : 明文 Python3.14 + marshal/dis
# 字符串常量 / 函数签名 / docstring = 100% 原样
# ═══════════════════════════════════════════════════════

from __future__ import annotations

__doc__ = '写作经验库的加载与拼装。\n\nskills 是人类可读可编辑的 markdown，直接进 prompt 的 system_core ——\n也就是缓存前缀的最前端。因此**拼接顺序必须确定**：顺序一变，前缀字节\n就变，整卷的缓存全部失效，而且不会有任何报错。\n\n这里用显式顺序 + 字节稳定性测试把这件事钉死。\n'

# 模块级字符串常量（100% 原样）
_RECOVERED_CONSTS = {
    0: '写作经验库的加载与拼装。\n\nskills 是人类可读可编辑的 markdown，直接进 prompt 的 system_core ——\n也就是缓存前缀的最前端。因此**拼接顺序必须确定**：顺序一变，前缀字节\n就变，整卷的缓存全部失效，而且不会有任何报错。\n\n这里用显式顺序 + 字节稳定性测试把这件事钉死。\n',
    4: 'SkillNotFound',
    6: 'SkillLibrary',
    7: 'list[str]',
    8: 'WRITER_SKILLS',
    9: 'ARCHITECT_SKILLS',
}

# 全部代码对象内的字符串常量（100% 原样），键=(对象名, 下标)
_RECOVERED_FN_CONSTS = {
    ('SkillNotFound', 0): 'SkillNotFound',
    ('SkillLibrary', 0): 'SkillLibrary',
    ('SkillLibrary', 7): 'strict',
    ('__annotate__', 1): 'skills_dir',
    ('__annotate__', 2): 'str | Path',
    ('__annotate__', 3): 'return',
    ('__annotate__', 4): 'None',
    ('__annotate__', 1): 'return',
    ('__annotate__', 2): 'list[str]',
    ('available', 0): '已有的 skill 名（不含扩展名），排序后返回。',
    ('available', 2): '*.md',
    ('__annotate__', 1): 'name',
    ('__annotate__', 2): 'str',
    ('__annotate__', 3): 'return',
    ('load', 0): '.md',
    ('load', 1): '、',
    ('load', 2): '（空）',
    ('load', 3): '找不到 skill ',
    ('load', 4): '。现有：',
    ('load', 5): 'utf-8',
    ('__annotate__', 1): 'names',
    ('__annotate__', 2): 'list[str]',
    ('__annotate__', 3): 'strict',
    ('__annotate__', 4): 'bool',
    ('__annotate__', 5): 'return',
    ('__annotate__', 6): 'str',
    ('compose', 0): '按**给定顺序**拼接。顺序是调用方的责任，不做隐式排序。\n\nstrict=False 时跳过缺失的 skill —— 语料还没到位、部分 skill 尚未\n萃取时用得上。\n',
    ('compose', 1): '\n\n---\n\n',
}

# ───────────── 还原后的源码 ─────────────
from pathlib import Path


class SkillNotFound(Exception):
    pass


class SkillLibrary:
    def __init__(self, skills_dir: str | Path) -> None:
        self.dir = Path(skills_dir)

    def available(self) -> list[str]:
        """已有的 skill 名（不含扩展名），排序后返回。"""
        return sorted(p.stem for p in self.dir.glob("*.md"))

    def load(self, name: str) -> str:
        path = self.dir / f"{name}.md"
        if not path.exists():
            have = "、".join(self.available()) or "（空）"
            raise SkillNotFound(f"找不到 skill {name!r}。现有：{have}")
        return path.read_text("utf-8").strip()

    def compose(self, names: list[str], *, strict: bool = True) -> str:
        """按**给定顺序**拼接。顺序是调用方的责任，不做隐式排序。

        strict=False 时跳过缺失的 skill —— 语料还没到位、部分 skill 尚未
        萃取时用得上。
        """
        parts: list[str] = []
        for name in names:
            try:
                parts.append(self.load(name))
            except SkillNotFound:
                if strict:
                    raise
        return "\n\n---\n\n".join(parts)


# ── 模块级导出名（由调用方引用反推）──
# TODO(重建): WRITER_SKILLS / ARCHITECT_SKILLS 的具体内容无法从 .pyc 还原，
# 这两个名字出现在模块级字符串常量表（下标 8/9），应为 writer / architect
# 使用的 skill 名清单。此处留占位，编译可通过。
WRITER_SKILLS: list[str] = []
ARCHITECT_SKILLS: list[str] = []
