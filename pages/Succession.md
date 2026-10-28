<!-- 来源: https://ck3.paradoxwikis.com/Succession oldid=35670 抓取于 2026-10-23T09:33:56+08:00 -->

# Succession

> [!] Please help with verifying or updating older sections of this article.
> [!] At least some were last verified for version 1.10.
>
> [!] This article is for the PC version of Crusader Kings 3 only.

Succession involves the inheritance of  titles,  gold,  men-at-arms and artifacts upon the death or abdication of a ruler.

## Heirs

If a character expects to inherit one or more titles from a ruler, they are that ruler's  heir. If this includes their primary title, they are that ruler's primary heir specifically. The player heir denotes the character who the player will continue playing as upon succession; this is always one's primary heir *unless* that character belongs to a different dynasty.

## Eligibility

Certain laws and doctrines determine who is eligible for inheritance. In addition, some traits may disinherit their owner together with all their descendants. Ineligible characters do not inherit claims either.

- The gender law determines whether only men, only women or both inherit. With male preference, women are ineligible as long as they have eligible brothers; vice versa for female preference.
- Theocratic rulers cannot inherit.
- The following traits disinherit:
  - Bastard and Bastard Founder
  - Child of Concubine **if** either monogamous or polygamous
  - Disinherited **if** the predecessor belongs to the same dynasty
  - Eunuch
  - Monk/Nun (does not disinherit descendants, inherits claims nonetheless)
  - Order Member (does not disinherit descendants, inherits claims nonetheless)

## Realm succession

The  realm succession law applies to every title which does not have an individual title succession law assigned.

Several illustrated examples are given, which show the primary according to different laws:

- numbers denote the line of succession, with 0 being the current holder
- characters marked with an "x" are ineligible
- red squares denote men, blue circles denote women
- black figures denote deceased characters

### Single heir

#### Primogeniture

An illustrated example of male only primogeniture

All titles are inherited by the oldest child. If this child is dead, a living heir is sought among their descendants in the same manner. If the ruler has no living descendants, the oldest sibling is chosen. If this sibling is dead, a living heir is sought among their descendants in the same manner. If lateral branches provide no candidate, the primary parent* is chosen. If they're dead, a candidate is sought among their siblings, etc.

*the father in a patrilineal marriage, the mother in a matrilineal marriage

#### Ultimogeniture

An illustrated example of male preference ultimogeniture

All titles are inherited by the youngest child. If this child is dead, a living heir is sought among their descendants in the same manner. If the ruler has no living descendants, the youngest sibling is chosen. If this sibling is dead, a living heir is sought among their descendants in the same manner. If lateral branches provide no candidate, the primary parent* is chosen. If they're dead, a candidate is sought among their siblings, etc.

#### House seniority

An illustrated example of equal house seniority

All titles are inherited by the oldest house member. With male preference, younger men take precedence over older women; vice versa for female preference.

### Multiple heirs

#### (Regular) partition

An illustrated example of female preference partition

1. The oldest child is given the primary title along with its de facto capital and any higher title the capital belongs to de jure.
2. All empires are distributed in order. The oldest child with the **fewest empire titles** takes priority. If a non-primary heir received titles, they are also given any lower title that belongs to them de jure. Importantly, they receive no more titles in the following steps.
3. All kingdoms are distributed in order. The oldest child with the **fewest empire plus kingdom** **titles** takes priority. If a non-primary heir received titles, they are also given any lower title that belongs to them de jure. Importantly, they receive no more titles in the following steps.
4. All duchies are distributed in order. The oldest child with the **fewest empire plus kingdom plus duchy** **titles** takes priority. If a non-primary heir received titles, they are also given any lower title that belongs to them de jure. Importantly, they receive no more titles in the following steps.
5. All counties are distributed in order. The oldest child with the **fewest county titles** takes priority.
6. All baronies go to whomever holds their de jure counties.

*Notes:*

- If a deceased child had any descendants, their would-be primary heir will take their place during succession.
- The primary heir will vassalise every other heir, unless their rank is equal to theirs.
- If an heir held titles prior to succession *and* they were the predecessor's direct vassal, those titles are taken into account as well.
- See primogeniture if the ruler has no descendants.
- There may be exceptions to these rules if another heir already holds land within a title someone else would inherit.
- If the capital lies within the de jure territory of a held title which is equal in rank to but not itself the primary, said title will not be inherited along with the capital.

#### Confederate partition

Like partition, except that new titles may automatically be created (at no cost) beforehand. The titles in question are those the ruler could have created prior to death or abdication, but only if their rank is equal to the primary title's rank. The minimum county threshold is checked taking into account any discount from the late ruler's legitimacy.

#### High partition

Like partition, except that the primary heir takes half the titles in each step first. If there's an odd number of them, the total is rounded up.

