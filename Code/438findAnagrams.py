from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dct = {}
        res = []

        for ch in p:
            dct[ch] = dct.get(ch, 0)+1

        left = 0
        count = len(dct)

        for right in range(len(s)):
            if s[right] in dct:
                dct[s[right]] -= 1
                if dct[s[right]] == 0:
                    count -= 1

            if right-left+1 >= len(p):
                if count == 0:
                    res.append(left)
                ch = s[left]
                if ch in dct:
                    if dct[ch] == 0:
                        count += 1
                    dct[ch] += 1
                left += 1

        return res


s = "cbaebabacd"
p = "abc"
slt = Solution()
print(slt.findAnagrams(s, p))
