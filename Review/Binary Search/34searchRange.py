from typing import List


class Solution:

    def binarySearch(self, nums: List[int], target, flag):
        n = len(nums)
        left = 0
        right = n - 1
        res = -1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                res = mid
                if flag:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        leftRes = self.binarySearch(nums, target, False)
        if leftRes == -1:
            return [-1, -1]

        rightRes = self.binarySearch(nums, target, True)

        return [leftRes, rightRes]


nums = [5, 7, 7, 8, 8, 10]
target = 8
slt = Solution()
print(slt.searchRange(nums, target))
