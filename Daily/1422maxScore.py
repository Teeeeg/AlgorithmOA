class Solution:

    def maxScore(self, s: str) -> int:
        n = len(s)

        ones = s.count('1')
        res = 0
        oneCount = 0

        for i in range(n - 1):
            if s[i] == '1':
                oneCount += 1
            score = i + 1 - oneCount + ones - oneCount
            res = max(res, score)

        return res


s = "00"
s1 = "00111"
slt = Solution()
print(slt.maxScore(s))
print(slt.maxScore(s1))
