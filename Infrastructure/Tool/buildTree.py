from typing import List, Optional


class TreeNode:

    def __init__(self, val) -> None:
        self.val = val
        self.left = Optional[TreeNode]
        self.right = Optional[TreeNode]


def buildTreeCore(nums, index):
    if index > len(nums) - 1:
        return

    if nums[index] == '#':
        return

    root = TreeNode(nums[index])

    root.left = buildTreeCore(nums, 2 * index + 1)
    root.right = buildTreeCore(nums, 2 * index + 2)

    return root


def buildTree(nums):
    tree = buildTreeCore(nums, 0)
    return tree


def preOrderCore(root: Optional[TreeNode], res: List[int]):
    if not root:
        return

    res.append(root.val)
    preOrderCore(root.left, res)
    preOrderCore(root.right, res)


def preOrder(root: TreeNode):
    res = []
    preOrderCore(root, res)

    return res


nums = [1, 2, '#', 3, 4, '#', '#', 5]
root = buildTree(nums)
preOrderRes = preOrder(root)
print(preOrderRes)