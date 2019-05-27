# Neo Geo Training Mode #

## Getting Started ###

Neo Geo Training Mode (NTM) is a tool on top of Fightcade witch gives you Dummy control and record/play features for Garou Mark Of The Wolves.

### Prerequisites ###

* Install [python 3.7](https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe)
* Latest [Unibios](http://unibios.free.fr/download.html) and be able to use it in offline Fightcade 1
* Latest [Fightcade 1](https://www.fightcade.com/download/windows)

### Features ###

* Dummy control
* Record and play p2 inputs

### Instructions ###

1. Click on **Clone or Download** and **Download ZIP**
2. Run run_iv.bat and test your controller inputs
3. Report your controller inputs in input_map.ini **player 2 and "Stop" inputs must be letters (ex: Z for Up input)**
4. Run offline fightcade emulator, garou (in mvs only, press START+A+B+C in game to open unibios menu) and enable infinite power, infinite life and infinite time
5. Chose P1 and P2 characters
6. run run_ntm.bat and start training

### Default ini ###

```
[p1 controls]
p1-up = ABS_HAT0Y
p1-left = ABS_HAT0X
p1-down = ABS_HAT0Y
p1-right = ABS_HAT0X
p1-a = BTN_WEST
p1-b = BTN_SOUTH
p1-c = BTN_NORTH
p1-d = BTN_EAST
p1-dummy = BTN_TR

[p2 controls]
p2-up = z
p2-left = q
p2-down = s
p2-right = d
p2-a = i
p2-b = k
p2-c = o
p2-d = l

[record controls]
record = BTN_TL
stop = a
play = ABS_Z
```
### NOTE: ###

**This tool is in an early stage and i'm not a software developer**
