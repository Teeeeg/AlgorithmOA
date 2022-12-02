from collections import defaultdict


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        char2Count1 = defaultdict(int)

        for char in word1:
            char2Count1[char] = char2Count1.get(char, 0) + 1

        char2Count2 = defaultdict(int)

        for char in word2:
            if char not in char2Count1:
                return False
            char2Count2[char] = char2Count2.get(char, 0) + 1

        chars1 = char2Count1.keys()
        chars2 = char2Count2.keys()

        chars1 = sorted(chars1)
        chars2 = sorted(chars2)

        freqs1 = char2Count1.values()
        freqs2 = char2Count2.values()

        freqs1 = sorted(freqs1)
        freqs2 = sorted(freqs2)

        return freqs1 == freqs2 and chars1 == chars2


word1 = "uau"
word2 = "ssx"
slt = Solution()
print(slt.closeStrings(word1, word2))
