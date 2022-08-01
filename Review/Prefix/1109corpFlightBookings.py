from typing import List


class Solution:
    # diffrence array
    # reduce to O(2m*n)

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        # if [left, right] + num
        # to diffrence array
        # boundry diffrence will be (left +num, right+1 -num)

        for left, right, num in bookings:
            res[left - 1] += num
            if right < n:
                res[right] -= num

        # sums up it's the original array
        for i in range(1, n):
            res[i] += res[i - 1]

        return res


bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
slt = Solution()
print(slt.corpFlightBookings(bookings, n))
