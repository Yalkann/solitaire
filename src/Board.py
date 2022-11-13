from src.Deck import *
from src.Stack import *


class Board:
    def __init__(self):
        self.stock = Deck()
        self.stock.shuffle()
        self.table = [Stack([]) for _ in range(7)]
        self.hiddenTable = [[] for _ in range(7)]
        self.foundation = [Stack([]) for _ in range(4)]
        self.waste = Stack([])

        for i in range(7):
            cards = []
            for j in range(i + 1):
                cards.append(self.stock.getTopCard())
                self.stock.removeTopCard()
                self.hiddenTable[i].append(True)
            self.table[i].add(cards)
            self.hiddenTable[i][-1] = False

    def __removeFromHiddenTable(self, tableIndex, cardIndex):
        curHiddenTable = self.hiddenTable[tableIndex]
        for _ in range(len(curHiddenTable) - cardIndex):
            self.hiddenTable[tableIndex].pop()
        if len(curHiddenTable) > 0:
            curHiddenTable[-1] = False

    def __addToHiddenTable(self, tableIndex, stackLen):
        self.hiddenTable[tableIndex] += [False for _ in range(stackLen)]

    def __isHidden(self, tableIndex, index):
        return self.hiddenTable[tableIndex][index]

    def __moveStackToStack(self, stackSource, stackDest, cardIndex):
        list = stackSource.getListFromStack(cardIndex)
        stackSource.remove(cardIndex)
        stackDest.add(list)

    def printBoard(self):
        print("Stock size: ", self.stock.getDeckLen())

        print("waste: ", self.waste)

        print("foundation: ")
        for foundStack in self.foundation:
            print("[ ", end="")
            foundList = foundStack.getListFromStack(0)
            if len(foundList) > 0:
                print(foundList[-1], end="")
            print(" ]")

        print("Table: ")
        for tableStackIndex in range(len(self.table)):
            print("[ ", end="")
            tableList = self.table[tableStackIndex].getListFromStack(0)
            if len(tableList) > 0:
                for tableIndex in range(len(tableList)):
                    if self.hiddenTable[tableStackIndex][tableIndex]:
                        print("H", end=";")
                    else:
                        print(tableList[tableIndex], end=";")
            print(" ]")
