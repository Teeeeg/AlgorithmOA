from typing import List


class Solution:

    def allPathsSourceTargetCore(self, path, target, graph, visited, res):
        if path[-1] == target:
            res.append(list(path))
            return

        for nbr in graph[path[-1]]:
            visited[nbr] = 1
            path.append(nbr)
            self.allPathsSourceTargetCore(path, target, graph, visited, res)
            path.pop()
            visited[nbr] = 0

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        visited = [0] * len(graph)

        self.allPathsSourceTargetCore([0], target, graph, visited, res)

        return res


graph = [[1, 2], [3], [3], []]
slt = Solution()
print(slt.allPathsSourceTarget(graph))