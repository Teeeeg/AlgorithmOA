from typing import Any, List, Optional


class TrieNode:
    def __init__(self) -> None:
        # Any用于suprress报错
        self.one = Any
        self.zero = Any


class Solution:
    def __init__(self) -> None:
        self.root = TrieNode()

    def find(self, num):
        root = self.root
        res = 0
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            if bit:
                if root.zero:
                    root = root.zero
                    res = res*2 + 1
                else:
                    root = root.one
                    res = res*2
            else:
                if root.one:
                    root = root.one
                    res = res*2 + 1
                else:
                    root = root.zero
                    res = res*2

        return res

    def buildTrie(self, num):
        root = self.root
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            if bit:
                if not root.one:
                    root.one = TrieNode()
                root = root.one
            else:
                if not root.zero:
                    root.zero = TrieNode()
                root = root.zero

    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            self.buildTrie(nums[i])
            res = max(res, self.find(nums[i+1]))

        return res


# nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
nums = [2, 4]
solution = Solution()
print(solution.findMaximumXOR(nums))
