
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        dct = {}
        cur = root

        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                if not cur.children:
                    break
                children = cur.children
                tmp = children.pop()
                dct[cur] = children
                cur = tmp

            cur = stack[-1]
            children = dct.get(cur, [])
            # 不同于二叉树，需要进入所有节点后才能pop
            if children:
                cur = children.pop(0)
            else:
                # 处理完所有节点再pop
                stack.pop()
                cur = None
        return res


class Solution:
    def preorder1(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack += cur.children[:: -1]

        return res
