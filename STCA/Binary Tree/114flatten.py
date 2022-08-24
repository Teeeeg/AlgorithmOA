# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse(self, root: Optional[TreeNode], preOrderList):
        if not root:
            return

        preOrderList.append(root)
        self.traverse(root.left, preOrderList)
        self.traverse(root.right, preOrderList)

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        preOrderList = []
        self.traverse(root, preOrderList)

        pre = None

        for node in preOrderList:
            if pre:
                pre.left = None
                pre.right = node
            pre = node


class Solution1:

    def flattenCore(self, root: Optional[TreeNode]):
        if not root:
            return

        leftLast = self.flattenCore(root.left)
        rightLast = self.flattenCore(root.right)

        if leftLast:
            leftLast.right = root.right
            root.right = root.left
            root.left = None
        # return the flatterned list's last node
        # because it is preOrder, so it should be reversed
        return rightLast or leftLast or root

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flattenCore(root)