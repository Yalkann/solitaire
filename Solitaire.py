from src.Game import *
from src.TextInterface import *
from src.AI_algo import *

if __name__ == "__main__":
    game = Game()
    ai = AI_algo()
    textInter = TextInterface(game, ai)
    results.append(textInter.getGameResult())
