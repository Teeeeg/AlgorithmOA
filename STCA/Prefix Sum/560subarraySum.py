from typing import List


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        # 初始化，0出现一次
        dct = {0: 1}
        res = 0

        for i in range(n):
            # 先计算前缀和
            total += nums[i]
            # 若当前所需的值存在
            res += dct.get((total - k), 0)
            # 再更新
            dct[total] = dct.get(total, 0) + 1

        return res


class Solution1:

    def __init__(self) -> None:
        self.res = 0

    def subarraySum(self, nums: List[int], k: int) -> int:
        self.subarraySumCore(nums, k, 0)
        return self.res

    def subarraySumCore(self, nums, target, startIndex):
        if target == 0:
            self.res += 1
            return

        for i in range(startIndex, len(nums)):
            self.subarraySumCore(nums, target - nums[i], i + 1)


nums = [1, 1, 1]
k = 2
slt = Solution1()
print(slt.subarraySum(nums, k))
