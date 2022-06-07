from typing import List


# 不同为1
# 相同为0
class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        # 先求所有数字的异或
        # 得到的结果是n1 ^ n2
        num1XORnum2 = 0
        for num in nums:
            num1XORnum2 ^= num

        # 找到n1 和 n2 不相同的一个bit
        rightMostBit = 1
        while not rightMostBit & num1XORnum2:
            rightMostBit = rightMostBit << 1

        # 用这个不同的bit来划分所有数字
        # 1. 所有数字该bit都为1
        # 2. 所有数字该bit都为0
        # 由于数字有重复项， 各个分组的异或变成落单数
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
