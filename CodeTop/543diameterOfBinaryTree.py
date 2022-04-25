# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recursiveCore(root)
        return self.diameter

    def recursiveCore(self, root):
        if not root:
            return 0

        leftHeight = self.recursiveCore(root.left)
        rightHeight = self.recursiveCore(root.right)

        curDiameter = leftHeight + rightHeight + 1
        self.diameter = max(curDiameter, self.diameter)

        return max(leftHeight, rightHeight) + 1
