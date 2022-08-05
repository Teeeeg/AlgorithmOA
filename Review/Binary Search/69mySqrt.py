class Solution:

    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid**2 == x:
                return int(mid)
            if mid**2 < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


slt = Solution()
print(slt.mySqrt(8))
