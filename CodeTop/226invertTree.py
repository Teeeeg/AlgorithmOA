# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.recursiveCore(root)

    def recursiveCore(self, root: TreeNode):
        if not root:
            return root
        root.left, root.right = root.left, root.right
        self.recursiveCore(root.left)
        self.recursiveCore(root.right)

        return root


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur.left, cur.right = cur.right, cur.left
                cur = cur.left

            cur = stack.pop()
            cur = cur.right

        return root
