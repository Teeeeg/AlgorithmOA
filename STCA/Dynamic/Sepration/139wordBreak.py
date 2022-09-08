from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        opt = [False] * (n + 1)
        opt[0] = True
        maxLen = 0
        for word in wordDict:
            maxLen = max(maxLen, len(word))

        # because str is continous and still
        # so do permutation rather than combination
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if i - j > maxLen:
                    break

                word = s[j:i]
                if word in wordDict and opt[j]:
                    opt[i] = True
                    break

        return opt[-1]


s = "leetcode"
wordDict = ["leet", "code"]
slt = Solution()
print(slt.wordBreak(s, wordDict))