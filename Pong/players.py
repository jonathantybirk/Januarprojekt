from top import *

class Player:
    def __init__(self,position,id):
        self.initPos = position
        self.speed = 1
        self.color = (255,255,255)
        self.dim = [1,3]

        self.pos = list(position)
        self.id = id

        self.inputs = [0,0,0,0]
        self.movement = [0,0]

    def control(self):
        if self.id == "1":
            self.inputs = [pg.key.get_pressed()[pg.K_w],pg.key.get_pressed()[pg.K_s]]
        elif self.id == "2":
            self.inputs = [pg.key.get_pressed()[pg.K_UP],pg.key.get_pressed()[pg.K_DOWN]]

        # up/down
        if self.inputs[0] and not self.inputs[1] and self.pos[1] > -(squares[1] - 1) / 2 + 1: self.movement[1] = -1
        elif not self.inputs[0] and self.inputs[1] and self.pos[1] < (squares[1] - 1) / 2 - 1: self.movement[1] = 1 
        else: self.movement[1] = 0

    def move(self):
        self.pos[1] += self.movement[1] * self.speed

    def draw(self):   
        self.drawDimFactor = 50
        self.drawDimSubtraction = 10
        self.drawPosFactor = 50

        self.drawDim = [self.dim[0] * self.drawDimFactor - self.drawDimSubtraction, self.dim[1] * self.drawDimFactor - self.drawDimSubtraction]
        self.drawPos = [round(self.pos[0]) * self.drawPosFactor + appDim[0] / 2 - self.drawDim[0] / 2, round(self.pos[1]) * self.drawPosFactor + appDim[1] / 2 - self.drawDim[1] / 2]
        pg.draw.rect(app,self.color,[self.drawPos[0],self.drawPos[1],self.drawDim[0],self.drawDim[1]])
    
    def reset(self):
        self.pos[1] = self.initPos[1]
        

players = [
    Player([-(squares[0] - 1) / 2 + 1, 0], "1"),
    Player([(squares[0] - 1) / 2 - 1, 0], "2")
    ]