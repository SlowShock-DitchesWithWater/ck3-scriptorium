# common/casus_belli_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：29（其中 Jomini 解析 28 个）
- 顶层块条目总数：126，跨文件唯一条目 126
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_casus_belli_types.txt` | 3778 | 2 | 0 | jomini |
| `00_civil_war.txt` | 61252 | 9 | 0 | jomini |
| `00_claim.txt` | 20235 | 1 | 0 | jomini |
| `00_conquest.txt` | 41849 | 4 | 0 | jomini |
| `00_dejure_war.txt` | 40705 | 6 | 0 | jomini |
| `00_dissolve_empire_cb.txt` | 5870 | 1 | 0 | jomini |
| `00_event_war.txt` | 97481 | 10 | 0 | jomini |
| `00_invasion_war.txt` | 53982 | 5 | 0 | jomini |
| `00_nomadic_conquest.txt` | 17531 | 2 | 0 | jomini |
| `00_peasant_war_new.txt` | 5930 | 1 | 0 | jomini |
| `00_religious_war.txt` | 114785 | 7 | 0 | jomini |
| `00_struggle_war.txt` | 9134 | 1 | 0 | jomini |
| `00_subjugation.txt` | 15012 | 1 | 0 | jomini |
| `00_tributarize.txt` | 19649 | 2 | 0 | jomini |
| `00_vassalization.txt` | 9411 | 1 | 0 | jomini |
| `01_ep1_wars.txt` | 16701 | 2 | 0 | jomini |
| `01_fp1_wars.txt` | 35165 | 1 | 0 | jomini |
| `03_fp2_wars.txt` | 27010 | 3 | 0 | jomini |
| `05_fp3_wars.txt` | 42498 | 6 | 0 | jomini |
| `06_ce1_wars.txt` | 51939 | 3 | 0 | jomini |
| `07_ep3_admin_cbs.txt` | 48609 | 5 | 0 | jomini |
| `07_ep3_wars.txt` | 179456 | 14 | 0 | jomini |
| `09_mpo_wars.txt` | 140717 | 10 | 0 | jomini |
| `10_tgp_china_wars.txt` | 83779 | 9 | 0 | jomini |
| `10_tgp_faction_wars.txt` | 20386 | 4 | 0 | jomini |
| `10_tgp_japan_wars.txt` | 77772 | 10 | 0 | jomini |
| `_casus_belli.info` | 11130 | - | - | 纯文档（非 Jomini） |
| `pam_wars.txt` | 20575 | 4 | 0 | jomini |
| `tgp_eastasia_wars.txt` | 14551 | 2 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_casus_belli_types.txt（2 条目）

- debug_war
- debug_artifact_war

### 00_civil_war.txt（9 条目）

- independence_faction_war
- liberty_faction_war
- populist_war
- claimant_faction_war
- depose_war
- refused_liege_demand_war
- independence_war
- nation_fracturing_faction_war
- nomadic_war

### 00_claim.txt（1 条目）

- claim_cb

### 00_conquest.txt（4 条目）

- county_conquest_cb
- duchy_conquest_cb
- ducal_conquest_cb
- ireland_laudabiliter_conquest_cb

### 00_dejure_war.txt（6 条目）

- de_jure_cb
- individual_county_de_jure_cb
- individual_duchy_de_jure_cb
- imperial_reconquest_cb
- dismantle_holy_pretender_cb
- dismantle_byz_pretender_cb

### 00_dissolve_empire_cb.txt（1 条目）

- dissolve_empire_war

### 00_event_war.txt（10 条目）

- norman_conquest_cb
- norwegian_invasion_cb
- sons_of_lothbrok_invasion_cb
- hungarian_migration_cb
- azariqa_rebellion_cb
- raiktor_claim_cb
- raiktor_conquest_cb
- fp1_scandi_adventurer_conquest
- diarch_vassalisation_cb
- remove_regent_cb

### 00_invasion_war.txt（5 条目）

- invasion_war
- clan_invasion_war
- mongol_invasion_war
- mongol_realm_invasion_war
- pax_romana_invasion_war

### 00_nomadic_conquest.txt（2 条目）

- nomadic_conquest_cb
- nomadic_conquest_duchy_cb

### 00_peasant_war_new.txt（1 条目）

- peasant_war

### 00_religious_war.txt（7 条目）

- minor_religious_war
- religious_war
- major_religious_war
- excommunication_war
- flowery_war_cb
- undirected_great_holy_war
- directed_great_holy_war

### 00_struggle_war.txt（1 条目）

- county_struggle_cb

### 00_subjugation.txt（1 条目）

- tribal_subjugation_cb

### 00_tributarize.txt（2 条目）

- make_tributary_cb
- tributary_independence_war

### 00_vassalization.txt（1 条目）

- vassalization_cb

### 01_ep1_wars.txt（2 条目）

- artifact_war
- reclaim_relic_artifact_war

### 01_fp1_wars.txt（1 条目）

- fp1_varangian_adventurer_conquest

### 03_fp2_wars.txt（3 条目）

- fp2_border_raid
- fp2_expel_interloper
- fp2_mediterranean_conquest_cb

### 05_fp3_wars.txt（6 条目）

- fp3_install_loyalist_cb
- fp3_turkic_invasion_cb
- fp3_seljuk_invasion_cb
- fp3_free_house_member_cb
- fp3_unify_house_cb
- fp3_zanj_rebellion_war

### 06_ce1_wars.txt（3 条目）

- mythical_ancestor_war
- legendary_adventure
- leg_demand_fealty_cb

### 07_ep3_admin_cbs.txt（5 条目）

- expansion_cb
- duchy_expansion_cb
- naval_expansion_cb
- naval_duchy_expansion_cb
- influence_war_cb

### 07_ep3_wars.txt（14 条目）

- ep3_laamp_adventurer_county_invasion
- ep3_laamp_adventurer_duchy_invasion
- ep3_laamp_adventurer_kingdom_invasion
- ep3_laamp_adventurer_empire_invasion
- ep3_laamp_raid_contract_cb
- crusading_claim_cb
- ep3_hasan_assassin_war
- imperial_expedition_cb
- ep3_pillaging_foray
- ep3_roman_empire_border_war
- ep3_laamp_apprehend_adventurer_cb
- greek_anarchy_cb
- ep3_laamp_peasant_war
- admin_barbarian_conquest_cb

### 09_mpo_wars.txt（10 条目）

- migration_cb
- mpo_nomad_invasion_cb
- mpo_nomad_duchy_invasion_cb
- humiliation_cb
- retaliation_cb
- domination_cb
- de_jure_cb_nomadic
- sovereignty_cb
- mpo_great_war_of_defiance_cb
- mpo_gok_onslaught_cb

### 10_tgp_china_wars.txt（9 条目）

- china_seize_county_cb
- china_hegemon_seize_county_cb
- china_seize_duchy_cb
- china_hegemon_seize_duchy_cb
- claim_the_mandate_cb
- chinese_consolidation_cb
- chinese_reunification_cb
- silk_road_vassalization_cb
- grand_campaign_kingdom_invasion_cb

### 10_tgp_faction_wars.txt（4 条目）

- replace_ceremonial_regent_faction_war
- restore_ceremonial_liege_faction_war
- ceremonial_claimant_faction_war
- imperial_policy_faction_war

### 10_tgp_japan_wars.txt（10 条目）

- japan_install_bloc_member_cb
- japan_soryo_conquest_county_landless_cb
- japan_soryo_conquest_county_cb
- japan_demand_administrative_cb
- japan_imperial_expansion_cb
- japan_imperial_reconquest_cb
- japan_refused_ritsuryo_cb
- eradicate_house_cb
- japan_establish_soryo_administration_cb
- japan_bloc_war_cb

### pam_wars.txt（4 条目）

- pam_humiliation_cb
- pam_challenge_hof_cb
- pam_antiking_cb
- pam_investiture_conflict_cb

### tgp_eastasia_wars.txt（2 条目）

- mandala_plunder_cb
- mandala_raze_capital_structure_cb

### 未解析文件

- `_casus_belli.info` — 纯文档（非 Jomini）
