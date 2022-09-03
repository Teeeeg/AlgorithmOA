from typing import List


class Solution:
    # monoStack farthest
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        # descending stack
        for i in range(n):
            if not stack or nums[stack[-1]] >= nums[i]:
                stack.append(i)

        res = 0
        index = n - 1
        # try every num from last
        while index >= 0:
            while stack and nums[stack[-1]] <= nums[index]:
                # if index - 1, the width will reduce
                res = max(res, index - stack.pop())

            index -= 1

        return res