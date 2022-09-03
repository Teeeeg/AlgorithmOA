# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # post order traversal and record every serialized string
    def traversal(self, root: Optional[TreeNode], counter, res):
        if not root:
            return '#'

        serializedString = f'{self.traversal(root.left, counter, res)},{self.traversal(root.right, counter, res)},{root.val}'
        counter[serializedString] = counter.get(serializedString, 0) + 1

        if counter[serializedString] == 2:
            res.append(root)

        return serializedString

    def findDuplicateSubtrees(self, root: Optional[TreeNode]):
        counter = {}
        res = []
        self.traversal(root, counter, res)
        return res