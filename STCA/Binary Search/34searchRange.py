from typing import List


class Solution:

    def binarySearch(self, nums: List[int], target: int, findLeft: bool):
        left, right = 0, len(nums) - 1
        res = -1

        while left <= right:
            mid = (left + right) // 2
            # 当等于目标值的时候
            if nums[mid] == target:
                res = mid
                # 向左缩小
                if findLeft:
                    right = mid - 1
                # 向右缩小
                else:
                    left = mid + 1
            # 细节，一定要用elif
            # 因为三个情况等价
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        res[0] = self.binarySearch(nums, target, True)
        res[1] = self.binarySearch(nums, target, False)

        return res


nums = [2, 2]
target = 2
slt = Solution()
print(slt.searchRange(nums, target))
