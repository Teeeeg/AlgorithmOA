# 超大数组
class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1


# 定长拉链法
class MyHashMap:

    def __init__(self):
        self.map = [[-1] * 1000 for _ in range(1001)]

    def put(self, key: int, value: int) -> None:
        row, col = key//1000, key % 1000
        self.get[row][col] = value

    def get(self, key: int) -> int:
        row, col = key//1000, key % 1000
        return self.map[row][col]

    def remove(self, key: int) -> None:
        row, col = key//1000, key % 1000
        self.map[row][col] = -1


# 变长拉链法
class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hashKey = self.hash(key)
        for entry in self.table[hashKey]:
            if entry[0] == key:
                entry[1] = value
                return
        self.table[hashKey].append([key, value])

    def get(self, key: int) -> int:
        hashKey = self.hash(key)
        for entry in self.table[hashKey]:
            if entry[0] == key:
                return entry[1]
        return -1

    def remove(self, key: int) -> None:
        hashKey = self.hash(key)
        for i, entry in enumerate(self.table[hashKey]):
            if entry[0] == key:
                self.table[hashKey].pop(i)
                return
