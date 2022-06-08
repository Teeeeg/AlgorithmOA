from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            matrix[row] = [0] * n

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # 用第一行第一列标记
        # 因此会丢失原先的数据，先记录是否第一行第一列可以为0
        rowFlag = False
        colFlag = False
        # 第一列
        for i in range(m):
            if matrix[i][0] == 0:
                colFlag = True
                break
        # 第一列
        for i in range(n):
            if matrix[0][i] == 0:
                rowFlag = True
                break
        # 用第一行第一列标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 置0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        # 第一行
        if rowFlag:
            matrix[0] = [0] * n
        # 第一列
        if colFlag:
            for i in range(m):
                matrix[i][0] = 0
