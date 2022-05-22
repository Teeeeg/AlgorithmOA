def fruits_into_baskets(fruits):
    n = len(fruits)
    dic = {}
    res = 0
    win_start = 0

    for win_end in range(n):
        right_chr = fruits[win_end]
        if right_chr not in dic:
            dic[right_chr] = 0
        dic[right_chr] += 1

        while len(dic) > 2:
            left_chr = fruits[win_start]
            dic[left_chr] -= 1
            if dic[left_chr] == 0:
                del dic[left_chr]
            win_start += 1

        res = max(res, win_end-win_start+1)

    return res


Fruit = ['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(Fruit))
