# Definition for a Node.
from typing import Optional


class Node:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):  # type: ignore
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 层次遍历
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = [root]
        while queue:
            n = len(queue)
            # 用于保存上一个节点
            pre = None
            for _ in range(n):
                cur = queue.pop(0)
                if pre:
                    pre.next = cur
                pre = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return root

    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        cur = root
        while cur.left:
            tmp = cur
            # 判断有没有子节点了
            while tmp:
                # 连接左右节点
                tmp.left.next = tmp.right
                # 若有同级节点
                if tmp.next:
                    # 连接
                    tmp.right.next = tmp.next.left
                tmp = tmp.next
            cur = cur.left

        return root