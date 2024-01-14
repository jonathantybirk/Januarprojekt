from ai import *
AI1.loadWeights()
AI2.loadWeights()

testMode = True

if testMode:
    AI1.epsilon = 0
    AI2.epsilon = 0
    
# stats
lastTotalScore = [0,0]
currentScore = [0,0]
currentScores = deque(maxlen = 1000)
avgScores = [0,0]

# init info
print()
print(f"TEST MODE: {testMode}")
print(f"epsilon:")
print(f"    init: {AI1.epsilon}")
if not testMode:
    print(f"    decay: {AI1.epsilon_decay}")
    print(f"    min: {AI1.minimum_epsilon}")
print("model:")
print(f"    name: {modelName}")
print(f"    batch size: {AI1.batchMaxLength}")
print(f"    minibatch size: {N}")
print(f"    neurons: {H}")
if testMode: print("WARNING, TEST MODE IS ON")
print()

# LOOP
def step():
    # paddles
    paddle1.move()
    paddle2.move()

    # Ball
    ball.collideBounds(AI)
    ball.collidePaddles()
    ball.move()

while not EXIT:
    # Exit
    for event in pg.event.get():
        if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
            EXIT = True
            with open(f"New Pong/Models/{modelName}/stats.csv", "a", newline="") as file:
                csv.writer(file).writerow("")
    if EXIT:
        break
    

    # AIs load state
    AI1.loadState()
    AI2.loadState()


    # Get NN to provide action or take random action
    paddle1.movement = AI1.getAction()
    paddle2.movement = AI2.getAction()

    # Step to next tick
    step()
    steps += 1

    ## Track score
    if AI.isTerminal:
        terminalCount += 1

        currentScore = [player1.score - lastTotalScore[0], player2.score - lastTotalScore[1]]
        lastTotalScore = [player1.score, player2.score]

        currentScores.append(currentScore)

        if terminalCount % 100 == 0:
            totalScores = [0,0]
            for score in currentScores:
                totalScores[0] += score[0]
                totalScores[1] += score[1]
            avgScores = [totalScores[0] / 1000, totalScores[1] / 1000]

        if terminalCount % 1000 == 0:
            with open(f"New Pong/Models/{modelName}/stats.csv", "a", newline="") as file:
                csv.writer(file).writerow([steps,terminalCount,currentScore])

    # AIs update Batch
    if not testMode:
        AI1.updateBatch(AI1.getAction())
        AI2.updateBatch(AI2.getAction())

    # Draw background (and clear screen)
    app.fill(backgroundColor)

    # paddles and ball
    paddle1.draw()
    paddle2.draw()
    ball.draw()
 
    # Update and save weights
    if steps % 10 == 0 and not testMode:
        AI1.updateWeights()
        AI2.updateWeights()

        if steps % 10000 == 0:
            AI1.saveWeights()
            AI2.saveWeights()
            print(f"step {steps}, game {terminalCount} : Weights saved, epsilon: {AI1.epsilon}, avg score: {avgScores}")

    # Misc
    controlAndReset(pg.key.get_pressed()[pg.K_k],pg.key.get_pressed()[pg.K_r],ball,paddle1,paddle2,steps)