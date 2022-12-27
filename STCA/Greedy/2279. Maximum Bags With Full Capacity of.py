from typing import List


class Solution:

    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        needs = [0] * n

        for i in range(n):
            needs[i] = capacity[i] - rocks[i]

        needs.sort()
        res = 0

        for need in needs:
            if need >= 0 and need <= additionalRocks:
                additionalRocks -= need
                res += 1

        return res


capacity = [54, 18, 91, 49, 51, 45, 58, 54, 47, 91, 90, 20, 85, 20, 90, 49, 10, 84, 59, 29, 40, 9, 100, 1, 64, 71, 30, 46, 91]
rocks = [14, 13, 16, 44, 8, 20, 51, 15, 46, 76, 51, 20, 77, 13, 14, 35, 6, 34, 34, 13, 3, 8, 1, 1, 61, 5, 2, 15, 18]
additionalRocks = 77
slt = Solution()
print(slt.maximumBags(capacity, rocks, additionalRocks))