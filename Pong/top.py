import pygame as pg
import random as rand

# Application
squares = [15,13]
squareSize = 50

appDim = (squares[0] * squareSize, squares[1] * squareSize)

backgroundColor = (15,15,20)
caption = "Collisions"

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