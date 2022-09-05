from typing import List


class Solution:

    def minMoves2(self, nums: List[int]) -> int:
        res = 0
        sortedNums = sorted(nums)
        median = sortedNums[len(nums) // 2]

        for num in sortedNums:
            res += abs(num - median)

        return res