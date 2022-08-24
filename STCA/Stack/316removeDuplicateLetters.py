from collections import Counter


class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        lastOccur = [0] * 26
        for i in range(len(s)):
            lastOccur[ord(s[i]) - ord('a')] = i
        for i, ch in enumerate(s):
            # if ch not exists
            if ch not in stack:
                # pop lexicographical order bigger than ch
                # and stack[-1] must have ch left in the last part
                while stack and (stack[-1] > ch and lastOccur[ord(stack[-1]) - ord('a')] > i):
                    stack.pop()
                stack.append(ch)

        return ''.join(stack)


s = "cbacdcbc"
slt = Solution()
print(slt.removeDuplicateLetters(s))