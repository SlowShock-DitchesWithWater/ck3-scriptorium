<!-- 来源: https://ck3.paradoxwikis.com/Data_types oldid=14585 抓取于 2026-10-22T21:43:41+08:00 -->

# Data types — Types


The following is a list of common Types and is *not* the complete list. There are close to 700 different Types listed by the game, however many of them are restricted on where they can be used or provide niche functions that are not commonly used.

### ActiveCasusBelli

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetAttacker | Character |  |
| GetDefender | Character |  |
| GetFirstTitleTarget | Title |  |
| GetType | CasusBelliType |  |
| AccessSelf | [unregistered] |  |
| GetAttacker | [unregistered] |  |
| GetDefender | [unregistered] |  |
| GetFirstTitleTarget | [unregistered] |  |
| GetType | [unregistered] |  |
| Self | [unregistered] |  |

### ActiveCouncilTask

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetCouncillor | Character |  |
| GetLocation | Province |  |
| GetPositionType | CouncilPositionType |  |
| GetProgressBreakdown | ValueBreakdown |  |
| GetTargetCourt | Character |  |
| GetTargetProvince | Province |  |
| GetTaskType | CouncilTaskType |  |
| GetTaskTypeOrDefault | CouncilTaskType |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| CanBeFired | bool |  |
| CanBeReassigned | bool |  |
| GetETA | CString |  |
| GetName | CString |  |
| GetPositionName | CString |  |
| GetPositionNamePossesive | CString |  |
| GetPositionTooltip | CString |  |
| GetPositionType | [unregistered] |  |
| GetProgress | CFixedPoint |  |
| GetProgressBreakdown | [unregistered] |  |
| GetProgressFloat | float |  |
| GetProgressMax | CFixedPoint |  |
| GetProgressMaxFloat | float |  |
| GetProgressPie | float |  |
| GetScopes | [unregistered] |  |
| GetTaskEffect | CString |  |
| GetTaskTarget | CString |  |
| GetTaskTypeOrDefault | [unregistered] |  |
| GetTaskValueName | CString |  |
| HasCouncillor | bool |  |
| HasMainSkill | bool |  |
| IsAutomaticallyFilled | bool |  |
| IsFrozen | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### Activity

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetLocation | Province |  |
| GetOwner | Character |  |
| GetType | ActivityType |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| Custom | CString |  |
| GetAccepted | [unregistered] |  |
| GetDeclined | [unregistered] |  |
| GetInvited | [unregistered] |  |
| GetLocation | [unregistered] |  |
| GetName | CString |  |
| GetOwner | [unregistered] |  |
| IsActivated | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |
| WriteListOfAcceptedGuests | CString |  |

### Army

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetCommander | Character |  |
| GetComposition | ArmyComposition |  |
| GetLocation | Province |  |
| GetOwner | Character |  |
| GetRaid | Raid |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| CalcQualityLevel | int32 |  |
| CommanderIsOwner | bool |  |
| GetAIInfo | CString |  |
| GetActivityFrame | int32 |  |
| GetAiCoordinatorId | int32 |  |
| GetAiSubUnitStackId | int32 |  |
| GetAiUnitStackId | int32 |  |
| GetArmyAttrition | int32 |  |
| GetArmyAttritionBreakdown | CString |  |
| GetArmyAttritionBreakdownPercentage | CString |  |
| GetArmyAttritionPercentage | CFixedPoint |  |
| GetArmyId | int32 |  |
| GetArmyQualityName | CString |  |
| GetArmyStatusIcon | [unregistered] |  |
| GetCombatPredictionForTooltip | CString |  |
| GetCommanderTooltip | CString |  |
| GetDescription | CString |  |
| GetDisembarkPenaltyDays | int32 |  |
| GetEmbarkInfoForTooltip | CString |  |
| GetEventTroopsAssociatedWithWarTooltip | CString |  |
| GetGatheringDaysLeft | int32 |  |
| GetGatheringProgress | float |  |
| GetLootCap | CFixedPoint |  |
| GetMovementInfoForTooltip | CString |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetRaidLoot | CFixedPoint |  |
| GetRaisingFleetCost | CFixedPoint |  |
| GetSoldierCount | int32 |  |
| GetSoldierCountString | CString |  |
| GetSpecialArmyStatus | CString |  |
| GetSupplyDesc | CString |  |
| GetSupplyInfoForTooltip | CString |  |
| GetUnitId | int32 |  |
| HasEventTroops | bool |  |
| HasLooterStance | bool |  |
| IsEmbarked | bool |  |
| IsEnemyOrHostileToPlayer | bool |  |
| IsGathering | bool |  |
| IsMoving | bool |  |
| IsNeutralToPlayer | bool |  |
| IsRaidArmy | bool |  |
| IsRaidLootCapped | bool |  |
| IsRecentlyDisembarked | bool |  |
| IsRetreating | bool |  |
| IsSieging | bool |  |
| IsTakingRaidAction | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### Artifact

Note that this list has been generated programmatically.

| Function | Return Type |
| --- | --- |
| GetAssociatedTitle | Title |
| GetCulture | Culture |
| GetHistory | ArtifactHistory |
| GetOwner | Character |
| MakeScope | Scope |
| AccessSelf | [unregistered] |
| CanBenefit | bool |
| CanBenefitPlayer | bool |
| CanPlayerEquip | bool |
| CanReforge | bool |
| CanReforgeOrRepair | bool |
| CanRepair | bool |
| Custom | CString |
| GetAge | int32 |
| GetAssociatedTitle | [unregistered] |
| GetCanBenefitPlayerDesc | CString |
| GetCanPlayerEquipDesc | CString |
| GetCategory | CString |
| GetCreator | [unregistered] |
| GetCulture | [unregistered] |
| GetDesc | CString |
| GetDurability | CFixedPoint |
| GetDurabilityTooltip | CString |
| GetFallbackEffects | CString |
| GetFeatureText | CString |
| GetForgottenSoldiersCount | int32 |
| GetHistory | [unregistered] |
| GetHouseClaimants | [unregistered] |
| GetHouseClaimantsString | CString |
| GetID | uint32 |
| GetIcon | [unregistered] |
| GetIconFrame | int32 |
| GetKills | [unregistered] |
| GetMaxDurability | CFixedPoint |
| GetModifierEffects | CString |
| GetName | CString |
| GetNameNoTooltip | CString |
| GetOwner | [unregistered] |
| GetPersonalClaimants | [unregistered] |
| GetPlayerModifierEffects | CString |
| GetRarity | CString |
| GetRarityAndSlotType | CString |
| GetRarityAndType | CString |
| GetRarityColor | CVector4f |
| GetReforgeOrRepairTooltip | CString |
| GetReforgeTooltip | CString |
| GetRepairTooltip | CString |
| GetSlotType | CString |
| GetType | CString |
| GetYearsUntilDecay | int32 |
| GetYearsUntilHouseClaim | int32 |
| HasCanBenefit | bool |
| HasClaim | bool |
| HasFeature | bool |
| HasFeatureOfType | bool |
| HasImminentHouseClaim | bool |
| IsCourtArtifact | bool |
| IsDurabilityLow | bool |
| IsInventoryArtifact | bool |
| IsUnique | bool |
| IsValid | bool |
| MakeScope | Scope |
| OpenArtifactKills | void |
| OpenRenameWindow | void |
| Self | [unregistered] |
| ShouldDecay | bool |

