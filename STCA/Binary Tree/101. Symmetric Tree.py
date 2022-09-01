# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetricCore(self, leftNode: Optional[TreeNode], rightNode: Optional[TreeNode]):
        if not leftNode and not rightNode:
            return True

        if not leftNode or not rightNode:
            return False

        if leftNode.val != rightNode.val:
            return False

        outerRes = self.isSymmetricCore(leftNode.left, rightNode.right)
        innerRes = self.isSymmetricCore(leftNode.right, rightNode.left)

        return outerRes and innerRes

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSymmetricCore(root.left, root.right)


class Solution1:
    # solve recursion overfolow
    # use bfs
    def isSymmetricCore(self, nodeList):
        n = len(nodeList)
        left = 0
        right = n - 1

        while left < right:
            if not nodeList[left] and not nodeList[right]:
                left += 1
                right -= 1
            elif not nodeList[left] or not nodeList[right]:
                return False
            elif nodeList[left].val != nodeList[right].val:
                return False
            else:
                left += 1
                right -= 1

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])

        while queue:
            n = len(queue)
            nextQueue = deque()
            for _ in range(n):
                cur = queue.popleft()
                if not cur:
                    continue
                nextQueue.append(cur.left)
                nextQueue.append(cur.right)

            if not self.isSymmetricCore(nextQueue):
                return False

            queue = nextQueue

        return True