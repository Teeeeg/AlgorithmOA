class Solution:

    def expand(self, s, left, right):
        n = len(s)
        # 不断扩展
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        # 注意返回的应该是之前的状态
        return (left + 1, right - 1)

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        for i in range(n):
            # 注意中心扩散可以是两个s也可以是一个
            l1, r1 = self.expand(s, i, i)
            l2, r2 = self.expand(s, i, i + 1)

            if r1 - l1 > end - start:
                start = l1
                end = r1
            if r2 - l2 > end - start:
                start = l2
                end = r2

        return s[start:end + 1]


s = "babad"
slt = Solution()
print(slt.longestPalindrome(s))