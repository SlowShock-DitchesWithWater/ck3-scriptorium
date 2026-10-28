# 管线契约（pipeline.md）

> 本文档是四阶段管线的技术契约，供后续工单 agent 对齐。内容与 `scripts/` 下
> 的实现一一对应；改代码必须同步改本文档。状态基线：工单 01（单页走通骨架）。

## 0. 单命令入口

```bash
# Python ≥3.10（项目在 3.13 开发测试）；第三方依赖共 3 个，全部安装：
#   selenium + requests + beautifulsoup4（pip 一次装齐）
#   Windows 示例：<你的 venv>\Scripts\python.exe 或 python -X utf8
python scripts\run.py --page Scripting
```

- `--page <标题>`：页面标题（MediaWiki 规范标题），默认 `Scripting`。
- `--stage all|crawl|clean|organize|catalog|gate`：跑全流程或单阶段，默认 all。
- `--force`：传给 crawl，忽略已抓记录强制重抓。
- 各阶段脚本也可直接执行：`scripts/crawl.py --page X` 等。

阶段顺序与依赖（后一阶段只依赖前一阶段的**磁盘产物**，不依赖其内存状态）：

```
crawl(阶段1) ──raw/<页>.json──▶ clean(阶段2) ──pages/<页>.md──▶ organize(阶段3,暂no-op)
     │                                                     │
     └──────────────manifest.json（登记/补记，贯穿）─────────┴──▶ catalog(阶段4) ──catalog.md
                                                                              │
                                                              quality_gate（断言）◀┘
```

## 1. 阶段边界

| 阶段 | 脚本 | 输入 | 输出 | 网络 | 幂等语义 |
|---|---|---|---|---|---|
| 1 抓取 | `scripts/crawl.py` | 页面标题 | `raw/<页名>.json` + manifest 登记 | 是（限速） | 单页：已抓页（manifest 有记录且 raw 在盘）直接跳过，零请求；`--force` 才重抓。批量 `--nav`：先离线确认（manifest+raw 完好+重定向映射），全部完成时整轮零请求；`--nav --refresh` 批量核对 revid（≤50 标题/请求），oldid 未变跳过，变化/损坏/缺失重抓 |
| 2 清洗 | `scripts/clean.py` | raw JSON | `pages/<页名>.md` + manifest 补记 | 否 | 纯函数重放：产物逐字节相同；manifest 按内容 sha256 判变，未变则登记字段原样保留 |
| 3 组织 | `scripts/organize.py` | raw 重放全文（纯函数） | 巨页章节拆分：>50KB 按 H2 拆 + 章节索引；单节 >150KB 且 ≥2 个 H3 再按 H3 拆；pages/ 目录与 manifest organize 登记 | 否 | 从 raw 重放重建，整目录重写（陈旧章节清理）；manifest 登记仅变化时刷新；重组校验（重组==原文）失败则拒绝写盘 |
| 4 建目录 | `scripts/catalog.py` | manifest + pages/ | `catalog.md` | 否 | 条目块整体重生成（派生字段），人工字段保留（见 §5） |
| 质量门 | `scripts/quality_gate.py` | 全部产物 | 控制台断言结果，退出码 0/1 | 否 | 只读 |

## 2. 目录与产物组织

```
ck3-scriptorium/             ← 仓库根（spec 中的存储组织；本地目录名可不同）
  raw/                       ← 阶段1：api.php 原始 JSON 存档（重放清洗用，发布时 gitignore）
  pages/                     ← 阶段2：清洗后结构化 Markdown（发布产物，CC BY-SA 3.0）
  game_docs/                 ← 工单07/08：script_docs dump 与原版结构索引（不发布）
  manifest.json              ← 每页版本登记（见 §3）
  catalog.md                 ← 唯一检索入口目录（见 §5）
  scripts/
    run.py                   ← 统一入口
    crawl.py / clean.py / organize.py / catalog.py / quality_gate.py
    lib/
      config.py              ← 全部路径常量与 MIN_CRAWL_DELAY_SECONDS（唯一事实来源）
      session.py             ← 过盾 + cookie 导出 + 双通道 api.php 访问 + 限速
      manifest.py            ← manifest 原子读改写（锁 + 临时文件 + os.replace）
      cleaner.py             ← HTML→Markdown 清洗库（阶段2核心，可被测试直接调用）
    state/                   ← 运行时状态，不属于产物（cookies.json、
                               last_request.txt、nav_pages.json 导航清单、
                               nav_redirects.json 重定向映射、batch_run*.log
                               运行日志与一次性探查残留）
```

