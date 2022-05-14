from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)

        for i in range(n):
            pattern = arr[i: i+m]
            if i+m < n:
                count = 1
                for j in range(i+m, n, m):
                    check = arr[j: j+m]
                    if check == pattern:
                        count += 1
                        if count == k:
                            return True
                    else:
                        break

        return False


arr = [1, 2, 1, 2, 1, 1, 1, 3]
m = 2
k = 2
s = Solution()
print(s.containsPattern(arr, m, k))
