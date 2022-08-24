# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=Optional, right=Optional):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]):
        if not preorder and not inorder:
            return None

        rootVal = preorder[0]
        rootIndex = inorder.index(rootVal)

        leftInorder = inorder[:rootIndex]
        rightInorder = inorder[rootIndex + 1:]
        leftLen = len(leftInorder)

        leftPreorder = preorder[1:leftLen + 1]
        rightPreorder = preorder[leftLen + 1:]

        root = TreeNode(rootVal)
        root.left = self.buildTree(leftPreorder, leftInorder)  # type: ignore
        root.right = self.buildTree(rightPreorder, rightInorder)  # type: ignore

        return root