### Character

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetActiveCouncilTask | ActiveCouncilTask |  |
| GetActiveLawInGroupWithFlag | Law |  |
| GetBeneficiary | Character |  |
| GetBetrothed | Character |  |
| GetBirthDate | Date |  |
| GetCapitalLocation | Province |  |
| GetConcubinist | Character |  |
| GetConsort | Character |  |
| GetConsortOrBetrothed | Character |  |
| GetCouncillorPosition | ActiveCouncilTask |  |
| GetCulture | Culture |  |
| GetCurrentActivity | Activity |  |
| GetCurrentLocation | Province |  |
| GetDeathDate | Date |  |
| GetDesignatedHeir | Character |  |
| GetDynasty | Dynasty |  |
| GetEmployer | Character |  |
| GetFaith | Faith |  |
| GetFather | Character |  |
| GetFocus | FocusType |  |
| GetFocusType | FocusType |  |
| GetGovernment | GovernmentType |  |
| GetHouse | DynastyHouse |  |
| GetImprisonedBy | Character |  |
| GetKiller | Character |  |
| GetKnightArmy | Army |  |
| GetLiege | Character |  |
| GetLiegeEvenWhenDead | Character |  |
| GetLiegeTitleEvenWhenDead | Title |  |
| GetLifestyle | Lifestyle |  |
| GetMother | Character |  |
| GetPlayerHeir | Character |  |
| GetPrimaryHolding | Title |  |
| GetPrimarySpouse | Character |  |
| GetPrimarySpouseOrBetrothed | Character |  |
| GetPrimaryTitle | Title |  |
| GetRaidHostilityEnd | Date |  |
| GetRealFather | Character |  |
| GetRelationOfType | Character |  |
| GetSealCoA | CoatOfArms |  |
| GetTopLiege | Character |  |
| GetVassalContract | VassalContract |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| CalcUnusedConsortSlots | int32 |  |
| CalcUnusedSecondarySpouseSlots | int32 |  |
| CalcUnusedSpouseSlots | int32 |  |
| CanBePunished | [unregistered] |  |
| CanCustomizePortrait | bool |  |
| CanHaveConsorts | bool |  |
| CanPlayerChangeMyFocus | bool |  |
| CanRaid | bool |  |
| CanRaiseRegiments | [unregistered] |  |
| CanStartRaid | bool |  |
| CharacterKnowsOfKiller | bool |  |
| CourtierWantsToLeaveCourt | bool |  |
| Custom | CString |  |
| Custom2 | CString |  |
| Custom2_Title | CString |  |
| GetAIBoldness | int32 |  |
| GetAIBoldnessAsAffectedByPlayerDread | [unregistered] |  |
| GetAICompassion | int32 |  |
| GetAIEnergy | int32 |  |
| GetAIGreed | int32 |  |
| GetAIHonor | int32 |  |
| GetAIPersonality | CString |  |
| GetAIRationality | int32 |  |
| GetAISociability | int32 |  |
| GetAIVengefulness | int32 |  |
| GetAIZeal | int32 |  |
| GetActiveCouncilTask | [unregistered] |  |
| GetActiveLawInGroupWithFlag | [unregistered] |  |
| GetAge | int32 |  |
| GetAgeInfo | CString |  |
| GetAiBudgetDescription | CString |  |
| GetAnimatedPortrait | [unregistered] |  |
| GetApprovalReasons | CString |  |
| GetAwayCourtiers | [unregistered] |  |
| GetBalance | [unregistered] |  |
| GetBalanceBreakdown | [unregistered] |  |
| GetBanishReasons | CString |  |
| GetBaseWeight | int32 |  |
| GetBeneficiary | Character |  |
| GetBetrothed | [unregistered] |  |
| GetBirthDate | [unregistered] |  |
| GetCachedPortrait | [unregistered] |  |
| GetCapitalLocation | [unregistered] |  |
| GetCharacterRelationCombine | CString |  |
| GetCharacterViewName | [unregistered] |  |
| GetCharacterViewNameNicknamed | [unregistered] |  |
| GetCharacterViewNameNicknamedNoTooltip | [unregistered] |  |
| GetCharacterViewNameNicknamedNoTooltipRegnal | [unregistered] |  |
| GetCharacterViewNameNicknamedOrMe | [unregistered] |  |
| GetCharacterViewNameNicknamedOrMeNoTooltip | [unregistered] |  |
| GetCharacterViewNameNicknamedOrMeNoTooltipRegnal | [unregistered] |  |
| GetCharacterViewNameNicknamedOrMeRegnal | [unregistered] |  |
| GetCharacterViewNameNicknamedPossessive | [unregistered] |  |
| GetCharacterViewNameNicknamedPossessiveNoTooltip | [unregistered] |  |
| GetCharacterViewNameNicknamedPossessiveNoTooltipRegnal | [unregistered] |  |
| GetCharacterViewNameNicknamedPossessiveOrMy | [unregistered] |  |
| GetCharacterViewNameNicknamedPossessiveOrMyNoTooltip | [unregistered] |  |
| GetCharacterViewNameNicknamedPossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetCharacterViewNameNicknamedPossessiveOrMyRegnal | [unregistered] |  |
| GetCharacterViewNameNicknamedPossessiveRegnal | [unregistered] |  |
| GetCharacterViewNameNicknamedRegnal | [unregistered] |  |
| GetCharacterViewNameNoTooltip | [unregistered] |  |
| GetCharacterViewNameNoTooltipRegnal | [unregistered] |  |
| GetCharacterViewNameOrMe | [unregistered] |  |
| GetCharacterViewNameOrMeNoTooltip | [unregistered] |  |
| GetCharacterViewNameOrMeNoTooltipRegnal | [unregistered] |  |
| GetCharacterViewNameOrMeRegnal | [unregistered] |  |
| GetCharacterViewNamePossessive | [unregistered] |  |
| GetCharacterViewNamePossessiveNoTooltip | [unregistered] |  |
| GetCharacterViewNamePossessiveNoTooltipRegnal | [unregistered] |  |
| GetCharacterViewNamePossessiveOrMy | [unregistered] |  |
| GetCharacterViewNamePossessiveOrMyNoTooltip | [unregistered] |  |
| GetCharacterViewNamePossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetCharacterViewNamePossessiveOrMyRegnal | [unregistered] |  |
| GetCharacterViewNamePossessiveRegnal | [unregistered] |  |
| GetCharacterViewNameRegnal | [unregistered] |  |
| GetCommanderAdvantage | int32 |  |
| GetCommanderAdvantageDesc | CString |  |
| GetCommanderLeadingOwnAdvantageDesc | CString |  |
| GetConcubineName | [unregistered] |  |
| GetConcubinist | [unregistered] |  |
| GetConsort | [unregistered] |  |
| GetConsortOrBetrothed | [unregistered] |  |
| GetContextTooltip | CString |  |
| GetCouncilTitle | CString |  |
| GetCouncilTitleFirstName | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamed | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedNoTooltip | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedNoTooltipRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedOrMe | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedOrMeNoTooltip | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedOrMeNoTooltipRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedOrMeRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedPossessive | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedPossessiveNoTooltip | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedPossessiveNoTooltipRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedPossessiveOrMy | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedPossessiveOrMyNoTooltip | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedPossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedPossessiveOrMyRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedPossessiveRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameNicknamedRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameNoTooltip | [unregistered] |  |
| GetCouncilTitleFirstNameNoTooltipRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameOrMe | [unregistered] |  |
| GetCouncilTitleFirstNameOrMeNoTooltip | [unregistered] |  |
| GetCouncilTitleFirstNameOrMeNoTooltipRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameOrMeRegnal | [unregistered] |  |
| GetCouncilTitleFirstNamePossessive | [unregistered] |  |
| GetCouncilTitleFirstNamePossessiveNoTooltip | [unregistered] |  |
| GetCouncilTitleFirstNamePossessiveNoTooltipRegnal | [unregistered] |  |
| GetCouncilTitleFirstNamePossessiveOrMy | [unregistered] |  |
| GetCouncilTitleFirstNamePossessiveOrMyNoTooltip | [unregistered] |  |
| GetCouncilTitleFirstNamePossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetCouncilTitleFirstNamePossessiveOrMyRegnal | [unregistered] |  |
| GetCouncilTitleFirstNamePossessiveRegnal | [unregistered] |  |
| GetCouncilTitleFirstNameRegnal | [unregistered] |  |
| GetCouncilTitleForPosition | CString |  |
| GetCouncilTitleForPositionPossessive | CString |  |
| GetCouncilTitlePossessive | CString |  |
| GetCouncillorModifierDesc | CString |  |
| GetCourt | [unregistered] |  |
| GetCourtierLeaveDescription | CString |  |
| GetCulture | [unregistered] |  |
| GetCurrentActivity | [unregistered] |  |
| GetCurrentLocation | [unregistered] |  |
| GetCurrentWeight | int32 |  |
| GetDeathDate | [unregistered] |  |
| GetDeathOrBirthDateInfo | CString |  |
| GetDeathReason | CString |  |
| GetDeathReasonHideKiller | CString |  |
| GetDeathReasonIcon | [unregistered] |  |
| GetDebtModifierDescription | CString |  |
| GetDebugCourtierLeaveReasons | CString |  |
| GetDebugGuestArriveReasons | CString |  |
| GetDebugGuestArriveStatus | bool |  |
| GetDebugGuestScore | CFixedPoint |  |
| GetDebugTooltip | CString |  |
| GetDefaultRealmFlagTooltip | CString |  |
| GetDefaultRealmFlagTooltipNoClickInfo | CString |  |
| GetDefaultRealmFlagTooltipPrimaryTitleClickInfo | CString |  |
| GetDesignatedHeir | [unregistered] |  |
| GetDesiredNumberOfConsorts | int32 |  |
| GetDifficultyInfoText | [unregistered] |  |
| GetDivorceReasons | CString |  |
| GetDomainLimit | int32 |  |
| GetDomainLimitBreakdown | CString |  |
| GetDomainLimitGracePeriodHoldings | CString |  |
| GetDomainLimitOverrunWithGracePeriod | int32 |  |
| GetDomainLimitOverrunWithoutGracePeriod | int32 |  |
| GetDomainLimitTooltip | CString |  |
| GetDomainSize | int32 |  |
| GetDomainSizeWithGracePeriod | int32 |  |
| GetDread | CFixedPoint |  |
| GetDreadBreakdown | [unregistered] |  |
| GetDreadEffectIconFrameFor | int32 |  |
| GetDreadEffectTooltipFor | CString |  |
| GetDynasty | [unregistered] |  |
| GetDynastyHeadRelationFrame | int32 |  |
| GetDynastyHeadRelationTooltip | CString |  |
| GetDynastyHeadTooltip | CString |  |
| GetDynastyHouseName | CString |  |
| GetDynastyHouseNameNoTooltip | CString |  |
| GetDynastyMembersText | CString |  |
| GetDynastyName | CString |  |
| GetDynastyNameNoTooltip | CString |  |
| GetEmployer | [unregistered] |  |
| GetExecuteReasons | CString |  |
| GetFaith | [unregistered] |  |
| GetFather | [unregistered] |  |
| GetFertility | CFixedPoint |  |
| GetFirstName | [unregistered] |  |
| GetFirstNameBase | CString |  |
| GetFirstNameNicknamed | [unregistered] |  |
| GetFirstNameNicknamedNoTooltip | [unregistered] |  |
| GetFirstNameNicknamedNoTooltipRegnal | [unregistered] |  |
| GetFirstNameNicknamedOrMe | [unregistered] |  |
| GetFirstNameNicknamedOrMeNoTooltip | [unregistered] |  |
| GetFirstNameNicknamedOrMeNoTooltipRegnal | [unregistered] |  |
| GetFirstNameNicknamedOrMeRegnal | [unregistered] |  |
| GetFirstNameNicknamedPossessive | [unregistered] |  |
| GetFirstNameNicknamedPossessiveNoTooltip | [unregistered] |  |
| GetFirstNameNicknamedPossessiveNoTooltipRegnal | [unregistered] |  |
| GetFirstNameNicknamedPossessiveOrMy | [unregistered] |  |
| GetFirstNameNicknamedPossessiveOrMyNoTooltip | [unregistered] |  |
| GetFirstNameNicknamedPossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetFirstNameNicknamedPossessiveOrMyRegnal | [unregistered] |  |
| GetFirstNameNicknamedPossessiveRegnal | [unregistered] |  |
| GetFirstNameNicknamedRegnal | [unregistered] |  |
| GetFirstNameNoTooltip | [unregistered] |  |
| GetFirstNameNoTooltipRegnal | [unregistered] |  |
| GetFirstNameOrMe | [unregistered] |  |
| GetFirstNameOrMeNoTooltip | [unregistered] |  |
| GetFirstNameOrMeNoTooltipRegnal | [unregistered] |  |
| GetFirstNameOrMeRegnal | [unregistered] |  |
| GetFirstNamePossessive | [unregistered] |  |
| GetFirstNamePossessiveNoTooltip | [unregistered] |  |
| GetFirstNamePossessiveNoTooltipRegnal | [unregistered] |  |
| GetFirstNamePossessiveOrMy | [unregistered] |  |
| GetFirstNamePossessiveOrMyNoTooltip | [unregistered] |  |
| GetFirstNamePossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetFirstNamePossessiveOrMyRegnal | [unregistered] |  |
| GetFirstNamePossessiveRegnal | [unregistered] |  |
| GetFirstNameRegnal | [unregistered] |  |
| GetFocus | [unregistered] |  |
| GetFullName | [unregistered] |  |
| GetFullNameNicknamed | [unregistered] |  |
| GetFullNameNicknamedNoTooltip | [unregistered] |  |
| GetFullNameNicknamedNoTooltipRegnal | [unregistered] |  |
| GetFullNameNicknamedOrMe | [unregistered] |  |
| GetFullNameNicknamedOrMeNoTooltip | [unregistered] |  |
| GetFullNameNicknamedOrMeNoTooltipRegnal | [unregistered] |  |
| GetFullNameNicknamedOrMeRegnal | [unregistered] |  |
| GetFullNameNicknamedPossessive | [unregistered] |  |
| GetFullNameNicknamedPossessiveNoTooltip | [unregistered] |  |
| GetFullNameNicknamedPossessiveNoTooltipRegnal | [unregistered] |  |
| GetFullNameNicknamedPossessiveOrMy | [unregistered] |  |
| GetFullNameNicknamedPossessiveOrMyNoTooltip | [unregistered] |  |
| GetFullNameNicknamedPossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetFullNameNicknamedPossessiveOrMyRegnal | [unregistered] |  |
| GetFullNameNicknamedPossessiveRegnal | [unregistered] |  |
| GetFullNameNicknamedRegnal | [unregistered] |  |
| GetFullNameNoTooltip | [unregistered] |  |
| GetFullNameNoTooltipRegnal | [unregistered] |  |
| GetFullNameOrMe | [unregistered] |  |
| GetFullNameOrMeNoTooltip | [unregistered] |  |
| GetFullNameOrMeNoTooltipRegnal | [unregistered] |  |
| GetFullNameOrMeRegnal | [unregistered] |  |
| GetFullNamePossessive | [unregistered] |  |
| GetFullNamePossessiveNoTooltip | [unregistered] |  |
| GetFullNamePossessiveNoTooltipRegnal | [unregistered] |  |
| GetFullNamePossessiveOrMy | [unregistered] |  |
| GetFullNamePossessiveOrMyNoTooltip | [unregistered] |  |
| GetFullNamePossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetFullNamePossessiveOrMyRegnal | [unregistered] |  |
| GetFullNamePossessiveRegnal | [unregistered] |  |
| GetFullNameRegnal | [unregistered] |  |
| GetGlowTintColor | CVector4f |  |
| GetGold | [unregistered] |  |
| GetGoldText | [unregistered] |  |
| GetGoldTextNoIcon | [unregistered] |  |
| GetGoldTooltipWithBalance | [unregistered] |  |
| GetGovernment | [unregistered] |  |
| GetHealth | CFixedPoint |  |
| GetHealthIconFrame | [unregistered] |  |
| GetHealthInfo | [unregistered] |  |
| GetHeirToDesc | CString |  |
| GetHeldBaroniesCount | int32 |  |
| GetHerHim | [unregistered] |  |
| GetHerHis | [unregistered] |  |
| GetHerHisMy | [unregistered] |  |
| GetHersHis | [unregistered] |  |
| GetHerselfHimself | [unregistered] |  |
| GetHookOrHookableSecretsFrame | [unregistered] |  |
| GetHostileRaiders | [unregistered] |  |
| GetHouse | [unregistered] |  |
| GetHumanName | CString |  |
| GetHumanNameIfNotLocalPlayer | CString |  |
| GetID | [unregistered] |  |
| GetImprisonedBy | [unregistered] |  |
| GetImprisonmentReasons | CString |  |
| GetIncomeAsReligiousHead | CFixedPoint |  |
| GetIncomeBreakdownAsReligiousHead | CString |  |
| GetIncomeBreakdownFromTheocraticLease | CString |  |
| GetIncomeFromTheocraticLease | CFixedPoint |  |
| GetKills | [unregistered] |  |
| GetKnightArmy | [unregistered] |  |
| GetKnightBreakdown | [unregistered] |  |
| GetKnightCount | [unregistered] |  |
| GetKnightEffectiveness | CFixedPoint |  |
| GetKnightEffectivenessBreakdown | CString |  |
| GetLadyLord | [unregistered] |  |
| GetLeviesBreakdownFromTheocraticLease | CString |  |
| GetLeviesFromTheocraticLease | int32 |  |
| GetLiege | [unregistered] |  |
| GetLiegeEvenWhenDead | [unregistered] |  |
| GetLiegeTitleEvenWhenDead | [unregistered] |  |
| GetLifestyle | [unregistered] |  |
| GetLifestyleExperienceProgress | float |  |
| GetLifestyleXp | CFixedPoint |  |
| GetLocalizedText | CString |  |
| GetLocationDesc | [unregistered] |  |
| GetMaxConsorts | int32 |  |
| GetMaxIncomeFromTheocraticLease | CFixedPoint |  |
| GetMaxLeviesFromTheocraticLease | int32 |  |
| GetMaxMilitaryStrength | CFixedPoint |  |
| GetMaxSpouses | int32 |  |
| GetMilitaryStrengthPercentGUI | [unregistered] |  |
| GetMilitaryStrengthText | [unregistered] |  |
| GetModifierDescForTask | CString |  |
| GetModifierDescription | CString |  |
| GetMother | [unregistered] |  |
| GetMotherFather | [unregistered] |  |
| GetMyCouncillorsTitle | CString |  |
| GetName | [unregistered] |  |
| GetNameNicknamed | [unregistered] |  |
| GetNameNicknamedNoTooltip | [unregistered] |  |
| GetNameNicknamedNoTooltipRegnal | [unregistered] |  |
| GetNameNicknamedOrMe | [unregistered] |  |
| GetNameNicknamedOrMeNoTooltip | [unregistered] |  |
| GetNameNicknamedOrMeNoTooltipRegnal | [unregistered] |  |
| GetNameNicknamedOrMeRegnal | [unregistered] |  |
| GetNameNicknamedPossessive | [unregistered] |  |
| GetNameNicknamedPossessiveNoTooltip | [unregistered] |  |
| GetNameNicknamedPossessiveNoTooltipRegnal | [unregistered] |  |
| GetNameNicknamedPossessiveOrMy | [unregistered] |  |
| GetNameNicknamedPossessiveOrMyNoTooltip | [unregistered] |  |
| GetNameNicknamedPossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetNameNicknamedPossessiveOrMyRegnal | [unregistered] |  |
| GetNameNicknamedPossessiveRegnal | [unregistered] |  |
| GetNameNicknamedRegnal | [unregistered] |  |
| GetNameNoTooltip | [unregistered] |  |
| GetNameNoTooltipRegnal | [unregistered] |  |
| GetNameOrMe | [unregistered] |  |
| GetNameOrMeNoTooltip | [unregistered] |  |
| GetNameOrMeNoTooltipRegnal | [unregistered] |  |
| GetNameOrMeRegnal | [unregistered] |  |
| GetNamePossessive | [unregistered] |  |
| GetNamePossessiveNoTooltip | [unregistered] |  |
| GetNamePossessiveNoTooltipRegnal | [unregistered] |  |
| GetNamePossessiveOrMy | [unregistered] |  |
| GetNamePossessiveOrMyNoTooltip | [unregistered] |  |
| GetNamePossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetNamePossessiveOrMyRegnal | [unregistered] |  |
| GetNamePossessiveRegnal | [unregistered] |  |
| GetNameRegnal | [unregistered] |  |
| GetNickname | CString |  |
| GetNumTitlesFromTheocraticLease | int32 |  |
| GetNumVassalsTowardsLimit | int32 |  |
| GetNumberOfControlledHolySites | int32 |  |
| GetOpinionBreakdownText | CString |  |
| GetOpinionHeadingText | CString |  |
| GetOpinionOf | int32 |  |
| GetOpinionOfTint | CVector4f |  |
| GetOriginalFirstName | CString |  |
| GetPerkPoints | int32 |  |
| GetPerkPointsUsed | int32 |  |
| GetPiety | CFixedPoint |  |
| GetPietyLevel | int32 |  |
| GetPietyLevelTexture | [unregistered] |  |
| GetPietyTooltipWithBalance | CString |  |
| GetPlaceInSuccession | [unregistered] |  |
| GetPlayableFrame | int32 |  |
| GetPlayableFrameTooltip | CString |  |
| GetPlayerDreadEffectIconFrame | [unregistered] |  |
| GetPlayerDreadEffectTooltip | [unregistered] |  |
| GetPlayerDynastyRelationFrame | int32 |  |
| GetPlayerDynastyRelationTooltip | CString |  |
| GetPlayerGuestDescription | CString |  |
| GetPlayerHeir | [unregistered] |  |
| GetPlayerInteractionName | [unregistered] |  |
| GetPlayerInteractionTooltip | [unregistered] |  |
| GetPlayerInteractionValidBlockers | CString |  |
| GetPlayerInteractionWithTargetCharacterTooltip | CString |  |
| GetPlayerInteractionWithTargetSecretTooltip | CString |  |
| GetPlayerInteractionWithTargetTitleName | [unregistered] |  |
| GetPlayerInteractionWithTargetTitleTooltip | [unregistered] |  |
| GetPortrait | [unregistered] |  |
| GetPortraitFrameFrame | [unregistered] |  |
| GetPowerfulVassalFrame | [unregistered] |  |
| GetPowerfulVassalTooltip | [unregistered] |  |
| GetPrestige | CFixedPoint |  |
| GetPrestigeLevel | int32 |  |
| GetPrestigeLevelTexture | [unregistered] |  |
| GetPrestigeTooltipWithBalance | CString |  |
| GetPrimaryHolding | [unregistered] |  |
| GetPrimarySpouse | [unregistered] |  |
| GetPrimarySpouseOrBetrothed | [unregistered] |  |
| GetPrimaryTitle | [unregistered] |  |
| GetPrisoners | [unregistered] |  |
| GetProwess | [unregistered] |  |
| GetProwessBreakdown | [unregistered] |  |
| GetRaidTargets | [unregistered] |  |
| GetRealFather | [unregistered] |  |
| GetRelationOfType | [unregistered] |  |
| GetRelationToString | CString |  |
| GetRevokeReasons | CString |  |
| GetSexuality | CString |  |
| GetSexualityFrame | int32 |  |
| GetSheHe | [unregistered] |  |
| GetShortUIName | [unregistered] |  |
| GetShortUINameNoFormat | [unregistered] |  |
| GetShortUINameNoTooltip | [unregistered] |  |
| GetShortUINameNoTooltipNoFormat | [unregistered] |  |
| GetShortUINameNotMe | [unregistered] |  |
| GetShortUINameNotMeNoFormat | [unregistered] |  |
| GetShortUINameNotMeNoTooltip | [unregistered] |  |
| GetShortUINameNotMeNoTooltipNoFormat | [unregistered] |  |
| GetShortUINamePossessive | [unregistered] |  |
| GetShortUINamePossessiveNoFormat | [unregistered] |  |
| GetShortUINamePossessiveNoTooltip | [unregistered] |  |
| GetShortUINamePossessiveNoTooltipNoFormat | [unregistered] |  |
| GetShortUINamePossessiveNotMy | [unregistered] |  |
| GetShortUINamePossessiveNotMyNoFormat | [unregistered] |  |
| GetShortUINamePossessiveNotMyNoTooltip | [unregistered] |  |
| GetShortUINamePossessiveNotMyNoTooltipNoFormat | [unregistered] |  |
| GetSimpleGoldTooltip | [unregistered] |  |
| GetSkill | [unregistered] |  |
| GetSkillWithLevel | [unregistered] |  |
| GetSlowHistoryIdForDebug | [unregistered] |  |
| GetSpecialGuestRelationDescription | CString |  |
| GetStartCouncilTaskInTooltip | CString |  |
| GetStartRaidBlockers | CString |  |
| GetStress | int32 |  |
| GetStressLevel | int32 |  |
| GetStressProgress | float |  |
| GetSuccessionRelation | CString |  |
| GetTargetWeight | int32 |  |
| GetTheocraticLessee | [unregistered] |  |
| GetTheocraticLesseeApprovalTooltip | CString |  |
| GetTitleAsName | [unregistered] |  |
| GetTitleAsNameNicknamed | [unregistered] |  |
| GetTitleAsNameNicknamedNoTooltip | [unregistered] |  |
| GetTitleAsNameNicknamedNoTooltipRegnal | [unregistered] |  |
| GetTitleAsNameNicknamedOrMe | [unregistered] |  |
| GetTitleAsNameNicknamedOrMeNoTooltip | [unregistered] |  |
| GetTitleAsNameNicknamedOrMeNoTooltipRegnal | [unregistered] |  |
| GetTitleAsNameNicknamedOrMeRegnal | [unregistered] |  |
| GetTitleAsNameNicknamedPossessive | [unregistered] |  |
| GetTitleAsNameNicknamedPossessiveNoTooltip | [unregistered] |  |
| GetTitleAsNameNicknamedPossessiveNoTooltipRegnal | [unregistered] |  |
| GetTitleAsNameNicknamedPossessiveOrMy | [unregistered] |  |
| GetTitleAsNameNicknamedPossessiveOrMyNoTooltip | [unregistered] |  |
| GetTitleAsNameNicknamedPossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetTitleAsNameNicknamedPossessiveOrMyRegnal | [unregistered] |  |
| GetTitleAsNameNicknamedPossessiveRegnal | [unregistered] |  |
| GetTitleAsNameNicknamedRegnal | [unregistered] |  |
| GetTitleAsNameNoTooltip | [unregistered] |  |
| GetTitleAsNameNoTooltipRegnal | [unregistered] |  |
| GetTitleAsNameOrMe | [unregistered] |  |
| GetTitleAsNameOrMeNoTooltip | [unregistered] |  |
| GetTitleAsNameOrMeNoTooltipRegnal | [unregistered] |  |
| GetTitleAsNameOrMeRegnal | [unregistered] |  |
| GetTitleAsNamePossessive | [unregistered] |  |
| GetTitleAsNamePossessiveNoTooltip | [unregistered] |  |
| GetTitleAsNamePossessiveNoTooltipRegnal | [unregistered] |  |
| GetTitleAsNamePossessiveOrMy | [unregistered] |  |
| GetTitleAsNamePossessiveOrMyNoTooltip | [unregistered] |  |
| GetTitleAsNamePossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetTitleAsNamePossessiveOrMyRegnal | [unregistered] |  |
| GetTitleAsNamePossessiveRegnal | [unregistered] |  |
| GetTitleAsNameRegnal | [unregistered] |  |
| GetTitleTierName | CString |  |
| GetTitleTierNamePossessive | CString |  |
| GetTitledFirstName | [unregistered] |  |
| GetTitledFirstNameNicknamed | [unregistered] |  |
| GetTitledFirstNameNicknamedNoTooltip | [unregistered] |  |
| GetTitledFirstNameNicknamedNoTooltipRegnal | [unregistered] |  |
| GetTitledFirstNameNicknamedOrMe | [unregistered] |  |
| GetTitledFirstNameNicknamedOrMeNoTooltip | [unregistered] |  |
| GetTitledFirstNameNicknamedOrMeNoTooltipRegnal | [unregistered] |  |
| GetTitledFirstNameNicknamedOrMeRegnal | [unregistered] |  |
| GetTitledFirstNameNicknamedPossessive | [unregistered] |  |
| GetTitledFirstNameNicknamedPossessiveNoTooltip | [unregistered] |  |
| GetTitledFirstNameNicknamedPossessiveNoTooltipRegnal | [unregistered] |  |
| GetTitledFirstNameNicknamedPossessiveOrMy | [unregistered] |  |
| GetTitledFirstNameNicknamedPossessiveOrMyNoTooltip | [unregistered] |  |
| GetTitledFirstNameNicknamedPossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetTitledFirstNameNicknamedPossessiveOrMyRegnal | [unregistered] |  |
| GetTitledFirstNameNicknamedPossessiveRegnal | [unregistered] |  |
| GetTitledFirstNameNicknamedRegnal | [unregistered] |  |
| GetTitledFirstNameNoTooltip | [unregistered] |  |
| GetTitledFirstNameNoTooltipRegnal | [unregistered] |  |
| GetTitledFirstNameOrMe | [unregistered] |  |
| GetTitledFirstNameOrMeNoTooltip | [unregistered] |  |
| GetTitledFirstNameOrMeNoTooltipRegnal | [unregistered] |  |
| GetTitledFirstNameOrMeRegnal | [unregistered] |  |
| GetTitledFirstNamePossessive | [unregistered] |  |
| GetTitledFirstNamePossessiveNoTooltip | [unregistered] |  |
| GetTitledFirstNamePossessiveNoTooltipRegnal | [unregistered] |  |
| GetTitledFirstNamePossessiveOrMy | [unregistered] |  |
| GetTitledFirstNamePossessiveOrMyNoTooltip | [unregistered] |  |
| GetTitledFirstNamePossessiveOrMyNoTooltipRegnal | [unregistered] |  |
| GetTitledFirstNamePossessiveOrMyRegnal | [unregistered] |  |
| GetTitledFirstNamePossessiveRegnal | [unregistered] |  |
| GetTitledFirstNameRegnal | [unregistered] |  |
| GetTopLiege | [unregistered] |  |
| GetTotalPerkPoints | int32 |  |
| GetTraitIndices | [unregistered] |  |
| GetUIName | [unregistered] |  |
| GetUINameNoFormat | [unregistered] |  |
| GetUINameNoTooltip | [unregistered] |  |
| GetUINameNoTooltipNoFormat | [unregistered] |  |
| GetUINameNotMe | [unregistered] |  |
| GetUINameNotMeNoFormat | [unregistered] |  |
| GetUINameNotMeNoTooltip | [unregistered] |  |
| GetUINameNotMeNoTooltipNoFormat | [unregistered] |  |
| GetUINamePossessive | [unregistered] |  |
| GetUINamePossessiveNoFormat | [unregistered] |  |
| GetUINamePossessiveNoTooltip | [unregistered] |  |
| GetUINamePossessiveNoTooltipNoFormat | [unregistered] |  |
| GetUINamePossessiveNotMy | [unregistered] |  |
| GetUINamePossessiveNotMyNoFormat | [unregistered] |  |
| GetUINamePossessiveNotMyNoTooltip | [unregistered] |  |
| GetUINamePossessiveNotMyNoTooltipNoFormat | [unregistered] |  |
| GetUnlandedTitle | [unregistered] |  |
| GetUnlandedTitleSkipPlayer | [unregistered] |  |
| GetUnraisedKnightBreakdown | [unregistered] |  |
| GetUnraisedKnightCount | [unregistered] |  |
| GetVariablesDescription | [unregistered] |  |
| GetVassalContract | [unregistered] |  |
| GetVassalInfoText | CString |  |
| GetVassalLimit | int32 |  |
| GetVassalLimitBreakdown | CString |  |
| GetVassalLimitOverrun | int32 |  |
| GetVassalLimitTooltip | CString |  |
| GetWarsInfo | [unregistered] |  |
| GetWifeHusband | [unregistered] |  |
| GetWomanMan | [unregistered] |  |
| GetWomenMen | [unregistered] |  |
| HasAtMostOneSpouse | [unregistered] |  |
| HasClaimOnTitle | [unregistered] |  |
| HasCouncillorWithTaskIn | [unregistered] |  |
| HasDifficultyInfo | [unregistered] |  |
| HasDynasty | bool |  |
| HasKillsKnownTo | bool |  |
| HasLandedTitles | bool |  |
| HasLiege | [unregistered] |  |
| HasLocation | bool |  |
| HasMultipleSpouses | [unregistered] |  |
| HasNormalCouncilPosition | bool |  |
| HasPerk | bool |  |
| HasPressedClaimOnTitle | [unregistered] |  |
| HasRaisedRegiments | [unregistered] |  |
| HasRealmLaw | [unregistered] |  |
| HasRegnalName | bool |  |
| HasRelationTo | bool |  |
| HasSealCoA | bool |  |
| HasSexuality | bool |  |
| HasSpecialCouncilPosition | bool |  |
| HasUnpressedClaimOnTitle | [unregistered] |  |
| HasVassalInfo | bool |  |
| HookTooltip | [unregistered] |  |
| IsAdult | bool |  |
| IsAlive | bool |  |
| IsAtWar | bool |  |
| IsBastard | bool |  |
| IsBetrothed | bool |  |
| IsConcubine | bool |  |
| IsCouncilTaskValid | bool |  |
| IsCouncillor | bool |  |
| IsDead | [unregistered] |  |
| IsDeadAndValid | [unregistered] |  |
| IsDynast | bool |  |
| IsDynastyHead | bool |  |
| IsFemale | bool |  |
| IsFounderOfDynasty | bool |  |
| IsGuest | bool |  |
| IsHouseHead | bool |  |
| IsHovered | bool |  |
| IsImprisoned | bool |  |
| IsIncapable | bool |  |
| IsIndependentRuler | bool |  |
| IsKnight | bool |  |
| IsKnightDefault | [unregistered] |  |
| IsKnightDisallowed | [unregistered] |  |
| IsKnightForced | [unregistered] |  |
| IsKnightInArmy | bool |  |
| IsKnightInSpecificArmy | bool |  |
| IsLegitimateMemberOfHouse | bool |  |
| IsLegitimizedBastard | bool |  |
| IsLocalPlayer | [unregistered] |  |
| IsMyPowerfulVassal | [unregistered] |  |
| IsOpposing | bool |  |
| IsOtherLiegeOrAbove | bool |  |
| IsOtherPlayer | [unregistered] |  |
| IsPinned | [unregistered] |  |
| IsPlayer | [unregistered] |  |
| IsPlayerInteractionShown | [unregistered] |  |
| IsPlayerInteractionShownAndCanPickTitle | [unregistered] |  |
| IsPlayerInteractionValid | [unregistered] |  |
| IsPlayerInteractionWithTargetCharacterValid | bool |  |
| IsPlayerInteractionWithTargetSecretValid | bool |  |
| IsPlayerInteractionWithTargetTitleValid | [unregistered] |  |
| IsPowerfulVassal | bool |  |
| IsReligiousHead | [unregistered] |  |
| IsRuler | bool |  |
| IsSelected | bool |  |
| IsShownInCharacterWindow | [unregistered] |  |
| IsTheocraticLessee | bool |  |
| IsTheocraticLesseeOf | bool |  |
| IsValid | bool |  |
| IsVisiblyInfertile | bool |  |
| LocalPlayerString | CString |  |
| MakeScope | Scope |  |
| NumberOfDirectlyHeldCounties | int32 |  |
| OnCustomizePortrait | void |  |
| OnMouseEnter | void |  |
| OnMouseLeave | void |  |
| OpenPlayerInteraction | [unregistered] |  |
| OpenPlayerInteractionWithTargetCharacter | void |  |
| OpenPlayerInteractionWithTargetSecret | void |  |
| OpenPlayerInteractionWithTargetTitle | [unregistered] |  |
| PlayerCanManageFocus | bool |  |
| PlayerHasHooksOrHookableSecrets | [unregistered] |  |
| PlayerName | [unregistered] |  |
| PunishmentTooltip | CString |  |
| RealmSize | int32 |  |
| Self | [unregistered] |  |
| ShouldShowDreadEffectIcon | [unregistered] |  |
| ShouldShowDreadEffectIconFor | bool |  |
| StartCouncilTaskIn | [unregistered] |  |
| StressLevelEffect | [unregistered] |  |
| StressProgressDesc | [unregistered] |  |
| TheocraticLesseeApprovesOfLiege | bool |  |
| TheocraticLesseeHasApprovalStatus | bool |  |
| ToggleCharacterPinned | [unregistered] |  |

