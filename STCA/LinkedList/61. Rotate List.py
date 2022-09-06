# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def getTotalLen(self, head: Optional[ListNode]):
        totalLen = 0
        cur = head
        pre = None
        while cur:
            totalLen += 1
            pre = cur
            cur = cur.next

        return totalLen, pre

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        totalLen, tailNode = self.getTotalLen(head)
        if totalLen == 1:
            return head

        k %= totalLen
        if k == 0:
            return head
        step = totalLen - k

        dummyHead = ListNode(next=head)
        pre = dummyHead
        for _ in range(step):
            pre = pre.next

        curHead = pre.next
        pre.next = None

        tailNode.next = head

        return curHead


class Solution1:

    def getTotalLen(self, head: Optional[ListNode]):
        totalLen = 0
        cur = head
        while cur:
            totalLen += 1
            cur = cur.next

        return totalLen

    def reverse(self, head: Optional[ListNode]):
        if not head or not head.next:
            return head

        pre = None
        cur = head

        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post

        return pre

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        totalLen = self.getTotalLen(head)
        if totalLen <= 1:
            return head

        k %= totalLen
        if k == 0:
            return head

        reversedHead = self.reverse(head)
        cur1 = reversedHead
        tailOfReversed1 = reversedHead

        for _ in range(k - 1):
            cur1 = cur1.next

        head2 = cur1.next
        cur1.next = None

        resHead = self.reverse(reversedHead)
        headOfReversed2 = self.reverse(head2)
        tailOfReversed1.next = headOfReversed2

        return resHead
