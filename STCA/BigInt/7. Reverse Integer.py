class Solution:

    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        flag = 1
        if x < 0:
            flag = -1

        res = 0

        while x:
            # negative should mod -10
            digit = x % (flag * 10)
            x = int(x / 10)

            if res > (MAX // 10) or res == (MAX // 10) and digit > 7:
                return 0

            if res < int(MIN / 10) or res == int(MIN / 10) and digit < -8:
                return 0

            res = res * 10 + digit

        return res
