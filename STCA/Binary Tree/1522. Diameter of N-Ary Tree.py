# Definition for a Node.
from heapq import heappop, heappush


class Node:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:

    def getLongestPath(self, root: 'Node', res):
        if not root:
            return 0

        minHeap = []
        for child in root.children:
            childPath = self.getLongestPath(child, res)
            heappush(minHeap, childPath)
            if len(minHeap) > 2:
                heappop(minHeap)

        if sum(minHeap) + 1 > res['maxDiameter']:
            res['maxDiameter'] = sum(minHeap) + 1

        if minHeap:
            return minHeap[-1] + 1
        return 1

    def diameter(self, root: 'Node') -> int:
        res = {'maxDiameter': 0}

        self.getLongestPath(root, res)

        return res['maxDiameter'] - 1