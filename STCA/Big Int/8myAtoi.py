class Solution:

    def myAtoi(self, s: str) -> int:
        MAX = (1 << 31) - 1
        MIN = -(1 << 31)

        n = len(s)
        sign = 1
        i = 0
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        res = 0
        while i < n:
            if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                break
            digit = int(s[i]) * sign
            # 先判断 res * 10 会不会越界， 若不越界，加上最后一位是否越界
            if res > MAX // 10 or (res == MAX // 10 and digit > 7):
                return MAX
            # 注意负数要向上取整
            if res < int(MIN / 10) or (res == int(MIN / 10) and digit < -8):
                return MIN

            res = res * 10 + digit
            i += 1

        return res


s = "-2147483649"
slt = Solution()
print(slt.myAtoi(s))