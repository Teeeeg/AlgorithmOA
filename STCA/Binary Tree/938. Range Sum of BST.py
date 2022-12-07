from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rangeSumBSTCore(self, root, low, high, res):
        if not root:
            return

        if root.val > low:
            self.rangeSumBSTCore(root.left, low, high, res)

        if low <= root.val <= high:
            res['sum'] += root.val

        if root.val < high:
            self.rangeSumBSTCore(root.right, low, high, res)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = {'sum': 0}
        self.rangeSumBSTCore(root, low, high, res)

        return res['sum']