# common/defines 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.21.0；快照日期与指纹见 manifest.json）
- 文件数：12（其中 Jomini 解析 12 个）
- 顶层块条目总数：168，跨文件唯一条目 149
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_defines.txt` | 137145 | 83 | 0 | jomini |
| `ai/00_ai.txt` | 71964 | 8 | 0 | jomini |
| `audio/00_audio.txt` | 4668 | 7 | 0 | jomini |
| `graphic/00_coa.txt` | 64 | 1 | 0 | jomini |
| `graphic/00_graphics.txt` | 69137 | 62 | 0 | jomini |
| `jomini/adjacencies.txt` | 325 | 1 | 0 | jomini |
| `jomini/fog_of_war.txt` | 804 | 1 | 0 | jomini |
| `jomini/mapeditor.txt` | 95 | 1 | 0 | jomini |
| `jomini/portraits.txt` | 1275 | 1 | 0 | jomini |
| `jomini/rivers.txt` | 375 | 1 | 0 | jomini |
| `jomini/text_coloring.txt` | 116 | 1 | 0 | jomini |
| `jomini/text_formatting.txt` | 285 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_defines.txt（83 条目）

- NGame
- NSetup
- NJominiMap
- NSkills
- NCharacter
- NOldAge
- NRulerObjective
- NChildbirth
- NMarriage
- NCharacterOpinion
- NLaw
- NCharacterInteraction
- NGovernment
- NActionPoints
- NCombat
- NArmy
- NFleet
- NRetreat
- NWar
- NScheme
- NPowerfulVassal
- NFaith
- NRite
- NReligion
- NTitle
- NSiege
- NChild
- NImprisonment
- NCounty
- NProvince
- NText
- NDynasty
- NHouse
- NHouseRelation
- NDreadEffectOnBoldness
- NDomain
- NFaction
- NPathFinding
- NCulture
- NMercenary
- NHolyOrder
- NCourt
- NSubjectContract
- NGUI
- NSuggestions
- NModifier
- NPortrait
- NPlayer
- NRaid
- NBarter
- NCharacterGlow
- NGraphics
- NRulerDesigner
- NInventory
- NRoyalCourt
- NInspiration
- NCourtPositions
- NStruggle
- NHouseUnity
- NMemories
- NTravel
- NDiarchy
- NActivity
- NVassalStance
- NAccolade
- NHostage
- NTaxSlot
- NEpidemic
- NLegend
- NDomicile
- NTaskContract
- NAdministrative
- NCouncilTasks
- NConfederation
- NKurultai
- NBloodBrother
- NMigration
- NSilkRoad
- NGreatProject
- NMandala
- NTreasuryBudgeting
- NTrade
- NRoad

### ai/00_ai.txt（8 条目）

- NAI
- NFaction
- NCourtPositions
- NInventory
- NActivity
- NMigration
- NDynastyHouse
- NTrade

### audio/00_audio.txt（7 条目）

- NJominiEars
- NGameAudioEffects
- NTextLinkAudio
- NGameAudio
- NPlayerMessage
- NCourtScene
- NDeclareWar

### graphic/00_coa.txt（1 条目）

- NCoatOfArms

### graphic/00_graphics.txt（62 条目）

- NJominiMapGraphics
- NJominiGraphics
- NGraphics
- NTerrainCulling
- NHud
- NCourt
- NDomicile
- NBarbershop
- NCamera
- NMapColors
- NBorder
- NTrees
- NRiver
- NMapName
- NCoatOfArms
- NUnitGraphics
- NTravelRouteGraphics
- NTradeRouteGraphics
- NCombatInterface
- NCombatPrediction
- NGrantTitleInterface
- NMapModes
- NTravel
- NWarMapModes
- NDiplomaticRelationsMapMode
- NCharacterWindow
- NLedgerWindow
- NArmyWindow
- NActivityWindow
- NGui
- NRallyPoint
- NMapIcon
- NGameIcons
- NGameDynamicIcons
- NOwnMapMode
- NProvincePositions
- NHoldingGraphics
- NCouncil
- NInspiration
- NMapObjects
- NMapLines
- NLifestyle
- NMainMenu
- NFindVassalList
- NElectionCandidateList
- NUnitStatusIcons
- NUnitStatus
- NUnitOrderIcons
- NSubjectContract
- NTextMatching
- NCultureHybridization
- NRoyalCourt
- NCoatOfArmsDesigner
- NStruggle
- NIntrigue
- NHouseUnity
- NHoldingSprawl
- NEpidemic
- NSilkRoad
- NRite
- NCharacterInteractionMenu
- NConfederationsMapMode

### jomini/adjacencies.txt（1 条目）

- NAdjacencies

### jomini/fog_of_war.txt（1 条目）

- NFogOfWar

### jomini/mapeditor.txt（1 条目）

- NMapEditor

### jomini/portraits.txt（1 条目）

- NJominiPortraits

### jomini/rivers.txt（1 条目）

- NRivers

### jomini/text_coloring.txt（1 条目）

- NTextColoring

### jomini/text_formatting.txt（1 条目）

- NTextFormatting
