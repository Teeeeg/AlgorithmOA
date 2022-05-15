# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorderTraversalCore(root, res)
        return res

    def preorderTraversalCore(self, root, res: List[TreeNode]):
        if not root:
            return

        res.append(root.val)
        self.preorderTraversalCore(root.left, res)
        self.preorderTraversalCore(root.right, res)
