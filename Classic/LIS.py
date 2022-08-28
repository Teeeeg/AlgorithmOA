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


class Solution1:

    def lengthOfLISCore(self, nums: List[int], index, memo):
        if index == len(nums):
            return 1

        if memo[index] != -1:
            return memo[index]

        memo[index] = 0
        for i in range(index + 1, len(nums)):
            if nums[index] >= nums[i]:
                continue

            memo[index] = max(memo[index], self.lengthOfLISCore(nums, i, memo) + 1)

        return memo[index]

    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        memo = [-1] * len(nums)

        for i in range(len(nums)):
            res = max(res, self.lengthOfLISCore(nums, i, memo) + 1)

        return res


nums = [10, 9, 2, 5, 3, 7, 101, 18]
slt = Solution()
print(slt.lengthOfLIS(nums))