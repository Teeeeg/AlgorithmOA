from typing import List


class Solution:

    def countOnes(self, num: int):
        res = 0
        while num:
            res += 1
            num &= (num - 1)

        return res

    def sortByBits(self, arr: List[int]) -> List[int]:
        results = []

        for num in arr:
            results.append([num, self.countOnes(num)])

        results.sort(key=lambda x: (x[1], x[0]))

        res = [num[0] for num in results]

        return res


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
slt = Solution()
print(slt.sortByBits(arr))