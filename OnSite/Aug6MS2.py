# There are N balls positioned in a row. Each of them is either red or
# white. In one move we can swap two adjacent balls. We want to
# arrange all the red balls into a consistent segment. What is the
# minimum number of swaps needed?
# Write a function:
# def solution (s)
# that, given string S of length N built from characters "R" and "W"
# representing red and white balls respectively, returns the minimum
# number of swaps needed to arrange all the red balls into a
# consistent seament. If the result exceeds 10°, return -1.
def solution(S):
    # move all R to the middle
    if not S:
        return 0

    n = len(S)
    redIndexs = []
    for i in range(n):
        if S[i] == 'R':
            redIndexs.append(i)

    if not redIndexs:
        return 0

    left = 0
    right = len(redIndexs) - 1
    res = 0

    while left < right:
        # move R to middle will swap the time of the count of W
        # count of the W can be calculated with two R's index length - the count of R
        res += (redIndexs[right] - redIndexs[left]) - (right - left)
        left += 1
        right -= 1

    return -1 if res > 10**9 else res


res = solution('WRRWWR')
print(res)
