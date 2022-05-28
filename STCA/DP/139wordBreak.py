from typing import List


class Solution:
    # 用动态规划做其实是一个0/1背包问题
    # s为容量
    # worDict为物品
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[i] 表示[0-i)之间是否都出现在字典中
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                if i - len(word) >= 0:
                    # 若这一段就是当前次且之前已经形成了单词
                    if s[i - len(word):i] == word and dp[i - len(word)]:
                        dp[i] = True

        return dp[-1]


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
slt = Solution()
print(slt.wordBreak(s, wordDict))