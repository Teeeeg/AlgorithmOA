from typing import List


class Solution:

    def permuteCore(self, path):
        if len(path) == self.n:
            self.res.append(path[:])
            return

        for i in range(self.n):
            if self.used[i] == 0:
                self.used[i] = 1
                path.append(self.nums[i])
                self.permuteCore(path)
                path.pop()
                self.used[i] = 0

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.nums = nums
        self.used = [0] * self.n
        self.res = []
        self.permuteCore([])
        return self.res


nums = [1, 2, 3]
slt = Solution()
print(slt.permute(nums))