from collections import deque
from typing import List


class Solution:

    def getNeighbors(self, word, steps):
        word = list(word)
        n = len(word)
        neighbors = []
        for i in range(n):
            orgCh = word[i]
            for offset in range(26):
                newCh = chr(offset + ord('a'))
                if newCh == orgCh:
                    continue
                word[i] = newCh
                newWord = ''.join(word)
                if newWord in self.wordSet and newWord not in steps:
                    neighbors.append(newWord)
            word[i] = orgCh

        return neighbors

    def bfs(self, queue, steps, otherSteps):

        for _ in range(len(queue)):
            curWord = queue.popleft()
            step = steps[curWord]
            for neighbor in self.getNeighbors(curWord, steps):
                if neighbor in otherSteps:
                    return step + otherSteps[neighbor]
                steps[neighbor] = step + 1
                queue.append(neighbor)

        return -1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        self.wordSet = set(wordList)
        steps = {beginWord: 1}
        steps1 = {endWord: 1}

        queue = deque([beginWord])
        queue1 = deque([endWord])

        while queue or queue1:
            res = self.bfs(queue, steps, steps1)
            if res != -1:
                return res
            res = self.bfs(queue1, steps1, steps)
            if res != -1:
                return res

        return 0


beginWord = "hbo"
endWord = "qbx"
wordList = ["abo", "hco", "hbw", "ado", "abq", "hcd", "hcj", "hww", "qbq", "qby", "qbz", "qbx", "qbw"]
slt = Solution()
print(slt.ladderLength(beginWord, endWord, wordList))
