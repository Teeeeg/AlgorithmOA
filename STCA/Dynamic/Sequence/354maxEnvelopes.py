from typing import List


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        # such as (2, 1) (3, 2), (3, 3) -> (2, 1) (3, 3), (3, 2)
        # in (3, 1), (3, 2) won't suit
        # in (3, 2), (3, 1) always use (3, 2) conver to LIS
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        opt = [10**9] * (n + 1)
        opt[0] = -(10**9)
        res = -1

        for _, h in envelopes:
            index = self.getGTE(opt, h)
            opt[index] = h
            res = max(res, index)

        return res

    def getGTE(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        # res = -1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
slt = Solution()
print(slt.maxEnvelopes(envelopes))