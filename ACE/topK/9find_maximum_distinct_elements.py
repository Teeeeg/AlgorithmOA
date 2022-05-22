
from heapq import heappop, heappush


def find_maximum_distinct_elements(nums, k):
    distincts = 0
    if not nums:
        return 0

    dct = {}
    minHeap = []

    for num in nums:
        dct[num] = dct.get(num, 0) + 1

    for num, freq in dct.items():
        if freq == 1:
            distincts += 1
        else:
            heappush(minHeap, (freq, num))

    while k > 0 and minHeap:
        freq, num = heappop(minHeap)

        k -= freq-1

        if k >= 0:
            distincts += 1

    if k > 0:
        distincts -= k

    return distincts


def main():

    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
