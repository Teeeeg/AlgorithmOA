from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        rootVal = preorder[0]
        sepIndex = inorder.index(rootVal)
        root = TreeNode(rootVal)

        inLeft = inorder[:sepIndex]
        inRight = inorder[sepIndex + 1 :]
        preLeft = preorder[1 : len(inLeft) + 1]
        preRight = preorder[len(inLeft) + 1 :]

        root.left = self.buildTree(preLeft, inLeft)
        root.right = self.buildTree(preRight, inRight)

        return root
