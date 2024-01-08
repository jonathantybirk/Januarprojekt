import pygame as pg
import random
import torch
from collections import deque

#A seed for easy reproduction Oo
#random.seed(1)
#torch.manual_seed(1)
# Application
squares = [19,13]
squareSize = 50

appDim = (squares[0] * squareSize, squares[1] * squareSize)

backgroundColor = (15,15,20)
caption = "Pong"

# Functional
app = pg.display.set_mode(appDim)
pg.display.set_caption(caption)
global EXIT
EXIT = False

# Visual
def drawGrid():
    color = (100,100,100)
    width = 2
    for i in range(1, squares[0]):
        x = i * squareSize
        pg.draw.rect(app, color,[x - width / 2, 0, width, appDim[1]])
    for i in range(1, squares[1]):
        y = i * squareSize
        pg.draw.rect(app, color,[0,y - width / 2, appDim[0], width])

# Game
scores = {"1": 0, "2": 0}
totalScores = {"1": 0, "2": 0}

def updateScore(id,mode,amount):
    global scores
    global totalScores

    if mode == "set":
        scores[id] = amount
    elif mode == "add":
        scores[id] += amount
        totalScores[id] += amount
    elif mode == "get":
        return scores[id]

def checkLoss(ball,paddle1,paddle2,AI1,AI2):
    if ball.pos[0] <= -(squares[0] - 1) / 2 or ball.pos[0] >= (squares[0] - 1) / 2:
        paddle1.reset()
        paddle2.reset()
        ball.reset()
        updateScore("1","set",0)
        updateScore("2","set",0)

        AI1.isTerminal = 1
        AI2.isTerminal = 1

    else:
        AI1.isTerminal = 0
        AI2.isTerminal = 0

steps = 0