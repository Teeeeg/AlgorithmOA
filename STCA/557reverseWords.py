class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i, word in enumerate(words):
            words[i] = ''.join(reversed(word))

        return ' '.join(words)


s = "Let's take LeetCode contest"
soltuion = Solution()
print(soltuion.reverseWords(s))
