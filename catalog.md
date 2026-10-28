# CK3 Modding 知识库目录（catalog）

> 检索规约：先读本目录定位文件与章节，再只读所需章节；禁止整库读入。
> 权威顺序：游戏 script_docs dump 层（game_docs/）> wiki 层（pages/）；
> 两层冲突时以 dump 层为准，冲突点会在条目中标注。
> 内容来源：ck3.paradoxwikis.com（CC BY-SA 3.0），每条目标注 oldid 与抓取日期。

<!-- ck3wiki-mod-kb:snapshot BEGIN -->
> 快照：抓取 2026-10-23 · wiki 141 页 · 游戏 1.20.1（dump 并入 2026-10-29） · 锚点 oldid：Effects=20200，Triggers=26702，Event modding=37279
<!-- ck3wiki-mod-kb:snapshot END -->

<!-- ck3wiki-mod-kb:entry BEGIN Scripting -->
## Scripting

- **文件位置**：`pages/Scripting.md`
- **来源**：<https://ck3.paradoxwikis.com/Scripting>（oldid 33911，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：写任何 CK3 脚本前打地基：关键字、操作符、if/while 语句、列表与迭代器写法不确定时查。
- **中文摘要**：脚本语言总纲：keywords/operators/statements、Lists/Arrays、Iterators、Templates（scripted_*）与常见 workaround。
- **英文关键词**：Scripting；trigger_if；switch；iterator；Basics；Keywords
- **章节**：
  - Basics — Documentation / Limitations / Script language name / Testing
  - Basics — Syntax / Scopes / Chaining / Prefixes / Formatting
  - Keywords
  - Operators — Logic operators / Relational operators
  - Saved scopes
  - Variables
  - Statements — if / else / else_if / switch / while loop / trigger_if / trigger_else / trigger_else_if
  - Lists / Arrays
  - Iterators — Effect iterators / Trigger iterator / List iterators
  - Templates — Scripted effects / Substitution / Scripted triggers / Script values
  - Workarounds — Exchanging information with other apps / Arrays
<!-- ck3wiki-mod-kb:entry END Scripting -->

<!-- ck3wiki-mod-kb:entry BEGIN Effects -->
## Effects

- **文件位置**：`pages/Effects.md`（章节索引）＋ 章节目录 `pages/Effects/`
- **来源**：<https://ck3.paradoxwikis.com/Effects>（oldid 20200，抓取 2026-10-22，页面标注版本 1.7）
- **何时查**：写事件/决策的执行动作、不确定某 effect 是否存在或参数形态时查；权威签名见游戏层 effects.md。
- **中文摘要**：effect 用法讲解：effect 块与语法、scripted_effects 宏、conditional/control effects 与 dump 导出。
- **英文关键词**：Effects；if；else_if；every；random；ordered
- **章节**：
  - Effect blocks（`01-Effect-blocks.md`）
  - Effect syntax（`02-Effect-syntax.md`）
    - Code effects
  - scripted_effects（`03-scripted_effects.md`）
    - Simple form
    - Complex form
  - Conditional effects（`04-Conditional-effects.md`）
  - Control effects（`05-Control-effects.md`）
  - Dump Export（`06-Dump-Export.md`）
<!-- ck3wiki-mod-kb:entry END Effects -->

<!-- ck3wiki-mod-kb:entry BEGIN Scopes -->
## Scopes

- **文件位置**：`pages/Scopes.md`
- **来源**：<https://ck3.paradoxwikis.com/Scopes>（oldid 28429，抓取 2026-10-22，页面标注版本 1.1）
- **何时查**：不确定当前作用域类型、如何切换/保存/引用作用域（root/this/prev、saved scope）时查。
- **中文摘要**：作用域机制：database/primitive/top scope、every_X 等 list-builder 语义与作用域引用。
- **英文关键词**：Scopes；root；this；prev；save_scope_as；scope:
- **章节**：
  - Definition — Database scope / Primitive scope / Top scope
  - Accessing scopes — root / Context switch / Database access / Event target / this / prev / Saved scope / List-builder / every_X / random_X / ordered_X / any_X / Saved scope value
  - References
<!-- ck3wiki-mod-kb:entry END Scopes -->

<!-- ck3wiki-mod-kb:entry BEGIN Triggers -->
## Triggers

- **文件位置**：`pages/Triggers.md`
- **来源**：<https://ck3.paradoxwikis.com/Triggers>（oldid 26702，抓取 2026-10-22，页面标注版本 1.7）
- **何时查**：写条件判断（trigger/limit 块）、不确定逻辑块或比较写法时查；权威清单见游戏层 triggers.md。
- **中文摘要**：trigger 语法：AND/OR/NOT 逻辑块、limit、scope/value 比较、scripted_triggers。
- **英文关键词**：Triggers；limit；AND；OR；NOT；trigger_if
- **章节**：
  - Trigger blocks — Early out / Logic blocks / AND / OR / NOT/NOR/NAND / Limit blocks / if/else_if / effect list-builders / trigger_if/trigger_else_if/trigger_else
  - Trigger syntax — Scope comparison / Value comparison / Code triggers / Basic triggers / Simple triggers / Complex triggers / In-line complex triggers / scripted_triggers / Basic scripted_triggers / Complex scripted_triggers
  - Logical Operators/Triggers
  - References
<!-- ck3wiki-mod-kb:entry END Triggers -->

<!-- ck3wiki-mod-kb:entry BEGIN Variables -->
## Variables

- **文件位置**：`pages/Variables.md`
- **来源**：<https://ck3.paradoxwikis.com/Variables>（oldid 30166，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：需要 set/change/remove 变量，或用 global/local 变量存取状态时查。
- **中文摘要**：变量操作：set_variable/change_variable、global 与 local 变量的生命周期和访问。
- **英文关键词**：Variables；set_variable；change_variable；clear_variable；Setting a variable；Modifying a variable
- **章节**：
  - Setting a variable
  - Modifying a variable
  - Removing a variable
  - Accessing a variable
  - Global variables
  - Local variables
  - References
<!-- ck3wiki-mod-kb:entry END Variables -->

<!-- ck3wiki-mod-kb:entry BEGIN Modifier list -->
## Modifier list

- **文件位置**：`pages/Modifier list.md`
- **来源**：<https://ck3.paradoxwikis.com/Modifier_list>（oldid 27588，抓取 2026-10-22，页面标注版本 1.12）
- **何时查**：给角色/王朝/头衔等加成、或查全部可用 modifier 名时查；权威以游戏层 modifiers.md 为准。
- **中文摘要**：自定义 character modifier 创建法与全量 modifier 清单表（vassal stance/government/holding/scheme/terrain/MaA 等类）。
- **英文关键词**：Modifier list；add_character_modifier；icon；Creating a Character Modifier；List of Modifiers
- **章节**：
  - Creating a Character Modifier — Icons
  - List of Modifiers — Vassal Stance Related Modifiers / Government Related Modifiers / Holding-type Related Modifiers / Scheme Related Modifiers / Terrain Modifiers / Men-at-Arms Related Modifiers
<!-- ck3wiki-mod-kb:entry END Modifier list -->

<!-- ck3wiki-mod-kb:entry BEGIN AI modding -->
## AI modding

- **文件位置**：`pages/AI modding.md`
- **来源**：<https://ck3.paradoxwikis.com/AI_modding>（oldid 35063，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：调 AI 行为：ai_will_do 权重、AI personality、chance 逻辑或相关 defines 时查。
- **中文摘要**：AI 定制途径：defines 调参、chance/weight 逻辑、AI personality 与 script 钩子。
- **英文关键词**：AI modding；ai_will_do；ai_personality；chance；Defines；Chance
- **章节**：
  - Defines
  - Chance
  - AI personality
  - Script
<!-- ck3wiki-mod-kb:entry END AI modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Bookmarks modding -->
## Bookmarks modding

- **文件位置**：`pages/Bookmarks modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Bookmarks_modding>（oldid 19306，抓取 2026-10-22，页面标注版本 1.1）
- **何时查**：做开局书签：起始日期、可选角色组、书签界面与按钮时查。
- **中文摘要**：bookmark 定义结构、portraits、书签界面按钮与本地化。
- **英文关键词**：Bookmarks modding；bookmark；playable_character；Creating the bookmark；Portraits；Bookmark Screen
- **章节**：
  - Creating the bookmark
  - Portraits
  - Bookmark Screen — Designing the Selection Screen Map / Bookmark Coat of Arms
  - Buttons
  - Localization
  - References
<!-- ck3wiki-mod-kb:entry END Bookmarks modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Characters modding -->
## Characters modding

- **文件位置**：`pages/Characters modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Characters_modding>（oldid 37252，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：用脚本改角色外观/服装 outfit、新增改写角色或跨脚本引用角色时查。
- **中文摘要**：角色脚本化：外观与 outfit tags、新增/改写角色、在其他脚本中调用角色。
- **英文关键词**：Characters modding；create_character；Changing appearance through scripts；Outfit Tags；Adding new characters or changing existing；Calling characters from other scripts
- **章节**：
  - Changing appearance through scripts
  - Outfit Tags — Using outfit_tags / Creating outfit_tags
  - Adding new characters or changing existing — Advanced use of date blocks / Hairstyles and beards for scripted characters
  - Calling characters from other scripts
  - References
<!-- ck3wiki-mod-kb:entry END Characters modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Commands -->
## Commands

- **文件位置**：`pages/Commands.md`
- **来源**：<https://ck3.paradoxwikis.com/Commands>（oldid 25990，抓取 2026-10-22，页面标注版本 1.0）
- **何时查**：查 wiki 版 effect（commands）大表：示例/作用域/值类型/分类；权威以游戏层 effects.md 为准。
- **中文摘要**：wiki 版 commands 清单大表：名称/作用域/值类型/示例/分类；数据偏旧。
- **英文关键词**：Commands；command；List of Commands
- **章节**：
  - List of Commands
<!-- ck3wiki-mod-kb:entry END Commands -->

<!-- ck3wiki-mod-kb:entry BEGIN Council modding -->
## Council modding

- **文件位置**：`pages/Council modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Council_modding>（oldid 33854，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：新增或修改内阁职位（council positions）及其任务时查。
- **中文摘要**：council positions 的定义结构（common/council_positions）与字段示例。
- **英文关键词**：Council modding；council_positions；council_task；Council Positions Structure
- **章节**：
  - Council Positions Structure
<!-- ck3wiki-mod-kb:entry END Council modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Culture modding -->
## Culture modding

- **文件位置**：`pages/Culture modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Culture_modding>（oldid 34599，抓取 2026-10-22，页面标注版本 1.4）
- **何时查**：建/改文化与文化组、heritage/pillar/tradition 或 name_list 时查。
- **中文摘要**：文化体系：culture groups 与 cultures 定义结构、ID 约定。
- **英文关键词**：Culture modding；heritage；pillar；tradition；name_list；Culture Groups
- **章节**：
  - Culture Groups
  - Cultures
  - Culture group ID
  - Culture ID
<!-- ck3wiki-mod-kb:entry END Culture modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Decisions modding -->
## Decisions modding

- **文件位置**：`pages/Decisions modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Decisions_modding>（oldid 26456，抓取 2026-10-22，页面标注版本 1.14）
- **何时查**：写决策（major/minor decisions）：结构、作用域、custom widget 或测试时查。
- **中文摘要**：决策定义：文件位置、block 结构、本地化、custom widgets 与测试方法。
- **英文关键词**：Decisions modding；major_decision；minor_decision；Location；Structure；Localization
- **章节**：
  - Location
  - Structure — Basic example
  - Localization — Keys/blocks / Values
  - Custom widgets
  - Testing Decisions
  - Decision ID
<!-- ck3wiki-mod-kb:entry END Decisions modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Dynasties modding -->
## Dynasties modding

- **文件位置**：`pages/Dynasties modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Dynasties_modding>（oldid 11523，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：新建王朝/家族分支、改王朝前缀、纹章或家训时查。
- **中文摘要**：王朝与 house：创建 dynasty、prefix、CoA、motto 与 house 定义。
- **英文关键词**：Dynasties modding；dynasty；house；motto；Creating a new dynasty；Prefixes
- **章节**：
  - Creating a new dynasty
  - Prefixes
  - Coat of arms
  - Motto
  - House
<!-- ck3wiki-mod-kb:entry END Dynasties modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Event modding -->
## Event modding

- **文件位置**：`pages/Event modding.md`（章节索引）＋ 章节目录 `pages/Event modding/`
- **来源**：<https://ck3.paradoxwikis.com/Event_modding>（oldid 37279，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：写事件：结构（trigger/immediate/option/after）、主题头像、on_action 挂载或触发策略时查。
- **中文摘要**：事件教程（拆 13 章）：结构、portrait/theme、immediate/option/after、on_action 与策略。
- **英文关键词**：Event modding；on_action；immediate；option；trigger_event；fire_only_once
- **章节**：
  - Scripting Tools（`01-Scripting-Tools.md`）
    - Visual Studio Code
    - Sublime Text
    - Notepad++
  - Location（`02-Location.md`）
  - Structure（`03-Structure.md`）
    - ID and namespace
    - Flags
  - Portraits（`04-Portraits.md`）
    - Portrait Positions
    - Animations
  - Themes（`05-Themes.md`）
    - Environments
  - Trigger（`06-Trigger.md`）
    - on_trigger_fail
  - Description（`07-Description.md`）
  - Immediate（`08-Immediate.md`）
  - Options（`09-Options.md`）
  - After（`10-After.md`）
  - Widgets（`11-Widgets.md`）
  - On Actions (on_action)（`12-On-Actions-on_action.md`）
    - Common examples
    - Appending
    - Scopes
    - Properties
    - On_actions from code
  - Strategy（`13-Strategy.md`）
    - Triggering the event
    - Techniques and design patterns
<!-- ck3wiki-mod-kb:entry END Event modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Governments modding -->
## Governments modding

- **文件位置**：`pages/Governments modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Governments_modding>（oldid 13009，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：新增/修改政体类型：primary holding、封臣契约、政体 AI 开关时查。
- **中文摘要**：government 定义示例（00_government_types）：primary_holding/valid_holdings/vassal_contract/ai 等字段。
- **英文关键词**：Governments modding；primary_holding；vassal_contract
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Governments modding -->

<!-- ck3wiki-mod-kb:entry BEGIN History modding -->
## History modding

- **文件位置**：`pages/History modding.md`
- **来源**：<https://ck3.paradoxwikis.com/History_modding>（oldid 17535，抓取 2026-10-22，页面标注版本 1.1）
- **何时查**：改开局历史：头衔持有/继承、文化变迁或历史角色效果时查。
- **中文摘要**：history 文件：title history（holder 等）、culture history 与 effects 用法。
- **英文关键词**：History modding；history/titles；holder；Title history modding；Culture history modding；Effects
- **章节**：
  - Title history modding
  - Culture history modding
  - Effects
<!-- ck3wiki-mod-kb:entry END History modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Holdings modding -->
## Holdings modding

- **文件位置**：`pages/Holdings modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Holdings_modding>（oldid 33465，抓取 2026-10-22，页面标注版本 1.3）
- **何时查**：新增地产类型（holding type）及其可用建筑/图标时查。
- **中文摘要**：holding 定义（common/holdings）：primary_building/buildings/flag 等变量示例。
- **英文关键词**：Holdings modding；primary_building
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Holdings modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Lifestyles modding -->
## Lifestyles modding

- **文件位置**：`pages/Lifestyles modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Lifestyles_modding>（oldid 35087，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：做生活方式、专精（focus）或 perk 树时查。
- **中文摘要**：生活方式体系：lifestyle/focus/perk 定义结构与原版清单。
- **英文关键词**：Lifestyles modding；lifestyle；focus；perk；Lifestyles；Lifestyle focuses
- **章节**：
  - Lifestyles — Scripting / Triggers / Graphics / Localization
  - Lifestyle focuses — Scripting / Graphics / Localization
  - Lifestyle perks — Scripting / Graphics / Localization
  - Vanilla list
<!-- ck3wiki-mod-kb:entry END Lifestyles modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Regiments modding -->
## Regiments modding

- **文件位置**：`pages/Regiments modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Regiments_modding>（oldid 16675，抓取 2026-10-22，页面标注版本 1.3）
- **何时查**：加兵种类型（Men-at-Arms）：属性、地形加成、克制与费用时查。
- **中文摘要**：men_at_arms_types 定义：damage/toughness/pursuit/screen、terrain_bonus、counters 与成本。
- **英文关键词**：Regiments modding；men_at_arms；damage；toughness；counters
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Regiments modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Religions modding -->
## Religions modding

