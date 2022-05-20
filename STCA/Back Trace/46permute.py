from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 用于树枝上去重
        visited = [False] * len(nums)
        self.permuteCore(nums, visited, [], res)
        return res

    def permuteCore(self, nums: List[int], visited: List[bool], path: List[int], res: List[List]):
        if len(path) == len(nums):
            res.append(path[:])

        for i in range(len(nums)):
            if not visited[i]:
                path.append(nums[i])
                visited[i] = True
                self.permuteCore(nums, visited, path, res)
                visited[i] = False
                path.pop()


nums = [1, 2, 3]
slt = Solution()
print(slt.permute(nums))