class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)

        needleHash = 0
        b = 131
        p = 10**9 + 7
        for ch in needle:
            digit = ord(ch)
            needleHash = (needleHash * b + digit) % p

        # kind of like the prefixSum
        prefixHash = [0] * (m + 1)
        powerOfB = [1] + [0] * m
        for i in range(m):
            ch = haystack[i]
            digit = ord(ch)
            prefixHash[i + 1] = (prefixHash[i] * b + digit) % p
            powerOfB[i + 1] = (powerOfB[i] * b) % p

        def calcHash(l, r):
            diff = powerOfB[r - l + 1]
            # prefixSum, get hash of [l, r]
            # prefixSum[r] - prefixSum[l-1] pivot one to right
            # 1989 - 19*100
            return (prefixHash[r + 1] - prefixHash[l] * diff + p) % p

        left = 0
        for right in range(m):
            if right - left + 1 >= n:
                if calcHash(left, right) == needleHash:
                    return left
                left += 1

        return -1


class Solution1:

    def getNext(self, needle: str):
        n = len(needle)
        next = [0] * n
        j = 0

        for i in range(1, n):
            while j > 0 and needle[i] != needle[j]:
                j = next[j - 1]
            if needle[i] == needle[j]:
                j += 1
            next[i] = j

        return next

    def strStr(self, haystack: str, needle: str) -> int:
        next = self.getNext(needle)
        j = 0

        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                # 因为最后 i 指向的是needle的最后一个字符，所以需要加1
                return i - len(needle) + 1

        return -1


haystack = "hello"
needle = "ll"
slt = Solution()
print(slt.strStr(haystack, needle))
