# Monster Hunter Portable/Freedom Event Quest Loader

Load event quests directly from an external file, now with support for Freedom (USA and EUR).

![Screenshot](/.github/screenshot.png)

## Usage

Create a new folder in `ms0:/PSP/SAVEDATA/` and name it one of the following, depending on your version:

- Portable (JPN): `ULJM05066QST`

- Freedom (USA): `ULUS10084QST`

- Freedom (EUR): `ULES00318QST`

Place `MHPSP.bin` in the newly created folder and copy the contents of the respective .ini to your cheats list OR apply the ISO patch with [DeltaPatcher](https://www.romhacking.net/utilities/704/). Then, you can access the quests from the event quest menu in the gathering hall.
 
- Freedom (EUR) **cannot** load JP quests as it will crash. You must use the English or Spanish translated quests.

## Monster Hunter Portable/Freedom DX (xdelta patch only)
- Includes the following patches:
  - Event Quest Loader
  - Input Drop Fix - by YuzucchiNyan
  - Hold to Gather - by YuzucchiNyan
  - True Raw - EUR version by YuzucchiNyan, ported to JPN and USA
  - Early Kill Lao-Shan Lung - Ported from IncognitoMan's FUC
  - English Menu Patch (Portable) - by YuzucchiNyan

## Notes

The external MHPSP.bin file is a simple concatenation of .mib quest files, each zero-padded to 0x6800 bytes in length.

## Credits

- Special thanks to [IncognitoMan](https://github.com/IncognitoMan) and [Kurogami2134](https://github.com/Kurogami2134) for tips and their own ASM as a groundwork.
- Special thanks as well to [Immortalcripple](https://github.com/Immortalcripple) for helping out with testing.
- Freedom Enhanced by [YuzucchiNyan](https://github.com/GReinoso96)
- English quests translated by [GrenderG](https://github.com/GrenderG)
- Spanish quests translated by Anonymous
