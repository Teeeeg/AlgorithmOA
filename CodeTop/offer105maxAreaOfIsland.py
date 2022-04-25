from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]:
                    res = max(res, self.getArea1(grid, i, j, visited))

        return res

    # 广度优先
    def getArea(self, grid, i, j, visited):
        m = len(grid)
        n = len(grid[0])
        stack = [(i, j)]
        area = 0
        visited[i][j] = True
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        while stack:
            i, j = stack.pop()
            area += 1
            for dir in dirs:
                newI, newJ = i+dir[0], j+dir[1]
                if isValid(newI, newJ) and grid[newI][newJ] and not visited[newI][newJ]:
                    visited[newI][newJ] = True
                    stack.append((newI, newJ))
        return area

    # 递归
    def getArea1(self, grid, i, j, visited):
        m = len(grid)
        n = len(grid[0])
        area = 0
        visited[i][j] = True

        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for dir in dirs:
            newI, newJ = i+dir[0], j+dir[1]
            if isValid(newI, newJ) and grid[newI][newJ] and not visited[newI][newJ]:
                area += self.getArea(grid, newI, newJ, visited)

        return area + 1


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

grid1 = [[1, 1], [1, 1]]
solution = Solution()
print(solution.maxAreaOfIsland(grid))
