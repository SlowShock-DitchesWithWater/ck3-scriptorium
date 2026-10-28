# common/dynasty_perks 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：12（其中 Jomini 解析 11 个）
- 顶层块条目总数：110，跨文件唯一条目 110
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_dynasty_perks.txt` | 9263 | 35 | 0 | jomini |
| `01_ep1_dynasty_perks.txt` | 2155 | 5 | 0 | jomini |
| `01_ep2_dynasty_perks.txt` | 3190 | 5 | 0 | jomini |
| `01_fp1_dynasty_perks.txt` | 4172 | 10 | 0 | jomini |
| `03_fp2_dynasty_perks.txt` | 3466 | 10 | 0 | jomini |
| `03_fp3_dynasty_perks.txt` | 2551 | 5 | 0 | jomini |
| `05_ce1_dynasty_perks.txt` | 3879 | 10 | 0 | jomini |
| `06_ep3_dynasty_perks.txt` | 2270 | 5 | 0 | jomini |
| `07_mpo_dynasty_perks.txt` | 1985 | 5 | 0 | jomini |
| `08_tgp_dynasty_perks.txt` | 8075 | 15 | 0 | jomini |
| `09_pam_dynasty_perks.txt` | 2380 | 5 | 0 | jomini |
| `_dynasty_perks.info` | 1052 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_dynasty_perks.txt（35 条目）

- blood_legacy_1
- blood_legacy_2
- blood_legacy_3
- blood_legacy_4
- blood_legacy_5
- warfare_legacy_1
- warfare_legacy_2
- warfare_legacy_3
- warfare_legacy_4
- warfare_legacy_5
- law_legacy_1
- law_legacy_2
- law_legacy_3
- law_legacy_4
- law_legacy_5
- guile_legacy_1
- guile_legacy_2
- guile_legacy_3
- guile_legacy_4
- guile_legacy_5
- erudition_legacy_1
- erudition_legacy_2
- erudition_legacy_3
- erudition_legacy_4
- erudition_legacy_5
- glory_legacy_1
- glory_legacy_2
- glory_legacy_3
- glory_legacy_4
- glory_legacy_5
- kin_legacy_1
- kin_legacy_2
- kin_legacy_3
- kin_legacy_4
- kin_legacy_5

### 01_ep1_dynasty_perks.txt（5 条目）

- ep1_culture_legacy_1
- ep1_culture_legacy_2
- ep1_culture_legacy_3
- ep1_culture_legacy_4
- ep1_culture_legacy_5

### 01_ep2_dynasty_perks.txt（5 条目）

- ep2_activities_legacy_2
- ep2_activities_legacy_1
- ep2_activities_legacy_3
- ep2_activities_legacy_4
- ep2_activities_legacy_5

### 01_fp1_dynasty_perks.txt（10 条目）

- fp1_adventure_legacy_1
- fp1_adventure_legacy_2
- fp1_adventure_legacy_3
- fp1_adventure_legacy_4
- fp1_adventure_legacy_5
- fp1_pillage_legacy_1
- fp1_pillage_legacy_2
- fp1_pillage_legacy_3
- fp1_pillage_legacy_4
- fp1_pillage_legacy_5

### 03_fp2_dynasty_perks.txt（10 条目）

- fp2_urbanism_legacy_1
- fp2_urbanism_legacy_2
- fp2_urbanism_legacy_3
- fp2_urbanism_legacy_4
- fp2_urbanism_legacy_5
- fp2_coterie_legacy_1
- fp2_coterie_legacy_2
- fp2_coterie_legacy_3
- fp2_coterie_legacy_4
- fp2_coterie_legacy_5

### 03_fp3_dynasty_perks.txt（5 条目）

- fp3_khvarenah_legacy_1
- fp3_khvarenah_legacy_2
- fp3_khvarenah_legacy_3
- fp3_khvarenah_legacy_4
- fp3_khvarenah_legacy_5

### 05_ce1_dynasty_perks.txt（10 条目）

- ce1_heroic_legacy_1
- ce1_heroic_legacy_2
- ce1_heroic_legacy_3
- ce1_heroic_legacy_4
- ce1_heroic_legacy_5
- ce1_legitimacy_legacy_1
- ce1_legitimacy_legacy_2
- ce1_legitimacy_legacy_3
- ce1_legitimacy_legacy_4
- ce1_legitimacy_legacy_5

### 06_ep3_dynasty_perks.txt（5 条目）

- ep3_administrative_legacy_1
- ep3_administrative_legacy_2
- ep3_administrative_legacy_3
- ep3_administrative_legacy_4
- ep3_administrative_legacy_5

### 07_mpo_dynasty_perks.txt（5 条目）

- mpo_nomad_legacy_1
- mpo_nomad_legacy_2
- mpo_nomad_legacy_3
- mpo_nomad_legacy_4
- mpo_nomad_legacy_5

### 08_tgp_dynasty_perks.txt（15 条目）

- tgp_chinese_legacy_1
- tgp_chinese_legacy_2
- tgp_chinese_legacy_3
- tgp_chinese_legacy_4
- tgp_chinese_legacy_5
- tgp_japan_legacy_1
- tgp_japan_legacy_2
- tgp_japan_legacy_3
- tgp_japan_legacy_4
- tgp_japan_legacy_5
- tgp_sea_legacy_1
- tgp_sea_legacy_2
- tgp_sea_legacy_3
- tgp_sea_legacy_4
- tgp_sea_legacy_5

### 09_pam_dynasty_perks.txt（5 条目）

- pam_legacy_1
- pam_legacy_2
- pam_legacy_3
- pam_legacy_4
- pam_legacy_5

### 未解析文件

- `_dynasty_perks.info` — 纯文档（非 Jomini）