### Combat

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetAttacker | CombatSide |  |
| GetDefender | CombatSide |  |
| GetLeftSide | CombatSide |  |
| GetLeftSideResult | CombatSideResultData |  |
| GetProvince | Province |  |
| GetRightSide | CombatSide |  |
| GetRightSideResult | CombatSideResultData |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| Custom | CString |  |
| GetAdvantageSlider | float |  |
| GetCombatWidth | CFixedPoint |  |
| GetCombatWidthBreakdown | CString |  |
| GetCurrentBalance | [unregistered] |  |
| GetName | CString |  |
| GetPhaseDesc | CString |  |
| GetPhaseTooltip | CString |  |
| GetPowerSlider | float |  |
| IsInPursuitPhase | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### CombatSide

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetComposition | ArmyComposition |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| GetComposition | [unregistered] |  |
| GetCurrentFightingMen | CFixedPoint |  |
| GetHardCasualties | CFixedPoint |  |
| GetPursuingRetreatingLabel | CString |  |
| GetPursuitPhaseMen | CFixedPoint |  |
| GetSoftCasualties | CFixedPoint |  |
| IsAttacker | bool |  |
| IsStillFighting | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### County

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetCapital | Province |  |
| GetCount | Character |  |
| GetCountyOccupant | Character |  |
| GetCulture | Culture |  |
| GetFaith | Faith |  |
| GetTitle | Title |  |
| AccessSelf | [unregistered] |  |
| GetCapital | [unregistered] |  |
| GetControl | CFixedPoint |  |
| GetControlLevel | CString |  |
| GetControlLevelOutOfMax | CString |  |
| GetCount | [unregistered] |  |
| GetCountyControlEffectsDesc | CString |  |
| GetCountyControlIncreaseDesc | CString |  |
| GetCountyDevelopmentEffectsDesc | CString |  |
| GetCountyDevelopmentIncreaseDesc | CString |  |
| GetCountyOccupant | [unregistered] |  |
| GetCulture | [unregistered] |  |
| GetDevelopmentIgnoredDesc | CString |  |
| GetDevelopmentLevel | int32 |  |
| GetDevelopmentLevelString | CString |  |
| GetFaith | [unregistered] |  |
| GetName | CString |  |
| GetTitle | [unregistered] |  |
| IsFullyOccupied | bool |  |
| Self | [unregistered] |  |

