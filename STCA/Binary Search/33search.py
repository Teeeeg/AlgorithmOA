from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            # 二分搜索
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # mid到right之间升序
            if nums[mid] < nums[right]:
                # 若target在此范围内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # left到mid之间升序
            else:
                # 若target在此范围内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1