class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct = [0] * 26
        count = 0

        for ch in ransomNote:
            if dct[ord(ch)-ord('a')] == 0:
                count += 1
            dct[ord(ch)-ord('a')] += 1

        for ch in magazine:
            dct[ord(ch)-ord('a')] -= 1
            if dct[ord(ch)-ord('a')] == 0:
                count -= 1

        return True if count == 0 else False
