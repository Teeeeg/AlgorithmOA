# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traversal(self, root: Optional[TreeNode], res, path):
        if not root:
            return

        path += chr(root.val + ord('a'))
        if not root.left and not root.right:
            res['min'] = min(res['min'], path[::-1])

        self.traversal(root.left, res, path)
        self.traversal(root.right, res, path)

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = {'min': 'zzzzzzzzzzzzzzzzzzz'}
        self.traversal(root, res, '')

        return res['min']
