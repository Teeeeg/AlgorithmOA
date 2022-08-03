from typing import List


class Solution:

    def subsetsCore(self, nums, path, startIndex):
        self.res.append(path[:])

        if startIndex >= self.n:
            return

        for i in range(startIndex, self.n):
            path.append(nums[i])
            self.subsetsCore(nums, path, i + 1)
            path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.n = len(nums)
        self.subsetsCore(nums, [], 0)
        return self.res