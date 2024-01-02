from players import *

class Ball:
    def __init__(self):
        self.speed = 0.5
        self.pos = [0,0]
        self.velocity = [rand.choice([-1,1]),rand.choice([-1,0,1])]

        self.color = (255,255,255)
        self.dim = [1,1]

        self.drawPos = [0,0]

        self.score = 0

    def collide(self):
        # Bounds
        if self.pos[1] == -(squares[1] - 1) / 2 or self.pos[1] == (squares[1] - 1) / 2:
            self.velocity[1] *= -1

        # player 1
        if self.pos[0] <= players[0].pos[0] and self.pos[1] >= players[0].pos[1] - (players[0].dim[1] - 1) / 2 and self.pos[1] <= players[0].pos[1] + (players[0].dim[1] - 1) / 2:
            if self.pos[1] == players[0].pos[1] - (players[0].dim[1] - 1) / 2:
                self.velocity = [1, -1]
            elif self.pos[1] == players[0].pos[1] + (players[0].dim[1] - 1) / 2:
                self.velocity = [1, 1]
            elif self.pos[1] == players[0].pos[1]:
                self.velocity = [1, 0]
            self.pos[0] = players[0].pos[0] + 1
            self.updateScore(1)

        # player 2
        if self.pos[0] >= players[1].pos[0] and self.pos[1] >= players[1].pos[1] - (players[1].dim[1] - 1) / 2 and self.pos[1] <= players[1].pos[1] + (players[1].dim[1] - 1) / 2:
            if self.pos[1] == players[1].pos[1] - (players[1].dim[1] - 1) / 2:
                self.velocity = [-1, -1]
            elif self.pos[1] == players[1].pos[1] + (players[1].dim[1] - 1) / 2:
                self.velocity = [-1, 1]
            elif self.pos[1] == players[1].pos[1]:
                self.velocity = [-1, 0]
            self.pos[0] = players[1].pos[0] - 1
            self.updateScore(1)

    def move(self):
        self.pos[0] += self.velocity[0] * self.speed
        self.pos[1] += self.velocity[1] * self.speed

    def lose(self):
        if self.pos[0] < -(squares[0] - 1) / 2 or self.pos[0] > (squares[0] - 1) / 2 or self.score == 20:
            for player in players:
                player.reset()
            self.pos = [0,0]
            self.velocity = [rand.choice([-1,1]),rand.choice([-1,0,1])]
            self.score = 0
            self.updateScore(0)

    def draw(self):
        self.drawDimFactor = 50
        self.drawDimSubtraction = 10
        self.drawPosFactor = 50

        self.drawDim = [self.dim[0] * self.drawDimFactor - self.drawDimSubtraction, self.dim[1] * self.drawDimFactor - self.drawDimSubtraction]
        self.drawPos = [round(self.pos[0]) * self.drawPosFactor + appDim[0] / 2 - self.drawDim[0] / 2, round(self.pos[1]) * self.drawPosFactor + appDim[1] / 2 - self.drawDim[1] / 2]
        pg.draw.rect(app,self.color,[self.drawPos[0],self.drawPos[1],self.drawDim[0],self.drawDim[1]])

    def updateScore(self,amount):
        self.score += amount
        print(f"score: {self.score}")

ball = Ball()