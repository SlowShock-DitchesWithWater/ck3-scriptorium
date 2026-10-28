# common/inspirations 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：12，跨文件唯一条目 12
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_inspirations.txt` | 54161 | 12 | 0 | jomini |
| `_inspirations.info` | 1202 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_inspirations.txt（12 条目）

- weapon_inspiration
- armor_inspiration
- book_inspiration
- weaver_inspiration
- adventure_inspiration
- artisan_inspiration
- smith_inspiration
- alchemy_inspiration
- research_inspiration
- religious_inspiration
- bow_inspiration
- religious_artifact_inspiration

### 未解析文件

- `_inspirations.info` — 纯文档（非 Jomini）
