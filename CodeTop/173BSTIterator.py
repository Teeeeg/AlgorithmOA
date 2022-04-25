# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.populateStack(root)

    def populateStack(self, root):
        if not root:
            return
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if not self.hasNext():
            return None
        node = self.stack.pop()
        self.populateStack(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0
