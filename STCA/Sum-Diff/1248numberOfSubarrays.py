from typing import List


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = {0: 1}
        total = 0
        res = 0

        for i in range(n):
            total += nums[i] % 2
            res += sums.get(total - k, 0)
            sums[total] = sums.get(total, 0) + 1

        return res


nums = [1, 1, 2, 1, 1]
k = 3
slt = Solution()
print(slt.numberOfSubarrays(nums, k))
