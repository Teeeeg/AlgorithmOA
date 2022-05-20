from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 同一数层的去重需要排序
        nums.sort()
        # 用于去除同一树枝上的
        visited = [False] * len(nums)
        self.permuteUniqueCore(nums, [], visited, res)
        return res

    def permuteUniqueCore(self, nums: List[int], path: List[int], visited, res: List[List[int]]):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if not visited[i]:
                # 用于去除同一数层的
                # 因为回溯之后，前面这个visited会变成False，代表被访问过
                # 因为保证是从前向后遍历的
                if (i > 0 and nums[i] == nums[i - 1]) and not visited[i - 1]:
                    continue
                path.append(nums[i])
                visited[i] = True
                self.permuteUniqueCore(nums, path, visited, res)
                visited[i] = False
                path.pop()


nums = [1, 1, 2]
slt = Solution()
print(slt.permuteUnique(nums))