from top import *

class Player():
    def __init__(self,id):
        self.id = id
        self.score = 0

    def getAction(self):
        if self.id == "1":
            self.inputs = [pg.key.get_pressed()[pg.K_w],pg.key.get_pressed()[pg.K_s]]
        elif self.id == "2":
            self.inputs = [pg.key.get_pressed()[pg.K_UP],pg.key.get_pressed()[pg.K_DOWN]]

        # up/down
        if self.inputs[0] and not self.inputs[1]: return -1.0
        elif not self.inputs[0] and self.inputs[1]: return 1.0
        else: return 0.0

    def updateScore(self,mode,amount = 0):
        if mode == "set":
            self.score = amount
        elif mode == "add":
            self.score += amount
        elif mode == "get":
            return self.score

        

player1 = Player("1")
player2 = Player("2")
