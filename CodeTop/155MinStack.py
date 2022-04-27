class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append((val, val))
        else:
            self.data.append((val, min(val, self.data[-1][1])))

    def pop(self) -> None:
        if self.data:
            self.data.pop()
        else:
            return None

    def top(self) -> int:
        if self.data:
            return self.data[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.data:
            return self.data[-1][1]
        else:
            return None


class MinStack:

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if self.data:
            if self.data.pop() == self.min[-1]:
                self.min.pop()
        else:
            return None

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]
        else:
            return None


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
minStack.top()