### Culture

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetCultureEra | CultureEra |  |
| GetCultureHead | Character |  |
| GetFascination | CultureInnovation |  |
| GetFascinationType | CultureInnovationType |  |
| GetGroup | CultureGroup |  |
| GetTemplate | CultureTemplate |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| GetCollectiveNoun | CString |  |
| GetCollectiveNounNoTooltip | CString |  |
| GetCultureEra | [unregistered] |  |
| GetCultureHead | [unregistered] |  |
| GetFascination | [unregistered] |  |
| GetFascinationType | [unregistered] |  |
| GetGroup | [unregistered] |  |
| GetID | uint32 |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetRelationToPlayer | [unregistered] |  |
| GetTemplate | [unregistered] |  |
| HasAvailableInnovation | bool |  |
| HasCultureHead | bool |  |
| HasFascination | bool |  |
| IsPlayerCulture | [unregistered] |  |
| IsPlayerCultureGroup | [unregistered] |  |
| IsPlayerCultureHead | [unregistered] |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### CultureGroup

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| GetCultures | [unregistered] |  |
| GetName | CString |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### Dynasty

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetDynast | Character |  |
| GetDynastyCoA | CoatOfArms |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| CanUnlockRelevantPerk | bool |  |
| GetAliveMembers | [unregistered] |  |
| GetBaseName | CString |  |
| GetBaseNameNoTooltip | CString |  |
| GetDeadMembers | [unregistered] |  |
| GetDynast | [unregistered] |  |
| GetDynastyHouses | [unregistered] |  |
| GetDynastyPrestigeLevelTexture | [unregistered] |  |
| GetFoundedDynastyHousesCount | int32 |  |
| GetID | uint32 |  |
| GetMembers | [unregistered] |  |
| GetMembersText | CString |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetNextPrestigeLevelName | [unregistered] |  |
| GetNumberOfLivingMembers | int32 |  |
| GetNumberOfMembers | int32 |  |
| GetPrestige | CFixedPoint |  |
| GetPrestigeBreakdown | [unregistered] |  |
| GetPrestigeFrame | [unregistered] |  |
| GetPrestigeIncome | CFixedPoint |  |
| GetPrestigeLevel | int32 |  |
| GetPrestigeLevelEffect | [unregistered] |  |
| GetPrestigeLevelName | [unregistered] |  |
| GetPrestigeLevelProgress | [unregistered] |  |
| GetPrestigeLevelProgressTooltip | [unregistered] |  |
| GetPrestigeNextLevelText | [unregistered] |  |
| GetPrestigeProgress | CString |  |
| GetRequiredPowerToReplaceDynast | CFixedPoint |  |
| HasDynast | bool |  |
| HasPerk | bool |  |
| IsMyDynasty | bool |  |
| IsValid | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### DynastyHouse

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetDynasty | Dynasty |  |
| GetFounder | Character |  |
| GetHeadOfHouse | Character |  |
| GetHeirOfHouse | Character |  |
| GetHouseCoA | CoatOfArms |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| GetAliveMembers | [unregistered] |  |
| GetBaseName | CString |  |
| GetBaseNameNoTooltip | CString |  |
| GetDeadMembers | [unregistered] |  |
| GetFoundYear | int32 |  |
| GetID | uint32 |  |
| GetMembers | [unregistered] |  |
| GetMembersText | CString |  |
| GetMotto | CString |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetNumberOfMembers | int32 |  |
| HasBeenFounded | bool |  |
| HasHeadOfHouse | bool |  |
| HasHeirOfHouse | bool |  |
| IsFoundingHouse | bool |  |
| IsPlayerMember | [unregistered] |  |
| IsValid | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### Faction

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetLeader | Character |  |
| GetSpecialCharacter | Character |  |
| GetSpecialTitle | Title |  |
| GetTarget | Character |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| GetDescription | CString |  |
| GetDiscontent | float |  |
| GetIcon | [unregistered] |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetPower | float |  |
| GetShortEffectDescription | CString |  |
| GetShowSpecialTitle | bool |  |
| GetSpecialCharacterTitle | CString |  |
| HasSpecialCharacter | bool |  |
| HasSpecialTitle | bool |  |
| IsAtWar | bool |  |
| IsDangerous | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### Faith

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetFounder | Character |  |
| GetGreatHolyWar | GreatHolyWar |  |
| GetReligion | Religion |  |
| GetReligiousHead | Character |  |
| GetReligiousHeadTitle | Title |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| AltPriestTermPlural | [unregistered] |  |
| BishopFemale | [unregistered] |  |
| BishopFemalePlural | [unregistered] |  |
| BishopMale | [unregistered] |  |
| BishopMalePlural | [unregistered] |  |
| BishopNeuter | [unregistered] |  |
| BishopNeuterPlural | [unregistered] |  |
| CreatorHerHim | [unregistered] |  |
| CreatorHerHis | [unregistered] |  |
| CreatorName | [unregistered] |  |
| CreatorNameAlternate | [unregistered] |  |
| CreatorNameAlternatePossessive | [unregistered] |  |
| CreatorNamePossessive | [unregistered] |  |
| CreatorSheHe | [unregistered] |  |
| Custom | CString |  |
| DeathDeityHerHis | [unregistered] |  |
| DeathDeityName | [unregistered] |  |
| DeathDeityNamePossessive | [unregistered] |  |
| DeathDeitySheHe | [unregistered] |  |
| DevilHerHim | [unregistered] |  |
| DevilHerHis | [unregistered] |  |
| DevilHerselfHimself | [unregistered] |  |
| DevilName | [unregistered] |  |
| DevilNamePossessive | [unregistered] |  |
| DevilSheHe | [unregistered] |  |
| DevoteeFemale | [unregistered] |  |
| DevoteeFemalePlural | [unregistered] |  |
| DevoteeMale | [unregistered] |  |
| DevoteeMalePlural | [unregistered] |  |
| DevoteeNeuter | [unregistered] |  |
| DevoteeNeuterPlural | [unregistered] |  |
| DivineRealm | [unregistered] |  |
| EvilGodNames | [unregistered] |  |
| FateGodHerHim | [unregistered] |  |
| FateGodHerHis | [unregistered] |  |
| FateGodName | [unregistered] |  |
| FateGodNameAlternate | [unregistered] |  |
| FateGodNameAlternatePossessive | [unregistered] |  |
| FateGodNamePossessive | [unregistered] |  |
| FateGodSheHe | [unregistered] |  |
| FertilityGodHerHim | [unregistered] |  |
| FertilityGodHerHis | [unregistered] |  |
| FertilityGodName | [unregistered] |  |
| FertilityGodNameAlternate | [unregistered] |  |
| FertilityGodNameAlternatePossessive | [unregistered] |  |
| FertilityGodNamePossessive | [unregistered] |  |
| FertilityGodSheHe | [unregistered] |  |
| GHWName | [unregistered] |  |
| GHWNamePlural | [unregistered] |  |
| GetAdherentName | CString |  |
| GetAdherentNameNoTooltip | CString |  |
| GetAdherentNamePlural | CString |  |
| GetAdherentNamePluralNoTooltip | CString |  |
| GetAdjective | CString |  |
| GetAdjectiveNoTooltip | CString |  |
| GetDefensiveGreatHolyWars | [unregistered] |  |
| GetDesc | CString |  |
| GetDoctrineBackgroundIcon | [unregistered] |  |
| GetDoctrines | [unregistered] |  |
| GetFervor | CFixedPoint |  |
| GetFlavorDesc | CString |  |
| GetFounder | [unregistered] |  |
| GetGreatHolyWar | [unregistered] |  |
| GetHostilityLevelTowards | int32 |  |
| GetID | uint32 |  |
| GetIcon | [unregistered] |  |
| GetLabelFaithReligion | CString |  |
| GetMonthlyFervorChange | CFixedPoint |  |
| GetMonthlyFervorChangeDesc | CString |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetNumberOfCountiesOfFaith | int32 |  |
| GetRelationNameTo | CString |  |
| GetReligion | [unregistered] |  |
| GetReligiousHead | [unregistered] |  |
| GetReligiousHeadTitle | [unregistered] |  |
| GetTextIcon | CString |  |
| GoodGodNames | [unregistered] |  |
| HasDoctrine | bool |  |
| HasDoctrineByKey | bool |  |
| HasOffensiveGreatHolyWar | bool |  |
| HasReservedNames | bool |  |
| HealthGodHerHim | [unregistered] |  |
| HealthGodHerHis | [unregistered] |  |
| HealthGodName | [unregistered] |  |
| HealthGodNameAlternate | [unregistered] |  |
| HealthGodNameAlternatePossessive | [unregistered] |  |
| HealthGodNamePossessive | [unregistered] |  |
| HealthGodSheHe | [unregistered] |  |
| HighGodHerHis | [unregistered] |  |
| HighGodHerselfHimself | [unregistered] |  |
| HighGodName | [unregistered] |  |
| HighGodNameAlternate | [unregistered] |  |
| HighGodNameAlternatePossessive | [unregistered] |  |
| HighGodNamePossessive | [unregistered] |  |
| HighGodNameSheHe | [unregistered] |  |
| HouseOfWorship | [unregistered] |  |
| HouseOfWorshipPlural | [unregistered] |  |
| HouseholdGodHerHim | [unregistered] |  |
| HouseholdGodHerHis | [unregistered] |  |
| HouseholdGodName | [unregistered] |  |
| HouseholdGodNameAlternate | [unregistered] |  |
| HouseholdGodNameAlternatePossessive | [unregistered] |  |
| HouseholdGodNamePossessive | [unregistered] |  |
| HouseholdGodSheHe | [unregistered] |  |
| IsSelected | bool |  |
| IsTraitSin | bool |  |
| IsTraitVirtue | bool |  |
| IsUnreformed | bool |  |
| IsValid | bool |  |
| KnowledgeGodHerHim | [unregistered] |  |
| KnowledgeGodHerHis | [unregistered] |  |
| KnowledgeGodName | [unregistered] |  |
| KnowledgeGodNamePossessive | [unregistered] |  |
| KnowledgeGodSheHe | [unregistered] |  |
| MakeScope | Scope |  |
| NegativeAfterLife | [unregistered] |  |
| NightGodHerHim | [unregistered] |  |
| NightGodHerHis | [unregistered] |  |
| NightGodName | [unregistered] |  |
| NightGodNameAlternate | [unregistered] |  |
| NightGodNameAlternatePossessive | [unregistered] |  |
| NightGodNamePossessive | [unregistered] |  |
| NightGodSheHe | [unregistered] |  |
| PantheonTerm | [unregistered] |  |
| PantheonTermHasHave | [unregistered] |  |
| PositiveAfterLife | [unregistered] |  |
| PriestFemale | [unregistered] |  |
| PriestFemalePlural | [unregistered] |  |
| PriestMale | [unregistered] |  |
| PriestMalePlural | [unregistered] |  |
| PriestNeuter | [unregistered] |  |
| PriestNeuterPlural | [unregistered] |  |
| RandomCustom | CString |  |
| ReligiousHeadName | [unregistered] |  |
| ReligiousHeadTitleName | [unregistered] |  |
| ReligiousSymbol | [unregistered] |  |
| ReligiousText | [unregistered] |  |
| Self | [unregistered] |  |
| TricksterGodHerHim | [unregistered] |  |
| TricksterGodHerHis | [unregistered] |  |
| TricksterGodName | [unregistered] |  |
| TricksterGodNamePossessive | [unregistered] |  |
| TricksterGodSheHe | [unregistered] |  |
| WarGodHerHim | [unregistered] |  |
| WarGodHerHis | [unregistered] |  |
| WarGodName | [unregistered] |  |
| WarGodNameAlternate | [unregistered] |  |
| WarGodNameAlternatePossessive | [unregistered] |  |
| WarGodNamePossessive | [unregistered] |  |
| WarGodSheHe | [unregistered] |  |
| WaterGodHerHim | [unregistered] |  |
| WaterGodHerHis | [unregistered] |  |
| WaterGodName | [unregistered] |  |
| WaterGodNameAlternate | [unregistered] |  |
| WaterGodNameAlternatePossessive | [unregistered] |  |
| WaterGodNamePossessive | [unregistered] |  |
| WaterGodSheHe | [unregistered] |  |
| WealthGodHerHim | [unregistered] |  |
| WealthGodHerHis | [unregistered] |  |
| WealthGodName | [unregistered] |  |
| WealthGodNameAlternate | [unregistered] |  |
| WealthGodNameAlternatePossessive | [unregistered] |  |
| WealthGodNamePossessive | [unregistered] |  |
| WealthGodSheHe | [unregistered] |  |
| WitchGodHerHim | [unregistered] |  |
| WitchGodHerHis | [unregistered] |  |
| WitchGodMistressMaster | [unregistered] |  |
| WitchGodMotherFather | [unregistered] |  |
| WitchGodName | [unregistered] |  |
| WitchGodSheHe | [unregistered] |  |
| random_AltPriestTermPlural | [unregistered] |  |
| random_BishopFemale | [unregistered] |  |
| random_BishopFemalePlural | [unregistered] |  |
| random_BishopMale | [unregistered] |  |
| random_BishopMalePlural | [unregistered] |  |
| random_BishopNeuter | [unregistered] |  |
| random_BishopNeuterPlural | [unregistered] |  |
| random_CreatorHerHim | [unregistered] |  |
| random_CreatorHerHis | [unregistered] |  |
| random_CreatorName | [unregistered] |  |
| random_CreatorNameAlternate | [unregistered] |  |
| random_CreatorNameAlternatePossessive | [unregistered] |  |
| random_CreatorNamePossessive | [unregistered] |  |
| random_CreatorSheHe | [unregistered] |  |
| random_DeathDeityHerHis | [unregistered] |  |
| random_DeathDeityName | [unregistered] |  |
| random_DeathDeityNamePossessive | [unregistered] |  |
| random_DeathDeitySheHe | [unregistered] |  |
| random_DevilHerHim | [unregistered] |  |
| random_DevilHerHis | [unregistered] |  |
| random_DevilHerselfHimself | [unregistered] |  |
| random_DevilName | [unregistered] |  |
| random_DevilNamePossessive | [unregistered] |  |
| random_DevilSheHe | [unregistered] |  |
| random_DevoteeFemale | [unregistered] |  |
| random_DevoteeFemalePlural | [unregistered] |  |
| random_DevoteeMale | [unregistered] |  |
| random_DevoteeMalePlural | [unregistered] |  |
| random_DevoteeNeuter | [unregistered] |  |
| random_DevoteeNeuterPlural | [unregistered] |  |
| random_DivineRealm | [unregistered] |  |
| random_EvilGodNames | [unregistered] |  |
| random_FateGodHerHim | [unregistered] |  |
| random_FateGodHerHis | [unregistered] |  |
| random_FateGodName | [unregistered] |  |
| random_FateGodNameAlternate | [unregistered] |  |
| random_FateGodNameAlternatePossessive | [unregistered] |  |
| random_FateGodNamePossessive | [unregistered] |  |
| random_FateGodSheHe | [unregistered] |  |
| random_FertilityGodHerHim | [unregistered] |  |
| random_FertilityGodHerHis | [unregistered] |  |
| random_FertilityGodName | [unregistered] |  |
| random_FertilityGodNameAlternate | [unregistered] |  |
| random_FertilityGodNameAlternatePossessive | [unregistered] |  |
| random_FertilityGodNamePossessive | [unregistered] |  |
| random_FertilityGodSheHe | [unregistered] |  |
| random_GHWName | [unregistered] |  |
| random_GHWNamePlural | [unregistered] |  |
| random_GoodGodNames | [unregistered] |  |
| random_HealthGodHerHim | [unregistered] |  |
| random_HealthGodHerHis | [unregistered] |  |
| random_HealthGodName | [unregistered] |  |
| random_HealthGodNameAlternate | [unregistered] |  |
| random_HealthGodNameAlternatePossessive | [unregistered] |  |
| random_HealthGodNamePossessive | [unregistered] |  |
| random_HealthGodSheHe | [unregistered] |  |
| random_HighGodHerHis | [unregistered] |  |
| random_HighGodHerselfHimself | [unregistered] |  |
| random_HighGodName | [unregistered] |  |
| random_HighGodNameAlternate | [unregistered] |  |
| random_HighGodNameAlternatePossessive | [unregistered] |  |
| random_HighGodNamePossessive | [unregistered] |  |
| random_HighGodNameSheHe | [unregistered] |  |
| random_HouseOfWorship | [unregistered] |  |
| random_HouseOfWorshipPlural | [unregistered] |  |
| random_HouseholdGodHerHim | [unregistered] |  |
| random_HouseholdGodHerHis | [unregistered] |  |
| random_HouseholdGodName | [unregistered] |  |
| random_HouseholdGodNameAlternate | [unregistered] |  |
| random_HouseholdGodNameAlternatePossessive | [unregistered] |  |
| random_HouseholdGodNamePossessive | [unregistered] |  |
| random_HouseholdGodSheHe | [unregistered] |  |
| random_KnowledgeGodHerHim | [unregistered] |  |
| random_KnowledgeGodHerHis | [unregistered] |  |
| random_KnowledgeGodName | [unregistered] |  |
| random_KnowledgeGodNamePossessive | [unregistered] |  |
| random_KnowledgeGodSheHe | [unregistered] |  |
| random_NegativeAfterLife | [unregistered] |  |
| random_NightGodHerHim | [unregistered] |  |
| random_NightGodHerHis | [unregistered] |  |
| random_NightGodName | [unregistered] |  |
| random_NightGodNameAlternate | [unregistered] |  |
| random_NightGodNameAlternatePossessive | [unregistered] |  |
| random_NightGodNamePossessive | [unregistered] |  |
| random_NightGodSheHe | [unregistered] |  |
| random_PantheonTerm | [unregistered] |  |
| random_PantheonTermHasHave | [unregistered] |  |
| random_PositiveAfterLife | [unregistered] |  |
| random_PriestFemale | [unregistered] |  |
| random_PriestFemalePlural | [unregistered] |  |
| random_PriestMale | [unregistered] |  |
| random_PriestMalePlural | [unregistered] |  |
| random_PriestNeuter | [unregistered] |  |
| random_PriestNeuterPlural | [unregistered] |  |
| random_ReligiousHeadName | [unregistered] |  |
| random_ReligiousHeadTitleName | [unregistered] |  |
| random_ReligiousSymbol | [unregistered] |  |
| random_ReligiousText | [unregistered] |  |
| random_TricksterGodHerHim | [unregistered] |  |
| random_TricksterGodHerHis | [unregistered] |  |
| random_TricksterGodName | [unregistered] |  |
| random_TricksterGodNamePossessive | [unregistered] |  |
| random_TricksterGodSheHe | [unregistered] |  |
| random_WarGodHerHim | [unregistered] |  |
| random_WarGodHerHis | [unregistered] |  |
| random_WarGodName | [unregistered] |  |
| random_WarGodNameAlternate | [unregistered] |  |
| random_WarGodNameAlternatePossessive | [unregistered] |  |
| random_WarGodNamePossessive | [unregistered] |  |
| random_WarGodSheHe | [unregistered] |  |
| random_WaterGodHerHim | [unregistered] |  |
| random_WaterGodHerHis | [unregistered] |  |
| random_WaterGodName | [unregistered] |  |
| random_WaterGodNameAlternate | [unregistered] |  |
| random_WaterGodNameAlternatePossessive | [unregistered] |  |
| random_WaterGodNamePossessive | [unregistered] |  |
| random_WaterGodSheHe | [unregistered] |  |
| random_WealthGodHerHim | [unregistered] |  |
| random_WealthGodHerHis | [unregistered] |  |
| random_WealthGodName | [unregistered] |  |
| random_WealthGodNameAlternate | [unregistered] |  |
| random_WealthGodNameAlternatePossessive | [unregistered] |  |
| random_WealthGodNamePossessive | [unregistered] |  |
| random_WealthGodSheHe | [unregistered] |  |
| random_WitchGodHerHim | [unregistered] |  |
| random_WitchGodHerHis | [unregistered] |  |
| random_WitchGodMistressMaster | [unregistered] |  |
| random_WitchGodMotherFather | [unregistered] |  |
| random_WitchGodName | [unregistered] |  |
| random_WitchGodSheHe | [unregistered] |  |

