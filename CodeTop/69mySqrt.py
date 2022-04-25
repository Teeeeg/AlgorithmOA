class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid+1
            else:
                right = mid-1

        return left


x = 8
solution = Solution()
print(solution.mySqrt(x))
