from typing import List


class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        left = 0
        res = 0

        for right in range(n):
            while right - left + 1 - (prefixSum[right + 1] - prefixSum[left]) > k:
                left += 1

            res = max(res, right - left + 1)

        return res


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
slt = Solution()
print(slt.longestOnes(nums, k))
