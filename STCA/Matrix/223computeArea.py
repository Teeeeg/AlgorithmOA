class Solution:
    # 整体面积-重叠部分

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)

        overLapWidth = min(ax2, bx2) - max(ax1, bx1)
        overLapHeight = min(ay2, by2) - max(ay1, by1)

        overLapArea = max(overLapWidth, 0) * max(overLapHeight, 0)

        return areaA + areaB - overLapArea