### Holding

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetConstructingHoldingType | HoldingType |  |
| GetConstructionBuilding | Building |  |
| GetDuchyBuildingType | Building |  |
| GetHolder | Character |  |
| GetLesseeOrHolder | Character |  |
| GetPrimaryBuildingType | Building |  |
| GetProvince | Province |  |
| GetType | HoldingType |  |
| AccessSelf | [unregistered] |  |
| CanConstructAnyBuilding | bool |  |
| GetConstructingHoldingType | [unregistered] |  |
| GetConstructionProgress | [unregistered] |  |
| GetConstructionTimeLeft | [unregistered] |  |
| GetDuchyBuildingType | [unregistered] |  |
| GetGarrisonSize | int32 |  |
| GetHolder | [unregistered] |  |
| GetIllustration | [unregistered] |  |
| GetIncome | CFixedPoint |  |
| GetLesseeOrHolder | [unregistered] |  |
| GetLeviesTooltip | [unregistered] |  |
| GetMaxLevySize | int32 |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetPrimaryBuildingType | [unregistered] |  |
| GetProvince | [unregistered] |  |
| GetTaxTooltip | [unregistered] |  |
| GetTooltip | CString |  |
| GetType | [unregistered] |  |
| GetUnraisedLevyRatio | CFixedPoint |  |
| GetUnraisedLevyRatioPercent | float |  |
| HasDuchyBuildingSlot | bool |  |
| IsConstructionInProgress | bool |  |
| IsEmpty | bool |  |
| IsHovered | bool |  |
| IsLowControl | [unregistered] |  |
| IsSelected | bool |  |
| IsShowHoldingPins | [unregistered] |  |
| IsValidForLesseeOrHolder | bool |  |
| LevyAndTaxIsAffectedByFixableSituation | bool |  |
| OnMouseEnter | void |  |
| OnMouseLeave | void |  |
| Self | [unregistered] |  |

