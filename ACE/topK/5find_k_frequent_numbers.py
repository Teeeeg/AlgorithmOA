from heapq import heappop, heappush


def find_k_frequent_numbers(nums, k):
    n = len(nums)
    minHeap = []
    dct = {}

    for num in nums:
        if num not in dct:
            dct[num] = 0
        dct[num] += 1

    for freq, v in dct.items():
        if len(minHeap) < k:
            heappush(minHeap, (v, freq))
        else:
            if v > minHeap[0][0]:
                heappop(minHeap)
                heappush(minHeap, (v, freq))

    return [_[1] for _ in minHeap]


def main():

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
