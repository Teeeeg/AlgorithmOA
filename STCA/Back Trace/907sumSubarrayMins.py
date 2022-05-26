from typing import List


class Solution:
    # 暴力
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res = []
        for i in range(n):
            for j in range(i, n):
                res.append(min(arr[i:j + 1]))

        return sum(res)

    # 单调递减栈
    # 具体思路和直方图一样
    def sumSubarrayMins1(self, arr: List[int]) -> int:
        # 最前面插入，以计算第一次
        arr.insert(0, 0)
        # 最后添加一个用于计算最后一个
        arr.append(0)
        # 先入栈第一个
        descStack = [0]
        res = 0

        for i in range(1, len(arr)):
            # 不断从递减栈中pop出比当前值大的
            while descStack and arr[descStack[-1]] > arr[i]:
                # 获取比他大的值的下标
                midIndex = descStack.pop()
                if descStack:
                    leftIndex = descStack[-1]
                    rightIndex = i
                    num = arr[midIndex]
                    # 在(left, right) 之间的最小值都应该是 midIndex
                    # 因为利用递减栈，left到midIndex之间的数字都比midIndex的值大
                    # midIndex 到right 一样
                    # 则可以计算出一共多少种顺序
                    # 左边有m个 中间1个 右边n个
                    # m*n + m + n + 1 = (m+1)(n+1)
                    res += num * (rightIndex - midIndex) * (midIndex - leftIndex)

            descStack.append(i)

        return res % (10**9 + 7)


arr = [3, 1, 2, 4]
slt = Solution()
print(slt.sumSubarrayMins1(arr))