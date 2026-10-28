[English](README.md) | 简体中文

[![ci](https://github.com/SlowShock-DitchesWithWater/ck3-scriptorium/actions/workflows/ci.yml/badge.svg)](https://github.com/SlowShock-DitchesWithWater/ck3-scriptorium/actions/workflows/ci.yml)

# CK3 Scriptorium —— CK3 Modding 知识库（缮写室）

本地、分层、权威、可精准定位的 CK3（十字军之王 3）modding 知识库，
服务两类读者：**写 mod 的 AI agent**（读 `AGENTS.md` 按规约检索，不凭
记忆作答）与 **modder / 知识库维护者**（人类直接翻目录查，或按本手册
重建、刷新）。三层结构（wiki 讲解、游戏导出的权威签名、原版文件索引）
互相配合，让每条答案都能带真实文件路径与版本标注，而不是幻觉脚本语法。

解决的问题：大模型对 CK3 脚本语言（Jomini）的 effect / trigger /
modifier / 字段名 / 文件结构知识不可靠，直接生成会产出"看起来像
CK3 语法"的幻觉代码。本库的做法：先读一份摘要目录（`catalog.md`），
按图索骥**只读所需文件的具体章节**，每条知识带来源路径与版本标注——
不用 RAG，不做全库塞入。

## 快速开始

### 路径一：只想用知识库（零安装、零命令）

获取文件：在 GitHub 仓库页点绿色 **Code** 按钮 → **Download ZIP**，
解压到任意目录即可（会用 git 的话 `git clone` 也行）。

**人类读者**：用任意文本编辑器打开 `catalog.md`。它是整个知识库的
目录（"目录" = 按图索骥的索引）：每个主题一个条目，告诉你该打开哪个
文件（`文件位置` 字段）、里面有哪些章节。条目摘要用中文写成，但每条
都带英文关键词与英文章节名，用编辑器查找（Ctrl+F）搜英文词就能命中。
然后打开条目指向的文件——wiki 讲解在 `pages\`，游戏权威签名在
`game_docs\script_docs\`。

**AI agent 用户**：把本仓库放到 agent 可读的位置，对它说一句：
"先读仓库根的 `AGENTS.md`，再基于本仓库回答我的问题，并给出来源
文件路径。" `AGENTS.md` 就是为 agent 写的检索规约（四步流程 +
按问题类型的查询配方）。

三个典型查询：

1. "effect `add_gold` 的准确签名是什么？"——在
   `game_docs\script_docs\effects.md` 里搜标题 `### add_gold`
   （dump 条目列出描述与支持的作用域）。
2. "trait `education_intrigue_1` 定义在原版哪个文件？"——在
   `game_docs\vanilla_structure\entry_map.tsv` 里查该名字，得到
   「条目名 → 定义文件 → 行号」（如 `common/traits/00_traits.txt`），
   再到你自己电脑的 CK3 安装目录里读原文件。
3. "成就 / on_action / mod 文件夹规则是怎样的？"——在 `catalog.md`
   里搜关键词，再读它列出的 `pages\` 下的 wiki 页。

> **游戏层不随仓库发布。** `game_docs\` 由游戏自带 debug dump 衍生，
> 分发它等于再分发游戏衍生数据（现实的 DMCA 下架风险），这是刻意的
> 合规决策。本机装有 CK3 的话，按下方**手册 A** 的游戏层步骤本地
> 生成等价物即可。

### 路径二：自己重建 / 刷新知识库（需要装 Python）

"爬取"就是把 wiki 页面下载存档，管线再清洗、编目。极简版（完整
细节见**手册 A**）：

```bat
:: 1) 从 https://www.python.org/downloads/ 安装 Python 3.10+（本项目在 3.13
::    上开发与测试），装完检查：
python --version

:: 2) 安装三个第三方库（pip 是 Python 的包安装器）：
pip install selenium requests beautifulsoup4

:: 3) 爬取 wiki（需联网 + 已装 Chrome；可断点续跑，已抓过的页自动跳过）：
<python> scripts\crawl.py --nav
<python> scripts\onehop.py --list
<python> scripts\onehop.py --crawl

