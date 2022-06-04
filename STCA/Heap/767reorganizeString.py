from heapq import heappop, heappush


class Solution:

    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        dct = {}

        # 计数
        for ch in s:
            dct[ch] = dct.get(ch, 0) + 1

        for ch, freq in dct.items():
            heappush(maxHeap, (-freq, ch))

        res = []
        # 每次拿两个交叉放
        while len(maxHeap) >= 2:
            freq1, ch1 = heappop(maxHeap)
            freq2, ch2 = heappop(maxHeap)
            res.append(ch1)
            freq1 += 1
            res.append(ch2)
            freq2 += 1

            if freq1 < 0:
                heappush(maxHeap, (freq1, ch1))

            if freq2 < 0:
                heappush(maxHeap, (freq2, ch2))
        # 若最后还有剩下的
        # 一定之一有1个
        if maxHeap:
            freq, ch = heappop(maxHeap)
            if freq == -1:
                res.append(ch)
            else:
                return ''

        return ''.join(res)


s = "aab"
slt = Solution()
print(slt.reorganizeString(s))