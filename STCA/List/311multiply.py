from typing import List


class Solution:

    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        row1 = len(mat1)
        row2 = len(mat2)
        # row2 与 col1 相等
        col1 = len(mat1[0])
        col2 = len(mat2[0])

        res = [[0] * col2 for _ in range(row1)]

        # i,j 为res的下标
        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    # k为 row2 和 col1
                    # 对于mat1 先动列即k
                    # 对于mat2 先动行即k
                    res[i][j] += mat1[i][k] * mat2[k][j]

        return res


mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
slt = Solution()
print(slt.multiply(mat1, mat2))
