# 原版结构索引（vanilla_structure）总索引

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与内容指纹见 manifest.json 的 game_docs.vanilla_structure）
- 权威顺序：script_docs dump（game_docs/script_docs/）> wiki 层（pages/）> 本结构索引（仅导航）。
- 生成方式：`scripts/vanilla_index.py` 递归扫描，只提取结构信息（路径/文件名/顶层块名/计数/大小），零原版文件内容复制（mod 制作时按索引直接读游戏目录）。

## 查询方式

1. **查某条目（trait/opinion/modifier/... 名）定义在哪个文件**：
   `grep -P "^<条目名>\t" game_docs\vanilla_structure\entry_map.tsv`
   （entry_map.tsv 共 96296 行映射；输出列为 条目名/定义文件/行号，文件路径相对 game\ 根）
2. **浏览某类内容的全部文件与条目**：读 `common/<子目录>.md`（下表）。
3. **events/history/gui/gfx 等其他目录**：读 `other_dirs.md`。

## common\ 子目录摘要（137 个，全覆盖）

| 子目录 | 文件数 | 顶层块条目 | 唯一条目 | 摘要文件 |
|---|---|---|---|---|
| accolade_icons | 2 | 0 | 0 | `common/accolade_icons.md` |
| accolade_names | 2 | 16 | 16 | `common/accolade_names.md` |
| accolade_types | 6 | 31 | 31 | `common/accolade_types.md` |
| achievements | 14 | 218 | 218 | `common/achievements.md` |
| activities | 78 | 498 | 498 | `common/activities.md` |
| ai_goaltypes | 1 | 1 | 1 | `common/ai_goaltypes.md` |
| ai_war_stances | 4 | 7 | 7 | `common/ai_war_stances.md` |
| artifacts | 32 | 1115 | 1074 | `common/artifacts.md` |
| bookmark_portraits | 360 | 359 | 359 | `common/bookmark_portraits.md` |
| bookmarks | 6 | 77 | 77 | `common/bookmarks.md` |
| buildings | 87 | 3548 | 3548 | `common/buildings.md` |
| casus_belli_groups | 2 | 21 | 21 | `common/casus_belli_groups.md` |
| casus_belli_types | 33 | 138 | 138 | `common/casus_belli_types.md` |
| character_backgrounds | 2 | 2 | 2 | `common/character_backgrounds.md` |
| character_interaction_categories | 2 | 16 | 16 | `common/character_interaction_categories.md` |
| character_interactions | 75 | 652 | 652 | `common/character_interactions.md` |
| character_memory_types | 24 | 421 | 421 | `common/character_memory_types.md` |
| coat_of_arms | 25 | 3716 | 3438 | `common/coat_of_arms.md` |
| combat_effects | 2 | 31 | 31 | `common/combat_effects.md` |
| combat_phase_events | 3 | 13 | 13 | `common/combat_phase_events.md` |
| confederation_aspirations | 2 | 7 | 7 | `common/confederation_aspirations.md` |
| confederation_types | 4 | 9 | 9 | `common/confederation_types.md` |
| connection_arrows | 2 | 21 | 21 | `common/connection_arrows.md` |
| console_groups | 2 | 3 | 3 | `common/console_groups.md` |
| council_positions | 3 | 15 | 15 | `common/council_positions.md` |
| council_tasks | 10 | 75 | 75 | `common/council_tasks.md` |
| court_amenities | 2 | 4 | 4 | `common/court_amenities.md` |
| court_positions | 51 | 186 | 186 | `common/court_positions.md` |
| court_types | 2 | 7 | 7 | `common/court_types.md` |
| courtier_guest_management | 3 | 2 | 2 | `common/courtier_guest_management.md` |
| culture | 160 | 2613 | 2611 | `common/culture.md` |
| customizable_localization | 165 | 2993 | 2993 | `common/customizable_localization.md` |
| deathreasons | 5 | 326 | 326 | `common/deathreasons.md` |
| decision_group_types | 2 | 23 | 23 | `common/decision_group_types.md` |
| decisions | 85 | 587 | 587 | `common/decisions.md` |
| defines | 12 | 168 | 149 | `common/defines.md` |
| diarchies | 6 | 17 | 17 | `common/diarchies.md` |
| districts | 12 | 352 | 352 | `common/districts.md` |
| dna_data | 10 | 465 | 465 | `common/dna_data.md` |
| domiciles | 11 | 2919 | 2919 | `common/domiciles.md` |
| dynasties | 11 | 11750 | 11750 | `common/dynasties.md` |
| dynasty_house_motto_inserts | 2 | 23 | 23 | `common/dynasty_house_motto_inserts.md` |
| dynasty_house_mottos | 2 | 74 | 74 | `common/dynasty_house_mottos.md` |
| dynasty_houses | 6 | 712 | 712 | `common/dynasty_houses.md` |
| dynasty_legacies | 12 | 24 | 24 | `common/dynasty_legacies.md` |
| dynasty_perks | 13 | 120 | 120 | `common/dynasty_perks.md` |
| effect_localization | 38 | 1121 | 1121 | `common/effect_localization.md` |
| epidemics | 2 | 7 | 7 | `common/epidemics.md` |
| ethnicities | 25 | 51 | 51 | `common/ethnicities.md` |
| event_2d_effects | 2 | 5 | 5 | `common/event_2d_effects.md` |
| event_backgrounds | 3 | 331 | 331 | `common/event_backgrounds.md` |
| event_themes | 3 | 201 | 201 | `common/event_themes.md` |
| event_transitions | 4 | 33 | 33 | `common/event_transitions.md` |
| factions | 9 | 14 | 14 | `common/factions.md` |
| flavorization | 10 | 1574 | 1574 | `common/flavorization.md` |
| focuses | 4 | 33 | 33 | `common/focuses.md` |
| game_concepts | 19 | 1269 | 1269 | `common/game_concepts.md` |
| game_rules | 3 | 86 | 86 | `common/game_rules.md` |
| genes | 12 | 13 | 6 | `common/genes.md` |
| governments | 4 | 21 | 21 | `common/governments.md` |
| graphical_unit_types | 2 | 9 | 9 | `common/graphical_unit_types.md` |
| great_projects | 6 | 40 | 40 | `common/great_projects.md` |
| guest_system | 2 | 2 | 2 | `common/guest_system.md` |
| holding_sprawl_graphics | 1 | 19 | 19 | `common/holding_sprawl_graphics.md` |
| holding_sprawl_patterns | 1 | 16 | 16 | `common/holding_sprawl_patterns.md` |
| holdings | 2 | 7 | 7 | `common/holdings.md` |
| holy_orders | 4 | 313 | 313 | `common/holy_orders.md` |
| hook_types | 2 | 50 | 50 | `common/hook_types.md` |
| house_aspirations | 6 | 35 | 35 | `common/house_aspirations.md` |
| house_relation_types | 2 | 1 | 1 | `common/house_relation_types.md` |
| house_unities | 2 | 2 | 2 | `common/house_unities.md` |
| important_actions | 39 | 338 | 338 | `common/important_actions.md` |
| inspirations | 2 | 12 | 12 | `common/inspirations.md` |
| landed_titles | 16 | 3475 | 3473 | `common/landed_titles.md` |
| law_groups | 8 | 49 | 49 | `common/law_groups.md` |
| laws | 9 | 283 | 283 | `common/laws.md` |
| lease_contracts | 2 | 2 | 2 | `common/lease_contracts.md` |
| legends | 6 | 74 | 73 | `common/legends.md` |
| legitimacy | 2 | 8 | 8 | `common/legitimacy.md` |
| lifestyle_perks | 19 | 162 | 162 | `common/lifestyle_perks.md` |
| lifestyles | 2 | 6 | 6 | `common/lifestyles.md` |
| men_at_arms_types | 11 | 112 | 112 | `common/men_at_arms_types.md` |
| menu_scenes | 1 | 0 | 0 | `common/menu_scenes.md` |
| message_filter_types | 3 | 210 | 210 | `common/message_filter_types.md` |
| message_group_types | 2 | 33 | 33 | `common/message_group_types.md` |
| messages | 46 | 823 | 823 | `common/messages.md` |
| modifier_definition_formats | 17 | 2851 | 2838 | `common/modifier_definition_formats.md` |
| modifier_icons | 1 | 1 | 1 | `common/modifier_icons.md` |
| modifiers | 153 | 7539 | 7539 | `common/modifiers.md` |
| morpheme_strip_rules | 3 | 6 | 6 | `common/morpheme_strip_rules.md` |
| named_colors | 3 | 3 | 1 | `common/named_colors.md` |
| nicknames | 13 | 787 | 787 | `common/nicknames.md` |
| on_action | 194 | 1073 | 1061 | `common/on_action.md` |
| opinion_modifiers | 81 | 1704 | 1704 | `common/opinion_modifiers.md` |
| playable_difficulty_infos | 2 | 14 | 14 | `common/playable_difficulty_infos.md` |
| pool_character_selectors | 7 | 12 | 12 | `common/pool_character_selectors.md` |
| portrait_types | 1 | 1 | 1 | `common/portrait_types.md` |
| province_terrain | 3 | 12919 | 12919 | `common/province_terrain.md` |
| puppets | 4 | 101 | 101 | `common/puppets.md` |
| raids | 2 | 10 | 10 | `common/raids.md` |
| religion | 80 | 1006 | 936 | `common/religion.md` |
| roads | 5 | 4202 | 4202 | `common/roads.md` |
| ruler_objective_advice_types | 2 | 3 | 3 | `common/ruler_objective_advice_types.md` |
| schemes | 72 | 550 | 550 | `common/schemes.md` |
| script_values | 149 | 4574 | 4574 | `common/script_values.md` |
| scripted_animations | 4 | 20 | 20 | `common/scripted_animations.md` |
| scripted_character_templates | 49 | 437 | 437 | `common/scripted_character_templates.md` |
| scripted_costs | 2 | 15 | 15 | `common/scripted_costs.md` |
| scripted_effects | 201 | 4735 | 4735 | `common/scripted_effects.md` |
| scripted_guis | 10 | 59 | 59 | `common/scripted_guis.md` |
| scripted_lists | 1 | 7 | 7 | `common/scripted_lists.md` |
| scripted_modifiers | 50 | 485 | 485 | `common/scripted_modifiers.md` |
| scripted_relations | 2 | 46 | 46 | `common/scripted_relations.md` |
| scripted_rules | 3 | 76 | 76 | `common/scripted_rules.md` |
| scripted_triggers | 157 | 4459 | 4459 | `common/scripted_triggers.md` |
| secret_types | 5 | 22 | 22 | `common/secret_types.md` |
| situation | 23 | 331 | 331 | `common/situation.md` |
| spiritual_fulfillment | 2 | 2 | 2 | `common/spiritual_fulfillment.md` |
| story_cycles | 57 | 55 | 55 | `common/story_cycles.md` |
| struggle | 5 | 129 | 129 | `common/struggle.md` |
| subject_contracts | 19 | 97 | 97 | `common/subject_contracts.md` |
| succession_appointment | 11 | 13 | 13 | `common/succession_appointment.md` |
| succession_election | 10 | 9 | 9 | `common/succession_election.md` |
| suggestions | 3 | 14 | 14 | `common/suggestions.md` |
| task_contracts | 17 | 179 | 179 | `common/task_contracts.md` |
| tax_slots | 4 | 9 | 9 | `common/tax_slots.md` |
| terrain_types | 2 | 17 | 17 | `common/terrain_types.md` |
| title_types | 2 | 11 | 11 | `common/title_types.md` |
| trade | 9 | 126 | 91 | `common/trade.md` |
| trade_goods_graphics | 1 | 69 | 69 | `common/trade_goods_graphics.md` |
| trade_tasks | 1 | 3 | 3 | `common/trade_tasks.md` |
| traits | 4 | 311 | 311 | `common/traits.md` |
| travel | 6 | 52 | 52 | `common/travel.md` |
| trigger_localization | 56 | 1780 | 1780 | `common/trigger_localization.md` |
| tutorial_lesson_chains | 2 | 21 | 21 | `common/tutorial_lesson_chains.md` |
| tutorial_lessons | 11 | 124 | 124 | `common/tutorial_lessons.md` |
| vassal_stances | 2 | 7 | 7 | `common/vassal_stances.md` |

## common\ 根散文件

| 文件 | 字节 | 顶层块 |
|---|---|---|
| `achievement_groups.txt` | 8769 | 5 |

## 其他内容目录概览

见 `other_dirs.md`（20 个 game\ 顶层目录，目录级统计；common 以外的脚本细节按需直接读游戏目录）。
