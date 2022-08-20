# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        levelSum = 0

        while queue:
            n = len(queue)
            levelSum = 0
            for _ in range(n):
                cur = queue.popleft()
                levelSum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return levelSum


class Solution1:

    def deepestLeavesSumCore(self, root, level):
        if not root:
            return

        if level == self.maxLevel:
            self.res += root.val

        if level > self.maxLevel:
            self.res = root.val
            self.maxLevel = level

        self.deepestLeavesSumCore(root.left, level + 1)
        self.deepestLeavesSumCore(root.right, level + 1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maxLevel = 0
        self.res = 0

        self.deepestLeavesSumCore(root, 0)

        return self.res