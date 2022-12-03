from collections import defaultdict


class Solution:

    def frequencySort(self, s: str) -> str:
        char2Count = defaultdict(int)

        for char in s:
            char2Count[char] = char2Count.get(char, 0) + 1

        charCountTups = []

        for char, count in char2Count.items():
            charCountTups.append((char, count))

        charCountTups.sort(key=lambda x: x[1], reverse=True)

        res = []

        for char, count in charCountTups:
            for _ in range(count):
                res.append(char)

        return ''.join(res)


s = "cccaaa"
slt = Solution()
print(slt.frequencySort(s))