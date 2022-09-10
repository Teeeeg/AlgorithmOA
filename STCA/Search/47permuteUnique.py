from typing import List


class Solution:

    def permuteUniqueCore(self, nums, visited, path, res):
        n = len(nums)

        if len(path) == n:
            res.append(list(path))

        for i in range(n):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            path.append(nums[i])
            visited[i] = 1
            self.permuteUniqueCore(nums, visited, path, res)
            path.pop()
            visited[i] = 0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [0] * len(nums)
        nums.sort()

        self.permuteUniqueCore(nums, visited, [], res)

        return res


nums = [1, 1, 2]
slt = Solution()
print(slt.permuteUnique(nums))