from src.Board import *


class Game(Board):
    def getClosestStack(self, card, isSingle):
        # returns [stack, stackindex] ex: stack = "T", "F"
        pass

    def isOppositeColor(self, card1, card2):
        return (
            card1.getCard()[1] in RED
            and card2.getCard()[1] in BLACK
            or card1.getCard()[1] in BLACK
            and card2.getCard()[1] in RED
        )

    def move(self, actions):
        if actions[0] == "S":
            if self.isTopCardRevealed():
                card = self.stock.getTopCard()
                (stack, stackIndex) = self.getClosestStack(card, True)
                if stack == "T":
                    self.moveCardToStack(card, self.table[stackIndex])
                    self.addToHiddenTable(stackIndex, 1)
                    return True
                elif stack == "F":
                    self.moveCardToStack(card, self.foundation[stackIndex])
                    return True
        elif actions[0] == "T":
            pass
        elif actions[0] == "F":
            pass
        return False

    def draw(self):
        pass

    def isFinished(self):
        pass

    def isWon(self):
        return self.foundation == [(13, s) for s in SUITES]
