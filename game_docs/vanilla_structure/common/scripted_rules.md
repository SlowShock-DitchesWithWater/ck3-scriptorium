# common/scripted_rules 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 3 个）
- 顶层块条目总数：72，跨文件唯一条目 72
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_rules.txt` | 43456 | 66 | 0 | jomini |
| `01_grant_title_rules.txt` | 8410 | 3 | 0 | jomini |
| `02_holy_sites.txt` | 2110 | 3 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_rules.txt（66 条目）

- can_command_troops
- can_command_troops_now
- ghw_give_barony_to_beneficiary
- can_edit_rite
- can_create_rite
- faith_conversion
- rite_conversion
- can_change_faith
- should_mother_give_house_to_bastard
- can_be_knight
- is_character_allowed_to_be_player
- is_secret_available_for_blackmail
- passes_faction_hard_block
- passes_faction_soft_block
- is_dangerous_faction
- is_alliance_valid
- can_designate_heir
- cares_about_powerful_vassal_council_position
- approves_of_succession_law_change
- has_natural_death_second_chance
- can_refund_perks
- can_defensively_join_holy_war
- can_fire_councillor
- can_raid
- can_start_raid
- can_start_bartering
- can_raid_across_water
- can_traverse_river
- is_hard_blocked_from_schemes
- ai_wants_matrilineal_marriage
- ai_wants_grand_wedding_promise
- buildings_enabled
- can_potentially_call_ally
- can_hybridize_culture
- can_diverge_culture
- can_add_tradition
- can_replace_pillar
- can_name_after_birth
- can_adopt_court_language
- ai_should_repair_artifact
- can_be_activity_guest
- is_diarch_visibly_loyal
- is_diarch_visibly_disloyal
- is_diarch_able
- is_diarch_valid
- should_have_diarchy
- can_be_acclaimed_knight
- is_hostage_valid
- can_create_legend
- can_promote_legend
- ai_wants_to_create_own_legend
- is_dominant_family
- is_hireable_ruler_trigger
- can_hire_hireable_ruler_trigger
- can_move_domicile
- is_kurultai_succession_chaotic
- ai_wants_to_migrate
- can_raze
- can_raze_own_holding
- can_create_title
- can_destroy_title
- ai_should_create_title
- ai_should_hire_title_maa
- can_build_in_tributaries
- can_build_in_liege_tributaries
- can_build_in_same_realm

### 01_grant_title_rules.txt（3 条目）

- allowed_to_be_granted_titles_by
- is_grant_government_shown
- is_grant_government_valid

### 02_holy_sites.txt（3 条目）

- can_enshrine_artifact
- can_create_dynamic_holy_site
- can_remove_enshrined_artifact
