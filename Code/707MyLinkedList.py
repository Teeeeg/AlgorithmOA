from typing import Any


class MyLinkedListNode:
    def __init__(self, val=0, next=Any) -> None:
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummyHead = MyLinkedListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if not 0 <= index < self.size:
            return -1

        cur = self.dummyHead
        for _ in range(index+1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        n = index
        if n < 0:
            n = 0
        if n > self.size:
            return

        cur = self.dummyHead
        for _ in range(n):
            cur = cur.next
        post = cur.next
        node = MyLinkedListNode(val)
        cur.next = node
        node.next = post
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if not 0 <= index < self.size:
            return

        cur = self.dummyHead
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


linkedList = MyLinkedList()
print(linkedList.addAtHead(1))
print(linkedList.addAtTail(3))
print(linkedList.addAtIndex(1, 2))
print(linkedList.get(1))
print(linkedList.deleteAtIndex(1))
print(linkedList.get(1))
