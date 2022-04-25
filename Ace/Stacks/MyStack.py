class MyStack:
    def __init__(self):
        self.stackList = []
        self.stackSize = 0

    def isEmpty(self):
        return self.stackSize == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.stackList[-1]

    def getSize(self):
        return self.stackSize

    def push(self, data):
        self.stackSize += 1
        self.stackList.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        self.stackSize -= 1
        return self.stackList.pop()


stack = MyStack()
print(stack.getSize())
print(stack.isEmpty())
