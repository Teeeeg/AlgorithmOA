class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = left + (right - left) // 2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1

        return right


solution = Solution()
print(solution.mySqrt(1))
