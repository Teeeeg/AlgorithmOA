from typing import List


class Solution:

    def plusOne(self, key: str, i):
        arr = list(key)
        # 处理边界情况
        if arr[i] == '9':
            arr[i] = '0'
        else:
            arr[i] = str(int(arr[i]) + 1)

        return ''.join(arr)

    def minusOne(self, key: str, i):
        arr = list(key)
        # 处理边界情况
        if arr[i] == '0':
            arr[i] = '9'
        else:
            arr[i] = str(int(arr[i]) - 1)

        return ''.join(arr)

    def openLock(self, deadends: List[str], target: str) -> int:
        # 边界情况
        source = '0000'
        if source in deadends:
            return -1

        deads = set(deadends)
        visited = set()
        queue = [source]
        visited.add(source)
        res = 0

        while queue:
            # 这边按层遍历用于统计步数
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur == target:
                    return res
                # 四个齿轮分别拨
                for i in range(4):
                    for next in [self.minusOne(cur, i), self.plusOne(cur, i)]:
                        if next not in visited and next not in deads:
                            queue.append(next)
                            visited.add(next)
            res += 1

        return -1

    def openLock1(self, deadends: List[str], target: str) -> int:
        source = '0000'
        if source in deadends:
            return -1
        deads = set(deadends)
        visited1 = set()
        visited2 = set()
        visited1.add(source)
        visited2.add(target)

        queue1 = [source]
        queue2 = [target]
        step = 0

        while queue1 and queue2:
            for _ in range(len(queue1)):
                cur = queue1.pop(0)
                if cur in visited2:
                    return 2 * step
                for i in range(4):
                    for next in [self.minusOne(cur, i), self.plusOne(cur, i)]:
                        if next not in visited1 and next not in deads:
                            queue1.append(next)
                            visited1.add(next)

            for _ in range(len(queue2)):
                cur = queue2.pop(0)
                if cur in visited1:
                    return 2 * step + 1
                for i in range(4):
                    for next in [self.minusOne(cur, i), self.plusOne(cur, i)]:
                        if next not in visited2 and next not in deads:
                            queue2.append(next)
                            visited2.add(next)

            # 选择从窄的一边出发
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1
                visited1, visited2 = visited2, visited1

            step += 1

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
slt = Solution()
print(slt.openLock1(deadends, target))