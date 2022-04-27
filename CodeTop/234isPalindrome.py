# Definition for singly-linked list.
import re


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummyHead = ListNode(next=head)
        slow = fast = dummyHead

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None

        reversedHead = self.reverseList(secondHalf)
        cur1 = head
        cur2 = reversedHead

        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        return True

    def reverseList(self, head: ListNode):
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
