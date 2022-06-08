from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        self.quickSort(nums, left, right)

        return nums

    def partition(self, nums: List[int], left, right):
        pivotIndex = right
        pivotVal = nums[pivotIndex]

        i = left

        for j in range(left, right):
            if nums[j] <= pivotVal:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]

        return i

    def quickSort(self, nums, left, right):
        if left >= right:
            return

        pivotIndex = self.partition(nums, left, right)
        self.quickSort(nums, left, pivotIndex - 1)
        self.quickSort(nums, pivotIndex + 1, right)


nums = [2, 3, 5, 7, 1, 6, 3, 3, 4, 7, 3, 2, 1]
slt = Solution()
print(slt.sortArray(nums))