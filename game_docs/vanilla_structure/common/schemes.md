# common/schemes 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：50（其中 Jomini 解析 46 个）
- 顶层块条目总数：483，跨文件唯一条目 483
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `agent_types/_agent_types.info` | 889 | - | - | 纯文档（非 Jomini） |
| `agent_types/agent_types.txt` | 148838 | 65 | 0 | jomini |
| `pulse_actions/_pulse_actions.info` | 788 | - | - | 纯文档（非 Jomini） |
| `pulse_actions/general_scheme_pulse_actions.txt` | 176628 | 315 | 1 | jomini |
| `scheme_countermeasures/00_basic_countermeasures.txt` | 27311 | 24 | 15 | jomini |
| `scheme_countermeasures/_scheme_countermeasures.info` | 1529 | - | - | 纯文档（非 Jomini） |
| `scheme_types/_schemes.info` | 12423 | - | - | 纯文档（非 Jomini） |
| `scheme_types/abduct_scheme.txt` | 8239 | 1 | 0 | jomini |
| `scheme_types/befriend_scheme.txt` | 19463 | 1 | 0 | jomini |
| `scheme_types/challenge_status_scheme.txt` | 6156 | 1 | 0 | jomini |
| `scheme_types/claim_throne_scheme.txt` | 5855 | 1 | 0 | jomini |
| `scheme_types/coerce_contribution_scheme.txt` | 5106 | 1 | 0 | jomini |
| `scheme_types/coerce_tributary_scheme.txt` | 6990 | 1 | 0 | jomini |
| `scheme_types/convert_to_witchcraft_scheme.txt` | 9245 | 1 | 0 | jomini |
| `scheme_types/court_scheme.txt` | 23687 | 1 | 0 | jomini |
| `scheme_types/damage_legitimacy_scheme.txt` | 4392 | 1 | 0 | jomini |
| `scheme_types/depose_scheme.txt` | 4898 | 1 | 0 | jomini |
| `scheme_types/diarch_schemes.txt` | 7000 | 1 | 0 | jomini |
| `scheme_types/disbelieve_mandala_scheme.txt` | 5420 | 1 | 0 | jomini |
| `scheme_types/elope_scheme.txt` | 9418 | 1 | 0 | jomini |
| `scheme_types/ep3_dispute_border_scheme.txt` | 7909 | 1 | 0 | jomini |
| `scheme_types/ep3_found_despotate_scheme.txt` | 6299 | 1 | 0 | jomini |
| `scheme_types/ep3_ingratiate_family_scheme.txt` | 7803 | 1 | 0 | jomini |
| `scheme_types/ep3_prepare_fire_dromons_scheme.txt` | 3345 | 1 | 0 | jomini |
| `scheme_types/ep3_raid_estate_scheme.txt` | 12424 | 1 | 0 | jomini |
| `scheme_types/ep3_subsume_province_scheme.txt` | 9290 | 1 | 0 | jomini |
| `scheme_types/ep3_teach_governor_scheme.txt` | 7772 | 1 | 0 | jomini |
| `scheme_types/expand_power_base_scheme.txt` | 3768 | 1 | 0 | jomini |
| `scheme_types/fabricate_hook_scheme.txt` | 12029 | 1 | 0 | jomini |
| `scheme_types/find_follower_of_faith.txt` | 4022 | 1 | 0 | jomini |
| `scheme_types/foster_legitimacy_scheme.txt` | 4864 | 1 | 0 | jomini |
| `scheme_types/generate_claim_scheme.txt` | 5507 | 1 | 0 | jomini |
| `scheme_types/laamp_base_contract_schemes.txt` | 90004 | 29 | 1 | jomini |
| `scheme_types/laamp_extra_contract_schemes.txt` | 14791 | 6 | 0 | jomini |
| `scheme_types/learn_language_scheme.txt` | 10658 | 1 | 0 | jomini |
| `scheme_types/leverage_contribution_scheme.txt` | 4735 | 1 | 0 | jomini |
| `scheme_types/murder_scheme.txt` | 9527 | 1 | 0 | jomini |
| `scheme_types/pam_study_scheme.txt` | 9095 | 1 | 0 | jomini |
| `scheme_types/promote_scheme.txt` | 5052 | 1 | 0 | jomini |
| `scheme_types/seduce_scheme.txt` | 32768 | 1 | 0 | jomini |
| `scheme_types/seize_realm_scheme.txt` | 8627 | 1 | 0 | jomini |
| `scheme_types/slander_scheme.txt` | 5414 | 1 | 0 | jomini |
| `scheme_types/steal_back_artifact_scheme.txt` | 6639 | 1 | 0 | jomini |
| `scheme_types/steal_herd_scheme.txt` | 7822 | 1 | 0 | jomini |
| `scheme_types/study_faith_scheme.txt` | 12885 | 1 | 0 | jomini |
| `scheme_types/sway_scheme.txt` | 13634 | 1 | 0 | jomini |
| `scheme_types/tgp_coup_ceremonial_liege.txt` | 7722 | 1 | 0 | jomini |
| `scheme_types/tgp_dynastic_cycle_schemes.txt` | 25441 | 4 | 0 | jomini |
| `scheme_types/tgp_mentoring_scheme.txt` | 12149 | 1 | 0 | jomini |
| `scheme_types/tgp_study_scheme.txt` | 4356 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### agent_types/agent_types.txt（65 条目）

