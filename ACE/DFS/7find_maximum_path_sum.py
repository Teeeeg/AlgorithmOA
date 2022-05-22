import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_maximum_path_sum(root):
    res = -math.inf

    def dfs(root: TreeNode):
        nonlocal res
        if not root:
            return 0

        leftSum = dfs(root.left)
        rightSum = dfs(root.right)

        leftSum = max(leftSum, 0)
        rightSum = max(rightSum, 0)

        pathSum = leftSum + rightSum + root.val
        res = max(pathSum, res)

        return max(leftSum, rightSum)+root.val

    dfs(root)
    return res


def main():
    # maximumPathSum = MaximumPathSum()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()
