from src.Interface import *
from src.TurnManager import *


class TextInterface(Interface):
    def run(self, game, ai):
        tm = TurnManager()
        while not (game.isFinished()):
            game.printBoard()
            legalMove = None
            while legalMove == None or legalMove == False:
                if ai == None:
                    actions = tm.getTurnAction(game)
                else:
                    actions = ai.getTurnAction(game)
                moveError = game.move(actions)
                legalMove = moveError == None
                if moveError != None:
                    print(moveError, ": illegal Move.", sep="")

        if game.isWon():
            print("\nGG\n")
        else:
            print("\nDOMMAGE\n")
