class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length(head: Node):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    res = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        res += 1
        if slow == fast:
            return res
