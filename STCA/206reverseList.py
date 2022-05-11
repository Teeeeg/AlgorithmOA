# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseListCore(None, head)

    def reverseListCore(self, pre, cur):
        if not cur:
            return pre
        post = cur.next
        cur.next = pre

        return self.reverseListCore(cur, post)
