class MyHashMap:

    def __init__(self):
        self.hash = 1009
        self.data = [[] for _ in range(self.hash)]

    def getID(self, key):
        return key % self.hash

    def put(self, key: int, value: int) -> None:
        id = self.getID(key)
        table = self.data[id]
        for kv in table:
            if kv[0] == key:
                kv[1] = value
                return
        table.append([key, value])

    def get(self, key: int) -> int:
        id = self.getID(key)
        table = self.data[id]
        for kv in table:
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        id = self.getID(key)
        table = self.data[id]
        for kv in table:
            if kv[0] == key:
                index = table.index(kv)
                table.pop(index)
                return
