def find_cycle_start(head):
    slow = fast = head
    inLoop = None

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            inLoop = slow
            break

    start = head
    while start != inLoop:
        start = start.next
        inLoop = inLoop.next

    return start

# Time O(n)
