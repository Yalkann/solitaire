class Stack:
    def __init__(self, list):
        self.stack = list.copy()

    def __str__(self):
        return str(self.stack)

    def getListFromStack(self, index):
        if len(self.stack) == 0:
            return []
        if index < len(self.stack) and index >= 0:
            return self.stack[index::]
        else:
            raise IndexError(
                "Index should be greater than or equal to 0 and smaller than the stack's length."
            )

    def getLastElement(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise Exception("Cannot get the last element from an empty stack.")

    def getLen(self):
        return len(self.stack)

    def add(self, list):
        self.stack += list

    def remove(self, index):
        if len(self.stack) == 0:
            raise Exception("Cannot remove a stack sub-list from an empty stack.")
        if index < len(self.stack) and index >= 0:
            for i in range(len(self.stack) - index):
                del self.stack[-1]
        else:
            raise IndexError(
                "Index should be greater than or equal to 0 and smaller than the stack's length."
            )

    def isEmpty(self):
        return len(self.stack) == 0
