# 二维数组
class TripleInOne:

    def __init__(self, stackSize: int):
        self.data = [[0] * stackSize for _ in range(3)]
        self.index = [0] * 3

    def push(self, stackNum: int, value: int) -> None:
        index = self.index[stackNum]
        stack = self.data[stackNum]
        if index < len(stack):
            stack[index] = value
            index += 1
            # 更新下标
            self.index[stackNum] = index

    def pop(self, stackNum: int) -> int:
        index = self.index[stackNum]
        stack = self.data[stackNum]
        if index > 0:
            index -= 1
            self.index[stackNum] = index
            return stack[index]
        else:
            return -1

    def peek(self, stackNum: int) -> int:
        index = self.index[stackNum]
        stack = self.data[stackNum]
        if index > 0:
            return stack[index-1]
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        index = self.index[stackNum]
        return index == 0


class TripleInOne1:

    def __init__(self, stackSize: int):
        self.size = stackSize
        self.data = [0] * (3 * stackSize)
        self.index = [stackSize*i for i in range(3)]

    def push(self, stackNum: int, value: int) -> None:
        index = self.index[stackNum]
        if index < self.size * (stackNum+1):
            self.data[index] = value
            index += 1
            self.index[stackNum] = index

    def pop(self, stackNum: int) -> int:
        index = self.index[stackNum]
        if index > self.size * stackNum:
            index -= 1
            self.index[stackNum] = index
            return self.data[index]
        else:
            return -1

    def peek(self, stackNum: int) -> int:
        index = self.index[stackNum]
        if index > self.size * stackNum:
            return self.data[index-1]
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.index[stackNum] == self.size*stackNum


tripleOne = TripleInOne1(0)
tripleOne.push(0, 1)
tripleOne.push(0, 2)
print(tripleOne.peek(0))
# print(tripleOne.pop(0))
# print(tripleOne.pop(0))
# print(tripleOne.pop(0))
# print(tripleOne.isEmpty(0))

# print([i for i in range(0, 3*2, 2)])
