class MyQueue:
    # 一个输入一个输出
    # 当要输出的时候，发现输出栈内无元素
    # 就将输入队的元素全部倒入输出
    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def push(self, x: int) -> None:
        self.inputStack.append(x)

    def pop(self) -> int:
        if self.outputStack:
            return self.outputStack.pop()

        while self.inputStack:
            self.outputStack.append(self.inputStack.pop())
        return self.outputStack.pop()

    def peek(self) -> int:
        if self.outputStack:
            return self.outputStack[-1]

        while self.inputStack:
            self.outputStack.append(self.inputStack.pop())
        return self.outputStack[-1]

    def empty(self) -> bool:
        return not self.inputStack and not self.outputStack
