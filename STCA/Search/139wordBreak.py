from typing import List


class Solution:

    def wordBreakCore(self, s: str, wordDict: List[str], index, maxLen, memo):
        if index == len(s):
            return True

        if memo[index] != -1:
            return memo[index]

        memo[index] = False
        for i in range(index, len(s)):
            if i - index + 1 > maxLen:
                break

            word = s[index:i + 1]
            if word not in wordDict:
                continue
            if self.wordBreakCore(s, wordDict, i + 1, maxLen, memo):
                memo[index] = True
                break

        return memo[index]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))

        memo = [-1] * len(s)
        return self.wordBreakCore(s, wordDict, 0, maxLen, memo)  # type: ignore