- **文件位置**：`pages/Religions modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Religions_modding>（oldid 37089，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：建宗教/信仰/仪式：religion/faith/rite 结构、圣地与教义时查。
- **中文摘要**：宗教体系：religion family、faith/rite 结构、holy sites、tenet 与本地化图形。
- **英文关键词**：Religions modding；faith；tenet；holy_site；rite；Religion family
- **章节**：
  - Religion family
  - Religion structure
  - Faith structure
  - Rite structure
  - Localization
  - Graphics
  - Holy sites
  - Tenet ID
<!-- ck3wiki-mod-kb:entry END Religions modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Script values -->
## Script values

- **文件位置**：`pages/Script values.md`
- **来源**：<https://ck3.paradoxwikis.com/Script_values>（oldid 35088，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：把数值算式抽成可复用 script_value 或写动态数值（算式函数）时查。
- **中文摘要**：script_values 定义（common/script_values）：add/subtract/…/max/min 算式与随处引用。
- **英文关键词**：Script values；add；subtract；multiply；divide；value
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Script values -->

<!-- ck3wiki-mod-kb:entry BEGIN Story cycles modding -->
## Story cycles modding

- **文件位置**：`pages/Story cycles modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Story_cycles_modding>（oldid 24141，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：做周期性事件管理器（如宠物剧情）或需跨角色死亡持久存变量时查。
- **中文摘要**：story cycle：on_setup/on_end/on_owner_death 与 effect_group 周期脉冲、create_story。
- **英文关键词**：Story cycles modding；create_story；effect_group；story_owner；Creating a story cycle
- **章节**：
  - Creating a story cycle
<!-- ck3wiki-mod-kb:entry END Story cycles modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Struggle modding -->
## Struggle modding

- **文件位置**：`pages/Struggle modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Struggle_modding>（oldid 35994，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：做 Iberia 式争端（struggle）：阶段、参与方、启动与联动时查。
- **中文摘要**：struggle 设置：setup、启动、phases 与其他 modding 教程链接。
- **英文关键词**：Struggle modding；struggle；phase；Setup；Starting the struggle；Phases
- **章节**：
  - Setup — Cultures and Faiths / Regions / Conditions / Involvement prerequisite percentage / Textures/2D-Graphics / Struggle-phase Background's / Struggle-phase Icon's
  - Starting the struggle — Starting the Struggle
  - Phases — Phases / Phase effects / Catalysts / Creating a catalysts / Localization / Defining catalysts in struggle phases
  - External Links
  - Other modding tutorials
<!-- ck3wiki-mod-kb:entry END Struggle modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Title modding -->
## Title modding

- **文件位置**：`pages/Title modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Title_modding>（oldid 32469，抓取 2026-10-22，页面标注版本 1.1）
- **何时查**：建/改头衔：titular title、属性表、公国首府建筑或文化命名时查。
- **中文摘要**：头衔定义：titular title、属性清单、duchy capital building、history 与文化名。
- **英文关键词**：Title modding；landed_titles；titular；de_jure；Basic Titular Title；Localization
- **章节**：
  - Basic Titular Title
  - Localization
  - Coat of Arms
  - List of attributes
  - Duchy Capital Building
  - History
  - Defining Cultural Names
<!-- ck3wiki-mod-kb:entry END Title modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Trait modding -->
## Trait modding

- **文件位置**：`pages/Trait modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Trait_modding>（oldid 35953，抓取 2026-10-22，页面标注版本 1.0）
- **何时查**：新增/修改角色特质及其图标、本地化时查。
- **中文摘要**：特质定义结构、创建字段、icon 与本地化；附过时的数值 ID 表。
- **英文关键词**：Trait modding；trait；icon；Character Traits；Creating a trait；Localization
- **章节**：
  - Character Traits
  - Creating a trait — Trait category / Trait validation / Special trait flags / Creating immortal traits / Trait Index
  - Localization
  - Icon
  - Unique Numerical Identifier List (Obsolete)
<!-- ck3wiki-mod-kb:entry END Trait modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Interface -->
## Interface

- **文件位置**：`pages/Interface.md`（章节索引）＋ 章节目录 `pages/Interface/`
- **来源**：<https://ck3.paradoxwikis.com/Interface>（oldid 35928，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：做 GUI：改界面、新窗口、scripted GUI 或 data binding 排障时查（已拆 9 章）。
- **中文摘要**：GUI 教程（拆 9 章）：GUI mod 基础、检查器、UI 代码、scripted GUI、view 清单与排障。
- **英文关键词**：Interface；gui；scripted_gui；widget；Basics；Creating a GUI mod
- **章节**：
  - Basics（`01-Basics.md`）
  - Creating a GUI mod（`02-Creating-a-GUI-mod.md`）
  - Inspecting GUI（`03-Inspecting-GUI.md`）
    - GUI Debug
    - GUI Editor
  - UI code（`04-UI-code.md`）
    - Promotes and Functions
    - UI Components
    - Templates
  - Scripted GUIs（`05-Scripted-GUIs.md`）
    - Displaying a variable or script value
    - Displaying data lists
  - New windows and toggles（`06-New-windows-and-toggles.md`）
    - Create a window as a scripted widget
    - Toggle window visibility
    - Toggles with PdxGuiWidget
    - Toggles with animation
    - System Variables
    - Creating a new Widget
  - List of existing game views（`07-List-of-existing-game-views.md`）
  - Troubleshooting（`08-Troubleshooting.md`）
    - Known crash reasons
  - Useful links（`09-Useful-links.md`）
<!-- ck3wiki-mod-kb:entry END Interface -->

<!-- ck3wiki-mod-kb:entry BEGIN Data types -->
## Data types

- **文件位置**：`pages/Data types.md`（章节索引）＋ 章节目录 `pages/Data types/`
- **来源**：<https://ck3.paradoxwikis.com/Data_types>（oldid 14585，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：查脚本 data type、promote 或 global function 的 wiki 讲解时查；权威以游戏层 data_types_*.md 为准。
- **中文摘要**：数据类型页（拆 4 章）：Data Types、Global Promotes、Global Functions、Types 清单。
- **英文关键词**：Data types；data type；promote；global function；Data Types；List of Global Promotes
- **章节**：
  - Data Types（`01-Data-Types.md`）
  - List of Global Promotes（`02-List-of-Global-Promotes.md`）
  - List of Global Functions（`03-List-of-Global-Functions.md`）
  - Types（`04-Types.md`）
    - ActiveCasusBelli
    - ActiveCouncilTask
    - Activity
    - Army
    - Artifact
    - Character
    - Combat
    - CombatSide
    - County
    - Culture
    - CultureGroup
    - Dynasty
    - DynastyHouse
    - Faction
    - Faith
    - Holding
    - Province
    - Religion
    - ReligionFamily
    - Scope
    - ScriptedGui
    - Title
    - TopScope
    - War
<!-- ck3wiki-mod-kb:entry END Data types -->

<!-- ck3wiki-mod-kb:entry BEGIN Localization -->
## Localization

- **文件位置**：`pages/Localization.md`
- **来源**：<https://ck3.paradoxwikis.com/Localization>（oldid 32485，抓取 2026-10-22，页面标注版本 1.4）
- **何时查**：写本地化：文件格式、key 复用、颜色/图标/链接/数字格式或特殊字符时查。
- **中文摘要**：本地化：格式化、条目复用、数据类型、链接/图标/数字/特殊字符与中文标点。
- **英文关键词**：Localization；l_english；localization；Formatting；Re-use other entries；Data Types
- **章节**：
  - Formatting
  - Re-use other entries
  - Data Types — Gender / Character names / Arguments
  - Special Characters
  - Linking — Game Concepts / Example Custom Game Concept / Traits / Titles
  - Number formatting
  - Icons
  - Usage of special characters & Line breaks
  - Chinese punctuation
  - References
<!-- ck3wiki-mod-kb:entry END Localization -->

<!-- ck3wiki-mod-kb:entry BEGIN Customizable localization -->
## Customizable localization

- **文件位置**：`pages/Customizable localization.md`
- **来源**：<https://ck3.paradoxwikis.com/Customizable_localization>（oldid 35064，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：需要按条件动态切换的本地化文本（一个 key 多分支）时查；称号显示见 Flavorization。
- **中文摘要**：customizable_localization 定义：type/scope + 多个 text 分支（trigger/fallback）。
- **英文关键词**：Customizable localization；customizable_localization；text；fallback；Game files；Modding customizable localization
- **章节**：
  - Game files
  - Modding customizable localization
<!-- ck3wiki-mod-kb:entry END Customizable localization -->

<!-- ck3wiki-mod-kb:entry BEGIN Flavorization -->
## Flavorization

- **文件位置**：`pages/Flavorization.md`
- **来源**：<https://ck3.paradoxwikis.com/Flavorization>（oldid 31792，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：定制角色/头衔的显示称号及其优先级（Prince/Petty King 等）时查。
- **中文摘要**：称号 flavor：type/gender/special/tier/priority 字段与示例。
- **英文关键词**：Flavorization；priority；special；tier；Grammar；Custom Flavor Example
- **章节**：
  - Grammar
  - Custom Flavor Example
  - Expanding Functionality Through Customizable Localization
  - Continue Reading
<!-- ck3wiki-mod-kb:entry END Flavorization -->

<!-- ck3wiki-mod-kb:entry BEGIN Map modding -->
## Map modding

- **文件位置**：`pages/Map modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Map_modding>（oldid 34676，抓取 2026-10-22，页面标注版本 1.1）
- **何时查**：换地图或改省份：heightmap、河流、province、地形与连接时查。
- **中文摘要**：地图全流程：heightmap/river/province map、titles、terrain、locator、connections 与自定义分辨率。
- **英文关键词**：Map modding；heightmap；province；rivers；Getting Started；Heightmap
- **章节**：
  - Getting Started
  - Heightmap — Creating a heightmap / The main heightmap file / Other heightmap files / Repacking
  - River map — Understanding river map colors / Pixel perfect / Draw procedure / River source / Underwater river tricks
  - Province map
  - Creating titles — Defining baronies / Defining the holdings, religions, and culture of baronies / Landed titles
  - Terrains of provinces
  - Map locators — Auto nudge
  - Connections
  - Creating a Map with a Custom Resolution — How to import the heightmap / Repacking terrain masks / North part of the hightmap not rendering and shows all black since 1.9
  - Creating Custom Terrain Textures
  - Frequently asked questions — Why can't I scroll all the way to the right? / Why can't I use the auto-nudge (dice) button to place my buildings and locators? / Why is there a line across the screen?
<!-- ck3wiki-mod-kb:entry END Map modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Terrain modding -->
## Terrain modding

- **文件位置**：`pages/Terrain modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Terrain_modding>（oldid 30475，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：新增地形类型及其 modifier、贴图或省份映射时查。
- **中文摘要**：地形类型定义：creating terrain type、modifiers、terrain mapping。
- **英文关键词**：Terrain modding；terrain；Creating a Terrain Type；Modifiers；Terrain mapping
- **章节**：
  - Creating a Terrain Type — Scripting / Graphics / Localization
  - Modifiers — Modifiers used in terrains / Generated modifiers
  - Terrain mapping
<!-- ck3wiki-mod-kb:entry END Terrain modding -->

<!-- ck3wiki-mod-kb:entry BEGIN 3D models -->
## 3D models

- **文件位置**：`pages/3D models.md`
- **来源**：<https://ck3.paradoxwikis.com/3D_models>（oldid 28182，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：导入自建 3D 模型（角色/物件）到游戏或地图时查。
- **中文摘要**：3D 模型流程：概览、制作准备、上地图步骤。
- **英文关键词**：3D models；mesh；asset；Overview；Tutorial: Setup；Making the Model
- **章节**：
  - Overview
  - Tutorial: Setup — Tools / Setup Clausewitz Maya exporter
  - Making the Model — Preparing Maya/Blender 3d model / UVs / Issues with UV maps / Broken normals / Textures / Formats / Icons / Illustrations & Backgrounds / Clothing Textures / Building Textures / Channel packing / Gimp
  - Tutorial: Getting them on the map — Holdings
<!-- ck3wiki-mod-kb:entry END 3D models -->

<!-- ck3wiki-mod-kb:entry BEGIN Exporters -->
## Exporters

- **文件位置**：`pages/Exporters.md`
- **来源**：<https://ck3.paradoxwikis.com/Exporters>（oldid 8918，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：配置 Paradox 官方 Photoshop/Maya 资产导出器时查。
- **中文摘要**：PdxExporter 安装与配置（Photoshop/Maya）及论坛入口。
- **英文关键词**：Exporters；PdxExporter；Maya；Photoshop；Setup；Forum
- **章节**：
  - Setup — Installation / Photoshop Setup / Maya Setup
  - Forum
<!-- ck3wiki-mod-kb:entry END Exporters -->

<!-- ck3wiki-mod-kb:entry BEGIN Coat of arms modding -->
## Coat of arms modding

- **文件位置**：`pages/Coat of arms modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Coat_of_arms_modding>（oldid 26714，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：做纹章：静态/动态 CoA、继承、emblem 或用游戏内设计器时查。
- **中文摘要**：纹章 modding：关键字、示例、继承 subs、动态 CoA 与 emblem。
- **英文关键词**：Coat of arms modding；coat_of_arms；emblem；pattern；Valid keywords；Examples
- **章节**：
  - Valid keywords
  - Examples
  - Inheritance and subs
  - Dynamic Coats of Arms
  - Easy going by using the IN-Game Designer — Designer weaknesses
  - Coat of Arms Emblem Modding — .DDS file formatting / Emblem definitions file
<!-- ck3wiki-mod-kb:entry END Coat of arms modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Graphical assets -->
## Graphical assets

- **文件位置**：`pages/Graphical assets.md`
- **来源**：<https://ck3.paradoxwikis.com/Graphical_assets>（oldid 19440，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：建角色 portrait 调色板（hair/skin/eye dds）时查。
- **中文摘要**：portrait palettes：gfx/portraits 的 256x256 8.8.8 BGR .dds 三件套。
- **英文关键词**：Graphical assets；hair_palette；skin_palette；eye_palette；Portrait palettes
- **章节**：
  - Portrait palettes
<!-- ck3wiki-mod-kb:entry END Graphical assets -->

<!-- ck3wiki-mod-kb:entry BEGIN Fonts -->
## Fonts

- **文件位置**：`pages/Fonts.md`
- **来源**：<https://ck3.paradoxwikis.com/Fonts>（oldid 35219，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：替换或新增游戏字体时查。
- **中文摘要**：字体获取、制备与 CK3 替换步骤。
- **英文关键词**：Fonts；Acquiring and Preparing Fonts；Changing Fonts in Crusader Kings 3
- **章节**：
  - Acquiring and Preparing Fonts — Fantastic Fonts and Where to Find Them / Converting TrueType Fonts to OpenType Fonts
  - Changing Fonts in Crusader Kings 3
<!-- ck3wiki-mod-kb:entry END Fonts -->

<!-- ck3wiki-mod-kb:entry BEGIN Music modding -->
## Music modding

- **文件位置**：`pages/Music modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Music_modding>（oldid 34736，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：加自定义音乐并让其在音乐播放器可见时查。
- **中文摘要**：音乐 mod：文件放置位置与 music player 显示。
- **英文关键词**：Music modding；Showing them in the Music Player；Where to put the Music
- **章节**：
  - Showing them in the Music Player
  - Where to put the Music
<!-- ck3wiki-mod-kb:entry END Music modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Sound modding -->
## Sound modding

- **文件位置**：`pages/Sound modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Sound_modding>（oldid 29990，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：导入/播放音效：随机、重叠、3D 声音或参数调优时查。
- **中文摘要**：音效：导入、游戏内播放、随机/重叠/3D/参数与最佳实践。
- **英文关键词**：Sound modding；Import sounds；Playing sounds in the game；Troubleshooting；Random sounds；Overlapping sounds
- **章节**：
  - Import sounds — With a template / Bank name and crashing / Create from scratch
  - Playing sounds in the game
  - Troubleshooting
  - Random sounds
  - Overlapping sounds
  - 3D sound
  - Sound Parameters — Adding Sound Parameters to Events in FMOD / Using the Sound Parameters in In-Game GUI
  - Best Practice — Organizing your Events in Folders
