from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount2Word = {}

        for word in strs:
            charCount = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                charCount[index] += 1

            key = '#'.join([str(x) for x in charCount])

            charCount2Word[key] = charCount2Word.get(key, [])
            charCount2Word[key].append(word)

        res = []
        for value in charCount2Word.values():
            res.append(value)

        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
slt = Solution()
print(slt.groupAnagrams(strs))