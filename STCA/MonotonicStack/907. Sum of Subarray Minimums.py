from typing import List


class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        monoStack = []
        res = 0

        for i in range(n + 1):
            curNum = 0
            if i < n:
                curNum = arr[i]
            while monoStack and arr[monoStack[-1]] >= curNum:
                midIndex = monoStack.pop()
                leftIndex = monoStack[-1] if monoStack else -1
                rightIndex = i
                res += arr[midIndex] * (rightIndex - midIndex) * (midIndex - leftIndex)

            monoStack.append(i)

        return res % MOD


arr = [3, 1, 2, 4]
slt = Solution()
print(slt.sumSubarrayMins(arr))