<!-- ck3wiki-mod-kb:entry END Sound modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Console commands -->
## Console commands

- **文件位置**：`pages/Console commands.md`
- **来源**：<https://ck3.paradoxwikis.com/Console_commands>（oldid 37115，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：开 debug 模式用控制台测试：命令、作弊、查 trait/innovation tag 时查。
- **中文摘要**：控制台页：debug 模式、debug info、cheats、测试命令与 tag 表。
- **英文关键词**：Console commands；debug_mode；cheats；tag；Debug mode；Debug info
- **章节**：
  - Debug mode — Enabling debug mode / Mods / Launcher / Steam / Windows / GOG / Xbox Game Pass
  - Debug info — Characters / Events / Interactions
  - Cheats — Spawning artifacts / Converting commands / Shattered World mode / Scripting commands
  - Testing commands
  - Trait tags
  - Innovation tags
  - See also
  - References
<!-- ck3wiki-mod-kb:entry END Console commands -->

<!-- ck3wiki-mod-kb:entry BEGIN Patches -->
## Patches

- **文件位置**：`pages/Patches.md`
- **来源**：<https://ck3.paradoxwikis.com/Patches>（oldid 34713，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：判断知识时效、查某版本改动、checksum 或回滚旧版本时查。
- **中文摘要**：版本历史：1.x 全部 changelog、checksum 与版本回滚。
- **英文关键词**：Patches；checksum；rollback；Version history；Checksum；Rollback
- **章节**：
  - Version history
  - Checksum
  - Rollback
<!-- ck3wiki-mod-kb:entry END Patches -->

<!-- ck3wiki-mod-kb:entry BEGIN Mod structure -->
## Mod structure

- **文件位置**：`pages/Mod structure.md`
- **来源**：<https://ck3.paradoxwikis.com/Mod_structure>（oldid 18579，抓取 2026-10-22，页面标注版本 1.1）
- **何时查**：建新 mod 骨架：.mod 文件、目录结构与覆盖注意点时查。
- **中文摘要**：mod 结构：初始文件、.mod 文件写法、mod folder 与 tips。
- **英文关键词**：Mod structure；.mod；Creating initial files；The .mod files；Mod folder；Tips
- **章节**：
  - Creating initial files
  - The .mod files — Syntax / Keys / Basic example
  - Mod folder
  - Tips
<!-- ck3wiki-mod-kb:entry END Mod structure -->

<!-- ck3wiki-mod-kb:entry BEGIN Mod compatibility -->
## Mod compatibility

- **文件位置**：`pages/Mod compatibility.md`
- **来源**：<https://ck3.paradoxwikis.com/Mod_compatibility>（oldid 32474，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：设计多 mod 兼容：footprint 不重叠、共享变量/scripted effect 互通时查。
- **中文摘要**：兼容实践：override/footprint 原则、总转换兼容、共享变量与共享 scripted effect。
- **英文关键词**：Mod compatibility；override；footprint；General practices；Basic techniques；Detecting other mods
- **章节**：
  - General practices — Total conversions
  - Basic techniques — Shared variable / Shared scripted effect
  - Detecting other mods — Global variable / Scripted trigger
<!-- ck3wiki-mod-kb:entry END Mod compatibility -->

<!-- ck3wiki-mod-kb:entry BEGIN Modding tools -->
## Modding tools

- **文件位置**：`pages/Modding tools.md`
- **来源**：<https://ck3.paradoxwikis.com/Modding_tools>（oldid 35501，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：找社区工具：tiger 校验、地图工具、翻译或音频工具时查。
- **中文摘要**：社区工具表：ck3-tiger、地图生成/合并、本地化翻译、音频等工具与链接。
- **英文关键词**：Modding tools；ck3-tiger；validator；Table
- **章节**：
  - Table
<!-- ck3wiki-mod-kb:entry END Modding tools -->

<!-- ck3wiki-mod-kb:entry BEGIN Mod troubleshooting -->
## Mod troubleshooting

- **文件位置**：`pages/Mod troubleshooting.md`
- **来源**：<https://ck3.paradoxwikis.com/Mod_troubleshooting>（oldid 31655，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：mod 不生效/报错：开发者控制台、debug 流程或 run script 自动化时查。
- **中文摘要**：排障：开发者控制台与调试、debug 方法论、run scripts 自动化。
- **英文关键词**：Mod troubleshooting；error.log；debug；run；Basics of the Developer Console & Enabling Debugging；The Art of Debugging
- **章节**：
  - Basics of the Developer Console & Enabling Debugging — Getting Access to the Debug Tools / The Basics of the Developer Console
  - The Art of Debugging — Localization Debugging / Error Spam: Debugging Dynamic Loc and Trigger Conditions / Scope Debugging / Hot-loading
  - Automating the Debug Process Through Run Scripts
<!-- ck3wiki-mod-kb:entry END Mod troubleshooting -->

<!-- ck3wiki-mod-kb:entry BEGIN Artifact modding -->
## Artifact modding

- **文件位置**：`pages/Artifact modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Artifact_modding>（oldid 33020，抓取 2026-10-22，页面标注版本 1.8）
- **何时查**：做宝物（artifact）：模板 can_equip/reforge、类型与获得方式时查。
- **中文摘要**：artifact 代码分布（common/artifacts 等）与 templates 结构；页面较简略。
- **英文关键词**：Artifact modding；artifact；template；can_equip；Location
- **章节**：
  - Location — Templates / Structure / Visuals / Structure / Creation Effect / Creating starting Artifacts
<!-- ck3wiki-mod-kb:entry END Artifact modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Defines -->
## Defines

- **文件位置**：`pages/Defines.md`
- **来源**：<https://ck3.paradoxwikis.com/Defines>（oldid 34030，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：改全局常量（END_DATE 等不可脚本化行为）或查 define 名时查。
- **中文摘要**：defines 覆盖写法（只写改动项）+ 分类 defines 大表（偏旧）。
- **英文关键词**：Defines；NGame；END_DATE；Configuration；List of defines
- **章节**：
  - Configuration
  - List of defines — Game / Setup / Jomini Map / Skills / Characters
<!-- ck3wiki-mod-kb:entry END Defines -->

<!-- ck3wiki-mod-kb:entry BEGIN Effects list -->
## Effects list

- **文件位置**：`pages/Effects list.md`
- **来源**：<https://ck3.paradoxwikis.com/Effects_list>（oldid 35939，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：快速查某 effect 的 wiki 版大表（名称/示例/scopes/target）时查；权威以游戏层 effects.md 为准。
- **中文摘要**：effects.log 的 wiki 转录大表（已知偏旧、缺新 effect）；优先用游戏层 dump。
- **英文关键词**：Effects list；effect；scopes
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Effects list -->

<!-- ck3wiki-mod-kb:entry BEGIN Interactions modding -->
## Interactions modding

- **文件位置**：`pages/Interactions modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Interactions_modding>（oldid 20307，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：做角色互动（character interactions）：on_accept/on_send、actor/recipient 时查。
- **中文摘要**：character_interactions：basic_interaction 示例、on_accept/on_send 与 scope:actor/recipient。
- **英文关键词**：Interactions modding；character_interactions；on_accept；auto_accept；Example
- **章节**：
  - Example
<!-- ck3wiki-mod-kb:entry END Interactions modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Lists -->
## Lists

- **文件位置**：`pages/Lists.md`
- **来源**：<https://ck3.paradoxwikis.com/Lists>（oldid 20403，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：用 every_X/any_X 迭代集合、或自建列表（add_to_list/variable list）时查。
- **中文摘要**：列表机制：code lists 及参数、scripted_lists、custom lists（add_to_list + in_list）。
- **英文关键词**：Lists；every；any；random；add_to_list；in_list
- **章节**：
  - Code lists — List Parameters
  - scripted_lists
  - Custom lists — Normal lists / Variable lists
<!-- ck3wiki-mod-kb:entry END Lists -->

<!-- ck3wiki-mod-kb:entry BEGIN Scopes list -->
## Scopes list

- **文件位置**：`pages/Scopes list.md`
- **来源**：<https://ck3.paradoxwikis.com/Scopes_list>（oldid 20023，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：查某 scope 类型可用的 event target 链（wiki 版表，偏旧）；权威以游戏层 event_targets/event_scopes 为准。
- **中文摘要**：event_scopes/event_targets 日志的 wiki 转录：按 scope 类型列 target 链与去向。
- **英文关键词**：Scopes list；event_target；event_scope；Culture；Landed title；Dynasty house
- **章节**：
  - Culture
  - Landed title
  - Dynasty house
  - Dynasty
  - Secret
  - Holy order
  - Character
  - Army
  - Province
  - Faith
  - Great holy war
  - Combat side
  - Scheme
  - Council task
  - Color
  - War
  - Casus belli
  - Combat
  - Story cycle
  - Faction
  - Activity
  - Primitive scopes
<!-- ck3wiki-mod-kb:entry END Scopes list -->

<!-- ck3wiki-mod-kb:entry BEGIN Scripted effects -->
## Scripted effects

- **文件位置**：`pages/Scripted effects.md`
- **来源**：<https://ck3.paradoxwikis.com/Scripted_effects>（oldid 12486，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：把重复 effect 抽成带 $参数$ 替换的宏（scripted effect）时查。
- **中文摘要**：scripted_effects 宏机制：定义、调用与 $ARG$ 文本替换。
- **英文关键词**：Scripted effects
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Scripted effects -->

<!-- ck3wiki-mod-kb:entry BEGIN Triggers list -->
## Triggers list

- **文件位置**：`pages/Triggers list.md`
- **来源**：<https://ck3.paradoxwikis.com/Triggers_list>（oldid 33864，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：快速查某 trigger 的 wiki 版大表（用法/scopes/targets）时查；权威以游戏层 triggers.md 为准。
- **中文摘要**：triggers.log 的 wiki 转录大表（偏旧）；优先用游戏层 dump。
- **英文关键词**：Triggers list；trigger；scopes
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Triggers list -->

<!-- ck3wiki-mod-kb:entry BEGIN Weight modifier -->
## Weight modifier

- **文件位置**：`pages/Weight modifier.md`
- **来源**：<https://ck3.paradoxwikis.com/Weight_modifier>（oldid 20105，抓取 2026-10-22，页面标注版本 未标注）
- **何时查**：写 weight_modifier/MTTH 块（base+add/factor）或 scripted_modifiers 时查。
- **中文摘要**：权重语法：base 与按序列应用的 add/factor modifier、scripted_modifiers 两形态。
- **英文关键词**：Weight modifier；base；add；factor；MTTH；Syntax
- **章节**：
  - Syntax
  - scripted_modifiers — Simple form / Complex form
  - References
<!-- ck3wiki-mod-kb:entry END Weight modifier -->

<!-- ck3wiki-mod-kb:entry BEGIN Modding -->
## Modding

- **文件位置**：`pages/Modding.md`
- **来源**：<https://ck3.paradoxwikis.com/Modding>（oldid 36869，抓取 2026-10-22，页面标注版本 timeless）
- **何时查**：起步/上传创意工坊/加载顺序与 override 规则/存档编辑等总入口时查。
- **中文摘要**：modding 总入口：起步指引、上传更新、手动安装、load order/override 规则、排障与工具。
- **英文关键词**：Modding；load order；override；workshop；Tips & guidelines；Creating a mod
- **章节**：
  - Tips & guidelines — Must know / File reloading / Text editor and tools / Logs / Other tips / Localization Files / Launch options
  - Creating a mod
  - Uploading/updating a mod
  - Installing mods manually — Installing Forum mods / Installing Paradox Mods
  - Extracting files From Microsoft Store version
  - Mod load order
  - Override rules — Full file override / Single object override / Defines / On_actions / Localization / UI types / Common issues
  - Troubleshooting — A mod from Paradox Mods is broken / The mod you uploaded to Steam doesn't work / Mods stopped working / Mods are conflicting
  - Tools & utilities
  - Save game editing — Contents of the gamestate file
  - Mods with wiki pages
  - External links
<!-- ck3wiki-mod-kb:entry END Modding -->

<!-- ck3wiki-mod-kb:entry BEGIN Achievement -->
## Achievement

- **文件位置**：`pages/Achievement.md`（章节索引）＋ 章节目录 `pages/Achievement/`
- **来源**：<https://ck3.paradoxwikis.com/Achievement>（oldid 37349，抓取 2026-10-23，页面标注版本 1.9）
- **何时查**：查原版成就清单（按 DLC 分组）或做成就解锁相关内容前了解其形态时查。
- **中文摘要**：原版成就全清单：本体与 Northern Lords 至 By God Alone 各 DLC 分组。
- **英文关键词**：Achievement；List of achievements；References
- **章节**：
  - List of achievements（`01-List-of-achievements.md`）
    - Base game
    - Northern Lords
    - Royal Court
    - Fate of Iberia
    - Tours and Tournaments
    - Legacy of Persia
    - Legend of the Dead
    - Roads to Power
    - Khans of the Steppe
    - All Under Heaven
    - By God Alone
  - References（`02-References.md`）
<!-- ck3wiki-mod-kb:entry END Achievement -->

<!-- ck3wiki-mod-kb:entry BEGIN Activity -->
## Activity

- **文件位置**：`pages/Activity.md`（章节索引）＋ 章节目录 `pages/Activity/`
- **来源**：<https://ck3.paradoxwikis.com/Activity>（oldid 37341，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改/新建活动前了解原版 regular/grand activities、cost 与 intents 形态时查。
- **中文摘要**：活动参考：cost、常规/grand activities 类型与 Intents 机制。
- **英文关键词**：Activity；Cost；Regular activities；Grand activities；Intents；References
- **章节**：
  - Cost（`01-Cost.md`）
  - Regular activities（`02-Regular-activities.md`）
    - University Visit
    - Examinations
    - Funeral
    - Camp Revelry
    - Coronation
    - Blót
    - Chariot Race
  - Grand activities（`03-Grand-activities.md`）
    - Grand Tournament
  - Intents（`04-Intents.md`）
  - References（`05-References.md`）
<!-- ck3wiki-mod-kb:entry END Activity -->

<!-- ck3wiki-mod-kb:entry BEGIN Adventurer -->
## Adventurer

- **文件位置**：`pages/Adventurer.md`
- **来源**：<https://ck3.paradoxwikis.com/Adventurer>（oldid 37359，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：做无地冒险者内容前了解 adventurer 营地、契约与落户机制形态时查。
- **中文摘要**：冒险者玩法：成为条件、Patrons、Adventurer armies、营地与契约、购置领地。
- **英文关键词**：Adventurer；Becoming an Adventurer；Roll of Patrons；Adventurer armies；Visiting holdings；Gathering provisions
- **章节**：
  - Becoming an Adventurer
  - Roll of Patrons
  - Adventurer armies
  - Visiting holdings
  - Gathering provisions
  - Camp purpose
  - Camp temperament
  - Contracts — Regular contracts / Justicar contracts / Transport contracts / Criminal contracts / Contracts for the contractor / Contracts against the contractor / Treasure Map / Legitimist Support
  - Becoming landed — Purchasing land
  - References
<!-- ck3wiki-mod-kb:entry END Adventurer -->

<!-- ck3wiki-mod-kb:entry BEGIN All Under Heaven -->
## All Under Heaven

- **文件位置**：`pages/All Under Heaven.md`
- **来源**：<https://ck3.paradoxwikis.com/All_Under_Heaven>（oldid 37046，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 All Under Heaven DLC 功能清单或做中华主题内容前了解其范围时查。
- **中文摘要**：DLC 介绍页：天命玩法 Key Features 与 Dev diaries 链接。
- **英文关键词**：All Under Heaven；DLC features；Dev diaries；References
- **章节**：
  - DLC features — Claim the Mandate of Heaven / Key Features
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END All Under Heaven -->

<!-- ck3wiki-mod-kb:entry BEGIN Alliance -->
## Alliance

- **文件位置**：`pages/Alliance.md`
- **来源**：<https://ck3.paradoxwikis.com/Alliance>（oldid 37277，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改联盟/参战机制前了解原版 alliance 与 confederations 形态时查。
- **中文摘要**：联盟参考：缔结条件、Joining wars 与 Confederations 机制。
- **英文关键词**：Alliance；Creating an alliance；Joining wars；Confederations；References
- **章节**：
  - Creating an alliance
  - Joining wars
  - Confederations — Elevating confederations
  - References
