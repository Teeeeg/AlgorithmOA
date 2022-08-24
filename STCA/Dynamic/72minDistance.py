class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # opt[i][j] represent word1[0: i] to word2[0: j]'s minDistance
        opt = [[0] * (n + 1) for _ in range(m + 1)]
        word1 = ' ' + word1
        word2 = ' ' + word2

        for i in range(m + 1):
            opt[i][0] = i

        for i in range(n + 1):
            opt[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # equal
                if word1[i] == word2[j]:
                    opt[i][j] = opt[i - 1][j - 1]
                else:
                    # need to be edited
                    opt[i][j] = min(opt[i - 1][j], opt[i][j - 1], opt[i - 1][j - 1]) + 1

        return opt[-1][-1]


word1 = "horse"
word2 = "ros"
slt = Solution()
print(slt.minDistance(word1, word2))
