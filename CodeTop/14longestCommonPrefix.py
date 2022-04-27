from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        m, n = len(strs[0]), len(strs)
        for i in range(m):
            ch = strs[0][i]
            for j in range(1, n):
                if i == len(strs[j]) or strs[j][i] != ch:
                    return strs[0][: i]

        return strs[0]


strs = ["flower", "flow", "flight"]
strs1 = ["dog", "racecar", "car"]
strs2 = ["flower", "flower", "flower", "flower"]
strs3 = ["ab", "a"]
solution = Solution()
print(solution.longestCommonPrefix(strs3))
