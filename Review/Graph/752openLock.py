from typing import List


class Solution:

    def plusOne(self, key: str, i):
        arr = list(key)
        if arr[i] == '9':
            arr[i] = '0'
        else:
            arr[i] = str(int(arr[i]) + 1)

        return ''.join(arr)

    def minusOne(self, key: str, i):
        arr = list(key)
        if arr[i] == '0':
            arr[i] = '9'
        else:
            arr[i] = str(int(arr[i]) - 1)

        return ''.join(arr)

    def getKeys(self, key: str, n):
        res = []
        for i in range(n):
            res.append(self.plusOne(key, i))
            res.append(self.minusOne(key, i))

        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        visited1 = set(['0000'])
        visited2 = set([target])
        queue1 = ['0000']
        queue2 = [target]
        res = 0

        while queue1 and queue2:
            n1 = len(queue1)
            for _ in range(n1):
                cur = queue1.pop(0)
                if cur in visited2:
                    return res * 2
                keys = self.getKeys(cur, len(cur))
                for key in keys:
                    if key not in visited1 and key not in deadends:
                        queue1.append(key)
                        visited1.add(key)

            n = len(queue2)
            for _ in range(n):
                cur = queue2.pop(0)
                if cur in visited1:
                    return res * 2 + 1
                keys = self.getKeys(cur, len(cur))
                for key in keys:
                    if key not in visited2 and key not in deadends:
                        queue2.append(key)
                        visited2.add(key)

            # if len(queue1) > len(queue2):
            #     queue1, queue2 = queue2, queue1
            #     visited1, visited2 = visited2, visited1
            res += 1

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

slt = Solution()
print(slt.openLock(deadends, target))