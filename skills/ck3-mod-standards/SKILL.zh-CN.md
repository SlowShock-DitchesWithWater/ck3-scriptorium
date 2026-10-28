# CK3 Mod 编码规约（ck3-mod-standards）· 中文版

> 本文件是英文主版 [SKILL.md](SKILL.md) 的中文副本，内容同步维护。
> agent 加载器只读 SKILL.md（英文主版）；本副本供人阅读与中文用户参考。

（对应英文版版本：1.3）

# CK3 Mod 编码规约

写给 AI agent：你在产出 CK3（Jomini 脚本）mod 代码时按本规约执行。规则分两层——
**程序性纪律**（长期稳定，本文件主体）与**签名事实**（随游戏版本变化，一律去知识库查，禁止凭记忆写）。

本 skill 只管"怎么写代码"；知识库本身的检索规约（怎么查资料）见知识库根目录
`AGENTS.md`；运行时报错诊断（Tiger 与游戏的 error 日志）不在本 skill 范围内。

## 0. 签名防幻觉（最高优先级）

任何 effect / trigger / modifier / on_action / 字段名：**要么来自知识库，要么明说"未核实"**。没有第三种。

知识库位置——按以下顺序解析，命中即停：

1. **同仓共位**：若相对本文件的 `../../` 处存在 `catalog.md` 与 `AGENTS.md`
   （即 skill 位于克隆的 ck3-scriptorium 仓库的 `skills/` 下），该仓库根目录
   **就是**知识库——无需任何配置。
2. **`kb_location.txt`**：本 skill 目录下的单行文件，内容为知识库根目录的
   绝对路径（每机配置，gitignored——知识库不在 skill 旁边时用它指定）。
3. **环境变量** `CK3_KB_PATH`：值为知识库根目录路径。
4. **询问用户**（通常是对方的 ck3-scriptorium 克隆位置），并建议把答案写入
   `kb_location.txt`，下次免问。

检索规约见知识库根目录 `AGENTS.md`（先 grep `catalog.md` → 按条目读 `pages/` 或 `game_docs/`）。快速路径：

- 查 effect/trigger 签名与 Supported Scopes → `game_docs/script_docs/effects.md` / `triggers.md`（`### 名称` 小节，权威层）
- 查某条目名（trait/title/culture…）定义在原版哪个文件 → `game_docs/vanilla_structure/entry_map.tsv`
- 查机制讲解 → grep `catalog.md` 关键词 → 读命中页

生成代码后，逐个核对用到的脚本词是否真实存在；记不准的词先查再用。

## 1. 作用域纪律

CK3 脚本的每一段都在某个作用域（character / title / province / faith / none…）里解释，作用域错了代码"看起来对"但行为全错。

- **写任何 effect/trigger 前先确认当前作用域**：事件里默认 root 即触发者所在链；on_action 的预期作用域各不相同（如 `on_game_start` 无 root、全局一次性触发，只能用 `every_ruler` 等全局效果；`yearly_playable_pulse` 以 character 为 root）——依据 `pages/Event modding/12-On-Actions-on_action.md`（on_action 表与 Scopes 节）与 `game_docs/script_docs/event_scopes.md`。
- **作用域切换后立即自证**：链式切换（如 `father = { … }`）可能落到空作用域；目标可能不存在时先加存在性判断（trigger 侧）或使用 `limit`。
- `root` / `this` / `prev` 只在**有默认上下文**的块里可用——character interactions 等部分块没有 `root`（依据 `pages/Scopes.md`）。不确定就查，别假设。
- 大范围迭代（`every_*`）必须带 `limit` 或权重收窄，见 §5 性能。

## 2. on_action 桥接（不覆盖原版）

向已有 on_action（如 `on_birth_child`）挂内容时，**禁止直接写它的 `trigger`/`effect`——那是覆盖，会吃掉原版和其他 mod 的逻辑**。正确姿势（依据 `pages/Event modding/12-On-Actions-on_action.md` §Appending）：

```
# 新建自己的 txt 文件（common/on_action/，注意目录名单数 on_action，不是 on_actions）
on_birth_child = {
  on_actions = { my_mod_my_on_action }   # 把自定义 on_action 追加进去
}
my_mod_my_on_action = {
  trigger = { ... }    # 只属于这段的触发条件
  effect = { ... }     # 效果安全追加，不覆盖任何人
}
```

要点：

