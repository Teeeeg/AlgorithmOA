from typing import Any


class Node:

    def __init__(self, key=0, val=0, next=Any, pre=Any) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def addAtHead(self, node: Node):
        post = self.head.next
        node.pre = self.head
        node.next = post
        post.pre = node
        self.head.next = node

    def removeNode(self, node: Node):
        pre = node.pre
        post = node.next
        pre.next = post
        post.pre = pre
        return node

    def removeTail(self):
        return self.removeNode(self.tail.pre)

    def moveToHead(self, node: Node):
        self.removeNode(node)
        self.addAtHead(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.addAtHead(node)
            self.cache[key] = node
            self.size += 1

            if self.size > self.capacity:
                delNode = self.removeTail()
                delKey = delNode.key
                self.cache.pop(delKey)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))