- agent_hitman
- agent_vampire
- agent_werewolf
- agent_mage
- agent_wraith
- agent_changeling
- agent_assassin
- agent_thug
- agent_comrade_in_arms
- agent_musician
- agent_tumbler
- agent_poet
- agent_shill
- agent_diplomat
- agent_scribe
- agent_wolf_hunter
- agent_thief
- agent_tutor
- agent_poisoner
- agent_eunuch
- agent_muscle
- agent_physic
- agent_smith
- agent_ambusher
- agent_bodyguard
- agent_scout
- agent_outrider
- agent_bookkeeper
- agent_bailiff
- agent_draughtsman
- agent_outcast
- agent_devotee
- agent_wrangler
- agent_wrangler_speed
- agent_alchemist
- agent_infiltrator
- agent_footpad
- agent_socialite
- agent_gabbler
- agent_gabbler_secrecy
- agent_cleric
- agent_cleric_success
- agent_theologian
- agent_theologian_success
- agent_herald
- agent_drillmaster
- agent_tracker
- agent_planner
- agent_supplier
- agent_lookout
- agent_lookout_success
- agent_lookout_speed
- agent_alibi
- agent_justiciar
- agent_justiciar_speed
- agent_decoy
- agent_intermediary
- agent_proponent
- agent_sycophant
- agent_political_socialite
- agent_bureaucrat
- agent_bureaucrat_title
- agent_courtesan
- agent_amanuensis
- agent_eunuch_speed

### pulse_actions/general_scheme_pulse_actions.txt（315 条目）

