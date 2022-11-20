from src.Board import *


class Game(Board):
    def areOppositeColor(self, card1, card2):
        return (
            card1.getSuite() in RED
            and card2.getSuite() in BLACK
            or card1.getSuite() in BLACK
            and card2.getSuite() in RED
        )

    def getClosestStack(self, card, isSingle):
        if isSingle:
            for stack in self.getFoundation():
                if stack.getLen() == 0:
                    if card.getValue() == 1:
                        return (stack, None)
                else:
                    lastCard = stack.getLastElement()
                    if (
                        card.getValue() == lastCard.getValue() - 1
                        and card.getSuite() == lastCard.getSuite()
                    ):
                        return (stack, None)
        table = self.getTable()
        for stackIndex in range(len(table)):
            if table[stackIndex].getLen() == 0:
                if card.getValue() == 13:
                    return (table[stackIndex], stackIndex)
            else:
                lastCard = table[stackIndex].getLastElement()
                if card.getValue() == lastCard.getValue() - 1 and self.areOppositeColor(
                    card, lastCard
                ):
                    return (table[stackIndex], stackIndex)

    def move(self, actions):
        if actions[0] == "D":
            if not (self.getStock().isEmpty()):
                self.draw()
            else:
                return "stockEmptyError"

        elif actions[0] == "S":
            if self.isTopCardRevealed():
                (stackDest, hiddenTableIndex) = self.getClosestStack(
                    self.getStock().getTopCard(), True
                )
                if stackDest != None:
                    self.moveStockCardToStack(stackDest)
                    if hiddenTableIndex != None:
                        self.addToHiddenTable(hiddenTableIndex, len(list))
                else:
                    return "stackDestError"
            else:
                return "stockTopCardError"

        elif actions[0] == "F":
            foundation = self.getFoundation()
            stackSource = foundation[actions[1]]
            if stackSource.getLen() > 0:
                card = stackSource.getLastElement()
                (stackDest, hiddenTableIndex) = self.getClosestStack(card, True)
                if stackDest != None:
                    self.moveStackToStack(
                        stackSource, stackDest, stackSource.getLen() - 1
                    )
                    if hiddenTableIndex != None:
                        self.addToHiddenTable(hiddenTableIndex, len(list))
                return "stackDestError"
            return "foundationStackSourceError"

        elif actions[0] == "T":
            table = self.getTable()
            tableIndex = actions[1]
            stackSource = table[tableIndex]
            if stackSource.getLen() > 0:
                cardIndex = actions[2]
                if cardIndex < stackSource.getLen():
                    list = stackSource.getListFromStack(cardIndex)
                    singleCard = len(list) == 1
                    (stackDest, hiddenTableIndex) = self.getClosestStack(
                        list[0], singleCard
                    )
                    if stackDest != None:
                        self.moveStackToStack(stackSource, stackDest, cardIndex)
                        if hiddenTableIndex != None:
                            self.addToHiddenTable(hiddenTableIndex, len(list))
                            self.removeFromHiddenTable(tableIndex, cardIndex)

                    else:
                        return "stackDestError"
                else:
                    return "tableStackSourceIndexError"
            else:
                return "tableStackSourceEmptyError"

    def draw(self):
        stock = self.getStock()
        waste = self.getWaste()
        if self.isTopCardRevealed():
            self.moveStockCardToStack(waste)
        if not (stock.isEmpty()):
            self.switchTopCardRevealed()
        elif not (waste.isEmpty()):
            for card in waste.getListFromStack(0):
                stock.addToBack(card)
            waste.remove(0)
        else:
            raise Exception("Cannot draw a card from an empty stock.")

    def isWon(self):
        for stack in self.getFoundation():
            if stack.getLen() != 13:
                return False
        return True

    def isFinished(self):
        return self.isWon()
