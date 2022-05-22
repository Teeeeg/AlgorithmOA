from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    res = []
    queue = []

    if not root:
        return res

    cur = root
    queue.append(cur)
    # 用一个bool表示顺序
    leftToRight = True

    while queue:
        cur_level = deque()
        len_level = len(queue)
        for _ in range(len_level):
            cur = queue.pop(0)
            if leftToRight:
                cur_level.append(cur.val)
            else:
                cur_level.appendleft(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        leftToRight = not leftToRight
        res.append(list(cur_level))

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
