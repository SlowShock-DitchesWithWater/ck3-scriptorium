# common/scripted_animations 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：3（其中 Jomini 解析 2 个）
- 顶层块条目总数：16，跨文件唯一条目 16
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_scripted_animations.txt` | 15494 | 15 | 0 | jomini |
| `_scripted_animations.info` | 2173 | - | - | 纯文档（非 Jomini） |
| `pam_scripted_animations.txt` | 2608 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_scripted_animations.txt（15 条目）

- duel_wield_weapon
- duel_celebrate
- idle
- bow_drawn
- bow_closed
- bow_drawn_blunt
- bow_closed_blunt
- scheme_prep_pick_best_stance
- coronation_guest_animation
- coronation_host_animation
- ecumenical_council_host_animation
- ecumenical_council_clergy_guest_animation
- ecumenical_council_clergy_guest_animation_alt
- ecumenical_council_lay_guest_animation
- ecumenical_council_lay_guest_animation_alt

### pam_scripted_animations.txt（1 条目）

- pam_reincarnation_personality_animation

### 未解析文件

- `_scripted_animations.info` — 纯文档（非 Jomini）
