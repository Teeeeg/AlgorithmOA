from collections import deque
from typing import List


class Block:

    def __init__(self, size) -> None:
        self.size = 2 * size
        self.blocks = [[] for _ in range(self.size)]

    def addToBlock(self, value):
        value += self.size
        blockId = value // self.size
        self.blocks[blockId].append(value)

    def getSmallerCount(self, value):
        value += self.size
        blockId = value // self.size
        count = 0

        for i in range(blockId):
            count += len(self.blocks[i])

        for num in self.blocks[blockId]:
            if num < value:
                count += 1

        return count


class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        block = Block(100)
        res = deque()
        n = len(nums)

        for i in range(n - 1, -1, -1):
            num = nums[i]
            block.addToBlock(num)
            count = block.getSmallerCount(num)
            res.appendleft(count)

        return list(res)


nums = [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97, 3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]
slt = Solution()
print(slt.countSmaller(nums))