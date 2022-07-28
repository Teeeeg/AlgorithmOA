class Node:

    def __init__(self, left=-1, right=-1, value=0, lazy=0) -> None:
        self.left = left
        self.right = right
        self.value = value
        self.lazy = lazy


class SegementTree:

    def __init__(self, n, arr) -> None:
        self.n = n
        self.maxSize = 4 * n
        self.tree = [Node() for _ in range(self.maxSize)]
        self.arr = arr

    def buildCore(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right

        if left == right:
            self.tree[index].value = self.arr[left]
        else:
            mid = (left + right) // 2
            self.buildCore(index * 2 + 1, left, mid)
            self.buildCore(index * 2 + 2, mid + 1, right)
            self.pushUp(index)

    def build(self):
        self.buildCore(0, 0, self.n)

    def pushUp(self, index):
        self.tree[index].value = self.tree[index * 2 + 1].value + self.tree[index * 2 + 2].value

    def pushDown(self, index):
        root = self.tree[index]
        lazy = root.lazy
        if lazy != 0:
            leftChild = self.tree[index * 2 + 1]
            rightChild = self.tree[index * 2 + 2]
            leftChild.lazy += lazy
            rightChild.lazy += lazy
            leftChild.value += (leftChild.right - leftChild.left + 1) * lazy
            rightChild.value += (rightChild.right - rightChild.left + 1) * lazy
            root.lazy = 0

    def updateCore(self, targetL, targetR, val, index, l, r):
        mid = (l + r) // 2
        if targetL == l and targetR == r:
            self.tree[index].value += (r - l + 1) * val
            self.tree[index].lazy += val
        else:
            self.pushDown(index)
            if mid >= targetL:
                self.updateCore(targetL, targetR, val, index * 2 + 1, l, mid)
            else:
                self.updateCore(targetL, targetR, val, index * 2 + 1, l, mid)
            self.pushUp(index)

    def update(self, targetL, targetR, val):
        self.updateCore(targetL, targetR, val, 0, 0, self.n)

    def queryCore(self, targetL, targetR, index, l, r):
        if targetL == l and targetR == r:
            return self.tree[index].value
        else:
            self.pushDown(index)
            mid = (l + r) // 2
            resLeft = 0
            resRight = 0
            if targetL <= mid:
                resLeft = self.queryCore(targetL, targetR, index * 2 + 1, l, mid)
            if targetR > mid:
                resRight = self.queryCore(targetL, targetR, index * 2 + 2, mid + 1, r)

            return resLeft + resRight
