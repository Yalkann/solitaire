from src.Interface import *
from src.TurnManager import *


class TextInterface(Interface):
    def run(self, game):
        tm = TurnManager()
        while not (game.isFinished()):
            game.printBoard()
            legalMove = None
            while legalMove == None or legalMove == False:
                actions = tm.getActions()
                legalMove = game.move(actions)
                if not (legalMove):
                    print("Error: illegal Move.")

        if game.isWon():
            print("\nGG\n")
        else:
            print("\nDOMMAGE\n")
