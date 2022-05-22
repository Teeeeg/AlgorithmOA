from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num1XORnum2 = 0
        for num in nums:
            num1XORnum2 ^= num

        rightMostBit = 1
        while not rightMostBit & num1XORnum2:
            rightMostBit = rightMostBit << 1

        num1 = 0
        num2 = 0
        for num in nums:
            if num & rightMostBit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


nums = nums = [1, 2, 1, 3, 2, 5]
solution = Solution()
print(solution.singleNumber(nums))