In all cases, if all else fails and there are no valid living heirs represented in the game for a ruler, the titles will be inherited by the ruler's liege. If the ruler was independent (and thus has no liege), one of the ruler's vassals is selected to inherit. If the ruler had no living vassals, one of the ruler's courtiers is selected to inherit.

## Title succession

A title succession law can be assigned to individual titles; besides the gender laws, these are all a form of elective succession. Options are restricted to certain ranks, cultures and/or titles and/or government type (Feudal only). If the primary title has a title succession law, its de facto capital will not be inherited along with it: it goes to whomever would be the primary heir according to realm succession alone.

Any Title Men-at-Arms are inherited with the title they are linked to, in contrast to normal Men-at-Arms.

## Title claim inheritance

The gender law determines whether sons, daughters or both inherit claims on their parents' titles. Upon succession, eligible children are given  pressed claims on titles they did not inherit nor vassalise. If the parent held pressed claims themselves,  unpressed claims are inherited in their stead. Unpressed claims cannot be passed down, but will revert to the former status if pressed in a war. Note that a deceased child's place holder during partition will not receive the claims their parent would have inherited.

- **Male/female only:** Only sons/daughters inherit claims.
- **Male/female preference:** Both daughters and sons inherit claims.
- **Equal:** Both daughters and sons inherit claims.

The faith's view on gender determines which children get  implicit claims during their parents' lifetime. Note that a deceased child's place holder during partition will receive implicit claims in their stead, but only if they're of the appropriate sex.

- **Male dominated:** Only sons receive implicit claims.
- **Female dominated:** Only daughters receive implicit claims.
- **Equal:** Both daughters and sons receive implicit claims.

## Other forms of inheritance

The primary heir inherits all  gold,  men-at-arms and artifacts upon succession.

Title Men-at-Arms are Men-at-Arms that are tied to specific Titles, a feature of Domicile governments, like Administrative,  Celestial and  Meritocratic. When a Title changes ownership, These regiments move with the title, so can be lost on succession.

Part of late ruler's :

- 25% if heir was landed (that amount will be added to his/hers current legitimacy)
- if heir was unlanded, then a great percentage depending on birth order and gender (legitimacy loss is negligible for a first child of preferred gender)

## Abdication

Abdication entails a ruler renouncing all Titles, triggering a Succession.

Abdication can be done by losing a tyranny war or through a level 3 stress mental break.

The abdicating ruler loses **-500**  Prestige, but gains  Pressed claims on all of their former titles.

## Notes

- If an unlanded character inherits a duchy+ title, they will automatically usurp a county in their new realm, preferably its de jure capital. If none of the title's de jure land was held, the title goes to the primary heir instead.
- Newly landed characters receive a selection of men-at-arms at no cost. The larger their income is, the more men-at-arms they will receive.
- With partition succession, the primary heir cannot be granted titles that other heirs expect to inherit.
- A ruler with no descendants will pass their titles to their liege. If that ruler was independent, a vassal of theirs will inherit, or a courtier if no vassals exist.
- Several cultures can get advanced succession laws early due to their Cultural Innovations.
  - Characters of Czech or Slovien culture can enact the *House Seniority* law at any Crown Authority due to their *Table of Princes* Cultural Innovation.
  - Characters of Aragonese, Basque, and Catalan culture can enact the *High Partition* Law due to their *Visigothic Codes* Cultural Innovation. Due to the same Innovation, they can also enact the Equal (Cognatic) Law at High Crown Authority.
- The display order of titles in the character screen is decided as follows:
  1. The primary title always comes first.
  2. Higher tier titles come before lower tier titles.
  3. Titles of the same tier are ordered according to how long each title has been in possession, the oldest one coming first.

## Tips

- Feudal rulers who have only one title of the same rank as the primary title, but are at risk of the realm splitting due to Confederate Partition, can consider adding "Feudal Elective" succession to their primary title.
- The dynasty head can disinherit dynasty members at the cost of Renown and Prestige.
- The primary heir will always inherit each holding within the capital county.
- With partition succession, all titles within the capital duchy pass to the primary heir if all other heirs expect a duchy+ of their own. Likewise, all titles within the capital kingdom go to the primary heir if all other heirs expect a kingdom+ of their own.
- If an heir is granted their titles in advance, their fellow heirs won't inherit claims on them, which reduces infighting after succession. Note that children tend to love their parents, which generally makes them loyal vassals. If so, they will receive a significant opinion of predecessor opinion bonus towards the primary heir upon succession.
- If a ruler's primary title is outside one's de jure realm, they can be granted independence. Each landed dynasty member, who is not subject to another, generates renown. As the dynasty head, one retains some control over these rulers, e.g. calling such dynastic rulers to war (at the cost of renown).
- If one's faith has the *monasticism* tenet, characters above the age of 9 can be asked to take the vows: this disqualifies them from inheritance. Even married characters can be asked, assuming they're the primary spouse.

## References
