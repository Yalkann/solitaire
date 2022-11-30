from src.Game import *


class TurnManager:
    def getTurnAction(self, game: Game):
        sourceStack, sourceStackIndex, cardIndex = None, None, None

        while sourceStack == None or sourceStack not in ["D", "S", "T", "F"]:
            sourceStack = input(
                "Select where to pick from: D (Draw), S (Stock), T (Table), F (Foundation).\n"
            )
            if sourceStack not in ["D", "S", "T", "F"]:
                print(
                    "Error: Expected D (Draw), S (Stock), T (Table) or F (Foundation) but got {}.".format(
                        sourceStack
                    )
                )

        if sourceStack == "T":
            while (
                sourceStackIndex == None or sourceStackIndex < 0 or sourceStackIndex > 6
            ):
                sourceStackIndex = int(input("Select what stack to pick from: 0-6.\n"))
                if sourceStackIndex < 0 or sourceStackIndex > 6:
                    print("Error: Expected 0-6 but got {}.".format(sourceStackIndex))

            maxIndex = len(game.getTable()[sourceStackIndex].getListFromStack(0)) - 1
            while cardIndex == None or cardIndex < 0 or cardIndex > maxIndex:
                cardIndex = int(
                    input("Select a card index to pick from: 0-{}.\n".format(maxIndex))
                )
                if cardIndex < 0 or cardIndex > maxIndex:
                    print(
                        "Error: Expected 0-{} but got {}.".format(maxIndex, cardIndex)
                    )

        elif sourceStack == "F":
            while (
                sourceStackIndex == None or sourceStackIndex < 0 or sourceStackIndex > 3
            ):
                sourceStackIndex = int(input("Select what stack to pick from: 0-3.\n"))
                if sourceStackIndex < 0 or sourceStackIndex > 3:
                    print("Error: Expected 0-3 but got {}.".format(sourceStackIndex))

        return [sourceStack, sourceStackIndex, cardIndex]
