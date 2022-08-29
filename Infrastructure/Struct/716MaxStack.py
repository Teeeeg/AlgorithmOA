from heapq import heappop, heappush


class MaxStack:

    def __init__(self):
        self.maxHeap = []
        self.data = []
        self.toDelete = set()
        self.key = 0

    def push(self, x: int) -> None:
        self.data.append((x, self.key))
        heappush(self.maxHeap, (-x, -self.key))
        self.key += 1

    def softDelete(self):
        while self.data and self.data[-1][1] in self.toDelete:
            self.data.pop()

        while self.maxHeap and -self.maxHeap[0][1] in self.toDelete:
            heappop(self.maxHeap)

    def pop(self) -> int:
        self.softDelete()
        self.toDelete.add(self.data[-1][1])

        return self.data[-1][0]

    def top(self) -> int:
        self.softDelete()

        return self.data[-1][0]

    def peekMax(self) -> int:
        self.softDelete()

        return -self.maxHeap[0][0]

    def popMax(self) -> int:
        self.softDelete()

        maxVal, key = heappop(self.maxHeap)
        self.toDelete.add(-key)

        return -maxVal


maxStack = MaxStack()
maxStack.push(74)
print(maxStack.popMax())
maxStack.push(89)
maxStack.push(67)
print(maxStack.popMax())
print(maxStack.pop())
# print(maxStack.pop())
