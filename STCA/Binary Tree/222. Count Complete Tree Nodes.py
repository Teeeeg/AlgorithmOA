# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = {'count': 0}

        self.countNodesCore(root, res)

        return res['count']

    def countNodesCore(self, root: Optional[TreeNode], res):
        if not root:
            return False

        if not root.left and not root.right:
            res['count'] += 1
            return True

        leftRes = self.countNodesCore(root.left, res)
        rightRes = self.countNodesCore(root.right, res)

        if leftRes and rightRes or (leftRes and not rightRes):
            res['count'] += 1
            return True

        return False