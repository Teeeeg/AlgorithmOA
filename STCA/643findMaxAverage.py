import math
from typing import List


class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        left = 0
        total = 0
        res = -math.inf

        for right in range(n):
            total += nums[right]

            if right - left + 1 >= k:
                res = max(res, total / k)
                total -= nums[left]
                left += 1

        return res


nums = [1, 12, -5, -6, 50, 3]
k = 4
slt = Solution()
print(slt.findMaxAverage(nums, k))