"""
This is ArrayReader's API interface.
You should not implement it, or speculate about its implementation
"""


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        start, end = 0, 1
        res = self.binarySearch(reader, start, end, target)
        while reader.get(end) <= target and res == -1:
            newStart = end+1
            end += (end-start+1)*2
            end = newStart
            res = self.binarySearch(reader, start, end, target)

        return res

    def binarySearch(self, reader: 'ArrayReader', start, end, target):
        while start <= end:
            mid = (start+end) // 2
            if reader.get(mid) == target:
                return mid
            if reader.get(mid) > target:
                end = mid-1
            else:
                start = mid+1
        return -1
