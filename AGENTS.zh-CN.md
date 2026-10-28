# AGENTS.md — CK3 Modding 知识库·AI 检索规约

> 本文件给在本仓库内回答 CK3 modding 问题的 AI agent。你的任务：用最少的上下文
> 拿到**带来源、无幻觉**的知识。规约的每条命令与路径都在本仓库实测存在。
> （英文版：[AGENTS.md](AGENTS.md)）

## 0. 仓库是什么（30 秒版）

三层知识库 + 一个唯一摘要目录。当前快照页数与游戏版本见 `catalog.md` 头部
快照块（不要在别处记这些数字，会腐烂）。

| 层 | 位置 | 内容 | 权威级 |
|---|---|---|---|
| wiki 讲解层 | `pages/` | ck3.paradoxwikis.com Modding 栏目清洗文本 | 低 |
| 游戏权威层 | `game_docs/script_docs/` | 游戏 debug dump：effects / triggers / modifiers / on_actions / event_targets / event_scopes / custom_localization 清单 + data_types×5 文件 | **高** |
| 原版结构索引层 | `game_docs/vanilla_structure/` | 条目名→定义文件映射 + common 128 子目录摘要 | 导航 |

**权威顺序：game_docs（dump）> pages（wiki）。** 两层冲突时以 dump 为准，
并在回答中指出冲突点。

**`game_docs/` 由用户本地生成、不随仓库发布。** 它派生自游戏自身的 debug
dump，公开仓库不含此目录——全新克隆只有 wiki 层。若 `game_docs/` 缺失，
告知用户可按 `README.md` 手册 A 的游戏层步骤生成等价物；在此之前只用
wiki 层回答，并说明 dump 层不可用。

`catalog.md` 是全部条目的两级摘要目录——**唯一检索入口，但禁止整读，
先 grep 再按图索骥**（见下）。

## 1. 标准检索流程（四步）

1. **判断问题类型**，选第 2 节的配方（A 签名 / B 讲解 / C 条目定位 / D 版本敏感）。
2. **查目录**：grep `catalog.md` 关键词，命中条目后按其「文件位置」「章节」字段
   只读对应文件——不要整读 catalog，也不要整读命中页。
3. **目录未命中 → pages 兜底**：对 `pages/` 全目录做关键词 grep（命令见配方 B），
   仍然只读命中文件。catalog 不可能收录每个事实，兜底是正常路径，不算弯路。
4. **回答必须带来源**：`pages/<页名>.md` 或 `game_docs/<层>/<产物>.md` 的具体文件
   + 章节/条目名。没读到就不回答：禁止凭模型记忆写 effect/trigger/modifier/字段名。

### grep 命令怎么写（catalog.md 与 pages/*.md 均为 UTF-8）

Windows cmd 代码页默认 GBK，**findstr 只能可靠匹配 ASCII 关键词**；
中文关键词（如 成就、作用域）必须用 python 或真 grep：

```bash
# ASCII 关键词（effect/trigger 名、页面名——绝大多数查询）：
findstr /n /i /c:"trait" catalog.md        # Windows cmd
grep -n -i "trait" catalog.md              # 有 grep 的环境（git-bash / WSL / Linux / macOS）

# 中文关键词（python 单行，仓库根执行）：
python -X utf8 -c "import sys;sys.stdout.reconfigure(encoding='utf-8');[print(f'{i}: {l.rstrip()}') for i,l in enumerate(open('catalog.md',encoding='utf-8'),1) if '成就' in l]"
```

catalog 条目字段速览（wiki 条目 + 游戏层条目，条数以 catalog 头部快照为准）：
`文件位置`（去读它）· `来源`（URL + oldid + 抓取日期 + 页面标注版本）·
`何时查`/`中文摘要`（判断是否命中）· `英文关键词` · `章节`（H2 清单，按需选读）。

## 2. 查询配方（命令均实测）

### 配方 A：effect / trigger / modifier / on_action / custom_localization / data type 签名

**直达权威层，不要先查 wiki。** 清单文件每条目一节，标题行是 `### 名称`，
小节内是描述/用法示例/`Supported Scopes:`。文件（均在 `game_docs/script_docs/`）：

`effects.md` · `triggers.md` · `modifiers.md` · `on_actions.md` ·
`event_targets.md` · `event_scopes.md` · `custom_localization.md` ·
`data_types_common.md` · `data_types_gui.md` ·
`data_types_internalclausewitzgui.md` · `data_types_script.md` ·
`data_types_uncategorized.md`（前四个 data_types 查不到的类型，兜底查它）。

```bash
# 已知名字，精确命中标题行（输出行号，再只读该 ### 小节）：
grep -n "### add_gold" game_docs/script_docs/effects.md
# Windows cmd 等价：findstr /n /c:"### add_gold" game_docs/script_docs/effects.md

# 只知语义（如"给角色加金钱"）：先用语义词搜清单、再筛标题行：
grep -n -i "gold" game_docs/script_docs/effects.md | grep "### "
```

**dump 条目通常只有描述 + Supported Scopes，没有用法示例。**要示例时直接对
wiki 层全文搜该 effect/trigger 名（冷启动验收实测这是最快路径）：

```bash
grep -rn "add_gold" pages/            # 或 Windows：findstr /s /n /c:"add_gold" pages\*.md
```

wiki 大表页（`pages/Effects list.md`、`pages/Triggers list.md`、`pages/Commands.md`）
只当讲解参考；条目级答案以 dump 层为准。

