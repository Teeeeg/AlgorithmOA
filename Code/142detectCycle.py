# Definition for singly-linked list.
from typing import Any


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = Any


class Solution:
    def detectCycle(self, head: ListNode):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p = head
                inLoop = slow
                while p != inLoop:
                    p = p.next
                    inLoop = inLoop.next
                return p

        return None
