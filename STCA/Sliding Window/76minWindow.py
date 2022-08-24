import math


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        counter = {}
        # 表示还需要匹配几个字符
        count = len(t)

        for ch in t:
            counter[ch] = counter.get(ch, 0) + 1

        left = 0
        res = ''
        curLen = math.inf

        for right in range(n):
            rightCh = s[right]
            if rightCh in counter:
                if counter[rightCh] > 0:
                    count -= 1
                counter[rightCh] -= 1

            while count == 0:
                leftCh = s[left]
                if right - left + 1 < curLen:
                    res = s[left:right + 1]
                    curLen = right - left + 1

                if leftCh in counter:
                    if counter[leftCh] == 0:
                        count += 1
                    counter[leftCh] += 1

                left += 1

        return res


s = "bba"
t = "ba"
slt = Solution()
print(slt.minWindow(s, t))