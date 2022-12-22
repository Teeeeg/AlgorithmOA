from collections import deque
from typing import List


class Solution:

    def buildGraph(self, n, dislikes):
        graph = {i: set() for i in range(1, n + 1)}
        for dislike in dislikes:
            graph[dislike[0]].add(dislike[1])
            graph[dislike[1]].add(dislike[0])

        return graph

    def bfs(self, graph, index, groups):
        queue = deque()
        queue.append(index)
        groups[index] = 1

        while queue:
            cur = queue.popleft()
            for nbr in graph[cur]:
                print(nbr)
                if groups[nbr] != 0 and groups[cur] == groups[nbr]:
                    return False
                if groups[nbr] != 0:
                    continue

                groups[nbr] = 1 if groups[cur] == 2 else 2
                queue.append(nbr)

        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(n, dislikes)
        groups = [0] * (n + 1)

        for i in range(1, n + 1):
            if groups[i]:
                continue

            if not self.bfs(graph, i, groups):
                return False

        return True


n = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
slt = Solution()
print(slt.possibleBipartition(n, dislikes))
