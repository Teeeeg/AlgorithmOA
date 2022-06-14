class Solution:

    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        rCount = 0
        lCount = 0
        res = 0

        for i in range(n):
            if s[i] == 'R':
                rCount += 1
            else:
                lCount += 1
            if lCount == rCount:
                res += 1
                lCount = 0
                rCount = 0

        return res


s = 'RLLLLRRRLR'
slt = Solution()
print(slt.balancedStringSplit(s))