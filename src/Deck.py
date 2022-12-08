from src.Card import *
import random as rd


class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITES:
            for v in range(1, 14):
                newCard = Card(v, s)
                self.deck.append(newCard)

    def __str__(self):
        str = "Deck size: " + str(len(self.deck)) + "\n"
        for c in self.deck:
            str += "(" + str(c[0]) + "," + str(c[1]) + ")" + "\n"
        return str

    def setShuffleSeed(self, seed):
        rd.seed(seed)

    def shuffle(self):
        rd.shuffle(self.deck)

    def getDeck(self):
        return self.deck

    def getDeckLen(self):
        return len(self.deck)

    def isEmpty(self):
        return len(self.deck) == 0

    def getTopCard(self):
        if len(self.deck) > 0:
            return self.deck[0]

    def removeTopCard(self):
        if len(self.deck) > 0:
            self.deck.remove(self.deck[0])
        else:
            raise Exception("Cannot remove a card from an empty deck.")

    def addToBack(self, card):
        if card not in self.deck:
            self.deck.append(card)
        else:
            raise Exception("Cannot add a duplicate into the deck.")
