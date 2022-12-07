from src.Board import *


class Game(Board):
    def areOppositeColor(self, card1: Card, card2: Card):
        return (
            card1.getSuite() in RED
            and card2.getSuite() in BLACK
            or card1.getSuite() in BLACK
            and card2.getSuite() in RED
        )

    def getClosestStack(self, card: Card, isSingle):
        if isSingle:
            for stack in self.getFoundation():
                if stack.getLen() == 0:
                    if card.getValue() == 1:
                        return (stack, None)
                else:
                    lastCard: Card = stack.getLastElement()
                    if (
                        card.getValue() == lastCard.getValue() + 1
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

    def draw(self):
        stock = self.getStock()
        waste = self.getWaste()

        if stock.isEmpty():
            if waste.isEmpty():
                raise Exception("Cannot draw a card from an empty stock.")
            for c in waste.getListFromStack(0):
                stock.addToBack(c)
            waste.remove(0)
        else:
            topCard = stock.getTopCard()
            waste.add([topCard])
            stock.removeTopCard()

    def drawMove(self):
        stock = self.getStock()
        waste = self.getWaste()

        if stock.isEmpty() and waste.isEmpty():
            return "stockEmptyError"
        self.draw()
        self.nbTurns += 1

    def stockMove(self):
        waste = self.getWaste()
        if waste.getLen() > 0:
            closestStack = self.getClosestStack(waste.getLastElement(), True)
            if closestStack != None:
                stackDest = closestStack[0]
                hiddenTableIndex = closestStack[1]
                self.moveWasteCardToStack(stackDest)
                self.nbTurns += 1
                if hiddenTableIndex != None:
                    self.addToHiddenTable(hiddenTableIndex, 1)
            else:
                return "stackDestError"
        else:
            return "stockTopCardError"

    def foundationMove(self, action):
        foundation = self.getFoundation()
        stackSource = foundation[action[1]]
        if stackSource.getLen() > 0:
            card = stackSource.getLastElement()
            closestStack = self.getClosestStack(card, True)
            if closestStack != None:
                stackDest = closestStack[0]
                hiddenTableIndex = closestStack[1]
                self.moveStackToStack(stackSource, stackDest, stackSource.getLen() - 1)
                self.nbTurns += 1
                if hiddenTableIndex != None:
                    self.addToHiddenTable(hiddenTableIndex, len(list))
            return "stackDestError"
        return "foundationStackSourceError"

    def tableMove(self, action):
        table = self.getTable()
        tableIndex = action[1]
        stackSource = table[tableIndex]
        if stackSource.getLen() > 0:
            cardIndex = action[2]
            if cardIndex < stackSource.getLen():
                list = stackSource.getListFromStack(cardIndex)
                closestStack = self.getClosestStack(list[0], len(list) == 1)
                if closestStack != None:
                    stackDest = closestStack[0]
                    hiddenTableIndex = closestStack[1]
                    self.moveStackToStack(stackSource, stackDest, cardIndex)
                    self.nbTurns += 1
                    if hiddenTableIndex != None:
                        self.addToHiddenTable(hiddenTableIndex, len(list))
                    self.removeFromHiddenTable(tableIndex, cardIndex)

                else:
                    return "stackDestError"
            else:
                return "tableStackSourceIndexError"
        else:
            return "tableStackSourceEmptyError"

    def move(self, action):

        if action[0] == "D":
            self.drawMove()
        elif action[0] == "S":
            self.stockMove()
        elif action[0] == "F":
            self.foundationMove(action)
        elif action[0] == "T":
            self.tableMove(action)
        else:
            return "actionError"

        self.appendHistory(action)

    def isWon(self):
        for stack in self.getFoundation():
            if stack.getLen() != 13:
                return False
        return True

    def isFinished(self):
        pass
