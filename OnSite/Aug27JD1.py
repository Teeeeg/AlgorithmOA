n, k = [int(x) for x in input().split()]
string = input()


def solve(string: str, n: int, k: int):
    if k > n:
        return string.upper()

    strList = list(string)

    for i in range(n):
        if i < k:
            strList[i] = strList[i].upper()
        else:
            strList[i] = strList[i].lower()

    return ''.join(strList)


res = solve(string, n, k)
print(res)
