[English](README.md) | 简体中文

# 抄写室（Copy Room）—— 缮写室的其他 Mod 知识库组

> 缮写室的 scriptorium 主体服务**原版** CK3；抄写室为**其他 mod**（工坊或本地）
> 建立同构知识库，帮助子 mod（sub-mod/兼容补丁）开发：查父 mod 新增的
> effect/trigger/on_action 签名、条目定义在哪个文件、与原版 API 面的差异。

## 名字

scriptorium（缮写室）诸房间之一。抄写室是缮写室里**对着底本誊抄衍生作品**
的房间——父 mod 就是子 mod 开发的"底本"。兄弟房间：地图室（map_room）、
阅览室（reading_room）。

## 架构（三通道，全部复用现有管线）

mod 知识库与文档同处一室：本目录下的 `<mod-id>/` 子目录即各 mod 的 KB
（本地生成，不入仓库）。原版侧的同构刷新入口是
`python scripts/run.py --stage game`（一条命令跑签名/结构/地图三通道）。

| 通道 | 产物 | 前置条件 |
|---|---|---|
| 签名层（权威） | `copy_room/<mod-id>/script_docs/`（12 清单，mod 加载态 dump 转换） | **用户以目标 mod 加载态进游戏跑 `script_docs` + `dump_data_types`**（两条都要，产物在 Documents\...\Crusader Kings III\logs\） |
| 结构层（导航） | `copy_room/<mod-id>/structure/`（INDEX + entry_map.tsv + common 逐子目录摘要） | 无需启动游戏，直接扫 mod 文件夹 |
| 地图层（换图 mod） | `copy_room/<mod-id>/map_docs/`（dossier + province_index.tsv + nudger 参数，同地图室三件套） | 无需启动游戏；mod 自带 `map_data/definition.csv` 时自动构建（EK2 这类全架空 mod 的核心知识），否则跳过 |
| 差异报告 | `copy_room/<mod-id>/DIFF_vs_vanilla.md` | 自动生成：该 mod 相对原版新增/移除的签名条目清单（子 mod 可调用的新 API 面） |

**实测依据（2026-11-09，Elder Kings 2）**：加载 mod 后 dump 为"原版+mod"合并
视图（effects +4、triggers +13、on_actions +145、custom_localization +641、
data_types +245；代码侧原生清单零变化）——dump 通道对 mod 有效且必要。

## 怎么用

```bat
:: 1) 看本机有哪些 mod 可建（工坊 + 本地，含 id/名字/路径）：
python scripts\copy_room.py --list

:: 2) 带目标 mod 启动游戏（-debug_mode），控制台跑 script_docs 和
::    dump_data_types，退出游戏（dump 落在 Documents\...\logs\）

:: 3) 建 mod 知识库（--id 取自 --list；或 --path 直接指 mod 文件夹，
::    本地 mod 可用 --name 覆盖命名；--dump 指定其他 dump 目录）：
python scripts\copy_room.py --build --id 2887120253

:: 4) 校验 catalog 抄写室区块（可选）：
python scripts\copy_room.py --check
```

签名层缺失（没跑过第 2 步）时 build 仍会完成结构层并留提示，补跑 dump 后
重新 --build 即可。

## catalog 索引约定

catalog.md 末尾的抄写室区块是**静态指引**（指向本 README 与 `ls copy_room/`），
不罗列具体 KB——mod KB 是本机产物，罗列会让发布版 catalog 依赖某台机器的
目录。每个 KB 自带 `README.md` 记录来源、组成与检索入口；`--sync` 可在区块
受损时重建，`--check` 校验其在位（CI 跑）。

## 发布边界（重要）

`copy_room/<mod-id>/` **不随仓库发布**（.gitignore 的 `copy_room/*` 规则，
本 README 除外）：mod 内容版权归各 mod 作者，且体积可观。任何用户按上面
四步都能在自己机器上重建等价物——这与 game logs/ 的处理一致。抄写室的
**代码与文档**（本 README + scripts/copy_room.py）随仓库发布。

## 检索约定

子 mod 开发问答时：mod 专属签名优先查 `copy_room/<mod-id>/script_docs/`，
条目定位查 `copy_room/<mod-id>/structure/entry_map.tsv`；与原版同名条目冲突时
以 mod 层为准（子 mod 运行在父 mod 环境里）；原版行为回查 `game_docs/`。
