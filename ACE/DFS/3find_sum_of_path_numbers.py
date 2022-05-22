class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root: TreeNode):
    def dfs(root: TreeNode, pathSum: int):
        if not root:
            return 0

        pathSum = root.val + pathSum*10
        if not root.left and not root.right:
            return pathSum

        return dfs(root.left, pathSum) + dfs(root.right, pathSum)
    return dfs(root, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
