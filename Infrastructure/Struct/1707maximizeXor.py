from typing import Any, List


class TrieNode:
    def __init__(self) -> None:
        self.one = Any
        self.zero = Any


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def buidTrie(self, num):
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

    def checkXOR(self, num):
        root = self.root
        res = 0
        for i in reversed(range(32)):
            bit = (num >> i) & 1
            if bit:
                if root.zero:
                    res = (res << 1) + 1
                    root = root.zero
                else:
                    res <<= 1
                    root = root.one
            else:
                if root.one:
                    res = (res << 1) + 1
                    root = root.one
                else:
                    res <<= 1
                    root = root.zero
        return res


class Solution:

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        res = []
        nums.sort()
        for i in range(n):
            p, offset = queries[i][0], queries[i][1]
            trie = Trie()
            tmp = 0
            count = 0
            for num in nums:
                if num <= offset:
                    count += 1
                    trie.buidTrie(num)
                    tmp = max(tmp, trie.checkXOR(p))
            if count == 0:
                tmp = -1
            res.append(tmp)

        return res


nums = [0, 1, 2, 3, 4]
queries = [[3, 1], [1, 3], [5, 6]]
solution = Solution()
print(solution.maximizeXor(nums, queries))
