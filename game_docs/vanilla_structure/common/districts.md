# common/districts 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与指纹见 manifest.json）
- 文件数：12（其中 Jomini 解析 11 个）
- 顶层块条目总数：352，跨文件唯一条目 352
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `_districts.info` | 6637 | - | - | 纯文档（非 Jomini） |
| `duchy_capital_districts.txt` | 7708 | 9 | 0 | jomini |
| `entrepot_districts.txt` | 589 | 1 | 0 | jomini |
| `great_districts.txt` | 2805 | 7 | 0 | jomini |
| `holding_districts.txt` | 7033 | 7 | 0 | jomini |
| `legendary_districts.txt` | 3028 | 5 | 0 | jomini |
| `other_special_districts.txt` | 4214 | 20 | 0 | jomini |
| `regular_districts.txt` | 33738 | 19 | 0 | jomini |
| `resource_districts.txt` | 47553 | 29 | 0 | jomini |
| `special_districts.txt` | 43787 | 199 | 0 | jomini |
| `special_mines_districts.txt` | 11077 | 55 | 0 | jomini |
| `trade_post_districts.txt` | 1106 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### duchy_capital_districts.txt（9 条目）

- governance_district
- assay_district
- bailiwick_district
- theodosian_walls_01_district
- aurelian_walls_01_district
- staple_district
- endowment_district
- military_duchy_capital_district
- ducal_residence_district

### entrepot_districts.txt（1 条目）

- entrepot_location_district

### great_districts.txt（7 条目）

- mandala_capital_01_district
- the_great_wall_01_district
- the_great_wall_04_district
- the_great_wall_shanhai_pass_district
- the_great_wall_liaodong_district
- great_project_cathedral_01_district
- republic_great_plaza_district

### holding_districts.txt（7 条目）

- castle_holding_district
- tribal_holding_district
- city_holding_district
- temple_holding_district
- nomad_holding_district
- herder_holding_district
- temple_citadel_holding_district

### legendary_districts.txt（5 条目）

- legendary_shrine_district
- legendary_palace_district
- legendary_statue_district
- legendary_watchtower_district
- legendary_hunting_lodge_district

### other_special_districts.txt（20 条目）

- drassanes_01_district
- kyz_kala_01_district
- cluny_abbey_01_district
- york_walls_01_district
- damascus_mosque_01_district
- jokhang_01_district
- wartburg_01_district
- beta_giyorgis_01_district
- holy_wisdom_01_district
- kano_walls_01_district
- somapura_university_01_district
- duomo_florence_01_district
- konark_temple_01_district
- al_qarawiyyin_university_01_district
- kairouan_basins_01_district
- ghana_palace_01_district
- visegrad_castle_01_district
- wawel_cathedral_01_district
- vatapi_caves_01_district
- jaisalmer_fort_01_district

### regular_districts.txt（19 条目）

- guild_district
- market_district
- port_district
- border_forts_district
- walls_district
- military_district
- bureaucratic_district
- household_district
- temple_district
- religious_community_district
- mandala_district
- patrician_district
- entertainment_district
- urban_housing_district
- manor_houses_district
- villages_district
- tribal_economy_prestige_district
- tribal_military_district
- tribal_wanua_district

### resource_districts.txt（29 条目）

- forestry_district
- grain_district
- wool_district
- cattle_district
- cotton_district
- stone_district
- fish_district
- wine_district
- oil_district
- rice_district
- millet_district
- mine_district
- salt_district
- amber_district
- silk_district
- furs_district
- spices_district
- tea_district
- dyes_district
- ivory_district
- sugar_district
- incense_district
- medicaments_district
- ceramics_district
- hemp_district
- flax_district
- honey_district
- fruit_district
- horses_district

### special_districts.txt（199 条目）

