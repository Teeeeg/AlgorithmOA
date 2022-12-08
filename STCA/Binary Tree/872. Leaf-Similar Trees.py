# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getLeafList(self, root, leafList, index):
        if not root:
            return

        if not root.left and not root.right:
            leafList[index].append(root.val)
            return

        self.getLeafList(root.left, leafList, index)
        self.getLeafList(root.right, leafList, index)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafList = {'root1': [], 'root2': []}

        self.getLeafList(root1, leafList, 'root1')
        self.getLeafList(root2, leafList, 'root2')

        return leafList['root1'] == leafList['root2']