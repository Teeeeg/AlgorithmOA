class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 迭代的时候破坏了其顺序
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return root

        stack = [root]
        pre = None

        while stack:
            cur = stack.pop()
            if pre:
                pre.left = None
                pre.right = cur
            pre = cur

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
