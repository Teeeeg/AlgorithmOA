# Definition for a binary tree node.
from typing import Any


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = Any
        self.right = Any


class Codec:
    # 后序遍历，前序存
    def serialize(self, root: TreeNode) -> str:
        # 标记None的
        if not root:
            return '#'

        leftRes = self.serialize(root.left)
        rightRes = self.serialize(root.right)

        # 前序序列
        res = f"{root.val},{leftRes},{rightRes}"
        return res

    def deserializeCore(self, queue):
        if not queue:
            return
        cur = queue.pop(0)

        if cur == '#':
            return None

        root = TreeNode(cur)
        root.left = self.deserializeCore(queue)
        root.right = self.deserializeCore(queue)

        return root

    def deserialize(self, data: str):
        # 利用队列进行递归
        queue = data.split(',')
        root = self.deserializeCore(queue)

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans