# 地图数据档案（map_docs dossier）

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与内容指纹见 manifest.json 的 game_docs.map_docs）
- 生成方式：`scripts/map_layer.py` 实测提取（PNG 头解析 / CSV 统计 / exe 字符串灰盒扫描），零推测、零原版内容复制。
- 权威顺序：本档案（游戏实测）> wiki 层（pages/Map modding.md，oldid 34676，页面标注版本 1.1）。冲突点在各节单独标注。
- 配套工具：`map_room/validate_map.py`（地图校验器）；工作流向导见 `map_room/WORKFLOW.md`。

## map_data/ 文件实测清单

共 14 个文件 + geographical_regions/ 子目录（4 个文件）。

| 文件 | 字节 | 实测规格 |
|---|---|---|
| `adjacencies.csv` | 20541 | 353 条连接；终止行在 |
| `climate.txt` | 3181 |  |
| `default.map` | 16084 | 8 个生效文件引用；含幽灵引用 |
| `definition.csv` | 432072 | 13270 活动行 + 874 注释行 |
| `heightmap.heightmap` | 293 | 分块索引（见下节全文） |
| `heightmap.png` | 122165778 | 18432×9216 · 16bit 灰度（colortype 0） |
| `indirection_heightmap.png` | 40357 | 288×144 · 8bit RGBA（colortype 6） |
| `island_region.txt` | 2147 |  |
| `nodes.dat` | 44739232 | 二进制（无 default.map 引用；疑为编辑器生成的寻路数据，待实验确认） |
| `packed_heightmap.png` | 16829933 | 3185×4061 · 16bit 灰度（colortype 0） |
| `positions.txt` | 349525 |  |
| `provinces.png` | 2488311 | 9216×4608 · 8bit RGB（colortype 2） |
| `rivers.png` | 601095 | 9216×4608 · 8bit 索引色（colortype 3） |
| `seasons.txt` | 733 |  |

### 关键尺寸关系（1.18+ 实测，wiki 未记载）

- heightmap.png 18432×9216 恰为 provinces.png/rivers.png 9216×4608 的 **2 倍边长**（4 倍像素）。
- wiki（oldid 34676，1.1 时代）"heightmap 与 provinces 同尺寸"的规则只适用于 1.17 及以前；1.18/1.19 起高度图独立为 2 倍分辨率分块体系（packed/indirection 两张派生图由编辑器 repack 生成）。
- indirection_heightmap.png 288×144 · 8bit RGBA（colortype 6）：寻址图，实测边长为 provinces.png 的 **1/32**（= heightmap 的 1/64）；wiki 旧文 "×1/32" 以 1.1 时代单一地图尺寸表述，按省份图口径衡量仍符。packed_heightmap.png 3185×4061 · 16bit 灰度（colortype 0）：非原图尺寸的压缩打包形态（repack 产物）。

## heightmap.heightmap（1.18+ 分块格式，全文）

```
heightmap_file="map_data/packed_heightmap.png"
indirection_file="map_data/indirection_heightmap.png"
original_heightmap_size={ 18432 9216 }
tile_size=65
should_wrap_x=no
level_offsets={ { 0 0 } { 0 1397 } { 0 3129 } { 0 3690 } { 0 3861 } }
max_compress_level=4
empty_tile_offset={ 225 39 }
```

字段注解（语义标注【推断】者为参数名推断，非官方文档）：`heightmap_file`/`indirection_file` 指向派生图；`original_heightmap_size` 必须等于 heightmap.png 实际尺寸；`tile_size`【推断】分块像素宽；`level_offsets`【推断】各压缩级别的行偏移；`max_compress_level`【推断】最大压缩级别数；`empty_tile_offset`【推断】空块指针。**此文件由编辑器 repack 生成，手改 heightmap 后应在编辑器里重打包，而非手编此文件。**

## definition.csv 实测

- 行格式：`id;r;g;b;名称;x;`（UTF-8 无 BOM、无引号字段；第 6 列原版恒为字面值 `x`；`#` 前缀为注释行）。
- 活动行 13270 个，id 0..13269 完全连续（缺口 0 个）；注释行 874 个，全部落在活动区间之外（历史遗留省份，仅作参考）。
- id 0 为水体（0;0;0;0;x;x;）；黑色 (0,0,0) 为保留色。活动行重复色 1 组。
- **wiki 冲突注记**：wiki 示例表头与首列语义（"ID From" 等）与实测不符——实测第 5 列为男爵领名（大写）、无独立 type 列；陆海类型由 default.map 的 sea_zones/river_provinces 区段表达。以本节实测为准。
- 逐省索引：`province_index.tsv`（同目录；`grep -P "^<id>\t"` 或按名称 grep）。

## rivers.png 调色板实测

索引色 PNG（colortype 3），256 槽调色板，实际用色 19 种：

| 颜色 | wiki 语义（oldid 34676） | 备注 |
|---|---|---|
| `#000064` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#000096` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#0000c8` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#0000e1` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#0000ff` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#005500` | — | **wiki 未记载，原版在用**（校验器降级为 WARN） |
| `#0064ff` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#007d00` | — | **wiki 未记载，原版在用**（校验器降级为 WARN） |
| `#0096ff` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#009e00` | — | **wiki 未记载，原版在用**（校验器降级为 WARN） |
| `#00c8ff` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#00e1ff` | — | wiki 记载：蓝色梯度，越暗越宽 |
| `#00ff00` | 河流系统源头（每系统仅一个） | wiki 记载 |
| `#020001` | — | 近黑占位槽（index 0 附近，疑未使用） |
| `#18ce00` | — | **wiki 未记载，原版在用**（校验器降级为 WARN） |
| `#ff0000` | 支流汇入（流向该像素） | wiki 记载 |
| `#ff0080` | 海/湖/可航河道 | wiki 记载 |
| `#fffc00` | 河流分叉（流离该像素） | wiki 记载 |
| `#ffffff` | 陆地 | wiki 记载 |

