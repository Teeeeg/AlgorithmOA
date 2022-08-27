from collections import deque
from typing import List


class Solution:

    def binarySearch(self, arr: List[int], x: int):
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] == x:
                return mid
            if arr[mid] > x:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        res = deque()
        pivotIndex = self.binarySearch(arr, x)

        left = pivotIndex
        right = pivotIndex + 1

        while k > 0:
            if left >= 0 and right < n:
                if (x - arr[left]) <= (arr[right] - x):
                    res.appendleft(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            elif left >= 0:
                res.appendleft(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1

            k -= 1

        return list(res)


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
slt = Solution()
print(slt.findClosestElements(arr, k, x))
