# common/struggle 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：5（其中 Jomini 解析 3 个）
- 顶层块条目总数：129，跨文件唯一条目 129
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `catalysts/_catalysts.info` | 279 | - | - | 纯文档（非 Jomini） |
| `catalysts/catalysts.txt` | 6894 | 127 | 0 | jomini |
| `struggles/_struggles.info` | 5085 | - | - | 纯文档（非 Jomini） |
| `struggles/iberian_struggle_script.txt` | 26041 | 1 | 0 | jomini |
| `struggles/persian_struggle_script.txt` | 20943 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### catalysts/catalysts.txt（127 条目）

- catalyst_concession_progress_transfered
- catalyst_successfully_expelled_interloper
- catalyst_conducted_border_raid
- catalyst_winning_large_conquest_war
- catalyst_win_any_war_within_the_region
- catalyst_supporter_declare_unfair_war_within_the_region
- catalyst_supporter_declare_fair_war_within_the_region
- catalyst_supporter_win_unfair_war_within_the_region
- catalyst_supporter_win_fair_war_within_the_region
- catalyst_detractor_declare_unfair_war_within_the_region
- catalyst_detractor_declare_fair_war_within_the_region
- catalyst_detractor_win_unfair_war_within_the_region
- catalyst_detractor_win_fair_war_within_the_region
- catalyst_defeated_any_faction_duke_and_above
- catalyst_lost_to_any_faction_duke_and_above
- catalyst_raided_involved
- catalyst_populist_uprise
- catalyst_war_ends_in_white_peace_between_supporter_detractor
- catalyst_install_loyalist_cb
- catalyst_caliph_or_emperor_loses_revolt_war
- catalyst_caliph_or_emperor_accepts_faction_demands
- catalyst_hybridise_or_diverge_regional_cultures
- catalyst_very_important_child_change_culture_or_faith
- catalyst_toledo_council_compromise
- catalyst_toledo_council_conciliation
- catalyst_toledo_council_hostility
- catalyst_toledo_council_tension
- catalyst_creating_a_holy_order
- catalyst_invite_diff_faith_culture_to_feast
- catalyst_bought_important_truce
- catalyst_formed_interreligious_alliance_with_important_character
- catalyst_broke_truce_against_important_character
- catalyst_forming_alliance_with_major_uninvolved_power
- catalyst_forming_alliance_between_independent_involved_rulers
- catalyst_forming_alliance_between_supporter_detractor_rulers
- catalyst_forming_alliance_between_detractor_uninvolved_rulers
- catalyst_truce_was_enforced
- catalyst_gift_independent_ruler
- catalyst_gift_supporter_detractor_ruler
- catalyst_join_war_as_assisant
- catalyst_sign_truce_outside_war
- catalyst_grant_privilege_to_diff_faith_culture_vassal
- catalyst_demanding_important_conversion
- catalyst_accepted_demand_from_faction_requesting_culture_faith_conversion
- catalyst_granted_powerful_diff_faith_vassal_religious_protection
- catalyst_revoked_powerful_diff_faith_vassal_religious_protection
- catalyst_gave_independence_to_powerful_diff_faith_culture_vassal
- catalyst_forced_conversion
- catalyst_supporter_forced_conversion
- catalyst_detractor_forced_conversion
- catalyst_convert_local_culture_faith
- catalyst_ruler_chooses_persian_faith
- catalyst_became_supporter_fp3
- catalyst_became_detractor_fp3
- catalyst_revealed_secret_faith_islam
- catalyst_revealed_secret_faith_non_islam
- catalyst_passing_of_time
- catalyst_missing_caliphate_or_arabian_empire
- catalyst_execute_important
- catalyst_execute_supporter
- catalyst_execute_detractor
- catalyst_release_important
- catalyst_release_supporter_detractor
- catalyst_ransom_important
- catalyst_ransom_supporter_detractor
- catalyst_imprison_important
- catalyst_imprison_detractor
- catalyst_imprison_supporter
- catalyst_new_building_in_castle
- catalyst_new_building_in_city
- catalyst_new_building_in_temple
- catalyst_new_islamic_temple_construction
- catalyst_improve_development_vassal_diff_faith_culture
- catalyst_grant_land_local_noble
- catalyst_revoke_title
- catalyst_new_building_in_holdings
- catalyst_grants_vassal_to_de_jure_liege_supporter_detractor
- catalyst_becomes_rival_with_involved
- catalyst_becomes_rival_supporter_detractor
- catalyst_became_best_friend_soulmate_with_very_important_character
- catalyst_became_best_friend_soulmate_supporter_detractor
- catalyst_became_friend_lover_with_character
- catalyst_became_friend_lover_supporter_detractor
- catalyst_unnatural_death_important_character
- catalyst_unnatural_death_supporter
- catalyst_unnatural_death_detractor
- catalyst_learned_new_language_important
- catalyst_fabricating_duchy_level_claims
- catalyst_using_a_hook_on_very_important_character
- catalyst_discovery_of_very_important_murder
- catalyst_reveal_secret_important
- catalyst_reveal_secret_supporter
- catalyst_reveal_secret_detractor
- catalyst_gain_claim_on_title_fp2
- catalyst_gain_claim_on_title_fp3
- catalyst_usurp_title_fp2
- catalyst_usurp_title_fp3
- catalyst_enforcing_de_jure_claims
- catalyst_accepted_independence_faction_demands
- catalyst_vassalize_independent_ruler
- catalyst_independence_from_non_dejure_vassal
- catalyst_interloper_uninvolved_gain_struggle_titles
- catalyst_interloper_uninvolved_gain_struggle_vassals
- catalyst_gain_struggle_vassals_from_interlopers_uninvolved
- catalyst_gain_struggle_titles_from_interlopers_uninvolved
- catalyst_cadet_branch_created
- catalyst_yearly_influential_house_is_harmonious
- catalyst_yearly_influential_house_is_harmonious_major
- catalyst_yearly_influential_house_is_harmonious_medium
- catalyst_yearly_influential_house_is_harmonious_minor
- catalyst_yearly_influential_house_is_harmonious_minimal
- catalyst_yearly_influential_house_is_antagonistic
- catalyst_yearly_influential_house_is_antagonistic_major
- catalyst_yearly_influential_house_is_antagonistic_medium
- catalyst_yearly_influential_house_is_antagonistic_minor
- catalyst_yearly_influential_house_is_antagonistic_minimal
- catalyst_invite_involved_as_honorary_guests_to_feast_hunt
- catalyst_coronation_event_stabilization
- catalyst_coronation_event_unrest
- catalyst_coronation_event_concession
- catalyst_abandon_hook_on_supporter_detractor
- catalyst_grants_pardon_supporter_detractor
- catalyst_caliph_vassalize_independent_rulers
- catalyst_turn_supporter_into_detractor
- catalyst_turn_detractor_into_supporter
- catalyst_caliph_died_naturally
- catalyst_caliph_died_violently

### struggles/iberian_struggle_script.txt（1 条目）

- iberian_struggle

### struggles/persian_struggle_script.txt（1 条目）

- persian_struggle

### 未解析文件

- `catalysts/_catalysts.info` — 纯文档（非 Jomini）
- `struggles/_struggles.info` — 纯文档（非 Jomini）
