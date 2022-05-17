from typing import List


class Solution:

    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        total = sum(arr)
        if total % 3:
            return False
        target = total // 3

        part = 0
        count = 0
        for i in range(n):
            part += arr[i]
            if part == target:
                count += 1
                part = 0

            if count == 2 and i != n - 1:
                last = sum(arr[i + 1:])
                return last == target

        return False


arr = [1, -1, 1, -1]
slt = Solution()
print(slt.canThreePartsEqualSum(arr))