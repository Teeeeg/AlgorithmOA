# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        # 自身以及其左右子树
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:
            return 0

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        return max(leftHeight, rightHeight)+1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.recursiveCore(root) != -1

    def recursiveCore(self, root):
        if not root:
            return 0

        leftHeight = self.recursiveCore(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.recursiveCore(root.right)
        if rightHeight == -1:
            return -1

        return max(leftHeight, rightHeight)+1 if abs(leftHeight - rightHeight) < 2 else -1
