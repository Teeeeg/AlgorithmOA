from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        num2Len = {}
        res = 0

        for num in nums:
            if num in num2Len:
                continue

            leftLen = num2Len.get(num - 1, 0)
            rightLen = num2Len.get(num + 1, 0)
            curLen = leftLen + rightLen + 1

            num2Len[num] = curLen
            num2Len[num - leftLen] = curLen
            num2Len[num + rightLen] = curLen

            res = max(res, curLen)

        return res


class DisjointSet:

    def __init__(self) -> None:
        self.root = {}
        self.sizeOfRoot = {}

    def find(self, x):
        if x != self.root.get(x, x):
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        self.add(y)
        if not self.contains(x):
            return

        rootOfX = self.find(x)
        rootOfY = self.find(y)
        if rootOfX != rootOfY:
            self.root[rootOfY] = rootOfX
            self.sizeOfRoot[rootOfX] += self.sizeOfRoot[rootOfY]

    def add(self, x):
        if x not in self.root:
            self.root[x] = x
            self.sizeOfRoot[x] = 1

    def getSizes(self):
        return self.sizeOfRoot.values()

    def contains(self, x):
        return x in self.root


class Solution1:

    def longestConsecutive(self, nums: List[int]) -> int:
        disjointSet = DisjointSet()
        for num in nums:
            disjointSet.union(num - 1, num)
            disjointSet.union(num + 1, num)

        sizes = disjointSet.getSizes()
        return max(sizes) if sizes else 0


nums = []
slt = Solution1()
print(slt.longestConsecutive(nums))