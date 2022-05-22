# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        peakIndex = self.findPeakIndex(mountain_arr)
        leftRes = self.binarySearch(mountain_arr, 0, peakIndex, target, True)
        rightRes = self.binarySearch(
            mountain_arr, peakIndex+1, n-1, target, False)
        if leftRes == -1 and rightRes == -1:
            return -1
        return leftRes if leftRes != -1 else rightRes

    def findPeakIndex(self, mountain_arr):
        n = mountain_arr.length()
        left, right = 0, n-1

        while left < right:
            mid = (left+right) >> 1
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                left = mid+1
            else:
                right = mid

        return left

    def binarySearch(self, arr, start, end, target, ascending):
        left, right = start, end

        while left <= right:
            mid = (left+right) >> 1
            if arr.get(mid) == target:
                return mid

            if ascending:
                if arr.get(mid) < target:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if arr.get(mid) < target:
                    right = mid-1
                else:
                    left = mid+1
        return -1
