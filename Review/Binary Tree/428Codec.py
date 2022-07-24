# Definition for a Node.
from typing import List


class Node(object):

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    # serialized structure
    # root.val + children size + children
    def serialize(self, root: 'Node') -> str:
        # '#' indicates is none
        if not root:
            return '#'
        res = ''
        res += str(root.val) + ',' + str(len(root.children))

        # recursively update
        for child in root.children:
            res += ',' + self.serialize(child)
        return res

    def deserializeCore(self, dataQueue: List[int]):
        # base condition
        if not dataQueue:
            return

        val = dataQueue.pop(0)
        # '#' means empty node
        if val == '#':
            return

        root = Node(int(val), [])
        size = int(dataQueue.pop(0))
        # use size to iterate certain size of the string for children
        for _ in range(size):
            root.children.append(self.deserializeCore(dataQueue))  # type: ignore
        return root

    def deserialize(self, data: str) -> 'Node':
        dataQueue = data.split(',')
        return self.deserializeCore(dataQueue)  # type: ignore