### Province

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetCoATitle | Title |  |
| GetController | Character |  |
| GetCounty | County |  |
| GetCountyCapitalProvince | Province |  |
| GetCountyOccupant | Character |  |
| GetEndOfRecentlyLooted | Date |  |
| GetHolding | Holding |  |
| GetRaid | Raid |  |
| GetSiege | Siege |  |
| GetTerrain | Terrain |  |
| GetTitle | Title |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| Custom | CString |  |
| GetCoATitle | [unregistered] |  |
| GetController | [unregistered] |  |
| GetCounty | [unregistered] |  |
| GetCountyCapitalProvince | [unregistered] |  |
| GetCountyOccupant | [unregistered] |  |
| GetFortLevel | int32 |  |
| GetFortLevelTooltip | CString |  |
| GetHolding | [unregistered] |  |
| GetId | int32 |  |
| GetLootTime | int32 |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetProvinceLoot | CFixedPoint |  |
| GetRaidLoot | CFixedPoint |  |
| GetRaidLootTooltip | CString |  |
| GetSiege | [unregistered] |  |
| GetSiegeStrength | int32 |  |
| GetSupplyLimitDescFor | CString |  |
| GetSupplyLimitFor | int32 |  |
| GetTag | CString |  |
| GetTerrain | [unregistered] |  |
| GetTitle | [unregistered] |  |
| HasActiveRaid | bool |  |
| HasActiveSiege | [unregistered] |  |
| HasCountyCapitalProvince | bool |  |
| HasFort | bool |  |
| HasSiege | bool |  |
| IsOccupied | bool |  |
| IsRealmCapital | [unregistered] |  |
| IsRecentlyLooted | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### Religion

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetFamily | ReligionFamily |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| Custom | CString |  |
| GetAdjective | CString |  |
| GetAdjectiveNoTooltip | CString |  |
| GetFaiths | [unregistered] |  |
| GetFlavorDesc | CString |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| HasPaganRoots | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |

