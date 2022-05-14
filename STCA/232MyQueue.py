class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if self.output:
            return self.output.pop()
        while self.input:
            self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        if self.output:
            return self.output.pop()
        while self.input:
            self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output
