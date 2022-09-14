from collections import deque
from typing import Deque, Dict, List


class Solution:

    def getNeighbors(self, digits: str):
        res = []
        listDigits = list(digits)

        for i in range(len(listDigits)):
            orgDigit = int(listDigits[i])
            nextDigit = (orgDigit + 1) % 10
            nextDigit1 = (orgDigit - 1 + 10) % 10
            listDigits[i] = str(nextDigit)
            res.append(''.join(listDigits))
            listDigits[i] = str(nextDigit1)
            res.append(''.join(listDigits))

            listDigits[i] = str(orgDigit)

        return res

    def bfs(self, deadends: List[str], queue: Deque[str], dist: Dict, dist1: Dict):
        for _ in range(len(queue)):
            curDigit = queue.popleft()
            for neighbor in self.getNeighbors(curDigit):
                if neighbor in deadends or neighbor in dist:
                    continue

                if neighbor in dist1:
                    return dist[curDigit] + dist1[neighbor] + 1

                dist[neighbor] = dist[curDigit] + 1
                queue.append(neighbor)

        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' == target:
            return 0

        if target in deadends or '0000' in deadends:
            return -1

        dist = {'0000': 0}
        dist1 = {target: 0}
        queue = deque(['0000'])
        queue1 = deque([target])

        while queue or queue1:
            if len(queue) > len(queue1):
                queue1, queue = queue, queue1
                dist, dist1 = dist1, dist

            res = self.bfs(deadends, queue, dist, dist1)
            if res != -1:
                return res
            res = self.bfs(deadends, queue1, dist1, dist)
            if res != -1:
                return res

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

slt = Solution()
print(slt.openLock(deadends, target))
# print(slt.getNeighbors('0000'))