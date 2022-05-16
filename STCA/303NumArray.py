from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sums = [0] * (n + 1)
        for i in range(n):
            self.sums[i + 1] = self.sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))
