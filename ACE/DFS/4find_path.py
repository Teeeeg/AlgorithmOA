class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    n = len(sequence)
    if not root:
        return n == 0

    def dfs(root: TreeNode, index):
        if not root:
            return False

        if index >= n or root.val != sequence[index]:
            return False

        if not root.left and not root.right and index == n-1:
            return True

        return dfs(root.left, index+1) or dfs(root.right, index+1)

    return dfs(root, 0)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
