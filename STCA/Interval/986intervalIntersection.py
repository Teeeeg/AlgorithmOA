from typing import List


class Solution:

    # 类似归并排序
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList:
            return []

        if not secondList:
            return []

        firstList.sort(key=lambda x: x[0])
        secondList.sort(key=lambda x: x[0])
        n1 = len(firstList)
        n2 = len(secondList)
        i = j = 0
        res = []

        # [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])] if interval1[1] >= interval2[0] else []

        while i < n1 and j < n2:
            interval1 = firstList[i]
            interval2 = secondList[j]

            intersection = []
            # 取交集
            if interval2[0] <= interval1[1] <= interval2[1]:
                intersection = [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
            elif interval1[0] <= interval2[1] <= interval1[1]:
                intersection = [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]

            # 每次更新较短的那个
            if interval1[1] > interval2[1]:
                j += 1
            else:
                i += 1

            if intersection:
                res.append(intersection)

        return res


firstList = [[4, 6], [7, 8], [10, 17]]
secondList = [[5, 10]]
slt = Solution()
print(slt.intervalIntersection(firstList, secondList))