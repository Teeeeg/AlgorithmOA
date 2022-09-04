# Definition for a binary tree node.
from typing import Dict, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 0 no cover, 1 indirect covering, 2 camera
    def minCameraCoverCore(self, root: Optional[TreeNode], res: Dict):
        # imagine the leaf node's child is covered
        if not root:
            return 1

        leftStat = self.minCameraCoverCore(root.left, res)
        rightStat = self.minCameraCoverCore(root.right, res)

        if leftStat == 0 or rightStat == 0:
            res['minCamera'] += 1
            return 2

        if leftStat == 2 or rightStat == 2:
            return 1

        return 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = {'minCamera': 0}
        # detail at root
        if self.minCameraCoverCore(root, res) == 0:
            res['minCamera'] += 1

        return res['minCamera']