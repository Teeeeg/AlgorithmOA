import math


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    res = 0
    if not root:
        return res
    cur = root
    queue = []
    queue.append(cur)

    while cur:
        # 每次开始时进行深度+1
        res += 1
        cur_level = []
        len_level = len(queue)

        for _ in range(len_level):
            cur = queue.pop(0)
            cur_level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            elif cur.right:
                queue.append(cur.right)
            else:
                return res

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
