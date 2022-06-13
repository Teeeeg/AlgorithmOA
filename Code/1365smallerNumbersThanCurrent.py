from typing import List


class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dct = {}
        sortedNums = sorted(nums)

        for i in range(n - 1, -1, -1):
            dct[sortedNums[i]] = i

        res = []
        for i in range(n):
            res.append(dct[nums[i]])

        return res


nums = [8, 1, 2, 2, 3]
slt = Solution()
print(slt.smallerNumbersThanCurrent(nums))