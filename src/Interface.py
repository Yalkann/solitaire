from src.Game import *


class Interface:
    def run(self, game):
        pass

    def __init__(self):
        game = Game()
        self.run(game)
