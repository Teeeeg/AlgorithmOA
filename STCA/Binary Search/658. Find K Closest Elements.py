from collections import deque
from typing import List


class Solution:

    def getPosition(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] >= x:
                right = mid
            else:
                left = mid

        if nums[left] >= x:
            return left

        if nums[right] >= x:
            return right

        return n

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()
        n = len(arr)
        pos = self.getPosition(arr, x)
        left = pos - 1
        right = pos

        while len(res) < k:
            if left >= 0 and right < n:
                if x - arr[left] <= arr[right] - x:
                    res.appendleft(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            elif left >= 0:
                res.appendleft(arr[left])
                left -= 1
            elif right < n:
                res.append(arr[right])
                right += 1

        return list(res)


arr = [1, 2, 3, 4, 5]
k = 4
x = -1
slt = Solution()
print(slt.findClosestElements(arr, k, x))