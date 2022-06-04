from typing import List


class Solution:

    def findSep(self, arr: List[int]):
        n = len(arr)
        left, right = 0, n - 1

        # 处理左右相等的情况
        while left < right and arr[left] == arr[right]:
            left += 1

        # 找到分界点，其实就是最小值
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < arr[right]:
                right = mid
            elif arr[mid] > arr[right]:
                left = mid + 1
            else:
                right -= 1

        return left

    def findleft(self, arr: List[int], left, right, target):
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                res = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return res

    def search(self, arr: List[int], target: int) -> int:
        sepIndex = self.findSep(arr)

        if arr[sepIndex] == target:
            return sepIndex
        left, right = 0, len(arr) - 1

        # 利用sepIndex 切分左右
        if arr[0] == target:
            return 0
        elif arr[0] > target:
            left = sepIndex
        else:
            right = sepIndex - 1

        # 找左边界函数
        res = self.findleft(arr, left, right, target)

        return res


arr = [1, 1, 1, 1, 1, 2, 1, 1, 1]
target = 2
slt = Solution()
print(slt.search(arr, target))