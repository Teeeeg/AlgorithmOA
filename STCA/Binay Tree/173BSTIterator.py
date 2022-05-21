# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    # 可以理解为拆开的中序遍历
    def __init__(self, root: TreeNode):
        self.stack = []
        self.cur = root

    def next(self) -> int:
        # 内层的while，用于不断往stack中push
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        self.cur = self.stack.pop()
        res = self.cur.val
        self.cur = self.cur.right
        return res

    # 中序遍历最外层的while
    def hasNext(self) -> bool:
        return True if self.stack or self.cur else False
