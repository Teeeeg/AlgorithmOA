from typing import List


class Solution:

    def getSepIndex(self, arr: List[int]):
        n = len(arr)
        left = 0
        right = n - 1

        # if arr[left] == arr[right] left ++
        while left + 1 < right and arr[left] == arr[right]:
            left += 1

        while left + 1 < right:
            mid = (left + right) // 2

            if arr[mid] < arr[right]:
                right = mid
            # if arr[mid] == arr[right] right --
            elif arr[mid] == arr[right]:
                right -= 1
            else:
                left = mid

        if arr[left] < arr[right]:
            return left

        return right

    def binarySearch(self, arr: List[int], target: int):
        if not arr:
            return -1
        n = len(arr)
        left = 0
        right = n - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if arr[mid] < target:
                left = mid
            else:
                right = mid

        if arr[left] == target:
            return left
        if arr[right] == target:
            return right

        return -1

    def search(self, arr: List[int], target: int) -> int:
        sepIndex = self.getSepIndex(arr)

        res1 = self.binarySearch(arr[:sepIndex], target)
        if res1 != -1:
            return res1

        res2 = self.binarySearch(arr[sepIndex:], target)

        return res2 + sepIndex if res2 != -1 else -1


arr = [1, 1, 1, 1, 1, 2, 1, 1, 1]
target = 2
slt = Solution()
print(slt.search(arr, target))