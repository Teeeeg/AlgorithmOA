from heapq import heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        dct = {}
        res = 0

        for task in tasks:
            dct[task] = dct.get(task, 0)+1

        for task, freq in dct.items():
            heappush(maxHeap, (-freq, task))

        while maxHeap:
            # 等待队列，必须是有效的，因此过滤
            waitList = []
            # n+1，因为n个间隔
            interval = n+1

            # 一个间隔内，添加结果，并且记录有效节点
            while interval > 0 and maxHeap:
                freq, task = heappop(maxHeap)
                res += 1
                if freq+1 < 0:
                    waitList.append((freq+1, task))
                interval -= 1

            # 上门一个结束，要么间隔结束，要么间隔没结束还有等待的
            # 若有等待队列
            if waitList:
                # 等待剩下的间隔
                res += interval

            # 将节点放回heap
            for freq, task in waitList:
                heappush(maxHeap, (freq, task))

        return res


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
solution = Solution()
print(solution.leastInterval(tasks, n))
