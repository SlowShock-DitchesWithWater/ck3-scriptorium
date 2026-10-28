# common/suggestions 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 2 个）
- 顶层块条目总数：14，跨文件唯一条目 14
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `01_suggestions.txt` | 39435 | 13 | 0 | jomini |
| `02_sanctify_artifact_suggestion.txt` | 1627 | 1 | 0 | jomini |
| `_suggestions.info` | 2877 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 01_suggestions.txt（13 条目）

- suggestion_recruit_maa
- suggestion_declare_war
- suggestion_construct_building
- suggestion_fabricate_claim
- suggestion_create_title
- suggestion_convert_county
- suggestion_increase_control
- suggestion_increase_opinion
- suggestion_raid
- suggestion_grant_title
- suggestion_can_hire_court_positions
- suggestion_request_war_aid_petition
- suggestion_create_nation_fracturing_faction

### 02_sanctify_artifact_suggestion.txt（1 条目）

- suggestion_sanctify_artifact

### 未解析文件

- `_suggestions.info` — 纯文档（非 Jomini）
