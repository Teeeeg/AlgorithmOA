import math
from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        res = math.inf

        for right in range(n):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1

        return res if res != math.inf else 0  # type: ignore


target = 7
nums = [2, 3, 1, 2, 4, 3]
slt = Solution()
print(slt.minSubArrayLen(target, nums))
