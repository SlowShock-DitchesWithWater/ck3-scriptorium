# common/tutorial_lessons 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：10（其中 Jomini 解析 9 个）
- 顶层块条目总数：116，跨文件唯一条目 116
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_ep4_japan_reactive_advice.txt` | 21102 | 4 | 0 | jomini |
| `00_ep4_playtest_intro.txt` | 2638 | 1 | 0 | jomini |
| `00_tutorial_lessons_basics.txt` | 85381 | 17 | 0 | jomini |
| `00_tutorial_lessons_china.txt` | 32614 | 2 | 0 | jomini |
| `00_tutorial_lessons_reactive.txt` | 139455 | 68 | 0 | jomini |
| `00_tutorial_lessons_war.txt` | 16259 | 15 | 0 | jomini |
| `01_ep1_tutorial_lessons_reactive.txt` | 11812 | 3 | 0 | jomini |
| `03_fp2_tutorial_lessons_reactive.txt` | 5578 | 1 | 0 | jomini |
| `07_ep3_tutorial_lessons_reactive.txt` | 18311 | 5 | 0 | jomini |
| `_tutorial_lesson.info` | 5275 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_ep4_japan_reactive_advice.txt（4 条目）

- reactive_advice_welcome_to_japan
- reactive_advice_soryo_intro
- reactive_advice_lead_your_soryo_bloc
- reactive_advice_soryo_regent_become_shogun

### 00_ep4_playtest_intro.txt（1 条目）

- lesson_tgp_playtest_intro_mandala

### 00_tutorial_lessons_basics.txt（17 条目）

- lesson_basics
- lesson_basics_quick_continued
- lesson_basics_map
- lesson_basics_character
- lesson_basics_resources
- lesson_basics_lifestyles
- lesson_basics_interacting
- lesson_basics_succession
- lesson_basics_marriage
- lesson_basics_titles
- lesson_basics_holdings
- lesson_basics_vassals
- lesson_basics_domain
- lesson_basics_council
- lesson_basics_schemes
- lesson_basics_war
- lesson_basics_unpause

### 00_tutorial_lessons_china.txt（2 条目）

- lesson_chain_china_paused
- reactive_advice_china_council

### 00_tutorial_lessons_reactive.txt（68 条目）

- reactive_advice_mercenaries
- reactive_advice_succession
- reactive_advice_domain_limit
- reactive_advice_vassal_limit
- reactive_advice_megaduke_penalty
- reactive_advice_bastards
- reactive_advice_protecting_against_hostile_schemes
- reactive_advice_protect_against_factions
- reactive_advice_imprisoned
- reactive_advice_county_control
- reactive_advice_looming_game_over
- reactive_advice_bankruptcy
- reactive_advice_rightful_liege
- reactive_advice_bishop_endorsement
- reactive_advice_encyclopedia
- reactive_advice_dynamic_culture
- reactive_advice_religion_rites
- reactive_advice_fabricate_claim
- reactive_advice_education
- reactive_advice_tooltip_modes
- reactive_advice_perk_bonus_cap
- reactive_advice_varangian_adventure
- reactive_advice_court_positions
- reactive_advice_artifact_inventory
- reactive_advice_station_maa
- reactive_advice_tours_picking_vassals
- reactive_advice_regency_for_liege
- reactive_advice_regency_for_regent
- reactive_advice_set_future_regent
- reactive_advice_travel_planning
- reactive_advice_create_accolade
- reactive_advice_house_unity
- reactive_advice_tax_collector
- reactive_advice_legitimacy
- reactive_advice_epidemics
- reactive_advice_legends
- reactive_advice_plague_resistance
- reactive_advice_tutorial_schemes
- reactive_advice_tutorial_war
- reactive_advice_lesson_army_movement
- reactive_advice_lesson_army_purpose
- reactive_advice_lesson_battle_mechanics
- reactive_advice_lesson_siege_mechanics
- reactive_advice_lesson_warscore
- reactive_advice_lesson_winning_wars
- reactive_advice_lesson_losing_wars
- reactive_advice_lesson_war_final_notes_victory
- reactive_advice_lesson_war_final_notes_defeat
- reactive_advice_lesson_war_final_notes_white_peace
- reactive_advice_lesson_war_final_notes_invalidated
- reactive_advice_favorite_child
- reactive_advice_army_automation
- reactive_advice_migration
- reactive_advice_great_steppe
- reactive_advice_kurultai
- reactive_advice_tributaries
- reactive_advice_meritocratic_governor
- reactive_advice_treasury
- reactive_advice_dynastic_cycle
- reactive_advice_merit_candidacy
- reactive_advice_great_projects
- reactive_advice_natural_disasters
- reactive_advice_women_in_china
- reactive_advice_christian_situation
- reactive_advice_puppets
- reactive_advice_clerical_regions
- reactive_advice_personal_beliefs
- reactive_advice_ecclesiastical_ruler

### 00_tutorial_lessons_war.txt（15 条目）

- lesson_safety_gating
- lesson_declare_war
- lesson_raise_troops
- lesson_army_movement
- lesson_army_purpose
- lesson_battle_mechanics
- lesson_siege_mechanics
- lesson_warscore
- lesson_winning_wars
- lesson_losing_wars
- lesson_war_final_notes_victory
- lesson_war_final_notes_defeat
- lesson_war_final_notes_white_peace
- lesson_war_final_notes_invalidated
- lesson_guided_final_notes_mission

### 01_ep1_tutorial_lessons_reactive.txt（3 条目）

- reactive_advice_should_form_hybrid_culture
- reactive_advice_royal_court
- reactive_advice_fund_inspiration

### 03_fp2_tutorial_lessons_reactive.txt（1 条目）

- reactive_advice_struggle_introduction

### 07_ep3_tutorial_lessons_reactive.txt（5 条目）

- reactive_advice_landless_adventurer
- reactive_advice_admin_gov
- reactive_advice_admin_gov_troops
- reactive_advice_agent_scheme_rework
- reactive_advice_laamp_contract_move

### 未解析文件

- `_tutorial_lesson.info` — 纯文档（非 Jomini）
