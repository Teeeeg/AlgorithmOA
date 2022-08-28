from typing import List


class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        opt = [1] * n
        pre = [-1] * n
        resIndex = -1
        maxLen = -1
        path = []

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j]:
                    continue

                if opt[j] + 1 > opt[i]:
                    opt[i] = opt[j] + 1
                    pre[i] = j

        for i in range(n):
            if opt[i] > maxLen:
                maxLen = opt[i]
                resIndex = i
        self.getPath(pre, nums, path, resIndex)

        return path

    def getPath(self, pre, nums: List[int], path: List[int], index):
        if pre[index] == -1:
            path.append(nums[index])
            return

        self.getPath(pre, nums, path, pre[index])
        path.append(nums[index])


nums = [1, 2, 3]
slt = Solution()
print(slt.largestDivisibleSubset(nums))