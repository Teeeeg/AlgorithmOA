# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        leftNums = nums[: mid]
        rightNums = nums[mid+1:]

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(leftNums)  # type: ignore
        root.right = self.sortedArrayToBST(rightNums)  # type: ignore

        return root
