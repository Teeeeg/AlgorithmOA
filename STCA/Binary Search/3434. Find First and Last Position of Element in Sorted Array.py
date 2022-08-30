from typing import List


class Solution:

    def getPos(self, nums: List[int], target: int, toLeft: bool):
        n = len(nums)
        left = 0
        right = n - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if toLeft:
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid

        if toLeft:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
        else:
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        leftBound = self.getPos(nums, target, True)
        if leftBound == -1:
            return [-1, -1]

        rightBound = self.getPos(nums, target, False)

        return [leftBound, rightBound]


nums = [5, 7, 7, 8, 8, 10]
target = 8
slt = Solution()
print(slt.searchRange(nums, target))
