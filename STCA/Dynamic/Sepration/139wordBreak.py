from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        opt = [False] * (n + 1)
        opt[0] = True
        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))

        for i in range(1, n + 1):
            for length in range(1, maxLen + 1):
                j = i - length

                if j < 0:
                    break

                word = s[j:i]
                if word in wordDict and opt[j]:
                    opt[i] = True
                    break

        return opt[-1]


class Solution1:
    # as 0/1 package
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        opt = [False] * (n + 1)
        opt[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                length = len(word)
                if not i >= length:
                    continue

                if s[i - length:i] == word and opt[i - length]:
                    opt[i] = True
                    break

        return opt[-1]