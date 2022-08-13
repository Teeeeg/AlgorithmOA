from heapq import heappop, heappush


def Solve(factories):
    if not factories:
        return 0

    total = sum(factories)
    if total == 0:
        return 0

    maxHeap = [-num for num in factories if num != 0]
    target = total / 2
    curPollution = total
    res = 0

    while curPollution > target:
        factory = -heappop(maxHeap)
        reduced = factory / 2
        curPollution -= reduced
        factory /= 2
        heappush(maxHeap, -factory)
        res += 1

    return res


factories = [5, 19, 8, 1]
factories1 = [10, 10]
factories2 = [3, 0, 5]
print(Solve(factories))
print(Solve(factories1))
print(Solve(factories2))