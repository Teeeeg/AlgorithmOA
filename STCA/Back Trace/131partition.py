from typing import List


class Solution:

    def isPalindrome(self, s, left, right):
        if left > right:
            return False

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True

    def partitionCore(self, s: str, res: List, path: List, startIndex):
        if startIndex >= len(s):
            res.append(path[:])
            return

        for i in range(len(s)):
            if self.isPalindrome(s, startIndex, i):
                path.append(s[startIndex:i + 1])
                self.partitionCore(s, res, path, i + 1)
                path.pop()
            else:
                continue

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.partitionCore(s, res, [], 0)
        return res


s = "aab"
slt = Solution()
print(slt.partition(s))