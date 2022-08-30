from typing import List


class Solution:
    # use binary search to get closest element to house
    def getMinRadius(self, heaters: List[int], house: int):
        left = 0
        right = len(heaters) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if heaters[mid] >= house:
                right = mid
            else:
                left = mid

        return min(abs(heaters[left] - house), abs(heaters[right] - house))

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        sortedHeaters = sorted(heaters)

        res = -1
        for house in houses:
            minRadius = self.getMinRadius(sortedHeaters, house)
            res = max(res, minRadius)

        return res


houses = [1, 2, 3, 4]
heaters = [1, 4]
slt = Solution()
print(slt.findRadius(houses, heaters))