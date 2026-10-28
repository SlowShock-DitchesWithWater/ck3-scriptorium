<!-- 来源: https://ck3.paradoxwikis.com/Lifestyles_modding oldid=35087 抓取于 2026-10-22T21:41:26+08:00 -->

# Lifestyles modding

## Lifestyles

Lifestyles represent the trees a character can progress in.

### Scripting

Lifestyles are defined in `common/lifestyles/`. Below is a list of all attributes usable when defining a lifestyle.

**Lifestyle attributes**

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| is_highlighted | trigger | If the trigger is valid, highlight the lifestyle. See triggers below. | is_highlighted = { has_trait = education_learning } |
| is_valid_showing_failures_only | trigger | Checks if the lifestyle can be selected. See triggers below. |  |
| is_valid | trigger | Checks if the lifestyle can be selected. See triggers below. | is_valid = { has_dlc_feature = wandering_nobles } |
| xp_per_level | number | How much XP do you need per perk point? | xp_per_level = 1000 |
| base_xp_gain | number | How much XP do you get each month? Before modifiers | base_xp_gain = 25 |
| icon | string | What key to use for the icon; if not defined, will use the key of the lifestyle. See graphics below. |  |

Here is a complete example:

```
learning_lifestyle = {

	is_highlighted = {
		has_trait = education_learning		
	}
	
	
	xp_per_level = 1000
	base_xp_gain = 25
}
```

#### Triggers

The triggers are in the character scope.

Any triggers that are part of the lifestyle script files cannot use:

- scripted triggers, effects, or modifiers
- triggers, effects, or modifiers that are generated based on scripted content, such as:
  - diplomacy_lifestyle_perk_points trigger (based on a scripted lifestyle)
  - has_relation_rival trigger (based on a scripted relation)

### Graphics

Lifestyle icons are put in `gfx/interface/icons/lifestyles/` in the `.dds` format, with the name `<LIFESTYLE KEY>.dds` by default (ex. `diplomacy_lifestyle.dds`), or with the key of the `icon` attribute.

- Lifestyle icon example (`education_learning.dds`)

### Localization

Vanilla localization files are located at `localization/<language>/focuses_l_<language>.yml`.

**Localization keys**

| Localization key | Description | Example |
| --- | --- | --- |
| <LIFESTYLE>_name | Name of the lifestyle. | `learning_lifestyle_name:0 "Learning"` |
| <LIFESTYLE>_desc | Description of the lifestyle. | `learning_lifestyle_desc:0 "Focus on learning all that you can. The realm of knowledge and divinity lie within your grasp, as well as the secrets to life itself."` |
| <LIFESTYLE>_highlight_desc | Description of the lifestyle when highlighted (using the trigger `is_highlighted` above) | `learning_lifestyle_highlight_desc:0 "Because of your Learning [education\|E], you gain #P [GetPlayer.Custom('GetEducationLifestylePercentageBoost')]#! more [experience\|E] in this Lifestyle."` |

## Lifestyle focuses

Lifestyle focuses are the focuses on specific lifestyle characters can choose.

### Scripting

Lifestyle focuses are defined in `common/focuses/`. Below is a list of all attributes usable when defining a lifestyle focus.

**Lifestyle focuses attributes**

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| type | <education\|lifestyle> | What type of focus is this? Education focuses are for childrens. | type = lifestyle |
| is_shown | trigger | Is the focus visible to the scoped character? Scope / Type / Description；root / Character / Character being evaluated for focus type. | is_shown = { NOT = { government_has_flag = government_is_landless_adventurer } } |
| is_valid | trigger | Can the scoped character choose this focus? Scope / Type / Description；root / Character / Character being evaluated for focus type. | is_valid = { NOT = { government_has_flag = government_is_landless_adventurer } } |
| is_valid_showing_failures_only | trigger | Can the scoped character choose this focus? These will be shown only if they fail. Scope / Type / Description；root / Character / Character being evaluated for focus type. |  |
| is_good_for | trigger | Is this a good education focus for the scoped child? This is used by education focuses. Scope / Type / Description；root / Character / Character being evaluated for focus type. | is_good_for = { has_diplomacy_education_affinity_childhood_trait_trigger = yes } |
| is_bad_for | trigger | Is this a bad education focus for the scoped child? This is used by education focuses. Scope / Type / Description；root / Character / Character being evaluated for focus type. | is_bad_for = { has_martial_education_disaffinity_childhood_trait_trigger = yes } |
| is_default | trigger | Is this the default education focus for the scoped child? This is used by education focuses. Scope / Type / Description；root / Character / Character being evaluated for focus type. | is_default = { has_trait = bossy } |
| on_change_to | effect | Effect to execute on the character changing to this type. Scope / Type / Description；root / Character / Character changing to this focus type. | on_change_to = { if = { limit = { exists = var:education_point_gain_variable } ... remove_variable = education_point_gain_variable } } |
| on_change_from | effect | Effect to execute on the character changing away from this type. Scope / Type / Description；root / Character / Character changing away from this focus type. | on_change_from = { if = { limit = { is_alive = yes is_adult = no } add_character_flag = learning_previous_education ... } } |
| on_birthday | effect | Effect to execute on the character's birthday if they are above NCharacter::FOCUS_CHILD_MIN_AGE. Scope / Type / Description；root / Character / Character that has birthday. |  |
| modifier | modifiers | Modifiers to apply to the character that has this focus | modifier = { learning = 3 development_growth_factor = 0.15 } |
| skill | enum | Which skill is this focus related to? This is used by education focuses. | skill = learning |
| lifestyle | Lifestyle | What lifestyle the focus belongs to. Adding this will make it a lifestyle focus. If the type is lifestyle this is required. Key is mapped to the lifestyle database: `common/lifestyles/` | lifestyle = learning_lifestyle |
| icon | string | Override for what key to use for the icon. Defaults to the key of the focus. |  |
| auto_selection_weight | scripted value | Script value for selection weight. Primarily used by the AI, but also when a character is promoted to having focus for any reason to select initial focus. Scope / Type / Description；root / Character / Character being evaluated for focus type. | auto_selection_weight = { value = 11 if = { limit = { has_education_learning_trigger = yes } add = 1989 } } |
| desc | dynamic description | Descriptions used to describe the focus in the interface. | desc = { desc = learning_scholarship_focus_desc desc = line_break } |

