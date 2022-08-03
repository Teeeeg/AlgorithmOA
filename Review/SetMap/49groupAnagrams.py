from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        res = []
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr not in dct:
                dct[sortedStr] = []
            dct[sortedStr].append(str)

        for value in dct.values():
            res.append(value)

        return res


class Solution1:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        res = []

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            key = '#'.join(([str(i) for i in count]))
            if key not in dct:
                dct[key] = []
            dct[key].append(word)

        for value in dct.values():
            res.append(value)

        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
slt = Solution1()
print(slt.groupAnagrams(strs))