from random import randint


class Heap:

    def __init__(self) -> None:
        self.data = []

    @property
    def size(self):
        """Get the size of this heap

        Returns:
            int: the size of heap
        """
        return len(self.data)

    def camparator(self, index1, index2):
        """Default Camparator

        Args:
            index1 (int): The index of num1
            index2 (int): The index of num2

        Returns:
            Bool: return True if num1 < num2
        """
        return self.data[index1] < self.data[index2]

    def swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    def siftDown(self, index):
        while index < self.size:
            leftIndex = 2 * index + 1
            rightIndex = 2 * index + 2
            index1 = index

            if leftIndex < self.size and self.camparator(leftIndex, index):
                index1 = leftIndex

            if rightIndex < self.size and self.camparator(rightIndex, index1):
                index1 = rightIndex

            if index1 == index:
                break

            self.swap(index, index1)
            index = index1

    def siftUp(self, index):
        while index != 0:
            parentIndex = index // 2
            if self.camparator(index, parentIndex):
                self.swap(parentIndex, index)

            index = parentIndex

    def pop(self):
        res = self.data[0]
        self.swap(0, self.size - 1)
        self.data.pop()
        self.siftDown(0)

        return res

    def push(self, val):
        self.data.append(val)
        self.siftUp(self.size - 1)


heap = Heap()

for _ in range(20):
    num = randint(1, 100)
    heap.push(num)

heap.push(6)
heap.push(8)

res = []
for _ in range(20):
    res.append(heap.pop())

print(res)