Here is a complete example:

```
learning_scholarship_focus = {
	lifestyle = learning_lifestyle
	
	is_shown = {
		NOT = { government_has_flag = government_is_landless_adventurer }
	}
	is_valid = {
		NOT = { government_has_flag = government_is_landless_adventurer }
	}

	desc = {
		desc = learning_scholarship_focus_desc
		desc = line_break
	}
	
	modifier = {
		learning = 3
		development_growth_factor = 0.15
	}

	auto_selection_weight = {
		value = 11
		if = {
			limit = {
				has_education_learning_trigger = yes
			}
			add = 1989
		}
		if = {
			limit = {
				government_has_flag = government_is_landless_adventurer
			}
			multiply = 0
		}
	}
}
```

### Graphics

Lifestyle focuses icons are put in `gfx/interface/icons/focuses/` in the `.dds` format, with the name `<LIFESTYLE FOCUS KEY>.dds` by default (ex. `education_learning.dds`), or with the key of the `icon` attribute.

Lifestyle tree background are put in `gfx/interface/icons/lifestyle_tree_backgrounds/` in the `.dds` format.

- Lifestyle focus icon example (`education_learning.dds`)

### Localization

Vanilla localization files are located at `localization/<language>/lifestyles/perks_l_<language>.yml`.

**Localization keys**

| Localization key | Description | Example |
| --- | --- | --- |
| <LIFESTYLE FOCUS KEY> | Focus name | `learning_scholarship_focus:0 "Scholarship Focus"` |
| <LIFESTYLE FOCUS KEY>_modifier | Focus modifier name | `learning_scholarship_focus_modifier:1 "[GetFocus('learning_scholarship_focus').GetName]"` |
| <LIFESTYLE FOCUS KEY>_desc | Focus description | `learning_scholarship_focus_desc:0 "The knowledge of those who have come before, the knowledge of those still living, and the knowledge of perpetual truths."` |
| <LIFESTYLE FOCUS KEY>_effect_desc | Focus effect description | `learning_scholarship_focus_effect_desc:0 "Focusing on Scholarship grants:"` |

## Lifestyle perks

Lifestyle perks are the components of lifestyles which can be unlocked.

### Scripting

Lifestyles perks are defined in `common/lifestyle_perks/`. Below is a list of all attributes usable when defining a lifestyle perk.

