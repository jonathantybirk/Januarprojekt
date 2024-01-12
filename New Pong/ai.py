from ball import *

## Variables
learning_rate=1e-4
N,D_in,H,D_out=32,6,200,3
gamma=0.99
lr=.01

# Define model
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.lin1=torch.nn.Linear(D_in,H)
        self.activation=torch.nn.ReLU()
        self.lin2=torch.nn.Linear(H,D_out)

    def forward(self, x):
        x = self.lin1(x) 
        x = self.activation(x)
        x = self.lin2(x)
        return x

# ## Define loss function
loss_fn = torch.nn.MSELoss(reduction='sum')

# Define model
model=Model()

modelName = "Distance-penalty"

class AI:
    isTerminal = 0
    def __init__(self,id):

        self.id = id
        self.entry = []
        self.batch = deque(maxlen = 100000)
        self.batchSize = 0

        self.players = {"1": player1, "2": player2}
        self.paddles = {"1": paddle1, "2": paddle2}

        #Randomness factors
        self.epsilon = 0.3
        self.epsilon_decay = 0.0000000
        self.minimum_epsilon = 0.1

        self.model = Model()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=learning_rate)


        self.weightPath = f"New Pong/Models/{modelName}/{self.id}.pt"

    def loadState(self):
        self.state = [paddle1.pos[1] / (appDim[1] / 2), paddle2.pos[1] / (appDim[1] / 2), ball.pos[0] / (appDim[0] / 2), ball.pos[1] / (appDim[1] / 2), ball.velocity[0] / (appDim[0] / 2), ball.velocity[1] / (appDim[1] / 2)]
        self.totalReward = self.players[self.id].score

    def updateBatch(self,action):
        self.newState = [paddle1.pos[1] / (appDim[1] / 2), paddle2.pos[1] / (appDim[1] / 2), ball.pos[0] / (appDim[0] / 2), ball.pos[1] / (appDim[1] / 2), ball.velocity[0] / (appDim[0] / 2), ball.velocity[1] / (appDim[1] / 2)]
        self.newTotalReward = self.players[self.id].score
        self.reward = self.newTotalReward - self.totalReward
        self.entry = [self.state[0],self.state[1],self.state[2],self.state[3],self.state[4],self.state[5],action,self.reward,
                      self.newState[0],self.newState[1],self.newState[2],self.newState[3],self.newState[4],self.newState[5],self.isTerminal]

        self.batch.append(self.entry)
        self.batchSize += 1

    def getAction(self):
        if self.epsilon > self.minimum_epsilon:
            self.epsilon -= self.epsilon_decay / 2

        if random.uniform(0,1) < self.epsilon:

            return random.sample([-1,0,1],1)[0]
        
        else:
            modelInput = torch.tensor(self.state)

            return torch.argmax(self.model(modelInput)).item() - 1
        
    def loadWeights(self):
        try:
            checkpoint = torch.load(self.weightPath)
            self.model.load_state_dict(checkpoint['model_state_dict'])
            self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        except:
            pass

    def saveWeights(self):
        torch.save({
        'model_state_dict': self.model.state_dict(),
        'optimizer_state_dict': self.optimizer.state_dict()
        }, self.weightPath)
        
    def updateWeights(self):
        if self.batchSize > N:
            minibatch = torch.tensor(random.sample(self.batch,N))
            states = minibatch[:,0:6]
            newStates = minibatch[:,8:14]
            rewards = minibatch[:,7]
            TerminalCheck=minibatch[:,14]
            actions=minibatch[:,6].long()
            modelOutput_states = self.model(states)

            y_pred = modelOutput_states[np.arange(N),actions.reshape(1,N)]            
            with torch.no_grad():
                newStatesQuality = (torch.max(model(newStates),dim=1).values * (1 - TerminalCheck)).unsqueeze(0)
                y_true = rewards + gamma * newStatesQuality
                
            loss = loss_fn(y_pred,y_true)

            # update weights
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

AI1 = AI("1")
AI2 = AI("2")