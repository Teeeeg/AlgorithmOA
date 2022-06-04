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
        if not node:
            return node

        # 若有右子树，则为右子树的最左节点
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur

        # 若无左子树，应该为最先一个为左节点的节点
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent

        return None