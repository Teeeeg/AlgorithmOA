def solution(S: str) -> int:
    cnt = {'a': 0, 'b': 0, 'l': 0, 'n': 0, 'o': 0}
    for char in S:
        if char in cnt:
            cnt[char] += 1
    cnt['l'] //= 2
    cnt['o'] //= 2
    return min(cnt.values())
