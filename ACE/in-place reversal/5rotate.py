from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head: Node, rotations):
    if not head or not head.next:
        return head

    len_list = 1
    tail = head
    while tail.next:
        tail = tail.next
        len_list += 1

    tail.next = head

    # 要移动后面的节点数
    # 需要把k个节点放到队头
    # 则需要定位到n-k，找到，前置节点
    rotations %= len_list
    # 则前面的节点数
    skip_len = len_list-rotations

    # 遍历到前一段的尾，所以-1
    tail_of_pre = head
    for _ in range(skip_len-1):
        tail_of_pre = tail_of_pre.next

    head = tail_of_pre.next
    # 前一段的尾节置空
    tail_of_pre.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 8)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
