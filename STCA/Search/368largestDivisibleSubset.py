from typing import List


class Solution:

    def largestDivisibleSubsetCore(self, nums: List[int], index, path):
        if index == len(nums):
            return (1, path[:])

        maxLen = 0
        for i in range(index + 1, len(nums)):
            if nums[i] % nums[index]:
                continue

            path.append(nums[i])
            maxLen = max(maxLen, self.largestDivisibleSubsetCore(nums, i, path)[0] + 1)

        return (maxLen, path)

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        maxLen = 0
        path = []

        for i in range(len(nums)):
            curLen, curPath = self.largestDivisibleSubsetCore(nums, i, [])
            if curLen > maxLen:
                maxLen = curLen
                path = curPath

        return path


nums = [1, 2, 3]
slt = Solution()
print(slt.largestDivisibleSubset(nums))