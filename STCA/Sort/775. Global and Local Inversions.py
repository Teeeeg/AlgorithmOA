from typing import List


class Solution:

    def mergeTwo(self, nums: List[int], left, mid, right):
        tmp = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1

        while i <= mid:
            tmp.append(nums[i])
            i += 1

        while j <= right:
            tmp.append(nums[j])
            j += 1

        nums[left:right + 1] = tmp

    def countReverePairs(self, nums: List[int], left, mid, right):
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[j] < nums[i]:
                j += 1
            self.globalPairs += j - mid - 1

    def mergeSortCore(self, nums: List[int], left, right):
        if left >= right:
            return

        mid = (right + left) // 2
        self.mergeSortCore(nums, left, mid)
        self.mergeSortCore(nums, mid + 1, right)
        self.countReverePairs(nums, left, mid, right)
        self.mergeTwo(nums, left, mid, right)

    def mergeSort(self, nums: List[int]):
        n = len(nums)
        left = 0
        right = n - 1
        self.mergeSortCore(nums, left, right)

    def isIdealPermutation(self, nums: List[int]) -> bool:
        self.globalPairs = 0
        self.mergeSort(nums[:])
        localPairs = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                localPairs += 1

        return self.globalPairs == localPairs


nums = [1, 2, 0]
slt = Solution()
print(slt.isIdealPermutation(nums))