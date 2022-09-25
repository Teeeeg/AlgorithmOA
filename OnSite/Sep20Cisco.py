from heapq import heappop, heappush

# n, m = map(int, input().split(' '))
# players = [int(x) for x in input().split(' ')]


class Solution:

    def choose(self, maxHeap, flag, chosen, n, m):
        orgIndex = -1
        if maxHeap:
            _, orgIndex = heappop(maxHeap)
            chosen[orgIndex] = flag

        if orgIndex == -1:
            return

        count = 0
        index = orgIndex + 1
        while count < m and index < n:
            if chosen[index] == 'C':
                chosen[index] = flag
                count += 1
            index += 1

        count = 0
        index = orgIndex - 1
        while count < m and index >= 0:
            if chosen[index] == 'C':
                chosen[index] = flag
                count += 1
            index -= 1

    def chooseTeam(self, players, n, m):
        chosen = ['C'] * n
        maxHeap = []
        for index, player in enumerate(players):
            heappush(maxHeap, (-player, index))

        count = 0
        while maxHeap:
            if chosen[maxHeap[0][1]] != 'C':
                heappop(maxHeap)
            else:
                flag = 'A' if count % 2 == 0 else 'B'
                count += 1
                self.choose(maxHeap, flag, chosen, n, m)

        return ''.join(chosen)


n = 7
m = 1
players = [3, 6, 1, 7, 2, 5, 4]
slt = Solution()
print(slt.chooseTeam(players, n, m))