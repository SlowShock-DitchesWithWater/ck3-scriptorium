# common/subject_contracts 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：18（其中 Jomini 解析 16 个）
- 顶层块条目总数：87，跨文件唯一条目 87
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `contracts/_subject_contracts.info` | 8614 | - | - | 纯文档（非 Jomini） |
| `contracts/administrative.txt` | 10455 | 3 | 0 | jomini |
| `contracts/celestial.txt` | 31817 | 14 | 0 | jomini |
| `contracts/clan.txt` | 1896 | 1 | 0 | jomini |
| `contracts/default_tributary.txt` | 2501 | 3 | 0 | jomini |
| `contracts/feudal.txt` | 4465 | 3 | 0 | jomini |
| `contracts/herder.txt` | 156 | 1 | 0 | jomini |
| `contracts/japan_administrative.txt` | 6660 | 3 | 0 | jomini |
| `contracts/mandala.txt` | 4872 | 4 | 0 | jomini |
| `contracts/meritocratic.txt` | 13367 | 7 | 0 | jomini |
| `contracts/nomad.txt` | 5928 | 3 | 0 | jomini |
| `contracts/republic.txt` | 2523 | 1 | 0 | jomini |
| `contracts/special_contracts.txt` | 20800 | 17 | 2 | jomini |
| `contracts/theocratic.txt` | 906 | 1 | 0 | jomini |
| `contracts/tribal.txt` | 392 | 1 | 0 | jomini |
| `contracts/wanua.txt` | 1228 | 2 | 0 | jomini |
| `groups/_subject_contract_groups.info` | 2570 | - | - | 纯文档（非 Jomini） |
| `groups/subject_contract_groups.txt` | 6953 | 23 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### contracts/administrative.txt（3 条目）

- administrative_obligations
- administrative_themes
- administrative_salary_rank

### contracts/celestial.txt（14 条目）

- celestial_obligations
- celestial_provinces
- celestial_ministry_obligations
- celestial_treasury
- celestial_ministry_budget
- celestial_salary
- celestial_salary_rank
- celestial_tribute_gold
- celestial_tribute_prestige
- celestial_tributary_investiture_privilege_trade
- celestial_tributary_investiture_privilege_marriage
- celestial_tributary_investiture_privilege_politics
- hegemonic_tribute_gold
- hegemonic_tribute_prestige

### contracts/clan.txt（1 条目）

- clan_tax_collector_obligations

### contracts/default_tributary.txt（3 条目）

- default_tributary_taxes
- default_tributary_levies
- default_tributary_prestige

### contracts/feudal.txt（3 条目）

- feudal_government_taxes
- feudal_government_levies
- feudal_government_prestige

### contracts/herder.txt（1 条目）

- herder_government_obligations

### contracts/japan_administrative.txt（3 条目）

- japan_administrative_obligations
- japan_administrative_provinces
- japan_administrative_salary

### contracts/mandala.txt（4 条目）

- mandala_government_piety
- mandala_government_taxes
- mandala_government_levies
- mandala_government_prestige

### contracts/meritocratic.txt（7 条目）

- meritocratic_obligations
- meritocratic_provinces
- meritocratic_treasury
- meritocratic_salary
- meritocratic_salary_rank
- meritocratic_tribute_gold
- meritocratic_tribute_prestige

### contracts/nomad.txt（3 条目）

- nomad_government_herd
- nomad_government_taxes
- nomad_government_prestige

### contracts/republic.txt（1 条目）

- republic_government_obligations

### contracts/special_contracts.txt（17 条目）

- special_contract
- religious_rights
- fortification_rights
- coinage_rights
- succession_rights
- war_declaration_rights
- council_rights
- title_revocation_rights
- jizya_special_rights
- iqta_special_rights
- ghazi_special_rights
- marriage_favor_rights
- kurultai_rights
- liege_war_participation_obligation
- suzerain_war_participation_guarantee
- mandala_suzerain_war_participation_guarantee
- tributary_war_participation_obligation

### contracts/theocratic.txt（1 条目）

- theocracy_government_obligations

### contracts/tribal.txt（1 条目）

- tribal_government_obligations

### contracts/wanua.txt（2 条目）

- wanua_obligations
- barter_goods_obligations

### groups/subject_contract_groups.txt（23 条目）

- feudal_vassal
- republic_vassal
- theocracy_vassal
- clan_vassal
- tribal_vassal
- admin_vassal
- nomad_vassal
- tributary_settled
- tributary_nomadic
- tributary_subjugated
- tributary_steppe
- herder_vassal
- celestial_vassal
- tributary_celestial
- tributary_hegemonic
- mandala_vassal
- tributary_mandala
- tributary_mandala_tribal
- japan_administrative_vassal
- japan_feudal_vassal
- wanua_vassal
- tributary_wanua
- meritocratic_vassal

### 未解析文件

- `contracts/_subject_contracts.info` — 纯文档（非 Jomini）
- `groups/_subject_contract_groups.info` — 纯文档（非 Jomini）
