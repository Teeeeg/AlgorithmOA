from heapq import heappop, heappush


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        visited = set()
        visited.add(1)
        factors = [2, 3, 5]
        cur = 1

        for _ in range(n):
            cur = heappop(minHeap)
            for factor in factors:
                num = factor * cur
                if num in visited:
                    continue
                visited.add(num)
                heappush(minHeap, factor * cur)

        return cur


class Solution1:

    def nthUglyNumber(self, n: int) -> int:
        opt = [0] * n
        opt[0] = 1
        index1 = 0
        index2 = 0
        index3 = 0

        for i in range(1, n):
            opt[i] = min(opt[index1] * 2, opt[index2] * 3, opt[index3] * 5)
            if opt[i] % 2 == 0:
                index1 += 1

            if opt[i] % 3 == 0:
                index2 += 1

            if opt[i] % 5 == 0:
                index3 += 1

        return opt[-1]


slt = Solution()
print(slt.nthUglyNumber(10))