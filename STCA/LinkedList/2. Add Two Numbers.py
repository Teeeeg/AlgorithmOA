from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        resHead = ListNode()
        cur = resHead
        carry = 0

        while cur1 or cur2:
            digit1 = 0
            if cur1:
                digit1 = cur1.val
                cur1 = cur1.next

            digit2 = 0
            if cur2:
                digit2 = cur2.val
                cur2 = cur2.next

            total = digit1 + digit2 + carry
            carry, digit = divmod(total, 10)

            cur.next = ListNode(digit)
            cur = cur.next

        if carry:
            cur.next = ListNode(carry)

        return resHead.next