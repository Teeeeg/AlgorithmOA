from heapq import *


def rearrange_string(str):
    maxHeap = []
    dct = {}
    res = []

    for ch in str:
        dct[ch] = dct.get(ch, 0) + 1

    for ch, freq in dct.items():
        heappush(maxHeap, (-freq, ch))

    preChr, preFreq = None, 0

    while maxHeap:
        freq, ch = heappop(maxHeap)

        if preChr and -preFreq > 0:
            heappush(maxHeap, (preFreq, preChr))

        res.append(ch)
        preChr = ch
        preFreq = freq+1

    return ''.join(res) if len(res) == len(str) else ''

# Time O(nlogn)
# Space O(n)


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
