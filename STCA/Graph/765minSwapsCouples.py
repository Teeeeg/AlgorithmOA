from typing import List


class Solution:
    # couple is [0, 1], [2, 3]
    # a even then the next odd
    # give a even to get its couple: num + 1
    # give a odd to get its couple: num - 1
    def getAnother(self, num):
        if num % 2:
            return num - 1
        else:
            return num + 1

    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        dct = {}
        # use dct to record {num, index} to reduce one iteration
        for i, num in enumerate(row):
            dct[num] = i
        res = 0

        for i in range(0, n, 2):
            another = self.getAnother(row[i])
            index = dct[another]
            if i + 1 == index:
                continue
            # update row[i+1]'s position
            dct[row[i + 1]] = index
            row[index] = row[i + 1]
            row[i + 1] = another
            res += 1
        return res


class DisjointSet:

    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.count = 0

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.count += 1

    def getCount(self):
        return self.count


class Solution1:
    # [0, 1] -> 0, [2, 3] -> 1, [4, 5] -> 2 ....
    # for every num, its coupleID comes to num // 2
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        uf = DisjointSet(n)
        for i in range(0, n, 2):
            uf.union(row[i] // 2, row[i + 1] // 2)
        return uf.getCount()


row = [0, 2, 4, 6, 7, 1, 3, 5]
slt = Solution1()
print(slt.minSwapsCouples(row))