# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return TreeNode()

        rootVal = postorder[-1]
        sepIndex = inorder.index(rootVal)
        root = TreeNode(rootVal)

        leftIn = inorder[:sepIndex]
        rightIn = inorder[sepIndex + 1 :]

        leftPost = postorder[: len(leftIn)]
        rightPost = postorder[len(leftIn) : len(postorder) - 1]

        root.left = self.buildTree(leftIn, leftPost)
        root.right = self.buildTree(rightIn, rightPost)

        return root
