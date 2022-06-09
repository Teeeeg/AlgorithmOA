class HitCounter:

    def __init__(self):
        self.window = []
        self.count = 0

    def hit(self, timestamp: int) -> None:
        # 与队尾进行比较，若最后一个一样，则直接更新气次数
        if self.window and self.window[-1][0] == timestamp:
            self.window[-1] = (timestamp, self.window[-1][1] + 1)
        else:
            # 否则添加新的
            self.window.append((timestamp, 1))
        self.count += 1

    def getHits(self, timestamp: int) -> int:
        # 每次get的时候判断队头是否超过300
        while self.window and timestamp - self.window[0][0] >= 300:
            self.count -= self.window[0][1]
            self.window.pop(0)

        return self.count


hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(3)
print(hc.getHits(4))
hc.hit(300)
print(hc.getHits(300))
print(hc.getHits(301))
