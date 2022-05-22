from heapq import heappop, heappush


def find_Kth_smallest(lists, k):
    minHeap = []

    for i, list in enumerate(lists):
        heappush(minHeap, (list[0], 0, i))

    count = num = 0
    while minHeap:
        num, eIndex, listIndex = heappop(minHeap)
        count += 1
        if count == k:
            break

        if len(lists[listIndex]) > eIndex + 1:
            heappush(minHeap, (lists[listIndex]
                     [eIndex+1], eIndex+1, listIndex))

    return num


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
