class Solution:

    def expand(self, s, left, right):
        # 从该点出发进行扩展
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        for i in range(len(s)):
            # 考虑单数情况和奇数的情况
            l1, r1 = self.expand(s, i, i)
            l2, r2 = self.expand(s, i, i + 1)

            if r1 - l1 > end - start:
                start = l1
                end = r1
            if r2 - l2 > end - start:
                start = l2
                end = r2

        return s[start:end + 1]


s = "cbbbd"
slt = Solution()
print(slt.longestPalindrome(s))