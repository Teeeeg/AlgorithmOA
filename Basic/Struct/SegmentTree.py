from typing import List


class SegmentTree:

    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.size = len(nums)
        # n leaf nodes has no more than 4*n total nodes
        self.tree = [0] * (self.size * 4)
        self.build(0, 0, self.size - 1)

    # tIndex is the index of tree
    # left, right is the bound of nodes
    # also, if left == right, it's the actual value in nums
    def build(self, tIndex, left, right):
        # find leaf node, update it
        if left == right:
            self.tree[tIndex] = self.nums[left]
            return

        mid = (left + right) // 2
        self.build(tIndex * 2 + 1, left, mid)
        self.build(tIndex * 2 + 2, mid + 1, right)
        # update from the bottom
        self.tree[tIndex] = self.tree[tIndex * 2 + 1] + self.tree[tIndex * 2 + 2]

    def queryCore(self, tIndex, left, right, qLeft, qRight):
        # off the grid
        if qLeft > right or qRight < left:
            return 0
        # in this case, query includes it
        if qLeft <= left and qRight >= right:
            return self.tree[tIndex]

        mid = (left + right) // 2

        leftRes = self.queryCore(tIndex * 2 + 1, left, mid, qLeft, qRight)
        rightRes = self.queryCore(tIndex * 2 + 2, mid + 1, right, qLeft, qRight)

        return leftRes + rightRes

    def query(self, qLeft, qRight):
        return self.queryCore(0, 0, self.size - 1, qLeft, qRight)

    def updateCore(self, tIndex, left, right, tLeft, tRight, value):
        # off grid
        if tLeft > right or tRight < left:
            return

        if tLeft <= left and tRight >= right:
            self.tree[tIndex] += (right - left + 1) * value
            return

        mid = (left + right) // 2

        self.updateCore(tIndex * 2 + 1, left, mid, tLeft, tRight, value)
        self.updateCore(tIndex * 2 + 2, mid + 1, right, tLeft, tRight, value)

    def updateSegment(self, tLeft, tRight, value):
        self.updateCore(0, 0, self.size - 1, tLeft, tRight, value)

    def update(self, index, value):
        self.updateCore(0, 0, self.size - 1, index, index, value)


nums = [0, 1, 3, 4, 6]
segTree = SegmentTree(nums)
print(segTree.query(2, 4))
# segTree.update(3, 4)
segTree.updateSegment(2, 4, 4)
print(segTree.query(2, 4))