# Definition for a binary tree node.


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 完全二叉树里有满二叉树

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        cur = root
        leftHeight = 1
        rightHeight = 1
        # 分别找到左右子树的高度
        while cur.left:
            cur = cur.left
            leftHeight += 1

        while cur.right:
            cur = cur.right
            rightHeight += 1
        # 若高度相等则直接用满二叉树的公式计算
        if leftHeight == rightHeight:
            return 2**leftHeight - 1

        leftRes = self.countNodes(root.left)
        rightRes = self.countNodes(root.right)

        return leftRes + rightRes + 1
