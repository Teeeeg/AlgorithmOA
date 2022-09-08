class Solution:

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        overLappedWidth = min(ax2, bx2) - max(ax1, bx1)
        overLappedHeight = min(ay2, by2) - max(ay1, by1)

        overLappedArea = max(overLappedHeight, 0) * max(overLappedWidth, 0)
        totalArea = (bx2 - bx1) * (by2 - by1) + (ax2 - ax1) * (ay2 - ay1)

        return totalArea - overLappedArea
