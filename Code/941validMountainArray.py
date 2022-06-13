from typing import List


class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        left, right = 0, n - 1

        while left < n - 1 and arr[left] < arr[left + 1]:
            left += 1

        while right > 1 and arr[right] < arr[right - 1]:
            right -= 1

        if left != right:
            return False

        if left == right and (left == 0 or right == n - 1):
            return False

        return True


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slt = Solution()
print(slt.validMountainArray(arr))