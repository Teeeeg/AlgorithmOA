# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.recursiveCore(root, targetSum)

    def recursiveCore(self, root, path):
        if not root.left and not root.right:
            return path == root.val
        res1 = self.recursiveCore(root.left, path-root.val)
        res2 = self.recursiveCore(root.right, path-root.val)

        return res1 or res2

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = []
        queue.append((root, targetSum))

        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right and path == node.val:
                return True
            if node.left:
                queue.append((node.left, path-node.val))
            if node.right:
                queue.append((node.right, path-node.val))

        return False