**Lifestyle perks attributes**

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| name | dynamic description | Dynamic description. If not set, generated loc key will be used. Character scope | name = { first_valid = { triggered_desc = { trigger = { is_landless_adventurer = yes } desc = apostate_perk_adventurer_name } desc = apostate_perk_name } } |
| tree | string (Lifestyle focus) | Which tree does it belong to? Only used for GUI layout | tree = scholarship |
| position | numbers | What is its positioning within the tree? Only used for GUI layout. Multiplied with PERK_X_OFFSET and PERK_Y_OFFSET | position = { 0 2 } |
| icon | string | What key to use for the icon; if not defined, will use the key of the perk. See graphics below. | icon = node_learning |
| lifestyle | string (Lifestyle) | Which lifestyle the perk belongs to | lifestyle = learning_lifestyle |
| parent | string (Lifestyle perk) | Parent perk. Needed to unlock this perk. Multiple parents can be defined | parent = apostate_perk parent = scholarly_circles_perk |
| can_be_picked | trigger | Trigger in character scope. | can_be_picked = { always = yes } |
| can_be_auto_selected | trigger | Trigger in character scope. Used in addition to can_be_picked and the parent perks to determine if a character can get a given perk on auto-selection (campaign start, and when becoming landed) |  |
| trait | string (Trait) | If effect unlocks a trait, use this to set trait used in the hover tooltip | trait = scholar |
| effect | effect | Run on unlock. Character scope | effect = { add_trait_force_tooltip = scholar } |
| character_modifier | effect | Applied to characters with the perk | character_modifier = { different_faith_opinion = 15 faith_conversion_piety_cost_mult = -0.75 } |
| doctrine_character_modifier | effect | Additional modifier applied to characters with the perk and their faith having the specified doctrine Multiple doctrine character modifiers can be applied. Attribute / Type / Description；doctrine / religious doctrine / Will trigger the effects if the character's religion have this doctrine. | doctrine_character_modifier = { doctrine = doctrine_theocracy_temporal clergy_opinion = 10 } |
| culture_character_modifier | effect | Additional modifier applied to characters with the perk and their culture having the specified parameter Multiple culture character modifier can be applied. Attribute / Type / Description；parameter / culture parameter / Will trigger the effects if the character's culture has this parameter applied. | culture_character_modifier = { parameter = automatic_befriend_access befriend_scheme_phase_duration_add = medium_scheme_phase_duration_bonus_value } |
| government_character_modifier | effect | Additional modifier applied to characters with the perk and their government type having the specified flag Multiple government character modifier can be applied. Attribute / Type / Description；flag / government flag / Will trigger the effects if the character's government has this flag.；invert_check / <yes/no> / If set to 'yes' then we will instead apply these modifiers if the government does NOT have the specified flag | government_character_modifier = { flag = government_is_landless_adventurer enemy_terrain_advantage = -0.5 knight_effectiveness_per_learning = 0.005 learning_per_piety_level = -1 } |
| auto_selection_weight | number | Script value for weight for auto-selection. Defaults to 1000 | auto_selection_weight = { value = 11 if = { limit = { has_education_learning_trigger = yes } add = 1989 } } |

Here is a complete example:

```
scholarly_circles_perk = {
	lifestyle = learning_lifestyle
	tree = scholarship
	position = { 2 2 }
	icon = node_learning
	
	parent = planned_cultivation_perk
	
	name = {
		first_valid = {
			triggered_desc = {
				trigger = { is_landless_adventurer = yes }
				desc = scholarly_circles_perk_adventurer_name
			}
			desc = scholarly_circles_perk_name
		}
	}
	
	character_modifier = {
		learning_per_piety_level = 1
	}
	government_character_modifier = {
		flag = government_is_landless_adventurer
		enemy_terrain_advantage = -0.5
		knight_effectiveness_per_learning = 0.005
		learning_per_piety_level = -1
	}
}
```

### Graphics

Lifestyle perks icons are put in `gfx/interface/icons/lifestyles_perks/` in the `.dds` format, with the name `<LIFESTYLE PERK KEY>.dds` by default (ex. `scientific_perk.dds`), or with the key of the `icon` attribute.

In vanilla, perks use a common node icon up to the final perk of a lifestyle tree, where the icon is the trait given by that perk.

- Lifestyle perk icon example (`trait_scholar.dds`)
- Lifestyle node icon example (`node_diplomacy.dds`)

### Localization

Vanilla localization files are located at `localization/<language>/lifestyles/perks_l_<language>.yml`.

**Localization keys**

| Localization key | Description | Example |
| --- | --- | --- |
| <LIFESTYLE PARK>_name | Name of the lifestyle perk. | `learn_on_the_job_perk_name:0 "Learn on the Job"` |

## Vanilla list

**Vanilla keys**

