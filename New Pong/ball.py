from paddles import *

class Ball:
    def __init__(self):
        self.initSpeed = 3
        self.speedUp = 0.1
        self.maxSpeed = 15
        self.initPos = [0,0]

        self.color = (255,255,255)
        self.dim = [5,10]

        self.speed = 0
        self.pos = [0,0]
        self.direction = [0,0]
        self.velocity = [0,0]
        self.reset()

    def collideBounds(self,AI1,AI2):
        # Bounds
        # ceiling/floor
        if self.pos[1] - self.dim[1] / 2 <= -appDim[1] / 2:
            self.pos[1] = -appDim[1] / 2 + self.dim[1] / 2
            self.direction[1] = abs(self.direction[1])
        elif self.pos[1] + self.dim[1] / 2 >= appDim[1] / 2:
            self.pos[1] = appDim[1] / 2 - self.dim[1] / 2
            self.direction[1] = -abs(self.direction[1])

        # left / right
        if self.pos[0] < -appDim[0] / 2:
            paddle1.reset()
            paddle2.reset()
            self.reset()

            AI1.isTerminal = 1
            AI2.isTerminal = 1

        elif self.pos[0] > appDim[0] / 2:
            paddle1.reset()
            paddle2.reset()
            self.reset()

            AI1.isTerminal = 1
            AI2.isTerminal = 1
        
        else:
            AI1.isTerminal = 0
            AI2.isTerminal = 0


    def collidePaddles(self):
        # Left paddle
        if self.pos[0] + self.dim[0] / 2 >= paddle1.pos[0] - Paddle.dim[0] / 2 and self.pos[0] - self.dim[0] / 2 <= paddle1.pos[0] + Paddle.dim[0] / 2:
            if self.pos[1] + self.dim[1] / 2 >= paddle1.pos[1] - Paddle.dim[1] / 2 and self.pos[1] - self.dim[1] / 2 <= paddle1.pos[1] + Paddle.dim[1] / 2:
                
                self.pos[0] = paddle1.pos[0] + Paddle.dim[0] / 2 + self.dim[0]

                collisionAngle = (math.pi / 3) * (self.pos[1] - paddle1.pos[1]) / ((Paddle.dim[1] + self.dim[1]) / 2)
                self.direction = [math.cos(collisionAngle), math.sin(collisionAngle)]
                
                self.speed = min(self.speed + self.speedUp, self.maxSpeed)
                player1.updateScore("add", 1)

        # Right paddle
        elif self.pos[0] + self.dim[0] / 2 >= paddle2.pos[0] - Paddle.dim[0] / 2 and self.pos[0] - self.dim[0] / 2 <= paddle2.pos[0] + Paddle.dim[0] / 2:
            if self.pos[1] + self.dim[1] / 2 >= paddle2.pos[1] - Paddle.dim[1] / 2 and self.pos[1] - self.dim[1] / 2 <= paddle2.pos[1] + Paddle.dim[1] / 2:
                
                self.pos[0] = paddle2.pos[0] - Paddle.dim[0] / 2 - self.dim[0]
                
                collisionAngle = (math.pi / 3) * (self.pos[1] - paddle2.pos[1]) / ((Paddle.dim[1] + self.dim[1]) / 2)
                self.direction = [-math.cos(collisionAngle), math.sin(collisionAngle)]
                
                self.speed = min(self.speed + self.speedUp, self.maxSpeed)
                player2.updateScore("add", 1)

    def move(self):
        self.velocity[0] = self.direction[0] * self.speed
        self.velocity[1] = self.direction[1] * self.speed

        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

    def draw(self):
        drawPos = [self.pos[0] + (appDim[0] - self.dim[0]) / 2, self.pos[1] + (appDim[1] - self.dim[1]) / 2]
        pg.draw.rect(app,self.color,[drawPos[0],drawPos[1],self.dim[0],self.dim[1]])
    
    def reset(self):
        self.pos[0] = self.initPos[0]
        self.pos[1] = self.initPos[1]
        self.speed = self.initSpeed

        angle = random.uniform(-math.pi / 3, math.pi / 3)
        self.direction = [random.sample([-math.cos(angle),math.cos(angle)],1)[0], math.sin(angle)]


ball = Ball()