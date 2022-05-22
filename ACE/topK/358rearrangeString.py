from heapq import heappop, heappush


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if len(s) == 1:
            return s
        if k == 0:
            return s

        maxHeap = []
        dct = {}
        res = []

        for ch in s:
            dct[ch] = dct.get(ch, 0)+1

        for ch, freq in dct.items():
            heappush(maxHeap, (-freq, ch))
        
        # 用队列保存之前的几次节点，队列保存操作次数，所以不提前过滤
        queue = []
        while maxHeap:
            # 获取最新节点，并且加入结果集
            freq, ch = heappop(maxHeap)
            res.append(ch)
            # 与此同时加入队列，表明现在进行了几步操作
            queue.append((freq+1, ch))

            # 进行了k次操作
            if len(queue) == k:
                # 将队列中的一个元素放回去
                freq, ch = queue.pop(0)
                # 过滤掉失效的节点
                if freq < 0:
                    heappush(maxHeap, (freq, ch))

        return ''.join(res) if len(res) == len(s) else ''
