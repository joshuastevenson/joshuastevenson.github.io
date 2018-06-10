---
title: My Computer's Organization
lastEdited: 2017-04-25
---

# My computer
My computer is set up just the way I like it. (Actually I have complaints. Everything it terrible.) Obviously this way is superior and everyone should copy me. Then I could use any computer. (Wait, I don't want to deal with everyone's sticky keyboard. Yes my keyboard is sticky too, but its sticky just right.)

See also Installed Programs. 

## Windows
Use Windows 10. I can't even use Windows 7. 7's task manager is too bad. Window's Defender is also pretty much all that is needed in 10. 

### Taskbar
On the left. Vertical pixels are too precious to have the taskbar on the top or the bottom. 

"Combine Taskbar Items: `Never`", "Use small taskbar buttons: `On`". Ideally there would be a "Never combine, hide labels" option but that is too much to ask for. On my old laptop which had a lower resolution screen, I used a program called 7taskbar tweeker. to make the taskbar thinner. 

#### Pinned to the taskbar
Task manager

A Shortcut targeting `%SystemRoot%\explorer.exe /E,::{20D04FE0-3AEA-1069-A2D8-08002B30309D}`, aka mycomputer. I have a custom icon of a triforce. At some point there wasn't a direct way to make a shortcut to root or what ever the drive selection level is called.

Firefox

### Desktop

Keep it clean. It actually helps performance.

* recycling bin
* dir "pi"
* dir "prg"
* "r.bat" (`shutdown -r -t 0`) 

r.bat is needed to restart without fastboot so that the windows partition is not locked and can be written to by linux. On the desktop for moderate access. I don't want it pinned to start and accidentally click it.

My wall paper is a picture of a wall. "KILROY WAS HERE"

### prg
Where I dump every program that is not installed to program files. Bare exe files need to be put in dirs.

#### zzzzPATHzzzz

* links
* path
* *generate.py*

*Desktop/prg/zzzzPATHzzzz/path/* is on my path. I drop Windows shortcuts into the links folder and then run *generate.py* to create bat and sh files of the same name. bat for cmd and extensionless sh for git bash.

This does 2 main things. It allows me to get new programs on my path without restarting my shell. It prevents my path from being polluted by noisy bin dirs.

<script src="https://gist.github.com/joshuastevenson/e831156dd25ca61a8cd43dcfe3ca5ff9.js"></script>

### pi
Your "My Documents" and your home directory are not yours. Every program ever assumes you want stuff there and will probably drop configuration data there.

Permanent structure:
* archived stuff
* cs
  * [langs]
* other
  * Other media
    * audio
    * gifs
    * images
    * other
    * video
  * res
  * stuff
* School
* WorkRes

Random files and directories end up littering this tree. If something appears on my desktop, in time it either is deleted or moved to pi. Over time it will be moved to a more specific directory. I prefer depth over breath. It provides less cognitive overhead in decision making. 

"School" will probably leave the root soon. I'll probably zip it up and drop it in "archived stuff".

### Start menu
I didn't hate Windows 8's start menu. I don't hate 10's. I do hate telling someone instructions and then they don't work because they're using classic shell or some other program. 

If I want to launch a program I hit the windows key and start typing the name and hit enter. It is simple. There's no choices. I already know what I'm opening. I don't need to search the screen. I do have a few things pinned to start but more often than not I'll search "pain" instead of clicking on the paint[.]net shortcut. I'm more likely to pin things that are harder to find.

pinned items:
* Control Panel
* Cygwin
* Uninstall programs
* Chrome
* WiinUSoft
* bluetooth (shortcut targeting `ms-settings:bluetooth`)
* cygwin package manager
* paint[.]net
* OBS
* Sublime
* Notepad++
* Windows media player
* display (shortcut to `ms-settings:display`)

A few of these things require shortcuts in `C:\Users\USER_sdfsdfs\AppData\Roaming\Microsoft\Windows\Start Menu\Programs` to be pinned to start.


### Explorer

**DO NOT HIDE KNOWN EXTENSION TYPES** and show hidden files.

Sidebar:

Everything is collapsed except for "Quick access". Quick access contains:
* C:
* [home]
* Downloads
* pi
* prg

Turn off showing of recent and frequently used files.

There are way too many choices if you leave all the views expanded. Onedrive doesn't exist in my life anyway. 

I hate that downloads and pictures have special thumbnails. I hate that you can't make a shortcut to your user directory or desktop and have there logical parents be the parent when you go to them.

## Linux

Currently Ubuntu Gnome 16.04 LTS. Gnome is my preferred environment but I'm getting less satisfied with it. I use ubuntu mate on pis.

### bash

* `PS1` MUST have color
* Root's PS1 is red (`31`)
* `alias ls=ls -A --color`


### GNOME
* Enable minimize/maximize buttons
* Alt tab by window, not application 

## grub
Default option: Windows. Let windows auto update in peace.