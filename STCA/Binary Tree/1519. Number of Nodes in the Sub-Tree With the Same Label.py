from typing import List


class Solution:

    def getGraph(self, n, edges):
        graph = {i: set() for i in range(n)}

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        return graph

    def countSubTreesCore(self, n, graph, cur, visited, labels, res):
        curLabelCount = {}
        curLabel = labels[cur]

        for nbr in graph[cur]:
            if visited[nbr]:
                continue

            visited[nbr] = 1
            labelCount = self.countSubTreesCore(n, graph, nbr, visited, labels, res)
            for key, value in labelCount.items():
                curLabelCount[key] = curLabelCount.get(key, 0) + value

        curLabelCount[curLabel] = curLabelCount.get(curLabel, 0) + 1

        res[cur] = curLabelCount[curLabel]

        return curLabelCount

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = self.getGraph(n, edges)
        res = [0] * n
        visited = [0] * n

        visited[0] = 1
        self.countSubTreesCore(n, graph, 0, visited, labels, res)

        return res


n = 4
edges = [[0, 1], [1, 2], [0, 3]]
labels = "bbbb"
slt = Solution()
print(slt.countSubTrees(n, edges, labels))