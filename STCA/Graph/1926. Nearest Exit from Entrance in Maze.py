from collections import deque
from typing import List


class cellType:
    WALL = '+'
    OPEN = '.'


class Solution:

    def isValid(self, maze: List[List[str]], cur):
        return 0 <= cur[0] < len(maze) and 0 <= cur[1] < len(maze[0]) \
            and maze[cur[0]][cur[1]] != cellType.WALL

    def isExit(self, maze, cur: List[int]):
        return cur[0] == 0 or cur[1] == 0 or cur[0] == len(maze) - 1 or cur[1] == len(maze[0]) - 1

    def getNeighbors(self, maze: List[List[str]], cur: List[int]):
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbors = []

        for deltaX, deltaY in dirs:
            nextX = cur[0] + deltaX
            nextY = cur[1] + deltaY

            if not self.isValid(maze, (nextX, nextY)):
                continue

            neighbors.append((nextX, nextY))

        return neighbors

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        entranceTup = (entrance[0], entrance[1])
        queue.append(entranceTup)
        dist = {entranceTup: 0}

        while queue:
            cur = queue.popleft()

            for neighbor in self.getNeighbors(maze, cur):
                if neighbor in dist:
                    continue

                dist[neighbor] = dist[cur] + 1
                if self.isExit(maze, neighbor):
                    return dist[neighbor]

                queue.append(neighbor)

        return -1


maze = [["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"], ["+", ".", "+", ".", "+", ".", "+"], ["+", ".", ".", ".", "+", ".", "+"], ["+", "+", "+", "+", "+", ".", "+"]]
entrance = [0, 1]

slt = Solution()
print(slt.nearestExit(maze, entrance))