from heapq import heappop, heappush


class MedianOfAStream:
    maxHeap = []
    minHeap = []

    # 维护两个堆
    # 大的一半放小堆
    # 小的放大堆
    # 奇数情况下，默认小堆=大堆+1
    # 中位数则与小堆顶和大堆顶相关
    def insert_num(self, num):
        if not self.minHeap or self.minHeap[0] <= num:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)

        if len(self.minHeap) > len(self.maxHeap)+1:
            heappush(self.maxHeap, -heappop(self.minHeap))
        elif len(self.minHeap) < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))

    def find_median(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0

        return self.minHeap[0] / 1.0


# Time O(logn)
# Space O(n)

def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
