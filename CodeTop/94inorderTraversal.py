from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.recursiveCore(root)
        return self.res

    def recursiveCore(self, root):
        if root:
            self.recursiveCore(root.left)
            self.res.append(root.val)
            self.recursiveCore(root.right)

    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            res.append(cur.val)
            cur = cur.right

        return res
