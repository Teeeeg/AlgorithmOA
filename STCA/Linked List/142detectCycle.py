# Definition for singly-linked list.
from typing import Any


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = Any


class Solution:

    def detectCycle(self, head: ListNode):
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # 快慢指针找到重合点
            if slow == fast:
                # 一个指针从头出发
                p = head
                inLoop = slow
                # 方程 2(x+y) = n(y+z) + (x+y)
                # x+y = n(y+z)
                # x = (n-1)(y+z) + z
                while p != inLoop:
                    p = p.next
                    inLoop = inLoop.next

                return p

        return None
