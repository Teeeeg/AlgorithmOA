from typing import List


class Solution:

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sums = []
        total = 0
        # 利用前缀和
        # 显然前面偏移的更加多
        for shift in reversed(shifts):
            total += shift
            sums.append(total)

        sums.reverse()
        res = list(s)

        for i in range(len(s)):
            # 与'a'的距离 与 26 取余数，最后加上'a'
            res[i] = chr((ord(s[i]) + sums[i] - ord('a')) % 26 + ord('a'))

        return ''.join(res)


s = "aaa"
shifts = [1, 2, 3]
slt = Solution()
print(slt.shiftingLetters(s, shifts))