- scheme_apa_positive.0001
- scheme_apa_positive.0011
- scheme_apa_positive.0021
- scheme_apa_positive.0031
- scheme_apa_positive.0041
- scheme_apa_positive.0051
- scheme_apa_positive.0061
- scheme_apa_positive.0071
- scheme_apa_positive.0081
- scheme_apa_positive.0091
- scheme_apa_positive.0111
- scheme_apa_positive.0121
- scheme_apa_positive.0131
- scheme_apa_positive.0141
- scheme_apa_positive.0151
- scheme_apa_positive.0161
- scheme_apa_positive.0171
- scheme_apa_positive.0181
- scheme_apa_positive.0191
- scheme_apa_positive.0201
- scheme_apa_positive.0211
- scheme_apa_positive.0221
- scheme_apa_positive.0231
- scheme_apa_positive.0241
- scheme_apa_positive.0251
- scheme_apa_positive.0261
- scheme_apa_positive.0271
- scheme_apa_positive.0281
- scheme_apa_positive.0291
- scheme_apa_positive.0301
- scheme_apa_positive.0311
- scheme_apa_positive.0321
- scheme_apa_positive.0331
- scheme_apa_positive.0341
- scheme_apa_positive.0351
- scheme_apa_positive.0361
- scheme_apa_positive.0371
- scheme_apa_positive.0381
- scheme_apa_positive.0391
- scheme_apa_positive.0401
- scheme_apa_positive.0411
- scheme_apa_positive.0421
- scheme_apa_positive.0431
- scheme_apa_positive.0441
- scheme_apa_positive.0451
- scheme_apa_positive.0461
- scheme_apa_positive.0471
- scheme_apa_positive.0481
- scheme_apa_positive.0491
- scheme_apa_positive.0501
- scheme_apa_positive.0511
- scheme_apa_positive.0521
- scheme_apa_positive.0531
- scheme_apa_positive.0541
- scheme_apa_positive.0551
- scheme_apa_positive.0561
- scheme_apa_positive.0571
- scheme_apa_positive.0581
- scheme_apa_positive.0591
- scheme_apa_positive.0601
- scheme_apa_positive.0611
- scheme_apa_positive.0621
- scheme_apa_positive.0631
- scheme_apa_positive.0641
- scheme_apa_positive.0651
- scheme_apa_positive.0661
- scheme_apa_positive.0671
- scheme_apa_positive.0681
- scheme_apa_positive.0691
- scheme_apa_positive.0701
- scheme_apa_positive.0711
- scheme_apa_positive.0721
- scheme_apa_positive.0731
- scheme_apa_positive.0741
- scheme_apa_positive.0751
- scheme_apa_positive.0761
- scheme_apa_positive.0771
- scheme_apa_positive.0781
- scheme_apa_positive.1001
- scheme_apa_positive.1011
- scheme_apa_positive.1021
- scheme_apa_positive.1031
- scheme_apa_positive.1041
- scheme_apa_positive.1051
- scheme_apa_positive.1061
- scheme_apa_positive.1071
- scheme_apa_positive.1081
- scheme_apa_positive.1091
- scheme_apa_positive.2001
- scheme_apa_positive.2011
- scheme_apa_positive.2021
- scheme_apa_positive.2031
- scheme_apa_positive.2041
- scheme_apa_positive.2051
- scheme_apa_positive.2061
- scheme_apa_positive.2071
- scheme_apa_positive.2081
- scheme_apa_positive.2091
- scheme_apa_positive.2101
- scheme_apa_positive.2111
- scheme_apa_positive.2121
- scheme_apa_positive.2131
- scheme_apa_positive.2141
- scheme_apa_positive.2151
- scheme_apa_positive.2161
- scheme_apa_positive.2171
- scheme_apa_positive.2181
- scheme_apa_positive.2191
- scheme_apa_positive.2201
- scheme_apa_positive.2211
- scheme_apa_positive.2221
- scheme_apa_positive.2231
- scheme_apa_positive.2241
- scheme_apa_positive.2251
- scheme_apa_negative.2261
- scheme_apa_positive.2271
- scheme_apa_positive.2281
- scheme_apa_positive.2291
- scheme_apa_positive.2301
- scheme_apa_positive.2311
- scheme_apa_positive.2321
- scheme_apa_positive.2331
- scheme_apa_positive.2341
- scheme_apa_positive.2351
- scheme_apa_positive.2361
- scheme_apa_positive.2371
- scheme_apa_positive.2381
- scheme_apa_positive.2391
- scheme_apa_negative.2401
- scheme_apa_positive.2411
- scheme_apa_positive.2421
- scheme_apa_positive.2431
- scheme_apa_positive.2441
- scheme_apa_positive.2451
- scheme_apa_positive.2461
- scheme_apa_positive.2471
- scheme_apa_positive.2481
- scheme_apa_positive.2491
- scheme_apa_positive.2501
- scheme_apa_positive.2511
- scheme_apa_positive.2521
- scheme_apa_positive.2531
- scheme_apa_positive.2541
- scheme_apa_positive.2561
- scheme_apa_positive.2571
- scheme_apa_positive.2581
- scheme_apa_positive.3001
- scheme_apa_positive.3011
- scheme_apa_positive.3021
- scheme_apa_positive.3031
- scheme_apa_positive.3041
- scheme_apa_positive.3051
- scheme_apa_positive.3061
- scheme_apa_positive.3071
- scheme_apa_positive.3081
- scheme_apa_positive.3091
- scheme_apa_positive.3101
- scheme_apa_positive.3111
- scheme_apa_positive.3131
- scheme_apa_negative.5001
- scheme_apa_negative.5011
- scheme_apa_negative.5021
- scheme_apa_negative.5031
- scheme_apa_negative.5041
- scheme_apa_negative.5051
- scheme_apa_negative.5061
- scheme_apa_negative.5071
- scheme_apa_negative.5081
- scheme_apa_negative.5091
- scheme_apa_negative.5101
- scheme_apa_negative.5111
- scheme_apa_negative.5121
- scheme_apa_negative.5131
- scheme_apa_negative.5141
- scheme_apa_negative.5151
- scheme_apa_negative.5161
- scheme_apa_negative.5171
- scheme_apa_negative.5181
- scheme_apa_negative.5191
- scheme_apa_negative.5201
- scheme_apa_negative.5211
- scheme_apa_negative.5221
- scheme_apa_negative.5231
- scheme_apa_negative.5241
- scheme_apa_negative.5251
- scheme_apa_negative.5261
- scheme_apa_negative.5271
- scheme_apa_negative.5281
- scheme_apa_negative.5291
- scheme_apa_negative.5301
- scheme_apa_negative.5311
- scheme_apa_negative.5321
- scheme_apa_negative.5331
- scheme_apa_negative.5341
- scheme_apa_negative.5351
- scheme_apa_negative.5361
- scheme_apa_negative.5371
- scheme_apa_negative.5381
- scheme_apa_negative.5391
- scheme_apa_negative.5401
- scheme_apa_negative.5411
- scheme_apa_negative.5421
- scheme_apa_negative.5431
- scheme_apa_negative.5441
- scheme_apa_negative.5451
- scheme_apa_negative.5461
- scheme_apa_negative.5471
- scheme_apa_negative.5481
- scheme_apa_negative.5491
- scheme_apa_negative.5501
- scheme_apa_negative.5511
- scheme_apa_negative.5521
- scheme_apa_negative.5531
- scheme_apa_negative.5541
- scheme_apa_negative.5551
- scheme_apa_negative.5561
- scheme_apa_negative.5571
- scheme_apa_negative.5581
- scheme_apa_negative.5591
- scheme_apa_negative.5601
- scheme_apa_negative.5611
- scheme_apa_negative.5621
- scheme_apa_negative.5631
- scheme_apa_negative.5641
- scheme_apa_negative.5651
- scheme_apa_negative.5661
- scheme_apa_negative.5671
- scheme_apa_negative.5681
- scheme_apa_negative.5691
- scheme_apa_negative.5701
- scheme_apa_negative.5711
- scheme_apa_negative.5721
- scheme_apa_negative.5731
- scheme_apa_negative.5741
- scheme_apa_negative.5751
- scheme_apa_negative.5761
- scheme_apa_negative.6001
- scheme_apa_negative.6011
- scheme_apa_negative.6021
- scheme_apa_negative.6031
- scheme_apa_negative.6041
- scheme_apa_negative.6051
- scheme_apa_negative.6061
- scheme_apa_negative.6071
- scheme_apa_negative.6081
- scheme_apa_negative.7001
- scheme_apa_negative.7011
- scheme_apa_negative.7021
- scheme_apa_negative.7031
- scheme_apa_negative.7041
- scheme_apa_negative.7051
- scheme_apa_negative.7061
- scheme_apa_negative.7071
- scheme_apa_negative.7081
- scheme_apa_negative.7091
- scheme_apa_negative.7101
- scheme_apa_negative.7111
- scheme_apa_negative.7121
- scheme_apa_negative.7131
- scheme_apa_negative.7141
- scheme_apa_negative.7151
- scheme_apa_negative.7161
- scheme_apa_negative.7171
- scheme_apa_negative.7181
- scheme_apa_negative.7191
- scheme_apa_negative.7201
- scheme_apa_negative.7211
- scheme_apa_negative.7221
- scheme_apa_negative.7231
- scheme_apa_negative.7241
- scheme_apa_negative.7251
- scheme_apa_negative.7261
- scheme_apa_negative.7271
- scheme_apa_negative.7281
- scheme_apa_negative.7291
- scheme_apa_negative.7301
- scheme_apa_negative.7311
- scheme_apa_negative.7321
- scheme_apa_negative.7331
- scheme_apa_negative.7341
- scheme_apa_negative.7351
- scheme_apa_negative.7361
- scheme_apa_negative.7371
- scheme_apa_negative.7381
- scheme_apa_negative.7391
- scheme_apa_negative.7401
- scheme_apa_negative.7411
- scheme_apa_negative.7421
- scheme_apa_negative.7431
- scheme_apa_negative.7441
- scheme_apa_negative.7451
- scheme_apa_negative.7461
- scheme_apa_negative.7471
- scheme_apa_negative.7481
- scheme_apa_negative.7491
- scheme_apa_negative.7501
- scheme_apa_negative.7511
- scheme_apa_negative.7521
- scheme_apa_negative.7531
- scheme_apa_negative.7541
- scheme_apa_negative.7551
- scheme_apa_negative.8001
- scheme_apa_negative.8011
- scheme_apa_negative.8021
- scheme_apa_negative.8031
- scheme_apa_negative.8041
- scheme_apa_negative.8051
- scheme_apa_negative.8061
- scheme_apa_negative.8071
- scheme_apa_negative.8081
- scheme_apa_negative.8091
- scheme_apa_negative.8101
- scheme_apa_negative.8111
- scheme_apa_negative.8121
- scheme_apa_negative.8131

