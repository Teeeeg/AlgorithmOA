from typing import List


class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        str2Count = {}
        res = []

        for i in range(n - 9):
            dnaStr = s[i:i + 10]
            if dnaStr in str2Count and str2Count[dnaStr] == 1:
                res.append(dnaStr)
            str2Count[dnaStr] = str2Count.get(dnaStr, 0) + 1

        return res


s = "AAAAAAAAAAAAA"
slt = Solution()
print(slt.findRepeatedDnaSequences(s))