### ReligionFamily

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| AccessSelf | [unregistered] |  |
| GetName | CString |  |
| GetNameNoTooltip | CString |  |
| GetReligions | CString |  |
| GetReligiousFamilyHostilityDescription | CString |  |
| IsPagan | bool |  |
| Self | [unregistered] |  |

### Scope

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| Activity | Activity |  |
| Army | Army |  |
| CasusBelli | ActiveCasusBelli |  |
| Char | Character |  |
| Combat | Combat |  |
| CombatSide | CombatSide |  |
| CouncilTask | ActiveCouncilTask |  |
| Culture | Culture |  |
| CultureGroup | CultureGroup |  |
| Dynasty | Dynasty |  |
| Faction | Faction |  |
| Faith | Faith |  |
| GetActivity | Activity |  |
| GetCharacter | Character |  |
| GetLandedTitle | Title |  |
| GetProvince | Province |  |
| GetScheme | Scheme |  |
| GetVariable | Scope |  |
| GreatHolyWar | GreatHolyWar |  |
| HolyOrder | HolyOrder |  |
| House | DynastyHouse |  |
| MercenaryCompany | MercenaryCompany |  |
| Province | Province |  |
| Religion | Religion |  |
| Scheme | Scheme |  |
| Secret | Secret |  |
| Story | Story |  |
| Title | Title |  |
| Var | Scope |  |
| War | War |  |
| AccessSelf | [unregistered] |  |
| Activity | [unregistered] |  |
| Army | [unregistered] |  |
| CasusBelli | [unregistered] |  |
| Char | [unregistered] |  |
| Combat | [unregistered] |  |
| CombatSide | [unregistered] |  |
| CouncilTask | [unregistered] |  |
| Culture | [unregistered] |  |
| CultureGroup | [unregistered] |  |
| Dynasty | [unregistered] |  |
| Faction | [unregistered] |  |
| Faith | [unregistered] |  |
| GetActivity | [unregistered] |  |
| GetCharacter | [unregistered] |  |
| GetFlagName | CString |  |
| GetLandedTitle | [unregistered] |  |
| GetList | [unregistered] |  |
| GetProvince | [unregistered] |  |
| GetScheme | [unregistered] |  |
| GetValue | CFixedPoint |  |
| GetValueWithDefault | CFixedPoint |  |
| GreatHolyWar | [unregistered] |  |
| HolyOrder | [unregistered] |  |
| House | [unregistered] |  |
| IsSet | bool |  |
| MercenaryCompany | [unregistered] |  |
| Province | [unregistered] |  |
| Religion | [unregistered] |  |
| Scheme | [unregistered] |  |
| Secret | [unregistered] |  |
| Self | [unregistered] |  |
| Story | [unregistered] |  |
| Title | [unregistered] |  |
| VarRemaining | int32 |  |
| War | [unregistered] |  |