### scheme_countermeasures/00_basic_countermeasures.txt（24 条目）

- debug_countermeasure
- bounties_for_whispers_t1
- bounties_for_whispers_t2
- bounties_for_whispers_t3
- bounties_for_whispers_t4
- arbitrary_arrests_t1
- arbitrary_arrests_t2
- arbitrary_arrests_t3
- arbitrary_arrests_t4
- strengthen_sentries_t1
- strengthen_sentries_t2
- strengthen_sentries_t3
- strengthen_sentries_t4
- redouble_guards_t1
- redouble_guards_t2
- redouble_guards_t3
- redouble_guards_t4
- withdraw_from_view_t1
- withdraw_from_view_t2
- withdraw_from_view_t3
- withdraw_from_view_t4
- bribe_officials_t1
- bribe_officials_t2
- bribe_officials_t3

### scheme_types/abduct_scheme.txt（1 条目）

- abduct

### scheme_types/befriend_scheme.txt（1 条目）

- befriend

### scheme_types/challenge_status_scheme.txt（1 条目）

- challenge_status

### scheme_types/claim_throne_scheme.txt（1 条目）

- claim_throne

### scheme_types/coerce_contribution_scheme.txt（1 条目）

- coerce_contribution

### scheme_types/coerce_tributary_scheme.txt（1 条目）

