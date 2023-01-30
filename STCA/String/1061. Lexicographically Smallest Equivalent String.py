class DisjointSet:

    def __init__(self) -> None:
        self.root = {}

    def add(self, x):
        if x in self.root:
            return False

        self.root[x] = x
        return True

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX < rootY:
            self.root[rootY] = rootX
        elif rootX > rootY:
            self.root[rootX] = rootY


class Solution:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        disjointSet = DisjointSet()

        for i in range(n):
            disjointSet.add(s1[i])
            disjointSet.add(s2[i])

            disjointSet.union(s1[i], s2[i])

        res = []

        for char in baseStr:
            if char in disjointSet.root:
                res.append(disjointSet.find(char))
                continue

            res.append(char)

        return ''.join(res)


s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
slt = Solution()
print(slt.smallestEquivalentString(s1, s2, baseStr))