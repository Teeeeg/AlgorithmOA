from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if '' in strs:
            return ''

        m = len(strs)
        n = len(strs[0])

        for i in range(n):
            ch = strs[0][i]
            for j in range(1, m):
                if strs[j] != ch or i == len(strs[j]):
                    return strs[0][: i]

        return strs[0]
