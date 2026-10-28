<!-- 来源: https://ck3.paradoxwikis.com/Event_modding oldid=37279 抓取于 2026-10-22T21:40:25+08:00 -->

# Event modding

> [!] This article is timeless and should be accurate for any version of the game.

|  | Please help improve this article or section by **expanding it**. |
| --- | --- |

Events are the meat of every well-rounded mod; smaller and larger bits of story that can happen to a player during the campaign.

**Checklist.** Your events must:

- be in `your_mod\events\` folder
- have a .txt extension
- have a namespace defined on the first line, like `namespace = my_events`
- use the namespace as their name + number, like `my_events.1 = {...`
- be fired from script in some way, like by an on_action

Events do not fire automatically otherwise, like in older games. Other ways to fire them are decisions, character interactions, story cycles, etc.


> [!] 本页为章节索引：清洗产物 60191B，已按 H2 拆为 13 个章节文件（目录 `Event modding/`，各文件自包含、原文逐字）。
> organize 阶段已做逐行重组校验：章节文件重组与清洗原文逐字节一致（零丢失零重复）。

## 章节文件

- `01-Scripting-Tools.md` — Scripting Tools（14152B）
- `02-Location.md` — Location（262B）
- `03-Structure.md` — Structure（2712B）
- `04-Portraits.md` — Portraits（7678B）
- `05-Themes.md` — Themes（4851B）
- `06-Trigger.md` — Trigger（1784B）
- `07-Description.md` — Description（8746B）
- `08-Immediate.md` — Immediate（577B）
- `09-Options.md` — Options（4403B）
- `10-After.md` — After（950B）
- `11-Widgets.md` — Widgets（96B）
- `12-On-Actions-on_action.md` — On Actions (on_action)（12311B）
- `13-Strategy.md` — Strategy（799B）
