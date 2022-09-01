# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSumCore(self, root: Optional[TreeNode], res):
        if not root:
            return 0
        # keep in mind if the sum is negative
        leftSum = max(self.maxPathSumCore(root.left, res), 0)
        rightSum = max(self.maxPathSumCore(root.right, res), 0)

        curSum = leftSum + root.val + rightSum
        if curSum > res['maxSum']:
            res['maxSum'] = curSum

        return max(leftSum, rightSum) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = {'maxSum': -10**9}
        self.maxPathSumCore(root, res)

        return res['maxSum']
