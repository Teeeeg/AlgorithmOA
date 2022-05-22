from heapq import heappop, heappush


def minimum_cost_to_connect_ropes(ropeLengths):
    res = 0
    minHeap = []

    for rope in ropeLengths:
        heappush(minHeap, rope)

    while len(minHeap) > 1:
        tmp = heappop(minHeap) + heappop(minHeap)
        res += tmp
        heappush(minHeap, tmp)

    return res


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
