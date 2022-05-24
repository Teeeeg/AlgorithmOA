from random import randint
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        # 用复制
        self.data = nums[:]
        self.res = nums

    def reset(self) -> List[int]:
        # 用复制
        self.res = self.data[:]
        return self.res

    # 每次从[i, n]之间选择j与i进行交换
    def shuffle(self) -> List[int]:
        for i in range(len(self.res)):
            j = randint(i, len(self.res) - 1)
            self.res[i], self.res[j] = self.res[j], self.res[i]

        return self.res


nums = [1, 2, 3]
slt = Solution(nums)
print(slt.shuffle())
print(slt.reset())
print(slt.shuffle())