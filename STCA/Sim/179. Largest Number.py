from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        for i in range(n):
            for j in range(i):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]

        res = ''
        for num in nums:
            res += str(num)

        return str(int(res))


nums = [3, 30, 34, 5, 9]
slt = Solution()
print(slt.largestNumber(nums))
