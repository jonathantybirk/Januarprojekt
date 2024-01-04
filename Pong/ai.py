from ball import *
import random
import numpy as np
import torch

## Variables
epsilon=1
epsilon_decay=0.00001
learning_rate=1e-4
N,D_in,H,D_out=100,5,100,3

## Model definition
model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out),
)
## Loss function definition
loss_fn = torch.nn.MSELoss(reduction='sum')


class AI:
    def __init__(self,id):
        self.discount = 0.99
        self.id = id
        self.log = []
        self.isTerminal = False
        self.batch=[]

    def getState(self):
        self.state = torch.tensor([paddle1.pos[1], paddle2.pos[1], ball.pos[0], ball.pos[1], ball.velocity[0], ball.velocity[1]])
        self.totalReward = updateScore("get",0)

    def updateLog(self,action):
        self.newState = torch.tensor([paddle1.pos[1], paddle2.pos[1], ball.pos[0], ball.pos[1], ball.velocity[0], ball.velocity[1]])
        self.newTotalReward = updateScore("get",0)
        self.reward = self.newTotalReward - self.totalReward
        entry = [self.state,action,self.reward,self.newState,self.isTerminal]
        self.log.append(entry)

        if checkLoss(ball,paddle1,paddle2,AI1,AI2):
             self.batch.append(self.log)
             self.log=[]

    def getAction(self):
        sample=np.random.uniform(low=0,high=1,size=1)
        if sample<epsilon:
            return random.sample([-1,0,1],1)[0]
        else:
            pass
            #return torch.argmax(model(miniBatch)) - 1
            

            
    def updateWeights(self):
            pass
    

    # def calculateQuality(self):
    #     self.reversedLog = list(reversed(self.log))
    #     self.reversedQualityList = [self.reversedLog[0][2]]

    #     for i in range(1,len(self.reversedLog)):
    #         quality = self.reversedLog[i][2] + self.discount * self.reversedQualityList[i - 1]
            
    #         self.reversedQualityList.append(quality)

    #     self.qualityList = list(reversed(self.reversedQualityList))

    #     print(self.qualityList)

AI1 = AI("1")
AI2 = AI("2")
