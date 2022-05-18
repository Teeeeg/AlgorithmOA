from collections import defaultdict
from typing import List


class Solution:

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        inDegrees = [0] * numCourses
        # graph 表示学完i课程之后可以学哪些课程[]
        graph = defaultdict(list)
        res = []

        for p in prerequisites:
            # 休0需要1 则 1->0
            inDegrees[p[0]] += 1
            # graph 为出度表
            graph[p[1]].append(p[0])

        # 遍历获得入度为0的课程
        # 从这些课程出发
        queue = []
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.pop(0)
            # 每学一个课程记录下
            res.append(cur)
            for post in graph[cur]:
                inDegrees[post] -= 1
                if inDegrees[post] == 0:
                    queue.append(post)

        return len(res) == numCourses


numCourses = 2
prerequisites = [[1, 0]]
slt = Solution()
print(slt.canFinish(numCourses, prerequisites))
