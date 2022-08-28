from typing import List


class Solution:

    def mergeInterval(self, merged, intervals, index):
        if merged[-1][1] >= intervals[index][0]:
            # use max in case it has inclusion
            merged[-1] = [merged[-1][0], max(merged[-1][1], intervals[index][1])]
        else:
            merged.append(intervals[index])

    def mergeTwoInterval(self, list1, list2):
        n1 = len(list1)
        n2 = len(list2)

        res = []
        index1 = 0
        index2 = 0

        if list1[0][0] <= list2[0][0]:
            lastInterval = list1[0]
            index1 += 1
        else:
            lastInterval = list2[0]
            index2 += 1

        res.append(lastInterval)

        while index1 < n1 and index2 < n2:
            if list1[index1][0] <= list2[index2][0]:
                self.mergeInterval(res, list1, index1)
                index1 += 1
            else:
                self.mergeInterval(res, list2, index2)
                index2 += 1

        while index1 < n1:
            self.mergeInterval(res, list1, index1)
            index1 += 1

        while index2 < n2:
            self.mergeInterval(res, list2, index2)
            index2 += 1

        return res


list1 = [[1, 2], [3, 4]]
list2 = [[4, 6], [6, 7]]
# Output: [(1,2),(3,5),(6,7)]

slt = Solution()
print(slt.mergeTwoInterval(list1, list2))