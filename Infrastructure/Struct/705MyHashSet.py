class MyHashSet:

    def __init__(self):
        self.hash = 1009
        self.data = [[] for _ in range(self.hash)]

    def getId(self, key):
        return key % self.hash

    def add(self, key: int) -> None:
        id = self.getId(key)
        if self.contains(key):
            return
        self.data[id].append(key)

    def remove(self, key: int) -> None:
        id = self.getId(key)
        if not self.contains(key):
            return
        self.data[id].remove(key)

    def contains(self, key: int) -> bool:
        id = self.getId(key)
        return key in self.data[id]
