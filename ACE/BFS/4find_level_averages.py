from statistics import mean


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root: TreeNode):
    res = []
    queue = []
    cur = root

    if not root:
        return res

    queue.append(cur)
    while queue:
        cur_level = []
        len_level = len(queue)
        for _ in range(len_level):
            cur = queue.pop(0)
            cur_level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        res.append(mean(cur_level))

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
