# common/succession_election 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：9（其中 Jomini 解析 8 个）
- 顶层块条目总数：8，跨文件唯一条目 8
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_feudal_elective.txt` | 5876 | 1 | 0 | jomini |
| `00_pam_clerical_elective.txt` | 2090 | 1 | 0 | jomini |
| `01_princely_elective.txt` | 7446 | 1 | 0 | jomini |
| `02_gaelic_elective.txt` | 4448 | 1 | 0 | jomini |
| `04_saxon_elective.txt` | 4529 | 1 | 0 | jomini |
| `05_scandinavian_elective.txt` | 4765 | 1 | 0 | jomini |
| `06_tribal_elective.txt` | 4845 | 1 | 0 | jomini |
| `09_confederation_elective.txt` | 4976 | 1 | 0 | jomini |
| `_succession_election.info` | 4627 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_feudal_elective.txt（1 条目）

- feudal_elective

### 00_pam_clerical_elective.txt（1 条目）

- theocratic_elective

### 01_princely_elective.txt（1 条目）

- princely_elective

### 02_gaelic_elective.txt（1 条目）

- gaelic_elective

### 04_saxon_elective.txt（1 条目）

- saxon_elective

### 05_scandinavian_elective.txt（1 条目）

- scandinavian_elective

### 06_tribal_elective.txt（1 条目）

- tribal_elective

### 09_confederation_elective.txt（1 条目）

- confederation_elective

### 未解析文件

- `_succession_election.info` — 纯文档（非 Jomini）
