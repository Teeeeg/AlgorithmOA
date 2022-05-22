from heapq import heappop, heappush


def find_sum_of_elements(nums, k1, k2):
    maxHeap = []
    res = 0

    for num in nums:
        if len(maxHeap) < k2-1:
            heappush(maxHeap, -num)
        else:
            if num < -maxHeap[0]:
                heappop(maxHeap)
                heappush(maxHeap, -num)

    for _ in range(k2-k1-1):
        res += -heappop(maxHeap)

    return res


# Time O(nlogn)
# Space O(n)


def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
