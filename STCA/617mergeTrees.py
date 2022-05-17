# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def mergeTrees(self, root1: TreeNode, root2: TreeNode):
        # 若都为空则容易返回
        if not root1 and not root2:
            return None

        # 返回有值的
        if not root1:
            return root2

        if not root2:
            return root1

        # 更改root1的值
        root1.val += root2.val

        # 分别递归更新root1的left，right
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1