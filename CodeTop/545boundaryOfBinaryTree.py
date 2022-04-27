# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        left = []
        leaf = []
        right = []

        self.getLeft(root.left, left)
        self.getLeaf(root, leaf)
        self.getRight(root.right, right)

        return [root.val] + left + leaf + right[::-1]

    def getLeft(self, root, left):
        if not root:
            return

        if root.left or root.right:
            left.append(root.val)
            if root.left:
                self.getLeft(root.left, left)
            else:
                self.getRight(root.right, left)

    def getRight(self, root, right):
        if not root:
            return

        if root.left or root.right:
            right.append(root.val)
            if root.right:
                self.getRight(root.right, right)
            else:
                self.getLeft(root.left, right)

    def getLeaf(self, root, leaf):
        if not root:
            return

        if not root.left and not root.right:
            leaf.append(root.val)
        else:
            self.getLeaf(root.left, leaf)
            self.getLeaf(root.right, leaf)
