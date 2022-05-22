class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head: Node):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# Time O(n)
