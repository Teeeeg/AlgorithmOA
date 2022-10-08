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


class Solution1:
    # merge sort

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        sortedHouses = sorted(houses)
        sortedHeaters = sorted(heaters)
        n1 = len(sortedHouses)
        n2 = len(sortedHeaters)
        i = 0
        j = 0
        res = 0

        while i < n1 and j < n2:
            cur = abs(sortedHouses[i] - sortedHeaters[j])
            post = abs(sortedHouses[i] - sortedHeaters[j + 1]) if j + 1 < n2 else 10**9 + 7

            if cur < post:
                res = max(res, cur)
                i += 1
            else:
                # next heater is smaller
                # go to next iteration
                j += 1

        while i < n1:
            res = max(res, abs(sortedHouses[i] - sortedHeaters[-1]))
            i += 1

        return res


houses = [1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999]
heaters = [499, 500, 501]
slt = Solution1()
print(slt.findRadius(houses, heaters))