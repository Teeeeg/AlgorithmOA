class Node:
    def __init__(self, val=0) -> None:
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # O(1)
    def getHead(self):
        return self.head

    # O(1)
    def isEmpty(self):
        return self.head is None

    def insertAtHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        return self.head

    def printLinkedList(self):
        if self.isEmpty():
            print("List is empty")
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next


lst = LinkedList()
for i in range(10):
    lst.insertAtHead(i)

lst.printLinkedList()
