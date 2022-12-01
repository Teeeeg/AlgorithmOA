class Solution:

    def halvesAreAlike(self, s: str) -> bool:
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        word1 = s[:n // 2]
        word2 = s[n // 2:]

        count = 0
        for char in word1:
            if char in VOWELS:
                count += 1

        for char in word2:
            if char in VOWELS:
                count -= 1

        return count == 0