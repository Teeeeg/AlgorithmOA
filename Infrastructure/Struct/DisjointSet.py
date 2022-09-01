class DisjointSet:

    def __init__(self) -> None:
        self.root = {}

    def find(self, x):
        if x == self.root.get(x, x):
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.root[rootY] = rootX

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)