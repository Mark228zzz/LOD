# LOD (life or dead)


## Overview

### LOD is a Python-based modeling project that includes various elements such as creatures, food, structures, and windows. In the game, creatures fight for life, reproducte, die, eat and etc. The game was made using `pygame`.

## Installation

### For download this project you need to download `pygame` with the following command:
1. For Linux: `pip install pygame`
2. For windows: go to *https://www.pygame.org* then find download, then press to download pygame


## Usage

### For using this project you need to run the `main.py` file after download `pygame`.


## How to play

### After download `pygame` and run the `main.py` file, you can see how creatures are developing, reproducting, dieing and eating.


## Logs

### This project has `logs.txt` contains information about the creation and death of creatures, food, etc. After starting the game, the `logs.txt` are cleared.
### This project has `logs2.txt` contains creature and food population graph. For use this logs you need to uncomment in the `main.py` file this code:
```py
#if Const.STEP % 25 == 0:
#    with open('logs2.txt', 'a') as logs2:
#        logs2.write(round(len(List.animals)/10) * 'A' + ' | ' + round(len(List.predators)/10) * 'P' + ' | ' + round(len(List.foods)/10) * 'F')
#        logs2.write('\n')
```
<span style="color:blue">Be careful when using this log because it is not cleared and may fill up your computer's memory.</span>
