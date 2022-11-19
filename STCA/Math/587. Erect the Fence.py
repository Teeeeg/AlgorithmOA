from typing import List


class Solution:

    def getRotation(self, A, B, C):
        return ((B[1] - A[1]) * (C[0] - A[0])) - ((B[0] - A[0]) * (C[1] - A[1]))

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) < 3:
            return trees

        sortedTrees = sorted(trees, key=lambda x: (x[0], x[1]))

        n = len(sortedTrees)
        uppers = []
        uppers.append(sortedTrees[0])
        uppers.append(sortedTrees[1])

        for i in range(2, n):
            while len(uppers) >= 2 and self.getRotation(uppers[-1], uppers[-2], sortedTrees[i]) < 0:
                uppers.pop()

            uppers.append(sortedTrees[i])

        lowers = []
        lowers.append(sortedTrees[-1])
        lowers.append(sortedTrees[-2])

        for i in range(n - 3, -1, -1):
            while len(lowers) >= 2 and self.getRotation(lowers[-1], lowers[-2], sortedTrees[i]) < 0:
                lowers.pop()

            lowers.append(sortedTrees[i])

        for lower in lowers:
            if lower in uppers:
                continue

            uppers.append(lower)

        return uppers


points = [[3, 7], [6, 8], [7, 8], [11, 10], [4, 3], [8, 5], [7, 13], [4, 13]]
slt = Solution()
print(slt.outerTrees(points))