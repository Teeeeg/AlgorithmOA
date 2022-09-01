# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def robCore(self, root: Optional[TreeNode]):
        if not root:
            return (0, 0)

        leftRob, leftNoRob = self.robCore(root.left)
        rightRob, righNoRob = self.robCore(root.right)

        curRob = leftNoRob + righNoRob + root.val
        curNoRob = max(leftRob, leftNoRob) + max(rightRob, righNoRob)

        return (curRob, curNoRob)

    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.robCore(root))