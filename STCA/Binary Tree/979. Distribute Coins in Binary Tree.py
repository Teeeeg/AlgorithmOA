# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def distributeCoinsCore(self, root: Optional[TreeNode]):
        if not root:
            return 0

        leftRes = self.distributeCoinsCore(root.left)
        rightRes = self.distributeCoinsCore(root.right)

        self.res += abs(leftRes) + abs(rightRes)
        return leftRes + rightRes + root.val - 1

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.distributeCoinsCore(root)

        return self.res