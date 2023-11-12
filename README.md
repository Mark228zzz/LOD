# LOD (life or dead)


## Overview

### LOD is a Python-based simulation project featuring various elements like creatures, food, structures, and interactive windows. In the game, creatures struggle for survival, reproduce, die, eat, among other activities. The game was made using `pygame`.


## Images
### There are images.
- Red and green represent `animals`. Green indicates a mutation."
- black is `predator`
- pink is `food`
![](/_images/github_image1.png)
![](/_images/github_image2.png)
![](/_images/github_image3.png)


## Installation

### For download this project you need to download `pygame` with the following command:
1. For Linux: `pip install pygame`
2. For windows: go to *https://www.pygame.org* then find download, then press to download pygame


## Usage

### To use this project, run the `main.py` file after downloading `pygame`.


## How to play

### After downloading `pygame` and running the `main.py` file, you can observe how creatures develop, reproduce, die, and eat.


## Logs

### This project includes a `logs.txt` file containing information about the creation and death of creatures, food, etc. After starting the game, the `logs.txt` are cleared.
### This project has `logs2.txt` contains creature and food population graph.
### `Be careful when using this log because it is not cleared and may fill up your computer's memory!`
### To use `logs2.txt`, you need to uncomment the following code in the main.py file:
```py
#if Const.STEP % 25 == 0:
#    with open('logs2.txt', 'a') as logs2:
#        logs2.write(round(len(List.animals)/10) * 'A' + ' | ' + round(len(List.predators)/10) * 'P' + ' | ' + round(len(List.foods)/10) * 'F')
#        logs2.write('\n')
```
