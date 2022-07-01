# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self) -> None:
        self.head = None
        self.pre = None

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        self.convertBiNodeCore(root)
        return self.head  # type: ignore

    def convertBiNodeCore(self, root):
        if not root:
            return

        self.convertBiNodeCore(root.left)

        if self.pre:
            self.pre.right = root
        else:
            self.head = root
        self.pre = root
        root.left = None

        self.convertBiNodeCore(root.right)
