from src.Game import *
from src.AI import *


class Interface:
    def run(self, game: Game, ai: AI):
        pass

    def __init__(self, game: Game, ai: AI = None):
        self.result = self.run(game, ai)

    def getGameResult(self):
        return self.result
