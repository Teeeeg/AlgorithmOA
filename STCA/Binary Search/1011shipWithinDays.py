from typing import List


class Solution:

    def isValid(self, weights: List[int], days: int, capacity: int):
        count = 1
        partial = 0

        for weight in weights:
            if partial + weight <= capacity:
                partial += weight
            else:
                count += 1
                partial = weight

        return count <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight = max(weights)
        sumWeight = sum(weights)
        left = maxWeight
        right = sumWeight
        res = sumWeight

        # binary search
        while left <= right:
            mid = (left + right) >> 1
            if self.isValid(weights, days, mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
slt = Solution()
print(slt.shipWithinDays(weights, days))
