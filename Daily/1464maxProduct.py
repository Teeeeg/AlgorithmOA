from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        maxNum = 0
        secMaxNum = 0

        for num in nums:
            if num > maxNum:
                secMaxNum = maxNum
                maxNum = num
            elif num > secMaxNum:
                secMaxNum = num

        return (maxNum - 1) * (secMaxNum - 1)


nums = [1, 5, 4]
slt = Solution()
print(slt.maxProduct(nums))
