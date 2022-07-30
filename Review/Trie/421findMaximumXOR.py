from typing import Any, List


class TrieNode:

    def __init__(self) -> None:
        self.children = [Any] * 2


class Solution:

    def __init__(self) -> None:
        self.root = TrieNode()

    def buildTrie(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def findMaximumXORCore(self, num):
        node = self.root
        res = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.children[1 - bit]:
                res = res * 2 + 1
                node = node.children[1 - bit]
            else:
                res = res * 2
                node = node.children[bit]

        return res

    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            self.buildTrie(num)
            res = max(res, self.findMaximumXORCore(num))

        return res


nums = [3, 10, 5, 25, 2, 8]
slt = Solution()
print(slt.findMaximumXOR(nums))