from collections import Counter
from heapq import heappop, heappush


class Solution:

    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        maxHeap = []
        for entry in counter.items():
            heappush(maxHeap, (-entry[1], entry[0]))
        res = ''
        while maxHeap:
            count, ch = heappop(maxHeap)
            res += ch * (-count)

        return res


s = "tree"
slt = Solution()
print(slt.frequencySort(s))