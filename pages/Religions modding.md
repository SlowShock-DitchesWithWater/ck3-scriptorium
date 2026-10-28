<!-- 来源: https://ck3.paradoxwikis.com/Religions_modding oldid=37089 抓取于 2026-10-22T21:41:55+08:00 -->

# Religions modding

> [!] This article has been verified for the current PC version (1.20) of the game.

New religions can easily be added into the game using the highly modular design which the game offers.

## Religion family

Each religion belongs to a family. The four vanilla families are Abrahamic, Eastern (Dharmic), Sinitic (Taoism), and Pagan. For instance:

- Christianity and Islam are part of the Abrahamic Family
- Slavism and Tengrism are part of the Pagan Family

Religion families are located in */common/religion/religion_family_types*. The religion family is defined as a tag with an alphanumerical ID. For example, the Sinitic family is defined as follows:

```
rf_sinitic = {
	piety_icon_group = "taoism"
	graphical_faith = "dharmic_gfx"
	hostility_doctrine = sinitic_hostility_doctrine
	tenet_background_icon = tenet_banner_known_core
	tenet_heretical_background_icon = tenet_banner_unknown_heretical
	tenet_neutral_background_icon = tenet_banner_known_neutral
	tenet_unknown_background_icon = tenet_banner_unknown_neutral
}
```

Below is a list of all parameters that can be set for religion families.

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| name | localization key | If not set will use the object key as localization key | name = name_of_the_family |
| piety_icon_group | gfx | All religions in this family default to this set of piety icons. Order of precedence is the lowest level scripted in: faith > religion > family. | piety_icon_group = christian |
| graphical_faith | gfx | All religions in this family default to this 3D model (currently used for temple assets). Order of precedence is the lowest level scripted in: faith > religion > family. | graphical_faith = catholic_gfx |
| hostility_doctrine | doctrine | INTERFACE ONLY: Use this doctrine when displaying hostility information for the whole religious family (if not scripted, then show no information) | hostility_doctrine = christian_hostility_doctrine |
| tenet_background_icon tenet_heretical_background_icon tenet_neutral_background_icon tenet_unknown_background_icon | gfx | This is the banner shown behind picked tenets. The small version adds a "_small" suffix to this icon, make sure both textures exists. Order of precedence is the lowest level scripted in: faith > religion > family. | tenet_background_icon = tenet_banner_known_core tenet_heretical_background_icon = tenet_banner_unknown_heretical tenet_neutral_background_icon = tenet_banner_known_neutral tenet_unknown_background_icon = tenet_banner_unknown_neutral |

## Religion structure

Religions are located in the */common/religion/religion_types* folder. Each religion is defined within a file. The religion is defined as a tag with an alphanumerical ID. Here is an example of a fictional religion (localization is addressed below):

