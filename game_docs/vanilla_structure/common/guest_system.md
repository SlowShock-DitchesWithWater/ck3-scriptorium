# common/guest_system 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：2，跨文件唯一条目 2
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_guest_system.txt` | 718 | 2 | 0 | jomini |
| `_guest_system.info` | 1096 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_guest_system.txt（2 条目）

- destination_for_guest_entering_pool
- destination_for_courtier_entering_pool

### 未解析文件

- `_guest_system.info` — 纯文档（非 Jomini）
