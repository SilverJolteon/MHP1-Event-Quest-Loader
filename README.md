# Monster Hunter Portable/Freedom Event Quest Loader

Load event quests directly from an external file, now with support for Freedom (USA and EUR).

<img src="/.github/screenshot.png" width="480px"/>

## Usage

Create a new folder in `ms0:/PSP/SAVEDATA/` and name it one of the following, depending on your version:

- Portable (JPN): `ULJM05066QST`

- Freedom (USA): `ULUS10084QST`

- Freedom (EUR): `ULES00318QST`

Place `MHPSP.bin` in the newly created folder and copy the contents of the respective .ini to your cheats list OR apply the ISO patch with [DeltaPatcher](https://www.romhacking.net/utilities/704/). Then, you can access the quests from the event quest menu in the gathering hall.
 
- Freedom (EUR) **cannot** load JP quests as it will crash. You must use the English or Spanish translated quests.
- The external MHPSP.bin file is a simple concatenation of .mib quest files, each zero-padded to 0x6800 bytes in length.

# Monster Hunter Portable/Freedom DX

 ### [<ins>**Download Latest Release**</ins>](https://github.com/SilverJolteon/MHP1-Event-Quest-Loader/raw/main/DX/Portable-Freedom%20DX.zip)

All-in-One patch that includes the following:
  - ### Event Quest Loader
    > Read event quests from an external file. By SilverJolteon
  - ### Input Drop Fix
    > Fixes issue where button inputs are ignored. By YuzucchiNyan
  - ### Hold to Gather
    > Allows you to simply press and hold the gather button when crouched. By YuzucchiNyan
  - ### True Raw
    > Displays the non-bloated "true" raw attack value of weapons. EUR version by YuzucchiNyan, ported to JPN and USA by SilverJolteon
  - ### Early Kill Lao-Shan Lung
    > Disables the HP threshold that prevents killing Lao-Shan Lung before reaching the final area. Ported by SilverJolteon from IncognitoMan's FUC
  - ### English Menu Patch (Portable)
    > Translates Menus, Items, Equipment, Skills, etc. into English. By YuzucchiNyan
  - ### English Quest Patch (Portable)
    > Translates non-event quests into English. By SilverJolteon
 


## Credits

- Special thanks to [IncognitoMan](https://github.com/IncognitoMan) and [Kurogami2134](https://github.com/Kurogami2134) for tips and their own ASM as a groundwork.
- Special thanks as well to [Immortalcripple](https://github.com/Immortalcripple) for helping out with testing.
- Freedom Enhanced by [YuzucchiNyan](https://github.com/GReinoso96)
- English quests translated by [GrenderG](https://github.com/GrenderG)
- Spanish quests translated by Anonymous
