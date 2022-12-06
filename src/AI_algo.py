from src.AI import *


class AI_algo(AI):
    def __init__(self):
        self.boardChanged = True
        self.consecutiveDraw = 0
        self.redKingsLeft = 2
        self.blackKingsLeft = 2

    def hasBoardChanged(self):
        return self.boardChanged

    def setBoardChanged(self, value):
        self.boardChanged = value

    def getConsecutiveDraw(self):
        return self.consecutiveDraw

    def incrConsecutiveDraw(self):
        self.consecutiveDraw += 1

    def resetConsecutiveDraw(self):
        self.consecutiveDraw = 0

    def canSendToFoundation(self, foundation, card: Card):
        for foundationIndex in range(len(foundation)):
            stackDest: Stack = foundation[foundationIndex]
            if stackDest.getLen() > 0:
                lastCard: Card = stackDest.getLastElement()
                if (
                    lastCard.getSuite() == card.getSuite()
                    and lastCard.getValue() == card.getValue() - 1
                ):
                    return True
        return False

    def setRedKingsLeft(self, number):
        self.redKingsLeft = number

    def setBlackKingsLeft(self, number):
        self.blackKingsLeft = number

    def getKingsLeft(self, game: Game):
        table = game.getTable()
        foundation = game.getFoundation()
        hiddenTable = game.getHiddenTable()
        redKingsLeft = 2
        blackKingsLeft = 2

        for stackIndex, stack in enumerate(table):
            stackList = stack.getListFromStack(0)
            for hidden, card in zip(hiddenTable[stackIndex], stackList):
                if not (hidden):
                    value, suite = card.getCard()
                    if suite in RED:
                        if value == 13:
                            redKingsLeft -= 1
                    else:
                        if value == 13:
                            blackKingsLeft -= 1
                    break
        for stack in foundation:
            card: Card = stack.getLastElement()
            if card != None and card.getValue() == 13:
                if card.getSuite() in RED:
                    redKingsLeft -= 1
                else:
                    blackKingsLeft -= 1

        return (redKingsLeft, blackKingsLeft)

    def getOptimalKingColor(self, game: Game):
        table = game.getTable()
        hiddenTable = game.getHiddenTable()
        scoreLayout = [None for _ in table]
        emptySpots = 0
        redKingScore = 0
        blackKingScore = 0

        for stackIndex, stack in enumerate(table):
            hiddenCount = 0
            stackList = stack.getListFromStack(0)
            if stack.isEmpty():
                emptySpots += 1
            for hidden, card in zip(hiddenTable[stackIndex], stackList):
                if hidden:
                    hiddenCount += 1
                else:
                    value, suite = card.getCard()
                    if value != 13:
                        if suite in RED:
                            if value % 2 == 0:
                                kingNeeded = BLACK
                            else:
                                kingNeeded = RED
                        else:
                            if value % 2 == 0:
                                kingNeeded = RED
                            else:
                                kingNeeded = BLACK
                        distanceToKing = 13 - value
                        scoreLayout[stackIndex] = [
                            kingNeeded,
                            distanceToKing,
                            hiddenCount,
                        ]
                        break

        redKingsLeft, blackKingsLeft = self.getKingsLeft(game)
        for score in scoreLayout:
            if score != None:
                if score[1] != 0:
                    if score[0] == RED:
                        redKingScore += (score[2] / score[1]) * redKingsLeft
                    else:
                        blackKingScore += (score[2] / score[1]) * blackKingsLeft

        game.printBoard()
        print("\n\n------------------------------")
        print(f"redKingScore: {redKingScore}\nblackKingScore: {blackKingScore}\n\n")

        if (
            redKingScore == 0
            and blackKingScore == 0
            or (redKingsLeft + blackKingsLeft <= emptySpots)
        ):
            return RED + BLACK
        if redKingScore > blackKingScore:
            return RED
        else:
            return BLACK

    def getShrinkingActions(self, game: Game):
        table = game.getTable()
        foundation = game.getFoundation()
        shrinkingActions = []

        for tableIndex in range(len(table)):
            stackSource = table[tableIndex]
            if stackSource.getLen() > 0:
                card: Card = stackSource.getLastElement()
                if self.canSendToFoundation(foundation, card):
                    shrinkingActions.append(["T", tableIndex, stackSource.getLen() - 1])
        return shrinkingActions

    def getRevealingActions(self, game: Game):
        table = game.getTable()
        hiddenTable = game.getHiddenTable()
        revealingActions = []

        for tableIndex in range(len(table)):
            stackSource = table[tableIndex]
            hiddenStack = hiddenTable[tableIndex]
            if len(hiddenStack) > 0:
                cardIndex = hiddenStack.index(False)
                list = stackSource.getListFromStack(cardIndex)
                if not (cardIndex == 0 and list[0].getValue() == 13):
                    stackDest = game.getClosestStack(list[0], len(list) == 1)
                    if stackDest != None:
                        revealingActions.append(["T", tableIndex, cardIndex])
        return revealingActions

    def getEnablingActions(self, game: Game):
        table = game.getTable()
        foundation = game.getFoundation()
        enablingActions = []

        for tableIndex in range(len(table)):
            stackSource = table[tableIndex]
            for cardIndex in range(1, stackSource.getLen()):
                if not (game.isHidden(tableIndex, cardIndex - 1)):
                    enablingList = stackSource.getListFromStack(cardIndex)
                    closestStack = game.getClosestStack(
                        enablingList[0], len(enablingList) == 1
                    )
                    if closestStack != None and self.canSendToFoundation(
                        foundation, stackSource.getListFromStack(cardIndex - 1)[0]
                    ):
                        enablingActions.append(["T", tableIndex, cardIndex])
        return enablingActions

    def getTableAction(self, game: Game):
        shrinkingActions = self.getShrinkingActions(game)
        revealingActions = self.getRevealingActions(game)
        enablingActions = self.getEnablingActions(game)

        tableActions = shrinkingActions + revealingActions + enablingActions
        if len(tableActions) > 0:
            return tableActions[0]

    def getTurnAction(self, game: Game):
        stock = game.getStock()
        waste = game.getWaste()
        action = None

        if waste.isEmpty() and not (stock.isEmpty()):
            action = ["D", None, None]
            self.incrConsecutiveDraw()
            return action

        if self.hasBoardChanged():
            tableAction = self.getTableAction(game)
            if tableAction != None:
                self.setBoardChanged(True)
                self.resetConsecutiveDraw()
                return tableAction

        card: Card = waste.getLastElement()
        if card != None:
            # self.updateKingsLeft(game)
            closestStack = game.getClosestStack(card, True)
            if closestStack == None or (
                card.getValue() == 13
                and card.getSuite() not in self.getOptimalKingColor(game)
            ):
                action = ["D", None, None]
                self.setBoardChanged(False)
                self.incrConsecutiveDraw()

            else:
                action = ["S", None, None]
                self.setBoardChanged(True)
                self.resetConsecutiveDraw()
        else:
            return None

        if self.getConsecutiveDraw() >= stock.getDeckLen() + waste.getLen() + 1:
            return None

        return action
