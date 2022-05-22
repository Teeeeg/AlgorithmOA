from heapq import heappop, heappush


class Element:
    def __init__(self, number, freq, seq) -> None:
        self.number = number
        self.freq = freq
        self.seq = seq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        return self.seq > other.seq


class FrequencyStack:
    seq = 0
    maxHeap = []
    freqMap = {}

    def push(self, num):
        self.freqMap[num] = self.freqMap.get(num, 0)+1
        heappush(self.maxHeap, Element(num, self.freqMap[num], self.seq))
        self.seq += 1

    def pop(self):
        num = heappop(self.maxHeap).number
        if self.freqMap[num] > 1:
            self.freqMap[num] -= 1
        else:
            del self.freqMap[num]

        return num


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
