from typing import List


class Solution:

    def getGraph(self, n, edges):
        graph = {i: set() for i in range(n)}

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        return graph

    def minTimeCore(self, graph, cur, hasApple, visited):
        time = 0

        for nbr in graph[cur]:
            if nbr in visited:
                continue

            visited.add(nbr)
            time += self.minTimeCore(graph, nbr, hasApple, visited)

        if time > 0:
            return time + 2

        return 2 if hasApple[cur] else 0

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = self.getGraph(n, edges)
        visited = set()
        visited.add(0)

        return max(self.minTimeCore(graph, 0, hasApple, visited) - 2, 0)


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]
slt = Solution()
print(slt.minTime(n, edges, hasApple))