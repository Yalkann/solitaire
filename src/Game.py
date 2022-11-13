from src.Board import *

ACTIONS = ["T" + str(t) for t in range(7)] + ["F" + str(f) for f in range(4)]


class Game(Board):
    def move(self, source, index, dest):
        pass

    def draw(self):
        pass

    def isFinished(self):
        pass

    def isWon(self):
        return self.foundation == [(13, s) for s in SUITS]

    def getMove(self, source, index, dest):
        pass
