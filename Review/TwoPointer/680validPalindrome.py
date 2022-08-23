class Solution:

    def findDifference(self, s, left, right):
        while left <= right and s[left] == s[right]:
            left += 1
            right -= 1
        return (left, right)

    def isPalindrome(self, s, left, right):
        resL, resR = self.findDifference(s, left, right)
        return resL >= resR

    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)

        diffL, diffR = self.findDifference(s, 0, n - 1)
        return self.isPalindrome(s, diffL + 1, diffR) or self.isPalindrome(s, diffL, diffR - 1)


s = "abc"
slt = Solution()
print(slt.validPalindrome(s))