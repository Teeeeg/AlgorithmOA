# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 利用二叉搜索树的特性
    # 一直找到叶子节点为止

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        cur = root
        # 注意用pre保存前一个节点
        pre = root
        while cur:
            pre = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if val < pre.val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)

        return root
