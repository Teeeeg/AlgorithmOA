import math
from typing import List


class Solution:

    def isValid(self, h: int, k: int):
        time = 0
        for pile in self.piles:
            if time <= h:
                time += math.ceil(pile / k)
            else:
                return False
        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = sorted(piles)
        maxPile = max(piles)
        left = 1
        right = maxPile
        res = maxPile

        while left <= right:
            mid = (left + right) >> 1
            if self.isValid(h, mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res


piles = [30, 11, 23, 4, 20]
h = 6
slt = Solution()
print(slt.minEatingSpeed(piles, h))
