# BubblePhysics-Education

BubblePhysics-Education is a feature in the sandbox-game [BubblePhysics](https://zenonet.itch.io/bubblephysics) which allows you to control the player autonomously using a TCP-Connection.<br>
The game side is part of any version of bubble physics >= 0.8. The feature is available on Linux, Windows and Android.

## Installation

The TCP-Functionality is built into BubblePhysics itself so you just need to download/install BubblePhysics from [itch.io](https://zenonet.itch.io/bubblephysics/download/oyaAxQJGwXlQ__hdlvmyrp7lCZ6xlvOxQGmtpaO2)<br>
Note that you need to use a desktop build because in most browsers, websites aren't able to create TCP-Servers.

If you want to download the library automatically or using `curl`, here is the direct link to the file: https://raw.githubusercontent.com/zenonet/BubblePhysics-Education/main/BubblePhysics.py

## Python Library

To make it easier, you can use a Python-Library that automatically connects to the TCP-Server and allows for easy control over the game.
The library is a single python file, which you can find [here](https://github.com/zenonet/BubblePhysics-Education/blob/main/BubblePhysics.py).<br>
It isn't on pip right now, so just copy the file to the folder where you have your so

### Quick Start

**To start automating BubblePhysics, follow these steps:**

* Download a desktop build of BubblePhysics (min version 0.8)
* Start a game of BubblePhysics (preferably sandbox mode)
* Go into the pause menu (ESC)
* Click on *Start TCP-Server*
* Put the python library into a directory with your python source file
* Paste this code into your source file:
```python3
from BubblePhysics import *
from time import sleep

# Connect to local host on port 26541 (the standard BubblePhysics port)
connect()

while True:
    move((0, -0.2))
    sleep(0.5)
    move((0, 0.2))
    sleep(0.5)
```
