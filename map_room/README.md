# 地图室（Map Room）—— 缮写室的地图 MOD 支持组

> 缮写室（CK3 Scriptorium）是本仓库的 modding 知识库主体；地图室是它下面
> 面向**地图 MOD** 的功能组。知识已并入知识库本体（catalog 可检索），工具与
> 向导放在本目录。

## 组成

### 1. 地图知识（并入知识库，从 catalog 进入）

| 内容 | 位置 | 权威级 |
|---|---|---|
| 地图数据实测档案（格式/尺寸/调色板/编辑器证据） | `game_docs/map_docs/map_data_dossier.md` | 游戏实测，最高 |
| 省份索引（id↔RGB↔名称，13270 行） | `game_docs/map_docs/province_index.tsv` | 游戏实测 |
| auto-nudge 摆放参数表（约 60 参数） | `game_docs/map_docs/nudger_parameters.md` | 数值实测+语义推断 |
| 地图 modding 讲解（heightmap/河流/省份教程） | `pages/Map modding.md`（wiki，1.1 时代） | 低，冲突以实测为准 |

检索方式同知识库规约：先 `grep catalog.md` 命中条目，再读条目指向的文件。
游戏版本更新后刷新知识层：

```
python scripts/map_layer.py --game-dir "<CK3安装目录>\game"
```

### 2. 地图校验器（本目录 `validate_map.py`）

对 mod 的 map_data 做 13 类硬约束检查（颜色集一致、id 连续、河流调色板、
尺寸倍率、引用完整……），规则取自实测档案并按原版校准严重度：

```
python map_room/validate_map.py <mod根目录> --game-root "<CK3安装目录>\game"
python map_room/validate_map.py <mod根目录> --deep        # 附加河流拓扑检查
```

退出码 = ERROR 数。原版 1.20.1 全量验收：ERROR 0。
依赖 Pillow（`pip install pillow`）；`--deep` 另需 numpy。

### 3. 工作流指南（本目录 `WORKFLOW.md`）

启动编辑器、图像层+ID 图谱的心智模型、改图循环、常见故障对照表、
1.18+ 新规则速查。**动手改图前先读它。**

## 规划中：地图生成器（暂缓）

输入真实地球高程（GEBCO/NASA）或用户草图，离线生成全套图像+数据粗坯，
玩家再进编辑器 repack 烘焙、手绘细节（两阶段烘焙架构）。
**当前搁置**：CK3 新版本将对地图管线大改，等新版本落地、格式稳定后再开工；
届时第一张工单是「最小可启动集实验」（见 WORKFLOW.md 第 7 节已知未知）。
