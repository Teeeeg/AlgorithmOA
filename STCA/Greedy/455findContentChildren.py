from typing import List


class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(s)

        index = 0
        res = 0

        for num in g:
            while index < n:
                if num <= s[index]:
                    index += 1
                    res += 1
                    break
                else:
                    index += 1

        return res


g = [1, 2, 3]
s = [3]
slt = Solution()
print(slt.findContentChildren(g, s))
