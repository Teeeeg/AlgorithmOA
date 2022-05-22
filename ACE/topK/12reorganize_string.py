from heapq import heappop, heappush


def reorganize_string(str, k):
    dct = {}
    maxHeap = []
    res = []

    for ch in str:
        dct[ch] = dct.get(ch, 0) + 1

    for ch, freq in dct.items():
        heappush(maxHeap, (-freq, ch))

    queue = []
    while maxHeap:
        freq, ch = heappop(maxHeap)
        res.append(ch)
        # queue 表示完成了几次操作
        queue.append((freq+1, ch))
        # 完成k此操作，即距离为k后
        if len(queue) == k:
            freq, ch = queue.pop(0)
            if -freq > 0:
                heappush(maxHeap, (freq, ch))

    return ''.join(res) if len(res) == len(str) else ''


# Time O(nlogn)
# Space O(n)

def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
