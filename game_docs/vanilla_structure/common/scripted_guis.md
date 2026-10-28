# common/scripted_guis 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：9（其中 Jomini 解析 9 个）
- 顶层块条目总数：54，跨文件唯一条目 54
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_character.txt` | 110 | 1 | 0 | jomini |
| `00_empire_faith_gate_guis.txt` | 3396 | 7 | 0 | jomini |
| `00_religion.txt` | 6819 | 11 | 0 | jomini |
| `ce1_funeral_scripted_guis.txt` | 332 | 2 | 0 | jomini |
| `ep2_activities.txt` | 1193 | 3 | 0 | jomini |
| `knight_permissions_sguis.txt` | 390 | 3 | 0 | jomini |
| `pam_scripted_guis.txt` | 3299 | 16 | 0 | jomini |
| `tgp_examination.txt` | 873 | 7 | 0 | jomini |
| `tgp_scripted_guis.txt` | 949 | 4 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_character.txt（1 条目）

- rename_character_after_birth

### 00_empire_faith_gate_guis.txt（7 条目）

- empire_faith_gate_panel_visible
- empire_faith_gate_organized_faith_check
- empire_faith_gate_hof_check
- empire_faith_gate_vassals_check
- empire_faith_gate_contested_warning_1
- empire_faith_gate_contested_warning_2
- empire_faith_gate_contested_warning_3

### 00_religion.txt（11 条目）

- toggle_great_holy_war_pledge
- join_great_holy_war_directed
- toggle_great_holy_war_pledge_defense
- join_great_holy_war_directed_defense
- great_holy_war_give_gold
- toggle_great_holy_war_beneficiary_stance
- not_pledged_not_donated_tooltip
- not_pledged_donated_tooltip
- change_target
- can_pledge_as_attacker
- can_pledge_as_defender

### ce1_funeral_scripted_guis.txt（2 条目）

- funeral_is_body_available_gui
- funeral_fill_available_targets_gui

### ep2_activities.txt（3 条目）

- tournament_is_character_martial_eligible_in_contest
- tournament_is_player_available_to_compete_non_martial
- tournament_is_player_available_to_compete_martial

### knight_permissions_sguis.txt（3 条目）

- kp_culture_minimum_prowess
- kp_culture_high_prowess
- kp_culture_admin_family_knights

### pam_scripted_guis.txt（16 条目）

- pam_great_schism_progress_gui
- pam_great_schism_can_start_gui
- pam_great_schism_ongoing_gui
- pam_investiture_crisis_chapter_unavailable_gui
- pam_has_schism_stance
- using_tenet_popularity_gui
- tenet_popularity_gui_very_popular
- tenet_popularity_gui_popular
- tenet_popularity_gui_neutral
- tenet_popularity_gui_unpopular
- pam_is_papabile
- pam_is_papabile_pious
- pam_is_papabile_populist
- pam_is_papabile_powerful
- pam_know_doctrine
- pam_can_create_holy_site_gui

### tgp_examination.txt（7 条目）

- examination_children_passed_gui
- examination_children_failed_gui
- examination_provincial_passed_gui
- examination_provincial_failed_gui
- examination_metropolitan_passed_gui
- examination_metropolitan_failed_gui
- examination_palace_passed_gui

### tgp_scripted_guis.txt（4 条目）

- on_silk_road_innovation_gui
- is_better_played_with_tgp_gui
- tgp_has_access_to_ministry_trigger_gui
- coronation_trigger_gui
