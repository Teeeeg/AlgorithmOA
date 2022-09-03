class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1

        BASE = 131
        BUCKET = 1e9 + 7

        n = len(needle)
        needleHash = 0
        power = 1
        for i in range(n):
            digit = ord(needle[i])
            power *= BASE
            needleHash = (needleHash * BASE + digit) % BUCKET

        m = len(haystack)
        prefixHash = [0] * (m + 1)
        left = 0
        for right in range(m):
            digit = ord(haystack[right])
            prefixHash[right + 1] = (prefixHash[right] * BASE + digit)

            if right - left + 1 >= n:
                curHash = (prefixHash[right + 1] - prefixHash[left] * power + BUCKET) % BUCKET
                if curHash == needleHash and needle == haystack[left:right + 1]:
                    return left
                left += 1

        return -1


haystack = "mississippi"
needle = "issip"
slt = Solution()
print(slt.strStr(haystack, needle))