- `events` 与 `on_actions` 列表是**追加**语义；`trigger`/`effect` 是**覆盖**语义——只有前两者可以直接加。
- 自定义 on_action 用来打包复用（group events/effects）；可以新建自定义 on_action，**不能新建代码侧 on_action**。
- 每个 on_action 的预期作用域不同，先查表（同上章节的 "On_actions from code" 表）。
- 没有月度 pulse（性能考量）；要近似月度用 `quarterly_playable_pulse` + `delay = { months = … }` 分次触发。

## 3. 加载顺序兼容（最小 footprint）

同路径文件**整文件覆盖**、同实体名**按文件名字母序后者胜出**（实体级覆盖；events 不是可覆盖实体，要经 scripted effect 中转）——依据 `pages/Mod compatibility.md`：

- **最小化 footprint**：只覆盖你确实要改的原版文件/实体；能用"追加"（on_action 列表、新文件新实体）就不覆盖。footprint 越小，与其他 mod 共存概率越高。
- **命名一律带 mod 前缀**：scripted_effects/triggers、on_action、事件 ID、变量名（如 `mymod_` 前缀）。裸名（`my_effect`）极易撞车。
- **跨 mod 协作点用约定实体**：
  - 共享变量：A mod 设 `set_variable = { name = amod_did_x … }`，B mod 用 `has_variable = amod_did_x` 探测——不依赖对方是否加载。
  - 共享 scripted effect（A 提供默认实现存 `aaa_` 早字母文件，B 想替换则把同名实体存 `zzz_` 晚字母文件覆盖）。
  - 探测他 mod：被探测方定义 `xxx_is_loaded = { always = yes }` scripted trigger 存晚字母文件；探测方同名定义 `always = no` 存早字母文件，用 `xxx_is_loaded = yes` 判断。
- 总换血 TC（删除原版内容）兼容是另一档要求（禁止引用具体 faith/culture 等数据库实体）——除非用户明确要求，不必默认满足。

## 4. 文件组织与本地化

- mod 结构：mod 文件夹 + 同名 `.mod` 描述文件位于 `~\Paradox Interactive\Crusader Kings III\mod`；文件夹路径不得含非英文字符（依据 `pages/Mod structure.md`）。
- 脚本文件按类型入对应 `common\*` 子目录（decisions → `common/decisions`，on_action → `common/on_action`…）；文件名带 mod 前缀。
- **玩家可见文本一律走本地化 key**，禁止硬编码进事件正文：
  - `localization\<language>\` 下建 `xxx_l_english.yml` 式文件：文件名含 `l_<language>`、首行 `l_english:`、**UTF-8 带 BOM** 编码（依据 `pages/Localization.md`）。
  - 事件/决议的 title/desc/option 全部用 key；生成脚本时同步产出 loc 文件，不留 `TITLE_MISSING`。

## 5. 性能习惯

- **不要在按角色循环的 pulse 里再全量遍历角色**：如 `yearly_playable_pulse` 已对每个可玩角色触发，内部再 `every_living_character` 会产生约 200002 次操作级别的灾难（依据 `pages/Event modding/12-On-Actions-on_action.md` §Scopes 警告）。
- 大作用域迭代必带 `limit`；随机抽取用 `random_` 系并配权重，而不是 every + 自造随机。
- 事件用 `mean_time_to_happen` / weight 控频，能低频不高频；重逻辑放低频 pulse。

## 6. 交付前自检清单

产出代码后逐项过：

1. 每个脚本词（effect/trigger/字段）都在知识库核对过？来源路径可追溯？
2. 每段的作用域明确？`root` 使用处确认该块有 root？
3. on_action 只做了追加（`on_actions = { … }` / `events = { … }`），没有覆盖原版 `trigger`/`effect`？
4. 实体/文件/变量/事件 ID 全部带 mod 前缀？没有覆盖不必要的原版文件？
5. 玩家可见文本全部有本地化 key？loc 文件格式（BOM / `l_english:` / 文件名）正确？
6. 循环都有 limit？没有在 per-character pulse 里嵌套全量遍历？

## 依据与时效

本规约的程序性纪律抽取自本地知识库：`pages/Mod compatibility.md`、
`pages/Event modding/12-On-Actions-on_action.md`、`pages/Localization.md`、
`pages/Scopes.md`、`pages/Mod structure.md`，以及 `game_docs/script_docs/`
（签名权威层）。知识库的快照日期与游戏版本以其 `catalog.md` 头部快照块为准
（本文件不记录这些数字——它们会随刷新变化）。签名与数值类事实会随版本漂移：
永远查库，不要把本文件的示例代码当签名事实（示例只演示结构与纪律）。
