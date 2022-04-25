def find_sum(lst, k):
    dct = {}

    for i, num in enumerate(lst):
        if k-num in dct:
            return [num, k-num]
        dct[num] = dct.get(num, 0) + i

    return []


lst = [1, 21, 3, 14, 5, 60, 7, 6]
k = 81
print(find_sum(lst, k))
