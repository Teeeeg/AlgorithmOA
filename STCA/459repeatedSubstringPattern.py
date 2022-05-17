class Solution:

    def getNext(self, s):
        n = len(s)
        next = [0] * n
        j = 0

        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

        return next


# 数组长度减去最长相同前后缀的长度相当于是第一个周期的长度

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        next = self.getNext(s)

        if next[-1] != 0 and n % (n - next[-1]) == 0:
            return True
        return False

s = 'abcabcabc'
slt = Solution()
print(slt.repeatedSubstringPattern(s))