# CK3 地图工作流指南（地图室）

> 权威顺序同知识库：`game_docs/map_docs/`（游戏 1.20.1 实测档案）> `pages/Map modding.md`
> （wiki oldid 34676，页面标注版本 1.1）。本文所有版本敏感结论都带来源；
> 未经 1.20 验证的历史偏方会明确标注。配套工具：`map_room/validate_map.py`。

## 1. 打开地图编辑器

编辑器内嵌于游戏本体，无独立程序（证据见 dossier「编辑器状态」节）：

1. Steam 库 → 右键 CK3 → 属性 → 通用 → 启动选项，填 `-mapeditor`；
2. 正常启动游戏即进入编辑器（先确保已有一个能跑的地图/可用的 mod 再动手改）。

`-debug_mode` 是另一套东西（控制台/校验日志/nudger），两者可按需分别使用；
校验 mod 时建议 `-debug_mode` 看 `error.log`。

## 2. 地图 = 图像层 + ID 图谱（先建立正确心智模型）

| 半边 | 文件 | 说明 |
|---|---|---|
| 图像 | `heightmap.png`（16bit 灰度，省份图 **2 倍边长**） | 几何高程；改后必须 repack |
| 图像 | `provinces.png`（8bit RGB 平色） | 每种颜色 = 一个男爵领/海域 |
| 图像 | `rivers.png`（**索引色**，19 色合法调色板） | 河流+海岸编码；最容易 CTD 的文件 |
| 数据 | `definition.csv`（`id;r;g;b;名称;x;`） | 颜色↔省份 id；**id 必须连续** |
| 数据 | `default.map` | sea_zones / river_provinces 区段（陆海判定） |
| 数据 | `adjacencies.csv` | 跨海/大河连接；**末尾终止行必须保留** |
| 脚本 | `common/landed_titles/` | b_（`province = id`）→ c/d/k/e 层级 |
| 脚本 | `history/provinces/` | 地产/文化/宗教（首男爵领必须有 holding） |
| 脚本 | `common/province_terrain/` | 逐省地形（17 种，1.20 实测） |
| 派生 | `packed/indirection_heightmap.png`、`nodes.dat` | **编辑器 repack 生成，勿手编** |

尺寸/格式的实测细节见 `game_docs/map_docs/map_data_dossier.md`；逐省查色用
`game_docs/map_docs/province_index.tsv`（`grep -P "^<id>\t"`）。

## 3. 标准工作流（改图循环）

1. **从原版复制起步**，不要从零造文件——尤其 `rivers.png` 必须以原版文件为底
   （GIMP 导出会重排调色板导致 CTD；导出时保留色彩配置、绝对比色 intent）。
2. 在图像编辑器（GIMP/Krita/Photoshop）里改 `heightmap.png` / `provinces.png` /
   `rivers.png`：provinces 只用**平色**、关抗锯齿、关透明；heightmap 保持
   16bit 灰度、无 alpha（RGBA 导出会出现白雾，wiki 记载）。
3. 同步数据侧：`definition.csv` 新颜色新 id（连续）、`default.map` 海区段、
   `adjacencies.csv`（保留终止行）、landed_titles / history / province_terrain。
4. **跑校验器**：`python map_room/validate_map.py <mod目录> --game-root <CK3的game目录>`
   （退出码 0 再进游戏；ERROR 修完，WARN 看着办）。
5. **编辑器 repack**：改过 heightmap（或河流/边界不听话）就在编辑器里 repack——
   它会重新生成 packed/indirection 高度图（dossier：1.18+ 分块体系的唯一合法产源）。
6. 游戏 `-debug_mode` 里看 `error.log`，回第 2 步。

> 1.1 时代 wiki 的「自定义高度图导入五步偏方」（删原版 indirection/packed 再验证
> 文件完整性那套）**未在 1.20 复验**，仅作历史参考；1.18+ 分块格式下优先走
> 编辑器 repack 正路。

## 4. 常见故障对照（症状 → 原因 → 校验器检查项）

| 症状 | 原因 | 检查 |
|---|---|---|
| 载入即 CTD | rivers.png 非索引色/调色板外颜色 | M06 |
| 载入即 CTD | provinces.png 带抗锯齿杂色/非 RGB | M04/M05 |
| 无限载入 | adjacencies.csv 末尾终止行丢失 | M09 |
| 崩溃 | definition.csv id 不连续 | M02 |
| 河流/边界/头衔“不听”高度图 | 改 heightmap 后没 repack | —（编辑器操作） |
| 地图北侧大片黑 | 1.9 起的宽高比 bug（wiki 记载，调宽度绕开） | — |
| 白雾 | heightmap 被导出成 RGBA（带 alpha） | M07 |
| 海陆判定错乱 | 改省份布局没同步 default.map 区段 | M10 |
| 省份无头衔不可用 | landed_titles 缺 b_ 条目 | M12 |

## 5. 1.18+ 新规则速查（wiki 尚未更新，实测来源 dossier）

- heightmap = 省份图 **2 倍边长**（旧教程的同尺寸规则是 1.17 及以前）；
- indirection_heightmap = 省份图 1/32；packed 为压缩打包形态（repack 产物）；
- 逐像素地形蒙版移到了 `gfx/map/terrain/masks/`（70 张）与 `masks_gen/`（52 张），
  旧教程“63 张 _mask 在 terrain 根目录”已过时；
- wiki 自定义分辨率章节整体挂着“1.18/1.19 起部分过时”横幅，比例系数仍可参考，
  文件位置以 dossier 为准。

## 6. 校验器检查项一览

M01 definition 解析 · M02 id 连续 · M03 颜色唯一/黑位 · M04 图像模式与尺寸 ·
M05 图↔csv 色集一致 · M06 rivers 调色板 · M07 heightmap 规格与倍率 ·
M08 heightmap.heightmap 尺寸 · M09 adjacencies · M10 default.map ·
M11 province_terrain · M12 landed_titles 引用 · M13 河流拓扑（`--deep`，启发式）。

## 7. 已知未知（改图时留意，勿想当然）

- `nodes.dat`（44MB）无 default.map 引用，疑为编辑器生成的寻路数据——**删除/手改
  的后果未实验**；
- `default.map` 的 `continent = "continent.txt"` 是幽灵引用（原版也没有该文件）；
- 视觉层（masks/colormap/flatmap）在新分辨率下的完整缩放规则未在 1.20 复验；
- 最小可启动文件集（砍到多小游戏还能载入）未实验——这是地图生成器（规划中）
  的第一张工单。
