class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root: TreeNode, sum):
    res = []
    cur = []

    def dfs(root: TreeNode, sum):
        if not root:
            return
        cur.append(root.val)
        if root.val == sum and not root.left and not root.right:
            res.append(list(cur))
        else:
            dfs(root.left, sum-root.val)
            dfs(root.right, sum-root.val)
        # 回溯
        del cur[-1]

    dfs(root, sum)
    return res


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
