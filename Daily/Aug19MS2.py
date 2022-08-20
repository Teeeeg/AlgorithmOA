def solution(S: str):
    n = len(S)
    if n == 1:
        return S

    counter = [0] * 10
    for ch in S:
        index = int(ch)
        counter[index] += 1

    palinrome = []

    for i in range(9, -1, -1):
        count = counter[i]
        if count != 0:
            if not count % 2:
                for _ in range(count // 2):
                    palinrome.append(str(i))

    for i in range(9, -1, -1):
        count = counter[i]
        if count != 0:
            if count % 2:
                for _ in range(count):
                    palinrome.append(str(i))
                break

    for i in range(10):
        count = counter[i]
        if count != 0:
            if not count % 2:
                for _ in range(count // 2):
                    palinrome.append(str(i))

    resString = ''.join(palinrome)
    if int(resString) == 0:
        return '0'

    return resString.strip('0')


S = '001000'
print(solution(S))