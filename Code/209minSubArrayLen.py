import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]):
        n = len(nums)
        left = 0
        winSum = 0
        res = math.inf

        for right in range(n):
            winSum += nums[right]
            while winSum >= target:
                res = min(res, right-left+1)
                winSum -= nums[left]
                left += 1

        return res if res != math.inf else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
solution = Solution()
print(solution.minSubArrayLen(target, nums))