### ScriptedGui

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| AccessSelf | [unregistered] |  |
| BuildTooltip | CString |  |
| Execute | void |  |
| ExecuteTooltip | CString |  |
| IsShown | bool |  |
| IsShownTooltip | CString |  |
| IsValid | bool |  |
| IsValidTooltip | CString |  |
| Self | [unregistered] |  |

### Title

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetCountyData | County |  |
| GetDeFactoLiege | Title |  |
| GetDeFactoTopLiege | Title |  |
| GetDeJureLiege | Title |  |
| GetFaction | Faction |  |
| GetHeir | Character |  |
| GetHolder | Character |  |
| GetHolderOrCountyHolder | Character |  |
| GetHolyOrder | HolyOrder |  |
| GetLessee | Character |  |
| GetLesseeOrHolder | Character |  |
| GetMercenaryCompany | MercenaryCompany |  |
| GetPlayerNominee | Character |  |
| GetPreferredCapital | Title |  |
| GetProvince | Province |  |
| GetTitleCoA | CoatOfArms |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| CanCharacterControlVote | [unregistered] |  |
| CanHaveClaim | bool |  |
| CanPlayerRenameTitle | bool |  |
| CanUseFindVassal | bool |  |
| CreateHolderForBarony | void |  |
| Custom | CString |  |
| GetAdjective | CString |  |
| GetAdjectiveNoTooltip | CString |  |
| GetBaseName | [unregistered] |  |
| GetBaseNameNoTier | [unregistered] |  |
| GetBaseNameNoTierNoTooltip | [unregistered] |  |
| GetBaseNameNoTierPossessive | [unregistered] |  |
| GetBaseNameNoTierPossessiveNoTooltip | [unregistered] |  |
| GetBaseNameNoTooltip | [unregistered] |  |
| GetBaseNamePossessive | [unregistered] |  |
| GetBaseNamePossessiveNoTooltip | [unregistered] |  |
| GetCOADeJureTooltip | [unregistered] |  |
| GetCOADefaultTooltip | [unregistered] |  |
| GetCanCharacterControlVoteReason | [unregistered] |  |
| GetClaimStateFor | CString |  |
| GetClickInfo | [unregistered] |  |
| GetCoatOfArms | [unregistered] |  |
| GetDeJureDriftTooltip | CString |  |
| GetFaction | [unregistered] |  |
| GetHolder | [unregistered] |  |
| GetID | uint32 |  |
| GetKey | CString |  |
| GetLaws | [unregistered] |  |
| GetLeaseInfo | CString |  |
| GetLeasedOutVassalList | CString |  |
| GetLineOfSuccession | [unregistered] |  |
| GetLineOfSuccessionDesc | CString |  |
| GetMercenaryCompany | [unregistered] |  |
| GetName | [unregistered] |  |
| GetNameNoTier | [unregistered] |  |
| GetNameNoTierNoTooltip | [unregistered] |  |
| GetNameNoTierPossessive | [unregistered] |  |
| GetNameNoTierPossessiveNoTooltip | [unregistered] |  |
| GetNameNoTooltip | [unregistered] |  |
| GetNamePossessive | [unregistered] |  |
| GetNamePossessiveNoTooltip | [unregistered] |  |
| GetNameWithUnderlying | [unregistered] |  |
| GetNameWithUnderlyingNoTooltip | [unregistered] |  |
| GetNameWithUnderlyingPossessive | [unregistered] |  |
| GetNameWithUnderlyingPossessiveNoTooltip | [unregistered] |  |
| GetPrefix | CString |  |
| GetPrefixNoTooltip | CString |  |
| GetRankConcept | CString |  |
| GetRealmLabel | [unregistered] |  |
| GetSpecialDescription | CString |  |
| GetTierAsName | [unregistered] |  |
| GetTierAsNameNoTooltip | [unregistered] |  |
| GetTierAsNamePossessive | [unregistered] |  |
| GetTierAsNamePossessiveNoTooltip | [unregistered] |  |
| GetTierFrame | int32 |  |
| HasFaction | bool |  |
| HasHolder | bool |  |
| HasLaws | bool |  |
| HasLeasedOutVassal | bool |  |
| HasSuccessionOrder | [unregistered] |  |
| HoldingCanBeHeldBy | bool |  |
| IsBarony | bool |  |
| IsCountyCapital | bool |  |
| IsHeldBy | bool |  |
| IsHolyOrder | bool |  |
| IsHovered | bool |  |
| IsLanded | bool |  |
| IsLeasedOut | bool |  |
| IsMercenaryCompany | bool |  |
| IsPlayerElector | [unregistered] |  |
| IsPrimary | bool |  |
| IsSelected | bool |  |
| IsShownInTitleView | [unregistered] |  |
| IsUnderTheocraticLease | bool |  |
| IsValid | bool |  |
| MakeScope | Scope |  |
| OnMouseEnter | void |  |
| OnMouseLeave | void |  |
| OnPlayerNominatesSuccessor | [unregistered] |  |
| SelectTitle | [unregistered] |  |
| Self | [unregistered] |  |

### TopScope

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| AddScope | TopScope |  |
| GetDecisionFromEventTargetFlag | Decision |  |
| GetRootScope | Scope |  |
| SetRoot | TopScope |  |
| event_target:actor | Character |  |
| event_target:agent | Character |  |
| event_target:duel_target | Character |  |
| event_target:recipient | Character |  |
| event_target:scheme | Scheme |  |
| sActivity | Activity |  |
| sArmy | Army |  |
| sC | Character |  |
| sCB | ActiveCasusBelli |  |
| sCharacter | Character |  |
| sCombat | Combat |  |
| sCombatSide | CombatSide |  |
| sCulture | Culture |  |
| sCultureGroup | CultureGroup |  |
| sDynasty | Dynasty |  |
| sFaction | Faction |  |
| sFaith | Faith |  |
| sGreatHolyWar | GreatHolyWar |  |
| sHolyOrder | HolyOrder |  |
| sHouse | DynastyHouse |  |
| sMercenary | MercenaryCompany |  |
| sProvince | Province |  |
| sScheme | Scheme |  |
| sSecret | Secret |  |
| sTitle | Title |  |
| sWar | War |  |
| AccessSelf | [unregistered] |  |
| Custom | [unregistered] |  |
| End | TopScope |  |
| GetFlagName | CString |  |
| GetRootScope | [unregistered] |  |
| GetValue | CFixedPoint |  |
| ScriptValue | CFixedPoint |  |
| Self | [unregistered] |  |
| event_target:actor | Character |  |
| event_target:agent | Character |  |
| event_target:duel_target | Character |  |
| event_target:recipient | Character |  |
| sActivity | [unregistered] |  |
| sArmy | [unregistered] |  |
| sC | [unregistered] |  |
| sCB | [unregistered] |  |
| sCharacter | [unregistered] |  |
| sCombat | [unregistered] |  |
| sCombatSide | [unregistered] |  |
| sCulture | [unregistered] |  |
| sCultureGroup | [unregistered] |  |
| sDynasty | [unregistered] |  |
| sFaction | [unregistered] |  |
| sFaith | [unregistered] |  |
| sGreatHolyWar | [unregistered] |  |
| sHolyOrder | [unregistered] |  |
| sHouse | [unregistered] |  |
| sMercenary | [unregistered] |  |
| sProvince | [unregistered] |  |
| sScheme | [unregistered] |  |
| sSecret | [unregistered] |  |
| sTitle | [unregistered] |  |
| sWar | [unregistered] |  |

### War

Note that this list has been generated programmatically.

| Function | Return Type | Usage |
| --- | --- | --- |
| GetActiveCB | ActiveCasusBelli |  |
| GetActiveCasusBelli | ActiveCasusBelli |  |
| GetPrimaryPlayerEnemy | Character |  |
| GetStartDate | Date |  |
| MakeScope | Scope |  |
| AccessSelf | [unregistered] |  |
| Custom | CString |  |
| GetActiveCB | [unregistered] |  |
| GetActiveCasusBelli | [unregistered] |  |
| GetID | uint32 |  |
| GetName | CString |  |
| GetStartDate | [unregistered] |  |
| IsValid | bool |  |
| MakeScope | Scope |  |
| Self | [unregistered] |  |
