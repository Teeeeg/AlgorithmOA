class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        charCount = {}
        left = 0
        res = 0

        for right in range(n):
            rightChar = s[right]
            charCount[rightChar] = charCount.get(rightChar, 0) + 1

            # not satisfied then make it satisfied
            while right - left + 1 >= k and len(charCount) > k:
                leftChar = s[left]

                if leftChar in charCount:
                    charCount[leftChar] -= 1
                    if charCount[leftChar] == 0:
                        del charCount[leftChar]
                left += 1
            # then record res
            res = max(res, right - left + 1)

        return res


s = "aa"
k = 1
slt = Solution()
print(slt.lengthOfLongestSubstringKDistinct(s, k))