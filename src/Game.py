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

    def move(self, actions):
        if actions[0] == "D":
            if not (self.getStock().isEmpty()):
                self.draw()
                self.nbTurns += 1
            else:
                return "stockEmptyError"

        elif actions[0] == "S":
            if self.isTopCardRevealed():
                closestStack = self.getClosestStack(self.getStock().getTopCard(), True)
                if closestStack != None:
                    stackDest = closestStack[0]
                    hiddenTableIndex = closestStack[1]
                    self.moveStockCardToStack(stackDest)
                    self.nbTurns += 1
                    if hiddenTableIndex != None:
                        self.addToHiddenTable(hiddenTableIndex, 1)
                else:
                    return "stackDestError"
            else:
                return "stockTopCardError"

        elif actions[0] == "F":
            foundation = self.getFoundation()
            stackSource = foundation[actions[1]]
            if stackSource.getLen() > 0:
                card = stackSource.getLastElement()
                closestStack = self.getClosestStack(card, True)
                if closestStack != None:
                    stackDest = closestStack[0]
                    hiddenTableIndex = closestStack[1]
                    self.moveStackToStack(
                        stackSource, stackDest, stackSource.getLen() - 1
                    )
                    self.nbTurns += 1
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

    def getStockAndWasteMoves(self):
        stock = self.getStock()
        waste = self.getWaste()
        moves = []

        for card in stock.getDeck() + waste.getListFromStack(0):
            stackDest = self.getClosestStack(card, True)
            if stackDest != None:
                moves.append(["S", None, None])
        return moves

    def getTableMoves(self):
        table = self.getTable()
        moves = []
        for stackIndex in range(len(table)):
            for cardIndex in range(table[stackIndex].getLen()):
                if not (self.isHidden(stackIndex, cardIndex)):
                    list = table[stackIndex].getListFromStack(cardIndex)
                    stackDest = self.getClosestStack(list[0], len(list) == 1)
                    if stackDest != None:
                        moves.append(["T", stackIndex, cardIndex])
        return moves

    def getFoundationMoves(self):
        foundation = self.getFoundation()
        moves = []

        for stackIndex in range(len(foundation)):
            if foundation[stackIndex].getLen() > 0:
                stackDest = self.getClosestStack(
                    foundation[stackIndex].getLastElement(), True
                )
                if stackDest != None:
                    moves.append(["F", stackIndex, None])
        return moves

    def getAllMoves(self):
        moves = []
        moves += self.getStockAndWasteMoves()
        moves += self.getTableMoves()
        # moves += self.getFoundationMoves()
        return moves

    def isWon(self):
        for stack in self.getFoundation():
            if stack.getLen() != 13:
                return False
        return True

    def isFinished(self):
        moves = self.getAllMoves()
        if len(moves) == 0:
            self.setGameTime()
        return len(moves) == 0
