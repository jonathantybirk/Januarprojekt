from ball import *

## Variables
# epsilon=0.9
# epsilon_decay=0.00001
learning_rate=1e-4
N,D_in,H,D_out=32,5,100,3
gamma=0.9
lr=.01





# Define model
class TheModelClass(nn.Module):
    def __init__(self):
        super(TheModelClass, self).__init__()
        self.lin1=nn.Linear(D_in,H)
        self.relu=nn.ReLU()
        self.lin2=nn.Linear(H,D_out)

    def forward(self, x):
        x=self.lin2(nn.ReLU(self.lin1(x)))
        return x

# Initialize model
model = TheModelClass()

# Initialize optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)



## Model definition
model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(),
    torch.nn.Linear(H, D_out),
    )
# ## Loss function definition
loss_fn = torch.nn.MSELoss(reduction='sum')

## Optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


class AI:
    def __init__(self,id):
        self.rows = 100
        self.discount = 0.99

        self.id = id
        self.entry = []
        self.batch = deque(maxlen = 10000)
        self.batchSize = 0
        self.isTerminal = 0

        self.paddles = {"1": paddle1, "2": paddle2}

        #Randomness factor
        self.epsilon = 1.0
        self.epsilon_decay = 0.00075
        self.minimum_epsilon = 0.1
        

        
    def loadState(self):
        self.state = [self.paddles[self.id].pos[1], ball.pos[0], ball.pos[1], ball.velocity[0], ball.velocity[1]]
        self.totalReward = updateScore("get",0)

    def updateBatch(self,action):
        self.newState = [self.paddles[self.id].pos[1], ball.pos[0], ball.pos[1], ball.velocity[0], ball.velocity[1]]
        self.newTotalReward = updateScore("get",0)
        self.reward = self.newTotalReward - self.totalReward
        self.entry = [self.state[0],self.state[1],self.state[2],self.state[3],self.state[4],action,self.reward,
                      self.newState[0],self.newState[1],self.newState[2],self.newState[3],self.newState[4],self.isTerminal]
        
        self.batch.append(self.entry)
        self.batchSize += 1

    def getAction(self):
        sample=random.uniform(0,1)
        if sample < self.epsilon:
            if self.epsilon > self.minimum_epsilon:
                self.epsilon -= self.epsilon_decay
            
            return random.sample([-1,0,1],1)[0]
        else:
            modelInput = torch.tensor(self.state)

            return torch.argmax(model(modelInput)).item() - 1
        
    def loadWeights(self):
        pass

    def saveWeights(self):
        pass
        
    def updateWeights(self):
        if self.batchSize > 32:
            minibatch = torch.tensor(random.sample(self.batch,N))
            states = minibatch[:,0:5]
            newStates = minibatch[:,7:12]
            
            TerminalCheck=minibatch[:,12]

            modelOutput_states = model(states)

            qPred_states = torch.empty(N,1)
            qPred_newStates = torch.empty(N,1)
            
            for i in range(N):
                qPred_states[i,0] = modelOutput_states[i,int(minibatch[i,5].item() + 1)]
                qPred_newStates[i]=max(model(newStates)[i])*(1. - TerminalCheck[i].item())

            loss = loss_fn(qPred_states,qPred_newStates)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            


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
