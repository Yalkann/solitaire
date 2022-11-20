SUITES = (
    "Clubs",
    "Hearts",
    "Spades",
    "Diamonds",
)
RED = ("Hearts", "Diamonds")
BLACK = ("Clubs", "Spades")


class Card:
    def __init__(self, value, suite):
        self.value = None
        self.suite = None
        if suite not in SUITES:
            raise Exception("Fatal error: No such card suit name.")
        elif value < 1 or value > 13:
            raise Exception("Fatal error: No such card value.")
        else:
            self.value = value
            self.suite = suite

    def __str__(self):
        return "(" + str(self.value) + "," + str(self.suite) + ")"

    def getCard(self):
        return (self.value, self.suite)

    def getValue(self):
        return self.value

    def getSuite(self):
        return self.suite