```
sea_cults = {
	religion_details = {
		family = rf_pagan
		piety_icon_group = "zoroastrian"
		theocracy_government_type = ecclesiastical_government
		theocracy_lease_contract_type = ecclesiastical_lease
	}
	
	doctrine = pagan_hostility_doctrine
	
	pagan_roots = yes
	
	#Main Group
	doctrine = doctrine_spiritual_head
	doctrine = doctrine_gender_male_dominated
	doctrine = doctrine_pluralism_fundamentalist
	doctrine = doctrine_theocracy_lay_clergy
	doctrine = doctrine_pilgrimage_encouraged
	doctrine = doctrine_funeral_bewailment

	#Marriage
	doctrine = doctrine_concubines
	doctrine = doctrine_divorce_allowed
	doctrine = doctrine_bastardry_legitimization
	doctrine = doctrine_consanguinity_cousins

	#Crimes
	doctrine = doctrine_homosexuality_shunned
	doctrine = doctrine_adultery_men_shunned
	doctrine = doctrine_adultery_women_accepted
	doctrine = doctrine_kinslaying_accepted
	doctrine = doctrine_deviancy_accepted
	doctrine = doctrine_witchcraft_crime

	#Clerical Functions
	doctrine = doctrine_clerical_function_taxation
	doctrine = doctrine_clerical_gender_either
	doctrine = doctrine_clerical_marriage_allowed
	doctrine = doctrine_clerical_succession_spiritual_appointment

    traits = {
		virtues = {
			brave = { weight = 50 scale = 1.5 }
			lunatic_1 = { weight = 25 scale = 1 }
			wrathful = { weight = 10 scale = 1 }
		}
		sins = {
			patient = { weight = 20 scale = 1 }
			content = { weight = 30 scale = 1 }
			shy = { weight = 10 scale = 1 }
		}
	}

	reserved_male_names = {
		Lobbo Lobbeu Lobst Lob Lobr Loabstr Lobb Lub Leurbo
	}
	reserved_female_names = {
		Lobba Lobbelia Lobsta Loba Lober Loabstra Lobba Lubas Leurbos
	}
	holy_order_names = {
		{ name = "holy_order_claw_bearers" }
		{ name = "holy_order_clackers" }
		{ name = "holy_order_servants_of_the_lobbo" }
		{ name = "holy_order_the_pile" }
	}
	holy_order_maa = { huscarl }
	custom_faith_icons = { custom_faith_1 custom_faith_2 custom_faith_3 custom_faith_4 custom_faith_5 custom_faith_6 custom_faith_7 custom_faith_8 custom_faith_9 custom_faith_10 lobbist lobbist_reformed }

	localization = {
		...
	}

}
```

Below is a list of all parameters that can be set for religions.

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| family | religion family | What religion family the religion belongs to | family = family_name |
| graphical_faith | gfx | All faiths in this religion default to this 3D model (currently used for temple assets). Order of precedence is the lowest level scripted in: faith > religion > family. | graphical_faith = catholic_gfx |
| piety_icon_group | gfx | All faiths in this religion default to this set of piety icons. Order of precedence is the lowest level scripted in: faith > religion > family. | piety_icon_group = christian |
| tenet_background_icon | image file | All faiths in this religion default to this doctrine background icon. Order of precedence is the lowest level scripted in: faith > religion > family. | doctrine_background_icon = core_tenet_banner_christian.dds |
| theocracy_government_type | government_type_key | Which government type should theocratic rulers of this religion have? (falls back to default theocracy government type if not defined) | theocracy_government_type = ecclesiastical_government |
| pagan_roots | boolean | If yes, then faiths without the unreformed doctrine are considered reformed by the interface. | pagan_roots = yes |
| doctrine | doctrine | Doctrines defined in a religion will be applied to all faiths within it. This is only at game start; it is purely for script convenience, and would be equivalent to putting the doctrine in all the faiths. It can be overridden by putting a different doctrine in the group in the specific faith. Note that doctrines that allow more than one pick can **not** be defined on a religion level, as there's no obvious override system that would work then. Doctrines cannot be defined after the faiths section. | doctrine = doctrine_spiritual_head |
| traits | clause | Defines which traits are considered virtues and sins by the religion. Notes on virtues and sins: List traits that are virtues for all followers. Trait groups also work. If more than one trait in a group is defined (or the group itself), only the first will be shown in the UI sins = { ... } # (sins) # Virtues and sins give an opinion bonus/penalty (see VIRTUOUS_TRAIT and SINFUL_TRAIT defines). For that it is the "viewer's" faith that matters. # E.g. if generous is a christian virtue, all christian characters will think more highly of all others with that trait, even if the others are not christian. # Holders of the traits will also get the virtue_owner_modifier/sin_owner_modifier for each matching trait. # Virtues and sins can optionally have a multiplier to scale the effects (default is 1): virtues = { brave = 0.5 } # scales both the opinion effect and the modifier # Scale is optional defaults to 1 # Weight is optional, defaults to 1. A virtue contributes its weight as base Spiritual Fulfillment for holders of the trait; a sin subtracts it instead. # The value is additionally multiplied per source by the SPIRITUAL_FULFILLMENT_MULT_* defines (religion trait, core/permitted/personal tenet). # If the same trait is listed more than once (or claimed by several tenets/doctrines), the entry with the highest weight decides its status and value sins = { stubborn = { scale = 2 weight = 2 } } | virtues = { brave generous } sins = { stubborn = { scale = 2 weight = 2 } } |
| reserved_male_names | list<string> | Names listed here will be applied to all faiths that don't define reserved_male_names themselves. These names can be applied to newborn males when selecting a religion-based name. | reserved_male_names = { Rodrigo Johan Paradoxus } |
| reserved_female_names | list<string> | Same as reserved_male_names, but applied to female characters instead. |  |
| custom_faith_icons | list<gfx> | When creating a custom faith, these will be the available icons. Path is "gfx/interface/icons/religion/%s.dds", where %s is the name. Also needs a text icon | custom_faith_icons = { custom_faith_1 custom_faith_2 custom_faith_3 } |
| localization | list<localization keys> | See localization inside faiths below. |  |
| holy_order_names | list<clause> | Names and CoAs that can be used by holy orders of this religion. These are used if there are none available for the faith. If there are none left here, it uses "holy_order_default" as name and a randomly generated CoA instead. | holy_order_names = { { name = "holy_order_name1" coat_of_arms = "holy_order_coa1" } { name = "holy_order_name2" coat_of_arms = "holy_order_coa2" } ... } |
| holy_order_maa | list<regiment type> | Men-At-Arms types mostly used for holy orders. The culture of the headquarters of the holy order must have unlocked the required innovation. (It will use the last available type in the list.) | holy_order_maa = { huscarl } |

