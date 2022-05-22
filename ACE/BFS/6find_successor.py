from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    if not root:
        return None

    cur = root
    queue = []
    queue.append(cur)

    # 不需要按层收集，只需要放入queue中
    while queue:
        cur = queue.pop(0)
        if cur.left:
            queue.append(cur.left)
        if cur.left:
            queue.append(cur.right)
        # 找到对应的key，则queue的队头则为答案
        if cur.val == key:
            break

    return queue[0] if queue else None


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 9)
    if result:
        print(result.val)

    result = find_successor(root, 12)
    if result:
        print(result.val)


main()
