from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        oddHead = head
        evenHead = head.next
        left = oddHead
        right = evenHead

        while right and right.next:
            nextLeft = right.next
            nextright = right.next.next

            left.next = nextLeft
            right.next = nextright

            left = nextLeft
            right = nextright

        left.next = evenHead

        return head
