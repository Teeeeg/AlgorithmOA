# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxProductCore(self, root, res):
        if not root:
            return 0

        leftSum = self.maxProductCore(root.left, res)
        rightSum = self.maxProductCore(root.right, res)

        res['maxProduct'] = max(res['maxProduct'], (res['sum'] - rightSum) * rightSum, (res['sum'] - leftSum) * leftSum)

        return leftSum + rightSum + root.val

    def getSum(self, root, res):
        if not root:
            return

        res['sum'] += root.val
        self.getSum(root.left, res)
        self.getSum(root.right, res)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        res = {'maxProduct': 0, 'sum': 0}

        self.getSum(root, res)
        self.maxProductCore(root, res)

        return res['maxProduct'] % MOD