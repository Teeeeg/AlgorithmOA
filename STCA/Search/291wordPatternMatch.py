class Solution:

    def wordPatternMatchCore(self, pattern, s, dct, used):
        if not pattern:
            return not s

        ch = pattern[0]

        if ch in dct:
            word = dct[ch]
            if not s.startswith(word):
                return False
            return self.wordPatternMatchCore(pattern[1:], s[len(word):], dct, used)

        for length in range(len(s)):
            word = s[:length + 1]

            if word in used:
                continue

            used.add(word)
            dct[ch] = word
            if self.wordPatternMatchCore(pattern[1:], s[len(word):], dct, used):
                return True
            used.remove(word)
            del dct[ch]

        return False

    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.wordPatternMatchCore(pattern, s, {}, set())


pattern = "gh"
s = "i"
slt = Solution()
print(slt.wordPatternMatch(pattern, s))