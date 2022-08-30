from typing import List


class Solution:

    def getSum(self, prefixSum: List[int], i, j):
        return prefixSum[j + 1] - prefixSum[i]

    def stone_game(self, stones: List[int]) -> int:
        if not stones:
            return 0

        n = len(stones)
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + stones[i]

        opt = [[10**9] * n for _ in range(n)]
        for i in range(n):
            opt[i][i] = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    # merge [i: k] and [k+1: j]
                    opt[i][j] = min(opt[i][j], opt[i][k] + opt[k + 1][j] + self.getSum(prefixSum, i, j))

        return opt[0][n - 1]


stones = [3, 4, 3]
slt = Solution()
print(slt.stone_game(stones))
