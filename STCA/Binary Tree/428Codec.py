# Definition for a Node.
from collections import deque
from typing import List


class Node(object):

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root: 'Node') -> str:
        if not root:
            return '#'

        childrenRes = ''
        for child in root.children:
            childrenRes += self.serialize(child)

        return f'{root.val},{len(root.children)},{childrenRes}'  # type: ignore

    def deserializeCore(self, dataQueue):
        if not dataQueue:
            return

        cur = dataQueue.popleft()
        if cur == '#':
            return

        childrenSize = int(dataQueue.popleft())
        root = Node(cur, [])

        for _ in range(childrenSize):
            root.children.append(self.deserializeCore(dataQueue))

        return root

    def deserialize(self, data: str) -> 'Node':
        dataQueue = deque(data.split(','))

        return self.deserializeCore(dataQueue)