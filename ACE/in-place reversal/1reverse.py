from __future__ import print_function
from typing import Any


class Node:

    def __init__(self, value, next=Any):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head: Node):
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


# Time O(n)
# Space O(1)

