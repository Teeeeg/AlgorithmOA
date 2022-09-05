from heapq import heappop, heappush
from typing import List, Set


class Solution:

    def isValid(self, heightMap: List[List[int]], visited: Set, row: int, col: int, curHeight: int):
        if (row, col) not in visited and 0 <= row < len(heightMap) and 0 <= col < len(heightMap[0]):
            return True

        return False

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        visited = set()
        minHeap = []
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        for i in range(n):
            visited.add((0, i))
            visited.add((m - 1, i))
            heappush(minHeap, (heightMap[0][i], 0, i))
            heappush(minHeap, (heightMap[-1][i], m - 1, i))

        for i in range(1, m - 1):
            visited.add((i, 0))
            visited.add((i, n - 1))
            heappush(minHeap, (heightMap[i][0], i, 0))
            heappush(minHeap, (heightMap[i][-1], i, n - 1))

        while minHeap:
            curHeight, row, col = heappop(minHeap)
            for deltaX, deltaY in dirs:
                newRow = row + deltaX
                newCol = col + deltaY
                if not self.isValid(heightMap, visited, newRow, newCol, curHeight):
                    continue

                diff = curHeight - heightMap[newRow][newCol]
                if diff > 0:
                    res += diff
                visited.add((newRow, newCol))
                height = max(curHeight, heightMap[newRow][newCol])
                heappush(minHeap, (height, newRow, newCol))

        return res


heightMap = [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]
slt = Solution()
print(slt.trapRainWater(heightMap))