from __future__ import print_function


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    if not root:
        return

    queue = []
    cur = root
    queue.append(cur)

    while queue:
        # 用于记录前一个节点
        pre = None
        len_level = len(queue)
        for _ in range(len_level):
            cur = queue.pop(0)
            if pre:
                pre.next = cur
            pre = cur

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
