# common/raids 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：2（其中 Jomini 解析 1 个）
- 顶层块条目总数：10，跨文件唯一条目 10
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `intents/raid_intents.info` | 2099 | - | - | 纯文档（非 Jomini） |
| `intents/raid_intents.txt` | 7899 | 10 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### intents/raid_intents.txt（10 条目）

- pillage_intent_nomadic
- pillage_intent_tribal
- pillage_intent
- raze_intent
- capture_intent_norse
- capture_intent_nomadic
- plunder_intent_nomadic
- adventure_intent_nomadic
- adventure_intent_viking
- destruction_intent

### 未解析文件

- `intents/raid_intents.info` — 纯文档（非 Jomini）
