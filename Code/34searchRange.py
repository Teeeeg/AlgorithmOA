from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftBound = self.binarySearch(nums, target, True)
        rightBound = self.binarySearch(nums, target, False)
        return [leftBound, rightBound]

    def binarySearch(self, nums, target, findLeft):
        left, right = 0, len(nums) - 1
        # 用于保存过程中的答案
        res = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # 找到对应的值先保存，再继续寻找边界
                res = mid
                if findLeft:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return res


solution = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(solution.searchRange(nums, target))
