class Node:

    def __init__(self, left=-1, right=-1, value=0, lazy=0) -> None:
        self.left = left
        self.right = right
        self.value = value
        self.lazy = lazy


# sum Tree withlazy tag
# update current node and record updates in lazy
# update it's children in need
class SegmentTree:

    def __init__(self, nums) -> None:
        self.nums = nums
        self.size = len(nums)
        self.tree = [Node() for _ in range(4 * self.size)]
        self.build(0, 0, self.size - 1)

    # update parent node
    def pushUp(self, index):
        self.tree[index].value = self.tree[index * 2 + 1].value + self.tree[index * 2 + 2].value

    # push down lazy tag
    def pushDown(self, tIndex):
        node = self.tree[tIndex]
        lazy = node.lazy
        # if parent node has lazy
        if lazy:
            leftChild = self.tree[tIndex * 2 + 1]
            rightChild = self.tree[tIndex * 2 + 2]
            # update children's lazy tag
            leftChild.lazy += lazy
            rightChild.lazy += lazy
            # update children's value
            leftChild.value += (leftChild.right - leftChild.left + 1) * lazy
            rightChild.value += (rightChild.right - rightChild.left + 1) * lazy
            # update completed, clear node's lazy tag
            node.lazy = 0

    # build normally
    def build(self, tIndex, left, right):
        if left == right:
            self.tree[tIndex].value = self.nums[left]
            return

        mid = (left + right) // 2
        self.build(tIndex * 2 + 1, left, mid)
        self.build(tIndex * 2 + 2, mid + 1, right)
        # update current node
        self.pushUp(tIndex)

    def queryCore(self, tIndex, left, right, qLeft, qRight):
        # query out of boundry
        if qLeft > right or qRight < left:
            return 0
        # if qleft <= left <= right <= right:
        # it's an answer
        if qLeft <= left and qRight >= right:
            return self.tree[tIndex].value

        # pushdown to update tree to get newest value
        self.pushDown(tIndex)
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

        # update it's value and record it in lazy tag
        if tLeft <= left and tRight >= right:
            self.tree[tIndex].value += (right - left + 1) * value
            self.tree[tIndex].lazy += value
            return
        # to update, push down first
        self.pushDown(tIndex)
        mid = (left + right) // 2

        self.updateCore(tIndex * 2 + 1, left, mid, tLeft, tRight, value)
        self.updateCore(tIndex * 2 + 2, mid + 1, right, tLeft, tRight, value)
        # update current node
        self.pushUp(tIndex)

    def update(self, tLeft, tRight, value):
        self.updateCore(0, 0, self.size - 1, tLeft, tRight, value)


nums = [0, 1, 3, 4, 6]
segTree = SegmentTree(nums)
print(segTree.query(0, 4))
segTree.update(0, 4, 4)
print(segTree.query(0, 4))