from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 递增栈，出现大的就弹出来
        # 从栈顶到栈底为递增
        ascStack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            # 出现比栈顶大的就更新答案
            while ascStack and temperatures[ascStack[-1]] < temperatures[i]:
                cur = ascStack.pop()
                res[cur] = i - cur
            ascStack.append(i)

        return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
slt = Solution()
print(slt.dailyTemperatures(temperatures))