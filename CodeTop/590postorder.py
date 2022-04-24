# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        dct = {}
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                if not cur.children:
                    break
                children = cur.children
                dct[cur] = children
                cur = children.pop()

            cur = stack[-1]
            children = dct.get(cur, [])
            # 不同于二叉树，需要进入所有节点后才能pop
            if children:
                cur = children.pop(0)
            else:
                # 处理完所有节点再pop
                res.append(cur.val)
                stack.pop()
                cur = None
        return res