- coerce_tributary

### scheme_types/convert_to_witchcraft_scheme.txt（1 条目）

- convert_to_witchcraft

### scheme_types/court_scheme.txt（1 条目）

- courting

### scheme_types/damage_legitimacy_scheme.txt（1 条目）

- damage_legitimacy_scheme

### scheme_types/depose_scheme.txt（1 条目）

- depose

### scheme_types/diarch_schemes.txt（1 条目）

- overthrow_regent

### scheme_types/disbelieve_mandala_scheme.txt（1 条目）

- disbelieve_mandala

### scheme_types/elope_scheme.txt（1 条目）

- elope

### scheme_types/ep3_dispute_border_scheme.txt（1 条目）

- dispute_border

### scheme_types/ep3_found_despotate_scheme.txt（1 条目）

- found_despotate

### scheme_types/ep3_ingratiate_family_scheme.txt（1 条目）

- ingratiate_family

### scheme_types/ep3_prepare_fire_dromons_scheme.txt（1 条目）

- prepare_fire_dromons_scheme

### scheme_types/ep3_raid_estate_scheme.txt（1 条目）

- raid_estate

### scheme_types/ep3_subsume_province_scheme.txt（1 条目）

- subsume_province

### scheme_types/ep3_teach_governor_scheme.txt（1 条目）

