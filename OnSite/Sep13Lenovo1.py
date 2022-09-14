from typing import List

n, m = map(int, input().split(' '))
data = [int(x) for x in input().split(' ')]


def sovle(data: List[int]):
    sortedData = sorted(data)
    res = []

    curInterval = [sortedData[0], sortedData[0]]

    for num in sortedData:
        if num == curInterval[1] + 1 or num == curInterval[1]:
            curInterval[1] = num
        else:
            string = str(curInterval[0])
            if curInterval[0] != curInterval[1]:
                string = str(curInterval[0]) + '-' + str(curInterval[1])
            res.append(string)
            curInterval = [num, num]

    string = str(curInterval[0])
    if curInterval[0] != curInterval[1]:
        string = str(curInterval[0]) + '-' + str(curInterval[1])
    res.append(string)
    curInterval = [curInterval[0], curInterval[0]]

    return ','.join(res)


# data = [1, 2, 4, 5]
print(sovle(data))
