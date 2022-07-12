from collections import deque
from typing import List


class AscQueue:
    # 维护一个递增的队列
    def __init__(self) -> None:
        self.data = deque()

    def append(self, value):
        # 保持 5 4 3
        while self.data and self.data[-1] < value:
            self.data.pop()
        self.data.append(value)

    def pop(self, value):
        if self.data and self.data[0] == value:
            self.data.popleft()

    def getMax(self):
        return self.data[0]


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ascQueue = AscQueue()
        res = []
        left = 0

        if n == 1 or k == 1:
            return nums

        for right in range(n):
            ascQueue.append(nums[right])
            # 当长度等于k之后
            if right - left + 1 >= k:
                res.append(ascQueue.getMax())
                ascQueue.pop(nums[left])
                left += 1

        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
slt = Solution()
print(slt.maxSlidingWindow(nums, k))
