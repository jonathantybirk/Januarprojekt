from players import *



class Paddle:
    speed = 20
    dim = [10,100]
    def __init__(self,position,id,color):
        self.color = color

        self.pos = [0,0]
        self.initPos = position
        self.id = id
        self.movement = 0.
        self.reset()

    def move(self):
        self.pos[1] += self.movement * self.speed

        # Stay within bounds
        if self.pos[1] - self.dim[1] / 2 <= -appDim[1] / 2:
            self.pos[1] = -appDim[1] / 2 + self.dim[1] / 2
        elif self.pos[1] + self.dim[1] / 2 >= appDim[1] / 2:
            self.pos[1] = appDim[1] / 2 - self.dim[1] / 2

    def draw(self):
        drawPos = [self.pos[0] + (appDim[0] - self.dim[0]) / 2, self.pos[1] + (appDim[1] - self.dim[1]) / 2]
        pg.draw.rect(app,self.color,[drawPos[0],drawPos[1],self.dim[0],self.dim[1]])
    
    def reset(self):
        self.pos[0] = self.initPos[0]
        self.pos[1] = self.initPos[1]

paddle1 = Paddle([-appDim[0] / 2 + Paddle.dim[0] / 2 + 10.0, 0.0], "1", (231, 83, 71))
paddle2 = Paddle([appDim[0] / 2 - Paddle.dim[0] / 2 - 10.0, 0.0], "2", (73, 225, 71))