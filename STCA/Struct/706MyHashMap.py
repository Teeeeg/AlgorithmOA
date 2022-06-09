class MyHashMap:

    def __init__(self):
        self.hash = 1009
        self.data = [[] for _ in range(self.hash)]

    def getId(self, key):
        return key % self.hash

    def put(self, key: int, value: int) -> None:
        id = self.getId(key)
        for data in self.data[id]:
            if data[0] == key:
                data[1] = value
                return
        self.data[id].append([key, value])

    def get(self, key: int) -> int:
        id = self.getId(key)
        for data in self.data[id]:
            if data[0] == key:
                return data[1]
        return -1

    def remove(self, key: int) -> None:
        id = self.getId(key)
        for i, data in enumerate(self.data[id]):
            if data[0] == key:
                self.data[id].pop(i)
                return
