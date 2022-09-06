class Node:

    def __init__(self, key=-1, val=-1) -> None:
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.key2Node = {}
        self.head.next = self.tail
        self.tail.pre = self.head

    def removeNode(self, node: Node):
        preNode = node.pre
        postNode = node.next
        preNode.next = postNode
        postNode.pre = preNode
        self.size -= 1

    def removeTail(self):
        key = self.tail.pre.key
        self.removeNode(self.tail.pre)
        return key

    def addToHead(self, node: Node):
        postNode = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = postNode
        postNode.pre = node
        self.size += 1

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def get(self, key: int) -> int:
        if key not in self.key2Node:
            return -1

        node = self.key2Node[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key2Node:
            node = self.key2Node[key]
            node.val = value
            self.moveToHead(node)
            return

        node = Node(key, value)
        self.key2Node[key] = node
        if self.size >= self.capacity:
            keyToDel = self.removeTail()
            del self.key2Node[keyToDel]
        self.addToHead(node)


cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
print(cache.get(1))
print(cache.get(2))