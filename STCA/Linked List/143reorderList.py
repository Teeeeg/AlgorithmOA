# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: ListNode):
        if not head:
            return head

        pre = None
        cur = head
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post

        return pre

    def reorderList(self, head: ListNode) -> None:
        dummyHead = ListNode(next=head)
        slow = fast = dummyHead
        # 找到中间点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        postHead = slow.next
        slow.next = None  # type: ignore
        cur = head
        # 倒转
        cur1 = self.reverseList(postHead)

        while cur and cur1:
            post = cur.next
            post1 = cur1.next
            cur.next = cur1
            cur1.next = post
            cur = post
            cur1 = post1