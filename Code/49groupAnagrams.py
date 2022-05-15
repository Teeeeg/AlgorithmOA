from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}

        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord('a')] += 1
            key = tuple(count)
            if key not in dct:
                dct[key] = []
            dct[key].append(word)

        return list(dct.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))
