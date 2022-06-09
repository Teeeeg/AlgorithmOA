from typing import List


class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # 2 未上色， 0, 1
        colors = [2] * n

        # 要从每一个节点出发综合判断
        for i in range(n):
            queue = [i]
            while queue:
                n = len(queue)
                for _ in range(n):
                    cur = queue.pop(0)
                    for post in graph[cur]:
                        if colors[post] == 2:
                            # 上不同的色
                            colors[post] = 1 - colors[cur]
                            queue.append(post)
                        # 若同一边有相同色则False
                        elif colors[post] == colors[cur]:
                            return False

        return True


graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
         [2, 4, 5, 6, 7, 8]]
slt = Solution()
print(slt.isBipartite(graph))