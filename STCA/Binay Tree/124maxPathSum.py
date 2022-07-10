# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.res = -math.inf

    def maxPathSumCore(self, root: Optional[TreeNode]):
        # 后序遍历
        if not root:
            return 0

        # 分别获取左右最大path
        leftPath = max(self.maxPathSumCore(root.left), 0)
        rightPath = max(self.maxPathSumCore(root.right), 0)

        # 目前最大path
        pathSum = leftPath + root.val + rightPath

        # 更新
        self.res = max(self.res, pathSum)

        # 返回单向最大的path
        return root.val + max(leftPath, rightPath)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumCore(root)
        return self.res  # type: ignore
