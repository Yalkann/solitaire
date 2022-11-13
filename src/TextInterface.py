from src.Interface import *
from src.TurnManager import *


class TextInterface(Interface):
    def run(self, game):
        tm = TurnManager()
        while not (game.isFinished()):
            game.printBoard()
            actions = tm.getActions()

        if game.isWon():
            print("\nGG\n")
        else:
            print("\nDOMMAGE\n")
