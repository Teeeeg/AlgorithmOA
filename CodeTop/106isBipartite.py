from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n
        for vertex in range(n):
            if colors[vertex] == -1:
                if not self.setColor(graph, colors, vertex, 0):
                    return False

        return True

    def setColor(self, graph, colors, vertex, color):
        queue = []
        queue.append(vertex)
        colors[vertex] = color

        while queue:
            vertex = queue.pop()
            for nextV in graph[vertex]:
                if colors[nextV] == -1:
                    colors[nextV] = 1 - colors[vertex]
                    queue.append(nextV)
                elif colors[nextV] == colors[vertex]:
                    return False

        return True


graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
solution = Solution()
print(solution.isBipartite(graph))
