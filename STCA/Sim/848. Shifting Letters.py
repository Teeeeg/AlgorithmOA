from typing import List


class Solution:

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        postFix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            postFix[i] = postFix[i + 1] + shifts[i]

        res = []
        for i in range(n):
            pivot = ord(s[i]) - ord('a')
            nextPivot = (pivot + postFix[i]) % 26
            res.append(chr(ord('a') + nextPivot))

        return ''.join(res)


s = "aaa"
shifts = [1, 2, 3]
slt = Solution()
print(slt.shiftingLetters(s, shifts))