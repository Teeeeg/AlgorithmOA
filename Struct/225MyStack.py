# two queues
class MyStack:

    def __init__(self):
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)

    # 每次将n-1个元素进helper
    # 最后一个在data里的即为栈顶
    def pop(self) -> int:
        while len(self.data) > 1:
            self.helper.append(self.data.pop(0))
        self.data, self.helper = self.helper, self.data
        return self.helper.pop(0)

    # 最后要还原
    def top(self) -> int:
        while len(self.data) > 1:
            self.helper.append(self.data.pop(0))
        res = self.data[0]
        self.helper.append(self.data.pop(0))
        self.data, self.helper = self.helper, self.data
        return res

    def empty(self) -> bool:
        return not self.data and not self.helper


# one queue
class MyStack1:

    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    # 即将n-1个数据放到队尾
    # 第一个即栈顶
    def pop(self) -> int:
        # 记录下当前的长度
        size = len(self.data)
        while size > 1:
            self.data.append(self.data.pop(0))
            size -= 1
        return self.data.pop(0)

    def top(self) -> int:
        size = len(self.data)
        while size > 1:
            self.data.append(self.data.pop(0))
            size -= 1
        # 还原
        res = self.data[0]
        self.data.append(self.data.pop(0))
        return res

    def empty(self) -> bool:
        return not self.data
