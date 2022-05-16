# Definition for singly-linked list.
from typing import Any


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = Any


class Solution:

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        slow = head

        for _ in range(k):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow