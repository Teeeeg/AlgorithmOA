# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.maxValue = 0

    def maxSumBSTCore(self, root: Optional[TreeNode]):
        if not root:
            return (0, math.inf, -math.inf)

        total1, left1, right1 = self.maxSumBSTCore(root.left)
        total2, left2, right2 = self.maxSumBSTCore(root.right)

        if right1 < root.val < left2:
            total = root.val + total1 + total2
            self.maxValue = max(self.maxValue, total)
            return (total, min(left1, root.val), max(right2, root.val))

        return (root.val, -math.inf, math.inf)

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSumBSTCore(root)
        return self.maxValue