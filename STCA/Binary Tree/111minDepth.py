from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # find shortest length to a leaf node

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # if it is a leaf node, return 1
        if not root.left and not root.right:
            return 1

        # if it is not
        # consider with onde branch
        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        if root.left and not root.right:
            return self.minDepth(root.left) + 1

        # else consider with both branch
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1