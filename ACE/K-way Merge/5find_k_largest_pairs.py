from heapq import heappop, heappush


def find_k_largest_pairs(nums1, nums2, k):
    n1 = len(nums1)
    n2 = len(nums2)
    minHeap = []

    for i in range(min(k, n1)):
        for j in range(min(k, n2)):
            if len(minHeap) < k:
                heappush(minHeap, (nums1[i]+nums2[j], nums1[i], nums2[j]))
            else:
                # 降序的，再小就不要了
                if nums1[i]+nums2[j] < minHeap[0][0]:
                    break
                else:
                    heappop(minHeap)
                    heappush(minHeap, (nums1[i]+nums2[j], nums1[i], nums2[j]))

    return [[tup[1], tup[2]] for tup in minHeap]


def main():
    print("Pairs with largest sum are: " +
          str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
