from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] == target:
                return mid

            # 去有序区间找
            # 由于向下取整数
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    # 到下一个无序区间
                    right = mid-1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1

        return -1


nums = [3, 1]
target = 1
solution = Solution()
print(solution.search(nums, target))
