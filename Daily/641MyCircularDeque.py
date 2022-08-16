from typing import Any


class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = Any[Node]
        self.pre = Any[Node]


class MyCircularDeque:

    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.head.pre = self.tail
        self.tail.pre = self.head
        self.tail.next = self.head

    def insertFront(self, value: int) -> bool:
        if self.size < self.maxSize:
            node = Node(value)
            post = self.head.next
            self.head.next = node
            node.pre = self.head
            node.next = post
            post.pre = node
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.maxSize:
            node = Node(value)
            pre = self.tail.pre
            self.tail.pre = node
            node.next = self.tail
            node.pre = pre
            pre.next = node
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.size > 0:
            post = self.head.next.next
            self.head.next = post
            post.pre = self.head
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            pre = self.tail.pre.pre
            self.tail.pre = pre
            pre.next = self.tail
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.size > 0:
            return self.head.next.value
        return -1

    def getRear(self) -> int:
        if self.size > 0:
            return self.tail.pre.value
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize