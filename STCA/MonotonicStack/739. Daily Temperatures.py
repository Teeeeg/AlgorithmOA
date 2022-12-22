from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        descStack = []

        for i in range(n):
            while descStack and temperatures[descStack[-1]] < temperatures[i]:
                index = descStack.pop()
                res[index] = i - index
            descStack.append(i)

        return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
slt = Solution()
print(slt.dailyTemperatures(temperatures))