from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue1 = ['0000']
        queue2 = [target]
        visited1 = set(['0000'])
        visited2 = set(target)
        step = 0

        if '0000' == target:
            return 0

        if '0000' in deadends:
            return -1

        while queue1 and queue2:
            # queue = queue1 if len(queue1) < len(queue2) else queue2
            n1 = len(queue1)
            for _ in range(n1):
                key = queue1.pop(0)
                if key in visited2:
                    return step*2
                neighbors = self.getNeighbors(key)
                for neighbor in neighbors:
                    if neighbor not in deadends and neighbor not in visited1:
                        queue1.append(neighbor)
                        visited1.add(neighbor)

            n2 = len(queue2)
            for _ in range(n2):
                key = queue2.pop(0)
                if key in visited1:
                    return step*2+1
                neighbors = self.getNeighbors(key)
                for neighbor in neighbors:
                    if neighbor not in deadends and neighbor not in visited2:
                        queue2.append(neighbor)
                        visited2.add(neighbor)
            step += 1
        return -1

    def getNeighbors(self, word: str):
        neighbors = []
        word = list(word)
        for i in range(len(word)):
            old_ord = ord(word[i])
            new_ord = ord('0') if old_ord+1 > ord('9') else old_ord+1
            word[i] = chr(new_ord)
            neighbors.append(''.join(word))
            word[i] = chr(old_ord)

            old_ord = ord(word[i])
            new_ord = ord('9') if old_ord-1 < ord('0') else old_ord-1
            word[i] = chr(new_ord)
            neighbors.append(''.join(word))
            word[i] = chr(old_ord)
        return neighbors


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"


deadends1 = ["8888"]
target1 = "0009"
solution = Solution()
print(solution.openLock(deadends, target))