- teach_governor

### scheme_types/expand_power_base_scheme.txt（1 条目）

- expand_power_base

### scheme_types/fabricate_hook_scheme.txt（1 条目）

- fabricate_hook

### scheme_types/find_follower_of_faith.txt（1 条目）

- find_follower_of_faith

### scheme_types/foster_legitimacy_scheme.txt（1 条目）

- foster_legitimacy_scheme

### scheme_types/generate_claim_scheme.txt（1 条目）

- generate_claim

### scheme_types/laamp_base_contract_schemes.txt（29 条目）

- laamp_base_0001_contract_scheme
- laamp_base_0011_contract_scheme
- laamp_base_0021_contract_scheme
- laamp_base_0031_contract_scheme
- laamp_base_0041_contract_scheme
- laamp_base_1001_contract_scheme
- laamp_base_1011_contract_scheme
- laamp_base_1041_contract_scheme
- laamp_base_2001_contract_scheme
- laamp_base_2011_contract_scheme
- laamp_base_2021_contract_scheme
- laamp_base_2031_contract_scheme
- laamp_base_2041_contract_scheme
- laamp_base_3001_contract_scheme
- laamp_base_3011_contract_scheme
- laamp_base_3021_contract_scheme
- laamp_base_3031_contract_scheme
- laamp_base_3041_contract_scheme
- laamp_base_4001_contract_scheme
- laamp_base_4011_contract_scheme
- laamp_base_4021_contract_scheme
- laamp_base_4031_contract_scheme
- laamp_base_4041_contract_scheme
- laamp_base_5031_contract_scheme
- laamp_base_5051_contract_scheme
- laamp_base_6001_contract_scheme
- laamp_base_6011_contract_scheme
- laamp_base_6021_contract_scheme
- laamp_base_6031_contract_scheme

### scheme_types/laamp_extra_contract_schemes.txt（6 条目）

- protect_minority_vassal_contract_diplomacy_scheme
- protect_minority_vassal_contract_martial_scheme
- protect_minority_vassal_contract_intrigue_scheme
- protect_minority_vassal_contract_learning_scheme
- laamp_prison_break_scheme
- laamp_help_find_secrets_scheme

### scheme_types/learn_language_scheme.txt（1 条目）

- learn_language

### scheme_types/leverage_contribution_scheme.txt（1 条目）

- leverage_contribution

### scheme_types/murder_scheme.txt（1 条目）

- murder

### scheme_types/pam_study_scheme.txt（1 条目）

- study_scripture

### scheme_types/promote_scheme.txt（1 条目）

- promote

### scheme_types/seduce_scheme.txt（1 条目）

- seduce

### scheme_types/seize_realm_scheme.txt（1 条目）

- seize_realm

### scheme_types/slander_scheme.txt（1 条目）

- slander

### scheme_types/steal_back_artifact_scheme.txt（1 条目）

- steal_back_artifact

### scheme_types/steal_herd_scheme.txt（1 条目）

- steal_herd

### scheme_types/study_faith_scheme.txt（1 条目）

- study_faith

### scheme_types/sway_scheme.txt（1 条目）

- sway

### scheme_types/tgp_coup_ceremonial_liege.txt（1 条目）

- coup_ceremonial_liege

### scheme_types/tgp_dynastic_cycle_schemes.txt（4 条目）

- celestial_siphon_treasury
- celestial_movement_power_promote
- celestial_movement_power_slander
- celestial_minister_find_secrets_scheme

### scheme_types/tgp_mentoring_scheme.txt（1 条目）

- mentoring

### scheme_types/tgp_study_scheme.txt（1 条目）

- study_confucian_classics

### 未解析文件

- `agent_types/_agent_types.info` — 纯文档（非 Jomini）
- `pulse_actions/_pulse_actions.info` — 纯文档（非 Jomini）
- `scheme_countermeasures/_scheme_countermeasures.info` — 纯文档（非 Jomini）
- `scheme_types/_schemes.info` — 纯文档（非 Jomini）
