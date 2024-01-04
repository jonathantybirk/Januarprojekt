import pygame as pg
import random as rand

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
score = 0
def updateScore(mode,amount):
    global score
    if mode == "set":
        score = amount
    elif mode == "add":
        score += amount
    elif mode == "get":
        return score
        
    #print(f"score: {score}")

def checkLoss(ball,paddle1,paddle2,AI1,AI2):
    if ball.pos[0] <= -(squares[0] - 1) / 2 or ball.pos[0] >= (squares[0] - 1) / 2:
        paddle1.reset()
        paddle2.reset()
        ball.reset()
        updateScore("add",0)

        AI1.isTerminal = True
        AI2.isTerminal = True

        return True
    else:
        AI1.isTerminal = False
        AI2.isTerminal = False

        return False


def step():
    pass