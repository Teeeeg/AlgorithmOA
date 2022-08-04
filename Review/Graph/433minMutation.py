from typing import List


class Solution:
    # use bfs to find the shortest way

    def getNext(self, cur: str):
        res = []
        for gen in self.bank:
            count = 0
            for i in range(len(cur)):
                if cur[i] != gen[i]:
                    count += 1
            if count == 1:
                res.append(gen)

        return res

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        self.bank = bank
        visited = set()
        res = 0

        queue = [start]

        while queue:
            n = len(queue)
            # for every layer of the queue
            for _ in range(n):
                cur = queue.pop(0)
                if cur == end:
                    return res
                visited.add(cur)
                for next in self.getNext(cur):
                    if next not in visited:
                        queue.append(next)
            res += 1

        return -1


start = "AAAAAAAA"
end = "CCCCCCCC"
bank = ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA"]
slt = Solution()
print(slt.minMutation(start, end, bank))