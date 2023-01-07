from typing import List


class Solution:

    def canCompleteCircuitCore(self, gas: List[int], cost: List[int], index, count, gasLeft):
        n = len(gas)

        if count == n:
            return True

        gasLeft = gasLeft - cost[index] + gas[index]
        if gasLeft < 0:
            return False

        if self.canCompleteCircuitCore(gas, cost, (index + 1) % n, count + 1, gasLeft):
            return True

        return False

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for index in range(len(gas)):
            if self.canCompleteCircuitCore(gas, cost, index, 0, 0):
                return index

        return -1


class Solution1:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)

        agg = 0
        res = -1
        for i in range(n):
            diff = gas[i] - cost[i]
            agg += diff

            if agg < 0:
                res = i + 1
                agg = 0

        return res


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
slt = Solution1()
print(slt.canCompleteCircuit(gas, cost))
