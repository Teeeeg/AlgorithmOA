from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.size = n
        self.data = [''] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        if not self.data[idKey]:
            self.data[idKey] = value

        res = []
        while self.ptr < self.size and self.data[self.ptr]:
            res.append(self.data[self.ptr])
            self.ptr += 1

        return res
