# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MIN = -10**9 + 7


class Solution:

    def maxPathSumCore(self, root, res):
        if not root:
            return MIN

        leftMax = max(self.maxPathSumCore(root.left, res), 0)
        rightMax = max(self.maxPathSumCore(root.right, res), 0)

        curMax = max(leftMax, rightMax) + root.val

        res['maxPathSum'] = max(res['maxPathSum'], leftMax + root.val + rightMax)

        return curMax

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = {'maxPathSum': MIN}

        self.maxPathSumCore(root, res)

        return res['maxPathSum']