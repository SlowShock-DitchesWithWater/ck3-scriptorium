<!-- 来源: https://ck3.paradoxwikis.com/Attributes oldid=37258 抓取于 2026-10-23T09:37:40+08:00 -->

# Attributes — Education


Characters up to the age of 6 can be given an Education Focus geared towards one of the skills. This will default to one of the two attributes in their Childhood trait, but a parent can choose it manually with the button at the lower left of their portrait. This can only be done once per child, and not be changed later on. When the character becomes an adult, they will gain an education trait for the matching attribute.

Between the ages of 6 and 16 the child will build up a hidden education score. It has a chance to increase by +2 every birthday (10 chances), plus some additional chances, as detailed below. Once the character reaches the age of 16 they will acquire an education trait based on that score.

| Score | Education trait level |
| --- | --- |
| 0-7 | ★ |
| 8-12 | ★★ |
| 13-17 | ★★★ |
| 18+ | ★★★★ |

The chance of the child getting a higher tier education is increased by the guardian's relevant skill plus half of their learning skill, as well as the child or guardian having a positive intelligence trait ( Quick/ Shrewd,  Intelligent,  Genius). The guardian or child having a negative intelligence trait ( Slow,  Stupid,  Imbecile) will negatively affect their education, as will pushing them to an Education Focus that does not match their Childhood trait. These modifications are further explained and calculated below.

A child of a culture that discovered the Knighthood innovation, has a Martial education focus, and is of a gender that can be knighted will also be trained as a squire, receiving a Prowess education trait when they come of age *in addition* to a Martial one. For Prowess, the educator's abilities or any other effects that enhance education are irrelevant; only the child's traits matter. Traits that boost Prowess ( Hale,  Robust,  Herculean,  Strong,  Giant) will increase the chance of a high-tier Prowess education, while negative Prowess and other sickly traits ( Delicate,  Frail,  Feeble,  Weak,  Dwarf,  Spindly,  Wheezing,  Hunchbacked,  Inbred,  Bleeder) will diminish it.

If the child has a guardian of a different faith or culture, when given the guardian, it can be specified whether the child should be raised in the parent's or guardian's faith and/or culture. The child also has a higher chance to copy the guardian's personality traits (and also less likely to have the personality trait opposite to that of guardian's). If the guardian has the Witch trait or secret, they will have the option to try converting their wards to witchcraft (always succeed if "Found Witch Coven" decision was taken).

A guardian has  **+5** towards the child and the ward has  **+15** opinion towards the guardian.

### Point modifiers

Several factors can provide extra education score modifiers above and beyond those earned via the normal yearly roll:

- The guardian's council having a spouse that is focused on patronage, has a high learning education, high learning skill, or Erudite trait, can trigger adding **+1** free point. This can occur happen multiple times over the course of the child's education, and the points are accumulated.
- Having a child educated by a guardian who has a University building in their realm (and paying gold for the privilege) provides a 60% chance of gaining **+2** points and a 40% chance of gaining **+3** points. The roll will happen on the 16th birthday. The internal flag for attending a university is set on the child immediately and not removed if their guardianship changes, so even if the University holding is lost or the guardian dies, the bonus will still be awarded.
- If your court has the Court Tutor position populated when the child comes of age, an additional education roll occurs. The guaranteed minimum bonus of **+2** points is most likely if the Tutor has Terrible, Poor, or Average aptitude, while Good or Excellent aptitude make getting **+3** points more likely. With Excellent aptitude only, there is an approximately 10% chance of the bonus being an entire **+4** points.
- If the child's dynasty has the second level of the "Kin" Dynasty Legacy unlocked, an additional education roll occurs when the child comes of age, with success (60%) equaling **+3** and failure (40%) equaling **+2** points. In essence, a guaranteed 2 bonus points with a chance of 1 additional.
- Some cultural traditions provide small modifications to educational outcomes, for instance:
  - The "Charismatic" tradition has a 60% chance of adding **+1** point for diplomatic educations only.
  - The "Agrarian" tradition applies a penalty of **-1** point for martial educations.

Note that, with the exception of the points earned sporadically via the guardian's spouse, none of these bonuses take into consideration how long the child "logically" would have been under their effect. As long as you have the Court Tutor, Dynasty Legacy, etc. on the day before the child turns 16, they will receive the full and complete benefit when they come of age. On the other side, this also means that if you have a working Court Tutor for the child's entire upbringing, only to fire them the day before the 16th birthday, there will be no bonus whatsoever.

### Education roll calculations

The success chances for a +2 education score has a base value of 60%.

Success Chance  =  (    60 + S u c c e s s F a c t o r   100 + S u c c e s s F a c t o r + F a i l u r e F a c t o r    )  × ×  100 % %    {\displaystyle {\text{Success Chance}}=\left({\frac {60+SuccessFactor}{100+SuccessFactor+FailureFactor}}\right)\times 100\%}

The success- and failure-factors are summed from the table below. Empty = 0.      Factor  = ∑ ∑   C h i l d T r a i t F a c t o r  + ∑ ∑   G u a r d i a n T r a i t F a c t o r    {\displaystyle {\text{Factor}}=\sum {ChildTraitFactor}+\sum {GuardianTraitFactor}}

**Success factors**

|  | Child Trait Factor | Guardian Trait Factor |
| --- | --- | --- |
| Genius | 20 | 15 |
| Intelligent | 15 | 10 |
| Quick / Shrewd | 10 | 5 |
| Guardian's culture has at least one of the following traditions: Dynastic Pragmatism Noble Adoption Northern Stories Storytellers |  | 10 |
| Childhood trait Matching | 20 |  |
| Childhood trait Not Matching | **-20** |  |
| Guardian's relevant Skill |  | 0.4 * relevant Skill |
| Guardian's learning skill |  | 0.2 * learning skill |

**Failure factors**

|  | Child Trait Factor | Guardian Trait Factor |
| --- | --- | --- |
| Slow / Dull | 10 | 5 |
| Stupid | 15 | 10 |
| Imbecile / Inbred (child only) | 20 | 15 |
| No Guardian |  | 20 |

### Prowess trait

Children undergoing a Martial education can also receive a Prowess education trait when they come of age. To qualify, the child's culture or the educator's culture must have the Knighthood innovation and the child must be of a gender that can become knights. The system that determines which Prowess trait the child gets is completely separate from the other education traits. The perks, spouse or universities don't influence the outcome.

When the child finishes their education, the game creates a temporary score for them, which starts equal to the Martial education level they obtained. Then, the game changes this score depending on the child's physical traits (multiple traits stack):

| Trait | Prowess Factor |
| --- | --- |
| Herculean | +3 |
| Robust, Strong, Giant | +2 |
| Hale | +1 |
| Delicate, Spindly, Wheezing, Hunchbacked, Inbred, Bleeder | -1 |
| Frail, Weak, Dwarf | -2 |
| Feeble | -3 |

Lastly, there's a 25% chance the score increases +2, 25% chance it decreases by -2, and 50% chance it stays unchanged.

The final score is then the child's Prowess education level.

