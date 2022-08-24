from typing import List


class Solution:
    # greedy approach
    # if is less than target, add it into the bucket
    def isValid(self, nums: List[int], target, m):
        n = len(nums)
        # initial size is 1
        res = 1
        partial = 0

        for num in nums:
            if partial + num <= target:
                partial += num
            else:
                res += 1
                partial = num
        # if res is eaqual to m
        # if res is less than m. It means if expand the bucket size, each sum will be smaller
        return res <= m

    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        res = right

        # binary search
        while left <= right:
            mid = (left + right) >> 1
            if self.isValid(nums, mid, m):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res


nums = [7, 2, 5, 10, 8]
m = 2
slt = Solution()
print(slt.splitArray(nums, m))
