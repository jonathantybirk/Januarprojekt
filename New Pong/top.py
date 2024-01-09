import pygame as pg
import numpy as np
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
scores = {"1": 0, "2": 0}
totalScores = {"1": 0, "2": 0}
steps = 0


# reset, render
rPressed = False
kPressed = False
rendering = True