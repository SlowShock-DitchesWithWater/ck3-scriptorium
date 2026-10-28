# common/succession_appointment 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：10（其中 Jomini 解析 9 个）
- 顶层块条目总数：12，跨文件唯一条目 12
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `_succession_appointment.info` | 4020 | - | - | 纯文档（非 Jomini） |
| `admin_emperor.txt` | 13281 | 1 | 0 | jomini |
| `admin_governor.txt` | 1494 | 1 | 0 | jomini |
| `celestial_governor.txt` | 2477 | 2 | 0 | jomini |
| `celestial_minister.txt` | 6184 | 1 | 0 | jomini |
| `clerical_christian.txt` | 17518 | 1 | 0 | jomini |
| `japanese_admin_governor.txt` | 5356 | 2 | 0 | jomini |
| `japanese_admin_regent.txt` | 987 | 1 | 0 | jomini |
| `meritocratic_governor.txt` | 2134 | 2 | 0 | jomini |
| `meritocratic_regent.txt` | 875 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### admin_emperor.txt（1 条目）

- admin_emperor

### admin_governor.txt（1 条目）

- admin_governor

### celestial_governor.txt（2 条目）

- celestial_civic_governor
- celestial_military_governor

### celestial_minister.txt（1 条目）

- celestial_minister

### clerical_christian.txt（1 条目）

- clerical_christian

### japanese_admin_governor.txt（2 条目）

- japanese_governor
- japanese_military_governor

### japanese_admin_regent.txt（1 条目）

- japanese_regent

### meritocratic_governor.txt（2 条目）

- meritocratic_civic_governor
- meritocratic_military_governor

### meritocratic_regent.txt（1 条目）

- meritocratic_regent

### 未解析文件

- `_succession_appointment.info` — 纯文档（非 Jomini）
