class Solution:

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
                return i - len(needle) + 1

        return -1


haystack = 'hello'
needle = 'll'
slt = Solution()
print(slt.strStr(haystack, needle))
