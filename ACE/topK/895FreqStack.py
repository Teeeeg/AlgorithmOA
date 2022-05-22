from heapq import heappop, heappush

# 定义一个新的类
# seq表示第几个进栈


class Element:
    def __init__(self, val, freq, seq) -> None:
        self.val = val
        self.freq = freq
        self.seq = seq

    # 比较器
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        return self.seq > other.seq


class FreqStack:

    def __init__(self):
        self.maxHeap = []
        # 外部存储所以节点的频率
        self.freqMap = {}
        self.seq = 0

    def push(self, val: int) -> None:
        self.freqMap[val] = self.freqMap.get(val, 0)+1
        heappush(self.maxHeap, Element(val, self.freqMap[val], self.seq))
        self.seq += 1

    def pop(self) -> int:
        res = heappop(self.maxHeap).val
        self.freqMap[res] -= 1
        # 删除节点，节省空间
        # if self.freqMap[res] == 0:
        #     del self.freqMap[res]

        return res