**命名约定**（`lib/config.py: safe_filename`）：页面标题 → 文件名。子页面
分隔符 `/` 替换为 `__`；Windows 非法字符 `:*?"<>|` 替换为 `_`；其余保留。
raw 与 pages 用同一函数，同名一一对应。例：`Scripting` →
`raw/Scripting.json` + `pages/Scripting.md`。

## 3. manifest.json schema

顶层：`{"schema_version": 1, "pages": { "<规范标题>": {…} }}`。
`pages` 的键是重定向解析后的规范标题（`action=query&redirects=1` 返回值）。

单页 entry 字段（crawl 写前 8 个，clean 补后 5 个）：

| 字段 | 写入者 | 含义 |
|---|---|---|
| `title` | crawl | 规范标题 |
| `oldid` | crawl | 抓取时的 last revid（版本固定锚点） |
| `fetched_at` | crawl | 抓取时刻（本地时区 ISO8601） |
| `game_version` | crawl | 页面横幅标注的游戏版本：数字（如 `1.16`）、`"timeless"`（版本无关横幅）或 `null`（未标注） |
| `size_bytes` | crawl | wikitext 源码大小（API 报告值，粗略量级参考） |
| `raw_file` | crawl | raw 存档相对路径 |
| `raw_bytes` | crawl | raw 存档字节数 |
| `cleaned_file` | clean | 清洗产物相对路径 |
| `cleaned_at` | clean | 本次内容变化的清洗时刻（内容未变的重放不刷新） |
| `cleaned_bytes` | clean | 清洗产物字节数 |
| `cleaned_sha256` | clean | 清洗产物内容哈希（幂等判据） |
| `clean_stats` | clean | 清洗统计：html_bytes/md_bytes/h1/h2/h3/tables/code_blocks/pruned_editsections/pruned_navboxes |

**并发安全**（`lib/manifest.py`）：多个 agent 并行抓取时，所有 manifest
写必须经 `manifest.update_page(title, mutate)`（读改写单页条目）或
`with manifest_locked():` 手动持锁批量写。实现：`manifest.json.lock`
（`O_CREAT|O_EXCL` 原子创建 + 30s 重试 + 120s 过期抢占）+ 同目录临时文件
`os.replace` 原子落盘（Windows 上被杀软/同步软件瞬时占用时指数退避重试）。
**任何阶段都不得绕过该模块直接写 manifest.json。**

### 3.1 game_docs 区（工单07/08 写入，工单10 补契约）

顶层还有 `game_docs` 键（与 `pages` 并列）：

- `game_docs.game_version` / `game_version_source`：游戏版本标注（优先从
  `game logs\code_revisions.log` 提取；为空时用基准事实 1.20.0 并注明来源）。
- `game_docs.script_docs["<产物名>"]`：12 个权威清单产物各一条——
  `source_file`（game logs 来源）、`entry_count`、`merged_at`（仅内容变化时
  刷新，保证幂等）、`source_mtime`（dump 会话时间近似）、`output_sha256`。
- `game_docs.vanilla_structure`：`scanned_at`、`game_dir`（**只记标签
  `"(local game install)/game"`，不登记本机绝对路径**——manifest 会发布；
  实际路径由 `--game-dir` 参数 / 环境变量 `CK3_GAME_DIR` /
  `scripts\state\local_paths.json`（gitignored）三者之一提供，见
  `vanilla_index.py` 的 `resolve_game_dir`）、`subdirs`/`products` 指纹。

## 4. 阶段1：抓取（crawl）契约

- 取 oldid：`action=query&prop=revisions&rvprop=ids|timestamp|size&rvlimit=1&redirects=1`
  （跟随重定向拿规范标题）。
- 取正文：`action=parse&oldid=<revid>&prop=text&format=json&formatversion=2&disablelimitreport=1`。
  **必须用 parse（模板展开后的渲染 HTML），禁止 action=raw**——部分页面正文
  在引用模板内，raw 会丢内容。raw/ 存档即该参数组合的**原始响应体逐字内容**；
  重放清洗时不得改变这些参数。
- 版本标注提取（`crawl.extract_game_version`）：优先匹配横幅
  "This article is timeless …"（记 `"timeless"`），否则匹配第一个
  `version x.y[.z]`。

### 批量模式（`--nav` / `--nav --refresh`，工单02）