<!-- ck3wiki-mod-kb:entry END Alliance -->

<!-- ck3wiki-mod-kb:entry BEGIN Army -->
## Army

- **文件位置**：`pages/Army.md`
- **来源**：<https://ck3.paradoxwikis.com/Army>（oldid 37365，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改军队/兵种/补给前了解原版军队构成形态时查；脚本见 Regiments modding。
- **中文摘要**：军队参考：stats/rally/reinforce、Men-at-Arms 分类、supply 与特殊兵种。
- **英文关键词**：Army；Stats；Rallying and Disbanding Armies；Reinforcing Armies；Quality；Commander
- **章节**：
  - Stats — Damage dealing
  - Rallying and Disbanding Armies
  - Reinforcing Armies
  - Quality
  - Commander
  - Knights
  - Basic soldiers
  - Men-at-Arms — Title Men-at-Arms / Regular / Traditional / Regional / Cultural / Dynastic / Siege weapons / Retinue / Outcasts / Nomadic
  - Supply — Supply limit
  - Attrition
  - Special soldiers
  - References
<!-- ck3wiki-mod-kb:entry END Army -->

<!-- ck3wiki-mod-kb:entry BEGIN Artifacts -->
## Artifacts

- **文件位置**：`pages/Artifacts.md`（章节索引）＋ 章节目录 `pages/Artifacts/`
- **来源**：<https://ck3.paradoxwikis.com/Artifacts>（oldid 37362，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改/新建 artifact 前了解原版稀有度、获取与改进形态时查；脚本见 Artifact modding。
- **中文摘要**：宝物参考：Rarity、创造途径、历史宝物/圣物清单与 Dynasty banners。
- **英文关键词**：Artifacts；Rarity；Creating artifacts；Sanctifying artifacts；Historical artifacts；Holy relics
- **章节**：
  - Rarity（`01-Rarity.md`）
  - Creating artifacts（`02-Creating-artifacts.md`）
    - Hunt trophies
    - Inspirations
    - Travels journal
    - Icons
  - Sanctifying artifacts（`03-Sanctifying-artifacts.md`）
  - Historical artifacts（`04-Historical-artifacts.md`）
    - Byzantine artifacts
    - Holy Roman artifacts
    - Shia artifacts
    - Pagan Kingdom artifacts
    - Hegemony of China artifacts
    - Swords of El Cid
    - Bells of Santiago
    - The Double-Moon Tome
    - Adventure artifacts
    - Coronation artifacts
    - Easter egg artifacts
  - Holy relics（`05-Holy-relics.md`）
    - Adventure holy relics
  - Dynasty banners（`06-Dynasty-banners.md`）
  - Mummification artifacts（`07-Mummification-artifacts.md`）
  - Travel itineraries（`08-Travel-itineraries.md`）
  - Paizas（`09-Paizas.md`）
  - Talismans（`10-Talismans.md`）
  - Cranial trophies（`11-Cranial-trophies.md`）
  - Holy Myron（`12-Holy-Myron.md`）
  - Improving artifacts（`13-Improving-artifacts.md`）
    - Courtier improves artifact
    - Grand Tournament Artisan improves artifact
  - References（`14-References.md`）
<!-- ck3wiki-mod-kb:entry END Artifacts -->

<!-- ck3wiki-mod-kb:entry BEGIN Attributes -->
## Attributes

- **文件位置**：`pages/Attributes.md`（章节索引）＋ 章节目录 `pages/Attributes/`
- **来源**：<https://ck3.paradoxwikis.com/Attributes>（oldid 37258，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改角色属性前了解原版各属性（skills、dread、stress 等）形态时查；脚本见 Characters modding。
- **中文摘要**：角色属性参考：Age/Skills/Dread/Stress/Legitimacy 等约 20 项。
- **英文关键词**：Attributes；Age；Skills；Candidate Score；Domain；Dread
- **章节**：
  - Age（`01-Age.md`）
  - Skills（`02-Skills.md`）
    - Value thresholds
  - Candidate Score（`03-Candidate-Score.md`）
  - Domain（`04-Domain.md`）
  - Dread（`05-Dread.md`）
    - Intimidation and terror
    - Natural dread
  - Education（`06-Education.md`）
    - Point modifiers
    - Education roll calculations
    - Prowess trait
  - Fertility（`07-Fertility.md`）
    - Pregnancy and Complications
    - Disease resistance (fertility)
  - Governor efficiency（`08-Governor-efficiency.md`）
  - Health（`09-Health.md`）
    - Health boosts and penalties
  - Known languages（`10-Known-languages.md`）
  - Legitimacy（`11-Legitimacy.md`）
    - Nomadic legitimacy
    - Mandala legitimacy
  - Mandala Radiance（`12-Mandala-Radiance.md`）
  - Merit（`13-Merit.md`）
    - Merit Rank
  - Movement Power（`14-Movement-Power.md`）
  - Obedience（`15-Obedience.md`）
  - Stress（`16-Stress.md`）
    - Mental Breaks
  - Spiritual fulfillment（`17-Spiritual-fulfillment.md`）
  - Personal tenet slots（`18-Personal-tenet-slots.md`）
  - Weight（`19-Weight.md`）
  - References（`20-References.md`）
<!-- ck3wiki-mod-kb:entry END Attributes -->

<!-- ck3wiki-mod-kb:entry BEGIN Tenet -->
## Tenet

- **文件位置**：`pages/Tenet.md`（章节索引）＋ 章节目录 `pages/Tenet/`
- **来源**：<https://ck3.paradoxwikis.com/Tenet>（oldid 37301，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改信仰 tenet 前了解原版分类与状态形态时查；脚本见 Religions modding。
- **中文摘要**：Tenet 参考：common/restricted tenets、Syncretism 与 popularity。
- **英文关键词**：Tenet；Tenet status；Common tenets；Restricted tenets；Syncretism；Tenet popularity
- **章节**：
  - Tenet status（`01-Tenet-status.md`）
  - Common tenets（`02-Common-tenets.md`）
  - Restricted tenets（`03-Restricted-tenets.md`）
    - Religion-specific tenets
  - Syncretism（`04-Syncretism.md`）
  - Tenet popularity（`05-Tenet-popularity.md`）
  - References（`06-References.md`）
<!-- ck3wiki-mod-kb:entry END Tenet -->

<!-- ck3wiki-mod-kb:entry BEGIN Barony -->
## Barony

- **文件位置**：`pages/Barony.md`
- **来源**：<https://ck3.paradoxwikis.com/Barony>（oldid 37108，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改男爵领/地产前了解原版 holdings 与 terrain、winter、plagues 影响形态时查；脚本见 Holdings modding。
- **中文摘要**：男爵领参考：capital、holdings 分类、terrain/winter/plagues 影响。
- **英文关键词**：Barony；Capital；Holdings；Terrain；Winter；Plagues
- **章节**：
  - Capital
  - Holdings — Castle / City / Temple / Tribe / Temple Citadel / Nomadic Settlement / Herder Pens / Razing holdings
  - Terrain
  - Winter
  - Plagues — Character infection chance
  - References
<!-- ck3wiki-mod-kb:entry END Barony -->

<!-- ck3wiki-mod-kb:entry BEGIN Bookmarks -->
## Bookmarks

- **文件位置**：`pages/Bookmarks.md`（章节索引）＋ 章节目录 `pages/Bookmarks/`
- **来源**：<https://ck3.paradoxwikis.com/Bookmarks>（oldid 35952，抓取 2026-10-23，页面标注版本 1.19）
- **何时查**：做开局剧本前了解原版 867/1066/1178 推荐角色形态时查；脚本见 Bookmarks modding。
- **中文摘要**：开局参考：867/1066/1178 三档 start date 的推荐角色与场景。
- **英文关键词**：Bookmarks；867 start date；1066 start date；1178 start date
- **章节**：
  - 867 start date（`01-867-start-date.md`）
    - The Iranian Intermezzo
    - The Struggle for Iberia
    - Wrath of The Northmen
    - Humble Beginnings
    - The Carolingians
    - Living Gods on Earth
    - Autumn of Virtue
  - 1066 start date（`02-1066-start-date.md`）
    - The Fate of England
    - Rags to Riches
    - Iberia in Pieces
    - The Wandering Exiles
    - At the Gates
    - Song of Splendor
    - A Never-Waning Moon
  - 1178 start date（`03-1178-start-date.md`）
    - Call of the Empire
    - Sword of Faith
    - The Endless Sky
    - Heaven in Turmoil
    - Rise of the Bushi
<!-- ck3wiki-mod-kb:entry END Bookmarks -->

<!-- ck3wiki-mod-kb:entry BEGIN Building -->
## Building

- **文件位置**：`pages/Building.md`
- **来源**：<https://ck3.paradoxwikis.com/Building>（oldid 36514，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改建筑前了解原版建筑分类与地形表形态时查；脚本见 Holdings modding。
- **中文摘要**：建筑参考：construction、经济/军事/特殊等类型与 terrain chart。
- **英文关键词**：Building；Construction；Types of buildings；Terrain chart；References
- **章节**：
  - Construction
  - Types of buildings — Economic buildings / Military buildings / Fortification buildings / Temple buildings / Temple Citadel buildings / Tribe buildings / County buildings / Duchy buildings / Special buildings / City buildings / Oath buildings
  - Terrain chart
  - References
<!-- ck3wiki-mod-kb:entry END Building -->

<!-- ck3wiki-mod-kb:entry BEGIN By God Alone -->
## By God Alone

- **文件位置**：`pages/By God Alone.md`
- **来源**：<https://ck3.paradoxwikis.com/By_God_Alone>（oldid 36840，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 By God Alone DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：信仰主题 Key Features 与 Dev diaries 链接。
- **英文关键词**：By God Alone；DLC features；References
- **章节**：
  - DLC features — Key Features
  - References
<!-- ck3wiki-mod-kb:entry END By God Alone -->

<!-- ck3wiki-mod-kb:entry BEGIN CK3AGOT -->
## CK3AGOT

- **文件位置**：`pages/CK3AGOT.md`（章节索引）＋ 章节目录 `pages/CK3AGOT/`
- **来源**：<https://ck3.paradoxwikis.com/CK3AGOT>（oldid 27940，抓取 2026-10-23，页面标注版本 1.12.5）
- **何时查**：查冰火 total conversion mod CK3AGOT 概况与子 wiki 入口时查。
- **中文摘要**：CK3AGOT 门户：子 wiki 入口、bookmarks、features 与 patches。
- **英文关键词**：CK3AGOT；Latest news；About this mod；Important pages；Want to help improve the CK3AGOT subwiki?；Bookmarks
- **章节**：
  - Latest news（`01-Latest-news.md`）
  - About this mod（`02-About-this-mod.md`）
  - Important pages（`03-Important-pages.md`）
  - Want to help improve the CK3AGOT subwiki?（`04-Want-to-help-improve-the-CK3AGOT-subwiki.md`）
  - Bookmarks（`05-Bookmarks.md`）
    - Robert's Rebellion
    - Crowned Stag
    - War of the Ninepenny Kings
  - Features（`06-Features.md`）
    - Mega Wars
    - Kingsguard
    - Expanded Councilors
    - Knights and Squires
    - The Night’s Watch & Beyond The Wall
    - Deeper Roleplay
    - Armors, Crowns, Artifacts, and Swords
    - More Cultures & Religions
    - Spy Networks
    - An Enormous Map
    - A Meticulously Detailed Map
    - Roads, Roads, Roads
    - And so much more…
  - Patches（`07-Patches.md`）
<!-- ck3wiki-mod-kb:entry END CK3AGOT -->

<!-- ck3wiki-mod-kb:entry BEGIN Casus belli -->
## Casus belli

- **文件位置**：`pages/Casus belli.md`
- **来源**：<https://ck3.paradoxwikis.com/Casus_belli>（oldid 37036，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改战争/CB 前了解原版 casus belli 全类型形态时查。
- **中文摘要**：CB 参考：独立/宣称/征服/De Jure/圣战等全类型战争及变体。
- **英文关键词**：Casus belli；Independence wars；Claims wars；Conquest wars；De Jure wars；Subjugate wars
- **章节**：
  - Independence wars
  - Claims wars
  - Conquest wars — Struggle Clash / Adventurer Invasion wars / Other Conquest CBs
  - De Jure wars
  - Subjugate wars — Forced Vassalization
  - Holy wars
  - Artifact wars
  - Humiliation wars
  - Bring Under Tribute — Retaliation War
  - Eradicate Rival House
  - Excommunication War — Dissolve Empire
  - Challenge Head of Faith
  - Depose Challenger Head of Faith
  - Raid for Captives
  - Rescue House Members
  - Unify The House
  - Migrate to Pannonia
  - Raid wars
  - Varangian Adventure
  - Install Loyalist
  - Raze Capital Temple Complex
  - Plunder for Contribution
  - Enforce Administrative Integration
  - Consolidate Land Under Heaven
  - Investiture Conflict
  - Decision wars
  - References
<!-- ck3wiki-mod-kb:entry END Casus belli -->

<!-- ck3wiki-mod-kb:entry BEGIN Character -->
## Character

- **文件位置**：`pages/Character.md`
- **来源**：<https://ck3.paradoxwikis.com/Character>（oldid 37343，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改角色系统前了解原版角色构成（opinion、关系、AI personality）形态时查；脚本见 Characters modding。
- **中文摘要**：角色参考：appearance、性取向、opinion 分类、AI Personality。
- **英文关键词**：Character；Appearance；Sexual Orientation；Opinion；Relationships；Diplomatic range
- **章节**：
  - Appearance
  - Sexual Orientation
  - Opinion — General opinion / Attraction opinion / Vassal opinion / Predecessor / Child Opinion / Courtier Opinion / Same Dynasty / Virtue & Sins / Faith Hostility / Tyranny
  - Relationships
  - Diplomatic range
  - Nicknames
  - AI Personality — Economic Archetype
  - Legends — Historical legend seeds / Legitimizing historical seeds / Decision legend seeds
  - Puppets
<!-- ck3wiki-mod-kb:entry END Character -->

<!-- ck3wiki-mod-kb:entry BEGIN Coronations -->
## Coronations

- **文件位置**：`pages/Coronations.md`
- **来源**：<https://ck3.paradoxwikis.com/Coronations>（oldid 33057，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Coronations DLC（加冕主题）功能清单时查。
- **中文摘要**：Coronations DLC 介绍：Kneel for the Crowning、Key Features。
- **英文关键词**：Coronations；DLC features；Dev diaries；References
- **章节**：
  - DLC features — Kneel for the Crowning / Key Features
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Coronations -->

<!-- ck3wiki-mod-kb:entry BEGIN Council -->
## Council

- **文件位置**：`pages/Council.md`
- **来源**：<https://ck3.paradoxwikis.com/Council>（oldid 36988，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改议会/廷臣前了解原版 council 构成形态时查；脚本见 Council modding。
- **中文摘要**：议会参考：Spymaster、regular council、Kurultai 与中华式 council。
- **英文关键词**：Council；Spymaster；Confidant；Regular council；Kurultai；Hegemony of China council
- **章节**：
  - Spymaster
  - Confidant
  - Regular council — Chancellor / Steward / Marshal / Religious affairs councilor
  - Kurultai
  - Hegemony of China council — Departments / Ministries
  - Benefits from being a councilor
  - References
<!-- ck3wiki-mod-kb:entry END Council -->

<!-- ck3wiki-mod-kb:entry BEGIN County -->
## County

- **文件位置**：`pages/County.md`
- **来源**：<https://ck3.paradoxwikis.com/County>（oldid 37276，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改伯爵领机制前了解原版 popular opinion、control、development 形态时查。
- **中文摘要**：伯爵领参考：popular opinion、control、development、corruption 等。
- **英文关键词**：County；Popular opinion；Control；Development；Corruption；County Fertility
- **章节**：
  - Popular opinion
  - Control
  - Development — Development growth / Sources of development growth:
  - Corruption — Fomented Revolts
  - County Fertility
  - Siberian permafrost
  - References
<!-- ck3wiki-mod-kb:entry END County -->

<!-- ck3wiki-mod-kb:entry BEGIN Court -->
## Court

