# -*- coding: utf-8 -*-
"""HTML → 结构化 Markdown 的清洗库（阶段2核心）。

规则集（与 spec 清洗决策、docs/pipeline.md 契约一致）：
保留：标题层级、正文段落、表格（转管道表；rowspan 展开跨行值逐行重复、
      colspan 补空列、单元格内嵌套表压缩为内联文本）、代码块逐字、
      版本横幅（eu4box/mbox 类信息框）、信息框（infobox 表）。
剥离：站点导航/侧栏/页脚、[编辑|编辑源代码]按钮（span.mw-editsection）、
      每页底部 Modding 导航框、分类标签（catlinks）、脚注编号（sup.reference）
      与脚注列表（div.reflist / ol.references，工单03 决策：引用 apparatus
      属站点噪声，链接已只留文字，保留引用文只会留下无 URL 的残句）、
      全部图片（img/figure/picture/audio/video）、站内目录框（div#toc，
      与标题结构重复，章节列表由 catalog 提供）。
链接只留文字，丢弃目标。

对外主接口：clean_html(title, html) -> (markdown, stats_dict)
"""
import re
from dataclasses import dataclass, field

from bs4 import BeautifulSoup, NavigableString, Tag

# ---- 剥离选择器（CSS select 语法）----
_PRUNE_SELECTORS = [
    "span.mw-editsection",       # [编辑|编辑源代码] 按钮（含 bracket/divider 子元素）
    "div#toc",                   # 站内目录框（与标题结构重复）
    "sup.reference",             # 脚注编号（正文中的上标标记）
    "div.reflist, ol.references, div.references",  # 脚注列表（工单03：引用 apparatus 属站点噪声）
    "div.catlinks",              # 分类标签
    "div.printfooter",           # 打印页脚
    "div.sitenotice",            # 站点公告
    "div.mw-jump-link",          # 跳转链接
    "img, figure, picture, audio, video",  # 全部图片/媒体
    "style, script, input, label, button", # 页面功能元素
    "table.navbox, div.navbox",  # 通用 navbox 类（本站 Modding 框不靠 class，见下）
]


def _prune(soup: BeautifulSoup) -> None:
    """按选择器剥离噪声元素。

    注意：find_all/select 返回静态列表，先分解外层元素后，列表里残留的
    内层元素会处于 decomposed 状态（attrs 为 None），必须跳过。
    """
    for sel in _PRUNE_SELECTORS:
        for el in soup.select(sel):
            el.decompose()
    # 本站底部 Modding 导航框：无 class 特征，识别特征为
    # div[style*="border-collapse"] 且首个链接指向 /Modding（已核查的页面结构）
    for div in soup.find_all("div"):
        if div.decomposed:
            continue
        style = div.get("style") or ""
        if "border-collapse" not in style:
            continue
        first_a = div.find("a")
        if first_a is not None and (first_a.get("href") == "/Modding"
                                    or first_a.get("title") == "Modding"):
            div.decompose()
    # 空 clear 框（导航框前的排版占位）
    for div in soup.find_all("div"):
        if div.decomposed:
            continue
        style = div.get("style") or ""
        if style.strip().startswith("clear:") and not div.get_text(strip=True):
            div.decompose()


# ---------------------------------------------------------------- 统计

@dataclass
class Stats:
    """单页清洗统计（spec 用户故事16：质量报告数据）。"""
    html_bytes: int = 0
    md_bytes: int = 0
    h1: int = 0
    h2: int = 0
    h3: int = 0
    tables: int = 0
    code_blocks: int = 0
    pruned_editsections: int = 0   # 剥离的[编辑]按钮数（噪声剥离证据）
    pruned_navboxes: int = 0       # 剥离的 Modding 导航框数
    def as_dict(self) -> dict:
        return {k: getattr(self, k) for k in self.__dict__}


# ---------------------------------------------------------------- 内联渲染

_INLINE_DOUBLE_WRAP = {"b", "strong"}      # 加粗
_INLINE_ITALIC = {"i", "em"}               # 斜体
_INLINE_CODE = {"code", "tt", "kbd", "samp"}  # 行内代码
# 行内原样透传的标签（不影响 Markdown 形态）
_INLINE_PASS = {"span", "small", "sub", "sup", "u", "s", "abbr", "time",
                "font", "big", "cite", "q", "mark"}


