class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.start = None
        self.last = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        self.treeToDoublyListCore(root)
        self.last.right = self.first
        self.first.left = self.last

    def treeToDoublyListCore(self, root: 'Node'):
        if not root:
            return None

        self.treeToDoublyListCore(root.left)

        if self.last:
            self.last.right = root
            root.left = self.last
        else:
            self.first = root

        self.last = root

        self.treeToDoublyListCore(root.right)


class Solution1:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        cur = root
        stack = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if self.tail:
                self.tail.right = cur
                cur.left = self.tail
            else:
                self.head = cur
            self.tail = cur

            cur = cur.right

        self.tail.right = self.head
        self.head.left = self.tail

        return self.head
