# Definition for a Node.
from typing import Any, Optional


class Node:

    def __init__(self, x: int, next: 'Node' = Any, random: 'Node' = Any):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # 字典中记录的是
        # {旧，复制}
        dct = {}
        cur = head
        # 第一遍遍历创建新的节点
        while cur:
            node = Node(cur.val)
            dct[cur] = node
            cur = cur.next
        # 第二遍遍历更新next和randoom
        cur = head
        while cur:
            dct[cur].next = dct.get(cur.next, None)
            dct[cur].random = dct.get(cur.random, None)
            cur = cur.next

        return dct[head]

    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # 第一遍遍历在旧节点之后创建新节点，横向复制
        # 1->1->2->2
        cur = head
        while cur:
            node = Node(cur.val)
            post = cur.next
            cur.next = node
            node.next = post
            # 更新下个迭代
            cur = post

        cur = head
        # 第二遍遍历更新next和random
        while cur:
            node = cur.next
            # 此处因为有.next所以先判断是否越界
            if cur.random:
                # 注意最后要加next
                node.random = cur.random.next
            # 更新下个迭代
            cur = node.next

        # 第三遍遍历，截取出新的节点们
        cur = head
        dummyHead = Node(0)
        newCur = dummyHead
        while cur:
            node = cur.next
            post = node.next
            newCur.next = node
            # 更新下个迭代
            newCur = newCur.next
            cur = post

        return dummyHead.next
