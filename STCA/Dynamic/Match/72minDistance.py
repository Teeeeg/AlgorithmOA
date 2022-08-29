class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        opt = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            opt[i][0] = i
        for i in range(1, n2 + 1):
            opt[0][i] = i

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                context = 1 if word1[i - 1] != word2[j - 1] else 0
                opt[i][j] = min(opt[i][j - 1] + 1, opt[i - 1][j] + 1, opt[i - 1][j - 1] + context)

        return opt[-1][-1]


word1 = "horse"
word2 = "ros"
slt = Solution()
print(slt.minDistance(word1, word2))