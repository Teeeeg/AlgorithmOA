from typing import List


class Solution:

    def swap(self, nums: List[int], left, right):
        nums[left], nums[right] = nums[right], nums[left]

    def comapre(self, nums: List[int], index1, index2):
        return nums[index1] < nums[index2]

    def siftDown(self, nums: List[int], index, heapLen):
        while index * 2 + 1 < heapLen:
            leftChild = index * 2 + 1
            rightChild = index * 2 + 2
            indexToSwap = index

            if self.comapre(nums, indexToSwap, leftChild):
                indexToSwap = leftChild

            if rightChild < heapLen and self.comapre(nums, indexToSwap, rightChild):
                indexToSwap = rightChild

            if indexToSwap == index:
                break

            self.swap(nums, indexToSwap, index)
            index = indexToSwap

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1, -1, -1):
            self.siftDown(nums, i, n)

        for i in range(n - 1, -1, -1):
            self.swap(nums, 0, i)
            self.siftDown(nums, 0, i)

        return nums


nums = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
slt = Solution()
print(slt.sortArray(nums))