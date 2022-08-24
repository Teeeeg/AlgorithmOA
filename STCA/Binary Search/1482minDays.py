from typing import List


class Solution:

    def isValid(self, bloomDay: List[int], m: int, k: int, day: int):
        count = 0
        partial = 0

        for bloom in bloomDay:
            if bloom <= day:
                partial += 1
                # if it is bigger than k
                # increment count and minus k
                if partial >= k:
                    partial -= k
                    count += 1
            else:
                # else set to zero
                partial = 0

        return count >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        res = right + 1
        # binary search
        while left <= right:
            mid = (left + right) >> 1
            if self.isValid(bloomDay, m, k, mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res if res != max(bloomDay) + 1 else -1


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
slt = Solution()
print(slt.minDays(bloomDay, m, k))
