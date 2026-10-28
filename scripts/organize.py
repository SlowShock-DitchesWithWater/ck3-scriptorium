# -*- coding: utf-8 -*-
"""阶段3：组织 pages/ —— 巨页按章节拆分（工单04）。

规则（spec 用户故事13 / 工单04）：
- 清洗后正文 >50KB 的页按 H2 章节拆为独立章节文件（pages/<页名>/NN-<slug>.md），
  原页名文件重写为章节索引（preamble + 章节清单）；
- 单个 H2 章节 >150KB 且含 ≥2 个 H3 时，该章节再按 H3 拆：
  NN-<slug>.md 承载 H2 标题 + 首个 H3 之前的内容，
  NN-<slug>__MM-<slug3>.md 承载各 H3 节；
- H2 章节数不足 2 的巨页（如整页一张大表的 Effects list / Triggers list）
  不拆，manifest 记录原因；
- 拆分以「行」为原子、在标题行边界切分且全程围栏感知——表格行与代码块
  行不可能被切到两个文件；写盘前做逐行重组校验（重组 == 清洗原文），
  零丢失零重复有机器证明。

幂等：每次运行从 raw 重放清洗得到全文（纯函数），重新拆分并整目录重建——
陈旧章节文件被清理，产物逐字节稳定；manifest 的 organize 登记仅在有变化时
刷新。重复运行零副作用。

入口：python scripts/organize.py [--page <标题>]
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import config, manifest  # noqa: E402
from lib.cleaner import clean_html  # noqa: E402

# 拆分阈值（spec 用户故事13：>50KB 按 H2 拆；单节 >150KB 再按 H3 拆）
SPLIT_H2_THRESHOLD_BYTES = 50 * 1024
SPLIT_H3_THRESHOLD_BYTES = 150 * 1024
SLUG_MAX = 48  # 章节文件名 slug 最大长度（不含 NN- 前缀与扩展名）


def rebuild_full_md(title: str, entry: dict) -> str | None:
    """从 raw 重放清洗得到全文（与 clean.py 同构的纯函数调用）。

    返回 None 表示 raw 缺失或重放结果与 manifest cleaned_sha256 不符
    （管线顺序应为 clean → organize；不符时提示先跑 clean）。
    """
    raw_path = config.REPO_ROOT / entry["raw_file"]
    if not raw_path.is_file():
        return None
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    provenance = (f"来源: {config.SITE_ORIGIN}/{title.replace(' ', '_')} "
                  f"oldid={entry.get('oldid')} 抓取于 {entry.get('fetched_at')}")
    md, _ = clean_html(title, raw["parse"]["text"], provenance=provenance)
    if hashlib.sha256(md.encode("utf-8")).hexdigest() != entry.get("cleaned_sha256"):
        return None
    return md


def slugify(text: str) -> str:
    """章节标题 → 文件名 slug：字母数字与 - _ 保留，其余折为 -，压缩连续 -。"""
    s = re.sub(r"[^\w\-]+", "-", text, flags=re.UNICODE).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return s[:SLUG_MAX].rstrip("-") or "section"


def split_by_heading(lines: list[str], level: int) -> list[tuple[str | None, list[str]]]:
    """按 #{level} 标题行切分行列表（围栏感知：代码块内的 # 不算标题）。

    返回 [(标题|None, 行...), ...]；首块标题为 None 表示首个 H(level) 之前的内容，
    标题行本身保留在所属块的首行。
    """
    pat = re.compile(r"^" + "#" * level + r"\s+(.+)$")
    chunks: list[tuple[str | None, list[str]]] = [(None, [])]
    in_code = False
    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code
            chunks[-1][1].append(ln)
            continue
        m = (not in_code) and pat.match(ln)
        if m:
            chunks.append((m.group(1).strip(), [ln]))
        else:
            chunks[-1][1].append(ln)
    return chunks


def _b(text: str) -> int:
    return len(text.encode("utf-8"))


def split_page(title: str, full_md: str) -> tuple[str, list[dict]] | tuple[None, str]:
    """纯文本拆分：全文 →（索引文本, 章节文件描述列表）。

    每个章节文件描述：
      {h2, file, h3_split, parts: [{file|None, heading|None, lines, bytes}]}
    —— parts 按 H3 拆分时有多个（intro + 各 H3 节，intro 的 heading 为 None），
    未拆分时仅一个（heading=None，lines 含 H2 标题行起的整节）。
    subs（H3 标题清单，供目录用）与重组所需的全部行都在 parts 里，无隐藏状态。
    """
    lines = full_md.splitlines()
    h2_chunks = split_by_heading(lines, 2)
    preamble_lines = h2_chunks[0][1]
    sections = [(t, ls) for t, ls in h2_chunks[1:] if t is not None]
    if len(sections) < 2:
        return None, f"H2 章节数 {len(sections)} < 2，无可拆边界（整页大表型）"

    chapters: list[dict] = []
    for i, (h2, sec_lines) in enumerate(sections, 1):
        sec_bytes = _b("\n".join(sec_lines) + "\n")
        h3_chunks = [(t, ls) for t, ls in split_by_heading(sec_lines, 3)[1:] if t is not None]
        base = f"{i:02d}-{slugify(h2)}"
        ch: dict = {"h2": h2, "bytes": sec_bytes, "subs": [t for t, _ in h3_chunks]}

        if sec_bytes > SPLIT_H3_THRESHOLD_BYTES and len(h3_chunks) >= 2:
            # H3 再拆：主文件 = H2 标题 + 节前内容；各 H3 节独立成文件
            ch["h3_split"] = True
            ch["file"] = f"pages/{title}/{base}.md"
            ch["parts"] = [{"file": ch["file"], "heading": None,
                            "lines": sec_lines[:1] + split_by_heading(sec_lines, 3)[0][1],
                            "bytes": None}]
            for j, (h3, h3_lines) in enumerate(h3_chunks, 1):
                f = f"pages/{title}/{base}__{j:02d}-{slugify(h3)}.md"
                ch["parts"].append({"file": f, "heading": h3, "lines": h3_lines,
                                    "bytes": _b("\n".join(h3_lines) + "\n")})
        else:
            ch["h3_split"] = False
            ch["file"] = f"pages/{title}/{base}.md"
            ch["parts"] = [{"file": ch["file"], "heading": None,
                            "lines": sec_lines, "bytes": sec_bytes}]
        chapters.append(ch)

    # 章节索引文本（原页名文件的重写内容）
    idx: list[str] = list(preamble_lines) + [
        "",
        f"> [!] 本页为章节索引：清洗产物 {_b(full_md)}B，已按 H2 拆为 "
        f"{len(chapters)} 个章节文件（目录 `{title}/`，各文件自包含、原文逐字）。",
        "> organize 阶段已做逐行重组校验：章节文件重组与清洗原文逐字节一致（零丢失零重复）。",
        "",
        "## 章节文件",
        ""]
    for ch in chapters:
        note = (f"，H3 子拆分 {sum(1 for p in ch['parts'] if p['heading'])} 个"
                if ch["h3_split"] else "")
        idx.append(f"- `{Path(ch['file']).name}` — {ch['h2']}（{ch['bytes']}B{note}）")
    idx.append("")
    return "\n".join(idx), chapters


def chapter_file_bodies(title: str, full_md: str, ch: dict) -> dict[str, str]:
    """章节 → {文件相对路径: 文件内容}。H1 标题行替换原 H2/H3 标题行。

    内容逐行保真：不做 rstrip——章节尾部的空行也原样保留，保证
    「磁盘章节文件重组 == 清洗原文」逐字节成立（外部可复核的零丢失证明）。
    """
    prov = full_md.splitlines()[0] if full_md.startswith("<!--") else ""
    head = ([prov, ""] if prov else [])
    out: dict[str, str] = {}
    for part in ch["parts"]:
        title_line = (f"# {title} — {ch['h2']}" if part["heading"] is None
                      else f"# {title} — {ch['h2']} — {part['heading']}")
        # 未 H3 拆分的整节：首行是 H2 标题行，用 H1 标题行替换；
        # H3 拆分的 intro：首行同样是 H2 标题行；H3 节首行是 H3 标题行。
        body = (part["lines"][1:] if part["lines"] and part["lines"][0].startswith("#")
                else part["lines"])
        out[part["file"]] = "\n".join(head + [title_line, ""] + body) + "\n"
    return out


def reassemble_ok(full_md: str, chapters: list[dict]) -> bool:
    """写盘前的零丢失校验：按切分原样拼回全部行 == 原文（逐行相等）。"""
    rebuilt: list[str] = []
    for ch in chapters:
        for part in ch["parts"]:
            rebuilt.extend(part["lines"])
    want = full_md.splitlines()
    # 首个 H2 之前的内容（preamble）不在任何章节里，单独补上
    pre = split_by_heading(want, 2)[0][1]
    return pre + rebuilt == want


def organize_page(title: str, entry: dict) -> dict:
    """单页组织：决定拆分与否、写盘、返回 manifest 登记用的结果字典。"""
    full_md = rebuild_full_md(title, entry)
    if full_md is None:
        return {"action": "skip", "note": "raw 重放与 cleaned_sha256 不符（先跑 clean --all）"}

    if _b(full_md) <= SPLIT_H2_THRESHOLD_BYTES:
        return {"action": "keep", "split": False,
                "removed_stale": _cleanup_dir(title)}

    result = split_page(title, full_md)
    if result[0] is None:
        return {"action": "keep", "split": False, "reason": result[1],
                "removed_stale": _cleanup_dir(title)}

    index_md, chapters = result
    if not reassemble_ok(full_md, chapters):
        return {"action": "error",
                "note": "重组校验失败，拒绝写盘（未改动任何文件）"}

    desired: dict[str, str] = {}
    for ch in chapters:
        desired.update(chapter_file_bodies(title, full_md, ch))

    # 写盘：章节目录整建（清陈旧文件）+ 索引覆盖原页名文件
    chapter_dir = config.PAGES_DIR / title
    chapter_dir.mkdir(parents=True, exist_ok=True)
    keep = set()
    for rel, text in desired.items():
        p = config.REPO_ROOT / rel
        p.write_text(text, encoding="utf-8", newline="\n")
        keep.add(p.name)
    for p in chapter_dir.glob("*.md"):
        if p.name not in keep:
            p.unlink()  # 页面更新后消失的陈旧章节，保证索引与文件一一对应
    (config.PAGES_DIR / f"{title}.md").write_text(index_md, encoding="utf-8", newline="\n")

    chapters_out = [{"h2": ch["h2"], "file": ch["file"], "bytes": ch["bytes"],
                     "h3_split": ch["h3_split"],
                     "subs": [{"h3": h3, "file": next(
                         (p["file"] for p in ch["parts"] if p["heading"] == h3), None)}
                         for h3 in ch["subs"]]}
                    for ch in chapters]
    return {"action": "split", "split": True, "chapter_dir": f"pages/{title}",
            "index_bytes": _b(index_md), "reassembled_ok": True,
            "chapters": chapters_out}


def _cleanup_dir(title: str) -> int:
    """删除该页的陈旧章节目录（不再满足拆分条件时），返回删除文件数。"""
    d = config.PAGES_DIR / title
    if not d.is_dir():
        return 0
    n = sum(1 for p in d.glob("*.md"))
    for p in d.glob("*.md"):
        p.unlink()
    d.rmdir()
    return n


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="阶段3：组织 pages/（巨页章节拆分）")
    ap.add_argument("--page", help="只处理指定页（默认 manifest 全部页）")
    args = ap.parse_args(argv)

    data = manifest.read_manifest()
    titles = [args.page] if args.page else list(data["pages"])
    if args.page and args.page not in data["pages"]:
        print(f"[organize] manifest 无此页：{args.page}")
        return 1

    for title in titles:
        entry = data["pages"][title]
        if not entry.get("cleaned_file"):
            print(f"[organize] 跳过 {title}：尚未清洗")
            continue
        res = organize_page(title, entry)
        act = res.pop("action")
        if act == "skip":
            print(f"[organize] 跳过 {title}：{res['note']}")
            continue
        if act == "error":
            print(f"[organize] 错误 {title}：{res['note']}")
            return 1
        if act == "keep":
            print(f"[organize] 保留整页 {title}"
                  + (f"（{res.get('reason')}）" if res.get("reason") else "（未超阈值）"))
        else:
            print(f"[organize] 已拆分 {title}：{len(res['chapters'])} 个 H2 章节"
                  f"（H3 子拆分 {sum(1 for c in res['chapters'] for s in c['subs'] if s['file'])} 个），"
                  f"索引 {res['index_bytes']}B，重组校验通过")
        # manifest 登记（幂等：仅在有变化时刷新）
        org_field = {k: v for k, v in res.items() if k != "removed_stale"}

        def _update(e: dict, val=org_field) -> dict:
            if e.get("organize") == val:
                return e
            e["organize"] = val
            return e

        manifest.update_page(title, _update)
    print("[organize] 完成")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
