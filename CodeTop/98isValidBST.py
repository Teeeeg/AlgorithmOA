# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 携带判断
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTCore(root, -math.inf, math.inf)

    def isValidBSTCore(self, root, minVal, maxVal):
        if not root:
            return True

        if root.val < minVal or root.val > maxVal:
            return False

        return self.isValidBSTCore(root.left, minVal, root.val) and self.isValidBSTCore(root.right, root.val, maxVal)


# 中序
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        stack = []
        cur = root
        preVal = -math.inf

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if cur.val <= preVal:
                return False
            preVal = cur.val
            cur = cur.right

        return True


class Solution2:
    def __init__(self) -> None:
        self.preVal = -math.inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTCore(root)

    def isValidBSTCore(self, root):
        if not root:
            return True

        leftRes = self.isValidBSTCore(root.left)

        if self.preVal >= root.val:
            return False
        self.preVal = root.val

        rightRes = self.isValidBSTCore(root.right)

        return leftRes and rightRes
