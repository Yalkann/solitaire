SUITS = (
    "Clubs",
    "Hearts",
    "Spades",
    "Diamonds",
)


class Card:
    def __init__(self, value, suit):
        self.value = None
        self.suit = None
        if suit not in SUITS:
            raise Exception("Fatal error: No such card suit name.")
        elif value < 1 or value > 13:
            raise Exception("Fatal error: No such card value.")
        else:
            self.value = value
            self.suit = suit

    def __str__(self):
        return "(" + str(self.value) + "," + str(self.suit) + ")"

    def getCard(self):
        return (self.value, self.suit)
