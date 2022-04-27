import math
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue1 = []
        queue2 = []
        queue1.append(beginWord)
        queue2.append(endWord)
        visited1 = set([beginWord])
        visited2 = set([endWord])
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        step = 1

        while queue1 and queue2:
            n1 = len(queue1)
            for _ in range(n1):
                word = queue1.pop(0)
                if word in visited2:
                    return step*2-1
                for neighbor in self.getNeighbors(word):
                    if neighbor in wordList and neighbor not in visited1:
                        queue1.append(neighbor)
                        visited1.add(neighbor)

            n2 = len(queue2)
            for _ in range(n2):
                word = queue2.pop(0)
                if word in visited1:
                    return step*2
                for neighbor in self.getNeighbors(word):
                    if neighbor in wordList and neighbor not in visited2:
                        queue2.append(neighbor)
                        visited2.add(neighbor)
            step += 1

        return 0

    def getNeighbors(self, word):
        neighbors = []
        for i, ch in enumerate(word):
            newWord = list(word)
            for ordCh in range(ord('a'), ord('z')+1):
                if ord(ch) != ordCh:
                    newWord[i] = chr(ordCh)
                    neighbors.append(''.join(newWord))

        return neighbors


beginWord = "a"
endWord = "c"
wordList = ['a', 'b', 'c']
solution = Solution()

beginWord1 = "hit"
endWord1 = "cog"
wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]

# print(solution.getNeighbors('abc'))
print(solution.ladderLength(beginWord, endWord, wordList))
print(solution.ladderLength(beginWord1, endWord1, wordList1))
