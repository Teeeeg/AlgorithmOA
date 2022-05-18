from typing import List


class MyHeap:

    def __init__(self, asc=True) -> None:
        self.data = []
        self.asc = asc

    @property
    def size(self):
        return len(self.data)

    def camparator(self, val1, val2):
        return val1 < val2 if self.asc else val1 > val2

    def swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[
            index1]

    def siftDown(self, index):
        while index * 2 + 1 < self.size:
            leftChild = index * 2 + 1
            rightChild = index * 2 + 2
            smallest = index

            while self.camparator(self.data[leftChild], self.data[smallest]):
                smallest = leftChild
            while rightChild < self.size and self.camparator(
                    self.data[rightChild], self.data[smallest]):
                smallest = rightChild

            if smallest == index:
                break

            self.swap(smallest, index)
            index = smallest

    def siftUp(self, index):
        while index:
            parent = (index - 1) // 2
            if self.camparator(self.data[index], self.data[parent]):
                self.swap(index, parent)

            index = parent

    def pop(self):
        self.swap(0, self.size - 1)
        value = self.data.pop()
        self.siftDown(0)
        return value

    def push(self, value):
        self.data.append(value)
        self.siftUp(self.size - 1)


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        index = self.partition(nums, left, right)
        while index != k - 1:
            if k - 1 < index:
                index = self.partition(nums, left, index - 1)
            else:
                index = self.partition(nums, index + 1, right)

        return nums[index]

    def partition(self, nums, left, right):
        pivotVal = nums[left]
        i = left
        j = right

        while i < j:
            while i < j and nums[j] <= pivotVal:
                j -= 1
            while i < j and nums[i] >= pivotVal:
                i += 1

            if i != j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[i], nums[left] = nums[left], nums[i]

        return i


class Solution1:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = MyHeap()
        for num in nums:
            minHeap.push(num)
            if minHeap.size > k:
                minHeap.pop()

        return minHeap.data[0]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
slt = Solution1()
print(slt.findKthLargest(nums, k))