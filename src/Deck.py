from src.Card import *
import random as rd


class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for v in range(1, 14):
                newCard = Card(v, s)
                self.deck.append(newCard)

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
        else:
            return None

    def removeTopCard(self):
        if len(self.deck) > 0:
            self.deck.remove(self.deck[0])
        else:
            raise Exception("Cannot remove a card from an empty deck.")

    def sendToBack(self, card):
        if card not in self.deck:
            self.deck.append(card)
        else:
            raise Exception("Cannot add a duplicate into the deck.")
