# auto-nudge 摆放参数表（auto_nudger_settings.json）

- 来源：游戏安装 `tools/mapeditor/auto_nudger_settings.json` 实测（数值列为原版当前值，重跑 `scripts/map_layer.py` 刷新）。
- 背景：wiki（pages/Map modding.md「Auto nudge」节）记载可在编辑器里微调自动摆放；本表把随游戏分发的全部约 60 个参数连同数值列出。
- **语义均为参数名 + 数值语境的推断，官方无文档**（仅 `building_priority`/`avoid_distance` 的「对象优先级/间距」语义有 wiki 原文背书）；拿不准的参数改前先在编辑器里做对照实验。

## building_priority

语义（推断）：各类对象自动摆放的优先级（数值小=先摆）

| 参数 | 原版值 |
|---|---|
| `buildings` | `5` |
| `special_buildings` | `0` |
| `stack_player` | `3` |
| `combat` | `2` |
| `siege` | `4` |
| `activities` | `1` |

## avoid_distance

语义（推断）：各类对象之间的最小间距（地图单位）

| 参数 | 原版值 |
|---|---|
| `buildings` | `5` |
| `special_buildings` | `1` |
| `stack_player` | `5` |
| `combat` | `10` |
| `siege` | `7` |
| `activities` | `5` |

## siege_pattern

语义（推断）：攻城器械落点的采样模式（距点距离/坡度/离边距离/避南北因子）

| 参数 | 原版值 |
|---|---|
| `dist_to_point_min` | `5.15` |
| `dist_to_point_max` | `9.75` |
| `steep_factor` | `0.25` |
| `steep_threshold_min` | `0.25` |
| `steep_threshold_max` | `0.75` |
| `dist_to_edge_max` | `2` |
| `avoid_south_factor` | `1` |
| `avoid_north_factor` | `0.25` |

## stack_player_pattern

语义（推断）：玩家部队堆叠落点模式（水平/垂直偏移与离边距离）

| 参数 | 原版值 |
|---|---|
| `distance_h` | `10` |
| `distance_v` | `-8` |
| `dist_to_edge_max` | `2` |

## combat_pattern

语义（推断）：战斗场景落点模式

| 参数 | 原版值 |
|---|---|
| `dist_to_point_min` | `1` |
| `dist_to_point_max` | `2` |
| `steep_factor` | `0.5` |
| `steep_threshold_min` | `0` |
| `steep_threshold_max` | `1` |
| `dist_to_edge_max` | `0` |
| `avoid_south_factor` | `1` |
| `avoid_north_factor` | `1` |

## building_pattern

语义（推断）：地产建筑落点模式（范围/朝南偏好/南岸距离）

| 参数 | 原版值 |
|---|---|
| `range_min` | `2` |
| `range_max` | `12` |
| `to_south_mult` | `12` |
| `dist_to_southern_shore_min` | `2` |
| `dist_to_southern_shore_max` | `4` |
| `southern_shore_score` | `2` |
| `steep_factor` | `0.25` |
| `steep_threshold_min` | `0.25` |
| `steep_threshold_max` | `0.75` |

## special_building_pattern

语义（推断）：特殊建筑落点模式

| 参数 | 原版值 |
|---|---|
| `dist_to_point_min` | `5.15` |
| `dist_to_point_max` | `9.75` |
| `steep_factor` | `0.25` |
| `steep_threshold_min` | `0.25` |
| `steep_threshold_max` | `0.75` |
| `dist_to_edge_max` | `2` |
| `avoid_south_factor` | `1` |
| `avoid_north_factor` | `1` |

## activities_pattern

语义（推断）：活动场景落点模式

| 参数 | 原版值 |
|---|---|
| `dist_to_point_min` | `1` |
| `dist_to_point_max` | `2` |
| `steep_factor` | `0.5` |
| `steep_threshold_min` | `0` |
| `steep_threshold_max` | `1` |
| `dist_to_edge_max` | `0` |
| `avoid_south_factor` | `1` |
| `avoid_north_factor` | `1` |

## rotation_unit_stack_player

语义（推断）：部队堆叠旋转角范围（from/to 弧度）

| 参数 | 原版值 |
|---|---|
| `from` | `0` |
| `to` | `0` |

## rotation_combat

语义（推断）：战斗场景旋转角范围

| 参数 | 原版值 |
|---|---|
| `from` | `0` |
| `to` | `0` |

## rotation_special_building

语义（推断）：特殊建筑旋转角范围

| 参数 | 原版值 |
|---|---|
| `from` | `0` |
| `to` | `0` |

## rotation_buildings

语义（推断）：建筑旋转角范围

| 参数 | 原版值 |
|---|---|
| `from` | `0` |
| `to` | `0` |

## rotation_activities

语义（推断）：活动场景旋转角范围

| 参数 | 原版值 |
|---|---|
| `from` | `0` |
| `to` | `0` |

