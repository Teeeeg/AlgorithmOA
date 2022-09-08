class Solution:

    def numTrees(self, n: int) -> int:
        opt = [0] * (n + 1)
        opt[0] = 1
        opt[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                # divide into i-1
                opt[i] += opt[j] * opt[i - j - 1]

        return opt[-1]


n = 2
slt = Solution()
print(slt.numTrees(n))