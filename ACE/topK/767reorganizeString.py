from heapq import heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = []
        dct = {}
        res = []

        for ch in s:
            dct[ch] = dct.get(ch, 0)+1

        for ch, freq in dct.items():
            heappush(maxHeap, (-freq, ch))

        # 交叉加入结果
        # 用于保存上一个节点
        preFreq, preCh = 0, None
        while maxHeap:
            # 获取最新节点，并且加入结果
            freq, ch = heappop(maxHeap)
            res.append(ch)

            # 如果上一个还有则放回heap
            if -preFreq > 0:
                heappush(maxHeap, (preFreq, preCh))

            # 将上一个节点更新为现在的节点
            preCh = ch
            preFreq = freq+1

        return ''.join(res) if len(res) == len(s) else ''
