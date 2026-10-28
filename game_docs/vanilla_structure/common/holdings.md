# common/holdings 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：7，跨文件唯一条目 7
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_holdings.txt` | 4662 | 7 | 0 | jomini |
| `_holdings.info` | 2237 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_holdings.txt（7 条目）

- castle_holding
- tribal_holding
- city_holding
- church_holding
- nomad_holding
- herder_holding
- temple_citadel_holding

### 未解析文件

- `_holdings.info` — 纯文档（非 Jomini）
