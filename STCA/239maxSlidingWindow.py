from typing import List


class AscQueue:

    def __init__(self):
        self.queue = []

    def push(self, value):
        # 与队尾比较，把比它小的全部弹出去
        # 保持队列单调递增
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def pop(self, value):
        if self.queue[0] == value:
            self.queue.pop(0)

    def get(self):
        return self.queue[0]


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ascQueue = AscQueue()
        res = []
        left = 0

        for right, num in enumerate(nums):
            ascQueue.push(num)
            if right - left + 1 >= k:
                res.append(ascQueue.get())
                value = nums[left]
                ascQueue.pop(value)
                left += 1

        return res


nums = [9, 10, 9, -7, -4, -8, 2, -6]
k = 5
slt = Solution()
print(slt.maxSlidingWindow(nums, k))
