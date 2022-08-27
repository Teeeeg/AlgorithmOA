from typing import List


class Node:

    def __init__(self, val, pre=None, next=None) -> None:
        self.val = val
        self.pre = pre
        self.next = next


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.duplicates = set()
        self.unique = {}

        self.head = Node(0)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

        for num in nums:
            self.add(num)

    def removeNode(self, node):
        pre = node.pre
        post = node.next
        pre.next = post
        post.pre = pre

    def addNode(self, node):
        pre = self.tail.pre
        pre.next = node
        node.pre = pre
        node.next = self.tail
        self.tail.pre = node

    def showFirstUnique(self) -> int:
        if self.head.next != self.tail:
            return self.head.next.val

        return -1

    def add(self, value: int) -> None:
        # skip if it is already duplicated
        if value in self.duplicates:
            return

        if value in self.unique:
            node = self.unique[value]
            self.removeNode(node)
            self.duplicates.add(value)
            del self.unique[value]
        else:
            node = Node(value)
            self.unique[value] = node
            self.addNode(node)


fu = FirstUnique([2, 3, 5])
print(fu.showFirstUnique())
fu.add(5)
print(fu.showFirstUnique())
fu.add(2)
print(fu.showFirstUnique())
fu.add(3)
print(fu.showFirstUnique())
