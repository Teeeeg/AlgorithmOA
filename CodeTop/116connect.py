# Definition for a Node.
from typing import Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        pre = root
        while pre.left:
            tmp = pre
            while tmp:
                tmp.left.next = tmp.right
                if tmp.next:
                    tmp.right.next = tmp.next.left
                tmp = tmp.next
            pre = pre.left

        return root

    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        self.connectCore(root)
        return root

    def connectCore(self, root):
        if not root:
            return

        left = root.left
        right = root.right

        while left:
            left.next = right
            left = left.right
            right = right.left
        self.connectCore(root.left)
        self.connectCore(root.right)
