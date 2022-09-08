class DisjointSet:

    def __init__(self) -> None:
        self.root = {}
        self.sizeOfRoot = {}
        self.sizeOfSet = 0

    def add(self, x):
        if x in self.root:
            return False

        self.root[x] = x
        self.sizeOfSet += 1
        self.sizeOfRoot[x] = 1
        return True

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.sizeOfSet -= 1
            self.sizeOfRoot[rootX] += self.sizeOfRoot[rootY]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def getSizeOfSet(self):
        return self.sizeOfSet

    def getSizeOfRoot(self, x):
        return self.sizeOfRoot[x]

    def getAllSizes(self):
        return self.sizeOfRoot
