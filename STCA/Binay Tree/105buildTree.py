# Definition for a binary tree node.
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]):
        if not preorder or not inorder:
            return None
        # 从前序遍历中获取根节点
        rootVal = (preorder[0])
        rootIndex = inorder.index(rootVal)

        # 根据根节点把中序遍历一分为二，注意不包括根节点
        # [@left, root, @right]
        inorderLeft = inorder[:rootIndex]
        inorderRight = inorder[rootIndex + 1:]
        # 根据根节点截取前序
        # 可以理解为按照先前中序遍历的长度，依次从第一个节点向后截取
        # [@root, left, right]
        preorderLeft = preorder[1:rootIndex + 1]
        preorderRight = preorder[rootIndex + 1:]

        root = TreeNode(rootVal)
        # 递归构建二叉树
        root.left = self.buildTree(preorderLeft, inorderLeft)  # type: ignore
        root.right = self.buildTree(preorderRight, inorderRight)  # type: ignore

        return root
