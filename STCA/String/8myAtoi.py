class Solution:

    def myAtoi(self, s: str) -> int:
        MIN = -(1 << 31)
        MAX = (1 << 31) - 1

        n = len(s)
        i = 0
        sign = 1

        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        if s[i] == '+':
            sign = 1
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        res = 0
        for k in range(i, n):
            digit = s[k]
            if not '0' <= digit <= '9':
                break

            digit = sign * int(digit)

            if res > MAX // 10 or (res == MAX // 10 and digit > 7):
                return MAX
            if res < int(MIN / 10) or (res == int(MIN / 10) and digit < -8):
                return MIN

            res = res * 10 + digit

        return res


s = ""
slt = Solution()
print(slt.myAtoi(s))