- **文件位置**：`pages/Court.md`（章节索引）＋ 章节目录 `pages/Court/`
- **来源**：<https://ck3.paradoxwikis.com/Court>（oldid 37354，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：做宫廷相关内容前了解原版 courtiers、guests 与 court positions 形态时查。
- **中文摘要**：宫廷参考：courtiers、guests 与 court positions（aptitude）机制。
- **英文关键词**：Court；Courtiers and followers；Guests；Court positions；References
- **章节**：
  - Courtiers and followers（`01-Courtiers-and-followers.md`）
    - Hostages
  - Guests（`02-Guests.md`）
  - Court positions（`03-Court-positions.md`）
    - Aptitude
    - Recruit for a Court Position
    - Common positions
    - Ruler positions
    - Officers
  - References（`04-References.md`）
<!-- ck3wiki-mod-kb:entry END Court -->

<!-- ck3wiki-mod-kb:entry BEGIN Crusader Kings III -->
## Crusader Kings III

- **文件位置**：`pages/Crusader Kings III.md`
- **来源**：<https://ck3.paradoxwikis.com/Crusader_Kings_III>（oldid 24009，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查游戏本体特性总览或新手入门导航时查。
- **中文摘要**：游戏主页面：Game features 概览、videos 与 Dev diaries 索引。
- **英文关键词**：Crusader Kings III；Game features；Videos；Dev diaries；References
- **章节**：
  - Game features
  - Videos — Cinematic trailers / Video diaries / Tutorials
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Crusader Kings III -->

<!-- ck3wiki-mod-kb:entry BEGIN Culture -->
## Culture

- **文件位置**：`pages/Culture.md`（章节索引）＋ 章节目录 `pages/Culture/`
- **来源**：<https://ck3.paradoxwikis.com/Culture>（oldid 37145，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改文化前了解原版文化体系（head、pillars、hybrid 等）形态时查；脚本见 Culture modding。
- **中文摘要**：文化参考：culture head、pillars、hybrid/divergent 文化与全文化清单。
- **英文关键词**：Culture；Culture head；Cultural acceptance；Cultural pillars；Traditions；New cultures
- **章节**：
  - Culture head（`01-Culture-head.md`）
  - Cultural acceptance（`02-Cultural-acceptance.md`）
  - Cultural pillars（`03-Cultural-pillars.md`）
    - Ethos
  - Traditions（`04-Traditions.md`）
  - New cultures（`05-New-cultures.md`）
    - Hybrid cultures
    - Divergent cultures
  - List of cultures（`06-List-of-cultures.md`）
    - Nomadic cultures
    - North Germanic cultures
    - Ancient cultures
  - List of unique formable cultures（`07-List-of-unique-formable-cultures.md`）
    - Unique divergent cultures
    - Unique hybrid cultures
  - Culture splits（`08-Culture-splits.md`）
  - Sicilian melting pot（`09-Sicilian-melting-pot.md`）
  - Harrying of the North（`10-Harrying-of-the-North.md`）
  - References（`11-References.md`）
<!-- ck3wiki-mod-kb:entry END Culture -->

<!-- ck3wiki-mod-kb:entry BEGIN Downloadable content -->
## Downloadable content

- **文件位置**：`pages/Downloadable content.md`
- **来源**：<https://ck3.paradoxwikis.com/Downloadable_content>（oldid 34452，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 DLC 清单/版本归属或 DLC 的 script codes 前缀时查。
- **中文摘要**：DLC 总表：各版扩展/风味/事件包分类与 DLC 文件名、script codes。
- **英文关键词**：Downloadable content；Base game editions；Major expansions；Core expansions；Flavor packs；Event packs
- **章节**：
  - Base game editions
  - Major expansions
  - Core expansions
  - Flavor packs
  - Event packs
  - Cosmetic packs
  - Music packs
  - File names and script codes
  - References
<!-- ck3wiki-mod-kb:entry END Downloadable content -->

<!-- ck3wiki-mod-kb:entry BEGIN Decisions -->
## Decisions

- **文件位置**：`pages/Decisions.md`
- **来源**：<https://ck3.paradoxwikis.com/Decisions>（oldid 35680，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：了解原版决策三分类概念时查；写法见 Decisions modding。
- **中文摘要**：决策概念页：character/ruler/adventurer decisions 三分类（无逐条清单）。
- **英文关键词**：Decisions
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Decisions -->

<!-- ck3wiki-mod-kb:entry BEGIN Developer diaries -->
## Developer diaries

- **文件位置**：`pages/Developer diaries.md`
- **来源**：<https://ck3.paradoxwikis.com/Developer_diaries>（oldid 37334，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查某机制设计意图的 dev diary 原文（按 DLC/补丁分组）时查。
- **中文摘要**：Dev diary 索引：自 Base game 至 Silk & Silver 各 DLC/补丁分组链接。
- **英文关键词**：Developer diaries；Silk & Silver；By God Alone；All Under Heaven；Coronations；Khans of the Steppe
- **章节**：
  - Silk & Silver
  - By God Alone
  - All Under Heaven
  - Coronations
  - Khans of the Steppe
  - Wandering Nobles
  - Roads to Power
  - Legends of the Dead
  - Legacy of Persia
  - Wards and Wardens
  - Tours and Tournaments
  - Friends and Foes
  - Fate of Iberia
  - Royal Court
  - Northern Lords
  - Post-release patches
  - Base game
  - Console Edition
  - Videos
<!-- ck3wiki-mod-kb:entry END Developer diaries -->

<!-- ck3wiki-mod-kb:entry BEGIN Doctrines -->
## Doctrines

- **文件位置**：`pages/Doctrines.md`（章节索引）＋ 章节目录 `pages/Doctrines/`
- **来源**：<https://ck3.paradoxwikis.com/Doctrines>（oldid 37118，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改信仰 doctrine 前了解原版各分类形态时查；脚本见 Religions modding。
- **中文摘要**：Doctrine 参考：main/marriage/crime/clergy/special 各类清单。
- **英文关键词**：Doctrines；Main doctrines；Religion doctrines；Marriage doctrines；Crime doctrines；Clergy doctrines
- **章节**：
  - Main doctrines（`01-Main-doctrines.md`）
  - Religion doctrines（`02-Religion-doctrines.md`）
  - Marriage doctrines（`03-Marriage-doctrines.md`）
  - Crime doctrines（`04-Crime-doctrines.md`）
  - Clergy doctrines（`05-Clergy-doctrines.md`）
    - Coronation Tradition
  - Special doctrines（`06-Special-doctrines.md`）
  - References（`07-References.md`）
<!-- ck3wiki-mod-kb:entry END Doctrines -->

<!-- ck3wiki-mod-kb:entry BEGIN Domicile -->
## Domicile

- **文件位置**：`pages/Domicile.md`
- **来源**：<https://ck3.paradoxwikis.com/Domicile>（oldid 37142，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改宅邸前了解原版 domicile 各类型形态时查。
- **中文摘要**：宅邸参考：estate、camp、celestial estate 等各类型与概览。
- **英文关键词**：Domicile；References
- **章节**：
  - References
<!-- ck3wiki-mod-kb:entry END Domicile -->

<!-- ck3wiki-mod-kb:entry BEGIN Duel -->
## Duel

- **文件位置**：`pages/Duel.md`
- **来源**：<https://ck3.paradoxwikis.com/Duel>（oldid 36520，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改决斗前了解原版流程与机制形态时查。
- **中文摘要**：决斗参考：发起挑战、mechanics 与 special moves。
- **英文关键词**：Duel；Issuing a challenge；Mechanics；References
- **章节**：
  - Issuing a challenge
  - Mechanics — Special moves
  - References
<!-- ck3wiki-mod-kb:entry END Duel -->

<!-- ck3wiki-mod-kb:entry BEGIN Dynasty -->
## Dynasty

- **文件位置**：`pages/Dynasty.md`
- **来源**：<https://ck3.paradoxwikis.com/Dynasty>（oldid 37137，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改家族前了解原版 houses、renown 与 legacies 形态时查；脚本见 Dynasties modding。
- **中文摘要**：家族参考：houses、disinheriting、renown 与各系 legacy 树。
- **英文关键词**：Dynasty；Houses；Disinheriting；Renown；Opinion modifiers；References
- **章节**：
  - Houses — House head / Dynasty head / Adoption / House relations / Blocs
  - Disinheriting
  - Renown — Level of Splendor / Dynasty legacies / North Germanic legacies / Iberian legacies / Brilliance / Bureaucracy / Nomadic / Virtues / Divine Aspirations / Elegance / Servants of God
  - Opinion modifiers
  - References
<!-- ck3wiki-mod-kb:entry END Dynasty -->

<!-- ck3wiki-mod-kb:entry BEGIN Elder Kings II -->
## Elder Kings II

- **文件位置**：`pages/Elder Kings II.md`
- **来源**：<https://ck3.paradoxwikis.com/Elder_Kings_II>（oldid 23398，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查老滚 total conversion mod Elder Kings II 概况/FAQ 时查。
- **中文摘要**：EK2 mod 门户：设定、2E 440/450 剧本、FAQ 与 troubleshooting。
- **英文关键词**：Elder Kings II；Development；Setting；Playable Scenarios；Team；Frequently Asked Questions
- **章节**：
  - Development — Mod Requirements
  - Setting
  - Playable Scenarios — 2E 440: Warlord Rising / 2E 450: The Interregnum
  - Team
  - Frequently Asked Questions — Does Mod x work with EK2? / Are DLC required to play? / Is EK2 multiplayer compatible? / Will there be more bookmarks? / Will missing features from EK1 be brought back? / Are you taking donations?
  - Troubleshooting
  - Please use the subreddit and our discord to provide feedback, suggestions and/or bug reports.
<!-- ck3wiki-mod-kb:entry END Elder Kings II -->

<!-- ck3wiki-mod-kb:entry BEGIN Events -->
## Events

- **文件位置**：`pages/Events.md`
- **来源**：<https://ck3.paradoxwikis.com/Events>（oldid 19880，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：了解原版事件分类概念时查；写事件见 Event modding。
- **中文摘要**：事件概念页：pulse 与 triggered-only 事件机制简介。
- **英文关键词**：Events
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Events -->

<!-- ck3wiki-mod-kb:entry BEGIN Family (relation) -->
## Family (relation)

- **文件位置**：`pages/Family (relation).md`
- **来源**：<https://ck3.paradoxwikis.com/Family_(relation)>（oldid 34905，抓取 2026-10-23，页面标注版本 1.10）
- **何时查**：做婚姻/遗传/近亲内容前了解原版规则形态时查；trait 定义见 Trait modding。
- **中文摘要**：家庭关系参考：婚姻、incest、congenital trait 遗传与 inbreeding 机制。
- **英文关键词**：Family (relation)；Marriage；Incest；Trait inheritance；Inbreeding；References
- **章节**：
  - Marriage — Polygamy / Marriage acceptance
  - Incest
  - Trait inheritance — Active and inactive traits / Chance of active inheritance / Chance of inactive inheritance / General logic for trait with tiers inheritance / List of congenital traits / List of other inherited traits
  - Inbreeding — Chance of inbreeding / Common ancestors / Inbreeding factor / Effect of Pure-blooded on inbreeding / Traits gained from inbreeding / Inbred / Pure-blooded
  - References
<!-- ck3wiki-mod-kb:entry END Family (relation) -->

<!-- ck3wiki-mod-kb:entry BEGIN Fate of Iberia -->
## Fate of Iberia

- **文件位置**：`pages/Fate of Iberia.md`
- **来源**：<https://ck3.paradoxwikis.com/Fate_of_Iberia>（oldid 33544，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Fate of Iberia DLC 功能清单时查；struggle 脚本见 Struggle modding。
- **中文摘要**：DLC 介绍页：伊比利亚主题 features、videos 与 Dev diaries。
- **英文关键词**：Fate of Iberia；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Videos — Cinematic trailers / Tutorials
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Fate of Iberia -->

<!-- ck3wiki-mod-kb:entry BEGIN Fertility (disambiguation) -->
## Fertility (disambiguation)

- **文件位置**：`pages/Fertility (disambiguation).md`
- **来源**：<https://ck3.paradoxwikis.com/Fertility_(disambiguation)>（oldid 36885，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：区分角色生育率与 County Fertility 两个概念时查。
- **中文摘要**：消歧义页：角色生育率与 County Fertility（游牧领地肥力）。
- **英文关键词**：Fertility (disambiguation)
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Fertility (disambiguation) -->

<!-- ck3wiki-mod-kb:entry BEGIN Lifestyle -->
## Lifestyle

- **文件位置**：`pages/Lifestyle.md`
- **来源**：<https://ck3.paradoxwikis.com/Lifestyle>（oldid 37104，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改生活方式前了解原版 focus 与 perk 树形态时查；脚本见 Lifestyles modding。
- **中文摘要**：Lifestyle 参考：focuses 与 Diplomacy 至 Wandering 各系 perk trees。
- **英文关键词**：Lifestyle；Focuses；Perk trees；References
- **章节**：
  - Focuses — Education focuses
  - Perk trees — Diplomacy / Diplomat / August / Family Hierarch / Martial / Strategist / Overseer / Gallant / Stewardship / Avaricious / Architect / Administrator / Intrigue / Schemer / Seducer / Torturer / Learning / Whole of Body / Scholar / Theologian / Wandering / Inspector / Wayfarer / Voyager
  - References
<!-- ck3wiki-mod-kb:entry END Lifestyle -->

<!-- ck3wiki-mod-kb:entry BEGIN Form of address -->
## Form of address

- **文件位置**：`pages/Form of address.md`
- **来源**：<https://ck3.paradoxwikis.com/Form_of_address>（oldid 35069，抓取 2026-10-23，页面标注版本 1.18）
- **何时查**：查统治者称谓表或 unique governments 称谓时查；本地化写法见 Localization。
- **中文摘要**：称谓参考：各国统治者称谓表与 unique governments 特殊称谓。
- **英文关键词**：Form of address；Unique Governments；See also；References
- **章节**：
  - Form of address
  - Unique Governments
  - See also
  - References
<!-- ck3wiki-mod-kb:entry END Form of address -->

<!-- ck3wiki-mod-kb:entry BEGIN Friends and Foes -->
## Friends and Foes

- **文件位置**：`pages/Friends and Foes.md`
- **来源**：<https://ck3.paradoxwikis.com/Friends_and_Foes>（oldid 24007，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Friends and Foes DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：友情/敌对主题 features、videos 与 Dev diaries。
- **英文关键词**：Friends and Foes；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Videos — Cinematic trailers
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Friends and Foes -->

<!-- ck3wiki-mod-kb:entry BEGIN Game rules -->
## Game rules

- **文件位置**：`pages/Game rules.md`
- **来源**：<https://ck3.paradoxwikis.com/Game_rules>（oldid 36445，抓取 2026-10-23，页面标注版本 1.9.X）
- **何时查**：改游戏规则前了解原版 game rules（difficulty、ironman 等）形态时查。
- **中文摘要**：游戏规则参考：difficulty、gameplay options 与 ironman。
- **英文关键词**：Game rules；Difficulty；Gameplay options；Ironman mode；References
- **章节**：
  - Difficulty
  - Gameplay options — Historical events / Conquerors / Situations / Extra Administrative Realms / Extra Nomadic Region
  - Ironman mode
  - References
<!-- ck3wiki-mod-kb:entry END Game rules -->

<!-- ck3wiki-mod-kb:entry BEGIN Government -->
## Government

- **文件位置**：`pages/Government.md`
- **来源**：<https://ck3.paradoxwikis.com/Government>（oldid 37119，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改政体前了解原版各 government 类型形态时查；脚本见 Governments modding。
- **中文摘要**：政体参考：tribal/feudal/clan/mandala 等类型与 non-dynastic 政体。
- **英文关键词**：Government；Landed governments；Non-dynastic governments；References
- **章节**：
  - Landed governments — Tribal / Feudal / Clan / Tax Jurisdictions / House unity / Theocratic / Mandala / Mandala Aspect / Wanua
  - Non-dynastic governments
  - References
<!-- ck3wiki-mod-kb:entry END Government -->

<!-- ck3wiki-mod-kb:entry BEGIN Great projects -->
## Great projects

- **文件位置**：`pages/Great projects.md`
- **来源**：<https://ck3.paradoxwikis.com/Great_projects>（oldid 37165，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改大型工程前了解原版 great projects 形态时查。
- **中文摘要**：Great projects 参考：Grand Cathedral、Mass Conversion 等工程条目。
- **英文关键词**：Great projects；Mass Conversion；Grand Cathedral；Develop Communities；Capital Temple Complex；Hegemony of China great projects
- **章节**：
  - Mass Conversion
  - Grand Cathedral
  - Develop Communities
  - Capital Temple Complex
  - Hegemony of China great projects
