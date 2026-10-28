# -*- coding: utf-8 -*-
"""阶段4：生成/合并 catalog.md —— 知识库唯一检索入口的两级中文摘要目录。

条目 schema（与 docs/pipeline.md 契约一致）：
- 文件位置：pages/ 下的相对路径（拆分页附章节目录）
- 来源：页面 URL + oldid + 抓取日期 + 页面标注的游戏版本
- 何时查：人工维护（草稿由工单06 agent 填入 catalog.md，用户确认后固化）
- 中文摘要：人工维护（同上）
- 英文关键词：标题 + EXTRA_KEYWORDS 补充词（脚本术语）+ H2 补足，
  目标 KEYWORD_TARGET 个、上限 KEYWORD_MAX（体积压缩：H2 本就完整保留在
  章节列表里，关键词行只补脚本词汇的检索面）
- 章节列表：从清洗产物提取的 H2 章节（含其下子标题）

工单06 扩展：
- 头部快照块（ck3wiki-mod-kb:snapshot BEGIN/END）：抓取日期/页数/游戏版本/
  锚点 oldid，每次全量重跑机械重建（幂等替换），文件头本体永不动；
- 游戏权威层条目（game_docs/script_docs 12 个产物 + vanilla_structure
  INDEX/entry_map）：跟 wiki 条目同构、同走 BEGIN/END 标记与人工字段保护，
  条目内各自明示「权威层：与 wiki 冲突时以本条目为准」；
- 插入顺序：wiki 条目永远在游戏层标题之前（新 wiki 页插到游戏层标题上方，
  而不是文件末尾），游戏层条目追加在文件末尾。

幂等与人工字段保护：每页条目包裹在 BEGIN/END 标记内；重跑时
派生字段（文件位置/来源/关键词/章节）按 manifest 与 pages/ 重新生成，
但"何时查/中文摘要"若已被人工改过（不再等于占位符）则原样保留。
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import config, manifest  # noqa: E402

PLACEHOLDER = "（待人工补充）"

# 目录文件头（只在文件不存在时写入；存在则完全不动，保护人工修订）
CATALOG_HEADER = """# CK3 Modding 知识库目录（catalog）

> 检索规约：先读本目录定位文件与章节，再只读所需章节；禁止整库读入。
> 权威顺序：游戏 script_docs dump 层（game_docs/）> wiki 层（pages/）；
> 两层冲突时以 dump 层为准，冲突点会在条目中标注。
> 内容来源：ck3.paradoxwikis.com（CC BY-SA 3.0），每条目标注 oldid 与抓取日期。

