# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.res = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.pathSumCore(root, [0], 0, targetSum)
        return self.res

    def pathSumCore(self, root, path, total, target):
        if not root:
            return

        total += root.val
        path.append(total)

        if total-target in path:
            self.res += 1

        self.pathSumCore(root.left, path, total, target)
        self.pathSumCore(root.right, path, total, target)
        total -= root.val
        path.pop()
