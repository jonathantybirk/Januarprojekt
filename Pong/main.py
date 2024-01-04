from ai import *

# LOOP
steps = 0
def step():
    global steps
    steps += 1
    # paddles
    paddle1.move()
    paddle2.move()

    # Ball
    ball.collide()
    ball.move()

    # Game
    checkLoss(ball,paddle1,paddle2,AI1,AI2)

while not EXIT:
    # Exit
    for event in pg.event.get():
        if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_ESCAPE]:
            EXIT = True

    # AIs log state
    AI1.getState()
    AI2.getState()

    # Get NN to provide action or take random action
    paddle1.movement = AI1.getAction()
    paddle2.movement = AI2.getAction()

    # Step to next tick
    step()

    # AIs update log
    AI1.updateLog(0)
    AI2.updateLog(0)

    # Draw background (and clear screen)
    app.fill(backgroundColor)
    drawGrid()

    # paddles and ball
    paddle1.draw()
    paddle2.draw()
    ball.draw()

    # Misc
    pg.display.update()
    pg.time.Clock().tick(5)