- holy_site_cathedral_01_district
- holy_site_mosque_01_district
- holy_site_fire_temple_01_district
- holy_site_pagan_grand_temple_01_district
- holy_site_indian_grand_temple_01_district
- holy_site_buddhist_grand_temple_01_district
- holy_site_japanese_temple_01_district
- holy_site_chinese_temple_01_district
- holy_site_se_asia_pagan_temple_01_district
- holy_site_other_grand_temple_01_district
- holy_site_mahabodhi_temple_01_district
- holy_site_imam_ali_mosque_01_district
- holy_site_great_mosque_of_mecca_01_district
- holy_site_great_mosque_of_cordoba_01_district
- holy_site_great_mosque_of_djenne_01_district
- holy_site_great_mosque_of_samarra_01_district
- holy_site_cologne_cathedral_01_district
- holy_site_canterbury_cathedral_01_district
- holy_site_prophetic_mosque_01_district
- doges_palace_01_district
- walls_of_genoa_01_district
- visby_ringmur_01_district
- walls_of_benin_01_district
- the_colosseum_01_district
- iron_pillar_of_delhi_01_district
- iron_pillar_of_dhar_01_district
- the_pyramids_01_district
- stonehenge_01_district
- offas_dyke_01_district
- hadrians_wall_01_district
- petra_01_district
- buddhas_of_bamian_01_district
- alhambra_01_district
- citadel_of_aleppo_01_district
- house_of_wisdom_01_district
- the_tower_of_london_01_district
- london_bridge_01_district
- notre_dame_01_district
- brihadeeswarar_temple_01_district
- shwedagon_pagoda_01_district
- ananda_temple_01_district
- the_friday_mosque_01_district
- khajuraho_01_district
- palace_of_aachen_01_district
- hagia_sophia_01_district
- dome_of_the_rock_01_district
- hall_of_heroes_01_district
- generic_university_district
- al_azhar_university_district
- sankore_university_district
- siena_university_district
- nalanda_university_district
- special_sicilian_parliament_01_district
- special_greenhouse_01_district
- hotin_fort_01_district
- golden_gate_of_kiev_01_district
- heddal_stave_church_01_district
- temple_of_uppsala_01_district
- lund_cathedral_01_district
- danevirke_01_district
- roman_wall_of_lugo_01_district
- rock_of_gibraltar_01_district
- aljaferia_palace_01_district
- tower_of_hercules_01_district
- city_wall_of_toledo_01_district
- alcazar_of_segovia_01_district
- holy_site_basilica_santiago_01_district
- imam_reza_shrine_01_district
- soltaniyeh_01_district
- palace_of_ctesiphon_01_district
- falak_ol_aflak_citadel_01_district
- minarets_and_remains_of_jam_01_district
- great_wall_of_gorgan_01_district
- maharloo_lake_01_district
- rainbow_mountains_01_district
- mount_damavand_01_district
- tomb_of_cyrus_01_district
- ark_of_bukhara_01_district
- shah_i_zinda_01_district
- alamut_castle_01_district
- assassin_castle_01_district
- event_tower_of_silence_01_district
- church_of_the_theotokos_district
- hagios_demetrios_district
- kassiopi_castle_district
- saint_lazarus_district
- sumela_monastery_01_district
- patras_castle_district
- maiden_tower_district
- despot_palace_district
- meteora_01_district
- mount_athos_01_district
- apollinare_nuovo_district
- saint_catherine_district
- jvari_monastery_district
- etchmiadzin_cathedral_district
- cattolica_stilo_district
- hosios_loukas_district
- sofia_ohrid_district
- fairy_chimneys_district
- cilician_gates_district
- pleasure_dome_district
- burkhan_khaldun_01_district
- swahili_port_pemba_district
- swahili_port_zanzibar_district
- swahili_port_mombasa_district
- swahili_port_pate_district
- swahili_port_lamu_district
- wulingyuan_01_district
- leshan_giant_buddha_01_district
- yungang_grottoes_01_district
- wudang_mountain_temples_01_district
- shaolin_monastery_01_district
- lingyin_temple_01_district
- giant_wild_goose_pagoda_01_district
- kaifeng_palace_01_district
- forbidden_city_01_district
- qianling_mausoleum_01_district
- quanzhou_seaport_01_district
- angkor_wat_01_district
- citadel_thang_long_01_district
- po_klong_garai_01_district
- krakatoa_01_district
- borobudur_01_district
- hoshi_ryokan_01_district
- herat_bazaar_01_district
- tabriz_bazaar_01_district
- lhasa_market_01_district
- gurganj_bazaar_01_district
- changan_market_01_district
- lahur_bazaar_01_district
- hamadan_bazaar_01_district
- dunhuang_market_01_district
- sunday_bazaar_01_district
- mount_fuji_01_district
- itsukushima_jinja_01_district
- heian_palace_01_district
- ise_jingu_01_district
- kofuku_ji_01_district
- enryaku_ji_01_district
- dazaifu_01_district
- chinjufu_01_district
- hakata_port_01_district
- hwangnyongsa_01_district
- byeokran_port_01_district
- mount_baekdu_01_district
- dau_temple_01_district
- liuhe_pagoda_01_district
- muaro_jambi_01_district
- hanging_temple_01_district
- pagoda_of_fogong_temple_01_district
- plain_of_jars_01_district
- dieng_plateau_01_district
- mount_apo_01_district
- besakih_temple_01_district
- gongsanseong_fortress_01_district
- white_deer_grotto_academy_01_district
- shigu_academy_01_district
- culai_academy_01_district
- lize_academy_01_district
- maoshan_academy_01_district
- tiantai_monasteries_01_district
- jizu_shan_temples_01_district
- nanhua_temple_01_district
- mozu_tombs_district
- holy_site_st_peters_basilica_01_district
- boudhanath_01_district
- qutb_minar_01_district
- sanchi_stupa_01_district
- yazd_mosque_01_district
- mont_st_michel_01_district
- goguryeo_tomb_01_district
- buddha_kamakura_01_district
- pyramid_lingapura_01_district
- maijishan_grottoes_01_district
- three_pagodas_dali_01_district
- iron_lion_cangzhou_01_district
- dengfeng_observatory_01_district
- muara_takus_01_district
- stone_pagoda_01_district
- thuriang_kilns_01_district
- yuelu_academy_01_district
- chocolate_hills_01_district
- fanfang_guangzhou_01_district
- wilwatikta_palace_01_district
- ha_long_bay_01_district
- my_son_sanctuary_01_district
- gunung_api_01_district
- suwalesi_megaliths_01_district
- izumo_taisha_01_district
- confucius_temple_01_district
- citadel_linan_01_district
- temples_angkor_01_district
- tower_of_pisa_district
- tower_of_pisa_leaning_district
- pam_abbey_of_st_gall_01_district
- pam_palais_de_papes_01_district
- pam_lateran_basilica_01_district
- pam_reims_cathedral_01_district

