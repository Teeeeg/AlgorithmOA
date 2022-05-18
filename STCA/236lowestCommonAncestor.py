# Definition for a binary tree node.
from typing import Any


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = Any
        self.right = Any


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode'):
        # base case
        if not root:
            return root

        # 若该节点等于其中一个，则返回该节点
        if root == p or root == q:
            return root

        # 后序
        leftRes = self.lowestCommonAncestor(root.left, p, q)
        rightRes = self.lowestCommonAncestor(root.right, p, q)

        # 左右都有返回值，说明该节点就是
        if leftRes and rightRes:
            return root

        # 若有一边存在p或q，说明目标在这一边上
        # 将这一边返回
        if leftRes and rightRes:
            return root

        if leftRes and not rightRes:
            return leftRes

        if rightRes and not leftRes:
            return rightRes
