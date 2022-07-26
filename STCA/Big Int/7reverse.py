class Solution:

    def reverse(self, x: int) -> int:
        MAX = (1 << 31) - 1
        MIN = -(1 << 31)

        res = 0

        while x:
            digit = x % 10 if x >= 0 else x % (-10)
            x = x // 10 if x >= 0 else int(x / 10)

            if res > (MAX // 10) or (res == MAX // 10 and digit > 7):
                return 0
            if res < int(MIN / 10) or (res == int(MIN / 10) and digit < -8):
                return 0

            res = res * 10 + digit

        return res


s = Solution()
print(s.reverse(-123))

print(1 << 31)
print((1 << 31) - 1)