def _inline(node, escape_pipes: bool = False) -> str:
    """把行内 HTML 渲染为 Markdown 文本。

    链接只保留文字（spec 决策）；escape_pipes 用于表格单元格，
    把裸 | 转义为 \\| 以免破坏管道表。
    """
    if isinstance(node, NavigableString):
        text = str(node)
        # HTML 空白折叠为单个空格（渲染语义），不转义任何字符
        text = re.sub(r"\s+", " ", text)
        if escape_pipes:
            text = text.replace("|", "\\|")
        return text
    if not isinstance(node, Tag):
        return ""
    name = node.name.lower()
    if name == "br":
        return "\n"
    if name == "table":
        # 行内语境中遇到的嵌套表（表格单元格内）：压缩为单行内联文本。
        # Markdown 管道表单元格放不下块级子表，见 _inline_table 的取舍说明。
        return _inline_table(node)
    if name == "a":
        # 链接只留文字：递归取子内容（含嵌套 span 等），丢弃目标
        return "".join(_inline(c, escape_pipes) for c in node.children)
    inner = "".join(_inline(c, escape_pipes) for c in node.children)
    if name in _INLINE_DOUBLE_WRAP:
        t = inner.strip()
        return f"**{t}**" if t else ""
    if name in _INLINE_ITALIC:
        t = inner.strip()
        return f"*{t}*" if t else ""
    if name in _INLINE_CODE:
        t = inner.strip()
        return f"`{t}`" if t else ""
    if name in _INLINE_PASS:
        return inner
    return inner  # 其余行内标签一律透传子内容


def _clean_heading_text(tag: Tag) -> str:
    """标题文本：折叠空白（mw-headline span 等一并取文字）。"""
    return re.sub(r"\s+", " ", _inline(tag)).strip()


# ---------------------------------------------------------------- 块渲染

def _render_list(node: Tag, ordered: bool, depth: int, stats: Stats) -> list[str]:
    """渲染 ul/ol 为 Markdown 列表（支持嵌套）。"""
    lines: list[str] = []
    idx = 0
    for li in node.find_all("li", recursive=False):
        idx += 1
        marker = f"{idx}." if ordered else "-"
        indent = "  " * depth
        # li 的直接行内内容 vs 嵌套子列表
        sub_lists: list[Tag] = []
        inline_parts: list[str] = []
        for child in li.children:
            if isinstance(child, Tag) and child.name in ("ul", "ol"):
                sub_lists.append(child)
            elif isinstance(child, Tag) and child.name in ("p", "div"):
                # li 内的段落按行内处理（MediaWiki 常见形态）
                inline_parts.append(_inline(child))
            else:
                inline_parts.append(_inline(child))
        text = re.sub(r"\s+", " ", "".join(inline_parts)).strip()
        lines.append(f"{indent}{marker} {text}" if text else f"{indent}{marker}")
        for sl in sub_lists:
            lines.extend(_render_list(sl, sl.name == "ol", depth + 1, stats))
    return lines


def _direct_rows(node: Tag) -> list[Tag]:
    """table 的直属 tr 行（可跨 thead/tbody/tfoot 容器），不进入嵌套表。

    旧实现用 find_all("tr") 递归抓行：嵌套表的行会被并进父表，列结构
    错位（行数虚增、嵌套表列按父表列对齐产生串行）。现按文档结构逐层
    取行；嵌套表本身交由 _inline_table 内联处理。
    """
    rows: list[Tag] = []
    for child in node.children:
        if not isinstance(child, Tag):
            continue
        if child.name == "tr":
            rows.append(child)
        elif child.name in ("thead", "tbody", "tfoot"):
            rows.extend(child.find_all("tr", recursive=False))
    return rows


def _span_int(cell: Tag, attr: str) -> int:
    """读取 colspan/rowspan 属性；非法值（空/非数字/0/负数）一律按 1。"""
    try:
        return max(1, int(cell.get(attr, 1) or 1))
    except (TypeError, ValueError):
        return 1


def _inline_table(node: Tag) -> str:
    """嵌套表 → 紧凑单行文本（工单03 决策：内容逐字保留，仅压缩排版）。

    形态：行与行以「；」分隔；恰好两列的表渲染为「键: 值」（覆盖最常见的
    Parameter/参数型子表），其他列数用「 / 」连接各单元格。
    嵌套中的再嵌套由 _inline 的 table 拦截递归处理。
    """
    row_texts: list[str] = []
    for tr in _direct_rows(node):
        cells = [re.sub(r"\s+", " ", _inline(c, escape_pipes=True)).strip()
                 for c in tr.find_all(["th", "td"], recursive=False)]
        if not any(cells):
            continue
        if len(cells) == 2:
            row_texts.append(f"{cells[0]}: {cells[1]}")
        else:
            row_texts.append(" / ".join(cells))
    return "；".join(row_texts)


