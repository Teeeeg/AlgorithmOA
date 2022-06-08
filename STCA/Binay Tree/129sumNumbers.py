# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.res = 0

    def sumNumbersCore(self, root: TreeNode, path):
        # base
        if not root:
            return
        # 到达叶子节点，记录
        if not root.left and not root.right:
            self.res += path * 10 + root.val
            return
        # 前序递归遍历
        self.sumNumbersCore(root.left, path * 10 + root.val)
        self.sumNumbersCore(root.right, path * 10 + root.val)

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.sumNumbersCore(root, 0)
        return self.res