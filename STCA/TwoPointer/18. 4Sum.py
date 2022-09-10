from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        sortedNums = sorted(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and sortedNums[j] == sortedNums[j - 1]:
                    continue

                l = j + 1
                r = n - 1
                nowTarget = target - sortedNums[i] - sortedNums[j]

                while l < r:
                    total = sortedNums[l] + sortedNums[r]
                    if total == nowTarget:
                        res.append([sortedNums[i], sortedNums[j], sortedNums[l], sortedNums[r]])

                        while l < r and sortedNums[l] == sortedNums[l + 1]:
                            l += 1
                        while l < r and sortedNums[r - 1] == sortedNums[r]:
                            r -= 1

                        l += 1
                        r -= 1

                    elif total > nowTarget:
                        r -= 1
                    else:
                        l += 1

        return res


nums = [1, 0, -1, 0, -2, 2]
target = 0
slt = Solution()
print(slt.fourSum(nums, target))
