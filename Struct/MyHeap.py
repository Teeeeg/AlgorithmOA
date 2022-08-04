from random import randint


class MyHeap:

    def __init__(self, desc=False) -> None:
        self.data = []
        self.desc = desc

    @property
    def size(self):
        return len(self.data)

    def swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    # 用于判断前者是否比后者小
    def camparator(self, nums1, nums2):
        return nums1 > nums2 if self.desc else nums1 < nums2

    # 弹出
    # 1. 获取该元素
    # 2. 与最后一个交换
    # 3. 弹出该元素
    # 4. 将第一个元素下沉
    def pop(self):
        item = self.data[0]
        self.swap(0, self.size - 1)
        self.data.pop()
        self.siftDown(0)
        return item

    # 1. 追加到最后
    # 2. 将该元素上浮
    def push(self, val):
        self.data.append(val)
        self.siftUp(self.size - 1)

    def siftDown(self, index):
        # 与其children对比
        # 比他们大就下沉
        while index * 2 + 1 < self.size:
            leftChildIndex = index * 2 + 1
            rightChildIndex = index * 2 + 2
            smallest = index

            # 记录左右哪个更加小
            if self.camparator(self.data[leftChildIndex], self.data[smallest]):
                smallest = leftChildIndex

            if rightChildIndex < self.size and self.camparator(self.data[rightChildIndex], self.data[smallest]):
                smallest = rightChildIndex

            if smallest == index:
                break

            self.swap(smallest, index)
            index = smallest

    def siftUp(self, index):
        # 与其parent对比
        # 若比parent小则上升
        while index:
            parendIndex = (index - 1) // 2

            if self.camparator(self.data[index], self.data[parendIndex]):
                self.swap(index, parendIndex)
                index = parendIndex
            else:
                break


heap = MyHeap()
for _ in range(20):
    val = randint(1, 20)
    heap.push(val)

for _ in range(20):
    print(heap.pop())
