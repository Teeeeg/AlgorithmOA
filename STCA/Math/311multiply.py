from typing import List


class Solution:

    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1 = len(mat1)
        n1 = len(mat1[0])
        m2 = len(mat2)
        n2 = len(mat2[0])

        AB = [[0] * n2 for _ in range(m1)]

        for i in range(m1):
            for j in range(n2):
                for k in range(n1):
                    AB[i][j] += mat1[i][k] * mat2[k][j]

        return AB


class Solution1:

    def getNonZeroes(self, mat: List[List[int]]):
        m = len(mat)
        n = len(mat[0])
        nonZeros = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                nonZeros.append((i, j, mat[i][j]))

        return nonZeros

    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        nonZeros1 = self.getNonZeroes(mat1)
        nonZeros2 = self.getNonZeroes(mat2)

        AB = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for x, y, val in nonZeros1:
            for x1, y1, val1 in nonZeros2:
                if not y == x1:
                    continue
                AB[x][y1] += val * val1

        return AB


mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
slt = Solution1()
print(slt.multiply(mat1, mat2))
