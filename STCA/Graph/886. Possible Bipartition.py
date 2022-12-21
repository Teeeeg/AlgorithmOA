from collections import deque
from typing import List


class Solution:

    def buildGraph(self, n: int, dislikes: List[List[int]]):
        graph = {i: set() for i in range(1, n + 1)}
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)

        return graph

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True

        p2Index = [0] * (n + 1)
        graph = self.buildGraph(n, dislikes)

        for i in range(1, n + 1):
            if p2Index[i] != 0:
                continue

            queue = deque()
            queue.append(i)
            p2Index[i] = 1

            while queue:
                cur = queue.popleft()
                for neighbor in graph[cur]:
                    if p2Index[cur] == p2Index[neighbor] and p2Index[neighbor] != 0:
                        return False
                    if p2Index[neighbor] != 0:
                        continue
                    p2Index[neighbor] = 1 if p2Index[cur] == 2 else 2
                    queue.append(neighbor)
        return True


n = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
slt = Solution()
print(slt.possibleBipartition(n, dislikes))
