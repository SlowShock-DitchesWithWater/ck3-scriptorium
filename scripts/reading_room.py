# -*- coding: utf-8 -*-
"""阅览室（reading_room/）目录同步器——自选文章层（2026-10-29 新增）。

职责：
- 扫描 reading_room/articles/*.md 的头部字段（title/source/author/found/
  game_version/tags/digest，单层 key: value，标准库可解析，不引入 yaml 依赖）；
- --sync：把条目再生进 catalog.md 末尾的标记区块
  （<!-- ck3wiki-mod-kb:reading-room BEGIN/END -->，整块机械生成，
  catalog.py 的重跑不触碰该区块）；
- --check：校验头部字段齐全 + 目录区块与盘上文章一致（CI 跑这个）。

权威级：阅览室为参考级（最低），与 wiki/dump 冲突时以后者为准
（AGENTS.md §0 权威表）。许可红线：只收自写笔记+出处，不收原文全文
（reading_room/README.md）。
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import config  # noqa: E402

ROOM_DIR = config.REPO_ROOT / "reading_room"
ARTICLES_DIR = ROOM_DIR / "articles"
REQUIRED = ["title", "source", "author", "found", "game_version", "tags", "digest"]
MARK_BEGIN = "<!-- ck3wiki-mod-kb:reading-room BEGIN -->"
MARK_END = "<!-- ck3wiki-mod-kb:reading-room END -->"


def parse_article(path: Path) -> dict:
    """解析单篇头部。返回 {字段: 值, '_file': 相对路径}；不合法抛 ValueError。"""
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        raise ValueError("缺少 --- 头部区块")
    fields: dict[str, str] = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(\w+):\s*(.+)$", line.strip())
        if kv:
            fields[kv.group(1)] = kv.group(2).strip()
    missing = [k for k in REQUIRED if not fields.get(k)]
    if missing:
        raise ValueError(f"头部缺字段：{missing}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fields["found"]):
        raise ValueError(f"found 应为 YYYY-MM-DD，得到 {fields['found']!r}")
    fields["_file"] = path.relative_to(config.REPO_ROOT).as_posix()
    return fields


def load_articles() -> list[dict]:
    """读全部文章并按发现日期倒序（新在前）。"""
    if not ARTICLES_DIR.is_dir():
        return []
    arts = []
    for p in sorted(ARTICLES_DIR.glob("*.md")):
        if p.name.startswith("_"):   # _template.md 等非文章文件跳过
            continue
        arts.append(parse_article(p))
    return sorted(arts, key=lambda a: (a["found"], a["title"]), reverse=True)


def render_section(articles: list[dict]) -> str:
    """渲染 catalog 的阅览室标记区块（整块机械生成，无人工字段）。"""
    lines = [MARK_BEGIN,
             "## 阅览室 · 自选文章（reading_room，参考级：与 wiki/dump 冲突时以后者为准）", ""]
    if not articles:
        lines.append("（暂无文章。添加方式见 `reading_room/README.md`：复制"
                     "`reading_room/_template.md` 到 `reading_room/articles/`，"
                     "填头部字段后跑 `python scripts/reading_room.py --sync`）")
    for a in articles:
        lines += [
            f"### 阅览室 · {a['title']}",
            f"- **文件**：`{a['_file']}`",
            f"- **来源**：{a['source']}（作者 {a['author']}，发现于 {a['found']}，"
            f"适用版本 {a['game_version']}）",
            f"- **摘要**：{a['digest']}",
            f"- **标签**：{a['tags']}",
            f"- **权威级**：参考（自写笔记+出处，非权威来源；冲突以 dump/wiki 为准）",
            "",
        ]
    lines.append(MARK_END)
    return "\n".join(lines) + "\n"


def sync() -> int:
    """把阅览室区块再生进 catalog.md（存在则整块替换，不存在则追加到末尾）。"""
    arts = load_articles()
    section = render_section(arts)
    cat = config.CATALOG_PATH
    text = cat.read_text(encoding="utf-8")
    if MARK_BEGIN in text and MARK_END in text:
        text = re.sub(re.escape(MARK_BEGIN) + r".*?" + re.escape(MARK_END),
                      lambda _: section.rstrip("\n"), text, flags=re.S)
    else:
        text = text.rstrip("\n") + "\n\n" + section
    cat.write_text(text, encoding="utf-8", newline="\n")
    print(f"[reading_room] 目录区块已同步（{len(arts)} 篇文章）")
    return 0


def check() -> int:
    """校验：文章头部合法 + catalog 区块与盘上文章逐字一致。空室也通过。"""
    arts = load_articles()
    want = render_section(arts)
    text = config.CATALOG_PATH.read_text(encoding="utf-8") if config.CATALOG_PATH.is_file() else ""
    ok = want.strip() in text
    print(f"[reading_room][check] 文章 {len(arts)} 篇，头部全部合法；"
          f"目录区块{'一致' if ok else '不一致（跑 --sync 刷新）'}")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    mode = (argv or sys.argv[1:])[0] if (argv or sys.argv[1:]) else "--sync"
    try:
        if mode == "--sync":
            return sync()
        if mode == "--check":
            return check()
    except ValueError as exc:
        print(f"[reading_room] FAIL  {exc}", file=sys.stderr)
        return 1
    print("用法：python scripts/reading_room.py --sync | --check")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
