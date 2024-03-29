# Definition for a Node.
from typing import Optional


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur

        else:
            while node.parent:
                if node.parent.left == node:
                    return node.parent
                node = node.parent

        return None