class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head: Node):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
