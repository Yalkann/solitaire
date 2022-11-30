from src.AI import *
from time import sleep


class AI_algo(AI):
    def __init__(self):
        self.boardChanged = True
        self.consecutiveDraw = 0

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
        # sleep(0.01)
        # print("\nConsec Draw:", self.getConsecutiveDraw(), "\n")

        if waste.isEmpty() and not (stock.isEmpty()):
            action = ["D", None, None]
            game.appendHistory(action)
            self.incrConsecutiveDraw()
            return action

        if self.hasBoardChanged():
            tableAction = self.getTableAction(game)
            if tableAction != None:
                game.appendHistory(tableAction)
                self.setBoardChanged(True)
                self.resetConsecutiveDraw()
                return tableAction

        card = waste.getLastElement()
        if card != None:
            closestStack = game.getClosestStack(card, True)
            if closestStack == None:
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

        game.appendHistory(action)
        return action
