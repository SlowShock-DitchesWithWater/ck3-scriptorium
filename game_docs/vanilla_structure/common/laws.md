# common/laws 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：7（其中 Jomini 解析 6 个）
- 顶层块条目总数：201，跨文件唯一条目 201
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_realm_laws.txt` | 78650 | 46 | 16 | jomini |
| `00_succession_laws.txt` | 56128 | 43 | 0 | jomini |
| `01_title_succession_laws.txt` | 9179 | 12 | 0 | jomini |
| `02_admininistrative_laws.txt` | 59600 | 91 | 1 | jomini |
| `03_imperial_policies.txt` | 7478 | 6 | 2 | jomini |
| `04_pam_ecclesiastical_laws.txt` | 746 | 3 | 0 | jomini |
| `_laws.info` | 13567 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_realm_laws.txt（46 条目）

- crown_authority_0
- crown_authority_1
- crown_authority_2
- crown_authority_3
- tribal_authority_0
- tribal_authority_1
- tribal_authority_2
- tribal_authority_3
- church_authority_0
- church_authority_1
- church_authority_2
- church_authority_3
- camp_purpose_wanderers
- camp_purpose_mercenaries
- camp_purpose_scholars
- camp_purpose_explorers
- camp_purpose_brigands
- camp_purpose_legitimists
- imperial_bureaucracy_0
- imperial_bureaucracy_1
- imperial_bureaucracy_2
- imperial_bureaucracy_3
- nomadic_authority_1
- nomadic_authority_2
- nomadic_authority_3
- nomadic_authority_4
- nomadic_authority_5
- celestial_bureaucracy_0
- celestial_bureaucracy_1
- celestial_bureaucracy_2
- celestial_bureaucracy_3
- mandala_decree_none
- mandala_decree_prosperity
- mandala_decree_expansion
- mandala_decree_reverence
- meritocratic_bureaucracy_0
- meritocratic_bureaucracy_1
- meritocratic_bureaucracy_2
- meritocratic_bureaucracy_3
- japanese_bureaucracy_0
- japanese_bureaucracy_1
- japanese_bureaucracy_2
- japanese_bureaucracy_3
- uncrowned
- crowned_king
- crowned_emperor

### 00_succession_laws.txt（43 条目）

- confederate_partition_succession_law
- partition_succession_law
- high_partition_succession_law
- single_heir_succession_law
- single_heir_succession_kurultai_law
- single_heir_succession_law_youngest
- single_heir_dynasty_house
- acclamation_succession_law
- appointment_succession_law
- landless_adventurer_succession_law
- theocratic_elective_succession_law
- clerical_appointment_law
- bishop_theocratic_succession_law
- holy_order_succession_law
- cultural_holy_order_succession_law
- monastic_holy_order_succession_law
- female_monastic_holy_order_succession_law
- male_monastic_holy_order_succession_law
- mercenary_company_succession_law
- city_succession_law
- clan_antagonistic_partition_succession_law
- clan_competitive_partition_succession_law
- clan_impassive_partition_succession_law
- clan_friendly_partition_succession_law
- clan_harmonious_partition_succession_law
- herder_succession_law
- celestial_appointment_succession_law
- celestial_military_appointment_succession_law
- japanese_regency_succession_law
- japanese_appointment_succession_law
- japanese_military_appointment_succession_law
- mandala_succession_law
- meritocratic_appointment_succession_law
- meritocratic_military_appointment_succession_law
- meritocratic_regency_succession_law
- male_only_law
- male_preference_law
- equal_law
- female_preference_law
- female_only_law
- same_faith_only_law
- same_faith_theocratic_succession_law
- same_faith_succession_law

### 01_title_succession_laws.txt（12 条目）

- feudal_elective_succession_law
- princely_elective_succession_law
- saxon_elective_succession_law
- scandinavian_elective_succession_law
- gaelic_elective_succession_law
- tribal_elective_succession_law
- temporal_head_of_faith_succession_law
- noble_family_succession_law
- law_of_the_land_succession_law
- confederation_elective_succession_law
- celestial_ministry_appointment_succession_law
- celestial_grand_marshal_appointment_succession_law

### 02_admininistrative_laws.txt（91 条目）

- province_war_law_0
- province_war_law_1
- province_war_law_2
- province_war_law_3
- province_border_law_0
- province_border_law_1
- province_border_law_2
- celestial_army_liege_law_0
- celestial_army_liege_law_1
- celestial_army_liege_law_2
- celestial_army_liege_law_3
- celestial_army_vassal_law_0
- celestial_army_vassal_law_1
- celestial_army_vassal_law_2
- celestial_army_vassal_law_3
- celestial_retirement_law_0
- celestial_retirement_law_1
- celestial_retirement_law_2
- celestial_retirement_law_3
- celestial_retirement_law_4
- celestial_retirement_law_5
- top_liege_redirected_to_border_wars_law
- top_liege_not_redirected_to_border_wars_law
- grand_chancellor_law
- grand_marshal_law
- grand_censor_law
- candidate_score_merit_law
- candidate_score_prestige_law
- budget_allocation_salary_0
- budget_allocation_salary_5
- budget_allocation_salary_10
- budget_allocation_salary_15
- budget_allocation_salary_20
- budget_allocation_salary_25
- budget_allocation_salary_30
- budget_allocation_salary_35
- budget_allocation_salary_40
- budget_allocation_salary_45
- budget_allocation_salary_50
- budget_allocation_salary_55
- budget_allocation_salary_60
- budget_allocation_salary_65
- budget_allocation_salary_70
- budget_allocation_salary_75
- budget_allocation_salary_80
- budget_allocation_salary_85
- budget_allocation_salary_90
- budget_allocation_salary_95
- budget_allocation_salary_100
- budget_allocation_ministry_0
- budget_allocation_ministry_5
- budget_allocation_ministry_10
- budget_allocation_ministry_15
- budget_allocation_ministry_20
- budget_allocation_ministry_25
- budget_allocation_ministry_30
- budget_allocation_ministry_35
- budget_allocation_ministry_40
- budget_allocation_ministry_45
- budget_allocation_ministry_50
- budget_allocation_ministry_55
- budget_allocation_ministry_60
- budget_allocation_ministry_65
- budget_allocation_ministry_70
- budget_allocation_ministry_75
- budget_allocation_ministry_80
- budget_allocation_ministry_85
- budget_allocation_ministry_90
- budget_allocation_ministry_95
- budget_allocation_ministry_100
- budget_allocation_military_0
- budget_allocation_military_5
- budget_allocation_military_10
- budget_allocation_military_15
- budget_allocation_military_20
- budget_allocation_military_25
- budget_allocation_military_30
- budget_allocation_military_35
- budget_allocation_military_40
- budget_allocation_military_45
- budget_allocation_military_50
- budget_allocation_military_55
- budget_allocation_military_60
- budget_allocation_military_65
- budget_allocation_military_70
- budget_allocation_military_75
- budget_allocation_military_80
- budget_allocation_military_85
- budget_allocation_military_90
- budget_allocation_military_95
- budget_allocation_military_100

### 03_imperial_policies.txt（6 条目）

- defense_mobilization_law
- disarmament_law
- isolation_law
- imperial_expansion_law
- manor_reform_law
- bandit_crackdown_law

### 04_pam_ecclesiastical_laws.txt（3 条目）

- budget_allocation_cardinal_50
- no_benefices
- cardinal_standard_benefices

### 未解析文件

- `_laws.info` — 纯文档（非 Jomini）
