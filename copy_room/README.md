# 抄写室（Copy Room）—— 缮写室的其他 Mod 知识库组

> 缮写室的 scriptorium 主体服务**原版** CK3；抄写室为**其他 mod**（工坊或本地）
> 建立同构知识库，帮助子 mod（sub-mod/兼容补丁）开发：查父 mod 新增的
> effect/trigger/on_action 签名、条目定义在哪个文件、与原版 API 面的差异。

## 名字

scriptorium（缮写室）诸房间之一。抄写室是缮写室里**对着底本誊抄衍生作品**
的房间——父 mod 就是子 mod 开发的"底本"。兄弟房间：地图室（map_room）、
阅览室（reading_room）。

## 架构（双通道，全部复用现有管线）

| 通道 | 产物 | 前置条件 |
|---|---|---|
| 签名层（权威） | `mods_docs/<mod>/script_docs/`（12 清单，mod 加载态 dump 转换） | **用户以目标 mod 加载态进游戏跑 `script_docs` + `dump_data_types`**（两条都要，产物在 Documents\...\Crusader Kings III\logs\） |
| 结构层（导航） | `mods_docs/<mod>/structure/`（INDEX + entry_map.tsv + common 逐子目录摘要） | 无需启动游戏，直接扫 mod 文件夹 |
| 差异报告 | `mods_docs/<mod>/DIFF_vs_vanilla.md` | 自动生成：该 mod 相对原版新增/移除的签名条目清单（子 mod 可调用的新 API 面） |

**实测依据（2026-11-09，Elder Kings 2）**：加载 mod 后 dump 为"原版+mod"合并
视图（effects +4、triggers +13、on_actions +145、custom_localization +641、
data_types +245；代码侧原生清单零变化）——dump 通道对 mod 有效且必要。

## 怎么用

```bat
:: 1) 看本机有哪些 mod 可建（工坊 + 本地，含 id/名字/路径）：
python scripts\copy_room.py --list

:: 2) 带目标 mod 启动游戏（-debug_mode），控制台跑 script_docs 和
::    dump_data_types，退出游戏（dump 落在 Documents\...\logs\）

:: 3) 建 mod 知识库（--id 取自 --list；或 --path 直接指 mod 文件夹）：
python scripts\copy_room.py --build --id 2887120253

:: 4) 并入 catalog 检索目录（抄写室区块）：
python scripts\copy_room.py --sync
```

## 发布边界（重要）

`mods_docs/` **不随仓库发布**（.gitignore 已排除）：mod 内容版权归各 mod
作者，且体积可观。任何用户按上面四步都能在自己机器上重建等价物——这与
game logs/ 的处理一致。抄写室的**代码与文档**（本目录 + scripts/copy_room.py）
随仓库发布。

## 检索约定

子 mod 开发问答时：mod 专属签名优先查 `mods_docs/<mod>/script_docs/`，
条目定位查 `mods_docs/<mod>/structure/entry_map.tsv`；与原版同名条目冲突时
以 mod 层为准（子 mod 运行在父 mod 环境里）；原版行为回查 `game_docs/`。