"""

# ---------------------------------------------------------------------------
# 工单06：英文关键词的脚本术语补充表（标题之外的检索钩子；H2 章节名
# 已完整保留在每条的章节列表里，此处只补章节名覆盖不到的脚本词汇）。
# ---------------------------------------------------------------------------
EXTRA_KEYWORDS: dict[str, list[str]] = {
    "Scripting": ["trigger_if", "switch", "iterator"],
    "Effects": ["if", "else_if", "every", "random", "ordered"],
    "Scopes": ["root", "this", "prev", "save_scope_as", "scope:"],
    "Triggers": ["limit", "AND", "OR", "NOT", "trigger_if"],
    "Variables": ["set_variable", "change_variable", "clear_variable"],
    "Modifier list": ["add_character_modifier", "icon"],
    "AI modding": ["ai_will_do", "ai_personality", "chance"],
    "Bookmarks modding": ["bookmark", "playable_character"],
    "Characters modding": ["create_character"],
    "Commands": ["command"],
    "Council modding": ["council_positions", "council_task"],
    "Culture modding": ["heritage", "pillar", "tradition", "name_list"],
    "Decisions modding": ["major_decision", "minor_decision"],
    "Dynasties modding": ["dynasty", "house", "motto"],
    "Event modding": ["on_action", "immediate", "option", "trigger_event",
                      "fire_only_once"],
    "Governments modding": ["primary_holding", "vassal_contract"],
    "History modding": ["history/titles", "holder"],
    "Holdings modding": ["primary_building"],
    "Lifestyles modding": ["lifestyle", "focus", "perk"],
    "Regiments modding": ["men_at_arms", "damage", "toughness", "counters"],
    "Religions modding": ["faith", "tenet", "holy_site", "rite"],
    "Script values": ["add", "subtract", "multiply", "divide", "value"],
    "Story cycles modding": ["create_story", "effect_group", "story_owner"],
    "Struggle modding": ["struggle", "phase"],
    "Title modding": ["landed_titles", "titular", "de_jure"],
    "Trait modding": ["trait", "icon"],
    "Interface": ["gui", "scripted_gui", "widget"],
    "Data types": ["data type", "promote", "global function"],
    "Localization": ["l_english", "localization"],
    "Customizable localization": ["customizable_localization", "text",
                                  "fallback"],
    "Flavorization": ["priority", "special", "tier"],
    "Map modding": ["heightmap", "province", "rivers"],
    "Terrain modding": ["terrain"],
    "3D models": ["mesh", "asset"],
    "Exporters": ["PdxExporter", "Maya", "Photoshop"],
    "Coat of arms modding": ["coat_of_arms", "emblem", "pattern"],
    "Graphical assets": ["hair_palette", "skin_palette", "eye_palette"],
    "Console commands": ["debug_mode", "cheats", "tag"],
    "Patches": ["checksum", "rollback"],
    "Mod structure": [".mod"],
    "Mod compatibility": ["override", "footprint"],
    "Modding tools": ["ck3-tiger", "validator"],
    "Mod troubleshooting": ["error.log", "debug", "run"],
    "Artifact modding": ["artifact", "template", "can_equip"],
    "Defines": ["NGame", "END_DATE"],
    "Effects list": ["effect", "scopes"],
    "Interactions modding": ["character_interactions", "on_accept",
                             "auto_accept"],
    "Lists": ["every", "any", "random", "add_to_list", "in_list",
              "add_to_variable_list"],
    "Scopes list": ["event_target", "event_scope"],
    "Triggers list": ["trigger", "scopes"],
    "Weight modifier": ["base", "add", "factor", "MTTH"],
    "Modding": ["load order", "override", "workshop"],
}
KEYWORD_TARGET = 6   # 关键词行目标条数（不足时用 H2 补足）
KEYWORD_MAX = 12     # 契约上限

# ---------------------------------------------------------------------------
# 工单06：头部快照块（机械字段，每次全量重跑幂等替换；头部的其余内容永不动）
# ---------------------------------------------------------------------------
SNAP_BEGIN = "<!-- ck3wiki-mod-kb:snapshot BEGIN -->"
SNAP_END = "<!-- ck3wiki-mod-kb:snapshot END -->"
ANCHOR_TITLES = ["Effects", "Triggers", "Event modding"]  # 快照锚点 oldid


def build_snapshot(data: dict) -> str:
    """头部下方的快照行：抓取日期 / wiki 页数 / 游戏版本 / dump 并入日期 /
    核心页 oldid 锚点。全部从 manifest 派生，重跑即刷新。"""
    pages = data["pages"]
    dates = [p.get("fetched_at") or "" for p in pages.values()]
    snap_date = (max(dates) if dates else "")[:10]
    gd = data.get("game_docs") or {}
    ver = gd.get("game_version") or "未知"
    merged = (gd.get("merged_at_latest") or "")[:10] or "未并入"
    anchors = "，".join(f"{t}={pages[t].get('oldid')}"
                       for t in ANCHOR_TITLES if t in pages)
    line = (f"> 快照：抓取 {snap_date} · wiki {len(pages)} 页 · "
            f"游戏 {ver}（dump 并入 {merged}）"
            + (f" · 锚点 oldid：{anchors}" if anchors else ""))
    return f"{SNAP_BEGIN}\n{line}\n{SNAP_END}"


def upsert_snapshot(text: str, snap: str) -> str:
    """幂等插入/替换快照块。已存在 → 整块替换；不存在 → 插在第一个
    条目 BEGIN 标记之前（即文件头下方、所有条目上方）。"""
    if SNAP_BEGIN in text and SNAP_END in text:
        pattern = re.compile(re.escape(SNAP_BEGIN) + r".*?"
                             + re.escape(SNAP_END), re.DOTALL)
        return pattern.sub(lambda _: snap, text)
    m = re.search(r"<!-- ck3wiki-mod-kb:entry BEGIN ", text)
    pos = m.start() if m else len(text.rstrip("\n"))
    return (text[:pos].rstrip("\n") + "\n\n" + snap + "\n\n"
            + text[pos:].lstrip("\n"))


# ---------------------------------------------------------------------------
# 工单06：游戏权威层条目（game_docs，与 wiki 条目同构、同保护机制）
# ---------------------------------------------------------------------------
GAME_LAYER_HEADING = "## 游戏权威层（game_docs，dump > wiki）"
GAME_AUTHORITY_LINE = "- **权威层**：与 wiki 冲突时以本条目为准（dump 层）"

# 每条游戏层条目的人工字段草稿（何时查/中文摘要/英文关键词）；
# 机械字段（文件位置/来源/条目数）每次重跑从 manifest game_docs 区刷新。
GAME_LAYER_META: dict[str, dict[str, object]] = {
    "game:effects.md": {
        "display": "权威层 effects（全量 effect 签名）",
        "when": "写任何 effect 调用前，查权威签名、参数与 Supported Scopes；"
                "与 wiki（Effects/Commands/Effects list）冲突时以此为准。",
        "summary": "游戏 1.20.0 debug dump 全量 effects 清单，含用法示例与作用域。",
        "keywords": ["effects", "Supported Scopes", "usage"],
    },
    "game:triggers.md": {
        "display": "权威层 triggers（全量 trigger 签名）",
        "when": "写任何 trigger/limit 前，查权威签名与 Supported Scopes；"
                "与 wiki（Triggers/Triggers list）冲突时以此为准。",
        "summary": "全量 triggers 清单：签名、用法与支持作用域。",
        "keywords": ["triggers", "Supported Scopes", "usage"],
    },
    "game:event_targets.md": {
        "display": "权威层 event_targets",
        "when": "查某 scope 下可用的 event target 链（如 father.holder）时；"
                "比 wiki Scopes list 权威。",
        "summary": "全量 event targets：target 链与来源分组。",
        "keywords": ["event_targets", "event target"],
    },
    "game:event_scopes.md": {
        "display": "权威层 event_scopes",
        "when": "查全部 scope 类型清单或事件可用 scope 时。",
        "summary": "全部 event scope 类型权威清单。",
        "keywords": ["event_scopes", "scope"],
    },
    "game:modifiers.md": {
        "display": "权威层 modifiers",
        "when": "查某 modifier 是否存在及形态时；与 wiki Modifier list 冲突时以此为准。",
        "summary": "全量 modifier 清单与用法形态。",
        "keywords": ["modifiers", "modifier"],
    },
    "game:on_actions.md": {
        "display": "权威层 on_actions",
        "when": "要把逻辑挂到 on_action（on_xxx 钩子）或查有哪些可挂钩子时。",
        "summary": "全量 on_action 钩子清单与触发说明。",
        "keywords": ["on_actions", "on_action"],
    },
    "game:custom_localization.md": {
        "display": "权威层 custom_localization",
        "when": "查原版 customizable_localization 键名与结构时。",
        "summary": "全量 custom localization 条目转储。",
        "keywords": ["custom_localization"],
    },
    "game:data_types_common.md": {
        "display": "权威层 data_types（common）",
        "when": "查 common 域 data type 的字段/方法签名时。",
        "summary": "common 域 data types 权威转储。",
        "keywords": ["data_types", "common"],
    },
    "game:data_types_gui.md": {
        "display": "权威层 data_types（gui）",
        "when": "写 GUI 时查 gui 域 data type 的字段/方法签名。",
        "summary": "gui 域 data types 权威转储。",
        "keywords": ["data_types", "gui"],
    },
    "game:data_types_internalclausewitzgui.md": {
        "display": "权威层 data_types（internal gui）",
        "when": "查引擎内部 GUI data type（进阶 GUI modding）时。",
        "summary": "引擎内部 GUI data types 权威转储。",
        "keywords": ["data_types", "internal"],
    },
    "game:data_types_script.md": {
        "display": "权威层 data_types（script）",
        "when": "查脚本域 data type 的字段/方法签名时。",
        "summary": "脚本域 data types 权威转储。",
        "keywords": ["data_types", "script"],
    },
    "game:data_types_uncategorized.md": {
        "display": "权威层 data_types（uncategorized）",
        "when": "前四个 data_types 文件都查不到某类型时，查此未分类兜底清单。",
        "summary": "未分类 data types 权威转储（条目最多）。",
        "keywords": ["data_types", "uncategorized"],
    },
    "game:INDEX.md": {
        "display": "原版结构索引 INDEX",
        "when": "查「某类内容在原版哪些文件、多少条目」或浏览 common 子目录时。",
        "summary": "原版结构总索引：128 个 common 子目录的文件/条目计数与查询方式。",
        "keywords": ["vanilla_structure", "INDEX"],
    },
    "game:entry_map.tsv": {
        "display": "原版条目定位表 entry_map",
        "when": "查「某条目名（trait/definition/…）定义在原版哪个文件哪一行」时。",
        "summary": "78167 行 条目名→定义文件/行号 TSV；grep -P \"^<条目名>\\t\" 定位。",
        "keywords": ["entry_map", "tsv"],
    },
}


def build_game_entry(gid: str, mech: dict, meta: dict) -> str:
    """生成单条游戏层条目（机械字段来自 manifest game_docs 区）。"""
    lines = [
        f"<!-- ck3wiki-mod-kb:entry BEGIN {gid} -->",
        f"## {meta['display']}",
        "",
        f"- **文件位置**：`{mech['file']}`",
        f"- **来源**：{mech['source']}",
        GAME_AUTHORITY_LINE,
        f"- **何时查**：{meta['when']}",
        f"- **中文摘要**：{meta['summary']}",
        f"- **英文关键词**：{'；'.join(str(k) for k in meta['keywords'])}",
        f"<!-- ck3wiki-mod-kb:entry END {gid} -->",
    ]
    return "\n".join(lines)


def game_layer_mech(gd: dict) -> dict[str, dict]:
    """从 manifest game_docs 区提取每条游戏层条目的机械字段。
    返回 {条目id: {file, source}}，键序 = GAME_LAYER_META 的登记顺序。"""
    ver = gd.get("game_version") or "未知"
    sd = gd.get("script_docs") or {}
    mech: dict[str, dict] = {}
    for name, info in sd.items():
        gid = f"game:{name}"
        merged = (info.get("merged_at") or "")[:10]
        mech[gid] = {
            "file": info["output_file"],
            "source": (f"游戏 {ver} script_docs dump（`{info['source_file']}`，"
                       f"{info.get('entry_count', '?')} 条，并入 {merged}）"),
        }
    vs = gd.get("vanilla_structure") or {}
    if vs:
        scanned = (vs.get("scanned_at") or "")[:10]
        common = (vs.get("common") or {}).get("top_subdir_count", "?")
        rows = (vs.get("common") or {}).get("entry_map_rows", "?")
        base = (f"游戏 {vs.get('game_version', ver)} 目录扫描（{common} 个 common "
                f"子目录，{rows} 行条目映射，扫描 {scanned}）")
        kp = vs.get("key_products") or {}
        if kp.get("index"):
            mech["game:INDEX.md"] = {"file": kp["index"], "source": base}
        if kp.get("entry_map"):
            mech["game:entry_map.tsv"] = {"file": kp["entry_map"],
                                          "source": base}
    # 只输出 manifest 里确有产物的条目（dump 未并入时不留死条目）
    return {gid: m for gid, m in mech.items() if gid in GAME_LAYER_META}


def extract_sections(md_path: Path) -> list[tuple[str, list[str]]]:
    """从清洗产物提取章节结构：[(H2 标题, [子标题...]), ...]。

    只认 ATX 标题（## Xxx），代码围栏内的 # 行不算标题。
    """
    sections: list[tuple[str, list[str]]] = []
    current: tuple[str, list[str]] | None = None
    in_code = False
    for ln in md_path.read_text(encoding="utf-8").splitlines():
        if ln.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{2,6})\s+(.*)$", ln)
        if not m:
            continue
        level, text = len(m.group(1)), m.group(2).strip()
        if level == 2:
            current = (text, [])
            sections.append(current)
        elif current is not None:
            current[1].append(text)
    return sections


def build_entry_block(title: str, entry: dict,
                      sections: list[tuple[str, list[str]]],
                      keep_when: str, keep_summary: str) -> str:
    """生成单页条目文本（BEGIN/END 标记包裹）。

    拆分页（entry.organize.split，工单04）：文件位置指向索引 + 章节目录，
    章节列表带每个 H2 对应的章节文件路径（H3 子拆分再加子文件行）——目录
    可精确定位到章节级。sections 参数此时应传 organize.chapters 的
    [(h2, [h3...]), ...] 形态（主循环已转换）。
    """
    url = f"{config.SITE_ORIGIN}/{title.replace(' ', '_')}"
    fetched_date = (entry.get("fetched_at") or "")[:10]  # ISO 日期部分
    version = entry.get("game_version") or "未标注"
    # 关键词 = 标题 + 脚本术语补充（EXTRA_KEYWORDS）+ H2 补足到目标个数
    keywords = ([title] + list(EXTRA_KEYWORDS.get(title, []))
                + [h2 for h2, _ in sections])
    seen: set[str] = set()
    kw: list[str] = []
    for k in keywords:
        if k not in seen:
            seen.add(k)
            kw.append(k)
    kw = kw[:KEYWORD_TARGET]
    kw = kw[:KEYWORD_MAX]

    org = entry.get("organize") or {}
    if org.get("split"):
        cleaned_file = (f"`{entry.get('cleaned_file')}`（章节索引）"
                        + f"＋ 章节目录 `{org['chapter_dir']}/`")
    else:
        cleaned_file = f"`{entry.get('cleaned_file') or '（待清洗）'}`"
    lines = [
        f"<!-- ck3wiki-mod-kb:entry BEGIN {title} -->",
        f"## {title}",
        "",
        f"- **文件位置**：{cleaned_file}",
        f"- **来源**：<{url}>（oldid {entry.get('oldid')}，抓取 {fetched_date}，"
        f"页面标注版本 {version}）",
        f"- **何时查**：{keep_when}",
        f"- **中文摘要**：{keep_summary}",
        f"- **英文关键词**：{'；'.join(kw)}",
        "- **章节**：",
    ]
    if sections:
        split = org.get("split")
        for h2, subs in sections:
            if split:
                # 拆分页：subs 元素为 {"h3":…, "file":…}，章节行附章节文件路径
                main_file = next((Path(c["file"]).name for c in org["chapters"]
                                  if c["h2"] == h2), "")
                lines.append(f"  - {h2}（`{main_file}`）")
                for s in subs:
                    sub_file = f"（`{Path(s['file']).name}`）" if s.get("file") else ""
                    lines.append(f"    - {s['h3']}{sub_file}")
            else:
                sub_part = f" — {' / '.join(subs)}" if subs else ""
                lines.append(f"  - {h2}{sub_part}")
    else:
        lines.append("  - （无章节结构）")
    lines.append(f"<!-- ck3wiki-mod-kb:entry END {title} -->")
    return "\n".join(lines)


def _field_value(block: str, field: str) -> str | None:
    """从现有条目块中取出某字段值（- **字段**：值）；不存在返回 None。"""
    m = re.search(rf"^- \*\*{field}\*\*：(.*)$", block, re.MULTILINE)
    return m.group(1).strip() if m else None


def merge_entry(catalog_text: str, title: str, new_block: str,
                before_anchor: str | None = None) -> str:
    """把（可能已存在的）条目替换/追加进目录文本。

    已存在的条目：保留人工维护字段（见模块头"幂等与人工字段保护"）。
    新条目：追加到文本末尾；传 before_anchor 时插到该锚点（游戏层标题）
    之前——保证 wiki 条目永远位于游戏层区块上方。
    """
    begin = f"<!-- ck3wiki-mod-kb:entry BEGIN {title} -->"
    end = f"<!-- ck3wiki-mod-kb:entry END {title} -->"
    if begin in catalog_text and end in catalog_text:
        # 取出旧块，保留人工字段后重建
        pattern = re.compile(
            re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
        old_block = pattern.search(catalog_text).group(0)
        for field in ("何时查", "中文摘要"):
            old_val = _field_value(old_block, field)
            if old_val is not None and old_val != PLACEHOLDER:
                new_block = re.sub(
                    rf"^- \*\*{field}\*\*：.*$",
                    f"- **{field}**：{old_val}",
                    new_block, flags=re.MULTILINE)
        return pattern.sub(lambda _: new_block, catalog_text)
    # 追加（保持末尾恰好一个换行）；新 wiki 页插到游戏层标题之前
    if before_anchor and before_anchor in catalog_text:
        idx = catalog_text.index(before_anchor)
        return (catalog_text[:idx].rstrip("\n") + "\n\n" + new_block + "\n\n"
                + catalog_text[idx:])
    text = catalog_text.rstrip("\n") + "\n\n" + new_block + "\n"
    return text


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):       # Windows 控制台中文安全输出
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="阶段4：生成/合并 catalog.md")
    ap.add_argument("--page", help="只处理指定页（默认 manifest 全部页；"
                                   "单页模式不动快照与游戏层）")
    args = ap.parse_args(argv)

    data = manifest.read_manifest()
    titles = [args.page] if args.page else list(data["pages"])
    if args.page and args.page not in data["pages"]:
        print(f"[catalog] manifest 无此页：{args.page}（先跑 crawl）")
        return 1

    config.ensure_dirs()
    if config.CATALOG_PATH.is_file():
        text = config.CATALOG_PATH.read_text(encoding="utf-8")
    else:
        text = CATALOG_HEADER
        print("[catalog] catalog.md 不存在，已写入文件头")

    for title in titles:
        entry = data["pages"][title]
        cleaned = entry.get("cleaned_file")
        if not cleaned:
            print(f"[catalog] 跳过 {title}：尚未清洗")
            continue
        org = entry.get("organize") or {}
        if org.get("split"):
            # 拆分页（工单04）：章节结构来自 manifest organize 登记而非磁盘索引
            # 文件（索引只有"章节文件"一个 H2，直接解析会丢章节列表）
            sections = [(c["h2"], c["subs"]) for c in org["chapters"]]
        else:
            sections = extract_sections(config.REPO_ROOT / cleaned)
        block = build_entry_block(title, entry, sections,
                                  PLACEHOLDER, PLACEHOLDER)
        # 新页插在游戏层标题之前，保持 wiki 条目连续
        text = merge_entry(text, title, block,
                           before_anchor=GAME_LAYER_HEADING)
        note = "，已拆分" if org.get("split") else ""
        print(f"[catalog] 条目就绪：{title}"
              f"（{len(sections)} 个 H2 章节{note}，来源 oldid {entry.get('oldid')}）")

    if not args.page:
        # 头部快照块（幂等替换；文件头本体不动）
        text = upsert_snapshot(text, build_snapshot(data))
        # 游戏权威层条目（wiki 条目之后；同走 merge 的人工字段保护）
        gd = data.get("game_docs") or {}
        mech = game_layer_mech(gd)
        if mech:
            if GAME_LAYER_HEADING not in text:
                text = text.rstrip("\n") + "\n\n" + GAME_LAYER_HEADING + "\n"
            for gid, m in mech.items():
                block = build_game_entry(gid, m, GAME_LAYER_META[gid])
                text = merge_entry(text, gid, block)
                print(f"[catalog] 游戏层条目就绪：{gid}（{m['source']}）")
        else:
            print("[catalog] manifest 无 game_docs 登记或产物缺失，跳过游戏层")

    config.CATALOG_PATH.write_text(text, encoding="utf-8", newline="\n")
    print(f"[catalog] 已写 {config.CATALOG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
