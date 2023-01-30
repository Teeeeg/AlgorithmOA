from typing import List


class Solution:

    def getGraph(self, parent):
        n = len(parent)
        graph = {i: set() for i in range(n)}

        for i in range(n):
            if parent[i] == -1:
                continue

            graph[parent[i]].add(i)

        return graph

    def longestPathCore(self, graph, cur, visited, s, res):
        lengths = []

        for nbr in graph[cur]:
            if visited[nbr]:
                continue

            visited[nbr] = 1
            lengths.append((nbr, self.longestPathCore(graph, nbr, visited, s, res)))

        curLongest = 1
        curLine = 1
        lengths.sort(key=lambda x: x[1], reverse=True)
        count = 0

        for index, length in lengths:
            if s[index] != s[cur]:
                if count < 2:
                    count += 1
                    curLongest += length

                curLine = max(curLine, 1 + length)

        res['longest'] = max(res['longest'], curLongest)
        return curLine

    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = self.getGraph(parent)
        visited = [0] * n
        visited[0] = 1
        res = {'longest': 0}

        self.longestPathCore(graph, 0, visited, s, res)

        return res['longest']


parent = [
    -1, 137, 65, 60, 73, 138, 81, 17, 45, 163, 145, 99, 29, 162, 19, 20, 132, 132, 13, 60, 21, 18, 155, 65, 13, 163, 125, 102, 96, 60, 50, 101, 100, 86, 162, 42, 162, 94, 21, 56, 45, 56, 13, 23, 101,
    76, 57, 89, 4, 161, 16, 139, 29, 60, 44, 127, 19, 68, 71, 55, 13, 36, 148, 129, 75, 41, 107, 91, 52, 42, 93, 85, 125, 89, 132, 13, 141, 21, 152, 21, 79, 160, 130, 103, 46, 65, 71, 33, 129, 0, 19,
    148, 65, 125, 41, 38, 104, 115, 130, 164, 138, 108, 65, 31, 13, 60, 29, 116, 26, 58, 118, 10, 138, 14, 28, 91, 60, 47, 2, 149, 99, 28, 154, 71, 96, 60, 106, 79, 129, 83, 42, 102, 34, 41, 55, 31,
    154, 26, 34, 127, 42, 133, 113, 125, 113, 13, 54, 132, 13, 56, 13, 42, 102, 135, 130, 75, 25, 80, 159, 39, 29, 41, 89, 85, 19
]
s = "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"

slt = Solution()
print(slt.longestPath(parent, s))
