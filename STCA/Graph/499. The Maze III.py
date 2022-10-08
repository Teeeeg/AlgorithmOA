from collections import deque
from typing import List


class GridType:
    WALL = 1


# directions
DIRS = {'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), 'd': (1, 0)}


class Solution:

    def isBoarderOrWall(self, maze: List[List[int]], x: int, y: int):
        if not 0 <= x < len(maze) or not 0 <= y < len(maze[0]):
            return True

        if maze[x][y] == GridType.WALL:
            return True

        return False

    def kickTheBall(self, maze: List[List[int]], hole, x, y, dir):
        deltaX, deltaY = DIRS[dir]

        while (x, y) != hole and not self.isBoarderOrWall(maze, x, y):
            x += deltaX
            y += deltaY

        if (x, y) == hole:
            return hole

        return (x - deltaX, y - deltaY)

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        if not ball or not hole:
            return 'impossible'
        if not maze or not maze[0]:
            return 'impossible'

        holeTup = (hole[0], hole[1])
        dist = {(ball[0], ball[1]): (0, '')}
        queue = deque([(ball[0], ball[1])])

        while queue:
            x, y = queue.popleft()
            if holeTup == (x, y):
                return dist[(x, y)][1]

            for dir in DIRS:
                nextX, nextY = self.kickTheBall(maze, holeTup, x, y, dir)
                newDist = dist[(x, y)][0] + abs(x - nextX) + abs(nextY - y)
                newPath = dist[(x, y)][1] + dir
                if (nextX, nextY) in dist and dist[(nextX, nextY)] <= (newDist, newPath):
                    continue
                dist[(nextX, nextY)] = (newDist, newPath)  # type: ignore
                queue.append((nextX, nextY))

        return 'impossible'


maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
ball = [4, 3]
hole = [0, 1]
slt = Solution()
print(slt.findShortestWay(maze, ball, hole))