<!-- ck3wiki-mod-kb:entry END Great projects -->

<!-- ck3wiki-mod-kb:entry BEGIN Hired forces -->
## Hired forces

- **文件位置**：`pages/Hired forces.md`
- **来源**：<https://ck3.paradoxwikis.com/Hired_forces>（oldid 36467，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改佣兵/骑士团前了解原版形态时查。
- **中文摘要**：佣兵与骑士团参考：mercenaries 机制与 military orders 创建、清单。
- **英文关键词**：Hired forces；Mercenaries；Military orders；References
- **章节**：
  - Mercenaries
  - Military orders — Creating military orders / Patronage / Members / List of military orders / Starting military orders
  - References
<!-- ck3wiki-mod-kb:entry END Hired forces -->

<!-- ck3wiki-mod-kb:entry BEGIN Holy sites -->
## Holy sites

- **文件位置**：`pages/Holy sites.md`（章节索引）＋ 章节目录 `pages/Holy sites/`
- **来源**：<https://ck3.paradoxwikis.com/Holy_sites>（oldid 37248，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改圣地前了解原版圣地状态与创建形态时查；脚本见 Religions modding。
- **中文摘要**：圣地参考：Enshrined Relics、holy site status、创建机制与全圣地清单。
- **英文关键词**：Holy sites；Enshrined Relics；Holy site status；Creating holy sites；List of holy sites
- **章节**：
  - Enshrined Relics（`01-Enshrined-Relics.md`）
  - Holy site status（`02-Holy-site-status.md`）
  - Creating holy sites（`03-Creating-holy-sites.md`）
  - List of holy sites（`04-List-of-holy-sites.md`）
<!-- ck3wiki-mod-kb:entry END Holy sites -->

<!-- ck3wiki-mod-kb:entry BEGIN Hooks -->
## Hooks

- **文件位置**：`pages/Hooks.md`
- **来源**：<https://ck3.paradoxwikis.com/Hooks>（oldid 36442，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改把柄/秘密前了解原版 hook 分级形态时查。
- **中文摘要**：Hook 参考：weak/perpetual/strong hooks、用途限制与 secrets。
- **英文关键词**：Hooks；Weak hooks；Perpetual hooks；Strong hooks；Spending hooks；Secrets
- **章节**：
  - Weak hooks
  - Perpetual hooks
  - Strong hooks
  - Spending hooks — What hooks can't do
  - Secrets
  - References
<!-- ck3wiki-mod-kb:entry END Hooks -->

<!-- ck3wiki-mod-kb:entry BEGIN Innovation -->
## Innovation

- **文件位置**：`pages/Innovation.md`
- **来源**：<https://ck3.paradoxwikis.com/Innovation>（oldid 37366，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改科技前了解原版 innovation 分时代分类形态时查。
- **中文摘要**：创新参考：四个 eras 与 military/civic/regional 等 innovation 分类。
- **英文关键词**：Innovation；Eras；Tribal innovations；Early Medieval innovations；High Medieval innovations；Late Medieval innovations
- **章节**：
  - Eras
  - Tribal innovations — Military innovations / Civic innovations / Regional innovations / Cultural innovations / Silk Road innovations
  - Early Medieval innovations — Military innovations / Civic innovations / Regional innovations / Mural Sextant / Silk Road innovations
  - High Medieval innovations — Military innovations / Civic innovations / Regional innovations / Fritware / Cultural innovations
  - Late Medieval innovations — Military innovations / Civic innovations / Regional innovations / Cultural innovations
  - References
<!-- ck3wiki-mod-kb:entry END Innovation -->

<!-- ck3wiki-mod-kb:entry BEGIN Interactions -->
## Interactions

- **文件位置**：`pages/Interactions.md`（章节索引）＋ 章节目录 `pages/Interactions/`
- **来源**：<https://ck3.paradoxwikis.com/Interactions>（oldid 36911，抓取 2026-10-23，页面标注版本 1.4）
- **何时查**：查原版各互动（diplomacy/personal/hostile 等）清单形态时查；脚本见 Interactions modding。
- **中文摘要**：互动参考：diplomacy/personal/hostile/vassal 等八类 interaction 清单。
- **英文关键词**：Interactions；Diplomacy actions；Personal actions；Hostile actions；Appointment Actions；Vassal actions
- **章节**：
  - Diplomacy actions（`01-Diplomacy-actions.md`）
    - War-related actions
    - Forming Alliances
    - Marriages & Concubines
    - Legitimize Bastard
    - Demand Payment
    - Buy Claim
    - Request Claim
  - Personal actions（`02-Personal-actions.md`）
    - Send Gift
    - Sway
    - Befriend
    - Seduce
    - Romance
    - Elope
    - Educate Child
    - Offer Ward
    - Offer Guardianship
    - Influence Ward's Personality
    - Ward's Martial Drill
    - Host as Honored Guest
    - Send Poem
    - Challenge to Boardgame
    - Make Shieldmaiden
    - Abandon Hook
  - Hostile actions（`03-Hostile-actions.md`）
    - Disinherit
    - Blackmail
    - Murder
    - Abduct
    - Claim Throne
    - Fabricate Hook
    - Dismiss hook
    - Excommunicate
    - Request Excommunication
    - Challenge Rival to Fight
    - Punish Criminal
    - Release your Anger
    - Trial-by-Combat
  - Appointment Actions（`04-Appointment-Actions.md`）
    - Influence Candidacy
    - Ask to Influence Candidacy
    - Expand Power Base
    - Slander
    - Promote
    - Retire Governor
    - Request Retirement
    - Force Retirement
  - Vassal actions（`05-Vassal-actions.md`）
    - Grant Landed Title
    - Offer Vassalage
    - Swear Fealty
    - Grant Independence
    - Grant Vassal
    - Retract Vassal
    - Factions
    - Stop Vassal War
    - Demand Council Position
    - Ask for Pardon
    - Grant Pardon
    - Petition Liege
    - Pay Homage
  - Courtier Actions（`06-Courtier-Actions.md`）
    - Ask to Take Vows
  - Imprisonment actions（`07-Imprisonment-actions.md`）
    - Negotiate Release
    - Execute
    - Ransom
    - Pay Ransom
    - Ransom Yourself
    - Move to House Arrest
    - Move to Dungeon
  - Religious actions（`08-Religious-actions.md`）
    - Demand Conversion
    - Adopt Faith
    - Seek Indulgences
    - Make Declaration of Repentance
    - Lift Excommunication
    - Condemn Sins
    - Ask for Gold
    - Literalist Debate
    - Designate Sacrifice
    - Refute Sacrifice
<!-- ck3wiki-mod-kb:entry END Interactions -->

<!-- ck3wiki-mod-kb:entry BEGIN Interesting characters -->
## Interesting characters

- **文件位置**：`pages/Interesting characters.md`（章节索引）＋ 章节目录 `pages/Interesting characters/`
- **来源**：<https://ck3.paradoxwikis.com/Interesting_characters>（oldid 35740，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：选/设计开局角色前查各 start date 推荐人物时查。
- **中文摘要**：推荐角色清单：867/1066/1178 各开局按信仰分组的 interesting characters。
- **英文关键词**：Interesting characters；Christian characters；Muslim characters；Jewish characters；Dualist characters；Pagan characters
- **章节**：
  - Christian characters（`01-Christian-characters.md`）
    - Catholic
    - Orthodox
    - Apostolic
    - Insular
    - Coptic
    - Nestorian
  - Muslim characters（`02-Muslim-characters.md`）
    - Ash'ari
    - Ibadi
    - Maturidi
    - Mu'tazili
    - Muwalladi
    - Zayidi
    - Isma'ili
    - Azariqa
  - Jewish characters（`03-Jewish-characters.md`）
    - Haymanot
    - Kuzarite
    - Rabbinic
  - Dualist characters（`04-Dualist-characters.md`）
    - Manichean
  - Pagan characters（`05-Pagan-characters.md`）
    - Ásatrú
    - Akom
    - Bidaic
    - Bori
    - Donyi-Poloist
    - Kiratist
    - Kushite
    - Melie
    - Orisan
    - Roogan
    - Sedist
    - Shintō
    - Siguic
    - Slovianskan
    - Táltosist
    - Tengri
    - Turumic
    - Ukonusko
    - Vidilist
    - Waaqi
    - Yumaist
    - Achamánic
    - Khyarwé Bönpo
    - Muist
    - Ezo
  - Eastern religions（`06-Eastern-religions.md`）
    - Buddhist
    - Hindu
    - Jain
    - Taoist
    - Confucian
  - Landless Adventurers（`07-Landless-Adventurers.md`）
  - Unlanded characters（`08-Unlanded-characters.md`）
  - Legends of Crusader Kings III（`09-Legends-of-Crusader-Kings-III.md`）
  - Christian characters（`01-Christian-characters.md`）
    - Catholic
    - Orthodox
    - Apostolic
    - Insular
    - Mozarabic
  - Muslim characters（`02-Muslim-characters.md`）
    - Ash'ari
    - Isma'ili
    - Druze
    - Maturidi
    - Muwalladi
  - Pagan characters（`05-Pagan-characters.md`）
    - Ásatrú
    - Bidaic
    - Slovianskan
    - Ukonusko
    - Shinto
  - Eastern religions（`06-Eastern-religions.md`）
    - Buddhist
    - Hindu - Shaivism
  - Landless Adventurers（`07-Landless-Adventurers.md`）
  - Unlanded characters（`08-Unlanded-characters.md`）
  - Christian characters（`01-Christian-characters.md`）
    - Catholic
    - Orthodox
    - Apostolic
    - Nestorian
  - Muslim characters（`02-Muslim-characters.md`）
    - Ash'ari
    - Maturidi
    - Isma'ili
    - Nizari
  - Buddhist Characters（`18-Buddhist-Characters.md`）
    - Mahayana
    - Theravada
  - Hindu Characters（`19-Hindu-Characters.md`）
    - Shaivism
  - Pagan characters（`05-Pagan-characters.md`）
    - Slovianskan
    - Tengri
  - Landless Adventurers（`07-Landless-Adventurers.md`）
  - Unlanded characters（`08-Unlanded-characters.md`）
<!-- ck3wiki-mod-kb:entry END Interesting characters -->

<!-- ck3wiki-mod-kb:entry BEGIN Jargon -->
## Jargon

- **文件位置**：`pages/Jargon.md`
- **来源**：<https://ck3.paradoxwikis.com/Jargon>（oldid 36758，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：读 wiki/社区帖遇术语或 DLC 缩写不明时查。
- **中文摘要**：术语缩写表：游戏术语与 DLC 的英文缩写对照。
- **英文关键词**：Jargon；The Acronyms；DLC Acronyms
- **章节**：
  - The Acronyms
  - DLC Acronyms
<!-- ck3wiki-mod-kb:entry END Jargon -->

<!-- ck3wiki-mod-kb:entry BEGIN Khans of the Steppe -->
## Khans of the Steppe

- **文件位置**：`pages/Khans of the Steppe.md`
- **来源**：<https://ck3.paradoxwikis.com/Khans_of_the_Steppe>（oldid 37047，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Khans of the Steppe DLC（游牧主题）功能清单时查。
- **中文摘要**：DLC 介绍页：Rule the Steppe、Key Features、videos、Dev diaries。
- **英文关键词**：Khans of the Steppe；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features — Rule the Steppe / Key Features
  - Videos — Cinematic trailers
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Khans of the Steppe -->

<!-- ck3wiki-mod-kb:entry BEGIN Kingdom of Heaven -->
## Kingdom of Heaven

- **文件位置**：`pages/Kingdom of Heaven.md`
- **来源**：<https://ck3.paradoxwikis.com/Kingdom_of_Heaven>（oldid 13709，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查 total conversion mod Kingdom of Heaven 概况时查。
- **中文摘要**：mod 门户：Total Conversion 类型、作者与 Features 简介。
- **英文关键词**：Kingdom of Heaven；Features
- **章节**：
  - Features
<!-- ck3wiki-mod-kb:entry END Kingdom of Heaven -->

<!-- ck3wiki-mod-kb:entry BEGIN Kinslayer (disambiguation) -->
## Kinslayer (disambiguation)

- **文件位置**：`pages/Kinslayer (disambiguation).md`
- **来源**：<https://ck3.paradoxwikis.com/Kinslayer_(disambiguation)>（oldid 6510，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：区分各 Kinslayer trait 与 Kinslaying doctrine 时查。
- **中文摘要**：消歧义页：三个 Kinslayer trait 与 Kinslaying doctrine。
- **英文关键词**：Kinslayer (disambiguation)
- **章节**：
  - （无章节结构）
<!-- ck3wiki-mod-kb:entry END Kinslayer (disambiguation) -->

<!-- ck3wiki-mod-kb:entry BEGIN Knight -->
## Knight

- **文件位置**：`pages/Knight.md`
- **来源**：<https://ck3.paradoxwikis.com/Knight>（oldid 36532，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改骑士前了解原版 knight 与 accolades 形态时查。
- **中文摘要**：骑士参考：任命、战斗表现、文化别名与 Accolades。
- **英文关键词**：Knight；Cultural alternatives；Appointment；Combat performance；Number of Knights；Accolades
- **章节**：
  - Cultural alternatives
  - Appointment
  - Combat performance
  - Number of Knights
  - Accolades — Rank / Accolade attributes / Retinue attributes
  - References
<!-- ck3wiki-mod-kb:entry END Knight -->

<!-- ck3wiki-mod-kb:entry BEGIN Laws -->
## Laws

- **文件位置**：`pages/Laws.md`
- **来源**：<https://ck3.paradoxwikis.com/Laws>（oldid 37112，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改法律前了解原版 law 类型形态时查。
- **中文摘要**：法律参考：Administrative/Celestial laws、Imperial Policy 等。
- **英文关键词**：Laws；Borders Wars Policy；Administrative laws；Celestial laws；Imperial Policy；Coronation
- **章节**：
  - Borders Wars Policy
  - Administrative laws
  - Celestial laws — Hegemony of China laws
  - Imperial Policy
  - Coronation
  - Cardinal Benefices
  - References
<!-- ck3wiki-mod-kb:entry END Laws -->

<!-- ck3wiki-mod-kb:entry BEGIN Legacy of Persia -->
## Legacy of Persia

- **文件位置**：`pages/Legacy of Persia.md`
- **来源**：<https://ck3.paradoxwikis.com/Legacy_of_Persia>（oldid 37050，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Legacy of Persia DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：波斯主题 features、videos 与 Dev diaries。
- **英文关键词**：Legacy of Persia；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Videos — Cinematic trailers / Tutorials
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Legacy of Persia -->

<!-- ck3wiki-mod-kb:entry BEGIN Legends of the Dead -->
## Legends of the Dead

- **文件位置**：`pages/Legends of the Dead.md`
- **来源**：<https://ck3.paradoxwikis.com/Legends_of_the_Dead>（oldid 37042，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Legends of the Dead DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：legends 与 plague 主题 features、Dev diaries。
- **英文关键词**：Legends of the Dead；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Videos — Cinematic trailers / Tutorials
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Legends of the Dead -->

<!-- ck3wiki-mod-kb:entry BEGIN LotR: Realms in Exile -->
## LotR: Realms in Exile

- **文件位置**：`pages/LotR_ Realms in Exile.md`
- **来源**：<https://ck3.paradoxwikis.com/LotR:_Realms_in_Exile>（oldid 34810，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查魔戒 mod LotR: Realms in Exile 概况/FAQ 时查。
- **中文摘要**：mod 门户：FAQ、About、Important Pages 与贡献指引。
- **英文关键词**：LotR: Realms in Exile；!!FAQ!!；About；Important Pages；Want to contribute?
- **章节**：
  - !!FAQ!! — This FAQ was taken from the Discord.
  - About
  - Important Pages
  - Want to contribute?
<!-- ck3wiki-mod-kb:entry END LotR: Realms in Exile -->

<!-- ck3wiki-mod-kb:entry BEGIN Mechanics -->
## Mechanics

