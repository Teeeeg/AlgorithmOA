# Definition for a binary tree node.
from itertools import count
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        count = 0

        while queue:
            n = len(queue)
            level = []
            count += 1
            for _ in range(n):
                cur = queue.pop(0)
                level.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            if count % 2:
                res.append(level)

            else:
                res.append(level[::-1])

        return res
