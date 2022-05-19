from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            # 二分搜索
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 左右相等无法判断哪边有序，可以随意去除一边
            if nums[left] == nums[mid]:
                left += 1
            # mid到right之间升序
            # 注意一定要用elif
            elif nums[mid] <= nums[right]:
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

        return False


nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
target = 2
slt = Solution()
print(slt.search(nums, target))