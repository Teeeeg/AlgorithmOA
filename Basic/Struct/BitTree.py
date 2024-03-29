class BitTree:
    # BitTree
    def __init__(self, nums) -> None:
        self.nums = nums
        self.n = len(nums)
        # sums[0] = 0
        self.bitSums = [0] * (self.n + 1)

        for i in range(self.n):
            self.add(i, nums[i])

    def lowBit(self, x):
        return x & (-x)

    def add(self, index, delta):
        # compensate the pivot index of sums
        # add one position will affect its parent node
        # update all the corresponding parent node
        index += 1
        while index <= self.n:
            self.bitSums[index] += delta
            index += self.lowBit(index)

    def get(self, index):
        return self.nums[index]

    def set(self, index, val):
        prev = self.nums[index]
        delta = val - prev
        self.add(index, delta)
        self.nums[index] = val

    def getSum(self, index):
        # sums comes with 0 ->
        # accumerate all the value of its child node
        res = 0
        while index > 0:
            res += self.bitSums[index]
            index -= self.lowBit(index)
        return res


nums = [1, 3, 5]
bitTree = BitTree(nums)
print(bitTree.getSum(3) - bitTree.getSum(0))