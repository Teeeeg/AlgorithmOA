from collections import deque


class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        mapping = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # must mapping the neighbor to clone graph
                mapping[cur].neighbors.append(mapping[neighbor])

        return mapping[node]
