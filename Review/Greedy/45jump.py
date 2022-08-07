from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        curCover = 0
        nextCover = 0
        res = 0

        for i in range(n):
            nextCover = max(nextCover, nums[i] + i)
            if curCover == i:
                res += 1
                curCover = nextCover
                if nextCover >= n - 1:
                    break
        return res
