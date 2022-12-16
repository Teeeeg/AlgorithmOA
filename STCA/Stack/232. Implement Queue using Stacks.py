class MyQueue:

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def pushToOutputStack(self):
        while self.inputStack:
            self.outputStack.append(self.inputStack.pop())

    def push(self, x: int) -> None:
        self.pushToOutputStack()
        self.inputStack.append(x)

    def pop(self) -> int:
        if not self.outputStack:
            self.pushToOutputStack()
        return self.outputStack.pop()

    def peek(self) -> int:
        if not self.outputStack:
            self.pushToOutputStack()

        return self.outputStack[-1]

    def empty(self) -> bool:
        return not self.inputStack and not self.outputStack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()