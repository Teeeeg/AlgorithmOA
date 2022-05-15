from typing import List


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = [i for i in range(n)]
        start = 0

        while len(nums) > 1:
            start = (start + m - 1) % len(nums)
            nums.pop(start)

        return nums[0]


slt = Solution()
print(slt.lastRemaining(82002, 120659))
