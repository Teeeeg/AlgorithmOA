import random


class RandomizedSet:

    def __init__(self):
        self.val2index = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.val2index:
            self.val2index[val] = len(self.data)
            self.data.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.val2index:
            lastVal = self.data[-1]
            index = self.val2index[val]
            self.data[index], self.data[-1] = self.data[-1], self.data[index]
            self.val2index[lastVal] = index
            self.data.pop()
            self.val2index.pop(val)
            return True

        return False

    def getRandom(self) -> int:
        index = random.randint(0, len(self.data) - 1)
        return self.data[index]


rs = RandomizedSet()
rs.remove(0)
rs.remove(0)
rs.insert(0)
print(rs.getRandom())
rs.remove(0)
rs.insert(0)