## Faith structure

Faiths are located in the */common/religion/faith_types* folder. Faiths are defined in the *00_faith_types.txt*, new faiths can be defined in a separate file. Here is an example of a fictional faith using the religion defined above.

```
lobbist = {
    main_rite = lobbist
	faith_details = {
		religion = sea_cults
		color = { 0.2 0.2 0.9 }
		icon = lobbist
		reformed_icon = lobbist_reformed
		graphical_faith = "pagan_gfx"
	}

	eminent_holy_sites = {
		uppsala
		lejre
		paderborn
	}

	holy_sites = {
		zeeland
		ranaheim
	}

	tenets = {
		tenet_warmonger
		tenet_human_sacrifice
		tenet_ancestor_worship
	}

	doctrines = {
		unreformed_faith_doctrine
        
	}
}
```

Below is a list of all parameters that can be set for faiths.

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| religion | key | Required, sets the religion for the faith. | religion = christianity_religion |
| color | rgb |  | color = { 0.2 0.2 0.9 } |
| icon | gfx | If you want to use another faith's icon | icon = bosnian_church |
| graphical_faith | gfx | This faith (and custom faiths based on this faith) use this 3D model (currently used for temple assets). Order of precedence is the lowest level scripted in: faith > religion > family. | graphical_faith = catholic_gfx |
| piety_icon_group | gfx | This faith (and custom faiths based on this faith) use this set of piety icons. Order of precedence is the lowest level scripted in: faith > religion > family. | piety_icon_group = christian |
| doctrine_background_icon | gfx | This faith (and custom faiths based on this faith) use this doctrine background icon. Order of precedence is the lowest level scripted in: faith > religion > family. |  |
| religious_head | title | What title should be this faith's religious head. If not set, will not have a religious head (unless created elsewhere in script) | religious_head = d_coptic_papacy |
| head_of_rite | title | Head of rite override - if set, holder of this title will be head of their rite ahead of clerical region rulers and secular rulers. Head of faith still is the absolute priority | head_of_rite = k_papal_state |
| holy_sites | holy site | The faith's Holy Sites that are not Eminent. They apply no global bonuses, only local ruler/county modifiers | holy_site = { cologne } |
| eminent_holy_sites | holy site | The faith's Eminent Holy Sites, which also apply global bonuses. Exclusive with holy_sites - never list one twice | eminent_holy_sites = { jerusalem } |
| tenets | tenet | If the faith has no scripted main Rite, tenets and tenet_selection_pair seed its dynamically created main Rite. If the faith has a scripted main Rite, define its core tenets on that Rite instead; the Rite's tenets override these. | tenets = { tenet_communion } |
| doctrines | doctrine | Faith doctrines are additive to a scripted main Rite. The faith doctrine is added when the Rite and parent religion have not already filled its doctrine group; a doctrine on the Rite in the same group takes precedence. Keep doctrines intrinsic to every Rite of the faith here. Put Rite-specific doctrine choices on the individual Rite. For a faith with no scripted main Rite, these doctrines seed the dynamically created main Rite. | doctrines = { doctrine_pluralism_pluralistic } |
| reserved_male_names/reserved_female_names | list<string> |  |  |
| localization |  |  |  |