:: 4) 从抓取存档离线生成全部产物（零网络）：
<python> scripts\clean.py --all
<python> scripts\organize.py
<python> scripts\catalog.py
<python> scripts\quality_gate.py
```

`<python>` 指你所用环境的 python 可执行文件——装进 PATH 就是 `python`
（Windows 下控制台输出乱码时，改用 `python -X utf8 ...` 运行）。

第 1–4 步得到 wiki 层与目录。游戏权威层、原版结构索引还需本机安装
CK3——完整重建见**手册 A**。

## 知识库结构（三层）

`catalog.md` 是唯一检索入口：两级摘要目录（页 → 章节，带"何时查"
钩子、关键词、来源与版本标注）。不要从头读到尾——先搜关键词，再只读
命中条目指向的文件与章节（agent 版规约见 `AGENTS.md`）。

| 层 | 位置 | 内容 | 权威级 |
|---|---|---|---|
| wiki 讲解层 | `pages\` | ck3.paradoxwikis.com Modding 栏目清洗文本（CC BY-SA 3.0）：机制讲解、教程、用法示例 | 低 |
| 游戏权威层 | `game_docs\script_docs\` | 游戏自带 debug dump（`script_docs` 控制台命令）：effects、triggers、modifiers、on_actions、event_targets、event_scopes、custom_localization 各一份全量机器生成清单 + data types 清单，每条目真实签名。不随仓库发布，本地生成（见手册 A） | **高** |
| 原版结构索引层 | `game_docs\vanilla_structure\` | `entry_map.tsv`：「条目名 → 定义文件 → 行号」映射 + `common` 各子目录摘要。纯导航，零游戏内容 | 导航 |

**权威顺序：游戏 dump 层（game_docs）> wiki 层（pages）**。两层冲突
以 dump 为准，回答时应指出冲突点。各层体积、来源与版本标注见
`catalog.md` 头部快照块与条目「来源」行。

## 目录结构

| 路径 | 用途 | 是否发布 |
|---|---|---|
| `catalog.md` | 唯一检索入口目录（原创） | 发布 |
| `pages\` | wiki 清洗文本（衍生自 CK3 Wiki，CC BY-SA 3.0；见 `pages\CONTENT-LICENSE.md`） | 发布 |
| `scripts\` | 管线：crawl / clean / organize / catalog / quality_gate / game_layer / vanilla_index | 发布 |
| `tests\` | 清洗规则断言、catalog 保护测试、金样本夹具 | 发布 |
| `skills\` | 自研程序性 skill：`ck3-mod-standards`——CK3 mod 脚本编码规约（作用域纪律、on_action 桥接、加载顺序兼容、本地化规范；签名强制对本知识库核对防幻觉）。安装：复制到 agent 的 skills 目录，如 `~/.agents/skills/` | 发布 |
| `docs\` | `docs\pipeline.md`（管线契约）、`docs\reports\`（清洗统计报告）；`docs\spec.md` 为内部规划文档 | 部分发布 |
| `AGENTS.md`、`AGENTS.zh-CN.md`、`README.md`、`README.zh-CN.md`、`LICENSES.md`、`LICENSE` | agent 检索规约（英/中）；双语手册；许可声明 | 发布 |
| `manifest.json` | 每页 oldid / 时间 / 版本登记（版本锚点） | 发布 |
| `raw\` | api.php 原始 JSON 存档（清洗规则改进后离线重放用） | 不发布（本地） |
| `game_docs\` | 游戏衍生内容：dump 转换产物 + 原版结构索引 | 不发布（本地生成） |
| `game logs\` | 游戏 script_docs dump 的原始 log（game_layer 的输入） | 不发布（本地） |
| `scripts\state\` | 运行时状态（导航清单、cookie、运行日志、自检脚本） | 不发布 |
| `_reference\`、`.scratch\` | 内部工作区 | 不发布 |

## 手册

### 环境要求（三条手册通用）

- Python 3.10+（本项目在 3.13 上开发与测试）。第三方依赖共 3 个：
  `selenium`、`requests`、`beautifulsoup4`，一条 pip 命令即可全部装上；
  用不用虚拟环境、怎么装都行，下文以 `<python>` 指代该环境的 python
  可执行文件。
- Chrome 浏览器：目标 wiki 有反爬盾，管线用真实浏览器会话过盾后
  才能以 requests 访问 api.php（`scripts\lib\session.py` 双通道）。
- 重建游戏权威层需要本机安装 CK3（debug 模式可执行 `script_docs`
  控制台命令）。
- 管线自带限速：对 wiki 的每个请求间隔 ≥ 15 秒（robots.txt
  Crawl-delay，硬下限不可配置），全量抓取耗时随页数增长。
- 手册中的命令在 Windows cmd 下实测；其他 shell 请自行等价替换。

### 手册 A：从零重建

```bat
:: —— 1. wiki 层（需要联网 + Chrome；已抓过的页幂等跳过，可断点续跑）——
<python> scripts\crawl.py --nav
::    抓取 Modding 导航模板的全部页面。之后补一跳种子页
::    （Effects list / Triggers list 等，勾选状态首次运行自动写入）：
<python> scripts\onehop.py --list
<python> scripts\onehop.py --crawl

