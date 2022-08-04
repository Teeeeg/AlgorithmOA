from typing import List


class Solution:

    def letterCombinationsCore(self, index, path):
        if index == self.n:
            self.res.append(path)
            return

        for ch in self.dct[self.digits[index]]:
            self.letterCombinationsCore(index + 1, path + ch)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.n = len(digits)
        self.digits = digits
        self.res = []
        self.dct = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        self.letterCombinationsCore(0, '')
        return self.res


digits = '23'
slt = Solution()
print(slt.letterCombinations(digits))