- **文件位置**：`pages/Mechanics.md`
- **来源**：<https://ck3.paradoxwikis.com/Mechanics>（oldid 37022，抓取 2026-10-23，页面标注版本 1.4）
- **何时查**：按分类找某玩法的机制页入口时查。
- **中文摘要**：机制导航页：按 Characters/Realm/Warfare 等分类的机制链接表。
- **英文关键词**：Mechanics；Characters；Realm & Governance；Warfare；Culture & Religion；Meta
- **章节**：
  - Characters
  - Realm & Governance
  - Warfare
  - Culture & Religion
  - Meta
<!-- ck3wiki-mod-kb:entry END Mechanics -->

<!-- ck3wiki-mod-kb:entry BEGIN Medieval Arts -->
## Medieval Arts

- **文件位置**：`pages/Medieval Arts.md`（章节索引）＋ 章节目录 `pages/Medieval Arts/`
- **来源**：<https://ck3.paradoxwikis.com/Medieval_Arts>（oldid 32564，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查原版 special buildings 与地图物件清单时查。
- **中文摘要**：美术参考：special buildings 清单与 map objects、unique cities。
- **英文关键词**：Medieval Arts；Special buildings；Map objects
- **章节**：
  - Special buildings（`01-Special-buildings.md`）
    - Upgradable Special buildings
  - Map objects（`02-Map-objects.md`）
    - For base game Special buildings
    - Unique cities
<!-- ck3wiki-mod-kb:entry END Medieval Arts -->

<!-- ck3wiki-mod-kb:entry BEGIN Modifiers -->
## Modifiers

- **文件位置**：`pages/Modifiers.md`
- **来源**：<https://ck3.paradoxwikis.com/Modifiers>（oldid 37348，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查原版 permanent/temporary modifier 形态时查；可用签名以游戏层 modifiers 为准。
- **中文摘要**：Modifier 参考：permanent/temporary 各作用域清单与 pets 等来源。
- **英文关键词**：Modifiers；Permanent dynasty modifiers；Permanent house modifiers；Permanent county modifiers；Permanent character modifiers；Temporary dynasty modifiers
- **章节**：
  - Permanent dynasty modifiers
  - Permanent house modifiers
  - Permanent county modifiers
  - Permanent character modifiers — Historical character modifiers / Decision modifiers / Personal Deity / Patron Saint / Designated Terrain / Honorary titles / Warhorse / Miraculous Tonic / Wise woman modifiers
  - Temporary dynasty modifiers
  - Temporary house modifiers — House unity modifiers
  - Pets
  - Court poet modifiers
  - Experimental Brew
  - Blood Brother modifiers
  - Coronation modifiers
  - Capital Temple Complex modifiers
  - Aspect modifiers
  - Puppet modifiers
  - References
<!-- ck3wiki-mod-kb:entry END Modifiers -->

<!-- ck3wiki-mod-kb:entry BEGIN Nickname -->
## Nickname

- **文件位置**：`pages/Nickname.md`（章节索引）＋ 章节目录 `pages/Nickname/`
- **来源**：<https://ck3.paradoxwikis.com/Nickname>（oldid 35899，抓取 2026-10-23，页面标注版本 1.4）
- **何时查**：改称号前了解原版 nickname 获取分类形态时查。
- **中文摘要**：Nickname 参考：可获取/历史/未用称号清单与 Nickname ID。
- **英文关键词**：Nickname；List of obtainable nicknames；Unobtainable nicknames；List of historical nicknames；List of unused nicknames；Nickname ID
- **章节**：
  - List of obtainable nicknames（`01-List-of-obtainable-nicknames.md`）
    - Obtained from Decisions
    - Obtained from Events
    - Obtained from Traits and Stats
    - Obtainable Nicknames from other sources
  - Unobtainable nicknames（`02-Unobtainable-nicknames.md`）
  - List of historical nicknames（`03-List-of-historical-nicknames.md`）
  - List of unused nicknames（`04-List-of-unused-nicknames.md`）
  - Nickname ID（`05-Nickname-ID.md`）
  - References（`06-References.md`）
<!-- ck3wiki-mod-kb:entry END Nickname -->

<!-- ck3wiki-mod-kb:entry BEGIN Nightmare in Britain -->
## Nightmare in Britain

- **文件位置**：`pages/Nightmare in Britain.md`
- **来源**：<https://ck3.paradoxwikis.com/Nightmare_in_Britain>（oldid 26078，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查 mod Nightmare in Britain 世界观设定时查。
- **中文摘要**：mod 设定页：后启示录英国 2147 年世界观（Imperial Commonwealth 等）。
- **英文关键词**：Nightmare in Britain；Setting and Lore
- **章节**：
  - Setting and Lore — The Pre-War Era of *Nightmare in Britain* / Formation of the Imperial Commonwealth / A Revolution of Culture and Industry / Notable Successor States / **The United Kingdom of Great Britain** / **The Strethling Terror and the Wall of Westminster** / **The "Concession" of Power and the Situation of the United Kingdom by 2147** / Post-War Society / Technology / The Outside World
<!-- ck3wiki-mod-kb:entry END Nightmare in Britain -->

<!-- ck3wiki-mod-kb:entry BEGIN Northern Lords -->
## Northern Lords

- **文件位置**：`pages/Northern Lords.md`
- **来源**：<https://ck3.paradoxwikis.com/Northern_Lords>（oldid 33543，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Northern Lords DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：北欧风味 DLC/patch features、videos、Dev diaries。
- **英文关键词**：Northern Lords；DLC features；Patch features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Patch features
  - Videos — Cinematic trailers / Video diaries
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Northern Lords -->

<!-- ck3wiki-mod-kb:entry BEGIN Power sharing -->
## Power sharing

- **文件位置**：`pages/Power sharing.md`
- **来源**：<https://ck3.paradoxwikis.com/Power_sharing>（oldid 36719，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改摄政/权力共享前了解原版机制形态时查。
- **中文摘要**：Power sharing 参考：Regency、Vizierate、Duumvirate 等权力共享机制。
- **英文关键词**：Power sharing；Mandates；Loyalty；Scales of Power ​；Regency；Entrenched Regency and Co-Monarchy
- **章节**：
  - Mandates
  - Loyalty
  - Scales of Power ​
  - Regency
  - Entrenched Regency and Co-Monarchy
  - Vizierate
  - Duumvirate — Nominal Duumvirate
  - Grand Secretariat
<!-- ck3wiki-mod-kb:entry END Power sharing -->

<!-- ck3wiki-mod-kb:entry BEGIN Prisoner -->
## Prisoner

- **文件位置**：`pages/Prisoner.md`
- **来源**：<https://ck3.paradoxwikis.com/Prisoner>（oldid 36542，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改囚禁前了解原版囚犯与刑罚形态时查。
- **中文摘要**：囚犯参考：prisoner value、监禁效果、release/ransom 与 punishment。
- **英文关键词**：Prisoner；Prisoner value；Imprisonment effects；Negotiate release；Ransom；Punishment
- **章节**：
  - Prisoner value
  - Imprisonment effects
  - Negotiate release
  - Ransom
  - Punishment — Execution / Torture / Tradition punishments / Sun trial
  - Crime — Familial crimes / Religious crimes
  - References
<!-- ck3wiki-mod-kb:entry END Prisoner -->

<!-- ck3wiki-mod-kb:entry BEGIN Traits -->
## Traits

- **文件位置**：`pages/Traits.md`（章节索引）＋ 章节目录 `pages/Traits/`
- **来源**：<https://ck3.paradoxwikis.com/Traits>（oldid 37335，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：新建/修改 trait 前了解原版 trait 的分类、等级与效果形态时查；脚本字段见 Trait modding。
- **中文摘要**：特质参考：原版 16 类 trait 清单（personality/congenital/health 等）。
- **英文关键词**：Traits；Personality traits；Education traits；Congenital traits；Physical traits；Leveled traits
- **章节**：
  - Personality traits（`01-Personality-traits.md`）
  - Education traits（`02-Education-traits.md`）
  - Congenital traits（`03-Congenital-traits.md`）
    - Leveled congenital traits
  - Physical traits（`04-Physical-traits.md`）
  - Leveled traits（`05-Leveled-traits.md`）
    - Commander traits
    - Adventurer traits
  - Lifestyle traits（`06-Lifestyle-traits.md`）
  - Infamy traits（`07-Infamy-traits.md`）
  - Coping mechanisms（`08-Coping-mechanisms.md`）
  - Childhood traits（`09-Childhood-traits.md`）
  - Health traits（`10-Health-traits.md`）
    - Wounds
    - Diseases
    - Old age traits
    - Incapable
  - Dynasty traits（`11-Dynasty-traits.md`）
    - Descendant traits
  - Decision traits（`12-Decision-traits.md`）
  - Faith traits（`13-Faith-traits.md`）
  - Event traits（`14-Event-traits.md`）
  - Court type traits（`15-Court-type-traits.md`）
  - Immortal（`16-Immortal.md`）
  - References（`17-References.md`）
<!-- ck3wiki-mod-kb:entry END Traits -->

<!-- ck3wiki-mod-kb:entry BEGIN Rajas of Asia -->
## Rajas of Asia

- **文件位置**：`pages/Rajas of Asia.md`
- **来源**：<https://ck3.paradoxwikis.com/Rajas_of_Asia>（oldid 26393，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查 total conversion mod Rajas of Asia 概况/功能时查。
- **中文摘要**：mod 门户：地图扩至东亚/东南亚、936 剧本、新政府与 tenets 等功能。
- **英文关键词**：Rajas of Asia；Pages
- **章节**：
  - Pages
<!-- ck3wiki-mod-kb:entry END Rajas of Asia -->

<!-- ck3wiki-mod-kb:entry BEGIN Religion -->
## Religion

- **文件位置**：`pages/Religion.md`
- **来源**：<https://ck3.paradoxwikis.com/Religion>（oldid 37180，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改信仰前了解原版宗教体系形态时查；脚本见 Religions modding。
- **中文摘要**：宗教参考：divergence、fervor、hostility、conversion 与信仰领袖机制。
- **英文关键词**：Religion；Divergence；Fervor；Faith hostility；Faith organization；Virtues and sins
- **章节**：
  - Divergence
  - Fervor — Heresy outbreaks
  - Faith hostility
  - Faith organization
  - Virtues and sins
  - Religion heads — Excommunication / Challenger heads of faith
  - Find an Adherent
  - Conversion
  - New rites — Reformation
  - College of Cardinals
  - Canonization
  - Monastic orders — Creating monastic orders / Interactions
  - Faiths at the start of the game
<!-- ck3wiki-mod-kb:entry END Religion -->

<!-- ck3wiki-mod-kb:entry BEGIN Resources -->
## Resources

- **文件位置**：`pages/Resources.md`
- **来源**：<https://ck3.paradoxwikis.com/Resources>（oldid 37127，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改资源前了解原版 gold/prestige/piety 等形态时查。
- **中文摘要**：资源参考：Gold、Prestige、Piety、Influence、Provisions、Herd 等。
- **英文关键词**：Resources；Gold；Prestige；Piety；Influence；Provisions
- **章节**：
  - Gold — Treasury / Debt
  - Prestige — Level of fame
  - Piety — Level of devotion / Monthly piety / Factors affecting monthly piety
  - Influence — Level of Influence
  - Provisions
  - Herd
  - Barter Goods
  - References
<!-- ck3wiki-mod-kb:entry END Resources -->

<!-- ck3wiki-mod-kb:entry BEGIN Roads to Power -->
## Roads to Power

- **文件位置**：`pages/Roads to Power.md`
- **来源**：<https://ck3.paradoxwikis.com/Roads_to_Power>（oldid 37049，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Roads to Power DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：行政政府与无地冒险者主题 features、Dev diaries。
- **英文关键词**：Roads to Power；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Videos — Cinematic trailers
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Roads to Power -->

<!-- ck3wiki-mod-kb:entry BEGIN Royal Court (DLC) -->
## Royal Court (DLC)

- **文件位置**：`pages/Royal Court (DLC).md`
- **来源**：<https://ck3.paradoxwikis.com/Royal_Court_(DLC)>（oldid 33541，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Royal Court DLC 功能清单时查；机制详见 Royal court 页。
- **中文摘要**：DLC 介绍页：宫廷主题 features、videos 与 Dev diaries。
- **英文关键词**：Royal Court (DLC)；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Videos — Cinematic trailers / Video diaries / Tutorials
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Royal Court (DLC) -->

<!-- ck3wiki-mod-kb:entry BEGIN Royal court -->
## Royal court

- **文件位置**：`pages/Royal court.md`
- **来源**：<https://ck3.paradoxwikis.com/Royal_court>（oldid 37267，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改宫廷机制前了解原版 court type、amenities、grandeur 形态时查。
- **中文摘要**：宫廷机制：court type、court language、amenities 与 grandeur。
- **英文关键词**：Royal court；DLC mechanics；References
- **章节**：
  - DLC mechanics — Court type / Tribal court / Nomadic court / Court language / Court amenities / Sumptuary debate / Court grandeur / Expectations
  - References
<!-- ck3wiki-mod-kb:entry END Royal court -->

<!-- ck3wiki-mod-kb:entry BEGIN Ruler Designer -->
## Ruler Designer

- **文件位置**：`pages/Ruler Designer.md`
- **来源**：<https://ck3.paradoxwikis.com/Ruler_Designer>（oldid 36991，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查捏人器功能或做自定义统治者内容参考时查。
- **中文摘要**：Ruler Designer 参考：特征、attributes、appearance 与注意事项。
- **英文关键词**：Ruler Designer；Essential Characteristics；Attributes；Appearance；Notes
- **章节**：
  - Essential Characteristics
  - Attributes — Age and Weight / Traits / Skills / Family
  - Appearance — Basic Customization / Further Customization
  - Notes
<!-- ck3wiki-mod-kb:entry END Ruler Designer -->

<!-- ck3wiki-mod-kb:entry BEGIN Schemes -->
## Schemes

- **文件位置**：`pages/Schemes.md`
- **来源**：<https://ck3.paradoxwikis.com/Schemes>（oldid 37344，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改计谋前了解原版 scheme 分类与 agents 形态时查。
- **中文摘要**：计谋参考：hostile/personal/political/mandala schemes 与 agents。
- **英文关键词**：Schemes；Scheme mechanics；Hostile schemes；Personal schemes；Political schemes；Mandala schemes
- **章节**：
  - Scheme mechanics
  - Hostile schemes
  - Personal schemes
  - Political schemes
  - Mandala schemes
  - Agents — Swaying Agents / Agent Personality / Scheme potential agents / Administrative agents / Phase length agents / Secrecy agents
  - Countermeasure focus
  - References
<!-- ck3wiki-mod-kb:entry END Schemes -->

<!-- ck3wiki-mod-kb:entry BEGIN Situation -->
## Situation

- **文件位置**：`pages/Situation.md`（章节索引）＋ 章节目录 `pages/Situation/`
- **来源**：<https://ck3.paradoxwikis.com/Situation>（oldid 37298，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改情境前了解原版 situation 实例形态时查。
- **中文摘要**：Situation 参考：natural disasters、Silk Road 等原版情境实例。
- **英文关键词**：Situation；Natural disasters；Dynastic Cycle；The Silk Road；Steppe seasons；The Christian Church
- **章节**：
  - Natural disasters（`01-Natural-disasters.md`）
    - Earthquake
    - Flood
  - Dynastic Cycle（`02-Dynastic-Cycle.md`）
    - Eras
    - Division
    - Political movements
  - The Silk Road（`03-The-Silk-Road.md`）
  - Steppe seasons（`04-Steppe-seasons.md`）
  - The Christian Church（`05-The-Christian-Church.md`）
    - Before Great Schism
    - After the Great Schism
  - References（`06-References.md`）
<!-- ck3wiki-mod-kb:entry END Situation -->

<!-- ck3wiki-mod-kb:entry BEGIN Subjects -->
## Subjects

- **文件位置**：`pages/Subjects.md`
- **来源**：<https://ck3.paradoxwikis.com/Subjects>（oldid 36525，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改封臣/朝贡前了解原版 vassal/tributary 形态时查。
- **中文摘要**：臣属参考：vassal contracts/factions、tributaries 与 lessees。
- **英文关键词**：Subjects；Vassals；Tributaries；Lessees；References
- **章节**：
  - Vassals — Vassal limit / Vassal directives / Powerful vassals / Vassal stances / Vassal contracts / Rights / Special contract / Obligations / Base obligations / Factions / Civil wars / Vassal factions / Popular factions
  - Tributaries — Pay tribute / Hegemonic tributaries / Tributaries of China
  - Lessees — Subordinates
  - References
