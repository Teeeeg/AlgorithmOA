from typing import List


class Solution:
    # 可以想象成链表
    # 环形链表找入口点
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        # 一步两步
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # 如果相等，则有重复点
            if slow == fast:
                # 用p从头出发
                p = 0
                inLoop = slow
                while p != inLoop:
                    p = nums[p]
                    inLoop = nums[inLoop]
                return p


nums = [8, 7, 1, 10, 17, 15, 18, 11, 16, 9, 19, 12, 5, 14, 3, 4, 2, 13, 18, 18]
slt = Solution()
print(slt.findDuplicate(nums))