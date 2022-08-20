from typing import List

n = int(input())
cord = [[int(x) for x in input().split()] for _ in range(3)]
dist = [int(x) for x in input().split()]


def solve(cords: List[List[int]], dist: List[int], size):
    n = len(cords)
    st = set()

    for x in range(1, size + 1):
        for y in range(1, size + 1):
            flag = True
            for i in range(n):
                if abs(x - cords[i][0]) + abs(y - cords[i][1]) != dist[i]:
                    flag = False
            if flag:
                st.add((x, y))

    resList = list(st)
    resList.sort(key=lambda x: (x[0], x[1]))
    return resList[0]


res = solve(cord, dist, n)
for num in res:
    print(num, end=' ')
