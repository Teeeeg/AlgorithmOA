# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        res = 0

        while queue:
            n = len(queue)
            leftMost = queue[0][1]
            rightMost = -1
            for _ in range(n):
                cur, index = queue.popleft()
                rightMost = max(rightMost, index)

                if cur.left:
                    queue.append((cur.left, index * 2 + 1))  # type: ignore
                if cur.right:
                    queue.append((cur.right, index * 2 + 2))  # type: ignore

            res = max(res, rightMost - leftMost + 1)

        return res