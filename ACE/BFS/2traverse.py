from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    res = deque()
    queue = []

    if not root:
        return res

    cur = root
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

        res.appendleft(cur_level)

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
