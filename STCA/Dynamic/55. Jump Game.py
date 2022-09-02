from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        n = len(nums)
        # opt[i] means it is reachable at index of i
        opt = [False] * n
        opt[0] = True

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if opt[j] and j + nums[j] >= i:
                    opt[i] = True
                    break

        return opt[-1]


class Solution1:

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        rightMost = 0

        for i in range(n):
            if i <= rightMost:
                rightMost = max(rightMost, nums[i] + i)
                if rightMost >= n - 1:
                    return True

        return False


nums = [1, 1, 1, 0]
slt = Solution()
print(slt.canJump(nums))