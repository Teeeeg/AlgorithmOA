# Definition for a binary tree node.
from typing import Any, List, Optional


class TreeNode:

    def __init__(self, val=0, left=Any, right=Any):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSumCore(self, root: Optional[TreeNode], targetSum: int, path: List[int], res: List[List[int]]):
        if not root:
            return

        path.append(root.val)
        if targetSum - root.val == 0 and not root.left and not root.right:
            res.append(path[:])

        self.pathSumCore(root.left, targetSum - root.val, path[:], res)
        self.pathSumCore(root.right, targetSum - root.val, path[:], res)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.pathSumCore(root, targetSum, [], res)
        return res