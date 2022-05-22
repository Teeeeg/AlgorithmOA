from heapq import heappop, heappush


def sort_character_by_frequency(str):
    dct = {}
    maxHeap = []
    res = []

    for ch in str:
        dct[ch] = dct.get(ch, 0) + 1

    for k, v in dct.items():
        heappush(maxHeap, (-v, k))

    while maxHeap:
        freq, ch = heappop(maxHeap)
        for _ in range(-freq):
            res.append(ch)

    return ''.join(res)

# Time O(NlogN)
# Space O(N)


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