def _render_table(node: Tag, stats: Stats) -> list[str]:
    """渲染 table 为 Markdown 管道表（工单03 精化后的规则）。

    - 行取自直属结构（table/thead/tbody/tfoot 下的 tr），不递归进嵌套表；
    - colspan>1：内容放首列，其余列补空单元格保持列对齐；
    - rowspan>1：跨行的值在每一被跨行内重复——Markdown 管道表没有
      rowspan 语义，逐行重复才能保证「每行自包含」，按行检索/阅读时不丢
      分组归属（全库 29 个 rowspan 单元格集中在 7 页，如 Localization
      的分组标签列）；
    - 单元格内嵌套表压缩为内联文本（_inline_table，全库 23 张嵌套表）；
    - 无表头行的表以首行充当表头（管道表语法要求表头）。
    """
    stats.tables += 1
    lines: list[str] = []
    caption = node.find("caption", recursive=False)
    if caption:
        lines.append(f"**{re.sub(r'\s+', ' ', _inline(caption)).strip()}**")
        lines.append("")

    # 先收集每行单元格 (文本, colspan, rowspan)，再按网格坐标展开
    rows_spec: list[list[tuple[str, int, int]]] = []
    for tr in _direct_rows(node):
        cells: list[tuple[str, int, int]] = []
        for cell in tr.find_all(["th", "td"], recursive=False):
            text = re.sub(r"\s+", " ", _inline(cell, escape_pipes=True)).strip()
            cells.append((text, _span_int(cell, "colspan"), _span_int(cell, "rowspan")))
        if cells:  # 整行无单元格的 tr（排版空行）跳过
            rows_spec.append(cells)
    if not rows_spec:
        return lines

    grid: dict[tuple[int, int], str] = {}
    for r, cells in enumerate(rows_spec):
        c = 0
        for text, colspan, rowspan in cells:
            while (r, c) in grid:  # 该位置已被上方 rowspan 占据，右移找空位
                c += 1
            for dc in range(colspan):
                grid[(r, c + dc)] = text if dc == 0 else ""
            for dr in range(1, rowspan):
                for dc in range(colspan):
                    grid[(r + dr, c + dc)] = text if dc == 0 else ""
            c += colspan
    n_rows = max(r for r, _ in grid) + 1
    max_cols = max(c for _, c in grid) + 1
    table_rows = [[grid.get((r, c), "") for c in range(max_cols)]
                  for r in range(n_rows)]

    header, body = table_rows[0], table_rows[1:]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "|".join([" --- "] * max_cols) + "|")
    for r in body:
        lines.append("| " + " | ".join(r) + " |")
    return lines


def _fence_for(code: str) -> str:
    """代码块围栏：内容含 ``` 时加长围栏，保证逐字保真。"""
    n = 3
    while "`" * n in code:
        n += 1
    return "`" * n


def _render_pre(node: Tag, stats: Stats) -> list[str]:
    """pre → 围栏代码块，内容逐字（mw-highlight 的着色 span 只取文字）。"""
    stats.code_blocks += 1
    code = node.get_text()
    if code.endswith("\n"):
        code = code[:-1]  # 去掉尾部换行，围栏自身占行
    fence = _fence_for(code)
    # mw-highlight 会标注语言类 mw-highlight-lang-c；有语言就带上
    lang = ""
    for cls in node.get("class", []) or []:
        m = re.match(r"mw-highlight-lang-(\w+)", cls)
        if m and m.group(1) != "text":
            lang = m.group(1)
            break
    return [f"{fence}{lang}", code, fence]


def _is_mbox(node: Tag) -> bool:
    """识别信息横幅类容器（版本横幅/提示框）：eu4box 是本站模板类名。"""
    classes = set(node.get("class", []) or [])
    if "eu4box" in classes or "metadata" in classes:
        return True
    return any(c.endswith("mbox") for c in classes)  # ambox/ombox/tmbox 等


def _looks_like_list_line(line: str) -> bool:
    """行首是否是 Markdown 列表标记（- 或 数字.）。"""
    s = line.lstrip()
    return s.startswith("- ") or bool(re.match(r"^\d+\. ", s))


def _render_blocks(node: Tag, stats: Stats) -> list[str]:
    """把容器（mw-parser-output/div 等）的子节点渲染为 Markdown 行列表。

    每个"块级子元素"产出一组行（chunk），chunk 之间以空行分隔——
    否则相邻 <p> 的行会被 Markdown 渲染器合并成同一段落，丢掉分段。
    例外：相邻 chunk 都是列表行（源 HTML 常把每项写成独立 <ul>），
    中间不插空行，保持紧凑列表形态。
    """
    chunks: list[list[str]] = []
    for child in node.children:
        chunk = _render_block_child(child, stats)
        if chunk:
            chunks.append(chunk)
    lines: list[str] = []
    for chunk in chunks:
        if lines:
            adjacent_lists = (_looks_like_list_line(lines[-1])
                              and _looks_like_list_line(chunk[0]))
            if not adjacent_lists:
                lines.append("")  # 块间空行，保证 Markdown 分段
        lines.extend(chunk)
    return lines


