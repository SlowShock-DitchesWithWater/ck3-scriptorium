# common/hook_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：48，跨文件唯一条目 48
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_hook_types.txt` | 4994 | 48 | 0 | jomini |
| `_hooks.info` | 542 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_hook_types.txt（48 条目）

- weak_blackmail_hook
- strong_blackmail_hook
- test_hook
- favor_hook
- strong_favor_hook
- deposed_antipope_hook
- obligation_hook
- strong_obligation_hook
- indebted_hook
- strong_indebted_hook
- supporter_hook
- loyalty_hook
- predecessor_loyalty_hook
- threat_hook
- life_threat_hook
- strong_test_hook
- perpetual_test_hook
- manipulation_hook
- house_head_hook
- fabrication_hook
- trial_by_combat_hook
- sumptuary_crime_hook
- minor_crime_accomplice_hook
- major_crime_accomplice_hook
- ritual_best_friend_hook
- blood_brother_hook
- blood_sister_hook
- saved_my_life_hook
- suspicious_activity_hook
- major_threat_hook
- weak_prostitute_blackmail_hook
- strong_prostitute_blackmail_hook
- caliphal_submission_hook
- liege_favour_strong_hook
- hostage_loyalty
- follower_oath_hook
- follower_oath_strong_hook
- influence_hook
- strong_influence_hook
- contact_list_weak_hook
- weak_blackmail_hook_no_secret
- filial_piety_hook
- oath_claimant
- oath_claimant_heir
- strong_contribution_hook
- spiritual_counsel_hook
- legitimized_by_clergy_hook
- granted_clerical_title_hook

### 未解析文件

- `_hooks.info` — 纯文档（非 Jomini）
