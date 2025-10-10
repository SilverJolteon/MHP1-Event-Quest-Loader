# Monster Hunter Portable/Freedom Event Quest Loader

Load event quests directly from an external file, now with support for Freedom (USA and EUR).

![Screenshot](/.github/screenshot.png)

## Usage

Create a new folder in `ms0:/PSP/SAVEDATA/` and name it one of the following, depending on your version:

- Portable (JPN): `ULJM05066QST`

- Freedom (USA): `ULUS10084QST`

- Freedom (EUR): `ULES00318QST`

Place `MHPSP.bin` in the newly created folder and copy the contents of the respective .ini to your cheats list. Then, you can access the quests from the event quest menu in the gathering hall.

- For Freedom (USA and EUR), to access the quests, do the following:
  - Talk to the quest receptionist dressed in red.
  - Highlight the bottom-most option and press right on the D-Pad.
  - Press X to open the menu.
 
- Freedom (EUR) **cannot** load JP quests as it will crash. You must use the English translated quests.

## Notes

The external MHPSP.bin file is a simple concatenation of .mib quest files, each zero-padded to 0x6800 bytes in length.

No patch for Freedom yet until I figure out the event quest menu.

## Credits

- Special thanks to [IncognitoMan](https://github.com/IncognitoMan) and [Kurogami2134](https://github.com/Kurogami2134) for tips and their own ASM as a groundwork.
- Special thanks as well to [Immortalcripple](https://github.com/Immortalcripple) for helping out with testing.
- Freedom Enhanced by [YuzucchiNyan](https://github.com/GReinoso96)
- English and Spanish quests translated by Anonymous
