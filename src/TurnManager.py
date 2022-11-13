class TurnManager:
    def __init__(self):
        pass

    def getActions(self):
        sourceStack, sourceStackIndex, cardIndex = None, None, None

        while sourceStack == None or sourceStack not in ["S", "T", "F"]:
            sourceStack = input(
                "Select where to pick a stack from: S (Stock), T (Table), F (Foundation).\n"
            )
            if sourceStack not in ["S", "T", "F"]:
                print(
                    "Error: Expected S (Stock), T (Table) or F (Foundation) but got ",
                    sourceStack,
                    ".",
                )

        if sourceStack == "T":
            while (
                sourceStackIndex == None or sourceStackIndex < 0 or sourceStackIndex > 6
            ):
                sourceStackIndex = int(input("Select what stack to pick from: 0-6.\n"))
                if sourceStackIndex < 0 or sourceStackIndex > 6:
                    print("Error: Expected 0-6 but got ", cardIndex, ".")

            while cardIndex == None or cardIndex < 0:
                cardIndex = int(
                    input("Select a card index to pick from: 0 or greater.\n")
                )
                if cardIndex < 0:
                    print("Error: Expected 0 or greater but got ", cardIndex, ".")

        elif sourceStack == "F":
            while (
                sourceStackIndex == None or sourceStackIndex < 0 or sourceStackIndex > 3
            ):
                sourceStackIndex = int(input("Select what stack to pick from: 0-3.\n"))
                if sourceStackIndex < 0 or sourceStackIndex > 3:
                    print("Error: Expected 0-3 but got ", sourceStackIndex, ".")

        return [sourceStack, sourceStackIndex, cardIndex]
