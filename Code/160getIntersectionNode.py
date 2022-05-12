# Definition for singly-linked list.
from typing import Any


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = Any


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        curB = headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA
