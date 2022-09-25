from collections import deque

# n = int(input())
# edges = [[int(x) for x in input().split()] for _ in range(n)]
# c1, c2 = map(int, input().split())


class Solution:

    def getGraph(self, edges):
        graph = {}

        for a, b in edges:
            graph[a] = graph.get(a, [])
            graph[a].append(b)

        return graph

    def bfs(self, graph, queue, visited, visited1):
        n = len(queue)

        for _ in range(n):
            cur = queue.popleft()
            if cur in visited1:
                return cur

            for neighbor in graph.get(cur, []):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)

        return -1

    def solve(self, edges, c1, c2):
        graph = self.getGraph(edges)

        queue = deque()
        queue.append(c1)
        visited = set()
        visited.add(c1)

        queue1 = deque()
        queue1.append(c2)
        visited1 = set()
        visited1.add(c2)

        while queue and queue1:
            res = self.bfs(graph, queue, visited, visited1)
            if res != -1:
                return res
            res = self.bfs(graph, queue1, visited1, visited)
            if res != -1:
                return res

        return -1


edges = [[2, 1], [3, 1], [4, 2], [5, 3]]
c1 = 4
c2 = 5
slt = Solution()
print(slt.solve(edges, c1, c2))