from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    dummyHead = ListNode(0)
    cur = dummyHead
    minHeap = []

    for list in lists:
        heappush(minHeap, list)

    while minHeap:
        minList = heappop(minHeap)
        cur.next = minList
        cur = cur.next

        if minList.next:
            heappush(minHeap, minList.next)

    return dummyHead.next

# Time O(N logK)
# Space O(K)


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
