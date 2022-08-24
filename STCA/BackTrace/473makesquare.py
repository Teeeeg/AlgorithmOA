from typing import List


class Solution:

    def __init__(self) -> None:
        self.buckets = [0] * 4

    def makesquareCore(self, matchsticks: List[int], matchId):
        if matchId == len(matchsticks):
            return self.buckets[0] == self.buckets[1] == self.buckets[2] == self.buckets[3]

        for i in range(4):
            # only if buckets <= length, it will go deeper
            if self.buckets[i] + matchsticks[matchId] <= self.length:
                self.buckets[i] += matchsticks[matchId]
                if self.makesquareCore(matchsticks, matchId + 1):
                    return True
                self.buckets[i] -= matchsticks[matchId]

        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        total = sum(matchsticks)
        # if it cannot form a square
        if total % 4:
            return False

        self.length = total // 4
        # from biggest to smallest
        matchsticks.sort(reverse=True)

        return self.makesquareCore(matchsticks, 0)


matchsticks = [14, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 8, 9, 19]
slt = Solution()
print(slt.makesquare(matchsticks))