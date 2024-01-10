import pygame as pg
import numpy as np
import csv
import random
import math
import torch
from collections import deque

# Application
# seed = 1
# random.seed(seed)
# torch.manual_seed(seed)

appDim = (1000, 700)

backgroundColor = (160,82,45)
caption = "Pong"

# Functional
app = pg.display.set_mode(appDim)
pg.display.set_caption(caption)
EXIT = False

# Visual

# Game
steps = 0
terminalCount = 0

doRender, kPressed, rPressed = True, False, False


def controlAndReset(k,r,ball,paddle1,paddle2,steps):
    global doRender, kPressed, rPressed
    if k:
        if not kPressed:
            kPressed = True 
            if doRender: doRender = False
            else: doRender = True
    else:
        kPressed = False
        
    if doRender:
        pg.display.update()
        pg.time.Clock().tick(10)

    # Reset?
    if r:
        if not rPressed:
            rPressed = True
            paddle1.reset()
            paddle2.reset()
            ball.reset()
            print(f"step {steps}: Manual reset")
    else:
        rPressed = False