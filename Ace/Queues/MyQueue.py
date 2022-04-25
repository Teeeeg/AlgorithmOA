class Node:
    def __init__(self, val, next=None, pre=None) -> None:
        self.val = val
        self.next = next
        self.pre = pre


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getHead(self):
        return self.head.val

    def isEmpty(self):
        return self.head == None

    def insertTail(self, val):
        self.size += 1
        node = Node(val)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node

        return node.val

    def removeHead(self):
        if self.isEmpty:
            return False
        node = self.head
        self.size -= 1
        if self.siz == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            self.head.pre = None
            node.next = None
        return node.val

    def getTail(self):
        return self.tail.val if self.head else None

    def __str__(self) -> str:
        if self.isEmpty():
            return ''
        node = self.head
        res = "[" + str(node.val) + ","
        node = node.next

        while node.next:
            res += str(node.val) + ','
            node = node.next
        res += str(node.val) + ']'
        return res


class MyQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def isEmpty(self):
        return self.data.size == 0

    def getFront(self):
        if self.isEmpty():
            return None
        return self.data.getHead()

    def getRear(self):
        if self.isEmpty():
            return None
        return self.data.getTail()

    def getSize(self):
        return self.data.size

    def enqueue(self, val):
        return self.data.insertTail(val)

    def dequeue(self):
        return self.data.getHead()

    def printList(self):
        return self.data.__str__()


myqueue = MyQueue()
print("queue.enqueue(2);")
myqueue.enqueue(2)
print("queue.enqueue(4);")
myqueue.enqueue(4)
print("queue.enqueue(6);")
myqueue.enqueue(6)
print("queue.enqueue(8);")
myqueue.enqueue(8)
print("queue.enqueue(10);")
myqueue.enqueue(10)

print(myqueue.printList())
print("is_empty(): " + str(myqueue.isEmpty()))
print("rear(): " + str(myqueue.getRear()))
print("front(): " + str(myqueue.getFront()))
print("size(): " + str(myqueue.getSize()))
