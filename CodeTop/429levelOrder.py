# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            levelCount = len(queue)
            levelList = []
            for _ in range(levelCount):
                cur = queue.pop(0)
                levelList.append(cur)
                queue += cur.children

            res.append(levelList)

        return res