## Rite structure

Rites are located in the */common/religion/rite_types* folder. Here is an example of a fictional rite using the faith defined above.

```

lobbist = {
	name = lobbist
	desc = lobbist_desc
	founder = k_sweden
	faith = lobbist

	color = { 0.3 0.3 0.9 }
	icon = christianity_papal_cross_01
    tenets = {
        tenet_communion
    }

	tenet_selection_pair = {
		requires_dlc_flag = by_god_alone
		tenet = tenet_dulia
		fallback_tenet = tenet_armed_pilgrimages
	}
	tenet_selection_pair = {
		requires_dlc_flag = by_god_alone
		tenet = tenet_apostolic_succession
		fallback_tenet = tenet_communal_identity
	}

	doctrines = {
		special_doctrine_is_western_christian_faith
		doctrine_clerical_marriage_disallowed
		doctrine_adultery_men_shunned
		doctrine_homosexuality_shunned
	}
}

```

Below is a list of all parameters that can be set for rites.

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| name | key | Dynamic description selecting name of rite. | name = roman_rite |
| desc | key + _desc | Dynamic description selecting description of rite. | desc = roman_rite_desc |
| color | rgb |  | color = { 0.2 0.2 0.9 } |
| icon | gfx | If you want to use a specific icon. The icon will be taken from the DYNAMIC_RITE_ICON_PATH path | icon = christianity_papal_cross_01 |
| graphical_faith | gfx | This faith (and custom faiths based on this faith) use this 3D model (currently used for temple assets). Order of precedence is the lowest level scripted in: faith > religion > family. | graphical_faith = catholic_gfx |
| founder | title_key | Rite founder will be first holder of provided title (unless set elsewhere in script) | founder = k_papal_state |
| faith | key | What is the parent faith of this Rite? If a faith has no scripted Rites a dynamic one with the same name will be created instead if no parent faith is defined, the Rite will not be generated from history and will only be available via the create_rite_from_type effect. | faith = christian_faith |
| cultures | key | keys of cultures associated with this rite. refers to the cultures found in culture/cultures | cultures = { italian roman lombard langobard cisalpine } |
| convert | bool | if set to no, characters cannot convert to this rite. default value is yes | convert = yes |
| create | bool | if set to no, this rite will not be created until specified in history. default value is yes | create = yes |
| tenets | tenet | List of tenets associated with this Rite. If this is a faith's scripted main Rite, these are the faith's effective core tenets; do not duplicate them in the faith type. | tenets = { tenet_communion } |
| doctrines | doctrine | List of doctrines associated with this Rite. Rite doctrines override parent-religion and faith doctrines from the same doctrine group. Faith doctrines from otherwise unfilled groups are added to the instantiated main Rite. | doctrines = { doctrine_clerical_marriage_disallowed } |
| localization |  |  |  |

## Localization

The localization clause in both faiths and religions provides key-value pairs for localization. However, this clause does not include object localization for the religion/faith itself and its basic properties. The following localization keys also need defining:

- <religion/faith_name>
- <religion/faith_name>_adj
- <religion/faith_name>_adherent
- <religion/faith_name>_adherent_plural
- <religion/faith_name>_desc

Below is a list of keys that need to be paired for localization. Although you can use this as a reference, it is also possible to simply copy and paste this list from a vanilla file and add your own keys where needed. Although many items in the list are not relevant to many religions/faiths, they can simply be assigned to a key used by another more relevant item. (e.g. FertilityGodName in Christianity is given as "$christianity_high_god_name$" in the localization file):

- HighGodName
- HighGodNamePossessive
- HighGodNameSheHe
- HighGodHerselfHimself
- HighGodHerHis
- HighGodNameAlternate
- HighGodNameAlternatePossessive
- CreatorName
- CreatorNamePossessive
- CreatorSheHe
- CreatorHerHis
- CreatorHerHim
- HealthGodName
- HealthGodNamePossessive
- HealthGodSheHe
- HealthGodHerHis
- HealthGodHerHim
- FertilityGodName
- FertilityGodNamePossessive
- FertilityGodSheHe
- FertilityGodHerHis
- FertilityGodHerHim
- WealthGodName
- WealthGodNamePossessive
- WealthGodSheHe
- WealthGodHerHis
- WealthGodHerHim
- HouseholdGodName
- HouseholdGodNamePossessive
- HouseholdGodSheHe
- HouseholdGodHerHis
- HouseholdGodHerHim
- FateGodName
- FateGodNamePossessive
- FateGodSheHe
- FateGodHerHis
- FateGodHerHim
- KnowledgeGodName
- KnowledgeGodNamePossessive
- KnowledgeGodSheHe
- KnowledgeGodHerHis
- KnowledgeGodHerHim
- WarGodName
- WarGodNamePossessive
- WarGodSheHe
- WarGodHerHis
- WarGodHerHim
- TricksterGodName
- TricksterGodNamePossessive
- TricksterGodSheHe
- TricksterGodHerHis
- TricksterGodHerHim
- NightGodName
- NightGodNamePossessive
- NightGodSheHe
- NightGodHerHis
- NightGodHerHim
- WaterGodName
- WaterGodNamePossessive
- WaterGodSheHe
- WaterGodHerHis
- WaterGodHerHim
- PantheonTerm
- PantheonTermHasHave
- GoodGodNames (list)
- DevilName
- DevilNamePossessive
- DevilSheHe
- DevilHerHis
- DevilHerselfHimself
- EvilGodNames (list)
- HouseOfWorship
- HouseOfWorshipPlural
- ReligiousSymbol
- ReligiousText
- ReligiousHeadName
- ReligiousHeadTitleName
- DevoteeMale
- DevoteeMalePlural
- DevoteeFemalePlural
- DevoteeNeuter
- DevoteeNeuterPlural
- PriestMale
- PriestMalePlural
- PriestFemale
- PriestFemalePlural
- PriestNeuter
- PriestNeuterPlural
- AltPriestTermPlural
- BishopMale
- BishopMalePlural
- BishopFemale
- BishopFemalePlural
- BishopNeuter
- BishopNeuterPlural
- DivineRealm
- PositiveAfterLife
- NegativeAfterLife
- DeathDeityName
- DeathDeityNamePossessive
- DeathDeitySheHe
- DeathDeityHerHis
- WitchGodName
- WitchGodHerHis
- WitchGodSheHe
- WitchGodHerHim
- WitchGodMistressMaster
- WitchGodMotherFather
- GHWName
- GHWNamePlural

## Graphics

No graphical modding is required to create a religion or faith, since there is an abundance of icons in the vanilla game, either in use by other religions or reserved for custom faiths. However, adding a new icon is very simple, if you feel that none of the vanilla icons are fitting for your religion. In the path */gfx/interface/icons/faith*, create a new 100x100 dds file. The name of the file is how the icon is referred to in the religion file. (e.g. icon = lobbist will refer to /gfx/interface/icons/faith/lobbist.dds).

