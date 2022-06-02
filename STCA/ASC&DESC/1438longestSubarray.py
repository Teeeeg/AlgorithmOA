from collections import deque
from typing import List


class Solution:
    # 两个单调队列分别维护最小值和最大值
    # 滑动窗口

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        # 用双端队列通过大数据集
        ascQueue = deque()
        descQueue = deque()
        res = 0
        left = 0

        for right in range(n):
            num = nums[right]
            # 维护最小值最大值
            while ascQueue and ascQueue[-1] > num:
                ascQueue.pop()
            while descQueue and descQueue[-1] < num:
                descQueue.pop()

            ascQueue.append(num)
            descQueue.append(num)

            # 若绝对值不满足条件，缩小窗口
            while ascQueue and descQueue and descQueue[0] - ascQueue[0] > limit:
                # 确认当前窗口最左侧是哪个
                # 缩小窗口的时候也要更新对应的单调队列
                if nums[left] == descQueue[0]:
                    descQueue.popleft()
                if nums[left] == ascQueue[0]:
                    ascQueue.popleft()

                left += 1

            res = max(res, right - left + 1)

        return res


nums = [10, 1, 2, 4, 7, 2]
limit = 5
slt = Solution()
print(slt.longestSubarray(nums, limit))
