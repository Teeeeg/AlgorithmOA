from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.recursiveCore(graph, 0, [], res)
        return res

    def recursiveCore(self, graph, vertex, path, res):
        path.append(vertex)

        if vertex == len(graph)-1:
            res.append(path[:])
            return

        for child in graph[vertex]:
            self.recursiveCore(graph, child, path, res)

        path.pop()


graph = [[1, 2], [3], [3], []]
solution = Solution()
print(solution.allPathsSourceTarget(graph))
