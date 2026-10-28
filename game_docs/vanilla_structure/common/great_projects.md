# common/great_projects 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：5（其中 Jomini 解析 4 个）
- 顶层块条目总数：24，跨文件唯一条目 24
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `types/00_great_project_types.txt` | 184420 | 11 | 12 | jomini |
| `types/00_ministry_projects.txt` | 123440 | 7 | 14 | jomini |
| `types/00_natural_disasters.txt` | 76647 | 2 | 6 | jomini |
| `types/01_pam_projects.txt` | 150383 | 4 | 6 | jomini |
| `types/_great_project_types.info` | 18410 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### types/00_great_project_types.txt（11 条目）

- mandala_capital_01
- mandala_capital_02
- mandala_capital_03
- mandala_capital_04
- mandala_capital_05
- construct_great_barracks
- strengthen_capital
- great_wall
- great_wall_extend_to_shanhai_pass
- great_wall_extend_to_liaodong
- grand_canals

### types/00_ministry_projects.txt（7 条目）

- grand_campaign_project
- minister_project_culture
- minister_project_development
- minister_project_establish_control
- minister_project_train_troops
- minister_project_conduct_census
- minister_compel_religious_uniformity

### types/00_natural_disasters.txt（2 条目）

- great_project_earthquake
- great_project_flood

### types/01_pam_projects.txt（4 条目）

- pam_cathedral_01
- pam_cathedral_02
- pam_cathedral_03
- pam_mass_rite_conversion

### 未解析文件

- `types/_great_project_types.info` — 纯文档（非 Jomini）
