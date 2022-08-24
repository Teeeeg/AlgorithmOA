from random import randint
from typing import List


class LinkedNode:

    def __init__(self, val=0, next=None, down=None) -> None:
        self.val = val
        self.next = next
        self.down = down


class Skiplist:

    def __init__(self):
        self.head = LinkedNode(-1)
        # self.level = 1
        # self.length = 1

    def get(self, target, start):
        pre = LinkedNode(next=start)
        cur = start
        while cur:
            while cur.next and target > cur.val:
                pre = cur
                cur = cur.next
            if cur.val == target:
                return pre
            cur = cur.down

        return None

    def search(self, target: int) -> bool:
        return True if self.get(target, self.head) else False

    def add(self, num: int) -> None:
        nodes = []
        cur = self.head
        while cur:
            while cur.next and cur.next.val < num:
                cur = cur.next
            nodes.append(cur)
            cur = cur.down

        node = nodes.pop()
        post = node.next
        newNode = LinkedNode(num)
        node.next = newNode
        newNode.next = post

        self.addIndex(num, nodes)

    def addIndex(self, num, nodes: List[LinkedNode]):
        flag = randint(0, 1)
        while flag and nodes:
            index = LinkedNode(num)
            node = nodes.pop()
            post = node.next
            node.next = index
            index.next = post  # type: ignore

            flag = randint(0, 1)

    def erase(self, num: int) -> bool:
        flag = False
        pre = self.get(num, self.head)

        while pre:
            pre.next = pre.next.next
            flag = True
            pre = self.get(num, pre.down)
        return flag


skipList = Skiplist()
skipList.add(1)
skipList.add(2)
skipList.add(2)
skipList.add(3)
skipList.erase(2)
print(skipList.search(3))
print(skipList.search(2))