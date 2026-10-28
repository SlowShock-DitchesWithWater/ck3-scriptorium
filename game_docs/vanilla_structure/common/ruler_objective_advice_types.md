# common/ruler_objective_advice_types 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：3，跨文件唯一条目 3
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_tutorial_advice.txt` | 3010 | 3 | 0 | jomini |
| `_ruler_objective_advice_types.info` | 1759 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_tutorial_advice.txt（3 条目）

- debug_advice
- become_house_head
- fabricate_claim_advice

### 未解析文件

- `_ruler_objective_advice_types.info` — 纯文档（非 Jomini）
