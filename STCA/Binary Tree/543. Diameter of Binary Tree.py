# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getLongestPath(self, root: Optional[TreeNode], res):
        if not root:
            return 0

        leftLongest = self.getLongestPath(root.left, res)
        rightLongest = self.getLongestPath(root.right, res)

        if leftLongest + rightLongest + 1 > res['maxDiameter']:
            res['maxDiameter'] = leftLongest + rightLongest + 1

        return max(leftLongest, rightLongest) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = {'maxDiameter': 0}

        self.getLongestPath(root, res)

        return res['maxDiameter'] - 1