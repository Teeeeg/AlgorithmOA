class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        if not s:
            return True

        words = s.split(' ')
        n = len(words)

        if len(pattern) != n:
            return False

        dct = {}
        visited = set()

        for i in range(n):
            word = words[i]
            p = pattern[i]

            if p not in dct:
                if word in visited:
                    return False
                visited.add(word)
                dct[p] = word

            if dct[p] != word:
                return False

        return True