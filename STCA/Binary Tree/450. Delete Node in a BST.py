# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == key:
            if not root.left and not root.right:
                return

            if not root.left and root.right:
                return root.right

            if root.left and not root.right:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            return root.right

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root