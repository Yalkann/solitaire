from src.Game import *
from src.TextInterface import *
from src.AI_algo import *

if __name__ == "__main__":
    nbgames = 100
    results = []
    seed0 = 12
    # rd.seed(seed0)
    seeds = [rd.randint(0, 2 * nbgames) for _ in range(nbgames)]

    for i in range(nbgames):
        game = Game()
        game.setDeckSeed(seeds[i])
        ai = AI_algo()
        textInter = TextInterface(game, ai)
        results.append(textInter.getGameResult())

    print("\n\n--------------------------------")
    print(f"nbgames: {nbgames}\nwinrate: {sum(results)/nbgames*100:.0f}%")