## Holy sites

  - *See also: Holy site ID*

Custom holy sites can be added in a text document in the */common/religion/holy_site_types* folder. Each site is identified by a name, and contains information on the location of the site and the benefits (or potentially negatives) it brings.

```
jerusalem = {
	county = c_jerusalem

	parameters = {
		jerusalem_conversion_bonus # +20% County Conversion
	}

	county_holder_character_modifier = {
		monthly_piety_gain_mult = 0.05
		different_faith_opinion = 5
	}

	county_modifier_scaled = {
		scale = holy_site_total_artifact_rarity
		development_growth_factor = 0.01
		travel_danger = -1
	}

	faith_character_modifier = {
		character_travel_safety_mult = 0.1
	}

	faith_character_modifier_scaled = {
		scale = holy_site_total_artifact_rarity
		character_travel_safety_mult = 0.01
	}
}
```

Below are the attributes which can be assigned to a holy site. Only the county is necessary.

| Attribute | Type | Description | Example |
| --- | --- | --- | --- |
| county | title | The county in which the holy site is located | county = c_jerusalem |
| barony | title | The barony in which the holy site is located | barony = b_vaticano |
| character modifier | modifier | Applied to all characters of any faith with this holy site when the holder of the barony is of their faith | character_modifier = { monthly_piety_gain_mult = 0.2 } |
| parameters | parameter list | Arbitrary parameters to be checked in applying various effects. | parameters = { kerala_conversion_bonus # +50% County Conversion Speed } |
| faith_character_modifier | modifiers | Modifiers applied to all characters of any faith with this holy site when the holder of the barony is of their faith. | faith_character_modifier = { clergy_opinion = 5 } |
| faith_character_modifier_scaled | scalable modifier list | Each entry defines a character modifier whose values multiply by a script-evaluated scale and is applied to all characters of the faith. Will only be applied if the holy site is an Eminent holy site for the Faith. | faith_character_modifier_scaled = { scale = holy_site_total_artifact_rarity monthly_piety_gain_mult = 0.01 faith_conversion_piety_cost_mult = -0.01 } |
| county_holder_character_modifier | modifiers | Modifiers applied to holder of county of holy site, if same faith. | county_holder_character_modifier = { monthly_piety_gain_mult = 0.05 } |
| county_modifier_scaled | scalable modifier list | Each entry defines a county modifier whose values multiply by a script-evaluated scale and is applied to the holy site's county. Will be applied if Regular or Eminent holy site of faith. | county_modifier_scaled = { scale = holy_site_total_artifact_rarity tax_mult = 0.01 travel_danger = -1 } |

Holy sites also require the following keys in localization:

- holy_site_<name>_name
- holy_site_<name>_effect_name
- holy_site_<name>_effects

```
 holy_site_jerusalem_name:0 "Jerusalem"
 holy_site_jerusalem_effect_name:0 "From [holy_site|E] #weak ($holy_site_jerusalem_name$)#!"
 holy_site_jerusalem_effects:0 "County Conversion Speed: #P +20%#!"
```

## Tenet ID

Each tenet has an internal ID used to reference it within the game files. In general, to get the tenet ID from its name:

1. Take the non-variant name (i.e. non-faith specific)
2. Turn all upper case letters into lower case (`A...Z->a...z`)
3. Replace all spaces () with underscores (`_`)
4. Add `tenet_` to the beginning

Tenets that do not fit the pattern above have been listed below:

| Name | Tenet ID |
| --- | --- |
| Auspicious Birthright | tenet_mystical_birthright |
| Ritual Suicide | tenet_consolamentum |
| Ecclesiarchy | tenet_pentarchy |
| Religious Law | tenet_religious_legal_pronouncements |
| Sacred Lies | tenet_sacred_shadows |
| Sanctioned False Conversions | tenet_false_conversion_sanction |
| Struggle and Submission | tenet_struggle_submission |
| Syncretic Folk Traditions | tenet_unreformed_syncretism |
