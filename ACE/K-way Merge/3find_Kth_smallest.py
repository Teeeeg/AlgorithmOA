from heapq import heappop, heappush


def find_Kth_smallest(matrix, k):
    minHeap = []

    for i, row in enumerate(matrix):
        heappush(minHeap, (row[0], 0, i))
        if len(minHeap) == k:
            return minHeap[0]

    count = res = 0
    while minHeap:
        count += 1
        res, eIndex, rowIndex = heappop(minHeap)

        if count == k:
            break

        if eIndex+1 < len(matrix[rowIndex]):
            heappush(minHeap, (matrix[rowIndex][eIndex+1], eIndex+1, rowIndex))

    return res


# Time O(KlogN + min(K, N))
# K 为题目k， N为行数

def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
