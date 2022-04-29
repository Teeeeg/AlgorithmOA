from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph or not graph[0]:
            return []

        n = len(graph)
        res = []
        self.allPathsSourceTargetCore(graph, 0, n-1, [], res)

        return res

    def allPathsSourceTargetCore(self, graph, src, dest, path, res):
        path = path[:]
        path.append(src)
        if src == dest:
            res.append(path)
            return

        for vertex in graph[src]:
            self.allPathsSourceTargetCore(
                graph, vertex, dest, path, res)
        path.pop()


graph = [[1, 2], [3], [3], []]
solution = Solution()
print(solution.allPathsSourceTarget(graph))
