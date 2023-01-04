from typing import List


class Solution:

    def getResult(self, count):
        div, mod = divmod(count, 3)

        if mod:
            return div + 1

        return div

    def minimumRounds(self, tasks: List[int]) -> int:
        dif2Count = {}
        res = 0

        for task in tasks:
            dif2Count[task] = dif2Count.get(task, 0) + 1

        for count in dif2Count.values():
            if count == 1:
                return -1

            res += self.getResult(count)
        return res


tasks = [
    66, 66, 63, 61, 63, 63, 64, 66, 66, 65, 66, 65, 61, 67, 68, 66, 62, 67, 61, 64, 66, 60, 69, 66, 65, 68, 63, 60, 67, 62, 68, 60, 66, 64, 60, 60, 60, 62, 66, 64, 63, 65, 60, 69, 63, 68, 68, 69, 68,
    61
]
slt = Solution()
print(slt.minimumRounds(tasks))