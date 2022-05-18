# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == key:
            # 无左右子树
            if not root.left and not root.right:
                return None

            # 有左子树，无右子树
            if root.left and not root.right:
                return root.left

            # 有右子树，无左子树
            if root.right and not root.left:
                return root.right

            # 都有
            # 用cur获取右子树的最左节点
            cur = root.right
            while cur.left:
                cur = cur.left
            # 把被删除节点的左子树头节点接到cur之后
            cur.left = root.left
            # 返回root.right
            root = root.right
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        return root