from random import randint


def solution(blocks):
    n = len(blocks)
    res = 0

    for i in range(n):
        left = i
        right = i

        while left > 0 and blocks[left - 1] >= blocks[left]:
            left -= 1
        while right < n - 1 and blocks[right + 1] >= blocks[right]:
            right += 1

        res = max(res, right - left + 1)

    return res


def solution1(blocks):
    n = len(blocks)
    res = 0
    leftToRight = [1] * n
    rightToLeft = [1] * n

    for i in range(1, n):
        if blocks[i - 1] >= blocks[i]:
            leftToRight[i] += leftToRight[i - 1]

    for i in range(n - 2, -1, -1):
        if blocks[i] <= blocks[i + 1]:
            rightToLeft[i] += rightToLeft[i + 1]

    for i in range(n):
        cur = rightToLeft[i] + leftToRight[i] - 1
        if cur > res:
            res = cur

    return res


blocks = []
for i in range(2):
    blocks.append(randint(1, 2))
print(solution(blocks))
print(solution1(blocks))