| Lifestyle keys | Lifestyle focus keys | Lifestyle perk trees keys keys | Lifestyle perks keys |
| --- | --- | --- | --- |
| diplomacy_lifestyle | diplomacy_foreign_affairs_focus | foreign_affairs | thoughtful_perk ducal_conquest_perk forced_vassalage_perk adaptive_traditions_perk flexible_truces_perk defensive_negotiations_perk embassies_perk accomplished_forger_perk diplomat_perk |
| diplomacy_lifestyle | diplomacy_majesty_focus | majesty | benevolent_intent_perk inspiring_rule_perk firm_hand_perk praetorian_guard_perk true_ruler_perk writing_history_perk a_life_of_glory_perk dignitas_perk august_perk |
| diplomacy_lifestyle | diplomacy_family_focus | family | befriend_perk confidants_perk flatterer_perk friendly_counsel_perk familial_familiar_perk groomed_to_rule_perk thicker_than_water_perk sound_foundations_perk family_man_perk |
| diplomacy_lifestyle | diplomacy_adventurer_focus |  |  |
| diplomacy_lifestyle | education_diplomacy |  |  |
| martial_lifestyle | martial_strategy_focus | strategy | bellum_justum_perk parthian_tactics_perk envelopment_perk organized_retreat_perk hit_and_run_perk engineered_for_destruction_perk living_off_the_land_perk sappers_perk strategist_perk |
| martial_lifestyle | martial_authority_focus | authority | serve_the_crown_perk a_mans_home_perk enduring_hardships_perk prepared_conscription_perk strict_organization_perk hard_rule_perk soldiers_of_lesser_fortune_perk absolute_control_perk overseer_perk |
| martial_lifestyle | martial_chivalry_focus | chivalry | stalwart_leader_perk courtship_perk promising_prospects_perk loyalty_and_respect_perk chivalric_dominance_perk never_back_down_perk kingsguard_perk peacemaker_perk gallant_perk |
| martial_lifestyle | martial_adventurer_focus |  |  |
| martial_lifestyle | education_martial |  |  |
| stewardship_lifestyle | stewardship_wealth_focus | wealth | golden_obligations_perk heregeld_perk detailed_ledgers_perk war_profiteer_perk fearful_troops_perk it_is_my_domain_perk golden_aplomb_perk at_any_cost_perk avaricious_perk |
| stewardship_lifestyle | stewardship_domain_focus | domain | tax_man_perk defensive_measures_perk organized_muster_rolls_perk cutting_corners_perk professional_workforce_perk centralization_perk popular_figurehead_perk divided_attention_perk architect_perk |
| stewardship_lifestyle | stewardship_duty_focus | duty | meritocracy_perk chains_of_loyalty_perk likable_perk positions_of_power_perk large_levies_perk soon_forgiven_perk toe_the_line_perk honored_to_serve_perk administrator_perk |
| stewardship_lifestyle | stewardship_adventurer_focus |  |  |
| stewardship_lifestyle | education_stewardship |  |  |
| intrigue_lifestyle | intrigue_skulduggery_focus | skulduggery | truth_is_relative_perk digging_for_dirt_perk kidnapper_perk court_of_shadows_perk prepared_for_anything_perk swift_execution_perk a_job_done_right_perk twice_schemed_perk schemer_perk |
| intrigue_lifestyle | intrigue_temptation_focus | temptation | like_weed_in_a_garden_perk unshackled_lust_perk subtle_desire_perk mortal_adoration_perk enticing_opportunity_perk home_advantage_perk graceful_recovery_perk smooth_operator_perk seducer_perk |
| intrigue_lifestyle | intrigue_intimidation_focus | intimidation | dark_insights_perk divine_retribution_perk dreadful_perk thriving_in_chaos_perk malice_implicit_perk fear_tax_perk forever_infamous_perk prison_feudal_complex_perk torturer_perk |
| intrigue_lifestyle | intrigue_adventurer_focus |  |  |
| intrigue_lifestyle | education_intrigue |  |  |
| learning_lifestyle | learning_medicine_focus | medicine | anatomical_studies_perk carefree_perk mental_resilience_perk restraint_perk know_thyself_perk wash_your_hands_perk iron_constitution_perk healthy_perk whole_of_body_perk |
| learning_lifestyle | learning_scholarship_focus | scholarship | pedagogy_perk open_minded_perk apostate_perk scientific_perk planned_cultivation_perk scholarly_circles_perk learn_on_the_job_perk sanctioned_loopholes_perk scholar_perk |
| learning_lifestyle | learning_theology_focus | theology | faithful_perk zealous_proselytizer_perk religious_icon_perk prophet_perk clerical_justifications_perk church_and_state_perk radiant_perk defender_of_the_faith_perk theologian_perk |
| learning_lifestyle | learning_adventurer_focus |  |  |
| learning_lifestyle | education_learning |  |  |
| wanderer_lifestyle | wanderer_internal_affairs_focus | surveyor | mustering_the_troops_perk local_inspection_perk know_your_land_know_your_people_perk no_stone_unturned_perk travel_logs_perk local_arbitration_perk realm_charts_perk personal_touch_perk surveyor_perk |
| wanderer_lifestyle | wanderer_journey_focus | wayfarer | well_prepared_perk roaming_perk far_and_wide_perk just_one_more_hill_perk of_the_people_perk local_hero_perk travel_companion_perk the_home_away_from_home_perk wayfarer_perk |
| wanderer_lifestyle | wanderer_destination_focus | voyager | power_at_home_perk mercenary_contacts_perk journey_perk been_there_done_that_perk finally_there_perk souvenirs_aplenty_perk gracious_host_impeccable_guest_perk journey_planner_perk voyager_perk |
