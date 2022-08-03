# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBSTCore(self, root: Optional[TreeNode]):
        if not root:
            return (True, math.inf, -math.inf)

        isValidLeft, minLeft, maxLeft = self.isValidBSTCore(root.left)
        isValidRight, minRight, maxRight = self.isValidBSTCore(root.right)

        if isValidLeft and isValidRight and maxLeft < root.val < minRight:
            return (True, min(minLeft, root.val), max(maxRight, root.val))

        return (False, -math.inf, math.inf)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        isValid, _, _ = self.isValidBSTCore(root)
        return isValid