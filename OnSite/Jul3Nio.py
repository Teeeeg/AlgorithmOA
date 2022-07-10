from typing import List


class Solution:

    def __init__(self) -> None:
        self.flag = False
        self.visited = [False] * 6
        self.first = [0] * 3
        self.second = [0] * 3

    def check(self, sticks: List[int]):
        if sticks[0] + sticks[1] > sticks[2] and sticks[1] + sticks[2] > sticks[0] and sticks[0] + sticks[2] > sticks[1]:
            return True
        return False

    def canConstructCore(self, data: List[int], count: int, cur):
        if self.flag:
            return

        if count == 3:
            if self.check(self.first):
                p = 0
                for i in range(6):
                    if not self.visited[i]:
                        self.second[p] = data[i]
                        p += 1
                if self.check(self.second):
                    self.flag = True
        else:
            self.visited[cur] = True
            self.first[count] = data[cur]
            for i in range(cur + 1, 6):
                if not self.visited[i]:
                    self.canConstructCore(data, count + 1, i)
                    self.visited[i] = False

    def canConstruct(self, data: List[int]):
        self.canConstructCore(data, 0, 0)
        return self.flag


n = int(input())
for _ in range(n):
    data = [int(x) for x in input().split()]
    slt = Solution()
    res = slt.canConstruct(data)
    if res:
        print('Yes')
    else:
        print('No')