from typing import List


class Solution:

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # simulate a clock-wise rotation
        dirX = [0, 1, 0, -1]
        dirY = [1, 0, -1, 0]
        # dir represent the current direction
        dir = 0
        x = 0
        y = 0
        res = 0
        obstSet = set()

        for obst in obstacles:
            obstSet.add((obst[0], obst[1]))

        for cmd in commands:
            if cmd >= 0:
                for i in range(cmd):
                    if (x + dirX[dir], y + dirY[dir]) in obstSet:
                        break
                    x += dirX[dir]
                    y += dirY[dir]
            # +1 to turn right
            elif cmd == -1:
                dir = (dir + 1) % 4
            else:
                # -1 to turn left
                # use +4 to remember
                dir = (dir - 1 + 4) % 4

            res = max(res, x**2 + y**2)

        return res


commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
slt = Solution()
print(slt.robotSim(commands, obstacles))
