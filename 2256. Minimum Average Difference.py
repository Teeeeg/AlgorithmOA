from typing import List


class Solution:

    def getDiff(self, prefixSum, index, n):
        leftTotal = prefixSum[index + 1]
        rightTotal = prefixSum[n] - prefixSum[index + 1]

        diff = abs(leftTotal // (index + 1) - rightTotal // (n - index - 1)) if (index + 1) != n else abs(leftTotal // (index + 1))

        return diff

    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        res = -1
        minDiff = 10**9 + 7

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        for i in range(n):
            diff = self.getDiff(prefixSum, i, n)
            if diff < minDiff:
                res = i
                minDiff = diff

        return res


slt = Solution()
nums = [0]
print(slt.minimumAverageDifference(nums))