- 清单来源：`scripts/state/nav_pages.json`，由 `scripts/nav_pages.py` 从
  已抓页 raw 存档的底部 Modding 导航框**离线确定性推导**（可重放校验）。
  红链（class=new / href 含 redlink=1 / action=edit，三选一）不入清单。
  Effects 置顶（工单03 金样本）。导航链接经重定向解析后按规范标题去重。
- **普通模式（断点续跑）**：先纯离线确认——manifest 有记录 + raw 完好
  （`raw_intact`：可解析且含 parse.text）+ 已知重定向映射即判完成；
  **全部确认时整轮零网络请求**（`state/last_request.txt` 时间戳不变即为
  证明）。仅离线无法确认的页才发批量 query。重定向映射（导航标题→规范
  标题，如 Checksum→Patches）由批量 query 学到并持久化于
  `scripts/state/nav_redirects.json`，供下轮离线确认复用。
- **refresh 模式（游戏新版本后重跑）**：action=query 多标题批量查当前
  revid（一次最多 50 标题；多标题模式禁止传 rvlimit）。oldid 未变且 raw
  完好 → 跳过（零 parse 请求）；oldid 变化 / raw 缺失或损坏 / 新页 →
  重抓覆盖（即改坏修复语义：oldid 比对发现不了截断损坏，靠 raw_intact）。
- 请求预算：每轮 1 次批量 query（≤50 标题）+ 每待抓页 1 次 parse。

### 会话与限速（`lib/session.py`）

- 站点有 Fastly Client Challenge 反爬盾。实测（2026-10-22）：盾放行不依赖
  cookie——CDP 全量导出（含 httpOnly）后 requests 仍被拦，差异在 TLS/HTTP2
  指纹。因此 api 访问为**双通道**：
  1. **requests + cookie**（首选）：过盾浏览器导出的 cookie 存
     `scripts/state/cookies.json`；被盾拦截时自动切换；
  2. **过盾浏览器内 fetch**（回退）：常驻 Chrome（有头，盾检测 headless），
     同源 fetch api.php 取原始响应体。
- 盾检测特征串：`looks_like_challenge()`（`client challenge`、`_fs-ch` 等）；
  响应命中即视为被拦。
- **Crawl-delay：`MIN_CRAWL_DELAY_SECONDS = 15.0`（`lib/config.py`），
  robots.txt 要求的硬下限，无任何配置入口可调小。**两条通道发出的每个
  站点请求前都调 `wait_crawl_delay()`，时间戳持久化于
  `scripts/state/last_request.txt`，跨进程生效。后续工单批量抓取必须
  继续走该函数，不得自建请求循环。

## 5. catalog.md 条目 schema（阶段4；工单06 扩展后）

每页条目包裹在标记内（幂等替换的边界）：

```
<!-- ck3wiki-mod-kb:entry BEGIN <规范标题> -->
## <规范标题>

- **文件位置**：`pages/<文件名>.md`（拆分页：`pages/<页>.md`（章节索引）＋ 章节目录 `pages/<页>/`）
- **来源**：<https://ck3.paradoxwikis.com/<页面URL>>（oldid <revid>，抓取 <YYYY-MM-DD>，页面标注版本 <版本>）
- **何时查**：（待人工补充）
- **中文摘要**：（待人工补充）
- **英文关键词**：<标题>；<EXTRA_KEYWORDS 补充词>；<H2 补足>（目标 6 个、上限 12，保留英文原名）
- **章节**：
  - <H2 标题> — <子标题 / 子标题 / …>（拆分页附章节文件名）
  - …
<!-- ck3wiki-mod-kb:entry END <规范标题> -->
```

- **人工字段保护**：`何时查`、`中文摘要` 为人工维护。重跑 catalog 时，
  派生字段（文件位置/来源/关键词/章节）按 manifest+pages 重新生成；
  人工字段若已不等于占位符 `（待人工补充）` 则**原样保留**，绝不覆盖。
  工单06 已把 56 页人工字段的**草稿**直接填入 catalog.md（用户确认后即固化，
  后续重跑靠本机制保护）。
- **英文关键词**（工单06 压缩规则）= 标题 + `catalog.EXTRA_KEYWORDS[标题]`
  （脚本术语补充表，只在 catalog.py 维护）+ H2 补足到 6 个（上限 12）。
  理由：H2 章节名已完整保留在章节列表里，关键词行只补章节名覆盖不到的
  脚本词汇检索面（如 on_action、add_to_list、MTTH）。
