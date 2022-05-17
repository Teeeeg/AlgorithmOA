from random import randint


class MyHeap:

    def __init__(self, asc=True) -> None:
        self.data = []
        self.asc = asc

    @property
    def size(self):
        return len(self.data)

    def comparator(self, val1, val2):
        return val1 < val2 if self.asc else False

    def swap(self, i1, i2):
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]

    def siftDown(self, index):
        while index * 2 + 1 < self.size:
            leftChild = index * 2 + 1
            rightChild = index * 2 + 2
            smallest = index

            if self.comparator(self.data[leftChild], self.data[smallest]):
                smallest = leftChild

            if rightChild < self.size and self.comparator(
                    self.data[rightChild], self.data[smallest]):
                smallest = rightChild

            if smallest == index:
                break

            self.swap(smallest, index)
            index = smallest

    def siftUp(self, index):
        while index:
            parent = (index - 1) // 2
            if self.comparator(self.data[index], self.data[parent]):
                self.swap(index, parent)

            index = parent

    def push(self, value):
        self.data.append(value)
        self.siftUp(self.size - 1)

    def pop(self):
        self.swap(0, self.size - 1)
        value = self.data.pop()
        self.siftDown(0)
        return value


heap = MyHeap()
for _ in range(20):
    val = randint(1, 20)
    heap.push(val)

for _ in range(20):
    print(heap.pop())