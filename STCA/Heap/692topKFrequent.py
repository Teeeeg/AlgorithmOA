from heapq import heappop, heappush
from typing import List


class Entry:
    # 自定义比较器

    def __init__(self, word, freq) -> None:
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        # 若不想等则直接返回比较，freq小的弹出去
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            # 若相等，字典序大的弹出去
            return self.word > other.word


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dct = {}
        for word in words:
            dct[word] = dct.get(word, 0) + 1

        minHeap = []
        for word, freq in dct.items():
            entry = Entry(word, freq)
            heappush(minHeap, entry)
            if len(minHeap) > k:
                heappop(minHeap)

        res = []
        # 输出的时候应该用heappop
        # 才能保证有序性
        while minHeap:
            res.append(heappop(minHeap).word)
        return res[::-1]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
slt = Solution()
print(slt.topKFrequent(words, k))