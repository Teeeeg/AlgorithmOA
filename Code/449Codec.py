from typing import Any, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = Any
        self.right = Any


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '#'

        leftRes = self.serialize(root.left)
        rightRes = self.serialize(root.right)

        res = f"{root.val},{leftRes},{rightRes}"
        return res

    def deserialize(self, data: str) -> Any:
        """Decodes your encoded data to tree.
        """
        dataQueue = data.split(',')
        res = self.deserializeCore(dataQueue)
        return res

    def deserializeCore(self, dataQueue: List[str]):
        if not dataQueue:
            return

        data = dataQueue.pop(0)
        if data == '#':
            return None

        root = TreeNode(int(data))

        root.left = self.deserializeCore(dataQueue)
        root.right = self.deserializeCore(dataQueue)

        return root
