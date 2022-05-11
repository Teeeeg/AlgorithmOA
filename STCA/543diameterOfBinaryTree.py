# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterOfBinaryTreeCore(root)
        return self.res

    def diameterOfBinaryTreeCore(self, root):
        if not root:
            return 0

        leftHeight = self.diameterOfBinaryTreeCore(root.left)
        rightHeight = self.diameterOfBinaryTreeCore(root.right)

        self.res = max(self.res, leftHeight+rightHeight+1)

        return max(leftHeight, rightHeight) + 1