<!-- ck3wiki-mod-kb:entry END Subjects -->

<!-- ck3wiki-mod-kb:entry BEGIN Succession -->
## Succession

- **文件位置**：`pages/Succession.md`
- **来源**：<https://ck3.paradoxwikis.com/Succession>（oldid 35670，抓取 2026-10-23，页面标注版本 1.10）
- **何时查**：改继承前了解原版 succession 类型形态时查。
- **中文摘要**：继承参考：单嗣/多嗣各型 succession、claim 继承与 abdication。
- **英文关键词**：Succession；Heirs；Eligibility；Realm succession；Title succession；Title claim inheritance
- **章节**：
  - Heirs
  - Eligibility
  - Realm succession — Single heir / Primogeniture / Ultimogeniture / House seniority / Multiple heirs / (Regular) partition / Confederate partition / High partition
  - Title succession
  - Title claim inheritance
  - Other forms of inheritance
  - Abdication
  - Notes
  - Tips
  - References
<!-- ck3wiki-mod-kb:entry END Succession -->

<!-- ck3wiki-mod-kb:entry BEGIN The Fallen Eagle -->
## The Fallen Eagle

- **文件位置**：`pages/The Fallen Eagle.md`
- **来源**：<https://ck3.paradoxwikis.com/The_Fallen_Eagle>（oldid 29517，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查 total conversion mod The Fallen Eagle 概况时查。
- **中文摘要**：mod 门户：361/395/476/532 剧本与古典时代晚期重制内容。
- **英文关键词**：The Fallen Eagle；Pages
- **章节**：
  - Pages
<!-- ck3wiki-mod-kb:entry END The Fallen Eagle -->

<!-- ck3wiki-mod-kb:entry BEGIN Titles -->
## Titles

- **文件位置**：`pages/Titles.md`
- **来源**：<https://ck3.paradoxwikis.com/Titles>（oldid 37353，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改头衔前了解原版 rank、de jure、claim 形态时查；脚本见 Title modding。
- **中文摘要**：头衔参考：rank、De Jure/usurpation/drift、claim、revocation。
- **英文关键词**：Titles；Title rank；De Jure；Claim；Revocation；Holding too many titles
- **章节**：
  - Title rank — Duchy
  - De Jure — Usurpation / De jure drift
  - Claim
  - Revocation
  - Holding too many titles
  - Empire titles restricted by organized faith
  - Head of faith titles
  - Roman Empire
  - Beseeching titles
  - References
<!-- ck3wiki-mod-kb:entry END Titles -->

<!-- ck3wiki-mod-kb:entry BEGIN Tours and Tournaments -->
## Tours and Tournaments

- **文件位置**：`pages/Tours and Tournaments.md`
- **来源**：<https://ck3.paradoxwikis.com/Tours_and_Tournaments>（oldid 33546，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Tours and Tournaments DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：tour/tournament 主题 features、videos、Dev diaries。
- **英文关键词**：Tours and Tournaments；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Videos — Cinematic trailers / Video diaries / Tutorials
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Tours and Tournaments -->

<!-- ck3wiki-mod-kb:entry BEGIN Traditions -->
## Traditions

- **文件位置**：`pages/Traditions.md`（章节索引）＋ 章节目录 `pages/Traditions/`
- **来源**：<https://ck3.paradoxwikis.com/Traditions>（oldid 37292，抓取 2026-10-23，页面标注版本 1.18）
- **何时查**：改传统前了解原版 tradition 分类与建立机制形态时查；脚本见 Culture modding。
- **中文摘要**：传统参考：effects/建立机制与 realm、warfare 等六类 tradition 清单。
- **英文关键词**：Traditions；Effects；Requirements；Establishment；Realm traditions；Warfare traditions
- **章节**：
  - Effects（`01-Effects.md`）
  - Requirements（`02-Requirements.md`）
    - Prestige Cost
  - Establishment（`03-Establishment.md`）
    - Cooldown
  - Realm traditions（`04-Realm-traditions.md`）
  - Warfare traditions（`05-Warfare-traditions.md`）
  - Social traditions（`06-Social-traditions.md`）
  - Ritual traditions（`07-Ritual-traditions.md`）
  - Regional traditions（`08-Regional-traditions.md`）
  - Parameters（`09-Parameters.md`）
  - References（`10-References.md`）
<!-- ck3wiki-mod-kb:entry END Traditions -->

<!-- ck3wiki-mod-kb:entry BEGIN Travel -->
## Travel

- **文件位置**：`pages/Travel.md`
- **来源**：<https://ck3.paradoxwikis.com/Travel>（oldid 36519，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改旅行前了解原版 travel 机制形态时查。
- **中文摘要**：旅行参考：mechanics、points of interest 与 travel options。
- **英文关键词**：Travel；Mechanics；Points of interest；Travel options；References
- **章节**：
  - Mechanics
  - Points of interest — Battles sites
  - Travel options — Ruler travel options / Adventurer travel options
  - References
<!-- ck3wiki-mod-kb:entry END Travel -->

<!-- ck3wiki-mod-kb:entry BEGIN Wandering Nobles -->
## Wandering Nobles

- **文件位置**：`pages/Wandering Nobles.md`
- **来源**：<https://ck3.paradoxwikis.com/Wandering_Nobles>（oldid 30304，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Wandering Nobles DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：旅行主题 features 与 Dev diaries 链接。
- **英文关键词**：Wandering Nobles；DLC features；Dev diaries；References
- **章节**：
  - DLC features
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Wandering Nobles -->

<!-- ck3wiki-mod-kb:entry BEGIN Wards and Wardens -->
## Wards and Wardens

- **文件位置**：`pages/Wards and Wardens.md`
- **来源**：<https://ck3.paradoxwikis.com/Wards_and_Wardens>（oldid 24008，抓取 2026-10-23，页面标注版本 timeless）
- **何时查**：查 Wards and Wardens DLC 功能清单时查。
- **中文摘要**：DLC 介绍页：教育与童年主题 features、videos、Dev diaries。
- **英文关键词**：Wards and Wardens；DLC features；Videos；Dev diaries；References
- **章节**：
  - DLC features
  - Videos — Cinematic trailers
  - Dev diaries
  - References
<!-- ck3wiki-mod-kb:entry END Wards and Wardens -->

<!-- ck3wiki-mod-kb:entry BEGIN Warfare -->
## Warfare

- **文件位置**：`pages/Warfare.md`
- **来源**：<https://ck3.paradoxwikis.com/Warfare>（oldid 37159，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：改战争机制前了解原版 battles、war score、GHW 形态时查；CB 类型见 Casus belli。
- **中文摘要**：战争参考：battles/siege、war score、great holy wars 与 raiding。
- **英文关键词**：Warfare；Battles；War score；Holy wars；Raiding；Capturing characters in a holding
- **章节**：
  - Battles — Combat phases / The advantage modifier / Capturing commanders / Siege / Siege progress / Siege statistics / Prestige and fame gain on victory
  - War score — Ending the war / War contribution
  - Holy wars — Great holy wars / Directed great holy wars / Undirected great holy wars / Unlocking great holy wars / Great Holy War Weights
  - Raiding
  - Capturing characters in a holding
  - Initial wars
  - Truce
  - References
<!-- ck3wiki-mod-kb:entry END Warfare -->

<!-- ck3wiki-mod-kb:entry BEGIN Way of Kings -->
## Way of Kings

- **文件位置**：`pages/Way of Kings.md`
- **来源**：<https://ck3.paradoxwikis.com/Way_of_Kings>（oldid 24022，抓取 2026-10-23，页面标注版本 未标注）
- **何时查**：查飓光志 mod Way of Kings 设定与机制时查。
- **中文摘要**：mod 门户：Roshar 设定与 Knights Radiant、Surgebinding 等机制。
- **英文关键词**：Way of Kings；Setting；Mechanics
- **章节**：
  - Setting — Geopolitics / Technology / Discrimination / Governments and Electives
  - Mechanics — Artifacts / Investiture / Knights Radiant / Surgebinding / Common thresholds / Squireships / Radiant Innovations and Luminocracy / Tips and tricks / Dungeon Delving / Dueling / Fishing / Shardic Victories / Custom Pilgrimages / Marriage and Consent / Destined Canon Spouses
<!-- ck3wiki-mod-kb:entry END Way of Kings -->

<!-- ck3wiki-mod-kb:entry BEGIN When the World Stopped Making Sense -->
## When the World Stopped Making Sense

- **文件位置**：`pages/When the World Stopped Making Sense.md`
- **来源**：<https://ck3.paradoxwikis.com/When_the_World_Stopped_Making_Sense>（oldid 35956，抓取 2026-10-23，页面标注版本 0.3.0）
- **何时查**：查迁移时代 mod When the World Stopped Making Sense（WtWSMS）功能/兼容性时查。
- **中文摘要**：mod 门户：兼容/安装、新剧本与 religions/cultures/traditions 功能。
- **英文关键词**：When the World Stopped Making Sense；Mod Compatibility；Installation；Features；Developer Diaries；Frequency Asked Questions
- **章节**：
  - Mod Compatibility — Vanilla / Recommended DLC / Mod Compatibility / Sub Mods
  - Installation — Steam Workshop / Paradox Mods / Manual
  - Features — Current Features / New Bookmarks / Religions / Faiths / Tenets / Cultures / Traditions / Other Features / Planned Features
  - Developer Diaries
  - Frequency Asked Questions — Where can I find the latest official version? / Does the mod require any DLC? / Is the mod compatible with all DLCs? / Is the mod compatible with any other mod? / What languages is the mod available in? / How do I migrate?
  - References
<!-- ck3wiki-mod-kb:entry END When the World Stopped Making Sense -->

## 游戏权威层（game_docs，dump > wiki）

<!-- ck3wiki-mod-kb:entry BEGIN game:effects.md -->
## 权威层 effects（全量 effect 签名）

- **文件位置**：`game_docs/script_docs/effects.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/effects.log`，2128 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：写任何 effect 调用前，查权威签名、参数与 Supported Scopes；与 wiki（Effects/Commands/Effects list）冲突时以此为准。
- **中文摘要**：游戏 1.20.0 debug dump 全量 effects 清单，含用法示例与作用域。
- **英文关键词**：effects；Supported Scopes；usage
<!-- ck3wiki-mod-kb:entry END game:effects.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:triggers.md -->
## 权威层 triggers（全量 trigger 签名）

- **文件位置**：`game_docs/script_docs/triggers.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/triggers.log`，1937 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：写任何 trigger/limit 前，查权威签名与 Supported Scopes；与 wiki（Triggers/Triggers list）冲突时以此为准。
- **中文摘要**：全量 triggers 清单：签名、用法与支持作用域。
- **英文关键词**：triggers；Supported Scopes；usage
<!-- ck3wiki-mod-kb:entry END game:triggers.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:event_targets.md -->
## 权威层 event_targets

- **文件位置**：`game_docs/script_docs/event_targets.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/event_targets.log`，328 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查某 scope 下可用的 event target 链（如 father.holder）时；比 wiki Scopes list 权威。
- **中文摘要**：全量 event targets：target 链与来源分组。
- **英文关键词**：event_targets；event target
<!-- ck3wiki-mod-kb:entry END game:event_targets.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:event_scopes.md -->
## 权威层 event_scopes

- **文件位置**：`game_docs/script_docs/event_scopes.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/event_scopes.log`，74 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查全部 scope 类型清单或事件可用 scope 时。
- **中文摘要**：全部 event scope 类型权威清单。
- **英文关键词**：event_scopes；scope
<!-- ck3wiki-mod-kb:entry END game:event_scopes.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:modifiers.md -->
## 权威层 modifiers

- **文件位置**：`game_docs/script_docs/modifiers.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/modifiers.log`，761 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查某 modifier 是否存在及形态时；与 wiki Modifier list 冲突时以此为准。
- **中文摘要**：全量 modifier 清单与用法形态。
- **英文关键词**：modifiers；modifier
<!-- ck3wiki-mod-kb:entry END game:modifiers.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:on_actions.md -->
## 权威层 on_actions

- **文件位置**：`game_docs/script_docs/on_actions.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/on_actions.log`，932 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：要把逻辑挂到 on_action（on_xxx 钩子）或查有哪些可挂钩子时。
- **中文摘要**：全量 on_action 钩子清单与触发说明。
- **英文关键词**：on_actions；on_action
<!-- ck3wiki-mod-kb:entry END game:on_actions.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:custom_localization.md -->
## 权威层 custom_localization

- **文件位置**：`game_docs/script_docs/custom_localization.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/custom_localization.log`，2782 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查原版 customizable_localization 键名与结构时。
- **中文摘要**：全量 custom localization 条目转储。
- **英文关键词**：custom_localization
<!-- ck3wiki-mod-kb:entry END game:custom_localization.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:data_types_common.md -->
## 权威层 data_types（common）

- **文件位置**：`game_docs/script_docs/data_types_common.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/data_types/data_types_common.txt`，368 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查 common 域 data type 的字段/方法签名时。
- **中文摘要**：common 域 data types 权威转储。
- **英文关键词**：data_types；common
<!-- ck3wiki-mod-kb:entry END game:data_types_common.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:data_types_gui.md -->
## 权威层 data_types（gui）

- **文件位置**：`game_docs/script_docs/data_types_gui.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/data_types/data_types_gui.txt`，875 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：写 GUI 时查 gui 域 data type 的字段/方法签名。
- **中文摘要**：gui 域 data types 权威转储。
- **英文关键词**：data_types；gui
<!-- ck3wiki-mod-kb:entry END game:data_types_gui.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:data_types_internalclausewitzgui.md -->
## 权威层 data_types（internal gui）

- **文件位置**：`game_docs/script_docs/data_types_internalclausewitzgui.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/data_types/data_types_internalclausewitzgui.txt`，2479 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查引擎内部 GUI data type（进阶 GUI modding）时。
- **中文摘要**：引擎内部 GUI data types 权威转储。
- **英文关键词**：data_types；internal
<!-- ck3wiki-mod-kb:entry END game:data_types_internalclausewitzgui.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:data_types_script.md -->
## 权威层 data_types（script）

- **文件位置**：`game_docs/script_docs/data_types_script.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/data_types/data_types_script.txt`，670 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查脚本域 data type 的字段/方法签名时。
- **中文摘要**：脚本域 data types 权威转储。
- **英文关键词**：data_types；script
<!-- ck3wiki-mod-kb:entry END game:data_types_script.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:data_types_uncategorized.md -->
## 权威层 data_types（uncategorized）

- **文件位置**：`game_docs/script_docs/data_types_uncategorized.md`
- **来源**：游戏 1.20.1 script_docs dump（`game logs/data_types/data_types_uncategorized.txt`，20227 条，并入 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：前四个 data_types 文件都查不到某类型时，查此未分类兜底清单。
- **中文摘要**：未分类 data types 权威转储（条目最多）。
- **英文关键词**：data_types；uncategorized
<!-- ck3wiki-mod-kb:entry END game:data_types_uncategorized.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:INDEX.md -->
## 原版结构索引 INDEX

- **文件位置**：`game_docs/vanilla_structure/INDEX.md`
- **来源**：游戏 1.20.1 目录扫描（128 个 common 子目录，78167 行条目映射，扫描 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查「某类内容在原版哪些文件、多少条目」或浏览 common 子目录时。
- **中文摘要**：原版结构总索引：128 个 common 子目录的文件/条目计数与查询方式。
- **英文关键词**：vanilla_structure；INDEX
<!-- ck3wiki-mod-kb:entry END game:INDEX.md -->

<!-- ck3wiki-mod-kb:entry BEGIN game:entry_map.tsv -->
## 原版条目定位表 entry_map

- **文件位置**：`game_docs/vanilla_structure/entry_map.tsv`
- **来源**：游戏 1.20.1 目录扫描（128 个 common 子目录，78167 行条目映射，扫描 2026-10-29）
- **权威层**：与 wiki 冲突时以本条目为准（dump 层）
- **何时查**：查「某条目名（trait/definition/…）定义在原版哪个文件哪一行」时。
- **中文摘要**：78167 行 条目名→定义文件/行号 TSV；grep -P "^<条目名>	" 定位。
- **英文关键词**：entry_map；tsv
<!-- ck3wiki-mod-kb:entry END game:entry_map.tsv -->
