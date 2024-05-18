# Kongregate and Flash games

After Adobe Flash Player's end of life in 2020, Kongregate made their Flash games load in another swf player: SuperNova. However, it was not perfect (and they did not implement it perfectly either) so they later decided to switch over to Ruffle. Unfortunately, they did not implement it properly and it is still is development. As a result, there are games on Kongregate that do not load while they should or are partly broken and none of the Flash games can submit high scores (meaning badges do not award naturally).

In order to solve this problem, I created a user script: [the Kongregate Flash games fixer](https://greasyfork.org/en/scripts/438325-kongregate-flash-games-fixer). This script allows people to choose between four different swf players to play Flash games by adding buttons above them (which can also be used to reload said games). You will find below a short description of each swf player, how to install my script (and whatever else that could be needed for each of them) and how to get everything working.

## 1) Ruffle

Ruffle is a Flash player emulator in active development. You can read more about it at [ruffle.rs](ruffle.rs). It can run most games, but not all. With my user script, you will be able to play more games than without and with a second one, **you will even see them submit high scores!**

How to proceed:
* Install a user script manager (a browser extension that... manages user scripts): Tampermonkey, Violentmonkey, Greasemonkey or something else (with "monkey" in the name, most of the time...). Then, activate it (if needed).
<br>*My user script does not work in Greasemonkey 4, so in any browser supporting that, use something else.*
* Go to [Greasyfork](https://greasyfork.org/en/scripts/438325-kongregate-flash-games-fixer) and click "install".
* **If you want high scores to be submitted, install the very good [Kong Flash API patcher](https://greasyfork.org/en/scripts/494088-kong-flash-api-patcher) user script from Colin969, a Ruffle developer.**

## 2) Adobe Flash Player

Despite its end of life, Adobe Flash Player can still be used with the proper setup. The upside is that everything will work as it used to, including high scores submission.

How to proceed:
* Install a browser supporting Flash. I recommend [Pale Moon](https://www.palemoon.org) or Basilisk. Most browsers (including Firefox, Edge and Chrome) stopped supporting Flash in 2020.
* (Windows and Mac only, I think) If Flash is already installed on your computer and if the version number is strictly higher than 32.0.0.371, then uninstall it.
* Download and unzip [these zipped files](https://archive.org/download/flashplayerarchive/pub/flashplayer/installers/archive/fp_32.0.0.371_archive.zip). Then, open the correct installer for your system: *flashplayer32_0r0_371_win.exe* (Windows), *flashplayer32_0r0_371_mac.dmg* (Mac), *flashplayer32_0r0_371_linux.i386.tar.gz* (32-bit Linux) or *flashplayer32_0r0_371_linux.x86_64.tar.gz* (64-bit Linux).
<br>**IMPORTANT:** If asked at the end of the installation, disable the automatic updates!
<br>**Note:** If you are using another browser, you *might* need to run the files that have the same names but also contain "pep". This will be the case for Chrome, Edge and Opera.
* Install Greasemonkey for Pale Moon, by opening [this link](https://github.com/janekptacijarabaci/greasemonkey/releases/download/3.31.4Fork/greasemonkey-3.31.4-pm_forkBranch.xpi) <u>in Pale Moon</u>.
* Go to [Greasyfork](https://greasyfork.org/en/scripts/438325-kongregate-flash-games-fixer) and click "install".

**Warning:** If all you see is a black screen while still being able to hear audio and interact, then you might want to read [this page](http://flashpointarchive.org/datahub/Extended_FAQ#AMD) (this bug only affects certain graphic cards).

## 3) SuperNova player *(Windows only!)*

The SuperNova player is launched from the browser but opens games in its own window. You can read more on the [official website](getsupernova.com) but the player is no longer maintained (or so it seems) and it can be wrongly labeled as a threat by antivirus softwares. Most games run in it but high scores do not (and will never) be submitted.

How to proceed:
* Install the [SuperNova player](https://web.archive.org/web/20210426173012id_/https://cdn.getsupernova.com/update/SuperNovaSetup0.1.23.exe) on your computer.
* Install a user script manager (a browser extension that... manages user scripts): Tampermonkey, Violentmonkey, Greasemonkey or something else (with "monkey" in the name, most of the time...). Then, activate it (if needed).
<br>*My user script does not work in Greasemonkey 4, so in any browser supporting that, use something else.*
* Go to [Greasyfork](https://greasyfork.org/en/scripts/438325-kongregate-flash-games-fixer) and click "install".

## 4) AwayFL

AwayFL is another Flash player emulator, still in development.

How to proceed:
* Install a user script manager (a browser extension that... manages user scripts): Tampermonkey, Violentmonkey, Greasemonkey or something else (with "monkey" in the name, most of the time...). Then, activate it (if needed).
<br>*My user script does not work in Greasemonkey 4, so in any browser supporting that, use something else.*
* Go to [Greasyfork](https://greasyfork.org/en/scripts/438325-kongregate-flash-games-fixer) and click "install".

<hr>

The Kongregate Flash games fixer has been successfully tested on Firefox, Pale Moon, Edge, Chrome, Basilisk and Waterfox Classic, on Windows, Mac and Linux (sparkylinux, at least).

*Last edited on 2024, May 8th.*