- **头部快照块**（工单06）：文件头下方、所有条目上方，独立标记块
  `<!-- ck3wiki-mod-kb:snapshot BEGIN/END -->`，内容为
  `> 快照：抓取 <max(fetched_at)> · wiki <N> 页 · 游戏 <版本>（dump 并入 <日期>）· 锚点 oldid：Effects/Triggers/Event modding`。
  语义：**机械字段**，每次全量重跑整块幂等替换（改 manifest 即刷新）；
  快照块之前的文件头本体（检索规约/权威顺序/许可）仍然永不动。单页模式
  （`--page`）不触碰快照块与游戏层。
- **游戏权威层条目**（工单06）：全部 wiki 条目之后，以受保护标题
  `## 游戏权威层（game_docs，dump > wiki）`（存在即不动）引导，逐条目
  同样走 BEGIN/END 标记（标记名 `game:<产物文件名>`，如 `game:effects.md`、
  `game:INDEX.md`）与同一套人工字段保护。覆盖 game_docs 区 14 个产物：
  script_docs 12 个 dump（effects/triggers/event_targets/event_scopes/
  modifiers/on_actions/custom_localization + data_types 五文件）+
  vanilla_structure 的 INDEX.md 与 entry_map.tsv。字段：
  - 机械（每次重跑从 manifest game_docs 区刷新）：文件位置、来源
    （游戏版本 + 来源 log + 条目数 + 并入日期；vanilla 为目录扫描统计）、
    `- **权威层**：与 wiki 冲突时以本条目为准（dump 层）` 标注行；
  - 人工草稿（catalog.GAME_LAYER_META 提供初值，写入后同受保护）：
    何时查、中文摘要、英文关键词。
- **条目顺序**：wiki 条目顺序 = manifest `pages` 插入顺序；新 wiki 页
  插入到游戏层标题**之前**（保证 wiki 条目连续），游戏层条目追加在末尾。
- **体积**：条目 schema 的机械部分（章节列表 + BEGIN/END 标记 + 来源行 +
  文件位置）56 页 + 游戏层合计约 40KB，为「不许砍条目/章节列表」约束下的
  硬底；工单06 验收实测全量 54.9KB（超 25KB 目标的原因即在此，人工字段
  清零也仍 43.5KB），已通过压缩关键词行（12→6 个）与精炼摘要 mitigation。
  **2026-10-23 用户决策：接受 ~55KB 体积**（检索规约按"先 grep 再读命中条目"
  使用，AGENTS.md 已按此写）；后续新增页面会使目录继续增大，属接受范围。

## 6. 阶段2：清洗规则（`lib/cleaner.py`，工单03 精化后）

保留：标题层级（h2-h6 → `##`-`######`，逐字保真，页面源码本身 h3/h4 混用
时照实保留）、正文段落（块间空行分隔）、表格→管道表（见下方表格规则）、
代码块逐字（`mw-highlight` 着色 span 只取文字；内容含 ``` 时自动加长围栏）、
版本横幅/信息框（`eu4box`/`*mbox` → `> [!]` 引用块）。

**表格规则**（全库 56 页 218 张内容表实测后定型）：
- 行取自直属结构（table/thead/tbody/tfoot 下的 tr），**不递归进嵌套表**
  （旧版递归抓行导致嵌套表行并进父表、列错位）；
- `colspan>1`：内容放首列，其余列补空单元格保持列对齐；
- `rowspan>1`：跨行的值在每一被跨行内**重复**（Markdown 管道表无 rowspan
  语义，逐行重复保证每行自包含、按行检索不丢分组归属）；
- 单元格内**嵌套表**压缩为内联文本：行间「；」，两列表「键: 值」，
  多列表「 / 」连接（内容逐字保留，仅压缩排版）；
- 无表头行的表以首行充当表头（管道表语法要求）。

剥离：`span.mw-editsection`（[编辑|编辑源代码]）、`div#toc`（站内目录框）、
`sup.reference`（脚注编号）与脚注列表（`div.reflist`/`ol.references`/
`div.references`——工单03 决策：引用 apparatus 属站点噪声，链接已只留文字，
保留引用文只会留下无 URL 的残句）、`div.catlinks`、
`img/figure/picture/audio/video`（全部图片）、`style/script/input/label`、
底部 Modding 导航框（识别特征：`div[style*="border-collapse"]` 且首个链接
指向 `/Modding`）。

链接只留文字（`<a>` unwrap）。首行恒为 `# <规范标题>`（parse 输出不含页面
标题），其上有一行 HTML 注释形态的来源标注（URL+oldid+抓取时间）。

