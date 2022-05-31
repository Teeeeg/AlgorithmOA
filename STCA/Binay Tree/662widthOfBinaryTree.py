# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 层次遍历
    # 记录该节点的位置
    # 左孩子为pos*2
    # 右孩子为pos*2+1

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        queue = [(root, 0)]
        while queue:
            n = len(queue)
            # 宽度为右孩子-左孩子的下标+1
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            for _ in range(n):
                cur, pos = queue.pop(0)
                if cur.left:
                    queue.append((cur.left, pos * 2))  # type: ignore
                if cur.right:
                    queue.append((cur.right, pos * 2 + 1))  # type: ignore

        return res
