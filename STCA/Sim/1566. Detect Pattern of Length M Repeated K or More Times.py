from typing import List


class Solution:

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)

        for i in range(n - m + 1):
            pattern = arr[i:i + m]
            count = 1
            for j in range(i + m, n - m + 1):
                cur = arr[j:j + m]

                if cur != pattern:
                    break

                count += 1
                if count == k:
                    return True

        return False


arr = [1, 2, 3, 1, 2]
m = 2
k = 2
slt = Solution()
print(slt.containsPattern(arr, m, k))