- wiki 称"调色板外颜色（含抗锯齿/透明）即 CTD"；实测原版自身携带 4 个未记载绿色变体，说明引擎对部分色有容忍——**安全做法仍是从原版 rivers.png 起步**（校验器对未记载色报 WARN 而非 ERROR）。

## default.map 实测

- 生效文件引用 8 个：`definitions`、`provinces`、`rivers`、`topology`、`continent`、`adjacencies`、`island_region`、`seasons`。
- **幽灵引用**（default.map 引用但 map_data/ 无此文件，原版亦如此，疑可选/遗留）：`continent = "continent.txt"`
- `sea_zones`：47 个 RANGE/LIST 区段，覆盖 id 约 463 个；`river_provinces`：42 个区段，覆盖 id 约 218 个（可航大河，陆海军通行规则见 wiki Map modding）。
- 修改省份 id 布局后必须同步更新这两类区段，否则海陆判定错乱。

## adjacencies.csv 实测

- 实测表头：`From;To;Type;Through;start_x;start_y;stop_x;stop_y;Comment`（wiki 示例表头 "ID From;…" 与原版不一致，以实测为准）。
- 连接条目 353 条；Type 实测取值：`river_large`、`sea`。
- 末尾终止行 `-1;-1;;-1;-1;-1;-1;-1;` 原版**存在**（wiki 警告缺失会导致无限载入，实测印证其必要性）。
- 坐标可用 `-1` 表示用默认军队落点；`#` 行为注释。

## 编辑器（-mapeditor）状态证据（灰盒实测）

- 主程序 `Crusader Kings III\binaries\ck3.exe` 101,125,752 字节；mapeditor/nudge 相关字符串 22 条：
  ```
  -mapeditor
  .nudger_metadata.json
  auto_nudger_settings
  gfx/FX/jomini/mapeditor/mapeditor.shader
  gui/map_editor/mapeditor.gui
  gui/map_editor/mapeditor.shortcuts
  mapeditor
  mapeditor.cpp
  mapeditor_auto_nudge.cpp
  mapeditor_border_helper.cpp
  mapeditor_composite_spline_graphics.cpp
  mapeditor_detail_data.cpp
  mapeditor_heightmap.cpp
  mapeditor_interface.cpp
  mapeditor_spline_network.cpp
  nudge
  nudger
  nudger.cpp
  nudger_mapcontent.cpp
  nudger_settings
  nudger_viewport
  tools/mapeditor
  ```
  模块名（mapeditor_heightmap / border_helper / spline_network / detail_data / composite_spline_graphics / interface / auto_nudge）与启动参数 `-mapeditor` 均内嵌于二进制；专用 shader 位于 `gfx/FX/jomini/mapeditor/`。
- `tools/mapeditor/` 出厂工件：`auto_nudger_settings.json`（1,966B）；`map_editor_status.txt`（559,937B）；`mask_painter/mask_painter_meta.json`（5B）；`nudger_settings.json`（2,556,874B）
  - `map_editor_status.txt`：39,828 行开发期任务清单，`=no` 条目 39,498 个——内部工具状态文件直接随游戏分发。
  - `mask_painter/mask_painter_meta.json` 内容为 []；`content_source/TODO.txt` 亦为开发备忘（提及 map_object_painter）。
- `gui/map_editor/` 数据文件：1 个（dockable_map_mode_selector.gui）——编辑器主 UI 硬编码于二进制（exe 引用的 `gui/map_editor/mapeditor` 数据文件未随游戏分发），仅地图模式切换面板为数据驱动。
- 游戏 `script_documentation` dump 中零 mapeditor 条目（官方文档缺失；wiki 教程为社区逆向成果）。

## 视觉层速览（gfx，1.18+ 重构后形态）

- `gfx/map/terrain/`：顶层 377 个文件（每地形类型的 diffuse/normal/properties PBR 三件套）+ 子目录 `flat_maps/`（3 个）、`masks/`（70 个）、`masks_gen/`（52 个）、`unmasked/`（6 个）。
- **逐像素地形蒙版仍在，已移入子目录**：`masks/` 70 张、`masks_gen/` 52 张 `_mask.png`（wiki 1.3 时代"63 张 _mask"清单过时；自定义分辨率需缩放的就是这批蒙版 + flat_maps/）。`flat_maps/` 为平面地图贴图，`unmasked/` 为无蒙版回退材质。
- `gfx/map/water/`：9 个文件（flowmap/foam/watercolor 等，自定义分辨率仍需按 wiki 比例缩放）。
- `content_source/`：map_objects、TODO.txt（对象蒙版源数据，TODO.txt 标注其挂载意图）。

## 配套索引与工具

- 逐省索引：`province_index.tsv`（本目录）。
- auto-nudge 摆放参数表：`nudger_parameters.md`（本目录）。
- 地图校验器：`map_room/validate_map.py`（对 mod 的 map_data 做本档案全部机械检查）。
- 工作流向导（启动项 / repack / 常见故障）：`map_room/WORKFLOW.md`。
