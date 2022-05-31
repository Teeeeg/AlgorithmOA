# Definition for a binary tree node.
from typing import Dict, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 前缀和

    def __init__(self) -> None:
        self.res = 0

    def pathSumCore(self, root: Optional[TreeNode], targetSum: int, sums: Dict, total):
        if not root:
            return

        # 先计算total
        total += root.val
        # 再统计
        self.res += sums.get(total - targetSum, 0)
        sums[total] = sums.get(total, 0) + 1

        self.pathSumCore(root.left, targetSum, sums, total)
        # 回溯
        sums[total] -= 1
        total -= root.val

        # 因为之前被回溯了，当前属于同一层
        # 应该加回去
        total += root.val
        sums[total] = sums.get(total, 0) + 1
        self.pathSumCore(root.right, targetSum, sums, total)
        # 回溯
        sums[total] -= 1
        total -= root.val

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        self.pathSumCore(root, targetSum, {0: 1}, 0)
        return self.res