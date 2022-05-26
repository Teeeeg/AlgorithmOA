from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0

        return res


nums = [1, 0, 1, 1, 0, 1]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))