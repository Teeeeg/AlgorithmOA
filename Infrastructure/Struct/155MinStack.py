# 两个栈
# 若新进的值比当前值小，则复制当前helper栈顶元素加入，与栈同步
# 其余一致
class MinStack:
    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.helper:
            if self.helper[-1] > val:
                self.helper.append(val)
            else:
                self.helper.append(self.helper[-1])
        else:
            self.helper.append(val)

    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.helper.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.helper[-1]


# 一个栈，存tuple
class MinStack1:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            minVal = self.stack[-1][0]
            if val < minVal:
                self.stack.append((val, val))
            else:
                self.stack.append((minVal, val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
