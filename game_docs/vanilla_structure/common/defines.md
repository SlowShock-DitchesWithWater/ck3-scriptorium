# common/defines 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：12（其中 Jomini 解析 12 个）
- 顶层块条目总数：162，跨文件唯一条目 144
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_defines.txt` | 125592 | 80 | 0 | jomini |
| `ai/00_ai.txt` | 66860 | 7 | 0 | jomini |
| `audio/00_audio.txt` | 3541 | 7 | 0 | jomini |
| `graphic/00_coa.txt` | 64 | 1 | 0 | jomini |
| `graphic/00_graphics.txt` | 62518 | 60 | 0 | jomini |
| `jomini/adjacencies.txt` | 325 | 1 | 0 | jomini |
| `jomini/fog_of_war.txt` | 804 | 1 | 0 | jomini |
| `jomini/mapeditor.txt` | 95 | 1 | 0 | jomini |
| `jomini/portraits.txt` | 1275 | 1 | 0 | jomini |
| `jomini/rivers.txt` | 375 | 1 | 0 | jomini |
| `jomini/text_coloring.txt` | 72 | 1 | 0 | jomini |
| `jomini/text_formatting.txt` | 285 | 1 | 0 | jomini |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_defines.txt（80 条目）

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

### ai/00_ai.txt（7 条目）

- NAI
- NFaction
- NCourtPositions
- NInventory
- NActivity
- NMigration
- NDynastyHouse

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

### graphic/00_graphics.txt（60 条目）

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
