from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generateParenthesisCore(0, 0, n, '', res)
        return res

    def generateParenthesisCore(self, leftCount, rightCount, n, path, res):
        # 返回的情况
        # 左右括号都满了
        if leftCount == n and rightCount == n:
            res.append(path[:])
            return

        # 当左括号还有剩下的，则可以添加左括号
        if leftCount < n:
            self.generateParenthesisCore(leftCount + 1, rightCount, n, path + '(', res)
        # 当右括号小于左括号时，可以添加右括号
        if rightCount < leftCount:
            self.generateParenthesisCore(leftCount, rightCount + 1, n, path + ')', res)


slt = Solution()
print(slt.generateParenthesis(3))