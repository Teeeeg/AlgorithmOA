from typing import (
    List,)


class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def getCount(self, woods: List[int], length):
        count = 0
        for wood in woods:
            count += wood // length

        return count

    def wood_cut(self, woods: List[int], k: int) -> int:
        if not woods:
            return 0

        left = 1
        right = max(woods)

        while left + 1 < right:
            mid = (left + right) // 2
            curCount = self.getCount(woods, mid)

            if curCount >= k:
                left = mid
            else:
                right = mid

        if self.getCount(woods, right) >= k:
            return right
        if self.getCount(woods, left) >= k:
            return left

        return 0


woods = [232, 124, 456]
k = 7
slt = Solution()
print(slt.wood_cut(woods, k))