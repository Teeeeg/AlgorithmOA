class Solution:

    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True

        n = len(word)
        count = 0
        lastIndex = -1

        for i in range(n):
            char = word[i]
            if char.isupper():
                count += 1
                lastIndex = i

        if count == 0:
            return True

        if count == 1 and lastIndex == 0:
            return True

        if count == n:
            return True

        return False