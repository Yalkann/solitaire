from src.AI import *
from time import sleep


class AI_algo(AI):
    def getTurnAction(self, game: Game):
        action = None
        history = game.getHistory()
        stock = game.getStock()
        sleep(1)

        if len(history) == 0:
            action = ["D", None, None]
            game.appendHistory(action)
            return action
