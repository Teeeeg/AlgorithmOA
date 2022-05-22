from heapq import heappop, heappush
import heapq


class SlidingWindowMedian:
    def __init__(self) -> None:
        self.minHeap = []
        self.maxHeap = []

    def find_sliding_window_median(self, nums, k):
        res = []
        n = len(nums)

        for i in range(n):
            if not self.minHeap or self.minHeap[0] <= nums[i]:
                heappush(self.minHeap, nums[i])
            else:
                heappush(self.maxHeap, -nums[i])

            self.rebalance()

            if i-k+1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    res.append((self.minHeap[0] - self.maxHeap[0]) / 2.0)
                else:
                    res.append(self.minHeap[0] / 1.0)

                numToRemove = nums[i-k+1]
                if numToRemove >= self.minHeap[0]:
                    self.removeLeft(self.minHeap, numToRemove)
                else:
                    self.removeLeft(self.maxHeap, -numToRemove)

            self.rebalance()
        return res

    def rebalance(self):
        if len(self.minHeap) > len(self.maxHeap)+1:
            heappush(self.maxHeap, -heappop(self.minHeap))
        if len(self.minHeap) < len(self.maxHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))

    def removeLeft(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        del heap[-1]

        heapq.heapify(heap)


# Time O(n*K)
# Space O(K)


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
