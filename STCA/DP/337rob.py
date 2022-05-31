# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def robCore(self, root: TreeNode):
        # tup[0]表示不考虑
        # tup[1]表示考虑
        if not root:
            return (0, 0)
        # 后序遍历
        leftRes = self.robCore(root.left)
        rightRes = self.robCore(root.right)
        # 不考虑当前节点，则左右考不考虑都可以，因此用max
        # 注意用max
        res0 = max(leftRes) + max(rightRes)
        # 取该节点，则左右应该都是不取
        res1 = leftRes[0] + rightRes[0] + root.val

        return (res0, res1)

    def rob(self, root: TreeNode) -> int:
        res = self.robCore(root)
        return max(res)