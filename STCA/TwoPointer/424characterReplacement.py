class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        n = len(s)
        left = 0
        maxFreq = 0
        res = 0
        dct = {}

        for right in range(n):
            dct[s[right]] = dct.get(s[right], 0) + 1
            maxFreq = max(maxFreq, dct[s[right]])

            while left < right and right - left + 1 - maxFreq > k:
                dct[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


s = "AABABBA"
k = 1
slt = Solution()
print(slt.characterReplacement(s, k))