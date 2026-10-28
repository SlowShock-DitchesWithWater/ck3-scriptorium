# 原版结构索引（vanilla_structure）总索引

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与内容指纹见 manifest.json 的 game_docs.vanilla_structure）
- 权威顺序：script_docs dump（game_docs/script_docs/）> wiki 层（pages/）> 本结构索引（仅导航）。
- 生成方式：`scripts/vanilla_index.py` 递归扫描，只提取结构信息（路径/文件名/顶层块名/计数/大小），零原版文件内容复制（mod 制作时按索引直接读游戏目录）。

## 查询方式

1. **查某条目（trait/opinion/modifier/... 名）定义在哪个文件**：
   `grep -P "^<条目名>\t" game_docs\vanilla_structure\entry_map.tsv`
   （entry_map.tsv 共 78167 行映射；输出列为 条目名/定义文件/行号，文件路径相对 game\ 根）
2. **浏览某类内容的全部文件与条目**：读 `common/<子目录>.md`（下表）。
3. **events/history/gui/gfx 等其他目录**：读 `other_dirs.md`。

## common\ 子目录摘要（128 个，全覆盖）

| 子目录 | 文件数 | 顶层块条目 | 唯一条目 | 摘要文件 |
|---|---|---|---|---|
| accolade_icons | 2 | 0 | 0 | `common/accolade_icons.md` |
| accolade_names | 2 | 16 | 16 | `common/accolade_names.md` |
| accolade_types | 6 | 31 | 31 | `common/accolade_types.md` |
| achievements | 13 | 198 | 198 | `common/achievements.md` |
| activities | 75 | 476 | 476 | `common/activities.md` |
| ai_goaltypes | 1 | 1 | 1 | `common/ai_goaltypes.md` |
| ai_war_stances | 4 | 7 | 7 | `common/ai_war_stances.md` |
| artifacts | 31 | 1085 | 1047 | `common/artifacts.md` |
| bookmark_portraits | 342 | 341 | 341 | `common/bookmark_portraits.md` |
| bookmarks | 6 | 75 | 75 | `common/bookmarks.md` |
| buildings | 23 | 989 | 989 | `common/buildings.md` |
| casus_belli_groups | 2 | 19 | 19 | `common/casus_belli_groups.md` |
| casus_belli_types | 29 | 126 | 126 | `common/casus_belli_types.md` |
| character_backgrounds | 2 | 2 | 2 | `common/character_backgrounds.md` |
| character_interaction_categories | 2 | 16 | 16 | `common/character_interaction_categories.md` |
| character_interactions | 68 | 560 | 560 | `common/character_interactions.md` |
| character_memory_types | 23 | 398 | 398 | `common/character_memory_types.md` |
| coat_of_arms | 24 | 3333 | 3061 | `common/coat_of_arms.md` |
| combat_effects | 2 | 31 | 31 | `common/combat_effects.md` |
| combat_phase_events | 3 | 13 | 13 | `common/combat_phase_events.md` |
| confederation_types | 3 | 7 | 7 | `common/confederation_types.md` |
| connection_arrows | 2 | 21 | 21 | `common/connection_arrows.md` |
| console_groups | 2 | 3 | 3 | `common/console_groups.md` |
| council_positions | 3 | 15 | 15 | `common/council_positions.md` |
| council_tasks | 10 | 72 | 72 | `common/council_tasks.md` |
| court_amenities | 2 | 4 | 4 | `common/court_amenities.md` |
| court_positions | 47 | 166 | 166 | `common/court_positions.md` |
| court_types | 2 | 7 | 7 | `common/court_types.md` |
| courtier_guest_management | 3 | 2 | 2 | `common/courtier_guest_management.md` |
| culture | 152 | 2532 | 2532 | `common/culture.md` |
| customizable_localization | 159 | 2782 | 2782 | `common/customizable_localization.md` |
| deathreasons | 4 | 317 | 317 | `common/deathreasons.md` |
| decision_group_types | 2 | 18 | 18 | `common/decision_group_types.md` |
| decisions | 77 | 501 | 501 | `common/decisions.md` |
| defines | 12 | 162 | 144 | `common/defines.md` |
| diarchies | 6 | 17 | 17 | `common/diarchies.md` |
| dna_data | 9 | 445 | 445 | `common/dna_data.md` |
| domiciles | 10 | 1870 | 1870 | `common/domiciles.md` |
| dynasties | 9 | 10398 | 10398 | `common/dynasties.md` |
| dynasty_house_motto_inserts | 2 | 23 | 23 | `common/dynasty_house_motto_inserts.md` |
| dynasty_house_mottos | 2 | 74 | 74 | `common/dynasty_house_mottos.md` |
| dynasty_houses | 6 | 604 | 604 | `common/dynasty_houses.md` |
| dynasty_legacies | 11 | 22 | 22 | `common/dynasty_legacies.md` |
| dynasty_perks | 12 | 110 | 110 | `common/dynasty_perks.md` |
| effect_localization | 37 | 1017 | 1017 | `common/effect_localization.md` |
| epidemics | 2 | 7 | 7 | `common/epidemics.md` |
| ethnicities | 25 | 51 | 51 | `common/ethnicities.md` |
| event_2d_effects | 2 | 5 | 5 | `common/event_2d_effects.md` |
| event_backgrounds | 3 | 313 | 313 | `common/event_backgrounds.md` |
| event_themes | 3 | 195 | 195 | `common/event_themes.md` |
| event_transitions | 4 | 33 | 33 | `common/event_transitions.md` |
| factions | 7 | 12 | 12 | `common/factions.md` |
| flavorization | 10 | 1359 | 1359 | `common/flavorization.md` |
| focuses | 4 | 28 | 28 | `common/focuses.md` |
| game_concepts | 18 | 1142 | 1142 | `common/game_concepts.md` |
| game_rules | 3 | 86 | 86 | `common/game_rules.md` |
| genes | 12 | 13 | 6 | `common/genes.md` |
| governments | 4 | 20 | 20 | `common/governments.md` |
| graphical_unit_types | 2 | 9 | 9 | `common/graphical_unit_types.md` |
| great_projects | 5 | 24 | 24 | `common/great_projects.md` |
| guest_system | 2 | 2 | 2 | `common/guest_system.md` |
| holdings | 2 | 7 | 7 | `common/holdings.md` |
| holy_orders | 4 | 313 | 313 | `common/holy_orders.md` |
| hook_types | 2 | 48 | 48 | `common/hook_types.md` |
| house_aspirations | 5 | 29 | 29 | `common/house_aspirations.md` |
| house_relation_types | 2 | 1 | 1 | `common/house_relation_types.md` |
| house_unities | 2 | 1 | 1 | `common/house_unities.md` |
| important_actions | 36 | 301 | 301 | `common/important_actions.md` |
| inspirations | 2 | 12 | 12 | `common/inspirations.md` |
| landed_titles | 14 | 1742 | 1739 | `common/landed_titles.md` |
| law_groups | 7 | 30 | 30 | `common/law_groups.md` |
| laws | 7 | 201 | 201 | `common/laws.md` |
| lease_contracts | 2 | 2 | 2 | `common/lease_contracts.md` |
| legends | 6 | 74 | 73 | `common/legends.md` |
| legitimacy | 2 | 8 | 8 | `common/legitimacy.md` |
| lifestyle_perks | 19 | 162 | 162 | `common/lifestyle_perks.md` |
| lifestyles | 2 | 6 | 6 | `common/lifestyles.md` |
| men_at_arms_types | 11 | 111 | 111 | `common/men_at_arms_types.md` |
| menu_scenes | 1 | 0 | 0 | `common/menu_scenes.md` |
| message_filter_types | 3 | 195 | 195 | `common/message_filter_types.md` |
| message_group_types | 2 | 31 | 31 | `common/message_group_types.md` |
| messages | 43 | 728 | 728 | `common/messages.md` |
| modifier_definition_formats | 14 | 1982 | 1980 | `common/modifier_definition_formats.md` |
| modifier_icons | 1 | 1 | 1 | `common/modifier_icons.md` |
| modifiers | 141 | 6351 | 6351 | `common/modifiers.md` |
| morpheme_strip_rules | 3 | 6 | 6 | `common/morpheme_strip_rules.md` |
| named_colors | 2 | 2 | 1 | `common/named_colors.md` |
| nicknames | 12 | 729 | 729 | `common/nicknames.md` |
| on_action | 174 | 940 | 932 | `common/on_action.md` |
| opinion_modifiers | 76 | 1630 | 1630 | `common/opinion_modifiers.md` |
| playable_difficulty_infos | 2 | 14 | 14 | `common/playable_difficulty_infos.md` |
| pool_character_selectors | 7 | 12 | 12 | `common/pool_character_selectors.md` |
| portrait_types | 1 | 1 | 1 | `common/portrait_types.md` |
| province_terrain | 3 | 12720 | 12720 | `common/province_terrain.md` |
| puppets | 4 | 101 | 101 | `common/puppets.md` |
| raids | 2 | 10 | 10 | `common/raids.md` |
| religion | 80 | 983 | 914 | `common/religion.md` |
| ruler_objective_advice_types | 2 | 3 | 3 | `common/ruler_objective_advice_types.md` |
| schemes | 50 | 483 | 483 | `common/schemes.md` |
| script_values | 123 | 3954 | 3953 | `common/script_values.md` |
| scripted_animations | 3 | 16 | 16 | `common/scripted_animations.md` |
| scripted_character_templates | 45 | 410 | 410 | `common/scripted_character_templates.md` |
| scripted_costs | 2 | 13 | 13 | `common/scripted_costs.md` |
| scripted_effects | 185 | 4123 | 4123 | `common/scripted_effects.md` |
| scripted_guis | 9 | 54 | 54 | `common/scripted_guis.md` |
| scripted_lists | 1 | 6 | 6 | `common/scripted_lists.md` |
| scripted_modifiers | 46 | 423 | 423 | `common/scripted_modifiers.md` |
| scripted_relations | 2 | 38 | 38 | `common/scripted_relations.md` |
| scripted_rules | 3 | 72 | 72 | `common/scripted_rules.md` |
| scripted_triggers | 148 | 3878 | 3878 | `common/scripted_triggers.md` |
| secret_types | 4 | 19 | 19 | `common/secret_types.md` |
| situation | 21 | 287 | 287 | `common/situation.md` |
| spiritual_fulfillment | 2 | 2 | 2 | `common/spiritual_fulfillment.md` |
| story_cycles | 54 | 52 | 52 | `common/story_cycles.md` |
| struggle | 5 | 129 | 129 | `common/struggle.md` |
| subject_contracts | 18 | 87 | 87 | `common/subject_contracts.md` |
| succession_appointment | 10 | 12 | 12 | `common/succession_appointment.md` |
| succession_election | 9 | 8 | 8 | `common/succession_election.md` |
| suggestions | 3 | 14 | 14 | `common/suggestions.md` |
| task_contracts | 12 | 159 | 159 | `common/task_contracts.md` |
| tax_slots | 4 | 9 | 9 | `common/tax_slots.md` |
| terrain_types | 2 | 17 | 17 | `common/terrain_types.md` |
| traits | 4 | 306 | 306 | `common/traits.md` |
| travel | 6 | 49 | 49 | `common/travel.md` |
| trigger_localization | 54 | 1706 | 1706 | `common/trigger_localization.md` |
| tutorial_lesson_chains | 2 | 21 | 21 | `common/tutorial_lesson_chains.md` |
| tutorial_lessons | 10 | 116 | 116 | `common/tutorial_lessons.md` |
| vassal_stances | 2 | 7 | 7 | `common/vassal_stances.md` |

## common\ 根散文件

| 文件 | 字节 | 顶层块 |
|---|---|---|
| `achievement_groups.txt` | 7869 | 5 |

## 其他内容目录概览

见 `other_dirs.md`（20 个 game\ 顶层目录，目录级统计；common 以外的脚本细节按需直接读游戏目录）。
