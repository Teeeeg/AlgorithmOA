from importlib.resources import path


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    cur = []

    def dfs(root):
        if not root:
            return 0
        # cur中添加
        cur.append(root.val)
        pathSum = 0
        pathCount = 0
        # 寻找sum
        for i in range(len(cur)-1, -1, -1):
            pathSum += cur[i]
            if pathSum == S:
                # 满足
                pathCount += 1
        # 探索下一个节点
        pathCount += dfs(root.left)
        pathCount += dfs(root.right)

        # 回溯
        del cur[-1]

        return pathCount

    return dfs(root)


# Time O(n2)
# Space O(n)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
