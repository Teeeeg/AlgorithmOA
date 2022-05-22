from heapq import heappop, heappush


class Solution:
    def frequencySort(self, s: str) -> str:
        dct = {}
        maxHeap = []
        res = []

        for chr in s:
            if chr not in dct:
                dct[chr] = 0
            dct[chr] += 1

        for chr, freq in dct.items():
            heappush(maxHeap, (-freq, chr))

        while maxHeap:
            freq, chr = heappop(maxHeap)
            for _ in range(-freq):
                res.append(chr)

        return ''.join(res)


s = "tree"
solution = Solution()
print(solution.frequencySort(s))
