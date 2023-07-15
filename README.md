# MUA+XML2 File Integrity Checker
This a basic file integrity checker used for Ultimate Alliance PC 2006, Ultimate Alliance 2 PC Steam 2016, and X-Men Legends 2 PC 2005. This is used as a troubleshooting tool to find any missing or altered game files and report them back to the user.

## Requirements
1. Python for all game checkers except MUA1 if you have Windows with PowerShell.

## Important Notes
- For all 3 games, it is expected that the user has already installed their cracked exe files to their game folders in order for each game to run properly. So for example, if someone runs the checker on a completely fresh version of MUA1 but without installing the cracked game.exe file, the checker will flag that file as altered.
- For MUA2, the checker will scan for the base game files + Update.v20160804 files as well. So for example if the user uses the checker on the base game of MUA2 without installing the Update.v20160804 files, the checker will flag those update files as missing.
- For XML2, the checker is made to scan for the UK version of the game files and not the US version that includes 3 separate iso files to setup.