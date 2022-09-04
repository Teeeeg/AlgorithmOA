from typing import List

n, m, k = input().split(' ')
n = int(n)
m = int(m)
k = int(k)

nums = [int(x) for x in input().split(' ')]


def solve(n: int, m: int, k: int, nums: List[int]):
    if k <= n:
        return nums[k - 1]

    mod = k % n
    index = mod - 1

    if mod % 2 == 0:
        return nums[index]
    return nums[-1 - index]


print(solve(n, m, k, nums))
