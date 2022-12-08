from src.Interface import *
from src.TurnManager import *


class TextInterface(Interface):
    def run(self, game, ai):
        finished = False
        tm = TurnManager()
        while not (finished):
            legalMove = None
            while legalMove == None or legalMove == False:
                if ai == None:
                    game.printBoard()
                    action = tm.getTurnAction(game)
                else:
                    # game.printBoard()
                    action = ai.getTurnAction(game)
                if action == None:
                    finished = True
                    break
                moveError = game.move(action)
                legalMove = moveError == None
                if moveError != None:
                    print(moveError, ": illegal Move.", sep="")

        # game.printBoard()
        if game.isWon():
            # print("\nGG\n")
            return True
        else:
            # print("\nDOMMAGE\n")
            return False
