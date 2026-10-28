# common/law_groups 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：7（其中 Jomini 解析 6 个）
- 顶层块条目总数：30，跨文件唯一条目 30
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_realm_law_groups.txt` | 1891 | 11 | 0 | jomini |
| `00_succession_law_groups.txt` | 544 | 4 | 0 | jomini |
| `01_title_succession_law_groups.txt` | 73 | 1 | 0 | jomini |
| `02_admininistrative_law_groups.txt` | 2326 | 11 | 0 | jomini |
| `03_imperial_policie_groups.txt` | 260 | 1 | 0 | jomini |
| `04_pam_ecclesiastical_law_groups.txt` | 587 | 2 | 0 | jomini |
| `_law_groups.info` | 1607 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_realm_law_groups.txt（11 条目）

- crown_authority
- tribal_authority
- church_authority
- camp_purpose
- imperial_bureaucracy
- nomadic_authority
- celestial_bureaucracy
- mandala_decree
- meritocratic_bureaucracy
- japanese_bureaucracy
- crowned_laws

### 00_succession_law_groups.txt（4 条目）

- succession_order_laws
- succession_gender_laws
- succession_faith
- succession_rel_head

### 01_title_succession_law_groups.txt（1 条目）

- title_succession_laws

### 02_admininistrative_law_groups.txt（11 条目）

- province_war_law
- province_border_law
- celestial_army_liege_law
- celestial_army_vassal_law
- celestial_retirement_law
- border_wars_laws
- grand_secretariat_laws
- candidate_score_laws
- budget_allocation_salary_law
- budget_allocation_ministry_law
- budget_allocation_military_law

### 03_imperial_policie_groups.txt（1 条目）

- imperial_policy_laws

### 04_pam_ecclesiastical_law_groups.txt（2 条目）

- budget_allocation_cardinal_law
- church_benefices_law

### 未解析文件

- `_law_groups.info` — 纯文档（非 Jomini）
