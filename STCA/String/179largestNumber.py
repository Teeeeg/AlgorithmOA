from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        # 一个一个比较
        for i in range(n):
            for j in range(i + 1, n):
                # 例如 10+2 < 2+10
                # 则需要交换，将2换到前面去
                # 注意用字符串比较
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]

        res = []
        for num in nums:
            res.append(str(num))

        return str(int(''.join(res)))


nums = [10, 2, 3]
slt = Solution()
print(slt.largestNumber(nums))