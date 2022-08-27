from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        opt = [1] * n
        pre = [-1] * n
        res = 1
        resIndex = -1
        path = []

        for i in range(1, n):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue

                if opt[j] + 1 > opt[i]:
                    opt[i] = opt[j] + 1
                    pre[i] = j

        for i in range(len(nums)):
            if opt[i] > res:
                res = opt[i]
                resIndex = i

        self.getSub(nums, pre, resIndex, path)
        print(path)

        return res

    def getSub(self, nums: List[int], path: List[int], index: int, sub: List[int]):
        if path[index] == -1:
            sub.append(nums[index])
            return

        self.getSub(nums, path, path[index], sub)
        sub.append(nums[index])


nums = [0, 1, 0, 3, 2, 3]
slt = Solution()
print(slt.lengthOfLIS(nums))