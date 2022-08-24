from typing import List


class Solution:

    def generateParenthesisCore(self, n, leftCount, rightCount, path):
        if leftCount == rightCount == n:
            self.res.append(path)

        if leftCount < n:
            self.generateParenthesisCore(n, leftCount + 1, rightCount, path + '(')

        if n >= leftCount > rightCount:
            self.generateParenthesisCore(n, leftCount, rightCount + 1, path + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.generateParenthesisCore(n, 0, 0, '')
        return self.res