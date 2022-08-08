from typing import List


class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # opt[i] repsent LIS of the sequence ends with nums[i]
        opt = [1] * n
        # count[i] repsent LIS count of the sequnce ends with nums[i]
        count = [1] * n
        maxLen = 0
        res = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # update opt and count
                    if opt[j] + 1 > opt[i]:
                        opt[i] = opt[j] + 1
                        # count begin from count[j]
                        count[i] = count[j]
                    # if it is the same length, add it to count[i]
                    elif opt[i] == opt[j] + 1:
                        count[i] += count[j]
                # record the maxLen
                if opt[i] > maxLen:
                    maxLen = opt[i]

        # get all the count
        for i in range(n):
            if opt[i] == maxLen:
                res += count[i]

        return res


nums = [1, 3, 5, 4, 7]
slt = Solution()
print(slt.findNumberOfLIS(nums))