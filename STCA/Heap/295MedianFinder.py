from heapq import heappop, heappush


class MedianFinder:

    def __init__(self):
        # 保存前面的，奇数前面比后面多一个
        self.maxHeap = []
        # 保存后面的
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # 小的一直往前面加
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        # 否则加到后面
        else:
            heappush(self.minHeap, num)

        # 平衡
        # 前面多了，奇数前面比后面多一个
        if len(self.maxHeap) > len(self.minHeap) + 1:
            # 把当前后面最小的放到前面去
            heappush(self.minHeap, -heappop(self.maxHeap))
        # 后面多了，把前面的最大放到后面去
        if len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        return -self.maxHeap[0] / 1.0


slt = MedianFinder()
slt.addNum(6)
print(slt.findMedian())
slt.addNum(10)
print(slt.findMedian())

slt.addNum(2)
print(slt.findMedian())

slt.addNum(6)
print(slt.findMedian())

slt.addNum(5)
print(slt.findMedian())

slt.addNum(0)
print(slt.findMedian())

slt.addNum(6)
print(slt.findMedian())

slt.addNum(3)
print(slt.findMedian())

slt.addNum(1)
print(slt.findMedian())

slt.addNum(0)
print(slt.findMedian())

slt.addNum(0)
print(slt.findMedian())
