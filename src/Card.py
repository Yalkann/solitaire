SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")


class Card:
    def __init__(self, value, suit):
        self.value = None
        self.suit = None
        if suit not in SUITS:
            quit("Fatal error: No such card suit name.")
        elif value < 1 or value > 13:
            quit("Fatal error: No such card value.")
        else:
            self.value = value
            self.suit = suit

    def getCard(self):
        return (self.value, self.suit)
