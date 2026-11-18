# common/council_tasks 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与指纹见 manifest.json）
- 文件数：10（其中 Jomini 解析 9 个）
- 顶层块条目总数：75，跨文件唯一条目 75
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_chancellor_tasks.txt` | 30206 | 5 | 0 | jomini |
| `00_court_chaplain_tasks.txt` | 34336 | 3 | 0 | jomini |
| `00_kurultai_tasks.txt` | 140541 | 32 | 0 | jomini |
| `00_marshal_tasks.txt` | 26600 | 4 | 0 | jomini |
| `00_spouse_tasks.txt` | 5537 | 6 | 0 | jomini |
| `00_spymaster_tasks.txt` | 22602 | 3 | 0 | jomini |
| `00_steward_tasks.txt` | 64111 | 7 | 0 | jomini |
| `00_vizier_tasks.txt` | 5607 | 6 | 0 | jomini |
| `01_ministry_tasks.txt` | 10573 | 9 | 0 | jomini |
| `_council_tasks.info` | 7828 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_chancellor_tasks.txt（5 条目）

- task_foreign_affairs
- task_domestic_affairs
- task_republic_assembly_preparation
- task_integrate_title
- task_bestow_royal_favor

### 00_court_chaplain_tasks.txt（3 条目）

- task_religious_relations
- task_conversion
- task_fabricate_claim

### 00_kurultai_tasks.txt（32 条目）

- task_kurultai_default_1
- task_kurultai_fertility_1
- task_kurultai_control_1
- task_kurultai_court_astrologer_1
- task_kurultai_domestic_affairs_1
- task_kurultai_exploit_area_1
- task_kurultai_raider_1
- task_kurultai_culture_1
- task_kurultai_default_2
- task_kurultai_fertility_2
- task_kurultai_control_2
- task_kurultai_court_astrologer_2
- task_kurultai_domestic_affairs_2
- task_kurultai_exploit_area_2
- task_kurultai_raider_2
- task_kurultai_culture_2
- task_kurultai_default_3
- task_kurultai_fertility_3
- task_kurultai_control_3
- task_kurultai_court_astrologer_3
- task_kurultai_domestic_affairs_3
- task_kurultai_exploit_area_3
- task_kurultai_raider_3
- task_kurultai_culture_3
- task_kurultai_default_4
- task_kurultai_fertility_4
- task_kurultai_control_4
- task_kurultai_court_astrologer_4
- task_kurultai_domestic_affairs_4
- task_kurultai_exploit_area_4
- task_kurultai_raider_4
- task_kurultai_culture_4

### 00_marshal_tasks.txt（4 条目）

- task_organize_levies
- task_train_commanders
- task_increase_control
- task_manage_guards

### 00_spouse_tasks.txt（6 条目）

- task_spouse_default
- task_court_politics
- task_chivalry
- task_manage_domain
- task_court_intrigue
- task_patronage

### 00_spymaster_tasks.txt（3 条目）

- task_disrupt_schemes
- task_support_schemes
- task_find_secrets

### 00_steward_tasks.txt（7 条目）

- task_collect_taxes
- task_develop_county
- task_republic_trade_logistics
- task_republic_market_oversight
- task_promote_culture
- task_accept_culture
- task_convince_dejure

### 00_vizier_tasks.txt（6 条目）

- task_vizier_default
- task_vizier_court_politics
- task_vizier_chivalry
- task_vizier_manage_domain
- task_vizier_court_intrigue
- task_vizier_patronage

### 01_ministry_tasks.txt（9 条目）

- task_manage_talent
- task_bestow_royal_favor_minister_of_personnel
- task_culture_minister
- task_justify_rule
- task_fabricate_claim_minister_of_rites
- task_great_projects
- task_develop_county_minister_of_works
- task_lead_troops
- task_train_commanders_grand_marshal

### 未解析文件

- `_council_tasks.info` — 纯文档（非 Jomini）