def _render_block_child(child, stats: Stats) -> list[str]:
    """渲染单个块级子元素为一组 Markdown 行（空输出返回空列表）。"""
    if isinstance(child, NavigableString):
        text = re.sub(r"\s+", " ", str(child)).strip()
        return [text] if text else []
    if not isinstance(child, Tag):
        return []
    lines: list[str] = []
    name = child.name.lower()
    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(name[1])
        text = _clean_heading_text(child)
        if text:
            if level == 1:
                stats.h1 += 1
            elif level == 2:
                stats.h2 += 1
            elif level == 3:
                stats.h3 += 1
            lines.append("#" * level + " " + text)
    elif name == "p":
        text = _inline(child).strip()
        if text:
            # 段内 <br /> 转行；行尾空格无意义
            lines = [ln.rstrip() for ln in text.split("\n")]
    elif name in ("ul", "ol"):
        lines.extend(_render_list(child, name == "ol", 0, stats))
    elif name == "dl":
        for d in child.children:
            if isinstance(d, Tag) and d.name == "dt":
                t = re.sub(r"\s+", " ", _inline(d)).strip()
                lines.append(f"**{t}**" if t else "")
            elif isinstance(d, Tag) and d.name == "dd":
                t = re.sub(r"\s+", " ", _inline(d)).strip()
                lines.append(f"  - {t}" if t else "")
    elif name == "pre":
        lines.extend(_render_pre(child, stats))
    elif name == "table":
        lines.extend(_render_table(child, stats))
    elif name == "hr":
        lines.append("---")
    elif name == "blockquote":
        inner = _render_blocks(child, stats)
        lines.extend("> " + l if l else ">" for l in inner)
    elif name == "div":
        if _is_mbox(child):
            # 版本横幅/信息框 → 引用块形态保留（防幻觉关键信息）
            inner = _render_blocks(child, stats)
            lines.extend("> [!] " + l if l else ">" for l in inner)
        else:
            lines.extend(_render_blocks(child, stats))
    elif name in ("center", "section", "span"):
        text = _inline(child).strip()
        if text:
            lines.append(text)
    else:
        # 未知块级标签：递归子内容，宁多勿丢
        lines.extend(_render_blocks(child, stats))
    return lines


def _finalize(lines: list[str]) -> str:
    """行列表 → 最终 Markdown：去代码块外的行尾空白、折叠多余空行。

    围栏识别：以 3+ 反引号开头的行视为围栏行，开合交替切换 in_code；
    代码块内部的行（含行尾空白）逐字保留。
    """
    out: list[str] = []
    in_code = False
    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code
            out.append(ln.rstrip())
            continue
        out.append(ln if in_code else ln.rstrip())
    text = "\n".join(out)
    # 折叠 3+ 连续空行为 1 个空行（两行间最多一个空白行）
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip("\n") + "\n"


def clean_html(title: str, html: str, provenance: str | None = None) -> tuple[str, Stats]:
    """清洗入口：渲染 HTML → (markdown, 统计)。

    title：页面规范标题，用于首行 H1（parse 输出不含页面标题）。
    provenance：可选来源注释（HTML 注释形态置于文件头，不影响阅读）。
    """
    stats = Stats(html_bytes=len(html.encode("utf-8")))
    stats.pruned_editsections = soup_select_count(html, "span.mw-editsection")
    soup = BeautifulSoup(html, "html.parser")
    root = soup.find("div", class_="mw-parser-output") or soup
    stats.pruned_navboxes = _count_navboxes(root)
    _prune(soup)

    lines: list[str] = []
    if provenance:
        lines.append(f"<!-- {provenance} -->")
        lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    lines.extend(_render_blocks(root, stats))

    md = _finalize(lines)
    stats.md_bytes = len(md.encode("utf-8"))
    return md, stats


def soup_select_count(html: str, selector: str) -> int:
    """统计选择器命中数（用于剥离前的噪声计数）。"""
    return len(BeautifulSoup(html, "html.parser").select(selector))


def _count_navboxes(root: Tag) -> int:
    """统计底部 Modding 导航框数量（剥离前计数，作为噪声剥离证据）。"""
    n = 0
    for div in root.find_all("div"):
        if div.decomposed:
            continue
        style = div.get("style") or ""
        if "border-collapse" in style:
            first_a = div.find("a")
            if first_a is not None and (first_a.get("href") == "/Modding"
                                        or first_a.get("title") == "Modding"):
                n += 1
    return n
