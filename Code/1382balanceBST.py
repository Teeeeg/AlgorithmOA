# Definition for a binary tree node.
from typing import Any


class TreeNode:

    def __init__(self, val=0, left=Any, right=Any):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.nums = []

    def getNums(self, root: TreeNode):
        if not root:
            return

        self.getNums(root.left)
        self.nums.append(root.val)
        self.getNums(root.right)

    def buildTree(self, left, right):
        if left > right:
            return

        mid = (right + left) // 2

        root = TreeNode(self.nums[mid])
        root.left = self.buildTree(left, mid - 1)
        root.right = self.buildTree(mid + 1, right)

        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.getNums(root)
        n = len(self.nums)
        return self.buildTree(0, n - 1)  # type: ignore
