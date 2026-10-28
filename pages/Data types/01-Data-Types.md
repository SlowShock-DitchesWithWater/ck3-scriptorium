<!-- 来源: https://ck3.paradoxwikis.com/Data_types oldid=14585 抓取于 2026-10-22T21:43:41+08:00 -->

# Data types — Data Types


Data Types are used in the gui and localization to control what the game does or displays. They are enclosed in square brackets and generally start with either a Promote or Global Function:

```
[GetPlayer.GetName]
```

`GetPlayer` is a Global Function that returns a Character Type (specifically the player), `GetName` is a function of the Character Type that returns the character's name. The `.` is used to separate each command in the chain.

Functions can be chained together to get different results:

```
[GetPlayer.GetSpouse.GetMother.GetName]
```

Will return the player's mother-in-law's name. `GetSpouse` and `GetMother` are both functions of the Character Type, but return another character instead of a string like `GetName`. The general rules are similar to scopes in scripting, the above example first gets the player, then switches context to their spouse, then their spouse's mother, before returning the name of that character.

Some functions require one or more arguments to correctly function:

```
[Add_int32( '(int32)3', '(int32)4' )]
```

`Add_int32` is a Global Function that takes two 32 bit integer arguments, and returns their sum as another 32 bit integer.

