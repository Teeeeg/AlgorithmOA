from random import randint
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # divide
    def mergeKListsCore(self, left, right):
        if left > right:
            return

        if left == right:
            return self.lists[left]

        mid = (left + right) // 2
        return self.mergeTwo(self.mergeKListsCore(left, mid), self.mergeKListsCore(mid + 1, right))

    # conquer
    def mergeTwo(self, leftList, rightList):
        dummyHead = ListNode(-1)
        cur = dummyHead
        cur1 = leftList
        cur2 = rightList

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next

            cur = cur.next

        while cur1:
            cur.next = cur1
            cur1 = cur1.next
            cur = cur.next

        while cur2:
            cur.next = cur2
            cur2 = cur2.next
            cur = cur.next

        return dummyHead.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.lists = lists
        n = len(lists)

        return self.mergeKListsCore(0, n - 1)


class MyHeap:

    def __init__(self) -> None:
        self.data = []

    @property
    def size(self):
        return len(self.data)

    def comparator(self, head1: ListNode, head2: ListNode):
        return -head1.val < -head2.val

    def swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    def siftDown(self, index, heapLen):
        while index * 2 + 1 < heapLen:
            lIndex = index * 2 + 1
            rIndex = index * 2 + 2
            sIndex = index

            if self.comparator(self.data[sIndex], self.data[lIndex]):
                sIndex = lIndex
            if rIndex < heapLen and self.comparator(self.data[sIndex], self.data[rIndex]):
                sIndex = rIndex

            if sIndex == index:
                break

            self.swap(index, sIndex)
            index = sIndex

    def siftUp(self, index):
        while index:
            sIndex = index
            pIndex = (index - 1) // 2
            if self.comparator(self.data[pIndex], self.data[sIndex]):
                sIndex = pIndex

            if sIndex == index:
                break

            self.swap(sIndex, index)
            index = sIndex

    def pop(self):
        res = self.data[0]
        self.swap(0, self.size - 1)
        self.data.pop()
        self.siftDown(0, self.size)
        return res

    def push(self, value):
        self.data.append(value)
        self.siftUp(self.size - 1)


class Solution1:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or (len(lists) == 1 and not lists[0]):
            return

        heap = MyHeap()
        dummyHead = ListNode(-1)
        cur = dummyHead

        for head in lists:
            if head:
                heap.push(head)

        while heap.size:
            cur1 = heap.pop()
            cur.next = cur1
            cur = cur.next
            if cur1.next:
                heap.push(cur.next)

        return dummyHead.next


# head1 = ListNode(1)
# head1.next = ListNode(4)
# head1.next.next = ListNode(5)

# head2 = ListNode(1)
# head2.next = ListNode(3)
# head2.next.next = ListNode(4)

# head3 = ListNode(2)
# head3.next = ListNode(6)

slt = Solution1()


def createFromList(nums):
    dummyHead = ListNode(-1)
    cur = dummyHead
    for num in nums:
        cur.next = ListNode(num)  # type: ignore
        cur = cur.next

    return dummyHead.next


def printLinkedList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next

    print(res)


[[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]]
head1 = createFromList([-8, -7, -7, -5, 1, 1, 3, 4])
head2 = createFromList([-2])
head3 = createFromList([-10, -10, -7, 0, 1, 3])
head4 = createFromList([2])

lists = [head1, head2, head3, head4]

res = slt.mergeKLists(lists)  # type: ignore
printLinkedList(res)