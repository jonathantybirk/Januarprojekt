from paddles import *

class Ball:
    def __init__(self):
        self.speed = 1
        self.pos = [0,0]
        self.velocity = [rand.choice([-1,1]),rand.choice([-1,1])]

        self.color = (255,255,255)
        self.dim = [1,1]

        self.drawPos = [0,0]

    def collide(self):
        # Bounds
        if self.pos[1] <= -(squares[1] - 1) / 2:
            self.velocity[1] = 1
        if self.pos[1] >= (squares[1] - 1) / 2:
            self.velocity[1] = -1

        # paddle 1
        if self.pos[0] <= paddle1.pos[0] and self.pos[1] >= paddle1.pos[1] - (paddle1.dim[1] - 1) / 2 and self.pos[1] <= paddle1.pos[1] + (paddle1.dim[1] - 1) / 2:
            if self.pos[1] == paddle1.pos[1] - (paddle1.dim[1] - 1) / 2:
                self.velocity = [1, -1]
            elif self.pos[1] == paddle1.pos[1] + (paddle1.dim[1] - 1) / 2:
                self.velocity = [1, 1]
            elif self.pos[1] == paddle1.pos[1]:
                self.velocity = [1, 0]
            self.pos[0] = paddle1.pos[0] + 1
            updateScore("add",1)

        # paddle 2
        if self.pos[0] >= paddle2.pos[0] and self.pos[1] >= paddle2.pos[1] - (paddle2.dim[1] - 1) / 2 and self.pos[1] <= paddle2.pos[1] + (paddle2.dim[1] - 1) / 2:
            if self.pos[1] == paddle2.pos[1] - (paddle2.dim[1] - 1) / 2:
                self.velocity = [-1, -1]
            elif self.pos[1] == paddle2.pos[1] + (paddle2.dim[1] - 1) / 2:
                self.velocity = [-1, 1]
            elif self.pos[1] == paddle2.pos[1]:
                self.velocity = [-1, 0]
            self.pos[0] = paddle2.pos[0] - 1
            updateScore("add",1)

    def move(self):
        self.pos[0] += self.velocity[0] * self.speed
        self.pos[1] += self.velocity[1] * self.speed

    def reset(self):
            self.pos = [0,0]
            self.velocity = [rand.choice([-1,1]),rand.choice([-1,0,1])]

    def draw(self):
        self.drawDimFactor = 50
        self.drawDimSubtraction = 10
        self.drawPosFactor = 50

        self.drawDim = [self.dim[0] * self.drawDimFactor - self.drawDimSubtraction, self.dim[1] * self.drawDimFactor - self.drawDimSubtraction]
        self.drawPos = [self.pos[0] * self.drawPosFactor + appDim[0] / 2 - self.drawDim[0] / 2, self.pos[1] * self.drawPosFactor + appDim[1] / 2 - self.drawDim[1] / 2]
        pg.draw.rect(app,self.color,[self.drawPos[0],self.drawPos[1],self.drawDim[0],self.drawDim[1]])

ball = Ball()