已知取舍（已审视定案）：`dl/dt/dd` 渲染为粗体行+缩进列表（内容完整，纯排版
选择）；无表头表以首行为表头。

### 金样本回放（spec 测试决策）

- 夹具：`tests/fixtures/{Scripting,Effects}.json`（1 小页 + 1 巨页的 raw JSON
  固定副本）+ `tests/fixtures/fixtures.json`（固定 oldid/抓取时间的元数据，
  golden 逐字节稳定、不随 manifest 变化）+ `tests/fixtures/golden/*.md`
  （期望产物；未受规则影响的页与 pages/ 逐字节一致）。
- `clean.py --replay-golden`：离线重放并 unified diff 比对，不一致退出码 1；
  `--update-golden` 规则改动有据后刷新期望产物。全程零网络（测试有
  sys.modules 断言：不加载 requests/selenium/lib.session）。
- 断言矩阵与表格零丢失抽查：`tests/test_cleaner_rules.py`（32 项，
  规则→断言一一对应）、`tests/spotcheck_tables.py`（raw 表行→产物单行
  逐字命中，内置 Effects 3 行 + Culture modding 嵌套行 1 例，支持 --needle）。

## 7. 质量门断言（`scripts/quality_gate.py`）

对 manifest 全部页（或 `--page` 单页）逐项断言，任一 FAIL 退出码 1：

1. manifest 有该页记录；
2. raw JSON 存在、非空、可解析且含 `parse.text`（重放前提）；
3. 清洗 md 存在且非空；
4. 有 H1（代码围栏内的 `#` 不算）；
5. 无站点噪声特征串：`Active Wikis`、`编辑源代码`、`[edit`、`[编辑`、
   `Navigation menu`、`导航菜单`、`Print/export`、`Personal tools`、`mw-editsection`；
6. manifest 记录了版本标注的页，该标注串保留在清洗产物中（横幅保留检查）；
7. catalog 含该页条目标记。

## 8. 后续工单的衔接点

- **工单02（批量抓取）**：已完成（46 导航页 + 工单05 种子页）。crawl 循环多页，
  每请求仍走 `session.api_get_text`（自带 15s 限速与双通道）；manifest 并发写
  必须走 `manifest.update_page`。
- **工单03（清洗精化+金样本回放）**：已完成。表格规则精化 + 脚注列表剥离见
  §6；夹具与回放/断言/抽查见 §6 金样本回放节；统计对照报告
  `docs/reports/clean_stats.md`（生成器 `scripts/clean_report.py`）。
- **工单04（巨页拆分）**：已完成。`scripts/organize.py` 从 raw 重放全文后按
  H2（>50KB）/H3（单节 >150KB）拆分：章节文件 `pages/<页>/<NN>-<slug>.md`
  （自包含：来源注释 + `# 页名 — 章节名` H1 + 原文逐行保真），原页名文件重写为
  章节索引；H2<2 的巨页（Effects list/Triggers list 整页大表型）保留整页并记原因。
  manifest 页条目新增 `organize` 字段：`{split, chapter_dir, chapters:[{h2, file,
  bytes, h3_split, subs:[{h3, file}]}], reassembled_ok}`；catalog 对拆分页据此生成
  章节级"文件位置/章节"。当前拆分：Effects(6)、Event modding(13)、Interface(9)、
  Data types(4)。质量门 E 组断言索引/章节/登记一一对应。
  验证：`scripts/state/verify_split_04.py`（磁盘重组==raw 重放全文、条目单文件
  完整、幂等复跑零差异）。注意管线顺序须 clean → organize（clean 会重写全文，
  organize 再拆回；cleaned_sha256 登记的是未拆分全文）。
- **工单05（一跳候选）**、**06（目录生成器）**：消费 manifest 与 pages/，
  不改前段。
- **工单06（目录生成器）**：已完成。catalog.py 扩展（关键词补充表
  EXTRA_KEYWORDS、头部快照块、游戏层 14 条目、新 wiki 页插到游戏层标题前、
  拆分页文件位置标记修复）见 §5；56 页人工字段草稿已填入 catalog.md，
  用户确认后由 §5 保护机制固化；夹具测试 `tests/test_catalog_protection.py`
  （16 项：幂等/人工字段保护/机械字段刷新/快照语义/覆盖/单页模式）。
- **工单07/08（游戏权威层）**：`game_docs/` 并入后，在 catalog 头部与条目
  中落实"dump > wiki"冲突标注（工单06 已在游戏层条目中落实，见 §5）。
