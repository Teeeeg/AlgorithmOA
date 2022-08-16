n = int(input())
data = [[int(x) for x in input().split()] for _ in range(n)]


def solve(matrix):
    result, count = [], 0
    if len(matrix) == 0:
        return result
    m, n = len(matrix), len(matrix[0])
    i, j = 0, 0
    while count < n**2:
        up = True
        while up == True and i >= 0 and j < n:
            result.append(matrix[i][j])
            i -= 1
            j += 1
            count += 1
        # 可以往右走
        if j <= n - 1:
            i += 1
        # 不能往右,就只能往下走
        else:
            i += 2
            j -= 1
        up = False
        while up == False and i < m and j >= 0:
            result.append(matrix[i][j])
            i += 1
            j -= 1
            count += 1
        # 可以往下走
        if i <= m - 1:
            j += 1
        # 不能往下走，就只能往右
        else:
            j += 2
            i -= 1
    return result


res = solve(data)
for num in res:
    print(num, end=' ')