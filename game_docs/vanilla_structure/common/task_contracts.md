# common/task_contracts 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：12（其中 Jomini 解析 11 个）
- 顶层块条目总数：159，跨文件唯一条目 159
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `_task_contracts.info` | 3045 | - | - | 纯文档（非 Jomini） |
| `admin_contracts.txt` | 83096 | 17 | 0 | jomini |
| `laamp_base_contracts.txt` | 265171 | 36 | 0 | jomini |
| `laamp_extra_contracts.txt` | 158702 | 18 | 0 | jomini |
| `laamp_nm_contracts.txt` | 25565 | 5 | 0 | jomini |
| `laamp_transport_contracts.txt` | 57034 | 6 | 0 | jomini |
| `nomads_migration_contracts.txt` | 12622 | 10 | 0 | jomini |
| `tgp_admin_contracts.txt` | 102590 | 17 | 0 | jomini |
| `tgp_admin_contracts_tova.txt` | 17633 | 4 | 0 | jomini |
| `tgp_admin_military_contracts.txt` | 5193 | 1 | 0 | jomini |
| `tgp_mandala_contracts.txt` | 97291 | 41 | 0 | jomini |
| `tgp_natural_disaster_contracts.txt` | 20150 | 4 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### admin_contracts.txt（17 条目）

- overdue_taxes
- hoarding_mayor
- bountiful_harvest
- rampant_bandits
- discontent_soldiers
- inept_mayor
- prov_investment
- raiding_peasants
- wild_predators
- evil_presence
- miraculous_healing
- buried_treasure
- public_land
- mad_prophet
- titles_sale
- hungry_times
- wartime_measures

### laamp_base_contracts.txt（36 条目）

- laamp_base_0001
- laamp_base_0011
- laamp_base_0021
- laamp_base_0031
- laamp_base_0041
- laamp_base_1001
- laamp_base_1011
- laamp_base_1041
- laamp_base_5031
- laamp_base_5051
- laamp_base_2001
- laamp_base_2011
- laamp_base_2021
- laamp_base_2031
- laamp_base_2041
- laamp_base_3001
- laamp_base_3011
- laamp_base_3021
- laamp_base_3031
- laamp_base_3041
- laamp_base_4001
- laamp_base_4011
- laamp_base_4021
- laamp_base_4031
- laamp_base_4041
- laamp_base_4100
- laamp_base_6001
- laamp_base_6011
- laamp_base_6021
- laamp_base_6031
- laamp_base_1021
- laamp_base_1031
- laamp_base_5001
- laamp_base_5011
- laamp_base_5021
- laamp_base_5041

### laamp_extra_contracts.txt（18 条目）

- laamp_raid_contract
- laamp_join_war_contract
- laamp_help_claimant_contract
- laamp_steal_artifact_contract
- laamp_construction_contract
- laamp_treasure_hunting_contract
- laamp_cultural_minority_contract
- laamp_religious_minority_contract
- laamp_prison_break_contract
- laamp_treasure_map_contract
- laamp_legitimist_support_contract
- laamp_join_faction_contract
- laamp_help_faith_conversion_contract
- laamp_fight_faith_conversion_contract
- laamp_help_train_commanders_contract
- laamp_help_find_secrets_contract
- laamp_help_fabricate_claim_contract
- laamp_help_increase_control_contract

### laamp_nm_contracts.txt（5 条目）

- laamp_boost_legitimacy_contract
- laamp_rid_councillor_contract
- laamp_gain_wanderer_contract
- laamp_find_secret_contract
- laamp_eliminate_heir_contract

### laamp_transport_contracts.txt（6 条目）

- laamp_transport_vip
- laamp_transport_artifact
- laamp_transport_gold
- laamp_transport_ward
- laamp_transport_explorer
- laamp_transport_animal

### nomads_migration_contracts.txt（10 条目）

- nomadic_migration_contract_1
- nomadic_migration_contract_2
- nomadic_migration_contract_3
- nomadic_migration_contract_4
- nomadic_migration_contract_5
- nomadic_migration_contract_6
- nomadic_migration_contract_7
- nomadic_migration_contract_8
- nomadic_migration_contract_9
- nomadic_migration_contract_10

### tgp_admin_contracts.txt（17 条目）

- jail_inspection
- potent_physick
- irregular_accounting
- salt_smugglers
- hoarding_grain
- doddering_magistrate
- burdensome_taxes
- unsafe_highways
- dam_in_disrepair
- lines_in_the_soil
- fraud_in_broad_daylight
- crumbling_bridge
- confusion_of_tongues
- seditious_storytelling
- quaking_in_panic
- monopoly_in_the_marketplace
- contested_inheritance

### tgp_admin_contracts_tova.txt（4 条目）

- unsanctioned_deity
- escaped_justice
- forced_conscription
- combat_train_monks

### tgp_admin_military_contracts.txt（1 条目）

- missing_equipment

### tgp_mandala_contracts.txt（41 条目）

- mandala_realm_contract_0001
- mandala_realm_contract_0002
- mandala_realm_contract_0003
- mandala_realm_contract_0004
- mandala_realm_contract_0005
- mandala_realm_contract_0006
- mandala_realm_contract_0007
- mandala_realm_contract_0008
- mandala_realm_contract_0009
- mandala_realm_contract_0010
- mandala_realm_contract_0011
- mandala_realm_contract_0012
- mandala_realm_contract_0013
- mandala_realm_contract_0014
- mandala_realm_contract_0015
- mandala_realm_contract_0016
- mandala_realm_contract_0017
- mandala_realm_contract_0018
- mandala_realm_contract_0019
- mandala_realm_contract_0020
- mandala_realm_contract_0021
- mandala_realm_contract_0022
- mandala_realm_contract_0023
- mandala_realm_contract_0024
- mandala_realm_contract_0025
- mandala_realm_contract_0026
- mandala_realm_contract_0027
- mandala_realm_contract_0028
- mandala_realm_contract_0029
- mandala_realm_contract_0030
- mandala_realm_contract_0031
- mandala_realm_contract_0032
- mandala_realm_contract_0033
- mandala_realm_contract_0034
- mandala_realm_contract_0035
- mandala_realm_contract_0036
- mandala_realm_contract_0037
- mandala_realm_contract_0038
- mandala_realm_contract_0039
- mandala_realm_contract_0040
- mandala_realm_contract_0041

### tgp_natural_disaster_contracts.txt（4 条目）

- tgp_food_shortage
- tgp_ravaged_buildings
- tgp_medieval_medicine
- tgp_disaster_displacement

### 未解析文件

- `_task_contracts.info` — 纯文档（非 Jomini）
