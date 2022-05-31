# Definition for a binary tree node.
from calendar import c
import queue
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = [root]
        while queue:
            n = len(queue)
            levelRes = []
            for _ in range(n):
                cur = queue.pop(0)
                levelRes.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(levelRes)

        return res