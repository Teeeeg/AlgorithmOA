from typing import Any


class Node:
    def __init__(self, key=0, value=0) -> None:
        self.key = key
        self.value = value
        self.pre = Any
        self.next = Any


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def deleteNode(self, node: Node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self, node: Node):
        self.deleteNode(node)
        self.addToHead(node)

    def deleteTail(self):
        node = self.tail.pre
        self.deleteNode(node)
        return node

    def addToHead(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    # 将size的处理都放在put中
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                delNode = self.deleteTail()
                self.cache.pop(delNode.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
