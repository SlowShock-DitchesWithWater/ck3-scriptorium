<!-- 来源: https://ck3.paradoxwikis.com/Fonts oldid=35219 抓取于 2026-10-22T21:46:09+08:00 -->

# Fonts

## Acquiring and Preparing Fonts

Finding fonts is no easy task, they need to be readable, thematically fitting and free of charge. But fret not, this section will quickly guide you through the necessary steps to find the perfect font for your mod.

### Fantastic Fonts and Where to Find Them

The first step is to find the font itself.
 Be warned that there are many websites that claim to have "free" fonts which are actually shackled to a license that makes them unusable for our intended purposes. You should **always check the license attached to the font** and ensure you will be able to meet its legal requirements. If in doubt, search for ones labelled as "CC0".

Here is a list of websites that offer fonts which you may use in your mods:

| Website | Notes |
| --- | --- |
| Font Squirrel | Has a licence tab in each font's page. |
| Cool Text | Most fonts are something akin to public domain, but look up the font name online and find the licence just to be sure. |
| Vic Fieger's Website | "No license is required" for "free fonts", contact information on website if you wish to double check. |
| Google Fonts | Every font in this repository is verified to be under Open Font Licence. |

### Converting TrueType Fonts to OpenType Fonts

Crusader Kings 3 predominantly uses OpenType fonts `.otf` instead of the more archaic `.ttf`, as OpenType fonts are capable of storing more information and have far more complex behaviors.

But how do you convert your old, rusty n' trusty TrueType font to the new and shiny OpenType font format? Well, that's actually easy!
 OpenType inherited the overall structure of TrueType and, as such, converting one file type to the other is as easy as using one of the many, many online font conversion websites.

| FontConverter | Cloud Convert | Convertio | Miconv |
| --- | --- | --- | --- |
| In a pinch: renaming the file from `myfont.ttf` to `myfont.otf` and praying the engine reads it. |  |  |  |

Once your font has been converted to the appropriate format, it is ready to be placed in the game files.

## Changing Fonts in Crusader Kings 3

For this example, we will be replacing the map's text font with Eurocentric Font by Vic Fieger.

The game's fonts are predominantly located in `Crusader Kings III\game\fonts`.
 Since our objective is to change the map's font, we need to recreate the path to where the font file we wish to overwrite resides. Like this: `..Documents\Paradox Interactive\Crusader Kings III\mod\CoolFontTestMod\Fonts\mapfont`.

Once inside our version of the `mapfont` folder, we will place our font file inside and rename it from it's original name (in this case: `eurcntrc.otf`) to the name of the file we wish to overwrite (in this case: `Paradox_King_Script.otf`).

And, voilà, our map is now in a beautiful, vaguely soviet font.

World Map after switching fonts.

NB: Since the Vanilla font is unicameral, the developers did not use the capitalisation function on the realm names on the map, so if you use a bicameral font, the nomadic realms will display as "the Mongols" or "the Khazars" rather than "The Mongols" and "The Khazars"
