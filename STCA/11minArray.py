from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1

        return numbers[left]


numbers = [1, 10, 10, 10, 10]
slt = Solution()
print(slt.minArray(numbers))
