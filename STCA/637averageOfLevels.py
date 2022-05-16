# Definition for a binary tree node.
from typing import Any, List, Optional


class TreeNode:

    def __init__(self, val=0, left=Any, right=Any):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]

        queue = [root]
        res = []

        while queue:
            n = len(queue)
            total = 0
            for _ in range(n):
                cur = queue.pop(0)
                total += cur.val
                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

            res.append(total / n)
            total = 0

        return res
