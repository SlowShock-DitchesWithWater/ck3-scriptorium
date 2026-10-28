# common/dynasty_legacies 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：11（其中 Jomini 解析 10 个）
- 顶层块条目总数：22，跨文件唯一条目 22
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `81_pam_legacies.txt` | 393 | 1 | 0 | jomini |
| `82_tgp_legacies.txt` | 1302 | 3 | 0 | jomini |
| `83_ep3_legacies.txt` | 383 | 1 | 0 | jomini |
| `92_mpo_legacies.txt` | 373 | 1 | 0 | jomini |
| `94_ce1_legacies.txt` | 162 | 2 | 0 | jomini |
| `95_fp3_legacies.txt` | 579 | 1 | 0 | jomini |
| `96_fp2_legacies.txt` | 1526 | 2 | 0 | jomini |
| `97_ep1_legacies.txt` | 94 | 0 | 0 | jomini |
| `98_fp1_legacies.txt` | 1026 | 2 | 0 | jomini |
| `99_legacies.txt` | 375 | 9 | 0 | jomini |
| `_dynasty_legacies.info` | 832 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 81_pam_legacies.txt（1 条目）

- pam_legacy_track

### 82_tgp_legacies.txt（3 条目）

- tgp_southeast_asia_legacy_track
- tgp_japan_legacy_track
- tgp_china_legacy_track

### 83_ep3_legacies.txt（1 条目）

- ep3_administrative_legacy_track

### 92_mpo_legacies.txt（1 条目）

- mpo_nomad_legacy_track

### 94_ce1_legacies.txt（2 条目）

- ce1_heroic_track
- ce1_legitimacy_legacy_track

### 95_fp3_legacies.txt（1 条目）

- fp3_khvarenah_legacy_track

### 96_fp2_legacies.txt（2 条目）

- fp2_urbanism_legacy_track
- fp2_coterie_legacy_track

### 97_ep1_legacies.txt（0 条目）

（无顶层块）

### 98_fp1_legacies.txt（2 条目）

- fp1_adventure_legacy_track
- fp1_pillage_legacy_track

### 99_legacies.txt（9 条目）

- ep1_culture_legacy_track
- ep2_activities_legacy_track
- warfare_legacy_track
- law_legacy_track
- guile_legacy_track
- blood_legacy_track
- erudition_legacy_track
- glory_legacy_track
- kin_legacy_track

### 未解析文件

- `_dynasty_legacies.info` — 纯文档（非 Jomini）
