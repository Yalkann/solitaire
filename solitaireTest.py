from src.Game import *
from src.TextInterface import *
from src.AI_algo import *

if __name__ == "__main__":
    nbgames = 100
    results = []

    for i in range(nbgames):
        game = Game()
        ai = AI_algo()
        textInter = TextInterface(game, ai)
        results.append(textInter.getGameResult())

    print("\n\n--------------------------------")
    print(f"nbgames: {nbgames}\nwinrate: {sum(results)/nbgames*100:.0f}%")
