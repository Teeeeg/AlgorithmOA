from collections import deque
from typing import List, Set


class Solution:

    def nextWords(self, curWord: str, wordList: Set[str]):
        res = []
        for word in wordList:
            count = 0
            if len(word) == len(curWord):
                for i in range(len(word)):
                    if curWord[i] != word[i]:
                        count += 1
            if count == 1:
                res.append(word)
        return res

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue1 = deque([beginWord])
        queue2 = deque([endWord])
        mapping = {beginWord: 1}

        while queue1 and queue2:
            n = len(queue1)
            for _ in range(n):
                curWord = queue1.popleft()
                path = mapping[curWord]
                if curWord == endWord:
                    return path
                nextWords = self.nextWords(curWord, wordSet)
                for word in nextWords:
                    if word not in mapping:
                        mapping[word] = path + 1
                        queue1.append(word)

        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        queue1 = deque([beginWord])
        queue2 = deque([endWord])
        visited1 = set()
        visited1.add(beginWord)
        visited2 = set()
        visited2.add(endWord)

        res = 1

        while queue1 and queue2:
            n = len(queue1)
            for _ in range(n):
                curWord = queue1.popleft()
                if curWord in visited2:
                    return res * 2 - 1
                nextWords = self.nextWords(curWord, wordSet)
                for word in nextWords:
                    if word not in visited1:
                        visited1.add(word)
                        queue1.append(word)

            n = len(queue2)
            for _ in range(n):
                curWord = queue2.popleft()
                if curWord in visited1:
                    return res * 2
                nextWords = self.nextWords(curWord, wordSet)
                for word in nextWords:
                    if word not in visited2:
                        visited2.add(word)
                        queue2.append(word)

            res += 1

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

slt = Solution()
print(slt.ladderLength1(beginWord, endWord, wordList))