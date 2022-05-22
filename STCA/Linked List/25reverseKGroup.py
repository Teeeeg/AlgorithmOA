# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head:
            return head

        pre = None
        cur = head

        # 记得有break
        while True:
            # 记录前一段的尾
            # 被翻转的尾
            tailOfPre = pre
            tailOfSub = cur
            i = 0

            # 该循环控制是否需要翻转
            # 即后面是否有个k个节点
            # 移除表示不满足也翻转
            tmp = cur
            for _ in range(k):
                if not tmp:
                    return head
                tmp = tmp.next

            # 正常翻转
            pre = None
            while cur and i < k:
                post = cur.next
                cur.next = pre
                pre = cur
                cur = post
                i += 1
            # 记录被翻转的头
            # 后一段的尾
            headOfSub = pre
            headOfPost = cur

            # 这是用于处理一开始的情况
            if tailOfPre:
                tailOfPre.next = headOfSub
            else:
                # 一开始的时候tailOfPre为None
                head = headOfSub

            # 连接到下一段
            tailOfSub.next = headOfPost
            # 记住更新pre
            # 被翻转的尾是下一个迭代的pre
            pre = tailOfSub
            # cur已经更新
            if not cur:
                break

        return head
