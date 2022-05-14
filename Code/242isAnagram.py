class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dct = [0]*26

        for ch in s:
            dct[ord(ch)-ord('a')] += 1

        for ch in t:
            dct[ord(ch)-ord('a')] -= 1
            if dct[ord(ch)-ord('a')] < 0:
                return False

        return True


s = "anagram"
t = "axgaam"
slt = Solution()
print(slt.isAnagram(s, t))