### 配方 B：机制 / 做法 / 讲解（wiki 层）

```bash
# 1) 先查目录（英文关键词优先：页面名、脚本词）：
grep -n -i "achievement" catalog.md
grep -n -i "on_action" catalog.md

# 2) 中文关键词 / 目录未命中时，pages 全目录兜底（python 单行）：
python -X utf8 -c "import sys,pathlib;sys.stdout.reconfigure(encoding='utf-8');[print(f'{p}: {i}: {l.rstrip()}') for p in pathlib.Path('pages').rglob('*.md') for i,l in enumerate(p.read_text(encoding='utf-8').splitlines(),1) if 'achievement' in l.lower()]"
```

命中条目后按「文件位置」读文件。**拆分页注意**：以下页的页名文件只是
章节索引，正文在同名子目录的章节文件里（索引文件里有逐文件清单）：

- `pages/Effects.md`（索引）→ `pages/Effects/01-Effect-blocks.md` 等 6 个
- `pages/Event modding.md` → `pages/Event modding/`（13 个章节）
- `pages/Interface.md` → `pages/Interface/`（9 个章节）
- `pages/Data types.md` → `pages/Data types/`（4 个章节）
- 共 22 个拆分页；完整清单见各索引文件或 manifest 的 organize 字段

### 配方 C：某条目（trait / decision / opinion / …）定义在原版哪个文件

```bash
grep -P "^education_intrigue_1\t" game_docs/vanilla_structure/entry_map.tsv
# Windows cmd 等价：findstr /b /c:"education_intrigue_1" game_docs\vanilla_structure\entry_map.tsv
```

输出制表符分隔的三列：条目名、定义文件（相对游戏安装目录 game/ 的路径）、行号，
如 `common/traits/00_traits.txt  11`。该表只含结构信息、零原版内容；
拿到路径后请读**用户本机游戏目录**里的原文件（本仓库不含原版全文）。

- 浏览某类内容的全部文件与条目：先读 `game_docs/vanilla_structure/INDEX.md`，
  再按其表格读 `game_docs/vanilla_structure/common/<子目录>.md`（128 个全覆盖）。
- events / history / gui / gfx 等非 common 目录：`game_docs/vanilla_structure/other_dirs.md`。

### 配方 D：版本敏感事实（"从哪个版本起…"类问题）

1. 先用配方 B 找到 wiki 正文——版本号通常写在正文句子里（如 "since 1.9 patch"）。
2. 核对两层版本标注，回答时必须带上：
   - wiki：catalog 条目「来源」行（oldid / 抓取日期 / 页面标注版本）；
   - dump：`game_docs/script_docs/` 各文件头部的游戏版本来源行。
3. 页面标注 `timeless` 表示 wiki 自称版本无关；与正文表述冲突时仍以 dump 为准。

## 3. 上下文纪律（硬规则）

- **禁止整读**这些大文件（一律先 grep 定位再读所需段）：
  `catalog.md`、`pages/Effects list.md`、`pages/Triggers list.md`、
  `game_docs/script_docs/` 下全部清单、`game_docs/vanilla_structure/entry_map.tsv`。
- **代码块 / 签名逐字引用**，不改写、不"顺手规范化"字段名。
- 任何 effect / trigger / modifier / 字段名：要么来自你刚读到的文件（带路径引用），
  要么明说"未在知识库中核实"。没有第三种。
- wiki 与 dump 冲突 → 以 dump 为准，并指出冲突点。
- 版本敏感结论必须附版本标注（配方 D）。

## 4. 不是知识入口的路径（检索时别读）

| 路径 | 是什么 |
|---|---|
| `raw/` | api.php 原始 JSON 存档（清洗重放用，非知识；clone 用户没有此目录） |
| `game logs/` | script_docs dump 的原始 log（已转换为 game_docs/script_docs/，读后者；clone 用户没有此目录） |
| `scripts/state/` | 管线运行时状态与一次性探查脚本 |
| `scripts/`、`tests/` | 管线代码与测试（维护者用，见 `README.md`） |
| `manifest.json` | 管线登记表（版本溯源进阶用；日常查版本用 catalog 条目「来源」行） |
| `_reference/`、`.scratch/` | 内部工作区（clone 用户没有） |
| `docs/pipeline.md`、`docs/spec.md` | 管线契约与项目 spec（维护者用） |
| `skills/` | 本仓库附带的 ck3-mod-standards 编码规约 skill（写 mod 代码时装到 agent，不是知识） |

## 5. 时效自检

回答前如果结论可能随游戏版本变化（新 effect、数值、成就规则…），
用配方 D 的两层标注判断快照时效（快照日期见 `catalog.md` 头部快照块）。
超出快照期的新版本内容本库没有，**明说"本库快照不含此信息"即可，不要用模型记忆补**。

## 6. 用户覆盖

用户在当前对话里的明确指令优先于本文件。若与上面某条冲突，先说清冲突点，
得到确认后再执行。

## 7. 这些情况先停下来问用户

- 需要**重抓 wiki 或重跑 dump**（任何联网/跑管线操作）：先说明要跑什么、
  预计多久（全量重抓约 30-40 分钟限速），得到同意再动。
- 发现 wiki 层与 dump 层冲突且影响回答结论：报告冲突点，不要默默二选一。
- 用户问的知识在快照期之后（新版本游戏）：明说没有，问是否要刷新快照，
  不要编。
