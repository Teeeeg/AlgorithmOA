# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
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

    def isPalindrome(self, head: ListNode) -> bool:
        dummyHead = ListNode(next=head)
        slow = dummyHead
        fast = dummyHead

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None  # type: ignore

        cur2 = self.reverse(head2)
        cur1 = head

        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False

            cur1 = cur1.next
            cur2 = cur2.next

        return True
