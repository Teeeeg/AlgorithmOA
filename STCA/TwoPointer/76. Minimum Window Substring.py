class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ''

        n1 = len(s)
        n2 = len(t)

        if n1 < n2:
            return ''

        tCounter = {}
        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1

        lenToMatch = n2
        count = 0
        left = 0
        maxLen = n1 + 1
        res = ''

        for right in range(n1):
            rightChar = s[right]
            if rightChar in tCounter:
                # need it
                if tCounter[rightChar] > 0:
                    count += 1
                # else over killed
                tCounter[rightChar] -= 1

            # satisfied then shrink
            while right - left + 1 >= lenToMatch and count == lenToMatch:
                # record first
                if maxLen > right - left + 1:
                    maxLen = right - left + 1
                    res = s[left:right + 1]

                leftChar = s[left]
                if leftChar in tCounter:
                    # breaking the point
                    if tCounter[leftChar] == 0:
                        count -= 1
                    tCounter[leftChar] += 1
                left += 1

        return res


s = "a"
t = "a"
slt = Solution()
print(slt.minWindow(s, t))