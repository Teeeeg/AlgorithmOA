class StockSpanner:

    def __init__(self):
        self.monoStack = []
        self.index = 0

    def push(self, price, index):
        while self.monoStack and self.monoStack[-1][0] <= price:
            self.monoStack.pop()
        leftIndex = self.monoStack[-1][1] if self.monoStack else -1
        self.monoStack.append((price, index))

        return index - leftIndex

    def next(self, price: int) -> int:
        res = self.push(price, self.index)
        self.index += 1

        return res


ss = StockSpanner()
print(ss.next(100))
print(ss.next(80))
print(ss.next(60))
print(ss.next(70))
print(ss.next(60))
print(ss.next(75))
print(ss.next(85))