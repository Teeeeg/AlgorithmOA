from typing import List


class Solution:

    def permuteUniqueCore(self, path):
        if len(path) == self.n:
            self.res.append(path[:])
            return

        for i in range(self.n):
            if self.used[i] == 0:
                if i > 0 and self.used[i - 1] and self.nums[i] == self.nums[i - 1]:
                    continue
                self.used[i] = 1
                path.append(self.nums[i])
                self.permuteUniqueCore(path)
                path.pop()
                self.used[i] = 0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.nums = sorted(nums)
        self.used = [0] * self.n
        self.res = []
        self.permuteUniqueCore([])
        return self.res


nums = [1, 1, 2]
slt = Solution()
print(slt.permuteUnique(nums))