### special_mines_districts.txt（55 条目）

- generic_copper_mines_01_district
- generic_silver_mines_01_district
- generic_gold_mines_01_district
- rammelsberg_mines_01_district
- kutna_hora_mines_01_district
- baofeng_mines_01_district
- kremnica_mines_01_district
- zijinshan_mines_01_district
- jiaodong_mines_01_district
- falun_mines_01_district
- schwaz_mines_01_district
- liangzhe_mines_01_district
- argentiera_mines_01_district
- kollur_mines_01_district
- siderokausia_mines_01_district
- mali_mines_01_district
- konasamudram_mines_01_district
- dean_mines_01_district
- phnom_dek_mines_01_district
- hanxing_mines_01_district
- chihu_mines_01_district
- zawar_mines_01_district
- takkeda_mines_01_district
- khetri_mines_01_district
- taghaza_mines_01_district
- ijil_mines_01_district
- turda_mines_01_district
- wieliczka_mines_01_district
- zigong_mines_01_district
- phocaea_mines_01_district
- pansjhir_mines_01_district
- trepca_mines_01_district
- rudnik_mines_01_district
- cevennes_mines_01_district
- guiyang_mines_01_district
- kaibao_mines_01_district
- hetian_mines_01_district
- dushan_mines_01_district
- xiuyan_mines_01_district
- itoigawa_mines_01_district
- lantian_mines_01_district
- fengtian_mines_01_district
- hpakant_mines_01_district
- allaq_mines_01_district
- verespatak_mines_01_district
- suvarnadvipa_mines_01_district
- nishapur_mines_01_district
- srebrenica_mines_01_district
- ratnapura_mines_01_district
- sar_i_sang_mines_01_district
- mogok_mines_01_district
- koganeyama_mines_01_district
- tsushima_mines_01_district
- sado_mines_01_district
- tada_mines_01_district

### trade_post_districts.txt（1 条目）

- trade_post_location_district

### 未解析文件

- `_districts.info` — 纯文档（非 Jomini）
