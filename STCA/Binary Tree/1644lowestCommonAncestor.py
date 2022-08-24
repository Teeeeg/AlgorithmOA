# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestorCore(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        # use (hasP, hasQ, LCA)
        if not root:
            return False, False, None

        leftHasP, leftHasQ, leftLCA = self.lowestCommonAncestorCore(root.left, p, q)  # type: ignore
        rightHasP, rightHasQ, rightLCA = self.lowestCommonAncestorCore(root.right, p, q)  # type: ignore

        # update hasP, hasQ
        hasP = leftHasP or rightHasP or root == p
        hasQ = leftHasQ or rightHasQ or root == q

        # if root encounter p or q
        # return current
        if root == p or root == q:
            return hasP, hasQ, root

        # if leftLCA and rightLCA
        # return root
        if leftLCA and rightLCA:
            if hasP and hasQ:
                return hasP, hasQ, root

        if leftLCA and not rightLCA:
            return hasP, hasQ, leftLCA

        if rightLCA and not leftLCA:
            return hasP, hasQ, rightLCA

        return hasP, hasQ, None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        hasP, hasQ, LCA = self.lowestCommonAncestorCore(root, p, q)
        if LCA and hasP and hasQ:
            return LCA

        return None  # type: ignore
