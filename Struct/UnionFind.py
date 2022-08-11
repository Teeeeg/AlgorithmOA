class DisjointSet:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        # 递归返回会更新节点
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)