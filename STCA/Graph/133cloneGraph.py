# Definition for a Node.
class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def __init__(self) -> None:
        # 保存的是 [old->cloned]
        self.dct = {}

    def cloneGraphCore(self, node: 'Node'):
        # base
        if not node:
            return node
        # 若有则直接返回
        if node in self.dct:
            return self.dct[node]
        # neighbors 用 []
        cloned = Node(node.val, [])
        self.dct[node] = cloned
        # 遍历递归neighbors
        for neighbor in node.neighbors:
            cloned.neighbors.append(self.cloneGraphCore(neighbor))

        return cloned

    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.cloneGraphCore(node)

    def cloneGraph1(self, node: 'Node') -> 'Node':
        if not node:
            return node
        # 保存的是 [old->cloned]
        dct = {}
        queue = [node]
        # 初始化节点
        dct[node] = Node(node.val, [])

        while queue:
            cur = queue.pop(0)
            for neighbor in cur.neighbors:
                # 没有复制的节点创建新的链接
                if neighbor not in dct:
                    queue.append(neighbor)
                    dct[neighbor] = Node(neighbor.val, [])
                # 不管有没有复制，都链接到新的neighbors上
                dct[cur].neighbors.append(dct[neighbor])

        return dct[node]
