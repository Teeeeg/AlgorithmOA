# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.isValidSequenceCore(root, arr, 0)

    def isValidSequenceCore(self, root, arr, index):
        if not root:
            return False

        if not root.val == arr[index]:
            return False

        if index == len(arr)-1 and not root.left and not root.right:
            return True

        return self.isValidSequenceCore(root.left, arr, index+1) or self.isValidSequenceCore(root.right, arr, index+1)
