from typing import List


class Solution:

    def binarySearch(self, arr, left, right, target):
        start = left
        end = right

        while start + 1 < end:
            mid = (start + end) // 2

            if arr[mid] >= target:
                end = mid
            else:
                start = mid

        if arr[start] >= target:
            return start
        if arr[end] >= target:
            return end

        return right + 1

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1

        while 0 <= left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        while 0 < right < n and arr[right - 1] <= arr[right]:
            right -= 1

        if left >= right:
            return 0

        res = n - 1

        for i in range(left, -2, -1):
            target = arr[i]
            if i == -1:
                target = -1
            index = self.binarySearch(arr, right, n - 1, target)
            res = min(index - i - 1, res)

        return res


arr = [16, 10, 0, 3, 22, 1, 14, 7, 1, 12, 15]
slt = Solution()
print(slt.findLengthOfShortestSubarray(arr))