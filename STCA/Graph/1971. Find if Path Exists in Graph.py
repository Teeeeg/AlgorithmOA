from collections import deque
from typing import List


class Solution:

    def buildGraph(self, edges: List[List[int]], n: int):
        graph = {i: [] for i in range(n)}

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        return graph

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = self.buildGraph(edges, n)
        queue = deque()
        visited = [0] * n
        queue.append(source)

        while queue:
            cur = queue.popleft()

            for child in graph[cur]:
                if visited[child]:
                    continue

                if child == destination:
                    return True

                visited[child] = 1
                queue.append(child)

        return False


n = 1
edges = []
source = 0
destination = 0

slt = Solution()
print(slt.validPath(n, edges, source, destination))