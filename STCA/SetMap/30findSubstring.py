from typing import Dict, List


class Solution:

    def dctIsSame(self, dct1: Dict, dct2: Dict):
        if len(dct1) != len(dct2):
            return False

        for key, value in dct1.items():
            if key not in dct2:
                return False
            if value != dct2[key]:
                return False

        return True

    def getDct(self, part: str):
        dct = {}
        n = len(part)

        for i in range(0, n, self.partLen):
            word = part[i:i + self.partLen]
            dct[word] = dct.get(word, 0) + 1

        return dct

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.partLen = len(words[0])
        n = len(s)
        totalLen = len(words) * self.partLen
        res = []
        dct = self.getDct(''.join(words))

        for i in range(0, n - totalLen + 1):
            part = s[i:i + totalLen]
            dct1 = self.getDct(part)
            if self.dctIsSame(dct1, dct):
                res.append(i)

        return res