:: —— 2. wiki 侧产物（零网络，从 raw 重放）——
<python> scripts\clean.py --all
<python> scripts\organize.py
<python> scripts\catalog.py
<python> scripts\quality_gate.py

:: —— 3. 游戏权威层（零网络；需要本机游戏）——
::    全新克隆只含 wiki 层；游戏权威层（dump 签名）在你机器上三步重建：
::    a) 给 CK3 加启动参数 -debug_mode（Steam 启动选项里加）后启动。
::    b) 开控制台（` 键）执行两个命令——各写一部分，缺一不可：
::         script_docs      → 7 个清单 .log
::         dump_data_types  → data_types\ 下 5 个 .txt
::       导出落在 %USERPROFILE%\Documents\Paradox Interactive\
::       Crusader Kings III\logs\（已按 CK3 1.20 实测）
::    c) 用 --source 直接指向该目录，无需拷贝（目录里的其他运行时日志
::       会被自动忽略）：
<python> scripts\game_layer.py --source "%USERPROFILE%\Documents\Paradox Interactive\Crusader Kings III\logs"
::    成功的样子：game_docs\script_docs\ 下出现 12 个 .md，manifest.json
::    多出 game_docs.script_docs 一节。
::    备选：自建仓库 game logs\ 目录（gitignored，克隆里没有），把导出
::    拷进去后免参运行本命令。

:: —— 4. 原版结构索引层（零网络；需要游戏安装目录）——
<python> scripts\vanilla_index.py --game-dir "<你的 CK3 安装目录>\game"
::    免参配置（三选一，本机长期使用推荐第 3 种）：
::    1) 每次传 --game-dir；2) 环境变量 CK3_GAME_DIR；
::    3) scripts\state\local_paths.json 写 {"game_dir": "<路径>"}（该目录已 gitignore）
::    可选：--game-version "<你的版本>"——写入 manifest/catalog 的版本标注
::    （默认 1.20.0；游戏版本更新时记得传新版本号）

:: —— 5. 游戏层并入目录 + 终检 ——
<python> scripts\catalog.py
<python> scripts\quality_gate.py
```

也可以用统一入口跑单页全流程（调试用）：`<python> scripts\run.py --page Scripting`。

### 手册 B：游戏版本更新后刷新

```bat
:: 1. 换新版本游戏重跑 script_docs，替换 game logs\ 下的全部 dump 文件
:: 2. 游戏层重并入（产物按新 dump 整体重生成，版本标注自动更新；零网络）
<python> scripts\game_layer.py
<python> scripts\vanilla_index.py --game-dir "<你的 CK3 安装目录>\game"
:: 3. wiki 侧增量刷新（需要联网：批量核对各页 revid，未变的页零请求）
<python> scripts\crawl.py --nav --refresh
::    若一跳补充页也要核对：重跑 <python> scripts\onehop.py --crawl
:: 4. 全管线重放（零网络）
<python> scripts\clean.py --all
<python> scripts\organize.py
<python> scripts\catalog.py
<python> scripts\quality_gate.py
```

