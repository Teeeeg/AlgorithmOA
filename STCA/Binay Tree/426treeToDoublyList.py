# Definition for a Node.
from typing import Any, Optional


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.preNode = Any
        self.head = Any

    def treeToDoublyListCore(self, root: 'Optional[Node]'):
        if not root:
            return

        self.treeToDoublyListCore(root.left)

        # 递归内容
        # 若此时preNode不为空
        if self.preNode:
            self.preNode.right = root
            root.left = self.preNode
        # 为空，则为第一个，赋值给head
        else:
            self.head = root
        # 更新preNode
        self.preNode = root

        self.treeToDoublyListCore(root.right)

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        self.treeToDoublyListCore(root)
        # 链接首尾
        self.head.left = self.preNode
        self.preNode.right = self.head

        return self.head