from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1] * (n + 1)
        postfixProd = [1] * (n + 1)

        for i in range(n):
            prefixProd[i + 1] = prefixProd[i] * nums[i]

        for i in range(n - 1, -1, -1):
            postfixProd[i] = postfixProd[i + 1] * nums[i]

        res = [0] * n
        for i in range(n):
            res[i] = prefixProd[i] * postfixProd[i + 1]

        return res


nums = [1, 2, 3, 4]
slt = Solution()
print(slt.productExceptSelf(nums))