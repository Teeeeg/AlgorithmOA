class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dct1 = {}
        dct2 = {}
        for i in range(len(s)):
            if s[i] not in dct1:
                dct1[s[i]] = t[i]
            if t[i] not in dct2:
                dct2[t[i]] = s[i]

            if dct1[s[i]] != t[i] or dct2[t[i]] != s[i]:
                return False

        return True


s = "egg"
t = "add"
slt = Solution()
print(slt.isIsomorphic(s, t))