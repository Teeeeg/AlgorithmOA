from collections import deque
from typing import List


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        monoQueue = deque()
        res = []
        left = 0

        for right in range(n):
            # keep monoQueue descending
            while monoQueue and nums[right] > nums[monoQueue[-1]]:
                monoQueue.pop()
            monoQueue.append(right)

            if right - left + 1 >= k:
                # if window width is k
                res.append(nums[monoQueue[0]])
                # popleft if left is head of queue
                if left == monoQueue[0]:
                    monoQueue.popleft()

                left += 1

        return res


nums = [1, 3, 1, 2, 0, 5]
k = 3
slt = Solution()
print(slt.maxSlidingWindow(nums, k))
