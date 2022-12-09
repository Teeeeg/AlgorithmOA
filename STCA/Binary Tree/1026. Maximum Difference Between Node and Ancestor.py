from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxAncestorDiffCore(self, root, res):
        if not root:
            return (10**5 + 7, -1)

        leftMin, leftMax = self.maxAncestorDiffCore(root.left, res)
        rightMin, rightMax = self.maxAncestorDiffCore(root.right, res)

        curMin = min(leftMin, rightMin, root.val)
        curMax = max(leftMax, rightMax, root.val)

        curMaxDiff = max(abs(curMin - root.val), (curMax - root.val))
        res['minDiff'] = max(res['minDiff'], curMaxDiff)

        return (curMin, curMax)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = {'minDiff': 0}

        self.maxAncestorDiffCore(root, res)

        return res['minDiff']