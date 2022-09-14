from collections import deque
from typing import List


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ascQueue = deque()
        descQueue = deque()
        left = 0
        res = 0

        for right in range(n):
            while ascQueue and nums[ascQueue[-1]] > nums[right]:
                ascQueue.pop()
            ascQueue.append(right)

            while descQueue and nums[descQueue[-1]] < nums[right]:
                descQueue.pop()
            descQueue.append(right)

            while left < right and nums[descQueue[0]] - nums[ascQueue[0]] > limit:
                if ascQueue[0] == left:
                    ascQueue.popleft()
                if descQueue[0] == left:
                    descQueue.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res


nums = [10, 1, 2, 4, 7, 2]
limit = 5
slt = Solution()
print(slt.longestSubarray(nums, limit))