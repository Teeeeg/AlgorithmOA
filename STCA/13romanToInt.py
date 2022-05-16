class Solution:

    def romanToInt(self, s: str) -> int:
        dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        n = len(s)
        res = 0

        for i in range(n - 1):
            if dct[s[i]] < dct[s[i + 1]]:
                res -= dct[s[i]]
            else:
                res += dct[s[i]]

        res += dct[s[-1]]

        return res


s = 'LVIII'
slt = Solution()
print(slt.romanToInt(s))