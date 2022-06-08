# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 因为与父节点是断开的
    # 建立每个节点的图，左右父

    def __init__(self) -> None:
        self.graph = defaultdict(list)

    # 建立图
    def buildGraph(self, root: TreeNode):
        if not root:
            return
        # 有左右节点才添加
        if root.left:
            self.graph[root.val].append(root.left.val)
            self.graph[root.left.val].append(root.val)
            self.buildGraph(root.left)
        if root.right:
            self.graph[root.val].append(root.right.val)
            self.graph[root.right.val].append(root.val)
            self.buildGraph(root.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        self.buildGraph(root)
        queue = []
        queue.append(target.val)
        visited = set()
        visited.add(target.val)

        # 因为是求最后一层的所有节点
        # 必须用广度优先
        while queue and k > 0:
            n = len(queue)
            for _ in range(n):
                # 当前层加处理
                cur = queue.pop(0)
                visited.add(cur)
                for post in self.graph[cur]:
                    if post not in visited:
                        queue.append(post)
            k -= 1

        return queue