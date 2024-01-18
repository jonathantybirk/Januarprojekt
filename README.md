The code, data, and report in this directory is the results of a 3-week group project for the 02461 Introduction to Intelligens Systems first-year course for the BSc Artificial Intelligence and Data study line at DTU.

The report can be read in the file 'Report.pdf', linked here: ''link''

In this report, we tested the ability of two Deep Q-learning models to cooporate with each other to keep a Pong game going. For four different model types, two instances controlling a paddle each were rewarded when specifically they hit the ball. As input every game step, the instances received the position of their own paddle as well as the position and velocity of the ball. The four models were as such:

1. Blind-Base, as described above
2. Blind-Nudge. as described above with an additional small reward when the other instance's paddle hits the ball.
3. Sighted-Base, as described above with an additional input, the position of the other instance's paddle
4. Sighted-Nudge, as described above with both the additional reward and the additional input

# The code: an overview
In this diretory, you will find two subfolders: "Old Pong", and "New Pong".
  Old Pong was our first try at a simple Pong Game. It is not relevant for our report.

In the New Pong folder, the code for the game as well as training the models and collecting data can be found.
top.py, players.py, paddles.py, and ball.py encodes the Pong game with its rules and mechanics.
ai.py trains the utilizes the model instances.
main.py runs the game and collects data.

Additionally, a folder named after each model can be found, consisting of a data.csv file used for analysis, as well as 1.pt and 2.pt containing the weights and biases of the model instances controlling the left and right paddle respectively.

# Testing a model
A model can be selected for testing or futher training by setting the variable 'modelName' in ai.py to he name of the model. As the blind model instances each take one fewer input, when loading this one, the first two indeces in 'self.state' and 'self.newState' should be replaced by just one input: 'self.players[self.id][1]'. The indeces of 'self.entry' should be updated to reflect the fewer inputs, and the specific indeces of the 'minibach' variable should too be updated. All these variables are found in the AI class.

A model can be tested by setting the variable testMode in main.py to True. In test mode, the weights and biases of the selected model will not be updated, and there will be no exploring random actions.

In main.py, in the 'track score'-section, code for loading data to the data.csv file in the model folder can be found.

# Training a model
The inputs of the model can be customized in the relevant variables described in the first paragraph in the section above. In addition, the model parameters can be tweaked.
'N', 'D_in', 'H', 'D_out', respectively: The size of the minibatches, number of inputs, number of neurons in the hidden layers, number of outputs. These parameters are found just above the Model class.

In the Model class, the hidden layers can be specified. Under the Model class, the specific loss-function used can be specified.

In the AI class, the 'self.epsilon' value can be chosen. This is the likelihood that the agent will take and record a random action instead of the top suggestion by the model Additionally, a decrease per game step and a minimum epsilon that i will not decrease under can be set.

# Thanks for reading, we hope you find our projecect and research interesting. :)

- Christoffer, Jonathan, and Viktor













