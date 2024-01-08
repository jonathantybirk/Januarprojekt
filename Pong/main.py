from ai import *
AI1.loadWeights()
AI2.loadWeights()

# LOOP
def step():
    # paddles
    paddle1.move()
    paddle2.move()

    # Ball
    ball.collide()
    ball.move()

    # Game
    checkLoss(ball,paddle1,paddle2,AI1,AI2)

#AI1.getBatch()
while not EXIT:
    # Exit
    for event in pg.event.get():
        if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
            EXIT = True
            AI1.saveWeights()
            AI2.saveWeights()

    # AIs log state
    AI1.loadState()
    AI2.loadState()

    # Get NN to provide action or take random action
    paddle1.movement = AI1.getAction()
    paddle2.movement = AI2.getAction()

    # Step to next tick
    step()
    steps += 1

    # AIs update Batch
    AI1.updateBatch(AI1.getAction())
    AI2.updateBatch(AI2.getAction())

    # Draw background (and clear screen)
    app.fill(backgroundColor)
    drawGrid()

    # paddles and ball
    paddle1.draw()
    paddle2.draw()
    ball.draw()

    AI1.updateWeights()
    AI2.updateWeights()

    print(AI1.epsilon)

    # Misc
    pg.display.update()
    pg.time.Clock().tick(10)