### 手册 C：新会话 AI agent 使用知识库

1. 让 agent 先读仓库根 `AGENTS.md`（检索规约：四步流程 + 按问题类型的
   查询配方）。
2. 核心动作：grep `catalog.md` 关键词 → 按命中条目「文件位置/章节」
   只读所需文件。
3. 任何回答必须带来源路径（`pages\...` 或 `game_docs\...`）；
   effect/trigger/modifier 签名一律查权威层，不凭模型记忆。
4. 规约自身健康检查（可选）：
   `<python> scripts\check_doc_paths.py`（验证 AGENTS / README
   引用路径无空指）。

## 测试与自检（全部零网络）

```bat
<python> scripts\quality_gate.py          :: 全部页面产物断言
<python> tests\test_cleaner_rules.py      :: 清洗规则→断言映射（真实夹具）
<python> tests\test_catalog_protection.py :: catalog 人工字段保护/幂等
<python> tests\spotcheck_tables.py        :: 表格零丢失抽查（raw 针式）
<python> scripts\clean.py --replay-golden :: 金样本回放（Scripting+Effects 固定夹具）
<python> scripts\check_doc_paths.py       :: AGENTS / README 路径引用自检
:: 仅维护者可跑（依赖不发布的本地数据）：
<python> scripts\game_layer.py --check    :: 游戏层产物与源一致（需 game logs/）
<python> scripts\vanilla_index.py --check :: 结构索引与游戏目录一致（需游戏目录）
```

前六条在全新克隆里也能跑：依赖不发布的 `raw/` 存档（或游戏目录）的检查
会检测到其缺席并**明示跳过而非报错**——CI 跑的就是这套克隆模式组合
（`.github/workflows/ci.yml`）。

## 快照信息与时效

本 README 中所有随快照变化的数字都集中在下表（正文其他位置不出现），
刷新后只需改这一处。同样信息由管线自动再生于 `catalog.md` 头部快照块。

| 项目 | 值 |
|---|---|
| wiki 层 · 抓取日期 | 2026-10-22（导航/种子两批）+ 2026-10-23（一跳补抓；Patch 旧版本日志页按决策排除） |
| wiki 层 · 快照页数 | 141（实时页数见 `catalog.md` 头部快照块） |
| 游戏层 · dump 游戏版本 | CK3 1.20.0 |
| 游戏层 · 并入日期 | 2026-10-22 |
| 游戏层 · 条目数 | effects 2128 · triggers 1937 · modifiers 761 · on_actions 932 · event_targets 328 · event_scopes 74 · custom_localization 2782 |
| 原版结构索引 | `entry_map.tsv` 78167 行；`common` 128 个子目录摘要；2026-10-22 按 CK3 1.20.0 扫描 |
| `catalog.md` 体积 | 约 131KB |

时效：超出上述日期的内容（新游戏补丁、抓取日期之后的 wiki 修改）不在
本库中。判断某条结论是否过期：看条目「来源」行的 oldid / 抓取日期 /
页面标注版本（agent 按 `AGENTS.md` 配方 D 核对）。追平方法：游戏更新
走**手册 B**，wiki 更新走**手册 A** 的抓取步骤。

## 许可

双层许可，按目录边界适用，完整声明见 `LICENSES.md`：

- **代码与原创文档**：`scripts\`、`tests\`、`catalog.md`、
  `manifest.json`、`docs\`（pipeline.md、reports）与根文档
  （`README.md`、`README.zh-CN.md`、`AGENTS.md`、`LICENSES.md`）——
  **MIT**，见 `LICENSE`。
- **wiki 衍生内容**：`pages\`（含章节子目录）与 `tests\fixtures\`
  金样本——**CC BY-SA 3.0**，署名 CK3 Wiki
  （<https://ck3.paradoxwikis.com>）；再分发须同许可共享，详见
  `pages\CONTENT-LICENSE.md`。
- **不随仓库分发**：`game_docs\`、`raw\`、`game logs\`、
  `scripts\state\`、`_reference\`——游戏衍生数据、抓取原始存档、
  会话状态与第三方参考资料，只留在本机。
