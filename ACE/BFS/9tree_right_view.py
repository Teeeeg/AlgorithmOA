from __future__ import print_function
from collections import deque
from lib2to3.pytree import Node


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root: Node):
    if not root:
        return root
    queue = [root]
    res = []

    while queue:
        len_level = len(queue)

        for i in range(len_level):
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            if i == len_level-1:
                res.append(cur)

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
